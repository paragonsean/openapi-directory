# OpenapiJsClient.Patient1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** |  | [optional] 
**email** | **String** |  | [optional] 
**fax** | **String** | Should follow format \&quot;xxx-xx-xxxx\&quot; | [optional] 
**firstName** | **String** |  | [optional] 
**lastName** | **String** |  | [optional] 
**middleName** | **String** |  | [optional] 
**npi** | **String** |  | [optional] 
**phone** | **String** | Should follow format \&quot;xxx-xx-xxxx\&quot; | [optional] 
**providerNumber** | **String** |  | [optional] 
**providerQualifier** | **String** | Can be one of following, &#x60;&#39;&#39;&#x60;, &#x60;&#39;0B&#39;&#x60;(State License #), &#x60;&#39;1G&#39;&#x60;(Provider UPIN #), &#x60;&#39;G2&#39;&#x60;(Provider Commercial #) | [optional] 
**specialty** | **String** | Can be one of following, &#x60;&#39;&#39;&#x60;, &#x60;&#39;Acupuncture&#39;&#x60;, &#x60;&#39;Advanced Practice Midwife&#39;&#x60;, &#x60;&#39;Aesthetic Medicine&#39;&#x60;, &#x60;&#39;Aesthetician&#39;&#x60;, &#x60;&#39;Allergist/Immunologist&#39;&#x60;, &#x60;&#39;Anesthesiologist&#39;&#x60;, &#x60;&#39;Cardiac Electrophysiologist&#39;&#x60;, &#x60;&#39;Cardiologist&#39;&#x60;, &#x60;&#39;Cardiothoracic Surgeon&#39;&#x60;, &#x60;&#39;Child/Adolescent Psychiatry&#39;&#x60;, &#x60;&#39;Chiropractor&#39;&#x60;, &#x60;&#39;Clinical Social Worker&#39;&#x60;, &#x60;&#39;Colorectal Surgeon&#39;&#x60;, &#x60;&#39;Correactology&#39;&#x60;, &#x60;&#39;Cosmetic Medicine&#39;&#x60;, &#x60;&#39;Counselor Mental Health&#39;&#x60;, &#x60;&#39;Counselor Professional&#39;&#x60;, &#x60;&#39;Counselor&#39;&#x60;, &#x60;&#39;Dentist&#39;&#x60;, &#x60;&#39;Diabetology&#39;&#x60;, &#x60;&#39;Dermatologist&#39;&#x60;, &#x60;&#39;Diagnostic Medical Sonographer&#39;&#x60;, &#x60;&#39;Dietitian, Registered&#39;&#x60;, &#x60;&#39;Ear-Nose-Throat Specialist (ENT)&#39;&#x60;, &#x60;&#39;Emergency Medicine Physician&#39;&#x60;, &#x60;&#39;Endocrinologist&#39;&#x60;, &#x60;&#39;Endodontist&#39;&#x60;, &#x60;&#39;Epidemiologist&#39;&#x60;, &#x60;&#39;Family Practitioner&#39;&#x60;, &#x60;&#39;Gastroenterologist&#39;&#x60;, &#x60;&#39;General Practice&#39;&#x60;, &#x60;&#39;General Surgeon&#39;&#x60;, &#x60;&#39;Geneticist&#39;&#x60;, &#x60;&#39;Geriatrician&#39;&#x60;, &#x60;&#39;Gerontologist&#39;&#x60;, &#x60;&#39;Gynecologist (no OB)&#39;&#x60;, &#x60;&#39;Gynegologic Oncologist&#39;&#x60;, &#x60;&#39;Hand Surgeon&#39;&#x60;, &#x60;&#39;Hematologist&#39;&#x60;, &#x60;&#39;Home Care&#39;&#x60;, &#x60;&#39;Hospice&#39;&#x60;, &#x60;&#39;Hospitalist&#39;&#x60;, &#x60;&#39;Infectious Disease Specialist&#39;&#x60;, &#x60;&#39;Integrative and Functional Medicine&#39;&#x60;, &#x60;&#39;Integrative Medicine&#39;&#x60;, &#x60;&#39;Internist&#39;&#x60;, &#x60;&#39;Interventional Radiology&#39;&#x60;, &#x60;&#39;Laboratory Medicine Specialist&#39;&#x60;, &#x60;&#39;Laser Surgery&#39;&#x60;, &#x60;&#39;Massage Therapist&#39;&#x60;, &#x60;&#39;Naturopathic Physician&#39;&#x60;, &#x60;&#39;Neonatologist&#39;&#x60;, &#x60;&#39;Nephrologist&#39;&#x60;, &#x60;&#39;Neurologist&#39;&#x60;, &#x60;&#39;Neuropsychology&#39;&#x60;, &#x60;&#39;Neurosurgeon&#39;&#x60;, &#x60;&#39;Not Actively Practicing&#39;&#x60;, &#x60;&#39;Nuclear Medicine Specialist&#39;&#x60;, &#x60;&#39;Nurse Practitioner&#39;&#x60;, &#x60;&#39;Nursing&#39;&#x60;, &#x60;&#39;Nutritionist&#39;&#x60;, &#x60;&#39;Obstetrician/Gynecologist&#39;&#x60;, &#x60;&#39;Occupational Medicine&#39;&#x60;, &#x60;&#39;Occupational Therapist&#39;&#x60;, &#x60;&#39;Oncologist&#39;&#x60;, &#x60;&#39;Ophthalmologist&#39;&#x60;, &#x60;&#39;Optometrist&#39;&#x60;, &#x60;&#39;Oral Surgeon&#39;&#x60;, &#x60;&#39;Orofacial Pain&#39;&#x60;, &#x60;&#39;Orthodontist&#39;&#x60;, &#x60;&#39;Orthopedic Surgeon&#39;&#x60;, &#x60;&#39;Orthotist&#39;&#x60;, &#x60;&#39;Other&#39;&#x60;, &#x60;&#39;Pain Management Specialist&#39;&#x60;, &#x60;&#39;Pathologist&#39;&#x60;, &#x60;&#39;Pediatric Dentist&#39;&#x60;, &#x60;&#39;Pediatric Gastroenterology&#39;&#x60;, &#x60;&#39;Pediatric Surgeon&#39;&#x60;, &#x60;&#39;Pediatrician&#39;&#x60;, &#x60;&#39;Perinatologist&#39;&#x60;, &#x60;&#39;Periodontist&#39;&#x60;, &#x60;&#39;Physical Medicine and Rehab Specialist&#39;&#x60;, &#x60;&#39;Physical Therapist&#39;&#x60;, &#x60;&#39;Physician Assistant&#39;&#x60;, &#x60;&#39;Plastic Surgeon&#39;&#x60;, &#x60;&#39;Podiatrist&#39;&#x60;, &#x60;&#39;Preventive-Aging Medicine&#39;&#x60;, &#x60;&#39;Preventive Medicine/Occupational-Environmental Medicine&#39;&#x60;, &#x60;&#39;Primary Care Physician&#39;&#x60;, &#x60;&#39;Prosthetist&#39;&#x60;, &#x60;&#39;Prosthodontist&#39;&#x60;, &#x60;&#39;Psychiatrist&#39;&#x60;, &#x60;&#39;Psychologist&#39;&#x60;, &#x60;&#39;Public Health Professional&#39;&#x60;, &#x60;&#39;Pulmonologist&#39;&#x60;, &#x60;&#39;Radiation Oncologist&#39;&#x60;, &#x60;&#39;Radiologist&#39;&#x60;, &#x60;&#39;Registered Nurse&#39;&#x60;, &#x60;&#39;Religious Nonmedical Practitioner&#39;&#x60;, &#x60;&#39;Reproductive Endocrinologist&#39;&#x60;, &#x60;&#39;Reproductive Medicine&#39;&#x60;, &#x60;&#39;Rheumatologist&#39;&#x60;, &#x60;&#39;Sleep Medicine&#39;&#x60;, &#x60;&#39;Speech-Language Pathologist&#39;&#x60;, &#x60;&#39;Sports Medicine Specialist&#39;&#x60;, &#x60;&#39;Urologist&#39;&#x60;, &#x60;&#39;Urgent Care&#39;&#x60;, &#x60;&#39;Vascular Surgeon&#39;&#x60; | [optional] 
**suffix** | **String** |  | [optional] 



## Enum: ProviderQualifierEnum


* `empty` (value: `""`)

* `0B` (value: `"0B"`)

* `1G` (value: `"1G"`)

* `G2` (value: `"G2"`)





## Enum: SpecialtyEnum


* `empty` (value: `""`)

* `Acupuncture` (value: `"Acupuncture"`)

* `Advanced Practice Midwife` (value: `"Advanced Practice Midwife"`)

* `Aesthetic Medicine` (value: `"Aesthetic Medicine"`)

* `Aesthetician` (value: `"Aesthetician"`)

* `Allergist/Immunologist` (value: `"Allergist/Immunologist"`)

* `Anesthesiologist` (value: `"Anesthesiologist"`)

* `Cardiac Electrophysiologist` (value: `"Cardiac Electrophysiologist"`)

* `Cardiologist` (value: `"Cardiologist"`)

* `Cardiothoracic Surgeon` (value: `"Cardiothoracic Surgeon"`)

* `Child/Adolescent Psychiatry` (value: `"Child/Adolescent Psychiatry"`)

* `Chiropractor` (value: `"Chiropractor"`)

* `Clinical Social Worker` (value: `"Clinical Social Worker"`)

* `Colorectal Surgeon` (value: `"Colorectal Surgeon"`)

* `Correactology` (value: `"Correactology"`)

* `Cosmetic Medicine` (value: `"Cosmetic Medicine"`)

* `Counselor Mental Health` (value: `"Counselor Mental Health"`)

* `Counselor Professional` (value: `"Counselor Professional"`)

* `Counselor` (value: `"Counselor"`)

* `Dentist` (value: `"Dentist"`)

* `Diabetology` (value: `"Diabetology"`)

* `Dermatologist` (value: `"Dermatologist"`)

* `Diagnostic Medical Sonographer` (value: `"Diagnostic Medical Sonographer"`)

* `Dietitian, Registered` (value: `"Dietitian, Registered"`)

* `Ear-Nose-Throat Specialist (ENT)` (value: `"Ear-Nose-Throat Specialist (ENT)"`)

* `Emergency Medicine Physician` (value: `"Emergency Medicine Physician"`)

* `Endocrinologist` (value: `"Endocrinologist"`)

* `Endodontist` (value: `"Endodontist"`)

* `Epidemiologist` (value: `"Epidemiologist"`)

* `Family Practitioner` (value: `"Family Practitioner"`)

* `Gastroenterologist` (value: `"Gastroenterologist"`)

* `General Practice` (value: `"General Practice"`)

* `General Surgeon` (value: `"General Surgeon"`)

* `Geneticist` (value: `"Geneticist"`)

* `Geriatrician` (value: `"Geriatrician"`)

* `Gerontologist` (value: `"Gerontologist"`)

* `Gynecologist (no OB)` (value: `"Gynecologist (no OB)"`)

* `Gynegologic Oncologist` (value: `"Gynegologic Oncologist"`)

* `Hand Surgeon` (value: `"Hand Surgeon"`)

* `Hematologist` (value: `"Hematologist"`)

* `Home Care` (value: `"Home Care"`)

* `Hospice` (value: `"Hospice"`)

* `Hospitalist` (value: `"Hospitalist"`)

* `Infectious Disease Specialist` (value: `"Infectious Disease Specialist"`)

* `Integrative and Functional Medicine` (value: `"Integrative and Functional Medicine"`)

* `Integrative Medicine` (value: `"Integrative Medicine"`)

* `Internist` (value: `"Internist"`)

* `Interventional Radiology` (value: `"Interventional Radiology"`)

* `Laboratory Medicine Specialist` (value: `"Laboratory Medicine Specialist"`)

* `Laser Surgery` (value: `"Laser Surgery"`)

* `Massage Therapist` (value: `"Massage Therapist"`)

* `Naturopathic Physician` (value: `"Naturopathic Physician"`)

* `Neonatologist` (value: `"Neonatologist"`)

* `Nephrologist` (value: `"Nephrologist"`)

* `Neurologist` (value: `"Neurologist"`)

* `Neuropsychology` (value: `"Neuropsychology"`)

* `Neurosurgeon` (value: `"Neurosurgeon"`)

* `Not Actively Practicing` (value: `"Not Actively Practicing"`)

* `Nuclear Medicine Specialist` (value: `"Nuclear Medicine Specialist"`)

* `Nurse Practitioner` (value: `"Nurse Practitioner"`)

* `Nursing` (value: `"Nursing"`)

* `Nutritionist` (value: `"Nutritionist"`)

* `Obstetrician/Gynecologist` (value: `"Obstetrician/Gynecologist"`)

* `Occupational Medicine` (value: `"Occupational Medicine"`)

* `Occupational Therapist` (value: `"Occupational Therapist"`)

* `Oncologist` (value: `"Oncologist"`)

* `Ophthalmologist` (value: `"Ophthalmologist"`)

* `Optometrist` (value: `"Optometrist"`)

* `Oral Surgeon` (value: `"Oral Surgeon"`)

* `Orofacial Pain` (value: `"Orofacial Pain"`)

* `Orthodontist` (value: `"Orthodontist"`)

* `Orthopedic Surgeon` (value: `"Orthopedic Surgeon"`)

* `Orthotist` (value: `"Orthotist"`)

* `Other` (value: `"Other"`)

* `Pain Management Specialist` (value: `"Pain Management Specialist"`)

* `Pathologist` (value: `"Pathologist"`)

* `Pediatric Dentist` (value: `"Pediatric Dentist"`)

* `Pediatric Gastroenterology` (value: `"Pediatric Gastroenterology"`)

* `Pediatric Surgeon` (value: `"Pediatric Surgeon"`)

* `Pediatrician` (value: `"Pediatrician"`)

* `Perinatologist` (value: `"Perinatologist"`)

* `Periodontist` (value: `"Periodontist"`)

* `Physical Medicine and Rehab Specialist` (value: `"Physical Medicine and Rehab Specialist"`)

* `Physical Therapist` (value: `"Physical Therapist"`)

* `Physician Assistant` (value: `"Physician Assistant"`)

* `Plastic Surgeon` (value: `"Plastic Surgeon"`)

* `Podiatrist` (value: `"Podiatrist"`)

* `Preventive-Aging Medicine` (value: `"Preventive-Aging Medicine"`)

* `Preventive Medicine/Occupational-Environmental Medicine` (value: `"Preventive Medicine/Occupational-Environmental Medicine"`)

* `Primary Care Physician` (value: `"Primary Care Physician"`)

* `Prosthetist` (value: `"Prosthetist"`)

* `Prosthodontist` (value: `"Prosthodontist"`)

* `Psychiatrist` (value: `"Psychiatrist"`)

* `Psychologist` (value: `"Psychologist"`)

* `Public Health Professional` (value: `"Public Health Professional"`)

* `Pulmonologist` (value: `"Pulmonologist"`)

* `Radiation Oncologist` (value: `"Radiation Oncologist"`)

* `Radiologist` (value: `"Radiologist"`)

* `Registered Nurse` (value: `"Registered Nurse"`)

* `Religious Nonmedical Practitioner` (value: `"Religious Nonmedical Practitioner"`)

* `Reproductive Endocrinologist` (value: `"Reproductive Endocrinologist"`)

* `Reproductive Medicine` (value: `"Reproductive Medicine"`)

* `Rheumatologist` (value: `"Rheumatologist"`)

* `Sleep Medicine` (value: `"Sleep Medicine"`)

* `Speech-Language Pathologist` (value: `"Speech-Language Pathologist"`)

* `Sports Medicine Specialist` (value: `"Sports Medicine Specialist"`)

* `Urologist` (value: `"Urologist"`)

* `Urgent Care` (value: `"Urgent Care"`)

* `Vascular Surgeon` (value: `"Vascular Surgeon"`)




