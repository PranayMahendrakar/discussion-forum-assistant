#!/usr/bin/env python3
"""Discussion Forum Assistant - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import ResponseGenerator, ModerationHelper

console = Console()
responder = ResponseGenerator()
moderator = ModerationHelper()

def main():
    console.print(Panel("💬 DISCUSSION FORUM ASSISTANT 💬\nModerate and Engage", style="bold purple"))
    
    while True:
        action = Prompt.ask("Action", choices=["respond", "moderate", "quit"])
        if action == "quit": break
        
        post = Prompt.ask("Post content")
        if action == "respond":
            result = responder.process(post)
        else:
            result = moderator.process(post)
        console.print(Panel(Markdown(result), title=action.title(), border_style="purple"))

if __name__ == "__main__": main()
