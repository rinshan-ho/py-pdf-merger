@echo off
title py-pdf-merger
call .\.venv\scripts\activate
python main.py %*

pause