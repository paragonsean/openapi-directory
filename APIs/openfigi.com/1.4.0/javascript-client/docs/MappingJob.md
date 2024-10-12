# OpenFigiApi.MappingJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contractSize** | **[Number]** | At least one entry should be non-null. | [optional] 
**coupon** | **[Number]** | At least one entry should be non-null. | [optional] 
**currency** | **String** |  | [optional] 
**exchCode** | **String** |  | [optional] 
**expiration** | **[Date]** | At least one entry should be non-null. | [optional] 
**idType** | **String** |  | 
**idValue** | [**MappingJobIdValue**](MappingJobIdValue.md) |  | 
**includeUnlistedEquities** | **Boolean** |  | [optional] 
**marketSecDes** | **String** |  | [optional] 
**maturity** | **[Date]** | At least one entry should be non-null. | [optional] 
**micCode** | **String** |  | [optional] 
**optionType** | **String** |  | [optional] 
**securityType** | **String** |  | [optional] 
**securityType2** | **String** |  | [optional] 
**stateCode** | **String** |  | [optional] 
**strike** | **[Number]** | At least one entry should be non-null. | [optional] 



## Enum: IdTypeEnum


* `ID_ISIN` (value: `"ID_ISIN"`)

* `ID_BB_UNIQUE` (value: `"ID_BB_UNIQUE"`)

* `ID_SEDOL` (value: `"ID_SEDOL"`)

* `ID_COMMON` (value: `"ID_COMMON"`)

* `ID_WERTPAPIER` (value: `"ID_WERTPAPIER"`)

* `ID_CUSIP` (value: `"ID_CUSIP"`)

* `ID_BB` (value: `"ID_BB"`)

* `ID_ITALY` (value: `"ID_ITALY"`)

* `ID_EXCH_SYMBOL` (value: `"ID_EXCH_SYMBOL"`)

* `ID_FULL_EXCHANGE_SYMBOL` (value: `"ID_FULL_EXCHANGE_SYMBOL"`)

* `COMPOSITE_ID_BB_GLOBAL` (value: `"COMPOSITE_ID_BB_GLOBAL"`)

* `ID_BB_GLOBAL_SHARE_CLASS_LEVEL` (value: `"ID_BB_GLOBAL_SHARE_CLASS_LEVEL"`)

* `ID_BB_SEC_NUM_DES` (value: `"ID_BB_SEC_NUM_DES"`)

* `ID_BB_GLOBAL` (value: `"ID_BB_GLOBAL"`)

* `TICKER` (value: `"TICKER"`)

* `ID_CUSIP_8_CHR` (value: `"ID_CUSIP_8_CHR"`)

* `OCC_SYMBOL` (value: `"OCC_SYMBOL"`)

* `UNIQUE_ID_FUT_OPT` (value: `"UNIQUE_ID_FUT_OPT"`)

* `OPRA_SYMBOL` (value: `"OPRA_SYMBOL"`)

* `TRADING_SYSTEM_IDENTIFIER` (value: `"TRADING_SYSTEM_IDENTIFIER"`)

* `ID_CINS` (value: `"ID_CINS"`)

* `ID_SHORT_CODE` (value: `"ID_SHORT_CODE"`)

* `BASE_TICKER` (value: `"BASE_TICKER"`)

* `VENDOR_INDEX_CODE` (value: `"VENDOR_INDEX_CODE"`)





## Enum: OptionTypeEnum


* `Put` (value: `"Put"`)

* `Call` (value: `"Call"`)





## Enum: StateCodeEnum


* `AB` (value: `"AB"`)

* `AC` (value: `"AC"`)

* `AC2` (value: `"AC"`)

* `AH` (value: `"AH"`)

* `AK` (value: `"AK"`)

* `AL` (value: `"AL"`)

* `AM` (value: `"AM"`)

* `AR` (value: `"AR"`)

* `AS` (value: `"AS"`)

* `AT` (value: `"AT"`)

* `AZ` (value: `"AZ"`)

* `BC` (value: `"BC"`)

* `BJ` (value: `"BJ"`)

* `CA` (value: `"CA"`)

* `CB` (value: `"CB"`)

* `CO` (value: `"CO"`)

* `CQ` (value: `"CQ"`)

* `CT` (value: `"CT"`)

* `CZ` (value: `"CZ"`)

* `DC` (value: `"DC"`)

* `DE` (value: `"DE"`)

* `EH` (value: `"EH"`)

* `FH` (value: `"FH"`)

* `FI` (value: `"FI"`)

* `FJ` (value: `"FJ"`)

* `FL` (value: `"FL"`)

* `FO` (value: `"FO"`)

* `FS` (value: `"FS"`)

* `GA` (value: `"GA"`)

* `GD` (value: `"GD"`)

* `GF` (value: `"GF"`)

* `GM` (value: `"GM"`)

* `GS` (value: `"GS"`)

* `GU` (value: `"GU"`)

* `GX` (value: `"GX"`)

* `GZ` (value: `"GZ"`)

* `HA` (value: `"HA"`)

* `HB` (value: `"HB"`)

* `HE` (value: `"HE"`)

* `HG` (value: `"HG"`)

* `HI` (value: `"HI"`)

* `HI2` (value: `"HI"`)

* `HL` (value: `"HL"`)

* `HN` (value: `"HN"`)

* `HO` (value: `"HO"`)

* `HS` (value: `"HS"`)

* `IA` (value: `"IA"`)

* `ID` (value: `"ID"`)

* `IG` (value: `"IG"`)

* `IK` (value: `"IK"`)

* `IL` (value: `"IL"`)

* `IN` (value: `"IN"`)

* `IT` (value: `"IT"`)

* `JL` (value: `"JL"`)

* `JS` (value: `"JS"`)

* `JX` (value: `"JX"`)

* `KA` (value: `"KA"`)

* `KC` (value: `"KC"`)

* `KN` (value: `"KN"`)

* `KO` (value: `"KO"`)

* `KS` (value: `"KS"`)

* `KT` (value: `"KT"`)

* `KU` (value: `"KU"`)

* `KY` (value: `"KY"`)

* `LA` (value: `"LA"`)

* `LN` (value: `"LN"`)

* `MA` (value: `"MA"`)

* `MB` (value: `"MB"`)

* `MD` (value: `"MD"`)

* `ME` (value: `"ME"`)

* `ME2` (value: `"ME"`)

* `MG` (value: `"MG"`)

* `MI` (value: `"MI"`)

* `MN` (value: `"MN"`)

* `MO` (value: `"MO"`)

* `MS` (value: `"MS"`)

* `MT` (value: `"MT"`)

* `MZ` (value: `"MZ"`)

* `NB` (value: `"NB"`)

* `NC` (value: `"NC"`)

* `ND` (value: `"ND"`)

* `NE` (value: `"NE"`)

* `NG` (value: `"NG"`)

* `NH` (value: `"NH"`)

* `NJ` (value: `"NJ"`)

* `NL` (value: `"NL"`)

* `NM` (value: `"NM"`)

* `NM2` (value: `"NM"`)

* `NN` (value: `"NN"`)

* `NR` (value: `"NR"`)

* `NS` (value: `"NS"`)

* `NS2` (value: `"NS"`)

* `NS3` (value: `"NS"`)

* `NT` (value: `"NT"`)

* `NU` (value: `"NU"`)

* `NV` (value: `"NV"`)

* `NW` (value: `"NW"`)

* `NX` (value: `"NX"`)

* `NY` (value: `"NY"`)

* `OH` (value: `"OH"`)

* `OK` (value: `"OK"`)

* `true` (value: `"true"`)

* `true2` (value: `"true"`)

* `OR` (value: `"OR"`)

* `OS` (value: `"OS"`)

* `OT` (value: `"OT"`)

* `OT2` (value: `"OT"`)

* `OY` (value: `"OY"`)

* `PA` (value: `"PA"`)

* `PE` (value: `"PE"`)

* `PR` (value: `"PR"`)

* `QC` (value: `"QC"`)

* `QH` (value: `"QH"`)

* `QL` (value: `"QL"`)

* `RI` (value: `"RI"`)

* `SA` (value: `"SA"`)

* `SA2` (value: `"SA"`)

* `SC` (value: `"SC"`)

* `SC2` (value: `"SC"`)

* `SD` (value: `"SD"`)

* `SD2` (value: `"SD"`)

* `SH` (value: `"SH"`)

* `SI` (value: `"SI"`)

* `SK` (value: `"SK"`)

* `SN` (value: `"SN"`)

* `SN2` (value: `"SN"`)

* `ST` (value: `"ST"`)

* `SX` (value: `"SX"`)

* `SZ` (value: `"SZ"`)

* `TA` (value: `"TA"`)

* `TG` (value: `"TG"`)

* `TJ` (value: `"TJ"`)

* `TK` (value: `"TK"`)

* `TN` (value: `"TN"`)

* `TS` (value: `"TS"`)

* `TT` (value: `"TT"`)

* `TT2` (value: `"TT"`)

* `TX` (value: `"TX"`)

* `TY` (value: `"TY"`)

* `UT` (value: `"UT"`)

* `VA` (value: `"VA"`)

* `VI` (value: `"VI"`)

* `VI2` (value: `"VI"`)

* `VT` (value: `"VT"`)

* `WA` (value: `"WA"`)

* `WA2` (value: `"WA"`)

* `WI` (value: `"WI"`)

* `WK` (value: `"WK"`)

* `WV` (value: `"WV"`)

* `WY` (value: `"WY"`)

* `XJ` (value: `"XJ"`)

* `XZ` (value: `"XZ"`)

* `YA` (value: `"YA"`)

* `YN` (value: `"YN"`)

* `YN2` (value: `"YN"`)

* `YT` (value: `"YT"`)

* `YU` (value: `"YU"`)

* `ZJ` (value: `"ZJ"`)




