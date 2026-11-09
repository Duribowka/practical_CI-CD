import subprocess


result = subprocess.run(
    ["python", "calculator.py"],
    capture_output=True,
    text=True
)

assert result.returncode == 0

assert "Addition: 15" in result.stdout
assert "Subtraction: 5" in result.stdout
assert "Multiplication: 50" in result.stdout
assert "Division: 2.0" in result.stdout

print("Integration tests passed!")