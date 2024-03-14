from output_module import output
from time_module import get_time
from database import get_answer_from_memory,insert_question_and_answer
from input_module import take_input

def process(query):
    answer = get_answer_from_memory(query)
    if answer == "get time details":
        return "Time is "+get_time()
    
    else:
        output("I don't know this one, can you please tell m what is means?")
        ans = take_input()
        if "it means" in ans :
            ans = ans.replace("it means", "")
            ans = ans.strip()
            value = get_answer_from_memory(ans)

            if value == "":
                return "Can't help with this one"
            else:
                insert_question_and_answer(query,value)
                return "Thanks I will remember it for the next time"

        return "Nothing to return"   



    # answer = get_answer_from_memory(query)
    # if answer == "get time details":
    #     return ("Time is " +get_time())
    # else:
    #     return "Nothing to return"