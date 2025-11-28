import shutil
import os

def zip_project():
    source_dir = "c:/Users/Harshavardhana Gowda/OneDrive/Desktop/speech/intelligent_speech_engine"
    output_filename = "c:/Users/Harshavardhana Gowda/OneDrive/Desktop/speech/intelligent_speech_engine_v1"
    
    # Create a temporary directory to exclude venv and node_modules if needed, 
    # but for a "complete" offline package, we might want to include them?
    # Usually node_modules and venv are not portable. 
    # The user asked for "Auto-install all dependencies", so the setup script handles that.
    # So we should exclude venv and node_modules to keep zip size small.
    
    def ignore_patterns(path, names):
        return [n for n in names if n in ['venv', 'node_modules', '__pycache__', '.git']]

    print(f"Zipping project to {output_filename}.zip...")
    shutil.make_archive(output_filename, 'zip', source_dir)
    print("Done!")

if __name__ == "__main__":
    zip_project()
