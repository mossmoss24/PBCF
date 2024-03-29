#Practice-based Compliance Framework developed by Mona Sloane, PhD. and Emanuel D. Moss, PhD.
#Article and additional documentation available at https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4060262
#
#released under GNU General Public License v3.0
#

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
        self.definition = {}  # tech definition
        self.int = {}  # intervention
        self.behavior = {}  # organization-wide behavioral change required

    def add_technology(self):
        i = str(input("Enter a technology affected by this regulation (press ENTER if there is nothing else to add):"))
        while i != "":
            self.tech[i] = {}
            j = str(input("Enter a definition of " + str(i)) + ":")
            self.definition[i] = j
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
                self.behavior[str(t)].append({str(i):behaviors})  # adds each behavior implicated by each intervention into each technology affected by a regulation to self.behavior() object

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
                    if u != "":
                        intervention[str(behaviorList)].append(u)
                    else:
                        pass
                    while u != "":
                        u = str(input("What behavioral change would you like to add to " + str(
                            intervention[11:-2]) + " as it relates to " + str(tech) + "?  (press ENTER if there is nothing else to add)"))
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
        self.allInterventions = {}
        self.selectedTech = None

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
        self.selectedTech = list(self.behaviors.keys())[az.index(enteredTech)]
        selectedTech = self.behaviors[str(list(self.behaviors.keys())[az.index(enteredTech)])]


        #prompts user to select an intervention related to the selected technology, saves response as a variable
        print("Which intervention into " + str(list(self.behaviors.keys())[az.index(enteredTech)]) + " should be in focus? [Out of the following list, pick one concrete intervention for micro-level analysis.] You may select: ")
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
        spPrompt = input("Within an organization, what are the existing practices affected by " + str(self.focusIntervention) + " :")
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

#function to report contents of the micro-level analysis
    def reportMicroAnalysis(self):
        print("The current Micro-level Analysis contains " + str(len(microAnalysis.allInterventions)) + " interventions: ")
        print(str(microAnalysis.allInterventions.keys())[12:-3])
        print("The current focus technology is " + str(microAnalysis.selectedTech) + ".")
        print("The current focus intervention is " + str(microAnalysis.focusIntervention) + ".")
        print(str(microAnalysis.focusIntervention) + " is associated with the following practices, which each have associated elements and carriers):")
        for p in list(microAnalysis.socialPractices.keys()):
            print("Social Practice: " + str(p) + " has the following elements:")
            print("Meanings: " + str(microAnalysis.socialPractices[p]['elements']['meanings']))
            print("Competencies: " + str(microAnalysis.socialPractices[p]['elements']['competencies']))
            print("Materials: " + str(microAnalysis.socialPractices[p]['elements']['materials']))
            print("Carriers: " + str(microAnalysis.socialPractices[p]['carriers']))
            print("\n")

#defines a class to contain the synthetic analysis
class syntheticAnalysis:
    def __init__(self, macro, micro):
        self.macro = macro
        self.micro = micro
        self.synthesis = {}

#defines a function that will prompt user for entries to complete synthetic analysis
    def populateSyntheticAnalysis(self):
        self.synthesis['Element Changes'] = input("How does one or multiple elements of the practice have to change in order to achieve the behavioral change?")
        self.synthesis['Process Changes'] = input("What are existing (organizational) processes that can be leveraged to achieve the desired change on the level of the elements?")
        self.synthesis['Lead Carriers'] = input("Who are the high-potential carriers of practice who can spearhead this recalibration of the social practice?")

# Testing and execution variables:
#aaa = MacroLevel("AAA2022", "FTC", "US")
#aaa.tech = {'facial recognition': {}, 'web tracking': {}}
#aaa.int = {'facial recognition': ['sociotechnical audit', 'informed consent'],
#           'web tracking': ['user opt-out', 'deanonymization']}
#aaa.behavior = {'facial recognition': [
#    {'sociotechnical audit': ['expose data to outside researchers', 'incorporate audit feedback into product']},
#    {'informed consent': ['edit front-end webcopy', 'adapt database to record user consent']}], 'web tracking': [{
#                                                                                                                     'user opt-out': [
#                                                                                                                         'edit front-end functionality to enable opt-out',
#                                                                                                                         'blind web tracking database to users who opt out']},
#                                                                                                                 {
#                                                                                                                     'deanonymization': [
#                                                                                                                         'design anonymizing protocol',
#                                                                                                                         'audit anonymizing protocol',
#                                                                                                                         'red-team anonymizing protocol']}]}
#
#gdpr = MacroLevel("GDPR", "Council of Europe", "EU")

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

#prompt for additional technologies - uncomment to add this functionality to the runtime script
#print("Would you like to add any additional technologies, interventions, or behaviors at this time?")
#print("press 'Enter' to skip adding additional items at this time")
#new_tech = input("Y?")
#if new_tech == "Y" or new_tech == "y":
#    print("The regulation currently being analyzed is " + str(regulationInput))
#    regAnalysis.add_technology()
#    regAnalysis.add_intervention()
#    regAnalysis.update_behaviors()
#else:
#    pass

#prompt for user to conduct micro-level analysis
print("Would you like to conduct a micro-level analysis now?")
new_micro = input("Y/N?")
if new_micro == "Y" or new_micro == "y":
    microAnalysis = MicroLevel(regAnalysis)
    microAnalysis.selectIntervention()
    microAnalysis.enterSocialPractice()
    microAnalysis.allInterventions[microAnalysis.focusIntervention[1:-1]] = {'intervention behaviors': microAnalysis.interventionBehaviors, 'social practices': microAnalysis.socialPractices}
else:
    pass

#prompt to conduct subsequent micro-level analyses - uncomment for functionality
#
#new_micro = input("Would you like to conduct another micro-level analysis now (Y/N)?")
#while new_micro == "Y" or new_micro == "y":
#    microAnalysis.selectIntervention()
#    microAnalysis.enterSocialPractice()
#    microAnalysis.allInterventions[microAnalysis.focusIntervention[1:-1]] = {
#        'intervention behaviors': microAnalysis.interventionBehaviors,
#        'social practices': microAnalysis.socialPractices}
#    new_micro = input("Would you like to conduct another micro-level analysis now (Y/N)?")
#else:
#    pass

#prompt user to conduct synthetic analysis
print("Would you like to conduct a synthesis, based on the micro-level analysis, now?")
new_synth = input("Y/N?")
if new_synth == "Y" or new_synth == "y":
    synth = syntheticAnalysis(regAnalysis, microAnalysis)
    syntheticAnalysis.populateSyntheticAnalysis(synth)

#compile analyses into single dictionary
full_analysis = {}

#create a temporary dictionary to extract behaviors
behaviors = {}

#pull behaviors for each intervention out, so they are not bucketed by technology
for i in regAnalysis.behavior:
    for j in regAnalysis.behavior[i]:
        behaviors[list(j.keys())[0]] = j[list(j.keys())[0]]

#populate dict with all three analyses
full_analysis['Macro-level Analysis'] = {'Regulation': regAnalysis.reg, 'Authority': regAnalysis.auth, 'Territory': regAnalysis.terr, 'Technologies': list(regAnalysis.tech.keys()), 'Technology Definitions': regAnalysis.definition, 'Technology Interventions': regAnalysis.int, 'Intervention Behaviors': behaviors}
full_analysis['Micro-level Analysis'] = {'Selected Technology': microAnalysis.selectedTech, 'Focus Intervention': microAnalysis.focusIntervention, 'Focus Intervention Behaviors': microAnalysis.interventionBehaviors, 'Social Practices': microAnalysis.socialPractices}
full_analysis['Synthetic Analysis'] = synth.synthesis


#JSON Dump of completed PCF

#prompt user for filename
filename = input("Enter a file name for exporting a json of the completed analysis:")

if filename != "":
    with open(str(filename) + ".json", "w") as writefile:
        json.dump(full_analysis, writefile)
else:
    pass

print("Thank You!")