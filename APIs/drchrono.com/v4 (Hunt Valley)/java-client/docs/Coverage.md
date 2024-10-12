

# Coverage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appointment** | **String** |  |  [optional] [readonly] |
|**cobLevel** | **String** | The level of insurance the eligibility check was run on. Can be one of the following: &#x60;Primary Insurance&#x60; or &#x60;Secondary Insurance&#x60; |  [optional] [readonly] |
|**coverageDetails** | **String** | A variable size object containing the details of the eligibility check, if returned by the clearinghouse that ran the eligibility check |  [optional] [readonly] |
|**coverageSubscriber** | **String** | A variable size object containing subscriber information, if returned by the clearinghouse that ran the eligibility check |  [optional] [readonly] |
|**eligibility** | **String** |  Value | Description --- | ---- &#x60;&#39;1&#39;&#x60; | Active Coverage &#x60;&#39;2&#39;&#x60; | Active - Full Risk Capitation &#x60;&#39;3&#39;&#x60; | Active - Services Capitated &#x60;&#39;4&#39;&#x60; | Active - Services Capitated to Primary Care Physician &#x60;&#39;5&#39;&#x60; | Active - Pending Investigation &#x60;&#39;6&#39;&#x60; | Inactive &#x60;&#39;7&#39;&#x60; | Inactive - Pending Eligibility Update &#x60;&#39;8&#39;&#x60; | Inactive - Pending Investigation &#x60;&#39;A&#39;&#x60; | Co-Insurance &#x60;&#39;B&#39;&#x60; | Co-Payment &#x60;&#39;C&#39;&#x60; | Deductible &#x60;&#39;CB&#39;&#x60; | Coverage Basis &#x60;&#39;D&#39;&#x60; | Benefit Description &#x60;&#39;E&#39;&#x60; | Exclusions &#x60;&#39;F&#39;&#x60; | Limitations &#x60;&#39;G&#39;&#x60; | Out of Pocket (Stop Loss) &#x60;&#39;H&#39;&#x60; | Unlimited &#x60;&#39;I&#39;&#x60; | Non-Covered &#x60;&#39;J&#39;&#x60; | Cost Containment &#x60;&#39;K&#39;&#x60; | Reserve &#x60;&#39;L&#39;&#x60; | Primary Care Provider &#x60;&#39;M&#39;&#x60; | Pre-existing Condition &#x60;&#39;MC&#39;&#x60; | Managed Care Coordinator &#x60;&#39;N&#39;&#x60; | Services Restricted to Following Provider &#x60;&#39;O&#39;&#x60; | Not Deemed a Medical Necessity &#x60;&#39;P&#39;&#x60; | Benefit Disclaimer &#x60;&#39;Q&#39;&#x60; | Second Surgical Opinion Required &#x60;&#39;R&#39;&#x60; | Other or Additional Payor &#x60;&#39;S&#39;&#x60; | Prior Year(s) History &#x60;&#39;T&#39;&#x60; | Card(s) Reported Lost/Stolen &#x60;&#39;U&#39;&#x60; | Contact Following Entity for Eligibility or Benefit Information &#x60;&#39;V&#39;&#x60; | Cannot Process &#x60;&#39;W&#39;&#x60; | Other Source of Data &#x60;&#39;X&#39;&#x60; | Health Care Facility &#x60;&#39;Y&#39;&#x60; | Spend Down  |  [optional] |
|**patient** | **String** |  |  [optional] [readonly] |
|**payerName** | **String** | The name of the payer as returned by the clearinghouse that ran the eligibility check |  [optional] |
|**queryDate** | **String** | The time at which the request was made |  [optional] [readonly] |
|**requestServiceType** | [**RequestServiceTypeEnum**](#RequestServiceTypeEnum) |  Value | Description --- | ---- &#x60;&#39;1&#39;&#x60; | Medical Care &#x60;&#39;2&#39;&#x60; | Surgical &#x60;&#39;3&#39;&#x60; | Consultation &#x60;&#39;4&#39;&#x60; | Diagnostic X-Ray &#x60;&#39;5&#39;&#x60; | Diagnostic Lab &#x60;&#39;6&#39;&#x60; | Radiation Therapy &#x60;&#39;7&#39;&#x60; | Anesthesia &#x60;&#39;8&#39;&#x60; | Surgical Assistance &#x60;&#39;9&#39;&#x60; | Other Medical &#x60;&#39;10&#39;&#x60; | Blood Charges &#x60;&#39;11&#39;&#x60; | Used Durable Medical Equipment &#x60;&#39;12&#39;&#x60; | Durable Medical Equipment Purchase &#x60;&#39;13&#39;&#x60; | Ambulatory Service Center Facility &#x60;&#39;14&#39;&#x60; | Renal Supplies in the Home &#x60;&#39;15&#39;&#x60; | Alternate Method Dialysis &#x60;&#39;16&#39;&#x60; | Chronic Renal Disease (CRD) Equipment &#x60;&#39;17&#39;&#x60; | Pre-Admission Testing &#x60;&#39;18&#39;&#x60; | Durable Medical Equipment Rental &#x60;&#39;19&#39;&#x60; | Pneumonia Vaccine &#x60;&#39;20&#39;&#x60; | Second Surgical Opinion &#x60;&#39;21&#39;&#x60; | Third Surgical Opinion &#x60;&#39;22&#39;&#x60; | Social Work &#x60;&#39;23&#39;&#x60; | Diagnostic Dental &#x60;&#39;24&#39;&#x60; | Periodontics &#x60;&#39;25&#39;&#x60; | Restorative &#x60;&#39;26&#39;&#x60; | Endodontics &#x60;&#39;27&#39;&#x60; | Maxillofacial Prosthetics &#x60;&#39;28&#39;&#x60; | Adjunctive Dental Services &#x60;&#39;30&#39;&#x60; | Health Benefit Plan Coverage &#x60;&#39;32&#39;&#x60; | Plan Waiting Period &#x60;&#39;33&#39;&#x60; | Chiropractic &#x60;&#39;34&#39;&#x60; | Chiropractic Office Visits &#x60;&#39;35&#39;&#x60; | Dental Care &#x60;&#39;36&#39;&#x60; | Dental Crowns &#x60;&#39;37&#39;&#x60; | Dental Accident &#x60;&#39;38&#39;&#x60; | Orthodontics &#x60;&#39;39&#39;&#x60; | Prosthodontics &#x60;&#39;40&#39;&#x60; | Oral Surgery &#x60;&#39;41&#39;&#x60; | Routine (Preventive) Dental &#x60;&#39;42&#39;&#x60; | Home Health Care &#x60;&#39;43&#39;&#x60; | Home Health Prescriptions &#x60;&#39;44&#39;&#x60; | Home Health Visits &#x60;&#39;45&#39;&#x60; | Hospice &#x60;&#39;46&#39;&#x60; | Respite Care &#x60;&#39;47&#39;&#x60; | Hospital &#x60;&#39;48&#39;&#x60; | Hospital - Inpatient &#x60;&#39;49&#39;&#x60; | Hospital - Room and Board &#x60;&#39;50&#39;&#x60; | Hospital - Outpatient &#x60;&#39;51&#39;&#x60; | Hospital - Emergency Accident &#x60;&#39;52&#39;&#x60; | Hospital - Emergency Medical &#x60;&#39;53&#39;&#x60; | Hospital - Ambulatory Surgical &#x60;&#39;54&#39;&#x60; | Long Term Care &#x60;&#39;55&#39;&#x60; | Major Medical &#x60;&#39;56&#39;&#x60; | Medically Related Transportation &#x60;&#39;57&#39;&#x60; | Air Transportation &#x60;&#39;58&#39;&#x60; | Cabulance &#x60;&#39;59&#39;&#x60; | Licensed Ambulance &#x60;&#39;60&#39;&#x60; | General Benefits &#x60;&#39;61&#39;&#x60; | In-vitro Fertilization &#x60;&#39;62&#39;&#x60; | MRI/CAT Scan &#x60;&#39;63&#39;&#x60; | Donor Procedures &#x60;&#39;64&#39;&#x60; | Acupuncture &#x60;&#39;65&#39;&#x60; | Newborn Care &#x60;&#39;66&#39;&#x60; | Pathology &#x60;&#39;67&#39;&#x60; | Smoking Cessation &#x60;&#39;68&#39;&#x60; | Well Baby Care &#x60;&#39;69&#39;&#x60; | Maternity &#x60;&#39;70&#39;&#x60; | Transplants &#x60;&#39;71&#39;&#x60; | Audiology Exam &#x60;&#39;72&#39;&#x60; | Inhalation Therapy &#x60;&#39;73&#39;&#x60; | Diagnostic Medical &#x60;&#39;74&#39;&#x60; | Private Duty Nursing &#x60;&#39;75&#39;&#x60; | Prosthetic Device &#x60;&#39;76&#39;&#x60; | Dialysis &#x60;&#39;77&#39;&#x60; | Otological Exam &#x60;&#39;78&#39;&#x60; | Chemotherapy &#x60;&#39;79&#39;&#x60; | Allergy Testing &#x60;&#39;80&#39;&#x60; | Immunizations &#x60;&#39;81&#39;&#x60; | Routine Physical &#x60;&#39;82&#39;&#x60; | Family Planning &#x60;&#39;83&#39;&#x60; | Infertility &#x60;&#39;84&#39;&#x60; | Abortion &#x60;&#39;85&#39;&#x60; | AIDS &#x60;&#39;86&#39;&#x60; | Emergency Services &#x60;&#39;87&#39;&#x60; | Cancer &#x60;&#39;88&#39;&#x60; | Pharmacy &#x60;&#39;89&#39;&#x60; | Free Standing Prescription Drug &#x60;&#39;90&#39;&#x60; | Mail Order Prescription Drug &#x60;&#39;91&#39;&#x60; | Brand Name Prescription Drug &#x60;&#39;92&#39;&#x60; | Generic Prescription Drug &#x60;&#39;93&#39;&#x60; | Podiatry &#x60;&#39;94&#39;&#x60; | Podiatry - Office Visits &#x60;&#39;95&#39;&#x60; | Podiatry - Nursing Home Visits &#x60;&#39;96&#39;&#x60; | Professional (Physician) &#x60;&#39;97&#39;&#x60; | Anesthesiologist &#x60;&#39;98&#39;&#x60; | Professional (Physician) Visit - Office &#x60;&#39;99&#39;&#x60; | Professional (Physician) Visit - Inpatient &#x60;&#39;A0&#39;&#x60; | Professional (Physician) Visit - Outpatient &#x60;&#39;A1&#39;&#x60; | Professional (Physician) Visit - Nursing Home &#x60;&#39;A2&#39;&#x60; | Professional (Physician) Visit - Skilled Nursing Facility &#x60;&#39;A3&#39;&#x60; | Professional (Physician) Visit - Home &#x60;&#39;A4&#39;&#x60; | Psychiatric &#x60;&#39;A5&#39;&#x60; | Psychiatric - Room and Board &#x60;&#39;A6&#39;&#x60; | Psychotherapy &#x60;&#39;A7&#39;&#x60; | Psychiatric - Inpatient &#x60;&#39;A8&#39;&#x60; | Psychiatric - Outpatient &#x60;&#39;A9&#39;&#x60; | Rehabilitation &#x60;&#39;AA&#39;&#x60; | Rehabilitation - Room and Board &#x60;&#39;AB&#39;&#x60; | Rehabilitation - Inpatient &#x60;&#39;AC&#39;&#x60; | Rehabilitation - Outpatient &#x60;&#39;AD&#39;&#x60; | Occupational Therapy &#x60;&#39;AE&#39;&#x60; | Physical Medicine &#x60;&#39;AF&#39;&#x60; | Speech Therapy &#x60;&#39;AG&#39;&#x60; | Skilled Nursing Care &#x60;&#39;AH&#39;&#x60; | Skilled Nursing Care - Room and Board &#x60;&#39;AI&#39;&#x60; | Substance Abuse &#x60;&#39;AJ&#39;&#x60; | Alcoholism &#x60;&#39;AK&#39;&#x60; | Drug Addiction &#x60;&#39;AL&#39;&#x60; | Vision (Optometry) &#x60;&#39;AM&#39;&#x60; | Frames &#x60;&#39;AN&#39;&#x60; | Routine Exam &#x60;&#39;AO&#39;&#x60; | Lenses &#x60;&#39;AQ&#39;&#x60; | Nonmedically Necessary Physical &#x60;&#39;AR&#39;&#x60; | Experimental Drug Therapy &#x60;&#39;B1&#39;&#x60; | Burn Care &#x60;&#39;B2&#39;&#x60; | Brand Name Prescription Drug - Formulary &#x60;&#39;B3&#39;&#x60; | Brand Name Prescription Drug - Non-Formulary &#x60;&#39;BA&#39;&#x60; | Independent Medical Evaluation &#x60;&#39;BB&#39;&#x60; | Partial Hospitalization (Psychiatric) &#x60;&#39;BC&#39;&#x60; | Day Care (Psychiatric) &#x60;&#39;BD&#39;&#x60; | Cognitive Therapy &#x60;&#39;BE&#39;&#x60; | Massage Therapy &#x60;&#39;BF&#39;&#x60; | Pulmonary Rehabilitation &#x60;&#39;BG&#39;&#x60; | Cardiac Rehabilitation &#x60;&#39;BH&#39;&#x60; | Pediatric &#x60;&#39;BI&#39;&#x60; | Nursery &#x60;&#39;BJ&#39;&#x60; | Skin &#x60;&#39;BK&#39;&#x60; | Orthopedic &#x60;&#39;BL&#39;&#x60; | Cardiac &#x60;&#39;BM&#39;&#x60; | Lymphatic &#x60;&#39;BN&#39;&#x60; | Gastrointestinal &#x60;&#39;BP&#39;&#x60; | Endocrine &#x60;&#39;BQ&#39;&#x60; | Neurology &#x60;&#39;BR&#39;&#x60; | Eye &#x60;&#39;BS&#39;&#x60; | Invasive Procedures &#x60;&#39;BT&#39;&#x60; | Gynecological &#x60;&#39;BU&#39;&#x60; | Obstetrical &#x60;&#39;BV&#39;&#x60; | Obstetrical/Gynecological &#x60;&#39;BW&#39;&#x60; | Mail Order Prescription Drug: Brand Name &#x60;&#39;BX&#39;&#x60; | Mail Order Prescription Drug: Generic &#x60;&#39;BY&#39;&#x60; | Physician Visit - Office: Sick &#x60;&#39;BZ&#39;&#x60; | Physician Visit - Office: Well &#x60;&#39;C1&#39;&#x60; | Coronary Care &#x60;&#39;CA&#39;&#x60; | Private Duty Nursing - Inpatient &#x60;&#39;CB&#39;&#x60; | Private Duty Nursing - Home &#x60;&#39;CC&#39;&#x60; | Surgical Benefits - Professional (Physician) &#x60;&#39;CD&#39;&#x60; | Surgical Benefits - Facility &#x60;&#39;CE&#39;&#x60; | Mental Health Provider - Inpatient &#x60;&#39;CF&#39;&#x60; | Mental Health Provider - Outpatient &#x60;&#39;CG&#39;&#x60; | Mental Health Facility - Inpatient &#x60;&#39;CH&#39;&#x60; | Mental Health Facility - Outpatient &#x60;&#39;CI&#39;&#x60; | Substance Abuse Facility - Inpatient &#x60;&#39;CJ&#39;&#x60; | Substance Abuse Facility - Outpatient &#x60;&#39;CK&#39;&#x60; | Screening X-ray &#x60;&#39;CL&#39;&#x60; | Screening laboratory &#x60;&#39;CM&#39;&#x60; | Mammogram, High Risk Patient &#x60;&#39;CN&#39;&#x60; | Mammogram, Low Risk Patient &#x60;&#39;CO&#39;&#x60; | Flu Vaccination &#x60;&#39;CP&#39;&#x60; | Eyewear and Eyewear Accessories &#x60;&#39;CQ&#39;&#x60; | Case Management &#x60;&#39;DG&#39;&#x60; | Dermatology &#x60;&#39;DM&#39;&#x60; | Durable Medical Equipment &#x60;&#39;DS&#39;&#x60; | Diabetic Supplies &#x60;&#39;GF&#39;&#x60; | Generic Prescription Drug - Formulary &#x60;&#39;GN&#39;&#x60; | Generic Prescription Drug - Non-Formulary &#x60;&#39;GY&#39;&#x60; | Allergy &#x60;&#39;IC&#39;&#x60; | Intensive Care &#x60;&#39;MH&#39;&#x60; | Mental Health &#x60;&#39;NI&#39;&#x60; | Neonatal Intensive Care &#x60;&#39;ON&#39;&#x60; | Oncology &#x60;&#39;PT&#39;&#x60; | Physical Therapy &#x60;&#39;PU&#39;&#x60; | Pulmonary &#x60;&#39;RN&#39;&#x60; | Renal &#x60;&#39;RT&#39;&#x60; | Residential Psychiatric Treatment &#x60;&#39;TC&#39;&#x60; | Transitional Care &#x60;&#39;TN&#39;&#x60; | Transitional Nursery Care &#x60;&#39;UC&#39;&#x60; | Urgent Care  |  [optional] |
|**serviceTypeDescription** | **String** |  |  [optional] [readonly] |



## Enum: RequestServiceTypeEnum

| Name | Value |
|---- | -----|
| _1 | &quot;1&quot; |
| _2 | &quot;2&quot; |
| _3 | &quot;3&quot; |
| _4 | &quot;4&quot; |
| _5 | &quot;5&quot; |
| _6 | &quot;6&quot; |
| _7 | &quot;7&quot; |
| _8 | &quot;8&quot; |
| _9 | &quot;9&quot; |
| _10 | &quot;10&quot; |
| _11 | &quot;11&quot; |
| _12 | &quot;12&quot; |
| _13 | &quot;13&quot; |
| _14 | &quot;14&quot; |
| _15 | &quot;15&quot; |
| _16 | &quot;16&quot; |
| _17 | &quot;17&quot; |
| _18 | &quot;18&quot; |
| _19 | &quot;19&quot; |
| _20 | &quot;20&quot; |
| _21 | &quot;21&quot; |
| _22 | &quot;22&quot; |
| _23 | &quot;23&quot; |
| _24 | &quot;24&quot; |
| _25 | &quot;25&quot; |
| _26 | &quot;26&quot; |
| _27 | &quot;27&quot; |
| _28 | &quot;28&quot; |
| _30 | &quot;30&quot; |
| _32 | &quot;32&quot; |
| _33 | &quot;33&quot; |
| _34 | &quot;34&quot; |
| _35 | &quot;35&quot; |
| _36 | &quot;36&quot; |
| _37 | &quot;37&quot; |
| _38 | &quot;38&quot; |
| _39 | &quot;39&quot; |
| _40 | &quot;40&quot; |
| _41 | &quot;41&quot; |
| _42 | &quot;42&quot; |
| _43 | &quot;43&quot; |
| _44 | &quot;44&quot; |
| _45 | &quot;45&quot; |
| _46 | &quot;46&quot; |
| _47 | &quot;47&quot; |
| _48 | &quot;48&quot; |
| _49 | &quot;49&quot; |
| _50 | &quot;50&quot; |
| _51 | &quot;51&quot; |
| _52 | &quot;52&quot; |
| _53 | &quot;53&quot; |
| _54 | &quot;54&quot; |
| _55 | &quot;55&quot; |
| _56 | &quot;56&quot; |
| _57 | &quot;57&quot; |
| _58 | &quot;58&quot; |
| _59 | &quot;59&quot; |
| _60 | &quot;60&quot; |
| _61 | &quot;61&quot; |
| _62 | &quot;62&quot; |
| _63 | &quot;63&quot; |
| _64 | &quot;64&quot; |
| _65 | &quot;65&quot; |
| _66 | &quot;66&quot; |
| _67 | &quot;67&quot; |
| _68 | &quot;68&quot; |
| _69 | &quot;69&quot; |
| _70 | &quot;70&quot; |
| _71 | &quot;71&quot; |
| _72 | &quot;72&quot; |
| _73 | &quot;73&quot; |
| _74 | &quot;74&quot; |
| _75 | &quot;75&quot; |
| _76 | &quot;76&quot; |
| _77 | &quot;77&quot; |
| _78 | &quot;78&quot; |
| _79 | &quot;79&quot; |
| _80 | &quot;80&quot; |
| _81 | &quot;81&quot; |
| _82 | &quot;82&quot; |
| _83 | &quot;83&quot; |
| _84 | &quot;84&quot; |
| _85 | &quot;85&quot; |
| _86 | &quot;86&quot; |
| _87 | &quot;87&quot; |
| _88 | &quot;88&quot; |
| _89 | &quot;89&quot; |
| _90 | &quot;90&quot; |
| _91 | &quot;91&quot; |
| _92 | &quot;92&quot; |
| _93 | &quot;93&quot; |
| _94 | &quot;94&quot; |
| _95 | &quot;95&quot; |
| _96 | &quot;96&quot; |
| _97 | &quot;97&quot; |
| _98 | &quot;98&quot; |
| _99 | &quot;99&quot; |
| A0 | &quot;A0&quot; |
| A1 | &quot;A1&quot; |
| A2 | &quot;A2&quot; |
| A3 | &quot;A3&quot; |
| A4 | &quot;A4&quot; |
| A5 | &quot;A5&quot; |
| A6 | &quot;A6&quot; |
| A7 | &quot;A7&quot; |
| A8 | &quot;A8&quot; |
| A9 | &quot;A9&quot; |
| AA | &quot;AA&quot; |
| AB | &quot;AB&quot; |
| AC | &quot;AC&quot; |
| AD | &quot;AD&quot; |
| AE | &quot;AE&quot; |
| AF | &quot;AF&quot; |
| AG | &quot;AG&quot; |
| AH | &quot;AH&quot; |
| AI | &quot;AI&quot; |
| AJ | &quot;AJ&quot; |
| AK | &quot;AK&quot; |
| AL | &quot;AL&quot; |
| AM | &quot;AM&quot; |
| AN | &quot;AN&quot; |
| AO | &quot;AO&quot; |
| AQ | &quot;AQ&quot; |
| AR | &quot;AR&quot; |
| B1 | &quot;B1&quot; |
| B2 | &quot;B2&quot; |
| B3 | &quot;B3&quot; |
| BA | &quot;BA&quot; |
| BB | &quot;BB&quot; |
| BC | &quot;BC&quot; |
| BD | &quot;BD&quot; |
| BE | &quot;BE&quot; |
| BF | &quot;BF&quot; |
| BG | &quot;BG&quot; |
| BH | &quot;BH&quot; |
| BI | &quot;BI&quot; |
| BJ | &quot;BJ&quot; |
| BK | &quot;BK&quot; |
| BL | &quot;BL&quot; |
| BM | &quot;BM&quot; |
| BN | &quot;BN&quot; |
| BP | &quot;BP&quot; |
| BQ | &quot;BQ&quot; |
| BR | &quot;BR&quot; |
| BS | &quot;BS&quot; |
| BT | &quot;BT&quot; |
| BU | &quot;BU&quot; |
| BV | &quot;BV&quot; |
| BW | &quot;BW&quot; |
| BX | &quot;BX&quot; |
| BY | &quot;BY&quot; |
| BZ | &quot;BZ&quot; |
| C1 | &quot;C1&quot; |
| CA | &quot;CA&quot; |
| CB | &quot;CB&quot; |
| CC | &quot;CC&quot; |
| CD | &quot;CD&quot; |
| CE | &quot;CE&quot; |
| CF | &quot;CF&quot; |
| CG | &quot;CG&quot; |
| CH | &quot;CH&quot; |
| CI | &quot;CI&quot; |
| CJ | &quot;CJ&quot; |
| CK | &quot;CK&quot; |
| CL | &quot;CL&quot; |
| CM | &quot;CM&quot; |
| CN | &quot;CN&quot; |
| CO | &quot;CO&quot; |
| CP | &quot;CP&quot; |
| CQ | &quot;CQ&quot; |
| DG | &quot;DG&quot; |
| DM | &quot;DM&quot; |
| DS | &quot;DS&quot; |
| GF | &quot;GF&quot; |
| GN | &quot;GN&quot; |
| GY | &quot;GY&quot; |
| IC | &quot;IC&quot; |
| MH | &quot;MH&quot; |
| NI | &quot;NI&quot; |
| TRUE | &quot;true&quot; |
| PT | &quot;PT&quot; |
| PU | &quot;PU&quot; |
| RN | &quot;RN&quot; |
| RT | &quot;RT&quot; |
| TC | &quot;TC&quot; |
| TN | &quot;TN&quot; |
| UC | &quot;UC&quot; |



