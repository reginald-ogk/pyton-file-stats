from pathlib import Path



def analyze_text(text: str) -> tuple[int, int, int]:
    lines = text.count('\n') + (1 if text else 0)
    words = len(text.split())
    no_spaces = text.replace(" ", "").replace("\n", "")
    chars = len(no_spaces)
    return lines, words, chars

def analyze_file(path: Path) -> tuple[int, int, int]:
    try:
        text = path.read_text(encoding='utf-8', errors='ignore')

    except Exception as e:
        print(f"Skipped {path.name}, error: {e}")
        return 0, 0, 0
    return analyze_text(text)

def analyze_folder(folder: Path, ext: str) -> None:
    if not folder.is_dir():
        print("Invalid folder path.")
        return

    total_lines = 0
    total_words = 0
    total_chars = 0
    file_count = 0

    for path in folder.iterdir():
        if path.is_file() and path.suffix.lower() == ext:
            file_count += 1
            lines, words, chars = analyze_file(path)
            
            print(f"\nProcessing file: {path.name}")
            print(f"Lines: {lines}")
            print(f"Words: {words}")
            print(f"Characters: {chars}")

            total_lines += lines
            total_words += words
            total_chars += chars

    print("\nTOTAL SUMMARY")
    print(f"Files processed: {file_count}")
    print(f"Total lines: {total_lines}")
    print(f"Total words: {total_words}")
    print(f"Total characters: {total_chars}")

def main() -> None:
    folder_input = input("Enter the folder path: ").strip()
    ext_input = input("Enter the extension (.txt or .py): ").strip()
    analyze_folder(Path(folder_input), ext='.txt')

if __name__ == "__main__":
    main()