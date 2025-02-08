# Cometa Git Tools

Una colección de herramientas Git para mejorar el flujo de trabajo de desarrollo, incluyendo un generador de mensajes de commit basado en AI y un generador de resúmenes de PR.

## Características

- 🤖 **AI Conventional Commits**: Genera mensajes de commit siguiendo la convención de Conventional Commits usando Google Gemini AI
- 📝 **PR Summary Generator**: Genera resúmenes de Pull Requests automáticamente
- 🎨 **Interfaz Amigable**: Interfaz de línea de comandos intuitiva y colorida

## Instalación

### Usando pip

```bash
pip install cometa-git-tools
```

### Instalación desde el código fuente

```bash
git clone https://github.com/cometa/cometa-git-tools.git
cd cometa-git-tools
pip install -e .
```

### Configuración

1. Configura tu API key de Google Gemini:
```bash
export GEMINI_API_KEY='your-api-key'
```

2. (Opcional) Agrega la variable a tu archivo .bashrc o .zshrc para hacerla permanente:
```bash
echo 'export GEMINI_API_KEY="your-api-key"' >> ~/.zshrc  # o ~/.bashrc
```

## Uso

### Commitizen AI

Este plugin extiende Commitizen para generar mensajes de commit usando AI:

```bash
# Agrega tus cambios
git add .

# Genera un mensaje de commit con AI
cz commit
```

### PR Summary Generator

Genera resúmenes de Pull Requests:

```bash
# Genera un resumen del PR actual
pr-summary generate

# Ver todas las opciones disponibles
pr-summary --help
```

## Desarrollo

Para contribuir al proyecto:

1. Clona el repositorio
2. Instala las dependencias de desarrollo:
```bash
pip install -e ".[dev]"
```

3. Ejecuta los tests:
```bash
pytest
```

## Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.

## Contribuir

Las contribuciones son bienvenidas! Por favor, lee [CONTRIBUTING.md](CONTRIBUTING.md) para detalles sobre nuestro código de conducta y el proceso para enviar pull requests.

## Soporte

Si encuentras algún problema o tienes una sugerencia, por favor crea un issue en el [repositorio de GitHub](https://github.com/cometa/cometa-git-tools/issues). 