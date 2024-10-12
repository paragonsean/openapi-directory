# OpenapiJsClient.LineItemTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment** | **Number** | Adjustment from total billed | [optional] 
**adjustmentGroupCode** | **String** | Group code for adjustment | [optional] [readonly] 
**adjustmentReason** | **String** | Reason for adjustment | [optional] 
**appointment** | **Number** | Appointment ID | [optional] 
**checkDate** | **String** | Date of check | [optional] [readonly] 
**claimStatus** | **String** | Status of claim | [optional] [readonly] 
**createdAt** | **String** |  | [optional] [readonly] 
**doctor** | **Number** | Doctor ID | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**insName** | **Number** | Can be one of the following, &#x60;1&#x60;(Primary Insurance), &#x60;2&#x60;(Secondary Insurance) | [optional] 
**insPaid** | **Number** |  | [optional] 
**lineItem** | **Number** | ID of &#x60;/api/line_item&#x60; object | [optional] 
**patient** | **Number** |  | [optional] 
**postedDate** | **String** | Date when transaction is created | [optional] [readonly] 
**traceNumber** | **String** | Check number | [optional] 
**updatedAt** | **String** |  | [optional] [readonly] 



## Enum: AdjustmentGroupCodeEnum


* `empty` (value: `""`)

* `CO` (value: `"CO"`)

* `OA` (value: `"OA"`)

* `PI` (value: `"PI"`)

* `PR` (value: `"PR"`)





## Enum: AdjustmentReasonEnum


* `-3` (value: `"-3"`)

* `-2` (value: `"-2"`)

* `-4` (value: `"-4"`)

* `-1` (value: `"-1"`)

* `0` (value: `"0"`)

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

* `18` (value: `"18"`)

* `19` (value: `"19"`)

* `20` (value: `"20"`)

* `21` (value: `"21"`)

* `22` (value: `"22"`)

* `23` (value: `"23"`)

* `24` (value: `"24"`)

* `26` (value: `"26"`)

* `27` (value: `"27"`)

* `29` (value: `"29"`)

* `31` (value: `"31"`)

* `32` (value: `"32"`)

* `33` (value: `"33"`)

* `34` (value: `"34"`)

* `35` (value: `"35"`)

* `39` (value: `"39"`)

* `40` (value: `"40"`)

* `44` (value: `"44"`)

* `45` (value: `"45"`)

* `49` (value: `"49"`)

* `50` (value: `"50"`)

* `51` (value: `"51"`)

* `53` (value: `"53"`)

* `54` (value: `"54"`)

* `55` (value: `"55"`)

* `56` (value: `"56"`)

* `58` (value: `"58"`)

* `59` (value: `"59"`)

* `60` (value: `"60"`)

* `61` (value: `"61"`)

* `66` (value: `"66"`)

* `69` (value: `"69"`)

* `70` (value: `"70"`)

* `74` (value: `"74"`)

* `75` (value: `"75"`)

* `76` (value: `"76"`)

* `78` (value: `"78"`)

* `85` (value: `"85"`)

* `87` (value: `"87"`)

* `89` (value: `"89"`)

* `90` (value: `"90"`)

* `91` (value: `"91"`)

* `94` (value: `"94"`)

* `95` (value: `"95"`)

* `96` (value: `"96"`)

* `97` (value: `"97"`)

* `100` (value: `"100"`)

* `101` (value: `"101"`)

* `102` (value: `"102"`)

* `103` (value: `"103"`)

* `104` (value: `"104"`)

* `105` (value: `"105"`)

* `106` (value: `"106"`)

* `107` (value: `"107"`)

* `108` (value: `"108"`)

* `109` (value: `"109"`)

* `110` (value: `"110"`)

* `111` (value: `"111"`)

* `112` (value: `"112"`)

* `114` (value: `"114"`)

* `115` (value: `"115"`)

* `116` (value: `"116"`)

* `117` (value: `"117"`)

* `118` (value: `"118"`)

* `119` (value: `"119"`)

* `121` (value: `"121"`)

* `122` (value: `"122"`)

* `125` (value: `"125"`)

* `128` (value: `"128"`)

* `129` (value: `"129"`)

* `130` (value: `"130"`)

* `131` (value: `"131"`)

* `132` (value: `"132"`)

* `133` (value: `"133"`)

* `134` (value: `"134"`)

* `135` (value: `"135"`)

* `136` (value: `"136"`)

* `137` (value: `"137"`)

* `138` (value: `"138"`)

* `139` (value: `"139"`)

* `140` (value: `"140"`)

* `142` (value: `"142"`)

* `143` (value: `"143"`)

* `144` (value: `"144"`)

* `146` (value: `"146"`)

* `147` (value: `"147"`)

* `148` (value: `"148"`)

* `149` (value: `"149"`)

* `150` (value: `"150"`)

* `151` (value: `"151"`)

* `152` (value: `"152"`)

* `153` (value: `"153"`)

* `154` (value: `"154"`)

* `155` (value: `"155"`)

* `157` (value: `"157"`)

* `158` (value: `"158"`)

* `159` (value: `"159"`)

* `160` (value: `"160"`)

* `161` (value: `"161"`)

* `162` (value: `"162"`)

* `163` (value: `"163"`)

* `164` (value: `"164"`)

* `165` (value: `"165"`)

* `166` (value: `"166"`)

* `167` (value: `"167"`)

* `168` (value: `"168"`)

* `169` (value: `"169"`)

* `170` (value: `"170"`)

* `171` (value: `"171"`)

* `172` (value: `"172"`)

* `173` (value: `"173"`)

* `174` (value: `"174"`)

* `175` (value: `"175"`)

* `176` (value: `"176"`)

* `177` (value: `"177"`)

* `178` (value: `"178"`)

* `179` (value: `"179"`)

* `180` (value: `"180"`)

* `181` (value: `"181"`)

* `182` (value: `"182"`)

* `183` (value: `"183"`)

* `184` (value: `"184"`)

* `185` (value: `"185"`)

* `186` (value: `"186"`)

* `187` (value: `"187"`)

* `188` (value: `"188"`)

* `189` (value: `"189"`)

* `190` (value: `"190"`)

* `191` (value: `"191"`)

* `192` (value: `"192"`)

* `193` (value: `"193"`)

* `194` (value: `"194"`)

* `195` (value: `"195"`)

* `197` (value: `"197"`)

* `198` (value: `"198"`)

* `199` (value: `"199"`)

* `200` (value: `"200"`)

* `201` (value: `"201"`)

* `202` (value: `"202"`)

* `203` (value: `"203"`)

* `204` (value: `"204"`)

* `205` (value: `"205"`)

* `206` (value: `"206"`)

* `207` (value: `"207"`)

* `208` (value: `"208"`)

* `209` (value: `"209"`)

* `210` (value: `"210"`)

* `211` (value: `"211"`)

* `212` (value: `"212"`)

* `213` (value: `"213"`)

* `214` (value: `"214"`)

* `215` (value: `"215"`)

* `216` (value: `"216"`)

* `217` (value: `"217"`)

* `218` (value: `"218"`)

* `219` (value: `"219"`)

* `220` (value: `"220"`)

* `221` (value: `"221"`)

* `222` (value: `"222"`)

* `223` (value: `"223"`)

* `224` (value: `"224"`)

* `225` (value: `"225"`)

* `226` (value: `"226"`)

* `227` (value: `"227"`)

* `228` (value: `"228"`)

* `229` (value: `"229"`)

* `230` (value: `"230"`)

* `231` (value: `"231"`)

* `232` (value: `"232"`)

* `233` (value: `"233"`)

* `234` (value: `"234"`)

* `235` (value: `"235"`)

* `236` (value: `"236"`)

* `237` (value: `"237"`)

* `238` (value: `"238"`)

* `239` (value: `"239"`)

* `240` (value: `"240"`)

* `241` (value: `"241"`)

* `242` (value: `"242"`)

* `243` (value: `"243"`)

* `244` (value: `"244"`)

* `245` (value: `"245"`)

* `246` (value: `"246"`)

* `247` (value: `"247"`)

* `248` (value: `"248"`)

* `249` (value: `"249"`)

* `250` (value: `"250"`)

* `251` (value: `"251"`)

* `252` (value: `"252"`)

* `253` (value: `"253"`)

* `254` (value: `"254"`)

* `256` (value: `"256"`)

* `257` (value: `"257"`)

* `258` (value: `"258"`)

* `259` (value: `"259"`)

* `260` (value: `"260"`)

* `261` (value: `"261"`)

* `262` (value: `"262"`)

* `263` (value: `"263"`)

* `264` (value: `"264"`)

* `265` (value: `"265"`)

* `266` (value: `"266"`)

* `267` (value: `"267"`)

* `268` (value: `"268"`)

* `269` (value: `"269"`)

* `270` (value: `"270"`)

* `271` (value: `"271"`)

* `272` (value: `"272"`)

* `273` (value: `"273"`)

* `274` (value: `"274"`)

* `275` (value: `"275"`)

* `276` (value: `"276"`)

* `277` (value: `"277"`)

* `287` (value: `"287"`)

* `288` (value: `"288"`)

* `A0` (value: `"A0"`)

* `A1` (value: `"A1"`)

* `A5` (value: `"A5"`)

* `A6` (value: `"A6"`)

* `A7` (value: `"A7"`)

* `A8` (value: `"A8"`)

* `B1` (value: `"B1"`)

* `B4` (value: `"B4"`)

* `B5` (value: `"B5"`)

* `B7` (value: `"B7"`)

* `B8` (value: `"B8"`)

* `B9` (value: `"B9"`)

* `B10` (value: `"B10"`)

* `B11` (value: `"B11"`)

* `B12` (value: `"B12"`)

* `B13` (value: `"B13"`)

* `B14` (value: `"B14"`)

* `B15` (value: `"B15"`)

* `B16` (value: `"B16"`)

* `B20` (value: `"B20"`)

* `B22` (value: `"B22"`)

* `B23` (value: `"B23"`)

* `P1` (value: `"P1"`)

* `P2` (value: `"P2"`)

* `P3` (value: `"P3"`)

* `P4` (value: `"P4"`)

* `P5` (value: `"P5"`)

* `P6` (value: `"P6"`)

* `P7` (value: `"P7"`)

* `P8` (value: `"P8"`)

* `P9` (value: `"P9"`)

* `P10` (value: `"P10"`)

* `P11` (value: `"P11"`)

* `P12` (value: `"P12"`)

* `P13` (value: `"P13"`)

* `P14` (value: `"P14"`)

* `P15` (value: `"P15"`)

* `P16` (value: `"P16"`)

* `P17` (value: `"P17"`)

* `P18` (value: `"P18"`)

* `P19` (value: `"P19"`)

* `P20` (value: `"P20"`)

* `P21` (value: `"P21"`)

* `P22` (value: `"P22"`)

* `P23` (value: `"P23"`)

* `W1` (value: `"W1"`)

* `W2` (value: `"W2"`)

* `W3` (value: `"W3"`)

* `W4` (value: `"W4"`)

* `Y1` (value: `"Y1"`)

* `Y2` (value: `"Y2"`)

* `Y3` (value: `"Y3"`)





## Enum: ClaimStatusEnum


* `empty` (value: `""`)

* `0` (value: `"0"`)

* `1` (value: `"1"`)

* `2` (value: `"2"`)

* `3` (value: `"3"`)

* `4` (value: `"4"`)

* `5` (value: `"5"`)

* `10` (value: `"10"`)

* `13` (value: `"13"`)

* `15` (value: `"15"`)

* `16` (value: `"16"`)

* `17` (value: `"17"`)

* `19` (value: `"19"`)

* `20` (value: `"20"`)

* `21` (value: `"21"`)

* `22` (value: `"22"`)

* `23` (value: `"23"`)

* `25` (value: `"25"`)

* `27` (value: `"27"`)




