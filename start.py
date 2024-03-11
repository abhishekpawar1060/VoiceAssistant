from input_module import take_input
from process_module import process
from output_module import output
import os
os.system("cls")

while(True):
    input = take_input()
    pro = process(input)
    output(pro)
