

# MappingJob

For V3: securityType2 is required when idType is BASE_TICKER or ID_EXCH_SYMBOL.  expiration is required when securityType2 is Option or Warrant.  maturity is required when securityType2 is Pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contractSize** | **List&lt;BigDecimal&gt;** | At least one entry should be non-null. |  [optional] |
|**coupon** | **List&lt;BigDecimal&gt;** | At least one entry should be non-null. |  [optional] |
|**currency** | **String** |  |  [optional] |
|**exchCode** | **String** |  |  [optional] |
|**expiration** | **List&lt;LocalDate&gt;** | At least one entry should be non-null. |  [optional] |
|**idType** | [**IdTypeEnum**](#IdTypeEnum) |  |  |
|**idValue** | [**MappingJobIdValue**](MappingJobIdValue.md) |  |  |
|**includeUnlistedEquities** | **Boolean** |  |  [optional] |
|**marketSecDes** | **String** |  |  [optional] |
|**maturity** | **List&lt;LocalDate&gt;** | At least one entry should be non-null. |  [optional] |
|**micCode** | **String** |  |  [optional] |
|**optionType** | [**OptionTypeEnum**](#OptionTypeEnum) |  |  [optional] |
|**securityType** | **String** |  |  [optional] |
|**securityType2** | **String** |  |  [optional] |
|**stateCode** | [**StateCodeEnum**](#StateCodeEnum) |  |  [optional] |
|**strike** | **List&lt;BigDecimal&gt;** | At least one entry should be non-null. |  [optional] |



## Enum: IdTypeEnum

| Name | Value |
|---- | -----|
| ID_ISIN | &quot;ID_ISIN&quot; |
| ID_BB_UNIQUE | &quot;ID_BB_UNIQUE&quot; |
| ID_SEDOL | &quot;ID_SEDOL&quot; |
| ID_COMMON | &quot;ID_COMMON&quot; |
| ID_WERTPAPIER | &quot;ID_WERTPAPIER&quot; |
| ID_CUSIP | &quot;ID_CUSIP&quot; |
| ID_BB | &quot;ID_BB&quot; |
| ID_ITALY | &quot;ID_ITALY&quot; |
| ID_EXCH_SYMBOL | &quot;ID_EXCH_SYMBOL&quot; |
| ID_FULL_EXCHANGE_SYMBOL | &quot;ID_FULL_EXCHANGE_SYMBOL&quot; |
| COMPOSITE_ID_BB_GLOBAL | &quot;COMPOSITE_ID_BB_GLOBAL&quot; |
| ID_BB_GLOBAL_SHARE_CLASS_LEVEL | &quot;ID_BB_GLOBAL_SHARE_CLASS_LEVEL&quot; |
| ID_BB_SEC_NUM_DES | &quot;ID_BB_SEC_NUM_DES&quot; |
| ID_BB_GLOBAL | &quot;ID_BB_GLOBAL&quot; |
| TICKER | &quot;TICKER&quot; |
| ID_CUSIP_8_CHR | &quot;ID_CUSIP_8_CHR&quot; |
| OCC_SYMBOL | &quot;OCC_SYMBOL&quot; |
| UNIQUE_ID_FUT_OPT | &quot;UNIQUE_ID_FUT_OPT&quot; |
| OPRA_SYMBOL | &quot;OPRA_SYMBOL&quot; |
| TRADING_SYSTEM_IDENTIFIER | &quot;TRADING_SYSTEM_IDENTIFIER&quot; |
| ID_CINS | &quot;ID_CINS&quot; |
| ID_SHORT_CODE | &quot;ID_SHORT_CODE&quot; |
| BASE_TICKER | &quot;BASE_TICKER&quot; |
| VENDOR_INDEX_CODE | &quot;VENDOR_INDEX_CODE&quot; |



## Enum: OptionTypeEnum

| Name | Value |
|---- | -----|
| PUT | &quot;Put&quot; |
| CALL | &quot;Call&quot; |



## Enum: StateCodeEnum

| Name | Value |
|---- | -----|
| AB | &quot;AB&quot; |
| AC | &quot;AC&quot; |
| AC2 | &quot;AC&quot; |
| AH | &quot;AH&quot; |
| AK | &quot;AK&quot; |
| AL | &quot;AL&quot; |
| AM | &quot;AM&quot; |
| AR | &quot;AR&quot; |
| AS | &quot;AS&quot; |
| AT | &quot;AT&quot; |
| AZ | &quot;AZ&quot; |
| BC | &quot;BC&quot; |
| BJ | &quot;BJ&quot; |
| CA | &quot;CA&quot; |
| CB | &quot;CB&quot; |
| CO | &quot;CO&quot; |
| CQ | &quot;CQ&quot; |
| CT | &quot;CT&quot; |
| CZ | &quot;CZ&quot; |
| DC | &quot;DC&quot; |
| DE | &quot;DE&quot; |
| EH | &quot;EH&quot; |
| FH | &quot;FH&quot; |
| FI | &quot;FI&quot; |
| FJ | &quot;FJ&quot; |
| FL | &quot;FL&quot; |
| FO | &quot;FO&quot; |
| FS | &quot;FS&quot; |
| GA | &quot;GA&quot; |
| GD | &quot;GD&quot; |
| GF | &quot;GF&quot; |
| GM | &quot;GM&quot; |
| GS | &quot;GS&quot; |
| GU | &quot;GU&quot; |
| GX | &quot;GX&quot; |
| GZ | &quot;GZ&quot; |
| HA | &quot;HA&quot; |
| HB | &quot;HB&quot; |
| HE | &quot;HE&quot; |
| HG | &quot;HG&quot; |
| HI | &quot;HI&quot; |
| HI2 | &quot;HI&quot; |
| HL | &quot;HL&quot; |
| HN | &quot;HN&quot; |
| HO | &quot;HO&quot; |
| HS | &quot;HS&quot; |
| IA | &quot;IA&quot; |
| ID | &quot;ID&quot; |
| IG | &quot;IG&quot; |
| IK | &quot;IK&quot; |
| IL | &quot;IL&quot; |
| IN | &quot;IN&quot; |
| IT | &quot;IT&quot; |
| JL | &quot;JL&quot; |
| JS | &quot;JS&quot; |
| JX | &quot;JX&quot; |
| KA | &quot;KA&quot; |
| KC | &quot;KC&quot; |
| KN | &quot;KN&quot; |
| KO | &quot;KO&quot; |
| KS | &quot;KS&quot; |
| KT | &quot;KT&quot; |
| KU | &quot;KU&quot; |
| KY | &quot;KY&quot; |
| LA | &quot;LA&quot; |
| LN | &quot;LN&quot; |
| MA | &quot;MA&quot; |
| MB | &quot;MB&quot; |
| MD | &quot;MD&quot; |
| ME | &quot;ME&quot; |
| ME2 | &quot;ME&quot; |
| MG | &quot;MG&quot; |
| MI | &quot;MI&quot; |
| MN | &quot;MN&quot; |
| MO | &quot;MO&quot; |
| MS | &quot;MS&quot; |
| MT | &quot;MT&quot; |
| MZ | &quot;MZ&quot; |
| NB | &quot;NB&quot; |
| NC | &quot;NC&quot; |
| ND | &quot;ND&quot; |
| NE | &quot;NE&quot; |
| NG | &quot;NG&quot; |
| NH | &quot;NH&quot; |
| NJ | &quot;NJ&quot; |
| NL | &quot;NL&quot; |
| NM | &quot;NM&quot; |
| NM2 | &quot;NM&quot; |
| NN | &quot;NN&quot; |
| NR | &quot;NR&quot; |
| NS | &quot;NS&quot; |
| NS2 | &quot;NS&quot; |
| NS3 | &quot;NS&quot; |
| NT | &quot;NT&quot; |
| NU | &quot;NU&quot; |
| NV | &quot;NV&quot; |
| NW | &quot;NW&quot; |
| NX | &quot;NX&quot; |
| NY | &quot;NY&quot; |
| OH | &quot;OH&quot; |
| OK | &quot;OK&quot; |
| TRUE | &quot;true&quot; |
| TRUE2 | &quot;true&quot; |
| OR | &quot;OR&quot; |
| OS | &quot;OS&quot; |
| OT | &quot;OT&quot; |
| OT2 | &quot;OT&quot; |
| OY | &quot;OY&quot; |
| PA | &quot;PA&quot; |
| PE | &quot;PE&quot; |
| PR | &quot;PR&quot; |
| QC | &quot;QC&quot; |
| QH | &quot;QH&quot; |
| QL | &quot;QL&quot; |
| RI | &quot;RI&quot; |
| SA | &quot;SA&quot; |
| SA2 | &quot;SA&quot; |
| SC | &quot;SC&quot; |
| SC2 | &quot;SC&quot; |
| SD | &quot;SD&quot; |
| SD2 | &quot;SD&quot; |
| SH | &quot;SH&quot; |
| SI | &quot;SI&quot; |
| SK | &quot;SK&quot; |
| SN | &quot;SN&quot; |
| SN2 | &quot;SN&quot; |
| ST | &quot;ST&quot; |
| SX | &quot;SX&quot; |
| SZ | &quot;SZ&quot; |
| TA | &quot;TA&quot; |
| TG | &quot;TG&quot; |
| TJ | &quot;TJ&quot; |
| TK | &quot;TK&quot; |
| TN | &quot;TN&quot; |
| TS | &quot;TS&quot; |
| TT | &quot;TT&quot; |
| TT2 | &quot;TT&quot; |
| TX | &quot;TX&quot; |
| TY | &quot;TY&quot; |
| UT | &quot;UT&quot; |
| VA | &quot;VA&quot; |
| VI | &quot;VI&quot; |
| VI2 | &quot;VI&quot; |
| VT | &quot;VT&quot; |
| WA | &quot;WA&quot; |
| WA2 | &quot;WA&quot; |
| WI | &quot;WI&quot; |
| WK | &quot;WK&quot; |
| WV | &quot;WV&quot; |
| WY | &quot;WY&quot; |
| XJ | &quot;XJ&quot; |
| XZ | &quot;XZ&quot; |
| YA | &quot;YA&quot; |
| YN | &quot;YN&quot; |
| YN2 | &quot;YN&quot; |
| YT | &quot;YT&quot; |
| YU | &quot;YU&quot; |
| ZJ | &quot;ZJ&quot; |



