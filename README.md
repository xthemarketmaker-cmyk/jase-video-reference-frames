# Jase Video Reference Frames

Automated last-frame hosting for consistent AI video generation.

Hosted on **Netlify** with Git backup.

## Stable Public URL (use this in video tools)
https://jase-video-frames.netlify.app/last-frame.jpg

## How it works
Run the updater script with the path to your actual last scene frame.

The script:
1. Copies the real last frame as `last-frame.jpg`
2. Commits + pushes to GitHub (history/backup)
3. Deploys to Netlify (live hosting)

The URL above always serves the **actual last frame** — no text descriptions.

## Update command (automated)
```bash
python "C:\Users\Hardcore\jase-frame-host\update_last_frame.py" "C:\path\to\your\last-scene-frame.jpg"
```

Example:
```bash
python "C:\Users\Hardcore\jase-frame-host\update_last_frame.py" "C:\Users\Hardcore\Videos\TheLastLight\scene_01_last.jpg"
```

## One-time setup done
- Netlify site created and linked: jase-video-frames
- Update script enhanced to deploy directly to Netlify

This gives you fully automated, actual-image last-frame chaining.