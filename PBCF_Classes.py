import os
import json
from string import ascii_uppercase as az


# create a class that houses each of the three main components of the Practice-based Compliance Framework.
# requires a label on creation
# macro, micro, and synthetic analyses are to be completed separately as different classes and then appended.
class ComplianceWorksheet:
    def __init__(self, label, regulationAnalysis, practiceAnalysis, syntheticAnalysis):
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
        self.tech = {}  # technology
        self.app = []  # applications (ie, specific products)
        self.int = {}  # intervention
        self.behavior = {}  # organization-wide behavioral change required

    def add_technology(self):
        i = str(input("Enter a technology affected by this regulation (press ENTER if there is nothing else to add):"))
        while i != "":
            self.tech[i] = {}
            i = str(input("Enter a technology affected by this regulation (press ENTER if there is nothing else to add):"))
        else:
            pass

    def add_intervention(self):
        for t in self.tech:  # iterates across every technology already entered
            if t not in self.int:  # creates a list for newly-added technologies
                interventions = []
                i = str(input("Enter an intervention required into " + str(t) + " (press ENTER if there is nothing else to add):"))
                interventions.append(i)
                while i != "":  # moves on to next technology following an empthy entry
                    i = str(input("Enter an intervention required into " + str(t) + " (press ENTER if there is nothing else to add):"))
                    interventions.append(i)
                else:
                    pass
            if t in self.int:  # provides for updating an existing intervention list
                interventions = self.int[str(t)]
                i = str(input("Enter an intervention required into " + str(t) + " (press ENTER if there is nothing else to add):"))
                interventions.append(i)
                while i != "":
                    i = str(input("Enter an intervention required into " + str(t) + " (press ENTER if there is nothing else to add):"))
                    interventions.append(i)
                else:
                    pass
            else:
                pass
            self.int[str(t)] = interventions[
                               :-1]  # append all interventions except for the blank that ends the while loop

    def add_behavior(self):
        for t in self.int:
            self.behavior[str(t)] = []
            for i in self.int[t]:
                behaviors = []
                b = str(input("Enter a behavioral change required for intervention: " + i + " as it relates to " + t + " (press ENTER if there is nothing else to add)"))
                while b != "":
                    behaviors.append(b)
                    b = str(
                        input("Enter a behavioral change required for intervention: " + i + " as it relates to " + t + " (press ENTER if there is nothing else to add)"))
                else:
                    pass
                self.behavior[str(t)].append({str(i):behaviors[:-1]})  # adds each behavior implicated by each intervention into each technology affected by a regulation to self.behavior() object

    def get_behaviors(self):
        for tech in self.behavior:
            report_tech = str(tech)
            n = 1
            for interv in self.behavior[tech]:
                for behav in interv:
                    print("Intervention #" + str(n) + " for " + report_tech + " is " + behav + ". This requires the following behavioral change:")
                    n += 1
                    a = 0
                    for x in interv[behav]:
                        # print(str(tech) + " " + str(behav) + " " + str(x)) #this is somewhat screwy, but it outputs each tech, intervention, and behavior even though the variable names are unclear
                        if a < 25:
                            print(str(az[a] + ") " + x))
                            a += 1
                        else:
                            print(str(az[int(a/26)]) + str(az[a % 26] + ") " + x))

    def update_behaviors(self):
        for tech in self.behavior:
            for intervention in self.behavior[tech]:
                for behaviorList in intervention:
                    u = str(input("What behavioral change would you like to add to " + str(
                        intervention)[11:-2] + " as it relates to " + str(tech) + "?  (press ENTER if there is nothing else to add)"))
                    # self.behavior[str(tech)][intervention][str(intervention)].append(u)
                    if u != "":
                        intervention[str(behaviorList)].append(u)
                    else:
                        pass
                    while u != "":
                        u = str(input("What behavioral change would you like to add to " + str(
                            intervention[11:-2]) + " as it relates to " + str(tech) + "?  (press ENTER if there is nothing else to add)"))
                        # self.behavior[str(tech)][intervention][str(intervention)].append(u)
                        if u != "":
                            intervention[str(behaviorList)].append(u)
                        else:
                            pass
                    else:
                        pass
#Define a class for the micro-level analysis, that calls on the interventions and behaviors of the macro analysis
class MicroLevel:
    def __init__(self, macroObject):
        self.regulation = macroObject.reg
        self.territory = macroObject.terr
        self.authority = macroObject.auth
        self.behaviors = macroObject.behavior
        self.focusIntervention = None
        self.interventionBehaviors = []
        self.socialPractices = {}

    #define a function that selects an intervention from the Macro Analysis
    def selectIntervention(self):
        #takes as an argument the MacroLevel.behaviors object, which should have >=1 technologies, interventions, and behaviors
        #prompts user to select a technology from that object, saves response as a variable
        print("Which technology would you like to conduct a micro analysis for? You may select: ")
        iterator = 0
        for b in self.behaviors.keys():
            print(str(az[iterator]) + ": " + b)
            iterator += 1
        enteredTech = input("Enter letter: ")
        selectedTech = self.behaviors[str(list(self.behaviors.keys())[az.index(enteredTech)])]

        #prompts user to select an intervention related to the selected technology, saves response as a variable
        print("Which intervention into " + str(list(self.behaviors.keys())[az.index(enteredTech)]) + " would you like to conduct a micro analysis for? You may select: ")
        iterator = 0
        for i in selectedTech:
            print(str(az[iterator]) + ": " + str(i.keys())[11:-2])
            iterator += 1
        enteredIntervention = input("Enter letter: ")
        selectedIntervention = selectedTech[az.index(enteredIntervention)]
        self.focusIntervention = str(selectedIntervention.keys())[11:-2]

        #prompts user to select a behavior that comprises the selected intervention, saves response as a variable
        print("The behaviors relevant to " + str(selectedIntervention.keys())[11:-2] + " are:")
        for j in selectedIntervention[str(selectedIntervention.keys())[12:-3]]:
            self.interventionBehaviors.append(j)
            print(j)

#define a function to add a single key to the social practices dictionary, with predefined elements and carriers keys, that prompts for entries for those keys
    def enterSocialPractice(self):
        spPrompt = input("Enter a social practice associated with " + str(self.focusIntervention) + " :")
        self.socialPractices[spPrompt]={'elements':{'meanings':[], 'competencies':[], 'materials':[]}, 'carriers':[]}

        #prompt for meanings, competencies, materials, and carriers
        #materials
        mats = []
        matPrompt = input("Enter a material associated with " + str(spPrompt) + " :")
        mats.append(matPrompt)

        while matPrompt != "":
            matPrompt = input("Enter another material associated with " + str(spPrompt) + " :")
            mats.append(matPrompt)

        self.socialPractices[spPrompt]['elements']['materials'] = mats[:-1]

        #meanings
        means = []
        meanPrompt = input("Enter a meaning associated with " + str(spPrompt) + " :")
        means.append(meanPrompt)

        while meanPrompt != "":
            meanPrompt = input("Enter another meaning associated with " + str(spPrompt) + " :")
            means.append(meanPrompt)

        self.socialPractices[spPrompt]['elements']['meanings'] = means[:-1]

        #competencies
        comps = []
        compPrompt = input("Enter a competency associated with " + str(spPrompt) + " :")
        comps.append(compPrompt)

        while compPrompt != "":
            compPrompt = input("Enter another competency associated with " + str(spPrompt) + " :")
            comps.append(compPrompt)

        self.socialPractices[spPrompt]['elements']['competencies'] = comps[:-1]

        #carriers
        carrs = []
        carrPrompt = input("Enter a carrier of " + str(spPrompt) + " :")
        carrs.append(carrPrompt)

        while carrPrompt != "":
            carrPrompt = input("Enter another carrier of " + str(spPrompt) + " :")
            carrs.append(carrPrompt)

        self.socialPractices[spPrompt]['carriers'] = carrs[:-1]

#[[[RESTART HERE]]]









    #def findSocialPractices(self):

#something like:
#x = input("Which technology are you interested in running a Micro Analysis for?" + for i in range(len(aaa.behavior): for x in aaa.behavior: print(az[i] + ": " + aaa.behavior[x])


# Testing and execution variables:
aaa = MacroLevel("AAA2022", "FTC", "US")
aaa.tech = {'facial recognition': {}, 'web tracking': {}}
aaa.int = {'facial recognition': ['sociotechnical audit', 'informed consent'],
           'web tracking': ['user opt-out', 'deanonymization']}
aaa.behavior = {'facial recognition': [
    {'sociotechnical audit': ['expose data to outside researchers', 'incorporate audit feedback into product']},
    {'informed consent': ['edit front-end webcopy', 'adapt database to record user consent']}], 'web tracking': [{
                                                                                                                     'user opt-out': [
                                                                                                                         'edit front-end functionality to enable opt-out',
                                                                                                                         'blind web tracking database to users who opt out']},
                                                                                                                 {
                                                                                                                     'deanonymization': [
                                                                                                                         'design anonymizing protocol',
                                                                                                                         'audit anonymizing protocol',
                                                                                                                         'red-team anonymizing protocol']}]}

gdpr = MacroLevel("GDPR", "Council of Europe", "EU")

#Script for prompting users to fill out Compliance worksheet

#begin Macro-Level Regulation Analysis
#prompt for legislative details
regulationInput = input("What is the regulation?")
authorityInput = input("Who is the authority?")
territoryInput = input("What is the territory?")

#create MacroLevel object regAnalysis
regAnalysis = MacroLevel(regulationInput, authorityInput, territoryInput)

#prompt for technologies subject to this regulation
print("Current regulation being analyzed is " + str(regulationInput))
regAnalysis.add_technology()

#prompt for interventions needed for each technology
regAnalysis.add_intervention()

#prompt behaviors associated with each intervention
regAnalysis.add_behavior()

#output MacroLevel worksheet status
print("The regulation currently being analyzed is " + str(regulationInput))

print(str(regulationInput) + " has been associated with " + str(len(regAnalysis.tech)) + " technologies:")
for t in regAnalysis.tech:
    print("- " + str(t))

regAnalysis.get_behaviors()

#prompt for additional technologies
print("Would you like to add any additional technologies, interventions, or behaviors at this time?")
print("press 'Enter' to skip adding additional items at this time")
new_tech = input("Y?")
if new_tech == "Y" or new_tech == "y":
    print("The regulation currently being analyzed is " + str(regulationInput))
    regAnalysis.add_technology()
    regAnalysis.add_intervention()
    regAnalysis.update_behaviors()
else:
    pass

print("Would you like to conduct a micro-level analysis now?")
new_micro = input("Y/N?")
if new_micro == "Y" or new_micro == "y":
    microAnalysis = MicroLevel(regAnalysis)
    microAnalysis.selectIntervention()
    microAnalysis.enterSocialPractice()
else:
    pass



### To-do: (1) "update" function dosen't seem to be working properly (2) add JSON functionality



