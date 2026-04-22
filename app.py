def greet(name: str) -> str:
    """Retourne un message de bienvenue."""
    if not name:
        raise ValueError("Le nom ne peut pas être vide")
    return f"Hello, {name}! Pipeline is active 🚀"


def add(a: int, b: int) -> int:
    """Additionne deux nombres."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Multiplie deux nombres."""
    return a * b


def subtract(a: int, b: int) -> int:
    """Soustrait b de a."""
    return a - b


if __name__ == "__main__":
    print(greet("DevOps"))
    print(f"2 + 3 = {add(2, 3)}")
