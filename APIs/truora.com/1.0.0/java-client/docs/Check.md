

# Check

Represents a background check

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**birthCertificate** | **String** | Person birth certificate |  [optional] |
|**checkId** | **String** | Background check ID |  |
|**companySummary** | [**CompanySummary**](CompanySummary.md) |  |  [optional] |
|**country** | [**CountryEnum**](#CountryEnum) | ID Document country |  |
|**creationDate** | **OffsetDateTime** | Background check creation date |  |
|**dateOfBirth** | **OffsetDateTime** | Person birthdate. Shown only if provided during check creation. YYYY-MM-DD format |  [optional] |
|**diplomaticId** | **String** | Person diplomatic id |  [optional] |
|**driverLicense** | **String** | Person driver&#39;s license |  [optional] |
|**firstName** | **String** | Person or entity first name. Shown only if provided during check creation |  [optional] |
|**foreignId** | **String** | Person foreign identification |  [optional] |
|**homonymProbability** | **Float** | [Experimental] Analyzes the probability that the results by name are attributed to a homonym. Number between 0 and 1 where 1 is the the greatest probability |  [optional] |
|**homonymScore** | **Float** | Background check score including results by name only. This might contain homonym information |  [optional] |
|**homonymScores** | [**List&lt;Score&gt;**](Score.md) | Background check scores by name for each profile group. [Deprecated for API key V1] |  [optional] |
|**idScore** | **Float** | Background check score regarding results by ID number only. It is a number between 0 and 1 where 1 is the best score. This result is a weighted average of the id_scores listed under scores. |  |
|**issueDate** | **OffsetDateTime** | Issue date of the person ID |  [optional] |
|**lastName** | **String** | Person or entity last name. Shown only if provided during check creation |  [optional] |
|**licensePlate** | **String** | Vehicle license plate |  [optional] |
|**nationalId** | **String** | Person national identification |  [optional] |
|**nativeCountry** | [**NativeCountryEnum**](#NativeCountryEnum) | Person origin country |  [optional] |
|**ownerDocumentId** | **String** | Vehicle owner identification |  [optional] |
|**ownerDocumentType** | **String** | Vehicle owner document type |  [optional] |
|**passport** | **String** | Person passport |  [optional] |
|**paymentDate** | **String** | Vehicle license payment date |  [optional] |
|**pep** | **String** | Colombian PEP idenfitication for Venezuelans |  [optional] |
|**phoneNumber** | **String** | Person phone number. Required by law in order to notify the person their background is being checked |  [optional] |
|**professionalCard** | **String** | Person professional card number |  [optional] |
|**ptp** | **String** | Temporary residence permit of the person |  [optional] |
|**region** | [**RegionEnum**](#RegionEnum) | Region where the background is to be checked. By default, background checks in Brazil are performed in region where the person is from. Applies for some Brazil collectors only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins.   |  [optional] |
|**reportId** | **String** | Report ID the background check is associated with |  [optional] |
|**score** | **Float** | Background check score. Number between 0 and 1 where 1 is the best score |  |
|**scores** | [**List&lt;Score&gt;**](Score.md) | Background check score of each profile group and dataset |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the check finished successfully, **error** means the check failed, **in_progress** means the check is currently being processed, **delayed** means the check is waiting for an additional requirement to be met, this can last up to 3 days. **Completed** and **error** are the two only final statuses |  |
|**statuses** | [**List&lt;Status&gt;**](Status.md) | Database status list |  |
|**summary** | [**Summary**](Summary.md) |  |  |
|**taxId** | **String** | Person or company tax id |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Background check type |  |
|**updateDate** | **OffsetDateTime** | Background check update date |  [optional] |
|**vehicleId** | **String** | Vehicle identification |  [optional] |
|**vehicleSummary** | [**VehicleSummary**](VehicleSummary.md) |  |  [optional] |
|**wrongInputs** | [**List&lt;WrongInput&gt;**](WrongInput.md) | List of parameters entered during background check creation that do not match the information obtained |  [optional] |



## Enum: CountryEnum

| Name | Value |
|---- | -----|
| ALL | &quot;ALL&quot; |
| BR | &quot;BR&quot; |
| CL | &quot;CL&quot; |
| CO | &quot;CO&quot; |
| CR | &quot;CR&quot; |
| EC | &quot;EC&quot; |
| MX | &quot;MX&quot; |
| PE | &quot;PE&quot; |
| AR | &quot;AR&quot; |



## Enum: NativeCountryEnum

| Name | Value |
|---- | -----|
| AD | &quot;ad&quot; |
| AE | &quot;ae&quot; |
| AF | &quot;af&quot; |
| AG | &quot;ag&quot; |
| AI | &quot;ai&quot; |
| AL | &quot;al&quot; |
| AM | &quot;am&quot; |
| AN | &quot;an&quot; |
| AO | &quot;ao&quot; |
| AQ | &quot;aq&quot; |
| AR | &quot;ar&quot; |
| AS | &quot;as&quot; |
| AT | &quot;at&quot; |
| AU | &quot;au&quot; |
| AW | &quot;aw&quot; |
| AX | &quot;ax&quot; |
| AZ | &quot;az&quot; |
| BA | &quot;ba&quot; |
| BB | &quot;bb&quot; |
| BD | &quot;bd&quot; |
| BE | &quot;be&quot; |
| BF | &quot;bf&quot; |
| BG | &quot;bg&quot; |
| BH | &quot;bh&quot; |
| BI | &quot;bi&quot; |
| BJ | &quot;bj&quot; |
| BM | &quot;bm&quot; |
| BN | &quot;bn&quot; |
| BO | &quot;bo&quot; |
| BR | &quot;br&quot; |
| BS | &quot;bs&quot; |
| BT | &quot;bt&quot; |
| BV | &quot;bv&quot; |
| BW | &quot;bw&quot; |
| BY | &quot;by&quot; |
| BZ | &quot;bz&quot; |
| CA | &quot;ca&quot; |
| CC | &quot;cc&quot; |
| CD | &quot;cd&quot; |
| CF | &quot;cf&quot; |
| CG | &quot;cg&quot; |
| CH | &quot;ch&quot; |
| CI | &quot;ci&quot; |
| CK | &quot;ck&quot; |
| CL | &quot;cl&quot; |
| CM | &quot;cm&quot; |
| CN | &quot;cn&quot; |
| CO | &quot;co&quot; |
| CR | &quot;cr&quot; |
| CU | &quot;cu&quot; |
| CV | &quot;cv&quot; |
| CX | &quot;cx&quot; |
| CY | &quot;cy&quot; |
| CZ | &quot;cz&quot; |
| DE | &quot;de&quot; |
| DJ | &quot;dj&quot; |
| DK | &quot;dk&quot; |
| DM | &quot;dm&quot; |
| DO | &quot;do&quot; |
| DZ | &quot;dz&quot; |
| EA | &quot;ea&quot; |
| EC | &quot;ec&quot; |
| EE | &quot;ee&quot; |
| EG | &quot;eg&quot; |
| EH | &quot;eh&quot; |
| ER | &quot;er&quot; |
| ES | &quot;es&quot; |
| ET | &quot;et&quot; |
| FI | &quot;fi&quot; |
| FJ | &quot;fj&quot; |
| FK | &quot;fk&quot; |
| FM | &quot;fm&quot; |
| FO | &quot;fo&quot; |
| FR | &quot;fr&quot; |
| GA | &quot;ga&quot; |
| GB | &quot;gb&quot; |
| GD | &quot;gd&quot; |
| GE | &quot;ge&quot; |
| GF | &quot;gf&quot; |
| GG | &quot;gg&quot; |
| GH | &quot;gh&quot; |
| GI | &quot;gi&quot; |
| GL | &quot;gl&quot; |
| GM | &quot;gm&quot; |
| GN | &quot;gn&quot; |
| GP | &quot;gp&quot; |
| GQ | &quot;gq&quot; |
| GR | &quot;gr&quot; |
| GS | &quot;gs&quot; |
| GT | &quot;gt&quot; |
| GU | &quot;gu&quot; |
| GW | &quot;gw&quot; |
| GY | &quot;gy&quot; |
| HK | &quot;hk&quot; |
| HM | &quot;hm&quot; |
| HN | &quot;hn&quot; |
| HR | &quot;hr&quot; |
| HT | &quot;ht&quot; |
| HU | &quot;hu&quot; |
| ID | &quot;id&quot; |
| IE | &quot;ie&quot; |
| IL | &quot;il&quot; |
| IM | &quot;im&quot; |
| IN | &quot;in&quot; |
| IO | &quot;io&quot; |
| IQ | &quot;iq&quot; |
| IR | &quot;ir&quot; |
| IS | &quot;is&quot; |
| IT | &quot;it&quot; |
| JE | &quot;je&quot; |
| JM | &quot;jm&quot; |
| JO | &quot;jo&quot; |
| JP | &quot;jp&quot; |
| KE | &quot;ke&quot; |
| KG | &quot;kg&quot; |
| KH | &quot;kh&quot; |
| KI | &quot;ki&quot; |
| KM | &quot;km&quot; |
| KN | &quot;kn&quot; |
| KP | &quot;kp&quot; |
| KR | &quot;kr&quot; |
| KW | &quot;kw&quot; |
| KY | &quot;ky&quot; |
| KZ | &quot;kz&quot; |
| LA | &quot;la&quot; |
| LB | &quot;lb&quot; |
| LC | &quot;lc&quot; |
| LI | &quot;li&quot; |
| LK | &quot;lk&quot; |
| LR | &quot;lr&quot; |
| LS | &quot;ls&quot; |
| LT | &quot;lt&quot; |
| LU | &quot;lu&quot; |
| LV | &quot;lv&quot; |
| LY | &quot;ly&quot; |
| MA | &quot;ma&quot; |
| MC | &quot;mc&quot; |
| MD | &quot;md&quot; |
| ME | &quot;me&quot; |
| MG | &quot;mg&quot; |
| MH | &quot;mh&quot; |
| MK | &quot;mk&quot; |
| ML | &quot;ml&quot; |
| MM | &quot;mm&quot; |
| MN | &quot;mn&quot; |
| MO | &quot;mo&quot; |
| MP | &quot;mp&quot; |
| MQ | &quot;mq&quot; |
| MR | &quot;mr&quot; |
| MS | &quot;ms&quot; |
| MT | &quot;mt&quot; |
| MU | &quot;mu&quot; |
| MV | &quot;mv&quot; |
| MW | &quot;mw&quot; |
| MX | &quot;mx&quot; |
| MY | &quot;my&quot; |
| MZ | &quot;mz&quot; |
| NA | &quot;na&quot; |
| NC | &quot;nc&quot; |
| NE | &quot;ne&quot; |
| NF | &quot;nf&quot; |
| NG | &quot;ng&quot; |
| NI | &quot;ni&quot; |
| NL | &quot;nl&quot; |
| FALSE | &quot;false&quot; |
| NP | &quot;np&quot; |
| NR | &quot;nr&quot; |
| NU | &quot;nu&quot; |
| NZ | &quot;nz&quot; |
| OM | &quot;om&quot; |
| PA | &quot;pa&quot; |
| PE | &quot;pe&quot; |
| PF | &quot;pf&quot; |
| PG | &quot;pg&quot; |
| PH | &quot;ph&quot; |
| PK | &quot;pk&quot; |
| PL | &quot;pl&quot; |
| PM | &quot;pm&quot; |
| PN | &quot;pn&quot; |
| PR | &quot;pr&quot; |
| PS | &quot;ps&quot; |
| PT | &quot;pt&quot; |
| PW | &quot;pw&quot; |
| PY | &quot;py&quot; |
| QA | &quot;qa&quot; |
| RE | &quot;re&quot; |
| RO | &quot;ro&quot; |
| RS | &quot;rs&quot; |
| RU | &quot;ru&quot; |
| RW | &quot;rw&quot; |
| SA | &quot;sa&quot; |
| SB | &quot;sb&quot; |
| SC | &quot;sc&quot; |
| SD | &quot;sd&quot; |
| SE | &quot;se&quot; |
| SG | &quot;sg&quot; |
| SH | &quot;sh&quot; |
| SI | &quot;si&quot; |
| SJ | &quot;sj&quot; |
| SK | &quot;sk&quot; |
| SL | &quot;sl&quot; |
| SM | &quot;sm&quot; |
| SN | &quot;sn&quot; |
| SO | &quot;so&quot; |
| SR | &quot;sr&quot; |
| ST | &quot;st&quot; |
| SV | &quot;sv&quot; |
| SY | &quot;sy&quot; |
| SZ | &quot;sz&quot; |
| TC | &quot;tc&quot; |
| TD | &quot;td&quot; |
| TF | &quot;tf&quot; |
| TG | &quot;tg&quot; |
| TH | &quot;th&quot; |
| TJ | &quot;tj&quot; |
| TK | &quot;tk&quot; |
| TL | &quot;tl&quot; |
| TM | &quot;tm&quot; |
| TN | &quot;tn&quot; |
| TO | &quot;to&quot; |
| TR | &quot;tr&quot; |
| TT | &quot;tt&quot; |
| TV | &quot;tv&quot; |
| TW | &quot;tw&quot; |
| TZ | &quot;tz&quot; |
| UA | &quot;ua&quot; |
| UG | &quot;ug&quot; |
| UM | &quot;um&quot; |
| US | &quot;us&quot; |
| UY | &quot;uy&quot; |
| UZ | &quot;uz&quot; |
| VA | &quot;va&quot; |
| VC | &quot;vc&quot; |
| VE | &quot;ve&quot; |
| VG | &quot;vg&quot; |
| VI | &quot;vi&quot; |
| VN | &quot;vn&quot; |
| VU | &quot;vu&quot; |
| WF | &quot;wf&quot; |
| WS | &quot;ws&quot; |
| YE | &quot;ye&quot; |
| YT | &quot;yt&quot; |
| ZA | &quot;za&quot; |
| ZM | &quot;zm&quot; |
| ZW | &quot;zw&quot; |



## Enum: RegionEnum

| Name | Value |
|---- | -----|
| DF | &quot;DF&quot; |
| AC | &quot;AC&quot; |
| AL | &quot;AL&quot; |
| AP | &quot;AP&quot; |
| AM | &quot;AM&quot; |
| BA | &quot;BA&quot; |
| CE | &quot;CE&quot; |
| ES | &quot;ES&quot; |
| GO | &quot;GO&quot; |
| MA | &quot;MA&quot; |
| MT | &quot;MT&quot; |
| MS | &quot;MS&quot; |
| MG | &quot;MG&quot; |
| PA | &quot;PA&quot; |
| PB | &quot;PB&quot; |
| PR | &quot;PR&quot; |
| PE | &quot;PE&quot; |
| PI | &quot;PI&quot; |
| RJ | &quot;RJ&quot; |
| RN | &quot;RN&quot; |
| RS | &quot;RS&quot; |
| RO | &quot;RO&quot; |
| RR | &quot;RR&quot; |
| SC | &quot;SC&quot; |
| SP | &quot;SP&quot; |
| SE | &quot;SE&quot; |
| TO | &quot;TO&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;not_started&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| COMPLETED | &quot;completed&quot; |
| ERROR | &quot;error&quot; |
| DELAYED | &quot;delayed&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMPANY | &quot;company&quot; |
| PERSON | &quot;person&quot; |
| VEHICLE | &quot;vehicle&quot; |



