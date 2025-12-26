def analyze_text(text: str) -> tuple[int, int, int]:
    lines = text.count('\n') + (1 if text else 0)
    words = len(text.split())
    chars = len(text.replace(" ", "").replace("\n", ""))

    return lines, words, chars

def main() -> None:
    path = input("Enter a file path:").strip()

    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found")
        return
    except Exception as e:
        print(f"Counld not read file: {e}")
        return
    
    lines, words, chars = analyze_text(content)

    report = (
        f"Report for: {path}\n"
        f"Lines: {lines}\n"
        f"Words: {words}\n"
        f"Characters (excluding spaces and newlines): {chars}\n"
    )

    print("\n" + report)

    out_path = "report.txt"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Saved report to {out_path}")

if __name__ == "__main__":
    main()