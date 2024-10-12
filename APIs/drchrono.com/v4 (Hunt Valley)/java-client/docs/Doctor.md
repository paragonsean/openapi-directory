

# Doctor


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cellPhone** | **String** |  |  [optional] |
|**country** | [**CountryEnum**](#CountryEnum) | Two-letter conutry code. Default is &#x60;US&#x60; |  [optional] |
|**email** | **String** |  |  [optional] [readonly] |
|**firstName** | **String** |  |  [optional] |
|**groupNpiNumber** | **String** |  |  [optional] |
|**homePhone** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**isAccountSuspended** | **Boolean** | Indicates the doctor&#39;s account is suspended or not |  [optional] |
|**jobTitle** | [**JobTitleEnum**](#JobTitleEnum) |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**npiNumber** | **String** | If both this field and &#x60;group_npi_number&#x60; are set, prefer this field |  [optional] |
|**officePhone** | **String** |  |  [optional] |
|**practiceGroup** | **String** | The ID of the practice group this user belongs to. This can be used to identify users in the same practice. |  [optional] [readonly] |
|**practiceGroupName** | **String** |  |  [optional] [readonly] |
|**profilePicture** | **String** |  |  [optional] [readonly] |
|**specialty** | **String** |  |  [optional] |
|**suffix** | **String** |  |  [optional] |
|**timezone** | **String** |  |  [optional] |
|**website** | **String** |  |  [optional] |



## Enum: CountryEnum

| Name | Value |
|---- | -----|
| BD | &quot;BD&quot; |
| WF | &quot;WF&quot; |
| BF | &quot;BF&quot; |
| BG | &quot;BG&quot; |
| BA | &quot;BA&quot; |
| BB | &quot;BB&quot; |
| BE | &quot;BE&quot; |
| BL | &quot;BL&quot; |
| BM | &quot;BM&quot; |
| BN | &quot;BN&quot; |
| BO | &quot;BO&quot; |
| JP | &quot;JP&quot; |
| BI | &quot;BI&quot; |
| BJ | &quot;BJ&quot; |
| BT | &quot;BT&quot; |
| JM | &quot;JM&quot; |
| BV | &quot;BV&quot; |
| JO | &quot;JO&quot; |
| WS | &quot;WS&quot; |
| BQ | &quot;BQ&quot; |
| BR | &quot;BR&quot; |
| BS | &quot;BS&quot; |
| JE | &quot;JE&quot; |
| BY | &quot;BY&quot; |
| BZ | &quot;BZ&quot; |
| RU | &quot;RU&quot; |
| RW | &quot;RW&quot; |
| RS | &quot;RS&quot; |
| TL | &quot;TL&quot; |
| RE | &quot;RE&quot; |
| TM | &quot;TM&quot; |
| TJ | &quot;TJ&quot; |
| RO | &quot;RO&quot; |
| TK | &quot;TK&quot; |
| GW | &quot;GW&quot; |
| GU | &quot;GU&quot; |
| GT | &quot;GT&quot; |
| GS | &quot;GS&quot; |
| GR | &quot;GR&quot; |
| GQ | &quot;GQ&quot; |
| GP | &quot;GP&quot; |
| BH | &quot;BH&quot; |
| GY | &quot;GY&quot; |
| GG | &quot;GG&quot; |
| GF | &quot;GF&quot; |
| GE | &quot;GE&quot; |
| GD | &quot;GD&quot; |
| GB | &quot;GB&quot; |
| GA | &quot;GA&quot; |
| GN | &quot;GN&quot; |
| GM | &quot;GM&quot; |
| GL | &quot;GL&quot; |
| KW | &quot;KW&quot; |
| GI | &quot;GI&quot; |
| GH | &quot;GH&quot; |
| OM | &quot;OM&quot; |
| TN | &quot;TN&quot; |
| BW | &quot;BW&quot; |
| HR | &quot;HR&quot; |
| HT | &quot;HT&quot; |
| HU | &quot;HU&quot; |
| HK | &quot;HK&quot; |
| HN | &quot;HN&quot; |
| HM | &quot;HM&quot; |
| KR | &quot;KR&quot; |
| AD | &quot;AD&quot; |
| PR | &quot;PR&quot; |
| PS | &quot;PS&quot; |
| PW | &quot;PW&quot; |
| PT | &quot;PT&quot; |
| KN | &quot;KN&quot; |
| PY | &quot;PY&quot; |
| AI | &quot;AI&quot; |
| PA | &quot;PA&quot; |
| PF | &quot;PF&quot; |
| PG | &quot;PG&quot; |
| PE | &quot;PE&quot; |
| PK | &quot;PK&quot; |
| PH | &quot;PH&quot; |
| PN | &quot;PN&quot; |
| PL | &quot;PL&quot; |
| PM | &quot;PM&quot; |
| ZM | &quot;ZM&quot; |
| EH | &quot;EH&quot; |
| EE | &quot;EE&quot; |
| EG | &quot;EG&quot; |
| ZA | &quot;ZA&quot; |
| EC | &quot;EC&quot; |
| AL | &quot;AL&quot; |
| AO | &quot;AO&quot; |
| KZ | &quot;KZ&quot; |
| ET | &quot;ET&quot; |
| ZW | &quot;ZW&quot; |
| KY | &quot;KY&quot; |
| ES | &quot;ES&quot; |
| ER | &quot;ER&quot; |
| ME | &quot;ME&quot; |
| MD | &quot;MD&quot; |
| MG | &quot;MG&quot; |
| MF | &quot;MF&quot; |
| MA | &quot;MA&quot; |
| MC | &quot;MC&quot; |
| UZ | &quot;UZ&quot; |
| MM | &quot;MM&quot; |
| ML | &quot;ML&quot; |
| MO | &quot;MO&quot; |
| MN | &quot;MN&quot; |
| MH | &quot;MH&quot; |
| MK | &quot;MK&quot; |
| MU | &quot;MU&quot; |
| MT | &quot;MT&quot; |
| MW | &quot;MW&quot; |
| MV | &quot;MV&quot; |
| MQ | &quot;MQ&quot; |
| MP | &quot;MP&quot; |
| MS | &quot;MS&quot; |
| MR | &quot;MR&quot; |
| AU | &quot;AU&quot; |
| UG | &quot;UG&quot; |
| MY | &quot;MY&quot; |
| MX | &quot;MX&quot; |
| MZ | &quot;MZ&quot; |
| FR | &quot;FR&quot; |
| AW | &quot;AW&quot; |
| AF | &quot;AF&quot; |
| AX | &quot;AX&quot; |
| FI | &quot;FI&quot; |
| FJ | &quot;FJ&quot; |
| FK | &quot;FK&quot; |
| FM | &quot;FM&quot; |
| FO | &quot;FO&quot; |
| NI | &quot;NI&quot; |
| NL | &quot;NL&quot; |
| FALSE | &quot;false&quot; |
| NA | &quot;NA&quot; |
| VU | &quot;VU&quot; |
| NC | &quot;NC&quot; |
| NE | &quot;NE&quot; |
| NF | &quot;NF&quot; |
| NG | &quot;NG&quot; |
| NZ | &quot;NZ&quot; |
| NP | &quot;NP&quot; |
| NR | &quot;NR&quot; |
| NU | &quot;NU&quot; |
| CK | &quot;CK&quot; |
| CI | &quot;CI&quot; |
| CH | &quot;CH&quot; |
| CO | &quot;CO&quot; |
| CN | &quot;CN&quot; |
| CM | &quot;CM&quot; |
| CL | &quot;CL&quot; |
| CC | &quot;CC&quot; |
| CA | &quot;CA&quot; |
| CG | &quot;CG&quot; |
| CF | &quot;CF&quot; |
| CD | &quot;CD&quot; |
| CZ | &quot;CZ&quot; |
| CY | &quot;CY&quot; |
| CX | &quot;CX&quot; |
| CR | &quot;CR&quot; |
| KP | &quot;KP&quot; |
| CW | &quot;CW&quot; |
| CV | &quot;CV&quot; |
| CU | &quot;CU&quot; |
| SZ | &quot;SZ&quot; |
| SY | &quot;SY&quot; |
| SX | &quot;SX&quot; |
| KG | &quot;KG&quot; |
| KE | &quot;KE&quot; |
| SS | &quot;SS&quot; |
| SR | &quot;SR&quot; |
| KI | &quot;KI&quot; |
| KH | &quot;KH&quot; |
| SV | &quot;SV&quot; |
| KM | &quot;KM&quot; |
| ST | &quot;ST&quot; |
| SK | &quot;SK&quot; |
| SJ | &quot;SJ&quot; |
| SI | &quot;SI&quot; |
| SH | &quot;SH&quot; |
| SO | &quot;SO&quot; |
| SN | &quot;SN&quot; |
| SM | &quot;SM&quot; |
| SL | &quot;SL&quot; |
| SC | &quot;SC&quot; |
| SB | &quot;SB&quot; |
| SA | &quot;SA&quot; |
| SG | &quot;SG&quot; |
| SE | &quot;SE&quot; |
| SD | &quot;SD&quot; |
| DO | &quot;DO&quot; |
| DM | &quot;DM&quot; |
| DJ | &quot;DJ&quot; |
| DK | &quot;DK&quot; |
| DE | &quot;DE&quot; |
| YE | &quot;YE&quot; |
| AT | &quot;AT&quot; |
| DZ | &quot;DZ&quot; |
| US | &quot;US&quot; |
| UY | &quot;UY&quot; |
| YT | &quot;YT&quot; |
| UM | &quot;UM&quot; |
| LB | &quot;LB&quot; |
| LC | &quot;LC&quot; |
| LA | &quot;LA&quot; |
| TV | &quot;TV&quot; |
| TW | &quot;TW&quot; |
| TT | &quot;TT&quot; |
| TR | &quot;TR&quot; |
| LK | &quot;LK&quot; |
| LI | &quot;LI&quot; |
| LV | &quot;LV&quot; |
| TO | &quot;TO&quot; |
| LT | &quot;LT&quot; |
| LU | &quot;LU&quot; |
| LR | &quot;LR&quot; |
| LS | &quot;LS&quot; |
| TH | &quot;TH&quot; |
| TF | &quot;TF&quot; |
| TG | &quot;TG&quot; |
| TD | &quot;TD&quot; |
| TC | &quot;TC&quot; |
| LY | &quot;LY&quot; |
| VA | &quot;VA&quot; |
| VC | &quot;VC&quot; |
| AE | &quot;AE&quot; |
| VE | &quot;VE&quot; |
| AG | &quot;AG&quot; |
| VG | &quot;VG&quot; |
| IQ | &quot;IQ&quot; |
| VI | &quot;VI&quot; |
| IS | &quot;IS&quot; |
| IR | &quot;IR&quot; |
| AM | &quot;AM&quot; |
| IT | &quot;IT&quot; |
| VN | &quot;VN&quot; |
| AQ | &quot;AQ&quot; |
| AS | &quot;AS&quot; |
| AR | &quot;AR&quot; |
| IM | &quot;IM&quot; |
| IL | &quot;IL&quot; |
| IO | &quot;IO&quot; |
| IN | &quot;IN&quot; |
| TZ | &quot;TZ&quot; |
| AZ | &quot;AZ&quot; |
| IE | &quot;IE&quot; |
| ID | &quot;ID&quot; |
| UA | &quot;UA&quot; |
| QA | &quot;QA&quot; |



## Enum: JobTitleEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| PROVIDER_STAFF_PRIVATE_PRACTICE_ | &quot;Provider/Staff (Private Practice)&quot; |
| PROVIDER_STAFF_HOSPITAL_ | &quot;Provider/Staff (Hospital)&quot; |
| PATIENTS_INTERVIEW_CANDIDATE | &quot;Patients/Interview Candidate&quot; |
| EDUCATOR_STUDENT | &quot;Educator/Student&quot; |
| API_DEVELOPER | &quot;API/Developer&quot; |
| CONSULTANT | &quot;Consultant&quot; |
| OTHER | &quot;Other&quot; |



