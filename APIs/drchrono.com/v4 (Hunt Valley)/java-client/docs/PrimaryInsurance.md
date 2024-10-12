

# PrimaryInsurance

**Warning:** Changing insurance information may make past appointments unbillable. Insurance data is also **unvalidated**; you should use the [`/api/insurances`](#apiinsurances) endpoint to find the appropriate insurance payer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**insuranceClaimOfficeNumber** | **String** | Insurance office phone number |  [optional] |
|**insuranceCompany** | **String** |  |  [optional] |
|**insuranceGroupName** | **String** |  |  [optional] |
|**insuranceGroupNumber** | **String** |  |  [optional] |
|**insuranceIdNumber** | **String** |  |  [optional] |
|**insurancePayerId** | **String** |  |  [optional] |
|**insurancePlanName** | **String** | Name of insurance plan. |  [optional] |
|**insurancePlanType** | [**InsurancePlanTypeEnum**](#InsurancePlanTypeEnum) |  |  [optional] |
|**isSubscriberThePatient** | **Boolean** | True if the insurance policy is under patient&#39;s own name. Defaults to true |  [optional] |
|**patientRelationshipToSubscriber** | [**PatientRelationshipToSubscriberEnum**](#PatientRelationshipToSubscriberEnum) | HCFA/1500 individual relationship code |  [optional] |
|**photoBack** | **String** | Photo of back of insurance card |  [optional] |
|**photoFront** | **String** | Photo of front of insurance card |  [optional] |
|**subscriberAddress** | **String** |  |  [optional] |
|**subscriberCity** | **String** |  |  [optional] |
|**subscriberCountry** | [**SubscriberCountryEnum**](#SubscriberCountryEnum) | Two-letter country code |  [optional] |
|**subscriberDateOfBirth** | **String** |  |  [optional] |
|**subscriberFirstName** | **String** |  |  [optional] |
|**subscriberGender** | [**SubscriberGenderEnum**](#SubscriberGenderEnum) | One of &#x60;\&quot;Male\&quot;&#x60; or &#x60;\&quot;Female\&quot;&#x60; |  [optional] |
|**subscriberLastName** | **String** |  |  [optional] |
|**subscriberMiddleName** | **String** |  |  [optional] |
|**subscriberSocialSecurity** | **String** |  |  [optional] |
|**subscriberState** | [**SubscriberStateEnum**](#SubscriberStateEnum) | Two-letter state code |  [optional] |
|**subscriberSuffix** | **String** | E.g. &#x60;\&quot;II\&quot;&#x60; or &#x60;\&quot;III\&quot;&#x60; |  [optional] |
|**subscriberZipCode** | **String** |  |  [optional] |



## Enum: InsurancePlanTypeEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| AM | &quot;AM&quot; |
| BL | &quot;BL&quot; |
| CH | &quot;CH&quot; |
| CI | &quot;CI&quot; |
| _17 | &quot;17&quot; |
| DS | &quot;DS&quot; |
| _14 | &quot;14&quot; |
| FI | &quot;FI&quot; |
| HM | &quot;HM&quot; |
| _16 | &quot;16&quot; |
| _15 | &quot;15&quot; |
| LM | &quot;LM&quot; |
| MC | &quot;MC&quot; |
| MA | &quot;MA&quot; |
| MB | &quot;MB&quot; |
| ZZ | &quot;ZZ&quot; |
| OF | &quot;OF&quot; |
| _11 | &quot;11&quot; |
| _13 | &quot;13&quot; |
| _12 | &quot;12&quot; |
| TV | &quot;TV&quot; |
| VA | &quot;VA&quot; |
| WC | &quot;WC&quot; |



## Enum: PatientRelationshipToSubscriberEnum

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



## Enum: SubscriberCountryEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| AF | &quot;AF&quot; |
| AX | &quot;AX&quot; |
| AL | &quot;AL&quot; |
| DZ | &quot;DZ&quot; |
| AS | &quot;AS&quot; |
| AD | &quot;AD&quot; |
| AO | &quot;AO&quot; |
| AI | &quot;AI&quot; |
| AQ | &quot;AQ&quot; |
| AG | &quot;AG&quot; |
| AR | &quot;AR&quot; |
| AM | &quot;AM&quot; |
| AW | &quot;AW&quot; |
| AU | &quot;AU&quot; |
| AT | &quot;AT&quot; |
| AZ | &quot;AZ&quot; |
| BS | &quot;BS&quot; |
| BH | &quot;BH&quot; |
| BD | &quot;BD&quot; |
| BB | &quot;BB&quot; |
| BY | &quot;BY&quot; |
| BE | &quot;BE&quot; |
| BZ | &quot;BZ&quot; |
| BJ | &quot;BJ&quot; |
| BM | &quot;BM&quot; |
| BT | &quot;BT&quot; |
| BO | &quot;BO&quot; |
| BQ | &quot;BQ&quot; |
| BA | &quot;BA&quot; |
| BW | &quot;BW&quot; |
| BV | &quot;BV&quot; |
| BR | &quot;BR&quot; |
| IO | &quot;IO&quot; |
| BN | &quot;BN&quot; |
| BG | &quot;BG&quot; |
| BF | &quot;BF&quot; |
| BI | &quot;BI&quot; |
| KH | &quot;KH&quot; |
| CM | &quot;CM&quot; |
| CA | &quot;CA&quot; |
| CV | &quot;CV&quot; |
| KY | &quot;KY&quot; |
| CF | &quot;CF&quot; |
| TD | &quot;TD&quot; |
| CL | &quot;CL&quot; |
| CN | &quot;CN&quot; |
| CX | &quot;CX&quot; |
| CC | &quot;CC&quot; |
| CO | &quot;CO&quot; |
| KM | &quot;KM&quot; |
| CG | &quot;CG&quot; |
| CD | &quot;CD&quot; |
| CK | &quot;CK&quot; |
| CR | &quot;CR&quot; |
| CI | &quot;CI&quot; |
| HR | &quot;HR&quot; |
| CU | &quot;CU&quot; |
| CW | &quot;CW&quot; |
| CY | &quot;CY&quot; |
| CZ | &quot;CZ&quot; |
| CYM | &quot;CYM&quot; |
| DK | &quot;DK&quot; |
| DJ | &quot;DJ&quot; |
| DM | &quot;DM&quot; |
| DO | &quot;DO&quot; |
| EC | &quot;EC&quot; |
| EG | &quot;EG&quot; |
| SV | &quot;SV&quot; |
| GQ | &quot;GQ&quot; |
| ER | &quot;ER&quot; |
| EE | &quot;EE&quot; |
| ET | &quot;ET&quot; |
| FK | &quot;FK&quot; |
| FO | &quot;FO&quot; |
| FJ | &quot;FJ&quot; |
| FI | &quot;FI&quot; |
| FR | &quot;FR&quot; |
| GF | &quot;GF&quot; |
| PF | &quot;PF&quot; |
| TF | &quot;TF&quot; |
| GA | &quot;GA&quot; |
| GM | &quot;GM&quot; |
| GE | &quot;GE&quot; |
| DE | &quot;DE&quot; |
| GH | &quot;GH&quot; |
| GI | &quot;GI&quot; |
| GR | &quot;GR&quot; |
| GL | &quot;GL&quot; |
| GD | &quot;GD&quot; |
| GP | &quot;GP&quot; |
| GU | &quot;GU&quot; |
| GT | &quot;GT&quot; |
| GG | &quot;GG&quot; |
| GN | &quot;GN&quot; |
| GW | &quot;GW&quot; |
| GY | &quot;GY&quot; |
| HT | &quot;HT&quot; |
| HM | &quot;HM&quot; |
| VA | &quot;VA&quot; |
| HN | &quot;HN&quot; |
| HK | &quot;HK&quot; |
| HU | &quot;HU&quot; |
| IS | &quot;IS&quot; |
| IN | &quot;IN&quot; |
| ID | &quot;ID&quot; |
| IR | &quot;IR&quot; |
| IQ | &quot;IQ&quot; |
| IE | &quot;IE&quot; |
| IM | &quot;IM&quot; |
| IL | &quot;IL&quot; |
| IT | &quot;IT&quot; |
| JM | &quot;JM&quot; |
| JP | &quot;JP&quot; |
| JE | &quot;JE&quot; |
| JO | &quot;JO&quot; |
| KZ | &quot;KZ&quot; |
| KE | &quot;KE&quot; |
| KI | &quot;KI&quot; |
| KP | &quot;KP&quot; |
| KR | &quot;KR&quot; |
| XK | &quot;XK&quot; |
| KW | &quot;KW&quot; |
| KG | &quot;KG&quot; |
| LA | &quot;LA&quot; |
| LV | &quot;LV&quot; |
| LB | &quot;LB&quot; |
| LS | &quot;LS&quot; |
| LR | &quot;LR&quot; |
| LY | &quot;LY&quot; |
| LI | &quot;LI&quot; |
| LT | &quot;LT&quot; |
| LU | &quot;LU&quot; |
| MO | &quot;MO&quot; |
| MK | &quot;MK&quot; |
| MG | &quot;MG&quot; |
| MW | &quot;MW&quot; |
| MY | &quot;MY&quot; |
| MV | &quot;MV&quot; |
| ML | &quot;ML&quot; |
| MT | &quot;MT&quot; |
| MH | &quot;MH&quot; |
| MQ | &quot;MQ&quot; |
| MR | &quot;MR&quot; |
| MU | &quot;MU&quot; |
| YT | &quot;YT&quot; |
| MX | &quot;MX&quot; |
| FM | &quot;FM&quot; |
| MD | &quot;MD&quot; |
| MC | &quot;MC&quot; |
| MN | &quot;MN&quot; |
| ME | &quot;ME&quot; |
| MS | &quot;MS&quot; |
| MA | &quot;MA&quot; |
| MZ | &quot;MZ&quot; |
| MM | &quot;MM&quot; |
| NA | &quot;NA&quot; |
| NR | &quot;NR&quot; |
| NP | &quot;NP&quot; |
| NL | &quot;NL&quot; |
| NC | &quot;NC&quot; |
| NZ | &quot;NZ&quot; |
| NI | &quot;NI&quot; |
| NE | &quot;NE&quot; |
| NG | &quot;NG&quot; |
| NU | &quot;NU&quot; |
| NF | &quot;NF&quot; |
| MP | &quot;MP&quot; |
| FALSE | &quot;false&quot; |
| OM | &quot;OM&quot; |
| PK | &quot;PK&quot; |
| PW | &quot;PW&quot; |
| PS | &quot;PS&quot; |
| PA | &quot;PA&quot; |
| PG | &quot;PG&quot; |
| PY | &quot;PY&quot; |
| PE | &quot;PE&quot; |
| PH | &quot;PH&quot; |
| PN | &quot;PN&quot; |
| PL | &quot;PL&quot; |
| PT | &quot;PT&quot; |
| PR | &quot;PR&quot; |
| QA | &quot;QA&quot; |
| RE | &quot;RE&quot; |
| RO | &quot;RO&quot; |
| RU | &quot;RU&quot; |
| RW | &quot;RW&quot; |
| BL | &quot;BL&quot; |
| SH | &quot;SH&quot; |
| KN | &quot;KN&quot; |
| LC | &quot;LC&quot; |
| MF | &quot;MF&quot; |
| PM | &quot;PM&quot; |
| VC | &quot;VC&quot; |
| WS | &quot;WS&quot; |
| SM | &quot;SM&quot; |
| ST | &quot;ST&quot; |
| SA | &quot;SA&quot; |
| SN | &quot;SN&quot; |
| RS | &quot;RS&quot; |
| SC | &quot;SC&quot; |
| SL | &quot;SL&quot; |
| SG | &quot;SG&quot; |
| SX | &quot;SX&quot; |
| SK | &quot;SK&quot; |
| SI | &quot;SI&quot; |
| SB | &quot;SB&quot; |
| SO | &quot;SO&quot; |
| ZA | &quot;ZA&quot; |
| GS | &quot;GS&quot; |
| SS | &quot;SS&quot; |
| ES | &quot;ES&quot; |
| LK | &quot;LK&quot; |
| SD | &quot;SD&quot; |
| SR | &quot;SR&quot; |
| SJ | &quot;SJ&quot; |
| SZ | &quot;SZ&quot; |
| SE | &quot;SE&quot; |
| CH | &quot;CH&quot; |
| SY | &quot;SY&quot; |
| TW | &quot;TW&quot; |
| TJ | &quot;TJ&quot; |
| TZ | &quot;TZ&quot; |
| TH | &quot;TH&quot; |
| TL | &quot;TL&quot; |
| TG | &quot;TG&quot; |
| TK | &quot;TK&quot; |
| TO | &quot;TO&quot; |
| TT | &quot;TT&quot; |
| TN | &quot;TN&quot; |
| TR | &quot;TR&quot; |
| TM | &quot;TM&quot; |
| TC | &quot;TC&quot; |
| TV | &quot;TV&quot; |
| UG | &quot;UG&quot; |
| UA | &quot;UA&quot; |
| AE | &quot;AE&quot; |
| GB | &quot;GB&quot; |
| US | &quot;US&quot; |
| UM | &quot;UM&quot; |
| UY | &quot;UY&quot; |
| UZ | &quot;UZ&quot; |
| VU | &quot;VU&quot; |
| VE | &quot;VE&quot; |
| VN | &quot;VN&quot; |
| VG | &quot;VG&quot; |
| VI | &quot;VI&quot; |
| WF | &quot;WF&quot; |
| EH | &quot;EH&quot; |
| YE | &quot;YE&quot; |
| ZM | &quot;ZM&quot; |
| ZW | &quot;ZW&quot; |



## Enum: SubscriberGenderEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| MALE | &quot;Male&quot; |
| FEMALE | &quot;Female&quot; |
| OTHER | &quot;Other&quot; |
| UNK | &quot;UNK&quot; |
| ASKU | &quot;ASKU&quot; |



## Enum: SubscriberStateEnum

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



