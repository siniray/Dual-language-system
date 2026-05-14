init python:
    import re
    DEFAULT_BL_COLOR = "#e8c972" 
    
    SUB_LANG_COLOR = "#AAAAAA"
    SUB_LANG_SIZE = 18

    def process_dual_lang_samanta(text):
        if not text:
            return text
        
        ru_parts = []
        en_parts = []
        
        block_pattern = r'\{(ru|en)\}([\s\S]*?)\{/\1\}'
        matches = list(re.finditer(block_pattern, text))
        
        if not matches:
            return text

        last_end = 0
        plain_text_prefix = ""
        
        for m in matches:
            prefix = text[last_end:m.start()]
            if not ru_parts and not en_parts:
                plain_text_prefix = prefix
            
            lang, content = m.groups()
            
            if lang == 'ru':
                ru_parts.append(content)
            elif lang == 'en':
                en_parts.append(content)
                
            last_end = m.end()
        
        suffix = text[last_end:]
        
        final_ru = plain_text_prefix + "".join(ru_parts) + suffix
        final_en = " ".join(en_parts)
        
        
        current_lang = persistent.ss_text_lang
        
        if current_lang == "en":
            main_text = final_en
            sub_text = final_ru
            
            
            main_color_tag = "{color=" + DEFAULT_BL_COLOR + "}"
            

            sub_color_tag = "{size=" + str(SUB_LANG_SIZE) + "}{color=" + SUB_LANG_COLOR + "}"
        else:

            main_text = final_ru
            sub_text = final_en
            
            style_ru_raw = persistent.ss_text_style_ru
            
            
            if style_ru_raw.startswith("color="):
                main_color_tag = "{" + style_ru_raw + "}"
            else:
                main_color_tag = "{color=" + style_ru_raw + "}"
                

            sub_color_tag = "{size=" + str(SUB_LANG_SIZE) + "}{color=" + SUB_LANG_COLOR + "}"
        
        if sub_text.strip():

            return main_color_tag + main_text + "{/color}\n" + sub_color_tag + sub_text + "{/color}{/size}"
        else:
            return main_color_tag + main_text + "{/color}"

    config.say_menu_text_filter = process_dual_lang_samanta