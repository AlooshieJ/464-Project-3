
from simv2 import Circuit


# Simulator :
# encompases the entire circuit sim, but also keeps track of how to run the sim
# The idea is we can use this class to determine:
# - how we control potential automation for every TV generation option
# - which inputs to use, (user input , auto generated inputs)

class Simulator(object):

    def __init__(self):

        self.C = Circuit()
        self.TV = ''  # to be class TV
        self.Full_Fault_List = []

        #  Different modes: 0 - user input (P1), 1 - auto TV and Fault  , 2 - input TV and auto fault
        self.run_mode = 0

    # initialize variables
    # Init FULL fault list for circuit
    # init TV generated LIST

    def init_inputs(self):
        pass

    # if sim should be user input or generated tv
    def set_inputs_mode(self):
        s = f"How do you want to run the simulator?\n" \
            f"(0) Run simulation with User input TV and Fault\n" \
            f"(1) Run simulation using PRPG on all Faults\n" \
            f"(2) ?!?!?!?!?!"
        options = ["0" , "1", "2"]
        print(s)
        choice = input(">")
        while choice not in options:
            print(s)
            choice = input(">")

        self.run_mode = choice

        pass

    # choose bench file , this takes place in Circuit class
    # def set_benchfile(self):
    #     # self.C.set_bench()
    #     pass

    def init_Circuit(self):

        # set the bench file
        self.C.set_bench()
        # construct nodelist
        self.C.construct_nodelist()


    def run_sim(self):

        # sets run mode for circuit.
        self.set_inputs_mode()
        self.init_inputs()


        if self.run_mode == 0:
            self.C.run_input()
        elif self.run_mode == 1:
            self.C.run_auto()

        pass

Sim = Simulator()

Sim.run_sim()