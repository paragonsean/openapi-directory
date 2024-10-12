

# AutoAccidentInsurance



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoAccidentCaseNumber** | **String** |  |  [optional] |
|**autoAccidentClaimRepAddress** | **String** |  |  [optional] |
|**autoAccidentClaimRepCity** | **String** |  |  [optional] |
|**autoAccidentClaimRepIsInsurer** | **Boolean** | Is the insurer&#39;s claim representative the insurer? |  [optional] |
|**autoAccidentClaimRepName** | **String** |  |  [optional] |
|**autoAccidentClaimRepState** | [**AutoAccidentClaimRepStateEnum**](#AutoAccidentClaimRepStateEnum) |  |  [optional] |
|**autoAccidentClaimRepZip** | **String** |  |  [optional] |
|**autoAccidentCompany** | **String** |  |  [optional] |
|**autoAccidentDateOfAccident** | **String** |  |  [optional] |
|**autoAccidentDisabledFromDate** | **String** | Patient was disabled (unable to work) from |  [optional] |
|**autoAccidentDisabledToDate** | **String** | Patient was disabled (unable to work) to |  [optional] |
|**autoAccidentHadSimilarCondition** | **Boolean** | Has the patient had same or similar condition? |  [optional] |
|**autoAccidentIsSubscriberThePatient** | **Boolean** | True if the insurance policy is under patient&#39;s own name. |  [optional] |
|**autoAccidentNotes** | **String** |  |  [optional] |
|**autoAccidentPatientRelationshipToSubscriber** | [**AutoAccidentPatientRelationshipToSubscriberEnum**](#AutoAccidentPatientRelationshipToSubscriberEnum) |  |  [optional] |
|**autoAccidentPayerAddress** | **String** |  |  [optional] |
|**autoAccidentPayerCity** | **String** |  |  [optional] |
|**autoAccidentPayerId** | **String** | Auto Accident Payer ID |  [optional] |
|**autoAccidentPayerState** | [**AutoAccidentPayerStateEnum**](#AutoAccidentPayerStateEnum) |  |  [optional] |
|**autoAccidentPayerZip** | **String** |  |  [optional] |
|**autoAccidentPolicyNumber** | **String** |  |  [optional] |
|**autoAccidentReturnToWorkDate** | **String** | If still disabled, patient should be able to return to work on |  [optional] |
|**autoAccidentSignificantInjury** | [**AutoAccidentSignificantInjuryEnum**](#AutoAccidentSignificantInjuryEnum) |  |  [optional] |
|**autoAccidentSignificantInjuryNotes** | **String** |  |  [optional] |
|**autoAccidentSimilarConditionDate** | **String** | Date of same or similar condition |  [optional] |
|**autoAccidentSimilarConditionNotes** | **String** |  |  [optional] |
|**autoAccidentStateOfOccurrence** | [**AutoAccidentStateOfOccurrenceEnum**](#AutoAccidentStateOfOccurrenceEnum) |  |  [optional] |
|**autoAccidentStillUnderCare** | **Boolean** | Is patient still under your care for this condition? |  [optional] |
|**autoAccidentSubscriberAddress** | **String** |  |  [optional] |
|**autoAccidentSubscriberCity** | **String** |  |  [optional] |
|**autoAccidentSubscriberDateOfBirth** | **String** |  |  [optional] |
|**autoAccidentSubscriberFirstName** | **String** |  |  [optional] |
|**autoAccidentSubscriberLastName** | **String** |  |  [optional] |
|**autoAccidentSubscriberMiddleName** | **String** |  |  [optional] |
|**autoAccidentSubscriberPhoneNumber** | **String** |  |  [optional] |
|**autoAccidentSubscriberSocialSecurity** | **String** |  |  [optional] |
|**autoAccidentSubscriberState** | [**AutoAccidentSubscriberStateEnum**](#AutoAccidentSubscriberStateEnum) |  |  [optional] |
|**autoAccidentSubscriberSuffix** | **String** |  |  [optional] |
|**autoAccidentSubscriberZipCode** | **String** |  |  [optional] |
|**autoAccidentTreatmentDuration** | **String** |  |  [optional] |
|**autoAccidentWillRequireTherapy** | **Boolean** | Will the patient require rehabilitation and/or occupational therapy as a result of the injuries sustained in this accident? |  [optional] |
|**autoAccidentWillRequireTherapyRec** | **String** |  |  [optional] |



## Enum: AutoAccidentClaimRepStateEnum

| Name | Value |
|---- | -----|
| AL | &quot;AL&quot; |
| AK | &quot;AK&quot; |
| AS | &quot;AS&quot; |
| AZ | &quot;AZ&quot; |
| AR | &quot;AR&quot; |
| AA | &quot;AA&quot; |
| AE | &quot;AE&quot; |
| AP | &quot;AP&quot; |
| CA | &quot;CA&quot; |
| CO | &quot;CO&quot; |
| CT | &quot;CT&quot; |
| DE | &quot;DE&quot; |
| DC | &quot;DC&quot; |
| FL | &quot;FL&quot; |
| GA | &quot;GA&quot; |
| GU | &quot;GU&quot; |
| HI | &quot;HI&quot; |
| ID | &quot;ID&quot; |
| IL | &quot;IL&quot; |
| IN | &quot;IN&quot; |
| IA | &quot;IA&quot; |
| KS | &quot;KS&quot; |
| KY | &quot;KY&quot; |
| LA | &quot;LA&quot; |
| ME | &quot;ME&quot; |
| MD | &quot;MD&quot; |
| MA | &quot;MA&quot; |
| MI | &quot;MI&quot; |
| MN | &quot;MN&quot; |
| MS | &quot;MS&quot; |
| MO | &quot;MO&quot; |
| MT | &quot;MT&quot; |
| NE | &quot;NE&quot; |
| NV | &quot;NV&quot; |
| NH | &quot;NH&quot; |
| NJ | &quot;NJ&quot; |
| NM | &quot;NM&quot; |
| NY | &quot;NY&quot; |
| NC | &quot;NC&quot; |
| ND | &quot;ND&quot; |
| MP | &quot;MP&quot; |
| OH | &quot;OH&quot; |
| OK | &quot;OK&quot; |
| OR | &quot;OR&quot; |
| PA | &quot;PA&quot; |
| PR | &quot;PR&quot; |
| RI | &quot;RI&quot; |
| SC | &quot;SC&quot; |
| SD | &quot;SD&quot; |
| TN | &quot;TN&quot; |
| TX | &quot;TX&quot; |
| UT | &quot;UT&quot; |
| VT | &quot;VT&quot; |
| VI | &quot;VI&quot; |
| VA | &quot;VA&quot; |
| WA | &quot;WA&quot; |
| WV | &quot;WV&quot; |
| WI | &quot;WI&quot; |
| WY | &quot;WY&quot; |



## Enum: AutoAccidentPatientRelationshipToSubscriberEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| _01 | &quot;01&quot; |
| _04 | &quot;04&quot; |
| _05 | &quot;05&quot; |
| _07 | &quot;07&quot; |
| _10 | &quot;10&quot; |
| _15 | &quot;15&quot; |
| _17 | &quot;17&quot; |
| _19 | &quot;19&quot; |
| _20 | &quot;20&quot; |
| _21 | &quot;21&quot; |
| _22 | &quot;22&quot; |
| _23 | &quot;23&quot; |
| _24 | &quot;24&quot; |
| _29 | &quot;29&quot; |
| _32 | &quot;32&quot; |
| _33 | &quot;33&quot; |
| _36 | &quot;36&quot; |
| _39 | &quot;39&quot; |
| _40 | &quot;40&quot; |
| _41 | &quot;41&quot; |
| _43 | &quot;43&quot; |
| _53 | &quot;53&quot; |
| _76 | &quot;76&quot; |
| G8 | &quot;G8&quot; |



## Enum: AutoAccidentPayerStateEnum

| Name | Value |
|---- | -----|
| AL | &quot;AL&quot; |
| AK | &quot;AK&quot; |
| AS | &quot;AS&quot; |
| AZ | &quot;AZ&quot; |
| AR | &quot;AR&quot; |
| AA | &quot;AA&quot; |
| AE | &quot;AE&quot; |
| AP | &quot;AP&quot; |
| CA | &quot;CA&quot; |
| CO | &quot;CO&quot; |
| CT | &quot;CT&quot; |
| DE | &quot;DE&quot; |
| DC | &quot;DC&quot; |
| FL | &quot;FL&quot; |
| GA | &quot;GA&quot; |
| GU | &quot;GU&quot; |
| HI | &quot;HI&quot; |
| ID | &quot;ID&quot; |
| IL | &quot;IL&quot; |
| IN | &quot;IN&quot; |
| IA | &quot;IA&quot; |
| KS | &quot;KS&quot; |
| KY | &quot;KY&quot; |
| LA | &quot;LA&quot; |
| ME | &quot;ME&quot; |
| MD | &quot;MD&quot; |
| MA | &quot;MA&quot; |
| MI | &quot;MI&quot; |
| MN | &quot;MN&quot; |
| MS | &quot;MS&quot; |
| MO | &quot;MO&quot; |
| MT | &quot;MT&quot; |
| NE | &quot;NE&quot; |
| NV | &quot;NV&quot; |
| NH | &quot;NH&quot; |
| NJ | &quot;NJ&quot; |
| NM | &quot;NM&quot; |
| NY | &quot;NY&quot; |
| NC | &quot;NC&quot; |
| ND | &quot;ND&quot; |
| MP | &quot;MP&quot; |
| OH | &quot;OH&quot; |
| OK | &quot;OK&quot; |
| OR | &quot;OR&quot; |
| PA | &quot;PA&quot; |
| PR | &quot;PR&quot; |
| RI | &quot;RI&quot; |
| SC | &quot;SC&quot; |
| SD | &quot;SD&quot; |
| TN | &quot;TN&quot; |
| TX | &quot;TX&quot; |
| UT | &quot;UT&quot; |
| VT | &quot;VT&quot; |
| VI | &quot;VI&quot; |
| VA | &quot;VA&quot; |
| WA | &quot;WA&quot; |
| WV | &quot;WV&quot; |
| WI | &quot;WI&quot; |
| WY | &quot;WY&quot; |



## Enum: AutoAccidentSignificantInjuryEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |
| N_A | &quot;N\\A&quot; |



## Enum: AutoAccidentStateOfOccurrenceEnum

| Name | Value |
|---- | -----|
| AL | &quot;AL&quot; |
| AK | &quot;AK&quot; |
| AS | &quot;AS&quot; |
| AZ | &quot;AZ&quot; |
| AR | &quot;AR&quot; |
| AA | &quot;AA&quot; |
| AE | &quot;AE&quot; |
| AP | &quot;AP&quot; |
| CA | &quot;CA&quot; |
| CO | &quot;CO&quot; |
| CT | &quot;CT&quot; |
| DE | &quot;DE&quot; |
| DC | &quot;DC&quot; |
| FL | &quot;FL&quot; |
| GA | &quot;GA&quot; |
| GU | &quot;GU&quot; |
| HI | &quot;HI&quot; |
| ID | &quot;ID&quot; |
| IL | &quot;IL&quot; |
| IN | &quot;IN&quot; |
| IA | &quot;IA&quot; |
| KS | &quot;KS&quot; |
| KY | &quot;KY&quot; |
| LA | &quot;LA&quot; |
| ME | &quot;ME&quot; |
| MD | &quot;MD&quot; |
| MA | &quot;MA&quot; |
| MI | &quot;MI&quot; |
| MN | &quot;MN&quot; |
| MS | &quot;MS&quot; |
| MO | &quot;MO&quot; |
| MT | &quot;MT&quot; |
| NE | &quot;NE&quot; |
| NV | &quot;NV&quot; |
| NH | &quot;NH&quot; |
| NJ | &quot;NJ&quot; |
| NM | &quot;NM&quot; |
| NY | &quot;NY&quot; |
| NC | &quot;NC&quot; |
| ND | &quot;ND&quot; |
| MP | &quot;MP&quot; |
| OH | &quot;OH&quot; |
| OK | &quot;OK&quot; |
| OR | &quot;OR&quot; |
| PA | &quot;PA&quot; |
| PR | &quot;PR&quot; |
| RI | &quot;RI&quot; |
| SC | &quot;SC&quot; |
| SD | &quot;SD&quot; |
| TN | &quot;TN&quot; |
| TX | &quot;TX&quot; |
| UT | &quot;UT&quot; |
| VT | &quot;VT&quot; |
| VI | &quot;VI&quot; |
| VA | &quot;VA&quot; |
| WA | &quot;WA&quot; |
| WV | &quot;WV&quot; |
| WI | &quot;WI&quot; |
| WY | &quot;WY&quot; |



## Enum: AutoAccidentSubscriberStateEnum

| Name | Value |
|---- | -----|
| AL | &quot;AL&quot; |
| AK | &quot;AK&quot; |
| AS | &quot;AS&quot; |
| AZ | &quot;AZ&quot; |
| AR | &quot;AR&quot; |
| AA | &quot;AA&quot; |
| AE | &quot;AE&quot; |
| AP | &quot;AP&quot; |
| CA | &quot;CA&quot; |
| CO | &quot;CO&quot; |
| CT | &quot;CT&quot; |
| DE | &quot;DE&quot; |
| DC | &quot;DC&quot; |
| FL | &quot;FL&quot; |
| GA | &quot;GA&quot; |
| GU | &quot;GU&quot; |
| HI | &quot;HI&quot; |
| ID | &quot;ID&quot; |
| IL | &quot;IL&quot; |
| IN | &quot;IN&quot; |
| IA | &quot;IA&quot; |
| KS | &quot;KS&quot; |
| KY | &quot;KY&quot; |
| LA | &quot;LA&quot; |
| ME | &quot;ME&quot; |
| MD | &quot;MD&quot; |
| MA | &quot;MA&quot; |
| MI | &quot;MI&quot; |
| MN | &quot;MN&quot; |
| MS | &quot;MS&quot; |
| MO | &quot;MO&quot; |
| MT | &quot;MT&quot; |
| NE | &quot;NE&quot; |
| NV | &quot;NV&quot; |
| NH | &quot;NH&quot; |
| NJ | &quot;NJ&quot; |
| NM | &quot;NM&quot; |
| NY | &quot;NY&quot; |
| NC | &quot;NC&quot; |
| ND | &quot;ND&quot; |
| MP | &quot;MP&quot; |
| OH | &quot;OH&quot; |
| OK | &quot;OK&quot; |
| OR | &quot;OR&quot; |
| PA | &quot;PA&quot; |
| PR | &quot;PR&quot; |
| RI | &quot;RI&quot; |
| SC | &quot;SC&quot; |
| SD | &quot;SD&quot; |
| TN | &quot;TN&quot; |
| TX | &quot;TX&quot; |
| UT | &quot;UT&quot; |
| VT | &quot;VT&quot; |
| VI | &quot;VI&quot; |
| VA | &quot;VA&quot; |
| WA | &quot;WA&quot; |
| WV | &quot;WV&quot; |
| WI | &quot;WI&quot; |
| WY | &quot;WY&quot; |



