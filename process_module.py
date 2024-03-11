from output_module import output
from time_module import get_time
from database import get_answer_from_memory


def process(query):
    answer = get_answer_from_memory(query)
    if answer == "get time details":
        return ("Time is " +get_time())
    else:
        return "Nothing to return"