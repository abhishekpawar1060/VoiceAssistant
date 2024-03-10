from input_module import take_input
from process_module import process
from output_module import output

while(True):
    input = take_input()
    pro = process(input)
    output(pro)
