def clean_text(text):
    return text

def get_layout_id(prs, name):
    for idx, l in enumerate(prs.slide_layouts):
        #print(idx, l, l.name)
        if l.name == name:
            return idx
        
def add_note(slide, note):
    if not note:
        return
    # Add notes to the slide
    notes_slide = slide.notes_slide
    notes_slide.notes_text_frame.text = note


class SlideLayouts:
    @staticmethod
    def title_and_content(prs, slide_data):
        slide_layout = prs.slide_layouts[get_layout_id(prs, "Title and Content")]  # 'Title and Content' layout
        slide = prs.slides.add_slide(slide_layout)
        add_note(slide, slide_data.get('notes'))

        # Set slide title
        slide.shapes.title.text = slide_data["title"]

        # Add content to the slide
        content_shape = slide.placeholders[1]
        for point in slide_data["content"]:
            p = content_shape.text_frame.add_paragraph()
            p.text = point

    @staticmethod
    def title_slide(prs, slide_data):
        slide_layout = prs.slide_layouts[get_layout_id(prs, "Title Slide")]  # 'Title and Content' layout
        slide = prs.slides.add_slide(slide_layout)
        add_note(slide, slide_data.get('notes'))

        # Set slide title
        slide.shapes.title.text = clean_text(slide_data["title"])

        left_content_shape = slide.placeholders[1]
        p = left_content_shape.text_frame.add_paragraph()
        p.text = clean_text(slide_data.get('subtitle'))

    @staticmethod
    def two_content(prs, slide_data):
        if (
            len(slide_data.get("content", [])) > 0
            and len(slide_data.get("left_content", [])) == 0
            and len(slide_data.get("right_content", [])) == 0
        ):
            SlideLayouts.title_and_content(prs, slide_data)
        else:
            slide_layout = prs.slide_layouts[get_layout_id(prs, "Two Content")]
            slide = prs.slides.add_slide(slide_layout)
            add_note(slide, slide_data.get('notes'))

            # Set slide title
            slide.shapes.title.text = clean_text(slide_data["title"])

            # Add content to the left placeholder
            left_content_shape = slide.placeholders[1]
            for point in slide_data["left_content"]:
                p = left_content_shape.text_frame.add_paragraph()
                p.text = clean_text(point)

            # Add content to the right placeholder
            right_content_shape = slide.placeholders[2]
            for point in slide_data["right_content"]:
                p = right_content_shape.text_frame.add_paragraph()
                p.text = clean_text(point)

    @staticmethod
    def comparison(prs, slide_data):
        if (
            len(slide_data.get("content", [])) > 0
            and len(slide_data.get("left_content", [])) == 0
            and len(slide_data.get("right_content", [])) == 0
        ):
            return SlideLayouts.title_and_content(prs, slide_data)


        slide_layout = prs.slide_layouts[
            get_layout_id(prs, "Comparison")
        ]  # Assuming 'Comparison' layout is at index 3
        slide = prs.slides.add_slide(slide_layout)
        add_note(slide, slide_data.get('notes'))

        # Set slide title
        slide.shapes.title.text = clean_text(slide_data["title"])

        # Add title to the left placeholder
        left_content_shape = slide.placeholders[1]
        p = left_content_shape.text_frame.add_paragraph()
        p.text = clean_text(slide_data.get('title_left'))


        # Add content to the left placeholder
        left_content_shape = slide.placeholders[2]
        for point in slide_data["left_content"]:
            p = left_content_shape.text_frame.add_paragraph()
            p.text = clean_text(point)

        # Add title to the rigth placeholder
        right_content_shape = slide.placeholders[3]
        p = right_content_shape.text_frame.add_paragraph()
        p.text = clean_text(slide_data.get('title_right'))

        # Add content to the right placeholder
        right_content_shape = slide.placeholders[4]
        for point in slide_data["right_content"]:
            p = right_content_shape.text_frame.add_paragraph()
            p.text = clean_text(point)

    @staticmethod
    def content_with_caption(prs, slide_data):
        slide_layout = prs.slide_layouts[
            get_layout_id(prs, "Content with Caption")
        ]  # Assuming 'Content with Caption' layout is at index 4
        slide = prs.slides.add_slide(slide_layout)
        add_note(slide, slide_data.get('notes'))

        # Set slide title
        slide.shapes.title.text = clean_text(slide_data["title"])

        # Add content
        content_shape = slide.placeholders[1]
        for point in slide_data["content"]:
            p = content_shape.text_frame.add_paragraph()
            p.text = clean_text(point)

        # Add caption
        caption_shape = slide.placeholders[0]
        caption_shape.text = clean_text(slide_data["title"])

    @staticmethod
    def blank(prs, slide_data):
        slide_layout = prs.slide_layouts[
            get_layout_id(prs, "Blank")
        ]  # Assuming 'Content with Caption' layout is at index 4
        slide = prs.slides.add_slide(slide_layout)
        add_note(slide, slide_data.get('notes'))

    @staticmethod
    def picture_with_caption(prs, slide_data):
        slide_layout = prs.slide_layouts[
            get_layout_id(prs, "Picture with Caption")
        ]  # Assuming 'Content with Caption' layout is at index 4
        slide = prs.slides.add_slide(slide_layout)
        add_note(slide, slide_data.get('notes'))

        content_shape = slide.placeholders[0]
        p = content_shape.text_frame.add_paragraph()
        p.text = slide_data["title"]    

        # Add content
        content_shape = slide.placeholders[2]
        p = content_shape.text_frame.add_paragraph()
        p.text = clean_text(slide_data["caption"])