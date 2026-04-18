#!/bin/bash
# Download subtitles from a YouTube video.
# Usage: ./download_subtitles.sh <YouTube_URL> [output_dir]
# Prefers human subtitles; falls back to auto-generated if none.
# Language preference: Chinese > English > others.

set -e

URL="$1"
OUTPUT_DIR="${2:-.}"

if [ -z "$URL" ]; then
    echo "Usage: ./download_subtitles.sh <YouTube_URL> [output_dir]"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo ">>> Checking available subtitles..."
yt-dlp --list-subs --no-download "$URL" 2>/dev/null | tail -20

echo ""
echo ">>> Trying human subtitles (Chinese first)..."

# Attempt 1: human Chinese subtitles
if yt-dlp --write-subs --sub-langs "zh-Hans,zh-Hant,zh,zh-CN,zh-TW" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -newer /tmp/.ytdlp_marker 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then
        echo "OK Downloaded: $FOUND"
        exit 0
    fi
fi

# Attempt 2: human English subtitles
echo ">>> No human Chinese subs. Trying English..."
if yt-dlp --write-subs --sub-langs "en,en-US,en-GB" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -mmin -1 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then
        echo "OK Downloaded: $FOUND"
        exit 0
    fi
fi

# Attempt 3: auto-generated (Chinese first)
echo ">>> No human subs. Trying auto-generated..."
if yt-dlp --write-auto-subs --sub-langs "zh-Hans,zh,en" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -o -name "*.vtt" 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then
        echo "OK Auto subs downloaded: $FOUND"
        exit 0
    fi
fi

echo "ERR No usable subtitles found"
exit 1
