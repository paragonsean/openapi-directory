# OpenapiJsClient.Coverage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointment** | **String** |  | [optional] [readonly] 
**cobLevel** | **String** | The level of insurance the eligibility check was run on. Can be one of the following: &#x60;Primary Insurance&#x60; or &#x60;Secondary Insurance&#x60; | [optional] [readonly] 
**coverageDetails** | **String** | A variable size object containing the details of the eligibility check, if returned by the clearinghouse that ran the eligibility check | [optional] [readonly] 
**coverageSubscriber** | **String** | A variable size object containing subscriber information, if returned by the clearinghouse that ran the eligibility check | [optional] [readonly] 
**eligibility** | **String** |  Value | Description --- | ---- &#x60;&#39;1&#39;&#x60; | Active Coverage &#x60;&#39;2&#39;&#x60; | Active - Full Risk Capitation &#x60;&#39;3&#39;&#x60; | Active - Services Capitated &#x60;&#39;4&#39;&#x60; | Active - Services Capitated to Primary Care Physician &#x60;&#39;5&#39;&#x60; | Active - Pending Investigation &#x60;&#39;6&#39;&#x60; | Inactive &#x60;&#39;7&#39;&#x60; | Inactive - Pending Eligibility Update &#x60;&#39;8&#39;&#x60; | Inactive - Pending Investigation &#x60;&#39;A&#39;&#x60; | Co-Insurance &#x60;&#39;B&#39;&#x60; | Co-Payment &#x60;&#39;C&#39;&#x60; | Deductible &#x60;&#39;CB&#39;&#x60; | Coverage Basis &#x60;&#39;D&#39;&#x60; | Benefit Description &#x60;&#39;E&#39;&#x60; | Exclusions &#x60;&#39;F&#39;&#x60; | Limitations &#x60;&#39;G&#39;&#x60; | Out of Pocket (Stop Loss) &#x60;&#39;H&#39;&#x60; | Unlimited &#x60;&#39;I&#39;&#x60; | Non-Covered &#x60;&#39;J&#39;&#x60; | Cost Containment &#x60;&#39;K&#39;&#x60; | Reserve &#x60;&#39;L&#39;&#x60; | Primary Care Provider &#x60;&#39;M&#39;&#x60; | Pre-existing Condition &#x60;&#39;MC&#39;&#x60; | Managed Care Coordinator &#x60;&#39;N&#39;&#x60; | Services Restricted to Following Provider &#x60;&#39;O&#39;&#x60; | Not Deemed a Medical Necessity &#x60;&#39;P&#39;&#x60; | Benefit Disclaimer &#x60;&#39;Q&#39;&#x60; | Second Surgical Opinion Required &#x60;&#39;R&#39;&#x60; | Other or Additional Payor &#x60;&#39;S&#39;&#x60; | Prior Year(s) History &#x60;&#39;T&#39;&#x60; | Card(s) Reported Lost/Stolen &#x60;&#39;U&#39;&#x60; | Contact Following Entity for Eligibility or Benefit Information &#x60;&#39;V&#39;&#x60; | Cannot Process &#x60;&#39;W&#39;&#x60; | Other Source of Data &#x60;&#39;X&#39;&#x60; | Health Care Facility &#x60;&#39;Y&#39;&#x60; | Spend Down  | [optional] 
**patient** | **String** |  | [optional] [readonly] 
**payerName** | **String** | The name of the payer as returned by the clearinghouse that ran the eligibility check | [optional] 
**queryDate** | **String** | The time at which the request was made | [optional] [readonly] 
**requestServiceType** | **String** |  Value | Description --- | ---- &#x60;&#39;1&#39;&#x60; | Medical Care &#x60;&#39;2&#39;&#x60; | Surgical &#x60;&#39;3&#39;&#x60; | Consultation &#x60;&#39;4&#39;&#x60; | Diagnostic X-Ray &#x60;&#39;5&#39;&#x60; | Diagnostic Lab &#x60;&#39;6&#39;&#x60; | Radiation Therapy &#x60;&#39;7&#39;&#x60; | Anesthesia &#x60;&#39;8&#39;&#x60; | Surgical Assistance &#x60;&#39;9&#39;&#x60; | Other Medical &#x60;&#39;10&#39;&#x60; | Blood Charges &#x60;&#39;11&#39;&#x60; | Used Durable Medical Equipment &#x60;&#39;12&#39;&#x60; | Durable Medical Equipment Purchase &#x60;&#39;13&#39;&#x60; | Ambulatory Service Center Facility &#x60;&#39;14&#39;&#x60; | Renal Supplies in the Home &#x60;&#39;15&#39;&#x60; | Alternate Method Dialysis &#x60;&#39;16&#39;&#x60; | Chronic Renal Disease (CRD) Equipment &#x60;&#39;17&#39;&#x60; | Pre-Admission Testing &#x60;&#39;18&#39;&#x60; | Durable Medical Equipment Rental &#x60;&#39;19&#39;&#x60; | Pneumonia Vaccine &#x60;&#39;20&#39;&#x60; | Second Surgical Opinion &#x60;&#39;21&#39;&#x60; | Third Surgical Opinion &#x60;&#39;22&#39;&#x60; | Social Work &#x60;&#39;23&#39;&#x60; | Diagnostic Dental &#x60;&#39;24&#39;&#x60; | Periodontics &#x60;&#39;25&#39;&#x60; | Restorative &#x60;&#39;26&#39;&#x60; | Endodontics &#x60;&#39;27&#39;&#x60; | Maxillofacial Prosthetics &#x60;&#39;28&#39;&#x60; | Adjunctive Dental Services &#x60;&#39;30&#39;&#x60; | Health Benefit Plan Coverage &#x60;&#39;32&#39;&#x60; | Plan Waiting Period &#x60;&#39;33&#39;&#x60; | Chiropractic &#x60;&#39;34&#39;&#x60; | Chiropractic Office Visits &#x60;&#39;35&#39;&#x60; | Dental Care &#x60;&#39;36&#39;&#x60; | Dental Crowns &#x60;&#39;37&#39;&#x60; | Dental Accident &#x60;&#39;38&#39;&#x60; | Orthodontics &#x60;&#39;39&#39;&#x60; | Prosthodontics &#x60;&#39;40&#39;&#x60; | Oral Surgery &#x60;&#39;41&#39;&#x60; | Routine (Preventive) Dental &#x60;&#39;42&#39;&#x60; | Home Health Care &#x60;&#39;43&#39;&#x60; | Home Health Prescriptions &#x60;&#39;44&#39;&#x60; | Home Health Visits &#x60;&#39;45&#39;&#x60; | Hospice &#x60;&#39;46&#39;&#x60; | Respite Care &#x60;&#39;47&#39;&#x60; | Hospital &#x60;&#39;48&#39;&#x60; | Hospital - Inpatient &#x60;&#39;49&#39;&#x60; | Hospital - Room and Board &#x60;&#39;50&#39;&#x60; | Hospital - Outpatient &#x60;&#39;51&#39;&#x60; | Hospital - Emergency Accident &#x60;&#39;52&#39;&#x60; | Hospital - Emergency Medical &#x60;&#39;53&#39;&#x60; | Hospital - Ambulatory Surgical &#x60;&#39;54&#39;&#x60; | Long Term Care &#x60;&#39;55&#39;&#x60; | Major Medical &#x60;&#39;56&#39;&#x60; | Medically Related Transportation &#x60;&#39;57&#39;&#x60; | Air Transportation &#x60;&#39;58&#39;&#x60; | Cabulance &#x60;&#39;59&#39;&#x60; | Licensed Ambulance &#x60;&#39;60&#39;&#x60; | General Benefits &#x60;&#39;61&#39;&#x60; | In-vitro Fertilization &#x60;&#39;62&#39;&#x60; | MRI/CAT Scan &#x60;&#39;63&#39;&#x60; | Donor Procedures &#x60;&#39;64&#39;&#x60; | Acupuncture &#x60;&#39;65&#39;&#x60; | Newborn Care &#x60;&#39;66&#39;&#x60; | Pathology &#x60;&#39;67&#39;&#x60; | Smoking Cessation &#x60;&#39;68&#39;&#x60; | Well Baby Care &#x60;&#39;69&#39;&#x60; | Maternity &#x60;&#39;70&#39;&#x60; | Transplants &#x60;&#39;71&#39;&#x60; | Audiology Exam &#x60;&#39;72&#39;&#x60; | Inhalation Therapy &#x60;&#39;73&#39;&#x60; | Diagnostic Medical &#x60;&#39;74&#39;&#x60; | Private Duty Nursing &#x60;&#39;75&#39;&#x60; | Prosthetic Device &#x60;&#39;76&#39;&#x60; | Dialysis &#x60;&#39;77&#39;&#x60; | Otological Exam &#x60;&#39;78&#39;&#x60; | Chemotherapy &#x60;&#39;79&#39;&#x60; | Allergy Testing &#x60;&#39;80&#39;&#x60; | Immunizations &#x60;&#39;81&#39;&#x60; | Routine Physical &#x60;&#39;82&#39;&#x60; | Family Planning &#x60;&#39;83&#39;&#x60; | Infertility &#x60;&#39;84&#39;&#x60; | Abortion &#x60;&#39;85&#39;&#x60; | AIDS &#x60;&#39;86&#39;&#x60; | Emergency Services &#x60;&#39;87&#39;&#x60; | Cancer &#x60;&#39;88&#39;&#x60; | Pharmacy &#x60;&#39;89&#39;&#x60; | Free Standing Prescription Drug &#x60;&#39;90&#39;&#x60; | Mail Order Prescription Drug &#x60;&#39;91&#39;&#x60; | Brand Name Prescription Drug &#x60;&#39;92&#39;&#x60; | Generic Prescription Drug &#x60;&#39;93&#39;&#x60; | Podiatry &#x60;&#39;94&#39;&#x60; | Podiatry - Office Visits &#x60;&#39;95&#39;&#x60; | Podiatry - Nursing Home Visits &#x60;&#39;96&#39;&#x60; | Professional (Physician) &#x60;&#39;97&#39;&#x60; | Anesthesiologist &#x60;&#39;98&#39;&#x60; | Professional (Physician) Visit - Office &#x60;&#39;99&#39;&#x60; | Professional (Physician) Visit - Inpatient &#x60;&#39;A0&#39;&#x60; | Professional (Physician) Visit - Outpatient &#x60;&#39;A1&#39;&#x60; | Professional (Physician) Visit - Nursing Home &#x60;&#39;A2&#39;&#x60; | Professional (Physician) Visit - Skilled Nursing Facility &#x60;&#39;A3&#39;&#x60; | Professional (Physician) Visit - Home &#x60;&#39;A4&#39;&#x60; | Psychiatric &#x60;&#39;A5&#39;&#x60; | Psychiatric - Room and Board &#x60;&#39;A6&#39;&#x60; | Psychotherapy &#x60;&#39;A7&#39;&#x60; | Psychiatric - Inpatient &#x60;&#39;A8&#39;&#x60; | Psychiatric - Outpatient &#x60;&#39;A9&#39;&#x60; | Rehabilitation &#x60;&#39;AA&#39;&#x60; | Rehabilitation - Room and Board &#x60;&#39;AB&#39;&#x60; | Rehabilitation - Inpatient &#x60;&#39;AC&#39;&#x60; | Rehabilitation - Outpatient &#x60;&#39;AD&#39;&#x60; | Occupational Therapy &#x60;&#39;AE&#39;&#x60; | Physical Medicine &#x60;&#39;AF&#39;&#x60; | Speech Therapy &#x60;&#39;AG&#39;&#x60; | Skilled Nursing Care &#x60;&#39;AH&#39;&#x60; | Skilled Nursing Care - Room and Board &#x60;&#39;AI&#39;&#x60; | Substance Abuse &#x60;&#39;AJ&#39;&#x60; | Alcoholism &#x60;&#39;AK&#39;&#x60; | Drug Addiction &#x60;&#39;AL&#39;&#x60; | Vision (Optometry) &#x60;&#39;AM&#39;&#x60; | Frames &#x60;&#39;AN&#39;&#x60; | Routine Exam &#x60;&#39;AO&#39;&#x60; | Lenses &#x60;&#39;AQ&#39;&#x60; | Nonmedically Necessary Physical &#x60;&#39;AR&#39;&#x60; | Experimental Drug Therapy &#x60;&#39;B1&#39;&#x60; | Burn Care &#x60;&#39;B2&#39;&#x60; | Brand Name Prescription Drug - Formulary &#x60;&#39;B3&#39;&#x60; | Brand Name Prescription Drug - Non-Formulary &#x60;&#39;BA&#39;&#x60; | Independent Medical Evaluation &#x60;&#39;BB&#39;&#x60; | Partial Hospitalization (Psychiatric) &#x60;&#39;BC&#39;&#x60; | Day Care (Psychiatric) &#x60;&#39;BD&#39;&#x60; | Cognitive Therapy &#x60;&#39;BE&#39;&#x60; | Massage Therapy &#x60;&#39;BF&#39;&#x60; | Pulmonary Rehabilitation &#x60;&#39;BG&#39;&#x60; | Cardiac Rehabilitation &#x60;&#39;BH&#39;&#x60; | Pediatric &#x60;&#39;BI&#39;&#x60; | Nursery &#x60;&#39;BJ&#39;&#x60; | Skin &#x60;&#39;BK&#39;&#x60; | Orthopedic &#x60;&#39;BL&#39;&#x60; | Cardiac &#x60;&#39;BM&#39;&#x60; | Lymphatic &#x60;&#39;BN&#39;&#x60; | Gastrointestinal &#x60;&#39;BP&#39;&#x60; | Endocrine &#x60;&#39;BQ&#39;&#x60; | Neurology &#x60;&#39;BR&#39;&#x60; | Eye &#x60;&#39;BS&#39;&#x60; | Invasive Procedures &#x60;&#39;BT&#39;&#x60; | Gynecological &#x60;&#39;BU&#39;&#x60; | Obstetrical &#x60;&#39;BV&#39;&#x60; | Obstetrical/Gynecological &#x60;&#39;BW&#39;&#x60; | Mail Order Prescription Drug: Brand Name &#x60;&#39;BX&#39;&#x60; | Mail Order Prescription Drug: Generic &#x60;&#39;BY&#39;&#x60; | Physician Visit - Office: Sick &#x60;&#39;BZ&#39;&#x60; | Physician Visit - Office: Well &#x60;&#39;C1&#39;&#x60; | Coronary Care &#x60;&#39;CA&#39;&#x60; | Private Duty Nursing - Inpatient &#x60;&#39;CB&#39;&#x60; | Private Duty Nursing - Home &#x60;&#39;CC&#39;&#x60; | Surgical Benefits - Professional (Physician) &#x60;&#39;CD&#39;&#x60; | Surgical Benefits - Facility &#x60;&#39;CE&#39;&#x60; | Mental Health Provider - Inpatient &#x60;&#39;CF&#39;&#x60; | Mental Health Provider - Outpatient &#x60;&#39;CG&#39;&#x60; | Mental Health Facility - Inpatient &#x60;&#39;CH&#39;&#x60; | Mental Health Facility - Outpatient &#x60;&#39;CI&#39;&#x60; | Substance Abuse Facility - Inpatient &#x60;&#39;CJ&#39;&#x60; | Substance Abuse Facility - Outpatient &#x60;&#39;CK&#39;&#x60; | Screening X-ray &#x60;&#39;CL&#39;&#x60; | Screening laboratory &#x60;&#39;CM&#39;&#x60; | Mammogram, High Risk Patient &#x60;&#39;CN&#39;&#x60; | Mammogram, Low Risk Patient &#x60;&#39;CO&#39;&#x60; | Flu Vaccination &#x60;&#39;CP&#39;&#x60; | Eyewear and Eyewear Accessories &#x60;&#39;CQ&#39;&#x60; | Case Management &#x60;&#39;DG&#39;&#x60; | Dermatology &#x60;&#39;DM&#39;&#x60; | Durable Medical Equipment &#x60;&#39;DS&#39;&#x60; | Diabetic Supplies &#x60;&#39;GF&#39;&#x60; | Generic Prescription Drug - Formulary &#x60;&#39;GN&#39;&#x60; | Generic Prescription Drug - Non-Formulary &#x60;&#39;GY&#39;&#x60; | Allergy &#x60;&#39;IC&#39;&#x60; | Intensive Care &#x60;&#39;MH&#39;&#x60; | Mental Health &#x60;&#39;NI&#39;&#x60; | Neonatal Intensive Care &#x60;&#39;ON&#39;&#x60; | Oncology &#x60;&#39;PT&#39;&#x60; | Physical Therapy &#x60;&#39;PU&#39;&#x60; | Pulmonary &#x60;&#39;RN&#39;&#x60; | Renal &#x60;&#39;RT&#39;&#x60; | Residential Psychiatric Treatment &#x60;&#39;TC&#39;&#x60; | Transitional Care &#x60;&#39;TN&#39;&#x60; | Transitional Nursery Care &#x60;&#39;UC&#39;&#x60; | Urgent Care  | [optional] 
**serviceTypeDescription** | **String** |  | [optional] [readonly] 



## Enum: RequestServiceTypeEnum


* `1` (value: `"1"`)

* `2` (value: `"2"`)

* `3` (value: `"3"`)

* `4` (value: `"4"`)

* `5` (value: `"5"`)

* `6` (value: `"6"`)

* `7` (value: `"7"`)

* `8` (value: `"8"`)

* `9` (value: `"9"`)

* `10` (value: `"10"`)

* `11` (value: `"11"`)

* `12` (value: `"12"`)

* `13` (value: `"13"`)

* `14` (value: `"14"`)

* `15` (value: `"15"`)

* `16` (value: `"16"`)

* `17` (value: `"17"`)

* `18` (value: `"18"`)

* `19` (value: `"19"`)

* `20` (value: `"20"`)

* `21` (value: `"21"`)

* `22` (value: `"22"`)

* `23` (value: `"23"`)

* `24` (value: `"24"`)

* `25` (value: `"25"`)

* `26` (value: `"26"`)

* `27` (value: `"27"`)

* `28` (value: `"28"`)

* `30` (value: `"30"`)

* `32` (value: `"32"`)

* `33` (value: `"33"`)

* `34` (value: `"34"`)

* `35` (value: `"35"`)

* `36` (value: `"36"`)

* `37` (value: `"37"`)

* `38` (value: `"38"`)

* `39` (value: `"39"`)

* `40` (value: `"40"`)

* `41` (value: `"41"`)

* `42` (value: `"42"`)

* `43` (value: `"43"`)

* `44` (value: `"44"`)

* `45` (value: `"45"`)

* `46` (value: `"46"`)

* `47` (value: `"47"`)

* `48` (value: `"48"`)

* `49` (value: `"49"`)

* `50` (value: `"50"`)

* `51` (value: `"51"`)

* `52` (value: `"52"`)

* `53` (value: `"53"`)

* `54` (value: `"54"`)

* `55` (value: `"55"`)

* `56` (value: `"56"`)

* `57` (value: `"57"`)

* `58` (value: `"58"`)

* `59` (value: `"59"`)

* `60` (value: `"60"`)

* `61` (value: `"61"`)

* `62` (value: `"62"`)

* `63` (value: `"63"`)

* `64` (value: `"64"`)

* `65` (value: `"65"`)

* `66` (value: `"66"`)

* `67` (value: `"67"`)

* `68` (value: `"68"`)

* `69` (value: `"69"`)

* `70` (value: `"70"`)

* `71` (value: `"71"`)

* `72` (value: `"72"`)

* `73` (value: `"73"`)

* `74` (value: `"74"`)

* `75` (value: `"75"`)

* `76` (value: `"76"`)

* `77` (value: `"77"`)

* `78` (value: `"78"`)

* `79` (value: `"79"`)

* `80` (value: `"80"`)

* `81` (value: `"81"`)

* `82` (value: `"82"`)

* `83` (value: `"83"`)

* `84` (value: `"84"`)

* `85` (value: `"85"`)

* `86` (value: `"86"`)

* `87` (value: `"87"`)

* `88` (value: `"88"`)

* `89` (value: `"89"`)

* `90` (value: `"90"`)

* `91` (value: `"91"`)

* `92` (value: `"92"`)

* `93` (value: `"93"`)

* `94` (value: `"94"`)

* `95` (value: `"95"`)

* `96` (value: `"96"`)

* `97` (value: `"97"`)

* `98` (value: `"98"`)

* `99` (value: `"99"`)

* `A0` (value: `"A0"`)

* `A1` (value: `"A1"`)

* `A2` (value: `"A2"`)

* `A3` (value: `"A3"`)

* `A4` (value: `"A4"`)

* `A5` (value: `"A5"`)

* `A6` (value: `"A6"`)

* `A7` (value: `"A7"`)

* `A8` (value: `"A8"`)

* `A9` (value: `"A9"`)

* `AA` (value: `"AA"`)

* `AB` (value: `"AB"`)

* `AC` (value: `"AC"`)

* `AD` (value: `"AD"`)

* `AE` (value: `"AE"`)

* `AF` (value: `"AF"`)

* `AG` (value: `"AG"`)

* `AH` (value: `"AH"`)

* `AI` (value: `"AI"`)

* `AJ` (value: `"AJ"`)

* `AK` (value: `"AK"`)

* `AL` (value: `"AL"`)

* `AM` (value: `"AM"`)

* `AN` (value: `"AN"`)

* `AO` (value: `"AO"`)

* `AQ` (value: `"AQ"`)

* `AR` (value: `"AR"`)

* `B1` (value: `"B1"`)

* `B2` (value: `"B2"`)

* `B3` (value: `"B3"`)

* `BA` (value: `"BA"`)

* `BB` (value: `"BB"`)

* `BC` (value: `"BC"`)

* `BD` (value: `"BD"`)

* `BE` (value: `"BE"`)

* `BF` (value: `"BF"`)

* `BG` (value: `"BG"`)

* `BH` (value: `"BH"`)

* `BI` (value: `"BI"`)

* `BJ` (value: `"BJ"`)

* `BK` (value: `"BK"`)

* `BL` (value: `"BL"`)

* `BM` (value: `"BM"`)

* `BN` (value: `"BN"`)

* `BP` (value: `"BP"`)

* `BQ` (value: `"BQ"`)

* `BR` (value: `"BR"`)

* `BS` (value: `"BS"`)

* `BT` (value: `"BT"`)

* `BU` (value: `"BU"`)

* `BV` (value: `"BV"`)

* `BW` (value: `"BW"`)

* `BX` (value: `"BX"`)

* `BY` (value: `"BY"`)

* `BZ` (value: `"BZ"`)

* `C1` (value: `"C1"`)

* `CA` (value: `"CA"`)

* `CB` (value: `"CB"`)

* `CC` (value: `"CC"`)

* `CD` (value: `"CD"`)

* `CE` (value: `"CE"`)

* `CF` (value: `"CF"`)

* `CG` (value: `"CG"`)

* `CH` (value: `"CH"`)

* `CI` (value: `"CI"`)

* `CJ` (value: `"CJ"`)

* `CK` (value: `"CK"`)

* `CL` (value: `"CL"`)

* `CM` (value: `"CM"`)

* `CN` (value: `"CN"`)

* `CO` (value: `"CO"`)

* `CP` (value: `"CP"`)

* `CQ` (value: `"CQ"`)

* `DG` (value: `"DG"`)

* `DM` (value: `"DM"`)

* `DS` (value: `"DS"`)

* `GF` (value: `"GF"`)

* `GN` (value: `"GN"`)

* `GY` (value: `"GY"`)

* `IC` (value: `"IC"`)

* `MH` (value: `"MH"`)

* `NI` (value: `"NI"`)

* `true` (value: `"true"`)

* `PT` (value: `"PT"`)

* `PU` (value: `"PU"`)

* `RN` (value: `"RN"`)

* `RT` (value: `"RT"`)

* `TC` (value: `"TC"`)

* `TN` (value: `"TN"`)

* `UC` (value: `"UC"`)




