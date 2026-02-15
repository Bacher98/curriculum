import traceback


class AutonomousCodingAgentPro:
    def __init__(self, variant="erläuternd"):
        self.variant = variant.lower()
        self.default_assumptions = {"language": "Python 3", "stack": "Standard Library"}

    def analyze_task(self, task_description):
        print("=== Schritt 1: Problemverständnis ===")
        print(f"Aufgabe: {task_description}")
        print(f"Default-Annahmen: {self.default_assumptions}")

    def select_strategy(self, task_description):
        print("\n=== Schritt 2: Lösungsansatz & Architektur ===")
        task_lower = task_description.lower()
        if "summe" in task_lower or "summ" in task_lower:
            return "sum_list"
        if "umkehren" in task_lower or "umkehr" in task_lower or "reverse" in task_lower:
            return "reverse_list"
        if "max" in task_lower:
            return "max_list"
        return "generic"

    def implement_solution(self, strategy):
        print("\n=== Schritt 3: Implementierung ===")
        code_templates = {
            "sum_list": """
def solution(numbers):
    if not isinstance(numbers, list):
        raise ValueError(\"Input muss eine Liste sein\")
    return sum(numbers)
""",
            "reverse_list": """
def solution(lst):
    if not isinstance(lst, list):
        raise ValueError(\"Input muss eine Liste sein\")
    return lst[::-1]
""",
            "max_list": """
def solution(numbers):
    if not isinstance(numbers, list):
        raise ValueError(\"Input muss eine Liste sein\")
    return max(numbers) if numbers else None
""",
            "generic": """
def solution(input_data):
    # Platzhalter für generische Aufgaben
    return input_data
""",
        }
        code = code_templates.get(strategy, code_templates["generic"])
        print(code)
        try:
            local_vars = {}
            exec(code, globals(), local_vars)
            self.solution_func = local_vars.get("solution")
        except Exception:
            print("Fehler bei der Implementierung:")
            traceback.print_exc()
            self.solution_func = None

    def run_tests(self, strategy):
        print("\n=== Schritt 4: Tests / Edge-Cases ===")
        if not hasattr(self, "solution_func") or self.solution_func is None:
            print("Keine Lösung zum Testen verfügbar.")
            return

        if strategy == "sum_list":
            test_cases = [
                {"input": [1, 2, 3], "expected": 6},
                {"input": [], "expected": 0},
                {"input": [-1, -2, -3], "expected": -6},
            ]
        elif strategy == "reverse_list":
            test_cases = [
                {"input": [1, 2, 3], "expected": [3, 2, 1]},
                {"input": [], "expected": []},
            ]
        elif strategy == "max_list":
            test_cases = [
                {"input": [1, 5, 3], "expected": 5},
                {"input": [], "expected": None},
            ]
        else:
            test_cases = [{"input": 42, "expected": 42}]

        for i, test in enumerate(test_cases):
            try:
                result = self.solution_func(test["input"])
                status = "OK" if result == test["expected"] else "FEHLER"
                print(
                    f"Test {i + 1}: Input={test['input']}, Output={result}, "
                    f"Erwartet={test['expected']} -> {status}"
                )
            except Exception as exc:
                print(f"Test {i + 1} Exception: {exc}")

    def review(self):
        print("\n=== Schritt 5: Review & mögliche Verbesserungen ===")
        print("Code modular, wartbar, Edge-Cases getestet.")
        print(
            "Mögliche Verbesserungen: Typprüfung, Dokumentation, "
            "Performance für große Daten, Exceptions abfangen."
        )

    def run(self, task_description):
        self.analyze_task(task_description)
        strategy = self.select_strategy(task_description)
        self.implement_solution(strategy)
        self.run_tests(strategy)
        self.review()


if __name__ == "__main__":
    agent = AutonomousCodingAgentPro(variant="erläuternd")
    tasks = [
        "Schreibe eine Funktion, die eine Liste von Zahlen summiert.",
        "Schreibe eine Funktion, die eine Liste umkehrt.",
        "Schreibe eine Funktion, die das Maximum einer Liste findet.",
    ]
    for task in tasks:
        print("\n" + "=" * 60 + "\n")
        agent.run(task)
