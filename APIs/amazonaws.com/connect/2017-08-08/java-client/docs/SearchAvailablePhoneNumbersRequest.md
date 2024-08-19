

# SearchAvailablePhoneNumbersRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetArn** | **String** | The Amazon Resource Name (ARN) for Amazon Connect instances or traffic distribution groups that phone numbers are claimed to. |  |
|**phoneNumberCountryCode** | [**PhoneNumberCountryCodeEnum**](#PhoneNumberCountryCodeEnum) | The ISO country code. |  |
|**phoneNumberType** | [**PhoneNumberTypeEnum**](#PhoneNumberTypeEnum) | The type of phone number. |  |
|**phoneNumberPrefix** | **String** | The prefix of the phone number. If provided, it must contain &lt;code&gt;+&lt;/code&gt; as part of the country code. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return per page. |  [optional] |
|**nextToken** | **String** | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. |  [optional] |



## Enum: PhoneNumberCountryCodeEnum

| Name | Value |
|---- | -----|
| AF | &quot;AF&quot; |
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
| BA | &quot;BA&quot; |
| BW | &quot;BW&quot; |
| BR | &quot;BR&quot; |
| IO | &quot;IO&quot; |
| VG | &quot;VG&quot; |
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
| CK | &quot;CK&quot; |
| CR | &quot;CR&quot; |
| HR | &quot;HR&quot; |
| CU | &quot;CU&quot; |
| CW | &quot;CW&quot; |
| CY | &quot;CY&quot; |
| CZ | &quot;CZ&quot; |
| CD | &quot;CD&quot; |
| DK | &quot;DK&quot; |
| DJ | &quot;DJ&quot; |
| DM | &quot;DM&quot; |
| DO | &quot;DO&quot; |
| TL | &quot;TL&quot; |
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
| PF | &quot;PF&quot; |
| GA | &quot;GA&quot; |
| GM | &quot;GM&quot; |
| GE | &quot;GE&quot; |
| DE | &quot;DE&quot; |
| GH | &quot;GH&quot; |
| GI | &quot;GI&quot; |
| GR | &quot;GR&quot; |
| GL | &quot;GL&quot; |
| GD | &quot;GD&quot; |
| GU | &quot;GU&quot; |
| GT | &quot;GT&quot; |
| GG | &quot;GG&quot; |
| GN | &quot;GN&quot; |
| GW | &quot;GW&quot; |
| GY | &quot;GY&quot; |
| HT | &quot;HT&quot; |
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
| CI | &quot;CI&quot; |
| JM | &quot;JM&quot; |
| JP | &quot;JP&quot; |
| JE | &quot;JE&quot; |
| JO | &quot;JO&quot; |
| KZ | &quot;KZ&quot; |
| KE | &quot;KE&quot; |
| KI | &quot;KI&quot; |
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
| AN | &quot;AN&quot; |
| NC | &quot;NC&quot; |
| NZ | &quot;NZ&quot; |
| NI | &quot;NI&quot; |
| NE | &quot;NE&quot; |
| NG | &quot;NG&quot; |
| NU | &quot;NU&quot; |
| KP | &quot;KP&quot; |
| MP | &quot;MP&quot; |
| NO | &quot;NO&quot; |
| OM | &quot;OM&quot; |
| PK | &quot;PK&quot; |
| PW | &quot;PW&quot; |
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
| CG | &quot;CG&quot; |
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
| KR | &quot;KR&quot; |
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
| TG | &quot;TG&quot; |
| TK | &quot;TK&quot; |
| TO | &quot;TO&quot; |
| TT | &quot;TT&quot; |
| TN | &quot;TN&quot; |
| TR | &quot;TR&quot; |
| TM | &quot;TM&quot; |
| TC | &quot;TC&quot; |
| TV | &quot;TV&quot; |
| VI | &quot;VI&quot; |
| UG | &quot;UG&quot; |
| UA | &quot;UA&quot; |
| AE | &quot;AE&quot; |
| GB | &quot;GB&quot; |
| US | &quot;US&quot; |
| UY | &quot;UY&quot; |
| UZ | &quot;UZ&quot; |
| VU | &quot;VU&quot; |
| VA | &quot;VA&quot; |
| VE | &quot;VE&quot; |
| VN | &quot;VN&quot; |
| WF | &quot;WF&quot; |
| EH | &quot;EH&quot; |
| YE | &quot;YE&quot; |
| ZM | &quot;ZM&quot; |
| ZW | &quot;ZW&quot; |



## Enum: PhoneNumberTypeEnum

| Name | Value |
|---- | -----|
| TOLL_FREE | &quot;TOLL_FREE&quot; |
| DID | &quot;DID&quot; |
| UIFN | &quot;UIFN&quot; |
| SHARED | &quot;SHARED&quot; |
| THIRD_PARTY_TF | &quot;THIRD_PARTY_TF&quot; |
| THIRD_PARTY_DID | &quot;THIRD_PARTY_DID&quot; |



