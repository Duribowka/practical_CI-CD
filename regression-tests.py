import subprocess

result = subprocess.run(
    ["python", "calculator.py"],
    capture_output=True,
    text=True
)

assert result.returncode == 0

expected_output = [
    "Addition: 15",
    "Subtraction: 5",
    "Multiplication: 50",
    "Division: 2.0"
]

for line in expected_output:
    assert line in result.stdout

print("Regression tests passed!")