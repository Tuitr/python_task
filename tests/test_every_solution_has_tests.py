from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_every_solution_has_tests():
    solutions = [
        p.stem for p in (ROOT / "problems").glob("*.py") if p.stem != "__init__"
    ]
    missing = [
        name for name in solutions if not (ROOT / "tests" / f"test_{name}.py").exists()
    ]
    assert not missing, f"Нет тестов для: {missing}"
