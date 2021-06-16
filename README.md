# cdn-game-launcher

A game launcher (only javascript for the moment)

## Installation and Deployment

Copy the .env.example file to .env and modify it as you want:

```bash
cp .env.example .env
```

Build:

```bash
docker-compose build
```

Deploy:

```bash
docker-compose up -d
```

## How to add games

1. Open Minio instance (localhost:10501 by default)

2. Select the bucket `javascript-games` and add a new folder with the name of your game.

3. Click on the upload files button or drag and drop your game files into the new folder.

Games need to contains specific files to be valid:

- `index.html`: the main html file launched by game launcher.
