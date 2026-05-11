# Im sorry I had AI write these tests 😓

# Standard Library
from project import add_basic_configurations, progress_hook
import os
import json
import pytest
import tempfile
from unittest.mock import patch, MagicMock

# Local
from history import add_to_history, load_history, save_history


# ─── History Tests ────────────────────────────────────────────────────────────

def test_load_history_missing_file():
    """load_history returns an empty list when the file doesn't exist."""
    assert load_history("nonexistent_file.json") == []


def test_load_history_empty_file():
    """load_history returns an empty list when the file exists but is empty."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name  # write nothing — empty file

    try:
        assert load_history(temp_path) == []
    finally:
        os.remove(temp_path)


def test_save_and_load_history():
    """Data saved with save_history can be read back correctly with load_history."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name

    try:
        data = [{"url": "https://example.com",
                 "title": "Test", "date": "2024-01-01 00:00-00"}]
        save_history(data, temp_path)
        assert load_history(temp_path) == data
    finally:
        os.remove(temp_path)


def test_add_to_history_creates_entry():
    """add_to_history appends a new entry with url and title to the history file."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name

    try:
        add_to_history("https://youtube.com/watch?v=123",
                       "My Video", temp_path)
        history = load_history(temp_path)

        assert len(history) == 1
        assert history[0]["url"] == "https://youtube.com/watch?v=123"
        assert history[0]["title"] == "My Video"
        assert "date" in history[0]
    finally:
        os.remove(temp_path)


def test_add_to_history_appends():
    """add_to_history appends to existing entries rather than overwriting them."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name

    try:
        add_to_history("https://youtube.com/watch?v=1", "Video 1", temp_path)
        add_to_history("https://youtube.com/watch?v=2", "Video 2", temp_path)
        history = load_history(temp_path)

        assert len(history) == 2
        assert history[0]["title"] == "Video 1"
        assert history[1]["title"] == "Video 2"
    finally:
        os.remove(temp_path)


# ─── add_basic_configurations Tests ──────────────────────────────────────────


def test_add_basic_configurations_keys():
    """add_basic_configurations adds all required keys to the opts dict."""
    opts = {}
    add_basic_configurations(opts, "downloads/video")

    assert opts["quiet"] is True
    assert opts["no_warnings"] is True
    assert opts["progress_hooks"] == [progress_hook]
    assert "outtmpl" in opts


def test_add_basic_configurations_outtmpl():
    """add_basic_configurations sets outtmpl to the correct folder path."""
    opts = {}
    folder = os.path.join("downloads", "audio")
    add_basic_configurations(opts, folder)

    expected = os.path.join(folder, "%(title)s.%(ext)s")
    assert opts["outtmpl"] == expected


def test_add_basic_configurations_does_not_overwrite_existing_keys():
    """add_basic_configurations doesn't touch keys already in opts like format."""
    opts = {"format": "bestaudio/best"}
    add_basic_configurations(opts, "downloads/audio")

    assert opts["format"] == "bestaudio/best"
