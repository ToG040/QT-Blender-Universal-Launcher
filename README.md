# QT Blender Universal Launcher

A universal 3D file launcher for Blender that makes opening external 3D assets feel more like a traditional DCC application.

Instead of opening Blender first and manually importing files, simply double-click a supported 3D file and the launcher will automatically start Blender and import the asset.

Inspired by workflows from applications like Cinema 4D, this tool provides a faster asset-opening workflow while keeping Blender's flexibility and scripting power.

---

## Features

- Open 3D files directly from Windows Explorer
- Automatically detects file extensions
- Launches Blender and imports the correct format
- No command prompt window
- Works as a Windows file association handler
- Blender-style workflow for external assets
- Lightweight standalone executable

---

## Supported Formats

Currently supported:

| Format | Extension |
|---|---|
| Autodesk FBX | `.fbx` |
| Wavefront OBJ | `.obj` |
| STL | `.stl` |
| glTF | `.gltf` |
| Binary glTF | `.glb` |
| Collada | `.dae` |
| Polygon File Format | `.ply` |
| Alembic | `.abc` |

More formats may be added in future releases.

---

# How It Works

```
Double-click 3D file
        ↓
QT Universal Launcher
        ↓
Detect file extension
        ↓
Start Blender
        ↓
Import asset automatically
```

Example:

```
Tree.fbx
   ↓
_QT_Universal_Launcher.exe
   ↓
Blender
   ↓
Imported Tree model
```

---

# Installation

## 1. Download

Download the latest release:

```
_QT_Universal_Launcher.exe
```

---

## 2. Place the Launcher

Place the executable inside your Blender installation folder.

Example:

```
C:\Program Files\Blender Foundation\Blender 5.2\
```

Your folder should look similar to:

```
Blender 5.2
│
├── blender.exe
├── _QT_Universal_Launcher.exe
└── ...
```

This allows the launcher to find your Blender installation.

---

## 3. Set File Associations

For each 3D format you want to open automatically:

1. Right-click your desired 3D file.

Example:

```
model.fbx
```

2. Select:

```
Properties
```

3. Under:

```
Opens with
```

click:

```
Change...
```

4. Select:

```
_QT_Universal_Launcher.exe
```

5. Enable:

```
Always use this app to open this file type
```

Repeat this process for other supported formats:

```
.fbx
.obj
.stl
.gltf
.glb
.dae
.ply
.abc
```

---

# Requirements

- Windows
- Blender 5.x installed

---

# Usage

After installation:

```
Double-click model.fbx
```

Blender will automatically open and import the file.

No need to:

```
Open Blender
        ↓
File
        ↓
Import
        ↓
Select format
        ↓
Browse file
```

---

# Why?

Blender normally opens `.blend` files directly, while other formats require manual importing.

This launcher adds a more Cinema 4D-like workflow where external 3D assets can be opened directly from Windows Explorer.

---

# Building From Source

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --windowed --icon=blender.ico _QT_Universal_Launcher.py
```

The executable will be created inside:

```
dist/
```

---

# Customization

The Blender installation path is defined inside:

```
_QT_Universal_Launcher.py
```

Example:

```python
BLENDER = r"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"
```

Change this path if your Blender installation is located somewhere else.

---

# License

MIT License

You are free to use, modify, and distribute this project.

---

# Credits

Created by **ToG**

Part of the QT Blender workflow tools collection.
