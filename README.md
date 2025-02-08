# Cometa Git Tools

Una colección de herramientas Git para mejorar el flujo de trabajo de desarrollo, incluyendo un generador de mensajes de commit basado en AI y un generador/creador de Pull Requests.

## Características

- 🤖 **AI Conventional Commits**: Genera mensajes de commit siguiendo la convención de Conventional Commits usando Google Gemini AI
- 📝 **PR Manager**: Genera y crea Pull Requests automáticamente con resúmenes inteligentes
- 🎨 **Interfaz Amigable**: Interfaz de línea de comandos intuitiva y colorida
- 🔧 **Fácil Configuración**: Comando `cz-setup` para configurar todo automáticamente

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

3. Configura Commitizen para usar el plugin AI:
```bash
# Configuración rápida (recomendado)
cz-setup

# Opciones avanzadas:
cz-setup --help         # Ver todas las opciones disponibles
cz-setup --no-global   # Solo configurar el proyecto actual
cz-setup --no-project  # Solo configurar globalmente
```

### Archivos de Configuración

El comando `cz-setup` creará/modificará dos archivos:

1. **~/.commitizen/config.toml**: Configuración global de commitizen
2. **./pyproject.toml**: Configuración local del proyecto

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

Herramienta completa para gestionar Pull Requests:

```bash
# Genera un resumen del PR actual para poder visualizarlo en el editor de texto
pr-summary generate

# Crea un nuevo PR con resumen automático
pr-summary create

# Crea un PR especificando la rama base
pr-summary create --base main

# Ver todas las opciones disponibles
pr-summary --help
```

La herramienta permite:
- 📝 Generar resúmenes detallados de los cambios
- ✨ Crear PRs directamente desde la línea de comandos
- 🔄 Especificar la rama base del PR
- 🤖 Generar títulos y descripciones usando AI

## Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.

## Contribuir

Las contribuciones son bienvenidas! Por favor, lee [CONTRIBUTING.md](CONTRIBUTING.md) para detalles sobre nuestro código de conducta y el proceso para enviar pull requests.

## Soporte

Si encuentras algún problema o tienes una sugerencia, por favor crea un issue en el [repositorio de GitHub](https://github.com/cometa/cometa-git-tools/issues). 