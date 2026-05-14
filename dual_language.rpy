init python:
    import re

    def process_dual_lang(text):
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
        
        if final_en.strip():
            return "{color=#8EC8FF}" + final_ru + "{/color}\n{size=18}{color=#AAAAAA}" + final_en + "{/color}{/size}"
        else:
            return "{color=#8EC8FF}" + final_ru + "{/color}"

    config.say_menu_text_filter = process_dual_lang