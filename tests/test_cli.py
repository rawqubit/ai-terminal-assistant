"""Tests for ai-terminal-assistant."""
import sys
import os
import subprocess
import pytest


def run(*args):
    env = os.environ.copy()
    env.setdefault('OPENAI_API_KEY', 'sk-dummy')
    return subprocess.run(
        [sys.executable, "main.py"] + list(args),
        capture_output=True, text=True, env=env
    )


def test_root_help():
    r = run("--help")
    assert r.returncode == 0
    assert len(r.stdout) > 0

def test_ask_help():
    r = run("ask", "--help")
    assert r.returncode == 0

def test_debug_help():
    r = run("debug", "--help")
    assert r.returncode == 0

def test_module_compiles():
    r = subprocess.run(
        [sys.executable, "-m", "py_compile", "main.py"],
        capture_output=True, text=True
    )
    assert r.returncode == 0, r.stderr
