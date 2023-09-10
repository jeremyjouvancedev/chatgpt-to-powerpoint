import json
from pptx import Presentation
from pptx.util import Inches


from langchainHandler import LangChainHandler
from slideLayout import SlideLayouts

class PowerPointGenerator:
    def __init__(self, model_type='ChatOpenAI', model_name='gpt-3.5-turbo'):
        self.langchain_model = LangChainHandler(model_type, model_name)
        self.slide_layouts = SlideLayouts()

    def generate_slides(self, nb_of_slides, topic, output, load_json=False):
        response = None

        if not load_json:
            chain = self.langchain_model.generate_chain(nb_of_slides)
            response = chain.run(topic)

            with open(output+'.json', 'w') as json_file:
                json.dump(response, json_file)
        else:
            with open(output + ".json", "r") as json_file:
                response = json.load(json_file)

        prs = Presentation()
        slides_data = response['slides']

        for idx, slide_data in enumerate(slides_data):
            print(f"Generated Slide {idx+1}/{len(slides_data)}")

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
            else:
                print(f'Layout >{slide_data["layout"]}< not implemented')


        prs.save(output)