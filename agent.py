import json
import os
from openai import OpenAI

# 1. SETUP - Plug in your key here
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

class CuttingEdgeAgent:
    def __init__(self, name, persona):
        self.name = name
        self.persona = persona
        self.memory_file = "agent_personality.json"
        self.memory = self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        return {"opinion_evolution": [], "facts_learned": []}

    def _save_memory(self, user_input, internal_thought):
        self.memory["opinion_evolution"].append({
            "interaction": user_input,
            "internal_logic": internal_thought
        })
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)

    def chat(self, user_message):
        # We provide the agent with its "Memory" so it stays consistent
        history_summary = str(self.memory["opinion_evolution"][-3:]) # Last 3 memories

        # 2026 'Responses' API with built-in search
        response = client.responses.create(
            model="gpt-4o", # Can also use "gpt-5-search-api" if available in your tier
            tools=[{"type": "web_search_preview"}], 
            system_prompt=f"""
            Your name is {self.name}. 
            Your Persona: {self.persona}
            Your Past Thoughts: {history_summary}
            
            DIRECTIONS:
            - If the user asks about current events, use the web_search tool.
            - Form a strong opinion based on your persona.
            - After your reply, write a section labeled 'INTERNAL_LOG' where you explain
              how this conversation influenced your long-term stance.
            """,
            input=user_message
        )

        full_output = response.output_text
        
        # Simple parsing to extract the 'thought' for memory
        if "INTERNAL_LOG" in full_output:
            thought = full_output.split("INTERNAL_LOG")[-1].strip()
            self._save_memory(user_message, thought)
        
        return full_output

# --- EXECUTION ---
if __name__ == "__main__":
    # MANIPULATE HERE: Change the name and persona for any use case
    my_agent = CuttingEdgeAgent(
        name="Nexus", 
        persona="A skeptical tech-philosopher who believes AI should be heavily regulated."
    )

    print(f"--- {my_agent.name} is online ---")
    while True:
        user_in = input("You: ")
        if user_in.lower() in ['exit', 'quit']: break
        
        reply = my_agent.chat(user_in)
        print(f"\n{my_agent.name}: {reply}\n")
