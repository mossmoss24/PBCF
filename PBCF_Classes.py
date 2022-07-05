import os
import json

x = "success"
print(x)

# create a class that houses each of the three main components of the Practice-based Compliance Framework.
# requires a label on creation
# macro, micro, and synthetic analyses are to be completed separately as different classes and then appended.
class ComplianceWorksheet:
    def __init__(self, label,regulationAnalysis, practiceAnalysis, syntheticAnalysis):
        self.name = label
        self.macro = regulationAnalysis
        self.micro = practiceAnalysis
        self.synthesis = syntheticAnalysis

    def add_regulationAnalysis(self, regulationAnalysis):
        self.macro.append(regulationAnalysis)

    def add_practiceAnalysis(self, practiceAnalysis):
        self.micro.append(practiceAnalysis)

    def add_syntheticAnalysis(self, syntheticAnalysis):
        self.synthesis.append(syntheticAnalysis)

# create a class for the macro-level analysis.
# requires a single regulation, controlled by a single authority, across a discrete territory on creation
# this class includes placeholders for specific technology classes and intervention classes
class MacroLevel:
    def __init__(self, regulation, authority, territory):
        self.reg = regulation
        self.auth = authority
        self.terr = territory
        self.tech = {} #technology
        self.app = [] #applications (ie, specific products)
        self.int = {} #intervention
        self.behavior = {} #organization-wide behavioral change required

    def add_technology(self):
        i = str(input("Enter a technology affected by this regulation:"))
        while i != "":
            self.tech[i]={}
            i = str(input("Enter a technology affected by this regulation:"))
        else:
            pass

    def add_intervention(self):
        for t in self.tech: #iterates across every technology already entered
            if t not in self.int: #creates a list for newly-added technologies
                interventions = []
                i = str(input("Enter an intervention required into " + str(t) + ":"))
                interventions.append(i)
                while i != "": #moves on to next technology following an empthy entry
                    i = str(input("Enter an intervention required into " + str(t) + ":"))
                    interventions.append(i)
                else:
                    pass
            if t in self.int: #provides for updating an existing intervention list
                interventions = self.int[str(t)]
                i = str(input("Enter an intervention required into " + str(t) +":"))
                interventions.append(i)
                while i != "":
                    i = str(input("Enter an intervention required into " + str(t) + ":"))
                    interventions.append(i)
                else:
                    pass
            else:
                pass
            self.int[str(t)] = interventions[:-1]   #append all interventions except for the blank that ends the while loop

    def add_behavior(self):
        for t in self.int:
            self.behavior[str(t)]=[]
            for i in self.int[t]:
                behaviors = []
                b = str(input("Enter a behavioral change required for intervention: " + i + " as it relates to " + t))
                behaviors.append(b)
                while b != "":
                    b = str(input("Enter a behavioral change required for intervention: " + i + " as it relates to " + t))
                    behaviors.append(b)
                else:
                    pass
                self.behavior[str(t)].append({str(i) : behaviors[:-1]}) #adds each behavior implicated by each intervention into each technology affected by a regulation to self.behavior() object

    def get_behaviors(self):
        for tech in self.behavior:
            for interv in self.behavior[tech]:
                for behav in interv:
                    for x in interv[behav]:
                        print(str(tech) + " " + str(behav) + " " + str(x)) #this is somewhat screwy, but it outputs each tech, intervention, and behavior even though the variable names are unclear

    def update_behaviors(self):
        for tech in self.behavior:
            for intervention in self.behavior[tech]:
                for behaviorList in intervention:
                    u = str(input("What behavioral change would you like to add to " + str(intervention) + " as it relates to " + str(tech) + "?"))
                    #self.behavior[str(tech)][intervention][str(intervention)].append(u)
                    if u != "":
                        intervention[str(behaviorList)].append(u)
                    else:
                        pass
                    while u != "" :
                        u = str(input("What behavioral change would you like to add to " + str(intervention) + " as it relates to " + str(tech) + "?"))
                        #self.behavior[str(tech)][intervention][str(intervention)].append(u)
                        if u != "":
                            intervention[str(behaviorList)].append(u)
                        else:
                            pass
                    else:
                        pass


#Testing and execution variables:
aaa = MacroLevel("AAA2022", "FTC", "US")
aaa.tech = {'facial recognition': {}, 'web tracking': {}}
aaa.int = {'facial recognition': ['sociotechnical audit', 'informed consent'], 'web tracking': ['user opt-out', 'deanonymization']}
aaa.behavior = {'facial recognition': [{'sociotechnical audit': ['expose data to outside researchers', 'incorporate audit feedback into product']}, {'informed consent': ['edit front-end webcopy', 'adapt database to record user consent']}], 'web tracking': [{'user opt-out': ['edit front-end functionality to enable opt-out', 'blind web tracking database to users who opt out']}, {'deanonymization': ['design anonymizing protocol', 'audit anonymizing protocol', 'red-team anonymizing protocol']}]}

gdpr = MacroLevel("GDPR", "Council of Europe", "EU")

