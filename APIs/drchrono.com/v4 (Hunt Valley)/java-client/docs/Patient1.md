

# Patient1



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**fax** | **String** | Should follow format \&quot;xxx-xx-xxxx\&quot; |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**middleName** | **String** |  |  [optional] |
|**npi** | **String** |  |  [optional] |
|**phone** | **String** | Should follow format \&quot;xxx-xx-xxxx\&quot; |  [optional] |
|**providerNumber** | **String** |  |  [optional] |
|**providerQualifier** | [**ProviderQualifierEnum**](#ProviderQualifierEnum) | Can be one of following, &#x60;&#39;&#39;&#x60;, &#x60;&#39;0B&#39;&#x60;(State License #), &#x60;&#39;1G&#39;&#x60;(Provider UPIN #), &#x60;&#39;G2&#39;&#x60;(Provider Commercial #) |  [optional] |
|**specialty** | [**SpecialtyEnum**](#SpecialtyEnum) | Can be one of following, &#x60;&#39;&#39;&#x60;, &#x60;&#39;Acupuncture&#39;&#x60;, &#x60;&#39;Advanced Practice Midwife&#39;&#x60;, &#x60;&#39;Aesthetic Medicine&#39;&#x60;, &#x60;&#39;Aesthetician&#39;&#x60;, &#x60;&#39;Allergist/Immunologist&#39;&#x60;, &#x60;&#39;Anesthesiologist&#39;&#x60;, &#x60;&#39;Cardiac Electrophysiologist&#39;&#x60;, &#x60;&#39;Cardiologist&#39;&#x60;, &#x60;&#39;Cardiothoracic Surgeon&#39;&#x60;, &#x60;&#39;Child/Adolescent Psychiatry&#39;&#x60;, &#x60;&#39;Chiropractor&#39;&#x60;, &#x60;&#39;Clinical Social Worker&#39;&#x60;, &#x60;&#39;Colorectal Surgeon&#39;&#x60;, &#x60;&#39;Correactology&#39;&#x60;, &#x60;&#39;Cosmetic Medicine&#39;&#x60;, &#x60;&#39;Counselor Mental Health&#39;&#x60;, &#x60;&#39;Counselor Professional&#39;&#x60;, &#x60;&#39;Counselor&#39;&#x60;, &#x60;&#39;Dentist&#39;&#x60;, &#x60;&#39;Diabetology&#39;&#x60;, &#x60;&#39;Dermatologist&#39;&#x60;, &#x60;&#39;Diagnostic Medical Sonographer&#39;&#x60;, &#x60;&#39;Dietitian, Registered&#39;&#x60;, &#x60;&#39;Ear-Nose-Throat Specialist (ENT)&#39;&#x60;, &#x60;&#39;Emergency Medicine Physician&#39;&#x60;, &#x60;&#39;Endocrinologist&#39;&#x60;, &#x60;&#39;Endodontist&#39;&#x60;, &#x60;&#39;Epidemiologist&#39;&#x60;, &#x60;&#39;Family Practitioner&#39;&#x60;, &#x60;&#39;Gastroenterologist&#39;&#x60;, &#x60;&#39;General Practice&#39;&#x60;, &#x60;&#39;General Surgeon&#39;&#x60;, &#x60;&#39;Geneticist&#39;&#x60;, &#x60;&#39;Geriatrician&#39;&#x60;, &#x60;&#39;Gerontologist&#39;&#x60;, &#x60;&#39;Gynecologist (no OB)&#39;&#x60;, &#x60;&#39;Gynegologic Oncologist&#39;&#x60;, &#x60;&#39;Hand Surgeon&#39;&#x60;, &#x60;&#39;Hematologist&#39;&#x60;, &#x60;&#39;Home Care&#39;&#x60;, &#x60;&#39;Hospice&#39;&#x60;, &#x60;&#39;Hospitalist&#39;&#x60;, &#x60;&#39;Infectious Disease Specialist&#39;&#x60;, &#x60;&#39;Integrative and Functional Medicine&#39;&#x60;, &#x60;&#39;Integrative Medicine&#39;&#x60;, &#x60;&#39;Internist&#39;&#x60;, &#x60;&#39;Interventional Radiology&#39;&#x60;, &#x60;&#39;Laboratory Medicine Specialist&#39;&#x60;, &#x60;&#39;Laser Surgery&#39;&#x60;, &#x60;&#39;Massage Therapist&#39;&#x60;, &#x60;&#39;Naturopathic Physician&#39;&#x60;, &#x60;&#39;Neonatologist&#39;&#x60;, &#x60;&#39;Nephrologist&#39;&#x60;, &#x60;&#39;Neurologist&#39;&#x60;, &#x60;&#39;Neuropsychology&#39;&#x60;, &#x60;&#39;Neurosurgeon&#39;&#x60;, &#x60;&#39;Not Actively Practicing&#39;&#x60;, &#x60;&#39;Nuclear Medicine Specialist&#39;&#x60;, &#x60;&#39;Nurse Practitioner&#39;&#x60;, &#x60;&#39;Nursing&#39;&#x60;, &#x60;&#39;Nutritionist&#39;&#x60;, &#x60;&#39;Obstetrician/Gynecologist&#39;&#x60;, &#x60;&#39;Occupational Medicine&#39;&#x60;, &#x60;&#39;Occupational Therapist&#39;&#x60;, &#x60;&#39;Oncologist&#39;&#x60;, &#x60;&#39;Ophthalmologist&#39;&#x60;, &#x60;&#39;Optometrist&#39;&#x60;, &#x60;&#39;Oral Surgeon&#39;&#x60;, &#x60;&#39;Orofacial Pain&#39;&#x60;, &#x60;&#39;Orthodontist&#39;&#x60;, &#x60;&#39;Orthopedic Surgeon&#39;&#x60;, &#x60;&#39;Orthotist&#39;&#x60;, &#x60;&#39;Other&#39;&#x60;, &#x60;&#39;Pain Management Specialist&#39;&#x60;, &#x60;&#39;Pathologist&#39;&#x60;, &#x60;&#39;Pediatric Dentist&#39;&#x60;, &#x60;&#39;Pediatric Gastroenterology&#39;&#x60;, &#x60;&#39;Pediatric Surgeon&#39;&#x60;, &#x60;&#39;Pediatrician&#39;&#x60;, &#x60;&#39;Perinatologist&#39;&#x60;, &#x60;&#39;Periodontist&#39;&#x60;, &#x60;&#39;Physical Medicine and Rehab Specialist&#39;&#x60;, &#x60;&#39;Physical Therapist&#39;&#x60;, &#x60;&#39;Physician Assistant&#39;&#x60;, &#x60;&#39;Plastic Surgeon&#39;&#x60;, &#x60;&#39;Podiatrist&#39;&#x60;, &#x60;&#39;Preventive-Aging Medicine&#39;&#x60;, &#x60;&#39;Preventive Medicine/Occupational-Environmental Medicine&#39;&#x60;, &#x60;&#39;Primary Care Physician&#39;&#x60;, &#x60;&#39;Prosthetist&#39;&#x60;, &#x60;&#39;Prosthodontist&#39;&#x60;, &#x60;&#39;Psychiatrist&#39;&#x60;, &#x60;&#39;Psychologist&#39;&#x60;, &#x60;&#39;Public Health Professional&#39;&#x60;, &#x60;&#39;Pulmonologist&#39;&#x60;, &#x60;&#39;Radiation Oncologist&#39;&#x60;, &#x60;&#39;Radiologist&#39;&#x60;, &#x60;&#39;Registered Nurse&#39;&#x60;, &#x60;&#39;Religious Nonmedical Practitioner&#39;&#x60;, &#x60;&#39;Reproductive Endocrinologist&#39;&#x60;, &#x60;&#39;Reproductive Medicine&#39;&#x60;, &#x60;&#39;Rheumatologist&#39;&#x60;, &#x60;&#39;Sleep Medicine&#39;&#x60;, &#x60;&#39;Speech-Language Pathologist&#39;&#x60;, &#x60;&#39;Sports Medicine Specialist&#39;&#x60;, &#x60;&#39;Urologist&#39;&#x60;, &#x60;&#39;Urgent Care&#39;&#x60;, &#x60;&#39;Vascular Surgeon&#39;&#x60; |  [optional] |
|**suffix** | **String** |  |  [optional] |



## Enum: ProviderQualifierEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| _0_B | &quot;0B&quot; |
| _1_G | &quot;1G&quot; |
| G2 | &quot;G2&quot; |



## Enum: SpecialtyEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| ACUPUNCTURE | &quot;Acupuncture&quot; |
| ADVANCED_PRACTICE_MIDWIFE | &quot;Advanced Practice Midwife&quot; |
| AESTHETIC_MEDICINE | &quot;Aesthetic Medicine&quot; |
| AESTHETICIAN | &quot;Aesthetician&quot; |
| ALLERGIST_IMMUNOLOGIST | &quot;Allergist/Immunologist&quot; |
| ANESTHESIOLOGIST | &quot;Anesthesiologist&quot; |
| CARDIAC_ELECTROPHYSIOLOGIST | &quot;Cardiac Electrophysiologist&quot; |
| CARDIOLOGIST | &quot;Cardiologist&quot; |
| CARDIOTHORACIC_SURGEON | &quot;Cardiothoracic Surgeon&quot; |
| CHILD_ADOLESCENT_PSYCHIATRY | &quot;Child/Adolescent Psychiatry&quot; |
| CHIROPRACTOR | &quot;Chiropractor&quot; |
| CLINICAL_SOCIAL_WORKER | &quot;Clinical Social Worker&quot; |
| COLORECTAL_SURGEON | &quot;Colorectal Surgeon&quot; |
| CORREACTOLOGY | &quot;Correactology&quot; |
| COSMETIC_MEDICINE | &quot;Cosmetic Medicine&quot; |
| COUNSELOR_MENTAL_HEALTH | &quot;Counselor Mental Health&quot; |
| COUNSELOR_PROFESSIONAL | &quot;Counselor Professional&quot; |
| COUNSELOR | &quot;Counselor&quot; |
| DENTIST | &quot;Dentist&quot; |
| DIABETOLOGY | &quot;Diabetology&quot; |
| DERMATOLOGIST | &quot;Dermatologist&quot; |
| DIAGNOSTIC_MEDICAL_SONOGRAPHER | &quot;Diagnostic Medical Sonographer&quot; |
| DIETITIAN_REGISTERED | &quot;Dietitian, Registered&quot; |
| EAR_NOSE_THROAT_SPECIALIST_ENT_ | &quot;Ear-Nose-Throat Specialist (ENT)&quot; |
| EMERGENCY_MEDICINE_PHYSICIAN | &quot;Emergency Medicine Physician&quot; |
| ENDOCRINOLOGIST | &quot;Endocrinologist&quot; |
| ENDODONTIST | &quot;Endodontist&quot; |
| EPIDEMIOLOGIST | &quot;Epidemiologist&quot; |
| FAMILY_PRACTITIONER | &quot;Family Practitioner&quot; |
| GASTROENTEROLOGIST | &quot;Gastroenterologist&quot; |
| GENERAL_PRACTICE | &quot;General Practice&quot; |
| GENERAL_SURGEON | &quot;General Surgeon&quot; |
| GENETICIST | &quot;Geneticist&quot; |
| GERIATRICIAN | &quot;Geriatrician&quot; |
| GERONTOLOGIST | &quot;Gerontologist&quot; |
| GYNECOLOGIST_NO_OB_ | &quot;Gynecologist (no OB)&quot; |
| GYNEGOLOGIC_ONCOLOGIST | &quot;Gynegologic Oncologist&quot; |
| HAND_SURGEON | &quot;Hand Surgeon&quot; |
| HEMATOLOGIST | &quot;Hematologist&quot; |
| HOME_CARE | &quot;Home Care&quot; |
| HOSPICE | &quot;Hospice&quot; |
| HOSPITALIST | &quot;Hospitalist&quot; |
| INFECTIOUS_DISEASE_SPECIALIST | &quot;Infectious Disease Specialist&quot; |
| INTEGRATIVE_AND_FUNCTIONAL_MEDICINE | &quot;Integrative and Functional Medicine&quot; |
| INTEGRATIVE_MEDICINE | &quot;Integrative Medicine&quot; |
| INTERNIST | &quot;Internist&quot; |
| INTERVENTIONAL_RADIOLOGY | &quot;Interventional Radiology&quot; |
| LABORATORY_MEDICINE_SPECIALIST | &quot;Laboratory Medicine Specialist&quot; |
| LASER_SURGERY | &quot;Laser Surgery&quot; |
| MASSAGE_THERAPIST | &quot;Massage Therapist&quot; |
| NATUROPATHIC_PHYSICIAN | &quot;Naturopathic Physician&quot; |
| NEONATOLOGIST | &quot;Neonatologist&quot; |
| NEPHROLOGIST | &quot;Nephrologist&quot; |
| NEUROLOGIST | &quot;Neurologist&quot; |
| NEUROPSYCHOLOGY | &quot;Neuropsychology&quot; |
| NEUROSURGEON | &quot;Neurosurgeon&quot; |
| NOT_ACTIVELY_PRACTICING | &quot;Not Actively Practicing&quot; |
| NUCLEAR_MEDICINE_SPECIALIST | &quot;Nuclear Medicine Specialist&quot; |
| NURSE_PRACTITIONER | &quot;Nurse Practitioner&quot; |
| NURSING | &quot;Nursing&quot; |
| NUTRITIONIST | &quot;Nutritionist&quot; |
| OBSTETRICIAN_GYNECOLOGIST | &quot;Obstetrician/Gynecologist&quot; |
| OCCUPATIONAL_MEDICINE | &quot;Occupational Medicine&quot; |
| OCCUPATIONAL_THERAPIST | &quot;Occupational Therapist&quot; |
| ONCOLOGIST | &quot;Oncologist&quot; |
| OPHTHALMOLOGIST | &quot;Ophthalmologist&quot; |
| OPTOMETRIST | &quot;Optometrist&quot; |
| ORAL_SURGEON | &quot;Oral Surgeon&quot; |
| OROFACIAL_PAIN | &quot;Orofacial Pain&quot; |
| ORTHODONTIST | &quot;Orthodontist&quot; |
| ORTHOPEDIC_SURGEON | &quot;Orthopedic Surgeon&quot; |
| ORTHOTIST | &quot;Orthotist&quot; |
| OTHER | &quot;Other&quot; |
| PAIN_MANAGEMENT_SPECIALIST | &quot;Pain Management Specialist&quot; |
| PATHOLOGIST | &quot;Pathologist&quot; |
| PEDIATRIC_DENTIST | &quot;Pediatric Dentist&quot; |
| PEDIATRIC_GASTROENTEROLOGY | &quot;Pediatric Gastroenterology&quot; |
| PEDIATRIC_SURGEON | &quot;Pediatric Surgeon&quot; |
| PEDIATRICIAN | &quot;Pediatrician&quot; |
| PERINATOLOGIST | &quot;Perinatologist&quot; |
| PERIODONTIST | &quot;Periodontist&quot; |
| PHYSICAL_MEDICINE_AND_REHAB_SPECIALIST | &quot;Physical Medicine and Rehab Specialist&quot; |
| PHYSICAL_THERAPIST | &quot;Physical Therapist&quot; |
| PHYSICIAN_ASSISTANT | &quot;Physician Assistant&quot; |
| PLASTIC_SURGEON | &quot;Plastic Surgeon&quot; |
| PODIATRIST | &quot;Podiatrist&quot; |
| PREVENTIVE_AGING_MEDICINE | &quot;Preventive-Aging Medicine&quot; |
| PREVENTIVE_MEDICINE_OCCUPATIONAL_ENVIRONMENTAL_MEDICINE | &quot;Preventive Medicine/Occupational-Environmental Medicine&quot; |
| PRIMARY_CARE_PHYSICIAN | &quot;Primary Care Physician&quot; |
| PROSTHETIST | &quot;Prosthetist&quot; |
| PROSTHODONTIST | &quot;Prosthodontist&quot; |
| PSYCHIATRIST | &quot;Psychiatrist&quot; |
| PSYCHOLOGIST | &quot;Psychologist&quot; |
| PUBLIC_HEALTH_PROFESSIONAL | &quot;Public Health Professional&quot; |
| PULMONOLOGIST | &quot;Pulmonologist&quot; |
| RADIATION_ONCOLOGIST | &quot;Radiation Oncologist&quot; |
| RADIOLOGIST | &quot;Radiologist&quot; |
| REGISTERED_NURSE | &quot;Registered Nurse&quot; |
| RELIGIOUS_NONMEDICAL_PRACTITIONER | &quot;Religious Nonmedical Practitioner&quot; |
| REPRODUCTIVE_ENDOCRINOLOGIST | &quot;Reproductive Endocrinologist&quot; |
| REPRODUCTIVE_MEDICINE | &quot;Reproductive Medicine&quot; |
| RHEUMATOLOGIST | &quot;Rheumatologist&quot; |
| SLEEP_MEDICINE | &quot;Sleep Medicine&quot; |
| SPEECH_LANGUAGE_PATHOLOGIST | &quot;Speech-Language Pathologist&quot; |
| SPORTS_MEDICINE_SPECIALIST | &quot;Sports Medicine Specialist&quot; |
| UROLOGIST | &quot;Urologist&quot; |
| URGENT_CARE | &quot;Urgent Care&quot; |
| VASCULAR_SURGEON | &quot;Vascular Surgeon&quot; |



