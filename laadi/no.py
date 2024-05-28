from rich.console import Console

console = Console()

account = {"num": 123456}

console.print(f'{account["num"]} start {"=" * 70}', style='white')
