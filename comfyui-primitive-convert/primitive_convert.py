from comfy.comfy_types import IO, InputTypeDict
from inspect import cleandoc


class ToStringNode:
    """
    Converts any primitive value (STRING, FLOAT, INT, BOOLEAN) to its string representation
    """

    DESCRIPTION = cleandoc(__doc__ or "")
    CATEGORY = "utils/convert"

    @classmethod
    def INPUT_TYPES(cls) -> InputTypeDict:
        return {
            "required": {
                "value": (IO.ANY, {}),
            },
        }

    RETURN_TYPES = (IO.STRING,)
    FUNCTION = "convert_to_string"

    def convert_to_string(self, value):

        return (str(value),)


class ToIntNode:
    """
    Converts any primitive value (STRING, FLOAT, INT, BOOLEAN) to its int representation
    """

    DESCRIPTION = cleandoc(__doc__ or "")
    CATEGORY = "utils/convert"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (IO.PRIMITIVE, {}),
            },
        }

    RETURN_TYPES = (IO.INT,)
    FUNCTION = "convert_to_int"

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
    """
    Converts any primitive value (STRING, FLOAT, INT, BOOLEAN) to its float representation
    """

    DESCRIPTION = cleandoc(__doc__ or "")
    CATEGORY = "utils/convert"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (IO.PRIMITIVE, {}),
            },
        }

    RETURN_TYPES = (IO.FLOAT,)
    FUNCTION = "convert_to_float"

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
