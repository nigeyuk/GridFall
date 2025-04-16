import os

# Root content path.
BASE_PATH = os.path.join(os.getcwd(), "Content")

# Define folder structure.
FOLDERS = [
    "../Build",
    "../Tools",
    "../External",
    "Core/Materials",
    "Core/Functions",
    "Core/Interfaces",
    "Core/Utilities",

    "Game/GameModes/Survival",
    "Game/GameModes/Evacuation",
    "Game/GameModes/Sabotage",

    "Game/Characters/Player/Animations",
    "Game/Characters/Player/Blueprints",
    "Game/Characters/Player/Meshes",

    "Game/Characters/Enemy/AI",
    "Game/Characters/Enemy/Animations",
    "Game/Characters/Enemy/Blueprints",
    "Game/Characters/Enemy/SFX",

    "Game/Items/HidingProps",
    "Game/Items/Pickups",
    "Game/Items/Interactables",

    "Game/Mechanics/TimerSystem",
    "Game/Mechanics/HidingSystem",
    "Game/Mechanics/DetectionSystem",
    "Game/Mechanics/Objectives",

    "Game/Controllers/AI",
    "Game/Controllers/Player",

    "Levels/Map_CityPark",
    "Levels/Map_UndergroundLab",
    "Levels/Map_Mansion",
    "Levels/Map_Shipyard",
    "Levels/Map_MountainCabin",
    "Levels/Map_FactoryRuins",

    "UI/HUD",
    "UI/Menus",
    "UI/Widgets",
    "UI/Icons",

    "FX/Niagara",
    "FX/Materials",
    "FX/Footsteps",
    "FX/Alerts",

    "Audio/Music",
    "Audio/SFX/Ambience",
    "Audio/SFX/Enemy",
    "Audio/SFX/UI",
    "Audio/SFX/Movement",
    "Audio/Dialogue",

    "Animations/Player",
    "Animations/Enemy",
    "Animations/Shared",

    "Blueprints/BaseClasses",
    "Blueprints/Components",
    "Blueprints/GameFlow",
    "Blueprints/DevTools",

    "Cinematics/Intros",
    "Cinematics/Outros",
    "Cinematics/Cameras",
]

def create_folders(base_path, folders):
    print(f"Creating folders in: {base_path}\n")
    for folder in folders:
        full_path = os.path.join(base_path, folder)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"✅ Created: {folder}")
        else:
            print(f"⏭️ Skipped (already exists): {folder}")

if __name__ == "__main__":
    if not os.path.exists(BASE_PATH):
        print(f"ERROR: The expected Content directory does not exist at: {BASE_PATH}")
    else:
        create_folders(BASE_PATH, FOLDERS)
