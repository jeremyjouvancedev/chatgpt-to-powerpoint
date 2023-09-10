import os
import json
from datetime import datetime
from pptx import Presentation
from pptx.util import Inches


from chatgpt_to_powerpoint.langchainHandler import LangChainHandler
from chatgpt_to_powerpoint.slideLayout import SlideLayouts

class PowerPointGenerator:
    def __init__(self, model_type='ChatOpenAI', model_name='gpt-3.5-turbo'):
        self.langchain_model = LangChainHandler(model_type, model_name)
        self.slide_layouts = SlideLayouts()

    def generate_slides(self, nb_of_slides, topic, output_folder, output_original, load_json=None):
        current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output = f"{current_date}_{output_original}.pptx"
        response = None

        if not load_json:
            chain = self.langchain_model.generate_chain(nb_of_slides)
            response = chain.run(topic)

            with open(os.path.join(output_folder, output) +'.json', 'w') as json_file:
                json.dump(response, json_file)
        else:
            with open(os.path.join(output_folder, load_json), "r") as json_file:
                response = json.load(json_file)

        prs = Presentation()
        slides_data = response['slides']

        for idx, slide_data in enumerate(slides_data):
            print(f"Generated Slide {idx+1}/{len(slides_data)} {slide_data['layout']}")

            if slide_data["layout"] == "Title Slide":
                SlideLayouts.title_slide(prs, slide_data)
            elif slide_data["layout"] == "Title and Content":
                SlideLayouts.title_and_content(prs, slide_data)
            elif slide_data["layout"] == "Two Content":
                SlideLayouts.two_content(prs, slide_data)
            elif slide_data["layout"] == "Comparison":
                SlideLayouts.comparison(prs, slide_data)
            elif slide_data["layout"] == "Content with Caption":
                SlideLayouts.content_with_caption(prs, slide_data)
            elif slide_data["layout"] == "Blank":
                SlideLayouts.blank(prs, slide_data)
            elif slide_data["layout"] == "Picture with Caption":
                SlideLayouts.picture_with_caption(prs, slide_data)
            else:
                print(f'Layout >{slide_data["layout"]}< not implemented')


        prs.save(os.path.join(output_folder, output))