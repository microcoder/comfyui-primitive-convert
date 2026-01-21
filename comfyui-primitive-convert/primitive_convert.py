

class ToStringNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Типы которые узел принимает на вход:
                "value": ("*"),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "convert_to_string"
    CATEGORY = "utils/convert"

    def convert_to_string(self, value):
        # Обрабатываем случай, если значение — число, булево, None и т.д.
        if isinstance(value, (int, float, str, bool)) or value is None:
            return (str(value),)
        else:
            raise ValueError(f"Unsupported type for ToString: {type(value)}")


class ToIntNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("*",),
            },
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "convert_to_int"
    CATEGORY = "utils/convert"

    def convert_to_int(self, value):

        if value is None:
            return (0,)

        if isinstance(value, int):
            return (value,)

        if isinstance(value, float):
            return (int(round(value)),)  # или int(value) для усечения

        if isinstance(value, str):
            value = value.strip()
            if value == "":
                return (0,)
            try:
                # Сначала пробуем как целое
                if '.' not in value and 'e' not in value.lower():
                    return (int(value),)
                else:
                    return (int(float(value)),)
            except ValueError:
                return (0,)

        # Если bool: True → 1, False → 0
        if isinstance(value, bool):
            return (int(value),)


        return (0,)


class ToFloatNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("*",),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "convert_to_float"
    CATEGORY = "utils/convert"

    def convert_to_float(self, value):

        if value is None:
            return (0.0,)

        if isinstance(value, float):
            return (value,)

        if isinstance(value, int):
            return (float(value),)

        if isinstance(value, str):
            value = value.strip()
            if value == "":
                return (0.0,)
            try:
                return (float(value),)
            except ValueError:
                return (0.0,)

        # Если bool: True → 1.0, False → 0.0
        if isinstance(value, bool):
            return (float(value),)

        return (0.0,)



NODE_CLASS_MAPPINGS = {
    "ToString": ToStringNode,
    "ToInt": ToIntNode,
    "ToFloat": ToFloatNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ToString": "To String",
    "ToInt": "To Int",
    "ToFloat": "To Float",
}
