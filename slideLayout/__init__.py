def clean_text(text):
    return text


class SlideLayouts:
    @staticmethod
    def title_and_content(prs, slide_data):
        slide_layout = prs.slide_layouts[1]  # 'Title and Content' layout
        slide = prs.slides.add_slide(slide_layout)

        # Set slide title
        slide.shapes.title.text = slide_data["title"]

        # Add content to the slide
        content_shape = slide.placeholders[1]
        for point in slide_data["content"]:
            p = content_shape.text_frame.add_paragraph()
            p.text = point

    @staticmethod
    def title_slide(prs, slide_data):
        slide_layout = prs.slide_layouts[0]  # 'Title and Content' layout
        slide = prs.slides.add_slide(slide_layout)

        # Set slide title
        slide.shapes.title.text = clean_text(slide_data["title"])

    @staticmethod
    def two_content(prs, slide_data):
        if (
            len(slide_data.get("content", [])) > 0
            and len(slide_data.get("left_content", [])) == 0
            and len(slide_data.get("right_content", [])) == 0
        ):
            SlideLayouts.title_and_content(prs, slide_data)
        else:
            slide_layout = prs.slide_layouts[3]
            slide = prs.slides.add_slide(slide_layout)

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
        slide_layout = prs.slide_layouts[
            3
        ]  # Assuming 'Comparison' layout is at index 3
        slide = prs.slides.add_slide(slide_layout)

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
    def content_with_caption(prs, slide_data):
        slide_layout = prs.slide_layouts[
            4
        ]  # Assuming 'Content with Caption' layout is at index 4
        slide = prs.slides.add_slide(slide_layout)

        # Set slide title
        slide.shapes.title.text = clean_text(slide_data["title"])

        # Add content
        content_shape = slide.placeholders[2]
        for point in slide_data["content"]:
            p = content_shape.text_frame.add_paragraph()
            p.text = clean_text(point)

        # Add caption
        caption_shape = slide.placeholders[4]
        caption_shape.text = clean_text(slide_data["caption"])
