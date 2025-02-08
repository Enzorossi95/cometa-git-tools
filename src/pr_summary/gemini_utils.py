"""Gemini utilities for PR Summary Generator"""

import google.generativeai as genai
from typing import Optional
from .git_utils import get_branch_name, extract_ticket_from_branch


def generate_pr_summary(diff: str, api_key: str, jira_number: Optional[str] = None) -> str:
    """Generate a PR summary using Gemini"""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    if not jira_number:
        branch_name = get_branch_name()
        jira_number = extract_ticket_from_branch(branch_name)

    ticket_section = (
        f'- [{jira_number}](https://cometa.atlassian.net/browse/{jira_number})'
        if jira_number
        else '- [JIRA-NUMBER](https://cometa.atlassian.net/browse/[JIRA-NUMBER])'
    )

    prompt = f"""
    Analiza los siguientes cambios de git y genera un resumen detallado del Pull Request.
    
    Reglas importantes:
    1. El resumen debe estar en español
    2. Debe incluir TODOS los cambios significativos
    3. Cada cambio debe explicar QUÉ se cambió y PARA QUÉ
    4. Incluir modificaciones de código, no solo nombres de archivos
    5. Mencionar refactorizaciones, nuevas funcionalidades o cambios en la lógica
    6. Usar viñetas con el símbolo • (no guiones -)
    7. Ser específico y técnico en la descripción
    
    El formato DEBE ser exactamente:
    
    ## Cambios realizados
    
    • [Primer cambio significativo con explicación del qué y para qué]
    • [Segundo cambio significativo con explicación del qué y para qué]
    • [Y así sucesivamente para cada cambio importante]
    
    ## Ticket
    
    {ticket_section}
    
    Aquí están los cambios a resumir:
    {diff}
    """

    generation_config = {
        'temperature': 0.7,
        'top_p': 0.8,
        'top_k': 40,
        'max_output_tokens': 2048,
    }

    safety_settings = [
        {'category': 'HARM_CATEGORY_HARASSMENT', 'threshold': 'BLOCK_NONE'},
        {'category': 'HARM_CATEGORY_HATE_SPEECH', 'threshold': 'BLOCK_NONE'},
        {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'threshold': 'BLOCK_NONE'},
        {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'threshold': 'BLOCK_NONE'},
    ]

    response = model.generate_content(
        prompt, generation_config=generation_config, safety_settings=safety_settings
    )

    return response.text
