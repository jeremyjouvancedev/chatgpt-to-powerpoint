json_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "presentationTitle": {
      "type": "string",
      "description": "The title of the entire presentation."
    },
    "author": {
      "type": "string",
      "description": "Author of the presentation."
    },
    "slides": {
      "type": "array",
      "description": "Array of slides in the presentation.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "Title of the slide."
          },
          "content": {
            "type": "array",
            "description": "List of content points or paragraphs for the slide.",
            "items": {
              "type": "string"
            }
          },
          "notes": {
            "type": "string",
            "description": "Notes associated with the slide."
          },
          "images": {
            "type": "array",
            "description": "List of image text that can be usefull for text-to-image engine.",
            "items": {
              "type": "string"
            }
          },
          "charts": {
            "type": "array",
            "description": "List of chart data for the slide.",
            "items": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string",
                  "description": "Type of the chart (e.g., bar, pie, line)."
                },
                "data": {
                  "type": "object",
                  "description": "Data for the chart."
                }
              }
            }
          }
        },
        "required": ["title", "content"]
      }
    }
  },
  "required": ["presentationTitle", "slides"]
}
