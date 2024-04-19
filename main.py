from PIL import Image
import json 
import requests 
from streamlit_lottie import st_lottie 
import streamlit as st

st.sidebar.title('Navigation')
nav = st.sidebar.radio('Go to: ',('Home', 'Landmines','FLC Sensor', 'Predictions', 'About'))
if nav=="Home":
    st.title("Land Mine Identification")
    st.image("pic1.jpg")
    st.write('''A landmine is a type of explosive device designed to be concealed underground or on the surface of the ground. They are typically used in warfare to target enemy personnel or vehicles, often causing severe injury or death upon detonation. Landmines can vary in size, shape, and triggering mechanisms, but they all share the common characteristic of being activated by pressure or proximity.

Landmines pose significant humanitarian concerns long after conflicts have ended, as they remain active and deadly even decades after they are deployed. They can cause indiscriminate harm to civilians, as well as impede the post-conflict recovery and development of affected regions by rendering land inaccessible for agriculture, infrastructure development, and resettlement.

Efforts to address the global landmine crisis have included mine clearance operations, risk education programs to educate communities about the dangers of landmines, and advocacy for international treaties such as the 1997 Mine Ban Treaty (also known as the Ottawa Treaty), which aims to eliminate the production, stockpiling, and use of anti-personnel landmines worldwide. Despite these efforts, millions of landmines remain active in various conflict-affected regions around the world, posing ongoing threats to civilian populations.''')

if nav=="Landmines":
    st.title("Different type of Landmines")
    st.subheader("1. Anti-Tank Landmines")
    st.write('''Anti-tank landmines are powerful explosive devices specifically designed to immobilize or destroy armored vehicles, particularly tanks. These mines are a critical component of military defenses and offensive strategies, aimed at impeding enemy movement and causing significant damage to enemy vehicles. Here's a detailed overview of anti-tank landmines:

### Design and Construction:
1. **Explosive Payload**: Anti-tank landmines typically contain a large amount of high-explosive material, such as TNT (trinitrotoluene) or RDX (cyclotrimethylenetrinitramine), capable of inflicting severe damage to armored vehicles.
  
2. **Pressure or Magnetic Activation**: These mines are activated by either pressure or magnetic influence. Pressure-sensitive mines detonate when sufficient weight or pressure is applied to the mine, usually by the weight of a vehicle. Magnetic influence mines are triggered by the disturbance of the Earth's magnetic field caused by the presence of a metal object, such as a tank.

3. **Detonation Mechanism**: Anti-tank mines employ various detonation mechanisms, including direct contact detonation, tilt-rod mechanisms, or remote detonation via command wire or radio frequency signals.

4. **Case Design**: The outer casing of anti-tank landmines is typically constructed from metal, plastic, or composite materials. This casing protects the internal components from environmental factors and facilitates the transfer of explosive force towards the target.

### Deployment and Tactics:
1. **Strategic Placement**: Anti-tank mines are strategically deployed in key defensive positions, such as chokepoints, roadways, bridges, or areas with high enemy vehicle traffic. They may also be laid in minefields to create barriers or deny access to specific areas.

2. **Concealment**: To maximize their effectiveness, anti-tank mines are often concealed or buried beneath the surface to evade detection by enemy forces. Camouflage techniques may be employed to blend the mines with the surrounding terrain and make them difficult to spot.

3. **Integration with Defensive Systems**: Anti-tank mines are frequently used in conjunction with other defensive measures, such as barbed wire obstacles, trenches, and anti-tank obstacles (e.g., dragon's teeth), to create layered defenses and impede enemy advancements.

4. **Ambushes and Offensive Operations**: In offensive operations, anti-tank mines may be employed as part of ambush tactics to target and immobilize enemy armored columns. They can also be used to disrupt enemy logistics and supply routes, causing delays and confusion.

### Impact and Risks:
1. **Vehicle Damage**: Anti-tank landmines pose a significant threat to armored vehicles, causing catastrophic damage to their hulls, tracks, and critical components. A single well-placed mine can immobilize or destroy even the most heavily armored tanks.

2. **Casualties and Collateral Damage**: In addition to their intended targets, anti-tank mines can also inflict casualties on dismounted infantry and civilians who inadvertently trigger them. The indiscriminate nature of these weapons presents a grave risk to both military personnel and civilian populations.

3. **Long-term Hazard**: Many anti-tank mines are designed to remain active for extended periods, posing a persistent threat long after the cessation of hostilities. These "legacy mines" continue to cause casualties and hinder post-conflict reconstruction efforts, making mine clearance and demining operations a challenging and costly endeavor.

### International Regulations and Humanitarian Concerns:
1. **Landmine Ban Treaty**: The use, production, and stockpiling of anti-personnel landmines are prohibited under the Ottawa Treaty (also known as the Mine Ban Treaty) of 1997. While this treaty does not explicitly cover anti-tank mines, there are ongoing efforts to address the humanitarian impact of all types of landmines.

2. **Clearance and Demining**: Humanitarian organizations and demining agencies work tirelessly to clear landmines and unexploded ordnance from affected areas, reducing the risk to civilians and enabling the safe return of displaced populations. Demining efforts often involve manual clearance, mechanical clearance, and the use of mine-detecting technologies.

3. **Victim Assistance**: Efforts to assist landmine survivors and affected communities include medical care, rehabilitation services, psychosocial support, and socioeconomic assistance. These initiatives aim to address the long-term physical, emotional, and economic consequences of landmine accidents.

In summary, anti-tank landmines are potent weapons designed to counter armored vehicles and impede enemy movements on the battlefield. However, their widespread deployment poses significant risks to military personnel, civilians, and post-conflict recovery efforts. Addressing the humanitarian impact of landmines requires concerted international efforts to mitigate their effects, clear affected areas, and provide assistance to survivors and affected communities.''')

    st.subheader("2. Anti-personnel landmines")
    st.write('''Anti-personnel landmines (APLs) are small explosive devices designed to injure or kill individuals on foot, primarily targeting soldiers, civilians, and humanitarian personnel. Unlike anti-tank landmines, which focus on armored vehicles, APLs are intended to inflict casualties on personnel. Here's a detailed overview of anti-personnel landmines:

### Design and Construction:
1. **Small Size**: Anti-personnel landmines are typically compact and lightweight, making them easy to deploy and conceal. They can vary in size from as small as a hockey puck to larger devices resembling small boxes.

2. **Fragmentation or Blast Effect**: APLs are usually equipped with an explosive charge that, upon detonation, generates a blast wave and releases shrapnel or fragments. The blast effect can cause severe injuries to anyone in close proximity to the mine.

3. **Various Activation Mechanisms**: Anti-personnel landmines can be activated through pressure, tripwires, or remote control mechanisms. Some models feature sensitive sensors that detonate the mine upon detecting nearby movement or vibration.

4. **Non-metallic Construction**: To evade detection by metal detectors, some APLs are constructed using non-metallic materials such as plastic or composite materials. This makes them particularly challenging to locate and remove during demining operations.

### Deployment and Tactics:
1. **Scattered Deployment**: APLs are often dispersed indiscriminately across areas of military significance, including defensive positions, borders, roads, and civilian areas. They may also be deployed as part of defensive perimeters around military installations or strategic assets.

2. **Concealment and Booby Traps**: APLs are concealed using various methods to avoid detection, such as burying them underground, hiding them in vegetation, or disguising them as harmless objects. Some mines are set as booby traps, attached to tripwires or pressure-sensitive mechanisms to detonate when triggered.

3. **Area Denial**: APLs are used to deny access to enemy forces and disrupt their movements. By creating a hazardous environment, they force adversaries to navigate carefully or divert from planned routes, slowing their progress and making them vulnerable to attack.

4. **Psychological Impact**: Beyond their physical effects, APLs instill fear and uncertainty among civilian populations, inhibiting normal activities such as farming, travel, and access to essential services. This psychological impact can have far-reaching consequences on communities affected by landmines.

### Impact and Risks:
1. **Civilian Casualties**: APLs pose a grave threat to civilians, particularly in post-conflict settings where they remain hidden in the ground for years or even decades. Accidental detonations by unsuspecting individuals, including children, result in severe injuries, amputations, and fatalities.

2. **Long-term Hazard**: Many APLs are designed to remain active for extended periods, contributing to the persistence of mine contamination long after the cessation of hostilities. These "legacy mines" continue to claim lives and hinder socioeconomic development in affected regions.

3. **Environmental Damage**: The presence of APLs in the environment can cause ecological damage, contaminating soil and water sources and disrupting ecosystems. Clearance and demining operations must consider environmental factors to minimize the impact of landmine contamination on biodiversity and natural resources.

### International Regulations and Humanitarian Concerns:
1. **Ottawa Treaty**: The Ottawa Treaty (Mine Ban Treaty) of 1997 prohibits the use, production, stockpiling, and transfer of anti-personnel landmines. The treaty aims to eliminate the humanitarian impact of APLs and promote mine clearance, victim assistance, and mine risk education.

2. **Mine Clearance and Demining**: Humanitarian organizations and demining agencies conduct clearance operations to remove APLs and other explosive remnants of war from affected areas. These efforts involve manual clearance, mechanical clearance, and the use of mine-detecting technologies to ensure the safe return of land to civilian use.

3. **Victim Assistance and Mine Risk Education**: Efforts to assist landmine survivors and affected communities include medical care, rehabilitation services, psychosocial support, and socioeconomic assistance. Mine risk education programs raise awareness about the dangers of landmines and teach safety measures to prevent accidents.

In conclusion, anti-personnel landmines represent a persistent threat to civilian populations, posing significant humanitarian, environmental, and socioeconomic challenges in conflict-affected regions. Addressing the impact of APLs requires international cooperation, adherence to disarmament treaties, and sustained efforts to clear contaminated areas, assist survivors, and educate communities about the dangers of landmines.''')

    st.subheader("3. Booby trap anti-personnel landmines")
    st.write('''Booby trap anti-personnel landmines (Booby trap APLs) are a particularly insidious form of landmine designed to be activated by the unsuspecting victim. These mines are deliberately set as traps, often camouflaged or disguised as harmless objects, to lure individuals into triggering their detonation. Here's a detailed overview of booby trap anti-personnel landmines:

### Design and Construction:
1. **Concealed Design**: Booby trap APLs are intentionally concealed to deceive potential victims. They may be disguised as everyday objects such as toys, tools, or household items, or hidden beneath foliage, debris, or loose soil.

2. **Sensitive Activation Mechanisms**: These mines are equipped with highly sensitive activation mechanisms, such as pressure plates, tripwires, or tilt rods. Even minimal disturbance or contact with the triggering mechanism can initiate the detonation sequence.

3. **Small Size and Lightweight**: Booby trap APLs are typically small and lightweight to facilitate their concealment and placement in areas frequented by pedestrians or targeted individuals. Their compact size makes them difficult to detect and renders them highly portable.

4. **Fragmentation or Blast Effect**: Similar to conventional anti-personnel landmines, booby trap APLs are designed to inflict injuries through the release of a blast wave and shrapnel upon detonation. The explosive charge is often enclosed within a casing to maximize the fragmentation effect.

### Deployment and Tactics:
1. **Strategic Placement**: Booby trap APLs are strategically placed in locations likely to be traversed by targeted individuals, such as footpaths, doorways, windows, or areas of high pedestrian traffic. They may also be positioned near valuable assets or sensitive installations to deter unauthorized access.

2. **Deception and Camouflage**: These mines are carefully disguised or camouflaged to blend with the surrounding environment and evade detection. Common camouflage techniques include covering the mine with natural materials like leaves, dirt, or branches to conceal its presence.

3. **Psychological Warfare**: Booby trap APLs are used not only to inflict physical harm but also to instill fear and uncertainty among enemy forces or civilian populations. The threat of hidden explosives creates a pervasive sense of danger and erodes trust in the safety of the environment.

4. **Tactical Advantage**: By exploiting the element of surprise, booby trap APLs offer a tactical advantage to their operators, allowing them to disrupt enemy movements, delay advances, or inflict casualties without direct confrontation.

### Impact and Risks:
1. **Civilian Casualties and Injuries**: Booby trap APLs pose a significant risk to civilians, particularly in conflict-affected areas or regions with a history of guerrilla warfare. Victims may inadvertently trigger these traps while performing routine activities, resulting in severe injuries or fatalities.

2. **Psychological Trauma**: The presence of booby trap APLs creates a pervasive atmosphere of fear and suspicion, causing psychological trauma and anxiety among affected communities. Individuals may become reluctant to venture into unfamiliar areas or carry out essential tasks due to the perceived threat of hidden explosives.

3. **Economic Disruption**: Landmine contamination, including booby trap APLs, disrupts socioeconomic activities such as agriculture, trade, and infrastructure development. Fear of landmines restricts access to arable land, impedes transportation routes, and hampers efforts to rebuild and revitalize war-torn communities.

### International Regulations and Humanitarian Concerns:
1. **Prohibition and Regulation**: Booby trap anti-personnel landmines are subject to international regulations governing the use of landmines and explosive devices. The Ottawa Treaty (Mine Ban Treaty) prohibits the use, production, stockpiling, and transfer of anti-personnel landmines, including booby traps.

2. **Clearance and Risk Education**: Humanitarian organizations and demining agencies conduct clearance operations to remove booby trap APLs and other explosive remnants of war from affected areas. Mine risk education programs raise awareness about the dangers of booby traps and teach safety measures to prevent accidental detonations.

3. **Victim Assistance**: Efforts to assist landmine survivors and affected communities include medical care, rehabilitation services, psychosocial support, and socioeconomic assistance. These initiatives aim to address the long-term physical, emotional, and economic consequences of booby trap APL incidents.

In summary, booby trap anti-personnel landmines represent a malicious form of warfare, designed to exploit the vulnerability of unsuspecting individuals and instill fear in affected communities. Addressing the humanitarian impact of these devices requires concerted efforts to clear contaminated areas, educate populations about the risks of booby traps, and provide assistance to survivors and affected communities.''')

    st.subheader("4. M14 anti-personnel landmine")
    st.write('''The M14 anti-personnel landmine is a type of bounding fragmentation mine that was widely used during the Vietnam War and remains a concern due to its persistent presence in various conflict-affected regions. Here's a detailed overview of the M14 anti-personnel landmine:

### Design and Construction:
1. **Bounding Fragmentation Mine**: The M14 is designed to propel itself into the air upon activation and then explode, dispersing lethal fragments over a wide area. This mechanism increases its lethality and effectiveness against personnel.

2. **Cylindrical Shape**: The M14 mine is cylindrical in shape, typically measuring around 4.5 inches (11.4 cm) in diameter and 4.75 inches (12.1 cm) in height. It is constructed from metal, with an olive drab or gray coloration to blend with the surrounding terrain.

3. **Explosive Charge**: The mine contains a powerful explosive charge, usually composed of Composition B or TNT, which generates the blast and fragmentation effects upon detonation.

4. **Pressure-Activated**: The M14 is triggered by pressure applied to the pressure plate located on the top surface of the mine. When sufficient pressure is exerted, the mine is armed, and subsequent pressure or release triggers the detonation sequence.

### Deployment and Tactics:
1. **Scattered Deployment**: M14 mines were often scattered indiscriminately across areas of military significance, such as defensive positions, patrol routes, or perimeters surrounding military installations. They were also deployed along trails and footpaths to disrupt enemy movements.

2. **Concealment and Camouflage**: To evade detection by enemy forces and increase their effectiveness, M14 mines were concealed using various methods. They might be buried partially or completely underground, covered with vegetation, or disguised as harmless objects to deceive unsuspecting individuals.

3. **Ambush and Defensive Operations**: M14 mines were frequently employed as part of ambush tactics to target enemy patrols or personnel. They were also used defensively to protect strategic assets or fortifications from infiltration or direct assault.

4. **Secondary Explosive Devices**: In some cases, M14 mines were rigged as secondary explosive devices, detonating in response to the detonation of a nearby primary explosive device or triggering mechanism, such as tripwires or command detonation.

### Impact and Risks:
1. **Casualties and Injuries**: The blast and fragmentation effects of the M14 mine pose a significant threat to personnel, causing severe injuries, amputations, and fatalities. Victims within the blast radius may suffer multiple penetrating wounds from the mine's fragments.

2. **Long-term Hazard**: Despite decades since their initial deployment, M14 mines remain a persistent threat in many conflict-affected regions, contributing to ongoing casualties and hindering post-conflict recovery efforts. Clearance and demining operations are required to mitigate the risks posed by these legacy mines.

3. **Environmental Damage**: The presence of M14 mines and other explosive remnants of war can have adverse effects on the environment, contaminating soil and water sources and disrupting ecosystems. Clearance efforts must consider environmental factors to minimize the impact of mine contamination on biodiversity and natural resources.

### International Regulations and Humanitarian Concerns:
1. **Mine Clearance and Demining**: Humanitarian organizations and demining agencies conduct clearance operations to remove M14 mines and other explosive remnants of war from affected areas. These efforts are essential for restoring land to civilian use and reducing the risk to local populations.

2. **Victim Assistance**: Efforts to assist landmine survivors and affected communities include medical care, rehabilitation services, psychosocial support, and socioeconomic assistance. These initiatives aim to address the long-term physical, emotional, and economic consequences of mine-related incidents.

3. **Mine Risk Education**: Mine risk education programs raise awareness about the dangers of M14 mines and other explosive remnants of war, teaching safety measures to prevent accidents and promote safe behavior in affected communities.

In summary, the M14 anti-personnel landmine represents a significant threat to personnel in conflict-affected regions, posing risks of injury, death, and environmental damage. Addressing the humanitarian impact of M14 mines requires concerted efforts to clear contaminated areas, assist survivors, and educate communities about the risks of explosive remnants of war.''')




























if nav=="FLC Sensor":
    st.title("FLC Sensor")
    st.image("pic2.jpg")
    st.write('''Voltage (V), in the context of a Fluxgate Magnetometer or Fluxgate Magnetometer Sensor, refers to the output voltage value produced by the sensor in response to magnetic distortion or the presence of a magnetic field. Fluxgate sensors are a type of magnetometer that are commonly used to measure magnetic fields with high accuracy and sensitivity. When employing fluxgate magnetometers or FLC sensors for land mine identification, the voltage output serves as a crucial parameter in detecting the presence of buried metallic objects, including land mines. Here's how the information provided above can be tailored to this specific application:

### Principle of Operation:
1. **Detection of Metallic Objects**: Land mines often contain metallic components, such as casings, detonators, or shrapnel, which can cause magnetic distortion in the surrounding soil. The fluxgate magnetometer detects these disturbances in the Earth's magnetic field caused by buried metallic objects.

2. **Feedback Mechanism**: The fluxgate sensor's feedback mechanism detects changes in magnetic flux density induced by the presence of metallic objects. This leads to deviations from the sensor's baseline output voltage, indicating the presence of a potential land mine.

### Output Voltage Response:
1. **Identification of Anomalies**: The voltage output of the FLC sensor exhibits spikes or deviations from the baseline voltage when passing over areas with buried metallic objects, such as land mines. These anomalies in the output voltage signal the presence of a potential threat and prompt further investigation.

2. **Threshold Detection**: By setting threshold levels for the voltage output, land mine detection systems can trigger alarms or alerts when the measured voltage exceeds predefined limits. This helps identify suspicious areas that require closer inspection for the presence of buried land mines.

### Calibration and Compensation:
1. **Calibration for Sensitivity**: Land mine detection systems undergo calibration procedures to optimize the sensitivity of the fluxgate magnetometer to detect buried metallic objects while minimizing false positives. Calibration ensures that the voltage output accurately reflects the presence of land mines in different soil conditions.

2. **Temperature Compensation**: Temperature variations can affect the performance of the sensor and lead to fluctuations in the output voltage. Temperature compensation techniques adjust the voltage output to account for temperature-induced variations, ensuring consistent detection accuracy across different environmental conditions.

### Applications:
1. **Surveying and Mapping**: Fluxgate magnetometers equipped with FLC sensors are used for surveying and mapping areas suspected of containing land mines. By measuring magnetic anomalies in the soil, these sensors help create maps indicating the locations of potential threats for demining operations.

2. **Demining Operations**: Land mine detection systems employing fluxgate magnetometers assist demining teams in locating and identifying buried land mines safely and efficiently. The voltage output of the sensor guides deminers to areas requiring clearance and helps prioritize resources for effective demining efforts.

3. **Humanitarian Mine Clearance**: In humanitarian mine clearance efforts, fluxgate magnetometers play a vital role in mitigating the risks posed by land mines to civilian populations. By accurately detecting buried explosives, these sensors contribute to the clearance of contaminated areas and the establishment of safe environments for communities affected by land mines.

### Conclusion:
In the context of land mine identification, fluxgate magnetometers equipped with FLC sensors provide a reliable means of detecting buried metallic objects, including land mines. The voltage output of these sensors serves as a key indicator of potential threats, guiding demining operations and contributing to the safe clearance of contaminated areas. Calibration, temperature compensation, and threshold detection techniques ensure the accuracy and effectiveness of land mine detection systems in various environmental conditions and operational scenarios.
             ''')


elif nav=="Predictions":


    import streamlit as st
    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler
    from catboost import CatBoostClassifier

    # Load the dataset
    dataset = pd.read_csv("dataset.csv")
    X = dataset.iloc[:, :-1].values
    Y = dataset.iloc[:, -1].values

    # Normalize the features
    scaler = MinMaxScaler()
    X_normalized = scaler.fit_transform(X)

    # Train the classifier
    classifier = CatBoostClassifier()
    classifier.fit(X_normalized, Y)

    # Function to normalize input values
    def normalize_input(value, min_val, max_val):
        return (value - min_val) / (max_val - min_val)

    # Mapping numeric labels to class names
    
    # Streamlit app
    st.title('FLC Sensor Data Prediction')

    # Input fields
    voltage = st.number_input('Voltage (V)', min_value=0.0)
    height = st.number_input('High (m)', min_value=0.0)
    soil_type = st.selectbox('Soil Type', ['dry and sandy', 'dry and humus', 'dry and limy', 'humid and sandy', 'humid and humus', 'humid and limy'])

    submitted = st.button('Submit')

    if submitted:
        # Normalizing input values
        min_voltage, max_voltage = 0.0, 10.0  # Update with actual min and max values
        min_height, max_height = 0.0, 3.0  # Update with actual min and max values
        normalized_voltage = normalize_input(voltage, min_voltage, max_voltage)
        normalized_height = normalize_input(height, min_height, max_height)

        # Convert soil type to numerical
        soil_mapping = {
            'dry and sandy': 1,
            'dry and humus': 2,
            'dry and limy': 3,
            'humid and sandy': 4,
            'humid and humus': 5,
            'humid and limy': 6
        }
        soil_code = soil_mapping[soil_type]

        # Store responses
        a, b, c = normalized_voltage, normalized_height, soil_code

        # Prediction
        new_sample = [[a, b, c]]
        prediction = classifier.predict(new_sample)
        print(prediction)  # Extracting the single value from the numpy array
        if prediction==[[1]]:
            result = "Null"
        elif prediction==[[3]]:
            result = "Anti-personnel"
        elif prediction==[[2]]:
            result = "Anti-Tank"
        elif prediction==[[4]]:
            result = "Booby Trapped Anti-personnel"
        elif prediction==[[5]]:
            result = "M14 Anti-personnel"
        # Display prediction
        st.write("Predicted class:", result)



elif nav=="About":
    st.title("About")
    st.divider()
    st.subheader('Created with ❤️ by Ishaan Verma')
    st.divider()
    st.write(''' ***Tech stack***: ''')
    st.write('''This website is made completely using python and is made on streamlit framework.''')
    st.write('''The prediction model uses CatBoos to predit Land Mines.The dataset on which the model is trained on has 2338 rows data.''')
    