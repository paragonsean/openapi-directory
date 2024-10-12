# OpenapiJsClient.DoctorFeeSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedAmount** | **Number** | Typical allowed amount for payer. Not used if blank. | [optional] 
**basePrice** | **Number** |  | [optional] 
**billingDescription** | **String** |  | [optional] 
**cashPrice** | **Number** |  | [optional] 
**code** | **String** |  | [optional] 
**codeType** | **String** |  | [optional] 
**cptHcpcsModifier1** | **String** |  | [optional] 
**cptHcpcsModifier2** | **String** |  | [optional] 
**cptHcpcsModifier3** | **String** |  | [optional] 
**cptHcpcsModifier4** | **String** |  | [optional] 
**createdAt** | **String** |  | [optional] [readonly] 
**description** | **String** |  | [optional] 
**doctor** | **Number** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**insuredOutOfNetworkPrice** | **Number** |  | [optional] 
**insuredPrice** | **Number** |  | [optional] 
**ndcCode** | **String** |  | [optional] 
**ndcQuantity** | **Number** |  | [optional] 
**ndcUnits** | **String** |  | [optional] 
**office** | **Number** |  | [optional] 
**payerId** | **String** | Fee Schedule pricing specific to this payer, if null, then applies as default to all payers without a more specific fee schedule. | [optional] 
**picklistCategory** | **String** | Optional: Category to organize the code into. | [optional] 
**planName** | **String** | Name of insurance plan. | [optional] 
**updatedAt** | **String** |  | [optional] [readonly] 



## Enum: CodeTypeEnum


* `CPT` (value: `"CPT"`)

* `HCPCS` (value: `"HCPCS"`)

* `Custom` (value: `"Custom"`)

* `ICD9` (value: `"ICD9"`)

* `ICD10` (value: `"ICD10"`)

* `Revenue` (value: `"Revenue"`)





## Enum: CptHcpcsModifier2Enum


* `empty` (value: `""`)

* `17` (value: `"17"`)

* `1D` (value: `"1D"`)

* `22` (value: `"22"`)

* `23` (value: `"23"`)

* `24` (value: `"24"`)

* `25` (value: `"25"`)

* `26` (value: `"26"`)

* `29` (value: `"29"`)

* `32` (value: `"32"`)

* `33` (value: `"33"`)

* `47` (value: `"47"`)

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

* `62` (value: `"62"`)

* `63` (value: `"63"`)

* `66` (value: `"66"`)

* `73` (value: `"73"`)

* `74` (value: `"74"`)

* `76` (value: `"76"`)

* `77` (value: `"77"`)

* `78` (value: `"78"`)

* `79` (value: `"79"`)

* `80` (value: `"80"`)

* `81` (value: `"81"`)

* `82` (value: `"82"`)

* `83` (value: `"83"`)

* `90` (value: `"90"`)

* `91` (value: `"91"`)

* `92` (value: `"92"`)

* `93` (value: `"93"`)

* `95` (value: `"95"`)

* `96` (value: `"96"`)

* `97` (value: `"97"`)

* `99` (value: `"99"`)

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

* `AD` (value: `"AD"`)

* `AE` (value: `"AE"`)

* `AF` (value: `"AF"`)

* `AG` (value: `"AG"`)

* `AH` (value: `"AH"`)

* `AI` (value: `"AI"`)

* `AJ` (value: `"AJ"`)

* `AK` (value: `"AK"`)

* `AM` (value: `"AM"`)

* `AO` (value: `"AO"`)

* `AP` (value: `"AP"`)

* `AQ` (value: `"AQ"`)

* `AR` (value: `"AR"`)

* `AS` (value: `"AS"`)

* `AT` (value: `"AT"`)

* `AU` (value: `"AU"`)

* `AV` (value: `"AV"`)

* `AW` (value: `"AW"`)

* `AX` (value: `"AX"`)

* `AY` (value: `"AY"`)

* `AZ` (value: `"AZ"`)

* `BA` (value: `"BA"`)

* `BL` (value: `"BL"`)

* `BO` (value: `"BO"`)

* `BP` (value: `"BP"`)

* `BR` (value: `"BR"`)

* `BU` (value: `"BU"`)

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

* `CR` (value: `"CR"`)

* `CS` (value: `"CS"`)

* `CT` (value: `"CT"`)

* `DA` (value: `"DA"`)

* `E1` (value: `"E1"`)

* `E2` (value: `"E2"`)

* `E3` (value: `"E3"`)

* `E4` (value: `"E4"`)

* `EA` (value: `"EA"`)

* `EB` (value: `"EB"`)

* `EC` (value: `"EC"`)

* `ED` (value: `"ED"`)

* `EE` (value: `"EE"`)

* `EJ` (value: `"EJ"`)

* `EM` (value: `"EM"`)

* `EP` (value: `"EP"`)

* `ER` (value: `"ER"`)

* `ET` (value: `"ET"`)

* `EX` (value: `"EX"`)

* `EY` (value: `"EY"`)

* `F1` (value: `"F1"`)

* `F2` (value: `"F2"`)

* `F3` (value: `"F3"`)

* `F4` (value: `"F4"`)

* `F5` (value: `"F5"`)

* `F6` (value: `"F6"`)

* `F7` (value: `"F7"`)

* `F8` (value: `"F8"`)

* `F9` (value: `"F9"`)

* `FA` (value: `"FA"`)

* `FB` (value: `"FB"`)

* `FC` (value: `"FC"`)

* `FP` (value: `"FP"`)

* `FX` (value: `"FX"`)

* `FY` (value: `"FY"`)

* `G0` (value: `"G0"`)

* `G1` (value: `"G1"`)

* `G2` (value: `"G2"`)

* `G3` (value: `"G3"`)

* `G4` (value: `"G4"`)

* `G5` (value: `"G5"`)

* `G6` (value: `"G6"`)

* `G7` (value: `"G7"`)

* `G8` (value: `"G8"`)

* `G9` (value: `"G9"`)

* `GA` (value: `"GA"`)

* `GB` (value: `"GB"`)

* `GC` (value: `"GC"`)

* `GD` (value: `"GD"`)

* `GE` (value: `"GE"`)

* `GF` (value: `"GF"`)

* `GG` (value: `"GG"`)

* `GH` (value: `"GH"`)

* `GJ` (value: `"GJ"`)

* `GK` (value: `"GK"`)

* `GL` (value: `"GL"`)

* `GM` (value: `"GM"`)

* `GN` (value: `"GN"`)

* `GO` (value: `"GO"`)

* `GP` (value: `"GP"`)

* `GQ` (value: `"GQ"`)

* `GR` (value: `"GR"`)

* `GS` (value: `"GS"`)

* `GT` (value: `"GT"`)

* `GU` (value: `"GU"`)

* `GV` (value: `"GV"`)

* `GW` (value: `"GW"`)

* `GX` (value: `"GX"`)

* `GY` (value: `"GY"`)

* `GZ` (value: `"GZ"`)

* `H9` (value: `"H9"`)

* `HA` (value: `"HA"`)

* `HB` (value: `"HB"`)

* `HC` (value: `"HC"`)

* `HD` (value: `"HD"`)

* `HE` (value: `"HE"`)

* `HF` (value: `"HF"`)

* `HG` (value: `"HG"`)

* `HH` (value: `"HH"`)

* `HI` (value: `"HI"`)

* `HJ` (value: `"HJ"`)

* `HK` (value: `"HK"`)

* `HL` (value: `"HL"`)

* `HM` (value: `"HM"`)

* `HN` (value: `"HN"`)

* `HO` (value: `"HO"`)

* `HP` (value: `"HP"`)

* `HQ` (value: `"HQ"`)

* `HR` (value: `"HR"`)

* `HS` (value: `"HS"`)

* `HT` (value: `"HT"`)

* `HU` (value: `"HU"`)

* `HV` (value: `"HV"`)

* `HW` (value: `"HW"`)

* `HX` (value: `"HX"`)

* `HY` (value: `"HY"`)

* `HZ` (value: `"HZ"`)

* `J1` (value: `"J1"`)

* `J2` (value: `"J2"`)

* `J3` (value: `"J3"`)

* `J4` (value: `"J4"`)

* `JA` (value: `"JA"`)

* `JB` (value: `"JB"`)

* `JC` (value: `"JC"`)

* `JD` (value: `"JD"`)

* `JE` (value: `"JE"`)

* `JF` (value: `"JF"`)

* `JG` (value: `"JG"`)

* `JW` (value: `"JW"`)

* `K0` (value: `"K0"`)

* `K1` (value: `"K1"`)

* `K2` (value: `"K2"`)

* `K3` (value: `"K3"`)

* `K4` (value: `"K4"`)

* `KA` (value: `"KA"`)

* `KB` (value: `"KB"`)

* `KC` (value: `"KC"`)

* `KD` (value: `"KD"`)

* `KE` (value: `"KE"`)

* `KF` (value: `"KF"`)

* `KG` (value: `"KG"`)

* `KH` (value: `"KH"`)

* `KI` (value: `"KI"`)

* `KJ` (value: `"KJ"`)

* `KK` (value: `"KK"`)

* `KL` (value: `"KL"`)

* `KM` (value: `"KM"`)

* `KN` (value: `"KN"`)

* `KO` (value: `"KO"`)

* `KP` (value: `"KP"`)

* `KQ` (value: `"KQ"`)

* `KR` (value: `"KR"`)

* `KS` (value: `"KS"`)

* `KT` (value: `"KT"`)

* `KU` (value: `"KU"`)

* `KV` (value: `"KV"`)

* `KW` (value: `"KW"`)

* `KX` (value: `"KX"`)

* `KY` (value: `"KY"`)

* `KZ` (value: `"KZ"`)

* `L1` (value: `"L1"`)

* `LC` (value: `"LC"`)

* `LD` (value: `"LD"`)

* `LL` (value: `"LL"`)

* `LM` (value: `"LM"`)

* `LR` (value: `"LR"`)

* `LS` (value: `"LS"`)

* `LT` (value: `"LT"`)

* `M2` (value: `"M2"`)

* `ME` (value: `"ME"`)

* `MI` (value: `"MI"`)

* `MR` (value: `"MR"`)

* `MS` (value: `"MS"`)

* `NB` (value: `"NB"`)

* `NH` (value: `"NH"`)

* `NM` (value: `"NM"`)

* `NR` (value: `"NR"`)

* `NU` (value: `"NU"`)

* `P1` (value: `"P1"`)

* `P2` (value: `"P2"`)

* `P3` (value: `"P3"`)

* `P4` (value: `"P4"`)

* `P5` (value: `"P5"`)

* `P6` (value: `"P6"`)

* `PA` (value: `"PA"`)

* `PB` (value: `"PB"`)

* `PC` (value: `"PC"`)

* `PD` (value: `"PD"`)

* `PE` (value: `"PE"`)

* `PI` (value: `"PI"`)

* `PL` (value: `"PL"`)

* `PM` (value: `"PM"`)

* `PN` (value: `"PN"`)

* `PO` (value: `"PO"`)

* `PS` (value: `"PS"`)

* `PT` (value: `"PT"`)

* `Q0` (value: `"Q0"`)

* `Q1` (value: `"Q1"`)

* `Q2` (value: `"Q2"`)

* `Q3` (value: `"Q3"`)

* `Q4` (value: `"Q4"`)

* `Q5` (value: `"Q5"`)

* `Q6` (value: `"Q6"`)

* `Q7` (value: `"Q7"`)

* `Q8` (value: `"Q8"`)

* `Q9` (value: `"Q9"`)

* `QA` (value: `"QA"`)

* `QB` (value: `"QB"`)

* `QC` (value: `"QC"`)

* `QD` (value: `"QD"`)

* `QE` (value: `"QE"`)

* `QF` (value: `"QF"`)

* `QG` (value: `"QG"`)

* `QH` (value: `"QH"`)

* `QJ` (value: `"QJ"`)

* `QK` (value: `"QK"`)

* `QL` (value: `"QL"`)

* `QM` (value: `"QM"`)

* `QN` (value: `"QN"`)

* `QP` (value: `"QP"`)

* `QQ` (value: `"QQ"`)

* `QR` (value: `"QR"`)

* `QS` (value: `"QS"`)

* `QT` (value: `"QT"`)

* `QU` (value: `"QU"`)

* `QV` (value: `"QV"`)

* `QW` (value: `"QW"`)

* `QX` (value: `"QX"`)

* `QY` (value: `"QY"`)

* `QZ` (value: `"QZ"`)

* `RA` (value: `"RA"`)

* `RB` (value: `"RB"`)

* `RC` (value: `"RC"`)

* `RD` (value: `"RD"`)

* `RE` (value: `"RE"`)

* `RI` (value: `"RI"`)

* `RP` (value: `"RP"`)

* `RR` (value: `"RR"`)

* `RT` (value: `"RT"`)

* `SA` (value: `"SA"`)

* `SB` (value: `"SB"`)

* `SC` (value: `"SC"`)

* `SD` (value: `"SD"`)

* `SE` (value: `"SE"`)

* `SF` (value: `"SF"`)

* `SG` (value: `"SG"`)

* `SH` (value: `"SH"`)

* `SJ` (value: `"SJ"`)

* `SK` (value: `"SK"`)

* `SL` (value: `"SL"`)

* `SM` (value: `"SM"`)

* `SN` (value: `"SN"`)

* `SP` (value: `"SP"`)

* `SQ` (value: `"SQ"`)

* `SS` (value: `"SS"`)

* `ST` (value: `"ST"`)

* `SU` (value: `"SU"`)

* `SV` (value: `"SV"`)

* `SW` (value: `"SW"`)

* `SY` (value: `"SY"`)

* `SZ` (value: `"SZ"`)

* `T1` (value: `"T1"`)

* `T2` (value: `"T2"`)

* `T3` (value: `"T3"`)

* `T4` (value: `"T4"`)

* `T5` (value: `"T5"`)

* `T6` (value: `"T6"`)

* `T7` (value: `"T7"`)

* `T8` (value: `"T8"`)

* `T9` (value: `"T9"`)

* `TA` (value: `"TA"`)

* `TB` (value: `"TB"`)

* `TC` (value: `"TC"`)

* `TD` (value: `"TD"`)

* `TE` (value: `"TE"`)

* `TF` (value: `"TF"`)

* `TG` (value: `"TG"`)

* `TH` (value: `"TH"`)

* `TJ` (value: `"TJ"`)

* `TK` (value: `"TK"`)

* `TL` (value: `"TL"`)

* `TM` (value: `"TM"`)

* `TN` (value: `"TN"`)

* `TP` (value: `"TP"`)

* `TQ` (value: `"TQ"`)

* `TR` (value: `"TR"`)

* `TS` (value: `"TS"`)

* `TT` (value: `"TT"`)

* `TU` (value: `"TU"`)

* `TV` (value: `"TV"`)

* `TW` (value: `"TW"`)

* `TX` (value: `"TX"`)

* `U1` (value: `"U1"`)

* `U2` (value: `"U2"`)

* `U3` (value: `"U3"`)

* `U4` (value: `"U4"`)

* `U5` (value: `"U5"`)

* `U6` (value: `"U6"`)

* `U7` (value: `"U7"`)

* `U8` (value: `"U8"`)

* `U9` (value: `"U9"`)

* `UA` (value: `"UA"`)

* `UB` (value: `"UB"`)

* `UC` (value: `"UC"`)

* `UD` (value: `"UD"`)

* `UE` (value: `"UE"`)

* `UF` (value: `"UF"`)

* `UG` (value: `"UG"`)

* `UH` (value: `"UH"`)

* `UJ` (value: `"UJ"`)

* `UK` (value: `"UK"`)

* `UN` (value: `"UN"`)

* `UP` (value: `"UP"`)

* `UQ` (value: `"UQ"`)

* `UR` (value: `"UR"`)

* `US` (value: `"US"`)

* `V1` (value: `"V1"`)

* `V2` (value: `"V2"`)

* `V3` (value: `"V3"`)

* `V4` (value: `"V4"`)

* `V5` (value: `"V5"`)

* `V6` (value: `"V6"`)

* `V7` (value: `"V7"`)

* `V8` (value: `"V8"`)

* `V9` (value: `"V9"`)

* `VP` (value: `"VP"`)

* `VR` (value: `"VR"`)

* `W1` (value: `"W1"`)

* `W5` (value: `"W5"`)

* `W6` (value: `"W6"`)

* `W7` (value: `"W7"`)

* `W8` (value: `"W8"`)

* `W9` (value: `"W9"`)

* `WC` (value: `"WC"`)

* `WH` (value: `"WH"`)

* `WP` (value: `"WP"`)

* `X1` (value: `"X1"`)

* `X2` (value: `"X2"`)

* `X3` (value: `"X3"`)

* `X4` (value: `"X4"`)

* `X5` (value: `"X5"`)

* `XE` (value: `"XE"`)

* `XP` (value: `"XP"`)

* `XS` (value: `"XS"`)

* `XU` (value: `"XU"`)

* `VM` (value: `"VM"`)

* `ZA` (value: `"ZA"`)

* `ZB` (value: `"ZB"`)

* `ZL` (value: `"ZL"`)

* `ZS` (value: `"ZS"`)

* `1P` (value: `"1P"`)

* `2P` (value: `"2P"`)

* `3P` (value: `"3P"`)

* `8P` (value: `"8P"`)





## Enum: CptHcpcsModifier3Enum


* `empty` (value: `""`)

* `17` (value: `"17"`)

* `1D` (value: `"1D"`)

* `22` (value: `"22"`)

* `23` (value: `"23"`)

* `24` (value: `"24"`)

* `25` (value: `"25"`)

* `26` (value: `"26"`)

* `29` (value: `"29"`)

* `32` (value: `"32"`)

* `33` (value: `"33"`)

* `47` (value: `"47"`)

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

* `62` (value: `"62"`)

* `63` (value: `"63"`)

* `66` (value: `"66"`)

* `73` (value: `"73"`)

* `74` (value: `"74"`)

* `76` (value: `"76"`)

* `77` (value: `"77"`)

* `78` (value: `"78"`)

* `79` (value: `"79"`)

* `80` (value: `"80"`)

* `81` (value: `"81"`)

* `82` (value: `"82"`)

* `83` (value: `"83"`)

* `90` (value: `"90"`)

* `91` (value: `"91"`)

* `92` (value: `"92"`)

* `93` (value: `"93"`)

* `95` (value: `"95"`)

* `96` (value: `"96"`)

* `97` (value: `"97"`)

* `99` (value: `"99"`)

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

* `AD` (value: `"AD"`)

* `AE` (value: `"AE"`)

* `AF` (value: `"AF"`)

* `AG` (value: `"AG"`)

* `AH` (value: `"AH"`)

* `AI` (value: `"AI"`)

* `AJ` (value: `"AJ"`)

* `AK` (value: `"AK"`)

* `AM` (value: `"AM"`)

* `AO` (value: `"AO"`)

* `AP` (value: `"AP"`)

* `AQ` (value: `"AQ"`)

* `AR` (value: `"AR"`)

* `AS` (value: `"AS"`)

* `AT` (value: `"AT"`)

* `AU` (value: `"AU"`)

* `AV` (value: `"AV"`)

* `AW` (value: `"AW"`)

* `AX` (value: `"AX"`)

* `AY` (value: `"AY"`)

* `AZ` (value: `"AZ"`)

* `BA` (value: `"BA"`)

* `BL` (value: `"BL"`)

* `BO` (value: `"BO"`)

* `BP` (value: `"BP"`)

* `BR` (value: `"BR"`)

* `BU` (value: `"BU"`)

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

* `CR` (value: `"CR"`)

* `CS` (value: `"CS"`)

* `CT` (value: `"CT"`)

* `DA` (value: `"DA"`)

* `E1` (value: `"E1"`)

* `E2` (value: `"E2"`)

* `E3` (value: `"E3"`)

* `E4` (value: `"E4"`)

* `EA` (value: `"EA"`)

* `EB` (value: `"EB"`)

* `EC` (value: `"EC"`)

* `ED` (value: `"ED"`)

* `EE` (value: `"EE"`)

* `EJ` (value: `"EJ"`)

* `EM` (value: `"EM"`)

* `EP` (value: `"EP"`)

* `ER` (value: `"ER"`)

* `ET` (value: `"ET"`)

* `EX` (value: `"EX"`)

* `EY` (value: `"EY"`)

* `F1` (value: `"F1"`)

* `F2` (value: `"F2"`)

* `F3` (value: `"F3"`)

* `F4` (value: `"F4"`)

* `F5` (value: `"F5"`)

* `F6` (value: `"F6"`)

* `F7` (value: `"F7"`)

* `F8` (value: `"F8"`)

* `F9` (value: `"F9"`)

* `FA` (value: `"FA"`)

* `FB` (value: `"FB"`)

* `FC` (value: `"FC"`)

* `FP` (value: `"FP"`)

* `FX` (value: `"FX"`)

* `FY` (value: `"FY"`)

* `G0` (value: `"G0"`)

* `G1` (value: `"G1"`)

* `G2` (value: `"G2"`)

* `G3` (value: `"G3"`)

* `G4` (value: `"G4"`)

* `G5` (value: `"G5"`)

* `G6` (value: `"G6"`)

* `G7` (value: `"G7"`)

* `G8` (value: `"G8"`)

* `G9` (value: `"G9"`)

* `GA` (value: `"GA"`)

* `GB` (value: `"GB"`)

* `GC` (value: `"GC"`)

* `GD` (value: `"GD"`)

* `GE` (value: `"GE"`)

* `GF` (value: `"GF"`)

* `GG` (value: `"GG"`)

* `GH` (value: `"GH"`)

* `GJ` (value: `"GJ"`)

* `GK` (value: `"GK"`)

* `GL` (value: `"GL"`)

* `GM` (value: `"GM"`)

* `GN` (value: `"GN"`)

* `GO` (value: `"GO"`)

* `GP` (value: `"GP"`)

* `GQ` (value: `"GQ"`)

* `GR` (value: `"GR"`)

* `GS` (value: `"GS"`)

* `GT` (value: `"GT"`)

* `GU` (value: `"GU"`)

* `GV` (value: `"GV"`)

* `GW` (value: `"GW"`)

* `GX` (value: `"GX"`)

* `GY` (value: `"GY"`)

* `GZ` (value: `"GZ"`)

* `H9` (value: `"H9"`)

* `HA` (value: `"HA"`)

* `HB` (value: `"HB"`)

* `HC` (value: `"HC"`)

* `HD` (value: `"HD"`)

* `HE` (value: `"HE"`)

* `HF` (value: `"HF"`)

* `HG` (value: `"HG"`)

* `HH` (value: `"HH"`)

* `HI` (value: `"HI"`)

* `HJ` (value: `"HJ"`)

* `HK` (value: `"HK"`)

* `HL` (value: `"HL"`)

* `HM` (value: `"HM"`)

* `HN` (value: `"HN"`)

* `HO` (value: `"HO"`)

* `HP` (value: `"HP"`)

* `HQ` (value: `"HQ"`)

* `HR` (value: `"HR"`)

* `HS` (value: `"HS"`)

* `HT` (value: `"HT"`)

* `HU` (value: `"HU"`)

* `HV` (value: `"HV"`)

* `HW` (value: `"HW"`)

* `HX` (value: `"HX"`)

* `HY` (value: `"HY"`)

* `HZ` (value: `"HZ"`)

* `J1` (value: `"J1"`)

* `J2` (value: `"J2"`)

* `J3` (value: `"J3"`)

* `J4` (value: `"J4"`)

* `JA` (value: `"JA"`)

* `JB` (value: `"JB"`)

* `JC` (value: `"JC"`)

* `JD` (value: `"JD"`)

* `JE` (value: `"JE"`)

* `JF` (value: `"JF"`)

* `JG` (value: `"JG"`)

* `JW` (value: `"JW"`)

* `K0` (value: `"K0"`)

* `K1` (value: `"K1"`)

* `K2` (value: `"K2"`)

* `K3` (value: `"K3"`)

* `K4` (value: `"K4"`)

* `KA` (value: `"KA"`)

* `KB` (value: `"KB"`)

* `KC` (value: `"KC"`)

* `KD` (value: `"KD"`)

* `KE` (value: `"KE"`)

* `KF` (value: `"KF"`)

* `KG` (value: `"KG"`)

* `KH` (value: `"KH"`)

* `KI` (value: `"KI"`)

* `KJ` (value: `"KJ"`)

* `KK` (value: `"KK"`)

* `KL` (value: `"KL"`)

* `KM` (value: `"KM"`)

* `KN` (value: `"KN"`)

* `KO` (value: `"KO"`)

* `KP` (value: `"KP"`)

* `KQ` (value: `"KQ"`)

* `KR` (value: `"KR"`)

* `KS` (value: `"KS"`)

* `KT` (value: `"KT"`)

* `KU` (value: `"KU"`)

* `KV` (value: `"KV"`)

* `KW` (value: `"KW"`)

* `KX` (value: `"KX"`)

* `KY` (value: `"KY"`)

* `KZ` (value: `"KZ"`)

* `L1` (value: `"L1"`)

* `LC` (value: `"LC"`)

* `LD` (value: `"LD"`)

* `LL` (value: `"LL"`)

* `LM` (value: `"LM"`)

* `LR` (value: `"LR"`)

* `LS` (value: `"LS"`)

* `LT` (value: `"LT"`)

* `M2` (value: `"M2"`)

* `ME` (value: `"ME"`)

* `MI` (value: `"MI"`)

* `MR` (value: `"MR"`)

* `MS` (value: `"MS"`)

* `NB` (value: `"NB"`)

* `NH` (value: `"NH"`)

* `NM` (value: `"NM"`)

* `NR` (value: `"NR"`)

* `NU` (value: `"NU"`)

* `P1` (value: `"P1"`)

* `P2` (value: `"P2"`)

* `P3` (value: `"P3"`)

* `P4` (value: `"P4"`)

* `P5` (value: `"P5"`)

* `P6` (value: `"P6"`)

* `PA` (value: `"PA"`)

* `PB` (value: `"PB"`)

* `PC` (value: `"PC"`)

* `PD` (value: `"PD"`)

* `PE` (value: `"PE"`)

* `PI` (value: `"PI"`)

* `PL` (value: `"PL"`)

* `PM` (value: `"PM"`)

* `PN` (value: `"PN"`)

* `PO` (value: `"PO"`)

* `PS` (value: `"PS"`)

* `PT` (value: `"PT"`)

* `Q0` (value: `"Q0"`)

* `Q1` (value: `"Q1"`)

* `Q2` (value: `"Q2"`)

* `Q3` (value: `"Q3"`)

* `Q4` (value: `"Q4"`)

* `Q5` (value: `"Q5"`)

* `Q6` (value: `"Q6"`)

* `Q7` (value: `"Q7"`)

* `Q8` (value: `"Q8"`)

* `Q9` (value: `"Q9"`)

* `QA` (value: `"QA"`)

* `QB` (value: `"QB"`)

* `QC` (value: `"QC"`)

* `QD` (value: `"QD"`)

* `QE` (value: `"QE"`)

* `QF` (value: `"QF"`)

* `QG` (value: `"QG"`)

* `QH` (value: `"QH"`)

* `QJ` (value: `"QJ"`)

* `QK` (value: `"QK"`)

* `QL` (value: `"QL"`)

* `QM` (value: `"QM"`)

* `QN` (value: `"QN"`)

* `QP` (value: `"QP"`)

* `QQ` (value: `"QQ"`)

* `QR` (value: `"QR"`)

* `QS` (value: `"QS"`)

* `QT` (value: `"QT"`)

* `QU` (value: `"QU"`)

* `QV` (value: `"QV"`)

* `QW` (value: `"QW"`)

* `QX` (value: `"QX"`)

* `QY` (value: `"QY"`)

* `QZ` (value: `"QZ"`)

* `RA` (value: `"RA"`)

* `RB` (value: `"RB"`)

* `RC` (value: `"RC"`)

* `RD` (value: `"RD"`)

* `RE` (value: `"RE"`)

* `RI` (value: `"RI"`)

* `RP` (value: `"RP"`)

* `RR` (value: `"RR"`)

* `RT` (value: `"RT"`)

* `SA` (value: `"SA"`)

* `SB` (value: `"SB"`)

* `SC` (value: `"SC"`)

* `SD` (value: `"SD"`)

* `SE` (value: `"SE"`)

* `SF` (value: `"SF"`)

* `SG` (value: `"SG"`)

* `SH` (value: `"SH"`)

* `SJ` (value: `"SJ"`)

* `SK` (value: `"SK"`)

* `SL` (value: `"SL"`)

* `SM` (value: `"SM"`)

* `SN` (value: `"SN"`)

* `SP` (value: `"SP"`)

* `SQ` (value: `"SQ"`)

* `SS` (value: `"SS"`)

* `ST` (value: `"ST"`)

* `SU` (value: `"SU"`)

* `SV` (value: `"SV"`)

* `SW` (value: `"SW"`)

* `SY` (value: `"SY"`)

* `SZ` (value: `"SZ"`)

* `T1` (value: `"T1"`)

* `T2` (value: `"T2"`)

* `T3` (value: `"T3"`)

* `T4` (value: `"T4"`)

* `T5` (value: `"T5"`)

* `T6` (value: `"T6"`)

* `T7` (value: `"T7"`)

* `T8` (value: `"T8"`)

* `T9` (value: `"T9"`)

* `TA` (value: `"TA"`)

* `TB` (value: `"TB"`)

* `TC` (value: `"TC"`)

* `TD` (value: `"TD"`)

* `TE` (value: `"TE"`)

* `TF` (value: `"TF"`)

* `TG` (value: `"TG"`)

* `TH` (value: `"TH"`)

* `TJ` (value: `"TJ"`)

* `TK` (value: `"TK"`)

* `TL` (value: `"TL"`)

* `TM` (value: `"TM"`)

* `TN` (value: `"TN"`)

* `TP` (value: `"TP"`)

* `TQ` (value: `"TQ"`)

* `TR` (value: `"TR"`)

* `TS` (value: `"TS"`)

* `TT` (value: `"TT"`)

* `TU` (value: `"TU"`)

* `TV` (value: `"TV"`)

* `TW` (value: `"TW"`)

* `TX` (value: `"TX"`)

* `U1` (value: `"U1"`)

* `U2` (value: `"U2"`)

* `U3` (value: `"U3"`)

* `U4` (value: `"U4"`)

* `U5` (value: `"U5"`)

* `U6` (value: `"U6"`)

* `U7` (value: `"U7"`)

* `U8` (value: `"U8"`)

* `U9` (value: `"U9"`)

* `UA` (value: `"UA"`)

* `UB` (value: `"UB"`)

* `UC` (value: `"UC"`)

* `UD` (value: `"UD"`)

* `UE` (value: `"UE"`)

* `UF` (value: `"UF"`)

* `UG` (value: `"UG"`)

* `UH` (value: `"UH"`)

* `UJ` (value: `"UJ"`)

* `UK` (value: `"UK"`)

* `UN` (value: `"UN"`)

* `UP` (value: `"UP"`)

* `UQ` (value: `"UQ"`)

* `UR` (value: `"UR"`)

* `US` (value: `"US"`)

* `V1` (value: `"V1"`)

* `V2` (value: `"V2"`)

* `V3` (value: `"V3"`)

* `V4` (value: `"V4"`)

* `V5` (value: `"V5"`)

* `V6` (value: `"V6"`)

* `V7` (value: `"V7"`)

* `V8` (value: `"V8"`)

* `V9` (value: `"V9"`)

* `VP` (value: `"VP"`)

* `VR` (value: `"VR"`)

* `W1` (value: `"W1"`)

* `W5` (value: `"W5"`)

* `W6` (value: `"W6"`)

* `W7` (value: `"W7"`)

* `W8` (value: `"W8"`)

* `W9` (value: `"W9"`)

* `WC` (value: `"WC"`)

* `WH` (value: `"WH"`)

* `WP` (value: `"WP"`)

* `X1` (value: `"X1"`)

* `X2` (value: `"X2"`)

* `X3` (value: `"X3"`)

* `X4` (value: `"X4"`)

* `X5` (value: `"X5"`)

* `XE` (value: `"XE"`)

* `XP` (value: `"XP"`)

* `XS` (value: `"XS"`)

* `XU` (value: `"XU"`)

* `VM` (value: `"VM"`)

* `ZA` (value: `"ZA"`)

* `ZB` (value: `"ZB"`)

* `ZL` (value: `"ZL"`)

* `ZS` (value: `"ZS"`)

* `1P` (value: `"1P"`)

* `2P` (value: `"2P"`)

* `3P` (value: `"3P"`)

* `8P` (value: `"8P"`)





## Enum: CptHcpcsModifier4Enum


* `empty` (value: `""`)

* `17` (value: `"17"`)

* `1D` (value: `"1D"`)

* `22` (value: `"22"`)

* `23` (value: `"23"`)

* `24` (value: `"24"`)

* `25` (value: `"25"`)

* `26` (value: `"26"`)

* `29` (value: `"29"`)

* `32` (value: `"32"`)

* `33` (value: `"33"`)

* `47` (value: `"47"`)

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

* `62` (value: `"62"`)

* `63` (value: `"63"`)

* `66` (value: `"66"`)

* `73` (value: `"73"`)

* `74` (value: `"74"`)

* `76` (value: `"76"`)

* `77` (value: `"77"`)

* `78` (value: `"78"`)

* `79` (value: `"79"`)

* `80` (value: `"80"`)

* `81` (value: `"81"`)

* `82` (value: `"82"`)

* `83` (value: `"83"`)

* `90` (value: `"90"`)

* `91` (value: `"91"`)

* `92` (value: `"92"`)

* `93` (value: `"93"`)

* `95` (value: `"95"`)

* `96` (value: `"96"`)

* `97` (value: `"97"`)

* `99` (value: `"99"`)

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

* `AD` (value: `"AD"`)

* `AE` (value: `"AE"`)

* `AF` (value: `"AF"`)

* `AG` (value: `"AG"`)

* `AH` (value: `"AH"`)

* `AI` (value: `"AI"`)

* `AJ` (value: `"AJ"`)

* `AK` (value: `"AK"`)

* `AM` (value: `"AM"`)

* `AO` (value: `"AO"`)

* `AP` (value: `"AP"`)

* `AQ` (value: `"AQ"`)

* `AR` (value: `"AR"`)

* `AS` (value: `"AS"`)

* `AT` (value: `"AT"`)

* `AU` (value: `"AU"`)

* `AV` (value: `"AV"`)

* `AW` (value: `"AW"`)

* `AX` (value: `"AX"`)

* `AY` (value: `"AY"`)

* `AZ` (value: `"AZ"`)

* `BA` (value: `"BA"`)

* `BL` (value: `"BL"`)

* `BO` (value: `"BO"`)

* `BP` (value: `"BP"`)

* `BR` (value: `"BR"`)

* `BU` (value: `"BU"`)

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

* `CR` (value: `"CR"`)

* `CS` (value: `"CS"`)

* `CT` (value: `"CT"`)

* `DA` (value: `"DA"`)

* `E1` (value: `"E1"`)

* `E2` (value: `"E2"`)

* `E3` (value: `"E3"`)

* `E4` (value: `"E4"`)

* `EA` (value: `"EA"`)

* `EB` (value: `"EB"`)

* `EC` (value: `"EC"`)

* `ED` (value: `"ED"`)

* `EE` (value: `"EE"`)

* `EJ` (value: `"EJ"`)

* `EM` (value: `"EM"`)

* `EP` (value: `"EP"`)

* `ER` (value: `"ER"`)

* `ET` (value: `"ET"`)

* `EX` (value: `"EX"`)

* `EY` (value: `"EY"`)

* `F1` (value: `"F1"`)

* `F2` (value: `"F2"`)

* `F3` (value: `"F3"`)

* `F4` (value: `"F4"`)

* `F5` (value: `"F5"`)

* `F6` (value: `"F6"`)

* `F7` (value: `"F7"`)

* `F8` (value: `"F8"`)

* `F9` (value: `"F9"`)

* `FA` (value: `"FA"`)

* `FB` (value: `"FB"`)

* `FC` (value: `"FC"`)

* `FP` (value: `"FP"`)

* `FX` (value: `"FX"`)

* `FY` (value: `"FY"`)

* `G0` (value: `"G0"`)

* `G1` (value: `"G1"`)

* `G2` (value: `"G2"`)

* `G3` (value: `"G3"`)

* `G4` (value: `"G4"`)

* `G5` (value: `"G5"`)

* `G6` (value: `"G6"`)

* `G7` (value: `"G7"`)

* `G8` (value: `"G8"`)

* `G9` (value: `"G9"`)

* `GA` (value: `"GA"`)

* `GB` (value: `"GB"`)

* `GC` (value: `"GC"`)

* `GD` (value: `"GD"`)

* `GE` (value: `"GE"`)

* `GF` (value: `"GF"`)

* `GG` (value: `"GG"`)

* `GH` (value: `"GH"`)

* `GJ` (value: `"GJ"`)

* `GK` (value: `"GK"`)

* `GL` (value: `"GL"`)

* `GM` (value: `"GM"`)

* `GN` (value: `"GN"`)

* `GO` (value: `"GO"`)

* `GP` (value: `"GP"`)

* `GQ` (value: `"GQ"`)

* `GR` (value: `"GR"`)

* `GS` (value: `"GS"`)

* `GT` (value: `"GT"`)

* `GU` (value: `"GU"`)

* `GV` (value: `"GV"`)

* `GW` (value: `"GW"`)

* `GX` (value: `"GX"`)

* `GY` (value: `"GY"`)

* `GZ` (value: `"GZ"`)

* `H9` (value: `"H9"`)

* `HA` (value: `"HA"`)

* `HB` (value: `"HB"`)

* `HC` (value: `"HC"`)

* `HD` (value: `"HD"`)

* `HE` (value: `"HE"`)

* `HF` (value: `"HF"`)

* `HG` (value: `"HG"`)

* `HH` (value: `"HH"`)

* `HI` (value: `"HI"`)

* `HJ` (value: `"HJ"`)

* `HK` (value: `"HK"`)

* `HL` (value: `"HL"`)

* `HM` (value: `"HM"`)

* `HN` (value: `"HN"`)

* `HO` (value: `"HO"`)

* `HP` (value: `"HP"`)

* `HQ` (value: `"HQ"`)

* `HR` (value: `"HR"`)

* `HS` (value: `"HS"`)

* `HT` (value: `"HT"`)

* `HU` (value: `"HU"`)

* `HV` (value: `"HV"`)

* `HW` (value: `"HW"`)

* `HX` (value: `"HX"`)

* `HY` (value: `"HY"`)

* `HZ` (value: `"HZ"`)

* `J1` (value: `"J1"`)

* `J2` (value: `"J2"`)

* `J3` (value: `"J3"`)

* `J4` (value: `"J4"`)

* `JA` (value: `"JA"`)

* `JB` (value: `"JB"`)

* `JC` (value: `"JC"`)

* `JD` (value: `"JD"`)

* `JE` (value: `"JE"`)

* `JF` (value: `"JF"`)

* `JG` (value: `"JG"`)

* `JW` (value: `"JW"`)

* `K0` (value: `"K0"`)

* `K1` (value: `"K1"`)

* `K2` (value: `"K2"`)

* `K3` (value: `"K3"`)

* `K4` (value: `"K4"`)

* `KA` (value: `"KA"`)

* `KB` (value: `"KB"`)

* `KC` (value: `"KC"`)

* `KD` (value: `"KD"`)

* `KE` (value: `"KE"`)

* `KF` (value: `"KF"`)

* `KG` (value: `"KG"`)

* `KH` (value: `"KH"`)

* `KI` (value: `"KI"`)

* `KJ` (value: `"KJ"`)

* `KK` (value: `"KK"`)

* `KL` (value: `"KL"`)

* `KM` (value: `"KM"`)

* `KN` (value: `"KN"`)

* `KO` (value: `"KO"`)

* `KP` (value: `"KP"`)

* `KQ` (value: `"KQ"`)

* `KR` (value: `"KR"`)

* `KS` (value: `"KS"`)

* `KT` (value: `"KT"`)

* `KU` (value: `"KU"`)

* `KV` (value: `"KV"`)

* `KW` (value: `"KW"`)

* `KX` (value: `"KX"`)

* `KY` (value: `"KY"`)

* `KZ` (value: `"KZ"`)

* `L1` (value: `"L1"`)

* `LC` (value: `"LC"`)

* `LD` (value: `"LD"`)

* `LL` (value: `"LL"`)

* `LM` (value: `"LM"`)

* `LR` (value: `"LR"`)

* `LS` (value: `"LS"`)

* `LT` (value: `"LT"`)

* `M2` (value: `"M2"`)

* `ME` (value: `"ME"`)

* `MI` (value: `"MI"`)

* `MR` (value: `"MR"`)

* `MS` (value: `"MS"`)

* `NB` (value: `"NB"`)

* `NH` (value: `"NH"`)

* `NM` (value: `"NM"`)

* `NR` (value: `"NR"`)

* `NU` (value: `"NU"`)

* `P1` (value: `"P1"`)

* `P2` (value: `"P2"`)

* `P3` (value: `"P3"`)

* `P4` (value: `"P4"`)

* `P5` (value: `"P5"`)

* `P6` (value: `"P6"`)

* `PA` (value: `"PA"`)

* `PB` (value: `"PB"`)

* `PC` (value: `"PC"`)

* `PD` (value: `"PD"`)

* `PE` (value: `"PE"`)

* `PI` (value: `"PI"`)

* `PL` (value: `"PL"`)

* `PM` (value: `"PM"`)

* `PN` (value: `"PN"`)

* `PO` (value: `"PO"`)

* `PS` (value: `"PS"`)

* `PT` (value: `"PT"`)

* `Q0` (value: `"Q0"`)

* `Q1` (value: `"Q1"`)

* `Q2` (value: `"Q2"`)

* `Q3` (value: `"Q3"`)

* `Q4` (value: `"Q4"`)

* `Q5` (value: `"Q5"`)

* `Q6` (value: `"Q6"`)

* `Q7` (value: `"Q7"`)

* `Q8` (value: `"Q8"`)

* `Q9` (value: `"Q9"`)

* `QA` (value: `"QA"`)

* `QB` (value: `"QB"`)

* `QC` (value: `"QC"`)

* `QD` (value: `"QD"`)

* `QE` (value: `"QE"`)

* `QF` (value: `"QF"`)

* `QG` (value: `"QG"`)

* `QH` (value: `"QH"`)

* `QJ` (value: `"QJ"`)

* `QK` (value: `"QK"`)

* `QL` (value: `"QL"`)

* `QM` (value: `"QM"`)

* `QN` (value: `"QN"`)

* `QP` (value: `"QP"`)

* `QQ` (value: `"QQ"`)

* `QR` (value: `"QR"`)

* `QS` (value: `"QS"`)

* `QT` (value: `"QT"`)

* `QU` (value: `"QU"`)

* `QV` (value: `"QV"`)

* `QW` (value: `"QW"`)

* `QX` (value: `"QX"`)

* `QY` (value: `"QY"`)

* `QZ` (value: `"QZ"`)

* `RA` (value: `"RA"`)

* `RB` (value: `"RB"`)

* `RC` (value: `"RC"`)

* `RD` (value: `"RD"`)

* `RE` (value: `"RE"`)

* `RI` (value: `"RI"`)

* `RP` (value: `"RP"`)

* `RR` (value: `"RR"`)

* `RT` (value: `"RT"`)

* `SA` (value: `"SA"`)

* `SB` (value: `"SB"`)

* `SC` (value: `"SC"`)

* `SD` (value: `"SD"`)

* `SE` (value: `"SE"`)

* `SF` (value: `"SF"`)

* `SG` (value: `"SG"`)

* `SH` (value: `"SH"`)

* `SJ` (value: `"SJ"`)

* `SK` (value: `"SK"`)

* `SL` (value: `"SL"`)

* `SM` (value: `"SM"`)

* `SN` (value: `"SN"`)

* `SP` (value: `"SP"`)

* `SQ` (value: `"SQ"`)

* `SS` (value: `"SS"`)

* `ST` (value: `"ST"`)

* `SU` (value: `"SU"`)

* `SV` (value: `"SV"`)

* `SW` (value: `"SW"`)

* `SY` (value: `"SY"`)

* `SZ` (value: `"SZ"`)

* `T1` (value: `"T1"`)

* `T2` (value: `"T2"`)

* `T3` (value: `"T3"`)

* `T4` (value: `"T4"`)

* `T5` (value: `"T5"`)

* `T6` (value: `"T6"`)

* `T7` (value: `"T7"`)

* `T8` (value: `"T8"`)

* `T9` (value: `"T9"`)

* `TA` (value: `"TA"`)

* `TB` (value: `"TB"`)

* `TC` (value: `"TC"`)

* `TD` (value: `"TD"`)

* `TE` (value: `"TE"`)

* `TF` (value: `"TF"`)

* `TG` (value: `"TG"`)

* `TH` (value: `"TH"`)

* `TJ` (value: `"TJ"`)

* `TK` (value: `"TK"`)

* `TL` (value: `"TL"`)

* `TM` (value: `"TM"`)

* `TN` (value: `"TN"`)

* `TP` (value: `"TP"`)

* `TQ` (value: `"TQ"`)

* `TR` (value: `"TR"`)

* `TS` (value: `"TS"`)

* `TT` (value: `"TT"`)

* `TU` (value: `"TU"`)

* `TV` (value: `"TV"`)

* `TW` (value: `"TW"`)

* `TX` (value: `"TX"`)

* `U1` (value: `"U1"`)

* `U2` (value: `"U2"`)

* `U3` (value: `"U3"`)

* `U4` (value: `"U4"`)

* `U5` (value: `"U5"`)

* `U6` (value: `"U6"`)

* `U7` (value: `"U7"`)

* `U8` (value: `"U8"`)

* `U9` (value: `"U9"`)

* `UA` (value: `"UA"`)

* `UB` (value: `"UB"`)

* `UC` (value: `"UC"`)

* `UD` (value: `"UD"`)

* `UE` (value: `"UE"`)

* `UF` (value: `"UF"`)

* `UG` (value: `"UG"`)

* `UH` (value: `"UH"`)

* `UJ` (value: `"UJ"`)

* `UK` (value: `"UK"`)

* `UN` (value: `"UN"`)

* `UP` (value: `"UP"`)

* `UQ` (value: `"UQ"`)

* `UR` (value: `"UR"`)

* `US` (value: `"US"`)

* `V1` (value: `"V1"`)

* `V2` (value: `"V2"`)

* `V3` (value: `"V3"`)

* `V4` (value: `"V4"`)

* `V5` (value: `"V5"`)

* `V6` (value: `"V6"`)

* `V7` (value: `"V7"`)

* `V8` (value: `"V8"`)

* `V9` (value: `"V9"`)

* `VP` (value: `"VP"`)

* `VR` (value: `"VR"`)

* `W1` (value: `"W1"`)

* `W5` (value: `"W5"`)

* `W6` (value: `"W6"`)

* `W7` (value: `"W7"`)

* `W8` (value: `"W8"`)

* `W9` (value: `"W9"`)

* `WC` (value: `"WC"`)

* `WH` (value: `"WH"`)

* `WP` (value: `"WP"`)

* `X1` (value: `"X1"`)

* `X2` (value: `"X2"`)

* `X3` (value: `"X3"`)

* `X4` (value: `"X4"`)

* `X5` (value: `"X5"`)

* `XE` (value: `"XE"`)

* `XP` (value: `"XP"`)

* `XS` (value: `"XS"`)

* `XU` (value: `"XU"`)

* `VM` (value: `"VM"`)

* `ZA` (value: `"ZA"`)

* `ZB` (value: `"ZB"`)

* `ZL` (value: `"ZL"`)

* `ZS` (value: `"ZS"`)

* `1P` (value: `"1P"`)

* `2P` (value: `"2P"`)

* `3P` (value: `"3P"`)

* `8P` (value: `"8P"`)





## Enum: NdcUnitsEnum


* `F2` (value: `"F2"`)

* `GR` (value: `"GR"`)

* `ME` (value: `"ME"`)

* `ML` (value: `"ML"`)

* `UN` (value: `"UN"`)




