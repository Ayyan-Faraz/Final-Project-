import tkinter as tk
from tkinter import *
from tkinter import messagebox


def identify_virus():
    symptoms_str = symptoms_str_entry.get().lower().strip()    

    if not symptoms_str:

        messagebox.showinfo("Virus Identification", "No symptoms provided. Please enter your symptoms.")
        return

    virus_info = identify_virus_from_symptoms_str(symptoms_str)

    messagebox.showinfo("Virus Identification", virus_info)



def identify_virus_from_symptoms_str(symptoms_str):
    if 'fever' in symptoms_str or 'cough' in symptoms_str  or 'runny nose' in symptoms_str:
        return ("You may have Flu\n\n"
                "Causes of the Flu:\nTransmission: Influenza viruses spread from person to person through respiratory droplets when an infected person coughs, sneezes, or talks. You can also get the flu by touching a surface or object that has the virus on it and then touching your mouth, nose, or eyes.\n"
                "Treatment of the Flu:\nAntiviral Medications, Rest")

    elif 'sneezing' in symptoms_str or 'sore throat' in symptoms_str or 'cough' in symptoms_str:
       return("You may have Rhinovirus (Common Cold)\n"
             "\nCause\n"
             "Rhinoviruses are highly contagious and spread through respiratory droplets when an infected person coughs or sneezes. They can also spread by touching contaminated surfaces and then touching the nose or mouth."
             "\nTreatment:\n"
             "Stay Hydrated: Drinking plenty of fluids, such as water, herbal teas, and clear broths, helps keep the body hydrated and can help loosen mucus.")
       
    



    elif 'fever' in symptoms_str or 'difficulty breathing' in symptoms_str or 'sore throat' in symptoms_str:
        return("You may have Parainfluenza Virus"
               "\nCauses:\nFrom someone nearby coughing or sneezing. Very small (microscopic) droplets containing HPIV can get into your nose or mouth directly through the air. They can also get on your hands, then get into your nose or mouth when you touch your face."
               "\nTreatment:\n Medications: Over-the-counter pain relievers such as acetaminophen (Tylenol) or ibuprofen (Advil, Motrin) can help reduce fever and alleviate discomfort. However, aspirin should not be given to children or teenagers with viral infections due to the risk of Reye's syndrome.")

    elif 'rash' in symptoms_str or 'sore throat' in symptoms_str or 'red eyes' in symptoms_str:
        return("You may have Measles Virus"
               "\nCauses\n Sharing drinks or food with someone with measles.\nShaking hands, holding hands or hugging someone with measles.\nTouching a surface containing the virus and then touching your mouth, nose or eyes."
               "\nTreatment:\n Prevention: The most effective way to prevent measles is through vaccination. The measles, mumps, and rubella (MMR) vaccine is highly effective in preventing measles and is typically administered in two doses")


    elif 'loss of taste' in symptoms_str or 'fever' in symptoms_str or 'difficulty breathing' in symptoms_str:
        return("You may have Coronaviruses"
               "\nCauses\nVirus Origin:\n COVID-19 is caused by the SARS-CoV-2 virus, which is a novel coronavirus that emerged in late 2019 in Wuhan, China.\nTransmission:\n The virus primarily spreads through respiratory droplets when an infected person coughs, sneezes, or talks. It can also spread by touching surfaces contaminated with the virus and then touching the face, especially the mouth, nose, or eyes."
               "\nMild Cases:\n Most cases of COVID-19 are mild and can be managed at home. Treatment typically involves rest, staying hydrated, and taking over-the-counter medications to alleviate symptoms_str like fever and pain (e.g., acetaminophen).\nSevere Cases: In severe cases where individuals experience difficulty breathing, persistent chest pain, confusion, bluish lips or face, or other severe symptoms_str, medical attention should be sought immediately. Hospitalization may be necessary, and treatment might include supplemental oxygen, mechanical ventilation, and medications such as corticosteroids and antiviral drugs.\nVaccination: Vaccines against COVID-19 have been developed and are being administered globally to prevent infection and reduce the severity of the disease. Vaccination campaigns aim to achieve herd immunity and control the spread of the virus.")



       

    elif 'muscle pain' in symptoms_str or ('joint pain' in symptoms_str or 'rash' in symptoms_str):
        return("You may have Dengue Virus"
               " \nCauses: \n When a mosquito infected with the dengue virus bites a person, the virus enters the bloodstream, leading to infection."
               " \nTreatment: \nFluid Replacement: Adequate fluid intake is crucial to prevent dehydration, especially in cases of severe dengue. Oral rehydration solutions or intravenous fluids may be administered to maintain hydration.")

        
    elif 'muscle pain' in symptoms_str or ('headache' in symptoms_str or 'rash' in symptoms_str):
        return("You may have Chikungunya Virus"
               " \nCauses: \nChikungunya virus is primarily transmitted to humans through the bite of infected Aedes mosquitoes, particularly Aedes aegypti and Aedes albopictus. These mosquitoes are daytime biters"
               " \nTreatment\n:Symptomatic Relief: Using topical treatments or creams for rashes and taking antihistamines for itching can provide relief from skin-related symptoms_str.")


    elif 'headache' in symptoms_str or ('cough' in symptoms_str or 'shortness of breath' in symptoms_str):
        return("You may have Hantavirus"
               " \nCauses:\n Hantavirus can affect anyone who comes in contact with infected mouse or rat poop, pee or spit. Cases occur throughout the world."
               "\n Treatment \n in severe cases of hantavirus pulmonary syndrome (HPS), patients may require hospitalization and intensive care.\n Supportive measures may include oxygen therapy to help with breathing difficulties and intravenous fluids to maintain hydration.")


    elif 'weakness' in symptoms_str or ('muscle aches' in symptoms_str or 'headache' in symptoms_str):
        return("You may have West Nile Virus"
               "\n Causes \n infected mosquitos transmit West Nile virus. They usually get the virus by biting an infected bird . The virus multiplies inside the mosquito, and it’s transmitted to you  when it bites you. "
               "\nTreatment \n For individuals with mild symptoms_str, supportive care is often recommended, which may include rest, over-the-counter pain relievers to reduce fever and relieve symptoms_str, and staying hydrated. In more severe cases, where the virus causes neuroinvasive disease, such as encephalitis or meningitis, hospitalization and supportive therapy may be required. ")


    elif 'fatigue' in symptoms_str or ('fever' in symptoms_str or 'swollen lymph nodes' in symptoms_str):
        return("You may have Immunodeficiency Virus"
               "Causes\nHIV is a virus that attacks the immune system, specifically targeting CD4 cells, which are a type of white blood cell that plays a crucial role in the body's defense against infection. HIV weakens the immune system over time, making it difficult for the body to fight off infections and diseases."
               "\n Treatment\n HIV is treated with a combination of medicines (pills) taken by mouth every day. This combination of pills is called antiretroviral therapy (ART).")


    elif 'nausea' in symptoms_str or 'vomiting' in symptoms_str or 'diarrhea' in symptoms_str:
        return("You may have Rift Valley Fever "
               "\n Causes: \n Animal Contact: Humans can also get infected through direct contact with blood, body fluids, or tissues of infected animals, particularly during slaughtering, butchering, or handling infected animals.Consumption of Contaminated Products: Drinking unpasteurized milk from infected animals can also transmit the virus to humans."
               "\n Treatment \n Symptomatic Treatment: Fever, pain, and other symptoms_str can be managed with antipyretics (fever-reducing medications) such as acetaminophen or ibuprofen.\n Rest and Hydration: Patients are advised to get plenty of rest and stay well-hydrated to help the body fight off the infection and maintain proper fluid balance.")



    elif 'fever' in symptoms_str or 'headache' in symptoms_str or 'swollen salivary glors' in symptoms_str:
        return("You may have Mumps Virus"
               "\n Causes: \n The mumps virus is spread through respiratory droplets, such as saliva, from an infected person. It can spread through:\nCoughing\nSneezing\n\nSharing utensils or cups with infected individuals"
               "Treatment: \n Vaccination: The best way to prevent mumps is through vaccination. The measles, mumps, and rubella (MMR) vaccine is highly effective in preventing mumps infection. ")

        
    elif 'headache' in symptoms_str or ('confusion' in symptoms_str or 'seizures' in symptoms_str):
        return("You may have Herpes Simplex Virus (HSV)"
               "\n Causes: \n HSV is highly contagious and is typically spread through direct contact with infected skin or mucous membranes. "
               "Treatment: \n Antiviral Medications: Doctors often prescribe antiviral medications to manage HSV outbreaks. These medications, such as acyclovir, valacyclovir, and famciclovir, can help reduce the severity and duration of symptoms_str when taken during outbreaks.\n creams and ointments containing docosanol or lidocaine, can help relieve pain, itching, and discomfort associated with HSV sores.")


    elif 'anxiety' in symptoms_str or ('confusion' in symptoms_str or 'hydrophobia' in symptoms_str):
        return("You may have Rabies Virus"
               "\n Causes: \nRabies is caused by the rabies virus, which is primarily transmitted through the saliva of infected animals. The virus can enter the body through a bite or scratch from an infected animal, allowing the virus to spread to the central nervous system."
               "Treatment: \n Rabies Vaccine: The rabies vaccine is given in a series of shots over a specific time frame. The vaccine helps your body develop immunity to the rabies virus.\n Wound Care: Proper wound care, including washing the wound thoroughly with soap and water, can help reduce the risk of infection.")



    elif 'deafness' in symptoms_str or 'eye defects' in symptoms_str:
        return("You may have German Measles"
               "\n Causes: \n German measles is caused by the rubella virus, which is transmitted through respiratory droplets when an infected person coughs or sneezes.It can also spread through direct contact with respiratory secretions or the rash of an infected person."
               "\nTreatment: \n German measles often resolves on its own without specific medical treatment in healthy individuals.")


    elif 'neck stiffness' in symptoms_str or ('confusion' in symptoms_str or 'tremors' in symptoms_str):
        return("You may have Encephalitis Virus"
               "\n Causes: \n The most common cause is when certain viruses affect your brain.That usually happens if you have the herpes simplex virus (HSV). But you can develop encephalitis if you have certain infectious diseases or other viruses."
               "Treatment: \nSupportive Care: Supportive care is essential to manage symptoms_str and provide comfort to the patient. This may include measures such as hydration, fever reduction, and pain management.\n Hospitalization: Severe cases of viral encephalitis may require hospitalization, especially if the patient experiences seizures, altered consciousness, or other neurological symptoms_str that need close monitoring and medical intervention.")



    elif 'redness' in symptoms_str or 'itching' in symptoms_str or 'pain' in symptoms_str:
        return("You may have Pink Eye Virus"
               "Cause: Bacterial infections can lead to pink eye."
               "Medication: Typically resolves on its own without specific treatment."
               "\nHowever, the following measures may be helpful:"
               "Use cool compresses to soothe the eyes or reduce discomfort."
               "Practice good hygiene, including frequent horwashing or avoiding touching or rubbing the eyes."
               "\nAvoid sharing towels, pillowcases, or eye makeup with others to prevent spreading the virus. ")

    elif 'pain' in symptoms_str or 'swelling' in symptoms_str or 'tears' in symptoms_str:
        return("You may have Stye"
               "Cause: Infection of an eyelash follicle."
               "Treatment: Warm compresses or sometimes antibiotics.")

    elif 'redness' in symptoms_str or 'blurred vision' in symptoms_str:
        return("You may have Uveitis"
               "Cause: Inflammation of the uvea (middle layer of the eye)"
               "Treatment: Eye drops, antiviral medications, or surgery (in severe cases)")

    elif 'redness' in symptoms_str or 'swelling' in symptoms_str or 'pain' in symptoms_str:
        return("You may have Cellulitis"
               "Cause: Infection of the skin around the eye."
               "Treatment: Antibiotics, rest, or elevation of the affected area")

    elif 'pain' in symptoms_str or 'discharge' in symptoms_str:
        return("You may have Dacryocystitis"
               "Cause: Infection of the tear sac due to blocked tear ducts."
               "Treatment: Warm compresses, antibiotics, or sometimes surgical intervention")

    elif 'dry eyes' in symptoms_str or 'redness' in symptoms_str or 'itching' in symptoms_str:
        return("You may have Blepharitis"
               "Causes of Blepharitis:"
               "Allergies: Allergic reactions to environmental allergens, such as pollen, dust, or pet dorer, can lead to blepharitis")


    elif 'itching' in symptoms_str or 'redness' in symptoms_str:
        return("You may have ECZEMA:"
        "\nCause: Combination of genetic, immune system, or environmental factors." 
        "\nTreatment: Moisturizing the skin regularly, avoiding triggers, using topical corticosteroids or other anti-inflammatory medications, or practicing good skincare habits.")

    elif 'formation of pimples' in symptoms_str or 'blackheads' in symptoms_str or 'cysts on the face':
        return("You may have ACNE:"
               "\nCause: including excess oil production, clogged hair follicles, bacteria (Propionibacterium acnes), hormonal changes, or inflammation.."
               "\nTreatment: Oral medications such as antibiotics, hormonal therapies (for women), or isotretinoin may be prescribed for severe cases.")
    
    elif 'persistent redness' in symptoms_str or 'flushing' in symptoms_str or 'visible blood vessels':
        return("You may have ROSACEA:"
               "\nCause: The exact cause of rosacea is unknown, but it may involve genetic, environmental, vascular, or immune system factors."
               "\nTreatment:  Avoiding triggers such as sun exposure, alcohol, spicy foods, or stress. Topical medications (metronidazole, azelaic acid), oral antibiotics, or laser therapy may be prescribed to reduce redness or inflammation.")

    elif 'itching' in symptoms_str or 'redness' in symptoms_str or 'inflammation':
       return("You may have CONTACT DERMATITIS:"
              "\nCause: Contact dermatitis is caused by direct contact with substances that irritate the skin (e.g., detergents, chemicals) or trigger an allergic reaction (e.g., nickel, latex)." 
              "\nTreatment: Avoiding triggers, applying topical corticosteroids or antihistamines to relieve symptoms_str, or using emollients or barrier creams to protect the skin.")

    elif 'thickness' in symptoms_str or 'redness' in symptoms_str or 'scaly patches':
       return("You may have PSORIASIS:"
              "\nCause: Psoriasis is an autoimmune disorder where the immune system mistakenly attacks healthy skin cells, leading to rapid turnover of skin cells or inflammation." 
              "\nTreatment: Topical corticosteroids, vitamin D analogs, retinoids, or moisturizers. In severe cases, phototherapy (light therapy), oral medications, or biologic drugs may be prescribed.")
        


    elif "genital warts" in symptoms_str or "abnormal vaginal bleeding" in symptoms_str or "bowel habits":
       return("you may be suffering from Human papillomavirus"
              "Cause:transmitted thruogh skin-to-skin contact"
              "Cure:there is non cure for this virus but treatments are available for related symptoms_str")
        
    elif "loss of apetite" in symptoms_str or "fatigue" in symptoms_str:
       return("you may be suffering from Varicella-zoster virus"
              "cause:it is transmitted direct contact with fluid from fromthe blisters of an infected person"
              "cure:Antiviral medicines")
        
    elif "red watery eyes"in symptoms_str or "small white spots inside the mouth":
       return("you may be suffering from measles virus"
              "The measles virus is caused by infection with the measles virus"    
              "Cure:There is no specific cure for measles, but the measles vaccine is highly effective in preventing the disease. Treatment focuses on managing symptoms_str or complications, such as fever or respiratory infections.")

    elif " muscle aches"in symptoms_str or "sore throat"in symptoms_str or " headache":
           return("you may be suffering from Coxsackievirus"
                  "Cause:Coxsackievirus is caused by infection with the Coxsackievirus, a type of enterovirus belonging to the Picornaviridae family. It is transmitted through close contact with an infected person or by touching contaminated surfaces"
                  "Cure:There is no specific cure for Coxsackievirus infections, so treatment focuses on relieving symptoms_str or providing supportive care.")
    

    elif "vomitting" in symptoms_str or "internal or external bleeding" in symptoms_str or "intense weakness":
       return("you may be suffering from Ebola virus"
              "cause:the ebola virus is believed to be animal borne,with bats bieng the most likely reservoir"
              "cure:There is no specific cure for Ebola virus disease (EVD) approved by the FDA. However, supportive care such as maintaining electrolyte balance, providing oxygen therapy, or treating other infections can improve survival")

    elif "Nausea or vomiting"in symptoms_str or "Abdominal pain" in symptoms_str or "Facial swelling" in symptoms_str or "Mucosal bleeding":
        return("you may be suffering from lassa virus"
               "cause:Lassa virus is caused by infection with the Lassa virus, which is primarily transmitted to humans through contact with food or household items contaminated with rodent urine or feces."
               "cure::There is no specific cure for Lassa fever, but early supportive care or antiviral treatment can improve outcomes.")

    elif "stiff neck" in symptoms_str or "coma" in symptoms_str or "paralysis" in symptoms_str or "body aches":
       return("you may be suffering from west nile virus"
              "cause:it is transmitted through the bites of infected Mosquitoes"
              "cure:no cure but depends upon symptoms_str")

    elif "organ failure" in symptoms_str or "bleeding from nose,mouth or eyes" in symptoms_str or "jaundice" in symptoms_str or "red eyes,face or tounge":
       return("you amy be suffering from yellow fever"
              "cause:it is caused by the yellow fever virus,which is primarily transmitted to humans through bite of infected mosquitoes"
              "cure:by vaccination")

    elif "joint or mucle pain" in symptoms_str or "difficulty breathing" in symptoms_str or "cold or clammy skin":
       return("you may be suffering from dengue virus"
              "cause:it is caused by dangue virus"
              "cure:there is no treatment but supportive care such as hydration or pain relief ,can help manage manage symptoms_str")




    elif "sneezing" in symptoms_str or  "blood in the urine" in symptoms_str or "frequent urination" in symptoms_str or "rash":
       return("you may be suffering from Adenovirus"
              "cause:it is spread through close personal contact,respiratory droplets,or conatct eith conataminated surfaces"
              "cure:there is no specific antiviral treatment so treatment focuses on managing symptoms_str ")

    elif "swollen glor" in symptoms_str or "flu-like symptoms_str" in symptoms_str or "pneumonia" in symptoms_str or "hepatitis":
       return("you may be suffering from Cytomegalovirus"
              "cause:it is caused by close-conatact with body fluids,such as salive,urinr,organ transplantation"
              "cure:antiviral medicines can help manage symptoms_str or reduce the risk of complication especially in weakened immune system")

    elif "blood in urine" in symptoms_str or "painful urination" in symptoms_str or "high blood pressure" in symptoms_str or "pain in the side or back":
       return("you may be suffering from BK virus"
              "cause:BK virus is a common virus that usually causes asymptomatic infection but can reactivate in people with weakened immune system"
              "cure:there is no specific antiviral treatment but reducing immunosuppression in transplant reciepients or managing symptoms_str can help ")

    elif "infection" in symptoms_str or "itching sensation" in symptoms_str or "burning during urination" in symptoms_str or "fever":
       return("you may be suffering from Herpes simplex virus "
               "cause:it is transmitted through direct contact with infected skin or mucuos membranes"
               "cure:there is no cure but antiviral medicines can help or reduce the frequency of outbreaks")


               



    elif "inflammation of heart" in symptoms_str or  "headache" in symptoms_str or "chest pain" in symptoms_str or "shortness of breath":
       return("you may be suffering from Enterovirus"
              "cause:spread through close contact with infected person's respiratory secretion,feces,or conatminated surfces "
              "cure:there is no specific antiviral treatment so treatment focuses on managing symptoms_str ")

    elif "anemia" in symptoms_str or "joint pain" in symptoms_str or "arthritis" in symptoms_str or "immune system disorders":
       return("you may be suffering from Parvovirus B19"
              "cause:it is caused by close-conatact or from person to person"
              "cure:antiviral medicines can help manage symptoms_str or reduce the risk of complication especially in weakened immune system")

    elif "High Fever" in symptoms_str or "Rash" in symptoms_str or "Swollen Glors:" in symptoms_str or "Decreased Appetite":
       return("you may be suffering from human herpesvirus 6"
              "cause:Human herpesvirus 6 (HHV-6) is a virus that infects most people during childhood, causing roseola, a common illness characterized by high fever or rash."
              "cure:There is no specific cure for human herpesvirus 6 (HHV-6), but treatment focuses on managing symptoms_str or complications. ")

    elif "Jaundice (yellowing of the skin or eyes" in symptoms_str or "diarrhea" in symptoms_str or "Muscle aches" in symptoms_str or "fever":
       return("you may be suffering from Cytomegalovirus "
              "cause:Cytomegalovirus (CMV) is caused by infection with the cytomegalovirus, which is a member of the herpesvirus family."
              "cure:Antiviral medications can help manage symptoms_str and reduce complications, but there is no cure for cytomegalovirus (CMV) infection.")

    else:
        return "No virus identified for the provided symptoms_str."

    if not any(word in symptoms_str for word in ['Fever', 'Cough', 'Runny nose', 'Sneezing', 'Sore throat', 'Difficulty breathing', 'Rash', 'Red eyes', 'Loss of taste', 'Muscle pain', 'Joint pain', 'Headache', 'Weakness', 'Nausea', 'Vomiting', 'Diarrhea', 'Loss of appetite', 'Fatigue', 'Swollen lymph nodes', 'Swollen salivary glands', 'Hydrophobia', 'Confusion', 'Seizures', 'Tremors', 'Redness', 'Itching', 'Pain', 'Swelling', 'Tears', 'Dry eyes', 'Blurred vision', 'Formation of pimples', 'Blackheads', 'Cysts on the face', 'Persistent redness', 'Flushing', 'Visible blood vessels', 'Thickness', 'Scaly patches', 'Itching sensation', 'Burning during urination', 'Facial swelling', 'Inflammation', 'Red watery eyes', 'Small white spots inside the mouth', 'Stiff neck', 'Coma', 'Paralysis', 'Body aches', 'Jaundice', 'Muscle aches', 'High blood pressure', 'Blood in urine', 'Painful urination', 'Organ failure', 'Bleeding from nose, mouth, or eyes', 'Mucosal bleeding', 'Anemia', 'Arthritis', 'Immune system disorders']):
        messagebox.showinfo("Virus Identification", "No virus identified for the provided symptoms_str.")
        return     




root = tk.Tk()
root.title("Genius Detector: Your Virtual Health Companion")
root.configure(bg='red')

#input_frame = tk.Frame(root, width=60, height=10)
#input_frame.pack(padx=20, pady=20)


choice_var = tk.StringVar(root)

tk.Label(root, text="Enter your symptoms:",width=60, height=3, font=('Times New Roman', 15, 'bold')).pack()




symptoms_str_entry = tk.Entry(root)
symptoms_str_entry.pack(pady=20)

def suggest_symptoms_str():
    selected_choice = choice_var.get()
    suggested_symptoms_str = ""
    suggested_symptoms_str = "\n⦿Fever\n ⦿Cough\n ⦿Runny nose\n ⦿Difficulty breathing\n ⦿Joint pain\n ⦿Rash\n ⦿Headache\n"
    
    messagebox.showinfo("Suggested symptoms are", f"Some suggested symptoms are: {suggested_symptoms_str}")

tk.Button(root, text="Suggest symptoms",width=25, height=3, font=('Times New Roman', 13, 'bold'), command=suggest_symptoms_str).pack()

identify_button = tk.Button(root, text="Identify Virus",width=45, height=3, font=('Times New Roman', 13, 'bold'), command=identify_virus)
identify_button.pack()

root.mainloop()
