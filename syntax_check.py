import ast


def check_syntax(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()

        # Try to parse the file
        ast.parse(source)
        print(f"✅ {filename}: Syntax is valid!")
        return True

    except SyntaxError as e:
        print(f"❌ {filename}: Syntax error at line {e.lineno}: {e.msg}")
        return False
    except Exception as e:
        print(f"❌ {filename}: Error reading file: {e}")
        return False


if __name__ == "__main__":
    check_syntax("app_combined_final.py")
