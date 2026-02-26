import os
import sys
import click
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
# Ensure OPENAI_API_KEY is set in your environment
client = OpenAI()
console = Console()

@click.group()
def cli():
    """AI-Powered Terminal Assistant: Your AI companion in the CLI."""
    pass

@cli.command()
@click.argument('query', nargs=-1)
def ask(query):
    """Ask the AI for help with terminal commands or general questions."""
    user_query = " ".join(query)
    if not user_query:
        console.print("[bold red]Error:[/bold red] Please provide a query.")
        return

    with console.status("[bold green]Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful terminal assistant. Provide concise, accurate terminal commands and explanations. Use markdown for code blocks."},
                    {"role": "user", "content": user_query}
                ]
            )
            answer = response.choices[0].message.content
            console.print(Markdown(answer))
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {str(e)}")

@cli.command()
@click.argument('error_msg', nargs=-1)
def debug(error_msg):
    """Provide an error message to get debugging suggestions."""
    error_text = " ".join(error_msg)
    if not error_text:
        console.print("[bold red]Error:[/bold red] Please provide an error message.")
        return

    with console.status("[bold yellow]Analyzing error..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are an expert debugger. Analyze the provided error message and suggest potential fixes."},
                    {"role": "user", "content": f"I got this error in my terminal: {error_text}"}
                ]
            )
            suggestion = response.choices[0].message.content
            console.print(Markdown(suggestion))
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {str(e)}")

if __name__ == "__main__":
    cli()
