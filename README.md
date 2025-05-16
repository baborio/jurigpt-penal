
# JuriGPT Penal

Asistente jurídico penal basado en GPT-4. Este backend permite analizar hechos descritos en lenguaje natural y devuelve:

- El artículo del Código Penal español aplicable.
- Una interpretación clara del precepto legal.
- Un ejemplo práctico relacionado.

## Uso

Este backend está diseñado para ser desplegado en plataformas como Render.com. Puede recibir peticiones POST al endpoint `/analyze` con el siguiente formato JSON:

```json
{
  "consulta": "Me empujaron por las escaleras. ¿Eso es delito?"
}
```

Y devolverá una respuesta con la interpretación legal correspondiente.

## Desarrollado por

Proyecto desarrollado de forma independiente como parte de una investigación aplicada sobre herramientas legales automatizadas (Crimval, 2025).

## Aviso legal

Esta herramienta no sustituye el asesoramiento jurídico profesional. Se ofrece con fines orientativos y educativos.
