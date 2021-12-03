 
class AddedToken:
    """
    AddedToken represents a token to be added to a Tokenizer 
    An AddedToken can have special options defining the
    way it should behave.
    """
    content: str 
    single_word: bool = False
    lstrip: bool = False
    rstrip: bool = False
    normalized: bool = True
    def __init__(self,content):
        self.content = content
    def __getstate__(self):
        return self.__dict__

def add_end_docstrings(*docstr):
    def docstring_decorator(fn):
        fn.__doc__ = fn.__doc__ + "".join(docstr)
        return fn

    return docstring_decorator


# class ExplicitEnum(Enum):
#     """
#     Enum with more explicit error message for missing values.
#     """

#     @classmethod
#     def _missing_(cls, value):
#         raise ValueError(
#             f"{value} is not a valid {cls.__name__}, please select one of {list(cls._value2member_map_.keys())}"
#         )


class PaddingStrategy:
    """
    Possible values for the ``padding`` argument in :meth:`PreTrainedTokenizerBase.__call__`. Useful for tab-completion
    in an IDE.
    """

    LONGEST = "longest"
    MAX_LENGTH = "max_length"
    DO_NOT_PAD = "do_not_pad"


class TruncationStrategy:
    """
    Possible values for the ``truncation`` argument in :meth:`PreTrainedTokenizerBase.__call__`. Useful for
    tab-completion in an IDE.
    """

    ONLY_FIRST = "only_first"
    ONLY_SECOND = "only_second"
    LONGEST_FIRST = "longest_first"
    DO_NOT_TRUNCATE = "do_not_truncate"

class TensorType:
    """
    Possible values for the ``return_tensors`` argument in :meth:`PreTrainedTokenizerBase.__call__`. Useful for
    tab-completion in an IDE.
    """

    PYTORCH = "pt"
    TENSORFLOW = "tf"
    NUMPY = "np"
    JAX = "jax"