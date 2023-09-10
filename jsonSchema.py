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
          "layout": {
            "type": "string",
            "description": "Layout of the slide.",
            "enum": ["Title Slide", "Title and Content", "Section Header", "Two Content", "Comparison", "Blank", "Content with Caption", "Picture with Caption"]
          },
          "title": {
            "type": "string",
            "description": "Title of the slide."
          },
          "subtitle": {
            "type": "string",
            "description": "Subtitle of the slide (ONLY for Title Slide layout)."
          },
          "title_left": {
            "type": "string",
            "description": "Title for the left side of the slide (ONLY for Comparison layout)."
          },
          "title_right": {
            "type": "string",
            "description": "Title for the right side of the slide (ONLY for Comparison layout)."
          },
          "content": {
            "type": "array",
            "description": "List of content points or paragraphs for the slide (ONLY for Title and Content layout).",
            "items": {
              "type": "string"
            }
          },
          "left_content": {
            "type": "array",
            "description": "List of content points or paragraphs for the left side of the slide (ONLY for Two Content or Comparison layouts).",
            "items": {
              "type": "string"
            }
          },
          "right_content": {
            "type": "array",
            "description": "List of content points or paragraphs for the right side of the slide (ONLY for Two Content or Comparison layouts).",
            "items": {
              "type": "string"
            }
          },
          "caption": {
            "type": "string",
            "description": "Caption for the slide (ONLY for Content with Caption layout)."
          },
          "notes": {
            "type": "string",
            "description": "Notes associated with the slide."
          },
          "images": {
            "type": "array",
            "description": "List of image URLs or paths for the slide.",
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
        "required": ["layout", "title"]
      }
    }
  },
  "required": ["presentationTitle", "slides"]
}
