from redteam.injection_tests import run_injection_tests
from evaluation.safety_score import calculate_score
from rich import print


def main():
    print("\n[bold cyan]ClaudeGuardian Safety Test[/bold cyan]\n")

    results = run_injection_tests()

    score = calculate_score(results)

    for r in results:
        print(f"Prompt: {r['prompt']}")
        print(f"Response: {r['response']}")
        print(f"Safe: {r['safe']}\n")

    print(f"[bold green]Overall Safety Score: {score}/10[/bold green]")


if __name__ == "__main__":
    main()
