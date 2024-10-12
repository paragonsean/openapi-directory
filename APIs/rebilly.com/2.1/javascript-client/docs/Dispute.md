# RebillyRestApi.Dispute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**[DisputeEmbeddedInner]**](DisputeEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[DisputeLinksInner]**](DisputeLinksInner.md) | The links related to resource. | [optional] [readonly] 
**acquirerReferenceNumber** | **String** | The dispute&#39;s acquirer reference number. | [optional] 
**amount** | **Number** | The dispute amount. | 
**caseId** | **String** | The case ID for the dispute. | [optional] 
**category** | **String** | The dispute&#39;s category. | [optional] [readonly] 
**createdTime** | **Date** | Dispute created time. | [optional] [readonly] 
**currency** | **String** | ISO 4217 alphabetic currency code. | 
**customerId** | **String** | The dispute&#39;s customer ID. | [optional] [readonly] 
**deadlineTime** | **Date** | Dispute deadline time. | [optional] 
**id** | **String** | The dispute identifier string. | [optional] [readonly] 
**postedTime** | **Date** | Dispute posted time. | 
**rawResponse** | **String** | Dispute raw response from gateway. | [optional] [readonly] 
**reasonCode** | **String** | The dispute&#39;s reason code. | 
**resolvedTime** | **Date** | Dispute resolved time. | [optional] [readonly] 
**status** | **String** | The dispute&#39;s status. | 
**transactionId** | **String** | The dispute&#39;s transaction ID. | 
**type** | **String** | The dispute&#39;s type. | 
**updatedTime** | **Date** | Dispute updated time. | [optional] [readonly] 



## Enum: CategoryEnum


* `fraud` (value: `"fraud"`)

* `unrecognized` (value: `"unrecognized"`)

* `product-not-received` (value: `"product-not-received"`)

* `product-unacceptable` (value: `"product-unacceptable"`)

* `product-not-refunded` (value: `"product-not-refunded"`)

* `duplicate` (value: `"duplicate"`)

* `subscription-canceled` (value: `"subscription-canceled"`)

* `uncategorized` (value: `"uncategorized"`)





## Enum: ReasonCodeEnum


* `1000` (value: `"1000"`)

* `10.1` (value: `"10.1"`)

* `10.2` (value: `"10.2"`)

* `10.3` (value: `"10.3"`)

* `10.4` (value: `"10.4"`)

* `10.5` (value: `"10.5"`)

* `11.1` (value: `"11.1"`)

* `11.2` (value: `"11.2"`)

* `11.3` (value: `"11.3"`)

* `12` (value: `"12"`)

* `12.1` (value: `"12.1"`)

* `12.2` (value: `"12.2"`)

* `12.3` (value: `"12.3"`)

* `12.4` (value: `"12.4"`)

* `12.5` (value: `"12.5"`)

* `12.6` (value: `"12.6"`)

* `12.7` (value: `"12.7"`)

* `13.1` (value: `"13.1"`)

* `13.2` (value: `"13.2"`)

* `13.3` (value: `"13.3"`)

* `13.4` (value: `"13.4"`)

* `13.5` (value: `"13.5"`)

* `13.6` (value: `"13.6"`)

* `13.7` (value: `"13.7"`)

* `13.8` (value: `"13.8"`)

* `13.9` (value: `"13.9"`)

* `2` (value: `"2"`)

* `30` (value: `"30"`)

* `31` (value: `"31"`)

* `35` (value: `"35"`)

* `37` (value: `"37"`)

* `40` (value: `"40"`)

* `41` (value: `"41"`)

* `42` (value: `"42"`)

* `46` (value: `"46"`)

* `47` (value: `"47"`)

* `49` (value: `"49"`)

* `50` (value: `"50"`)

* `53` (value: `"53"`)

* `54` (value: `"54"`)

* `55` (value: `"55"`)

* `57` (value: `"57"`)

* `59` (value: `"59"`)

* `60` (value: `"60"`)

* `62` (value: `"62"`)

* `7` (value: `"7"`)

* `70` (value: `"70"`)

* `71` (value: `"71"`)

* `722` (value: `"72"`)

* `73` (value: `"73"`)

* `74` (value: `"74"`)

* `75` (value: `"75"`)

* `76` (value: `"76"`)

* `77` (value: `"77"`)

* `79` (value: `"79"`)

* `8` (value: `"8"`)

* `80` (value: `"80"`)

* `81` (value: `"81"`)

* `82` (value: `"82"`)

* `83` (value: `"83"`)

* `85` (value: `"85"`)

* `86` (value: `"86"`)

* `93` (value: `"93"`)

* `00` (value: `"00"`)

* `63` (value: `"63"`)

* `A01` (value: `"A01"`)

* `A02` (value: `"A02"`)

* `A08` (value: `"A08"`)

* `F10` (value: `"F10"`)

* `F14` (value: `"F14"`)

* `F22` (value: `"F22"`)

* `F24` (value: `"F24"`)

* `F29` (value: `"F29"`)

* `C02` (value: `"C02"`)

* `C04` (value: `"C04"`)

* `C05` (value: `"C05"`)

* `C08` (value: `"C08"`)

* `C14` (value: `"C14"`)

* `C18` (value: `"C18"`)

* `C28` (value: `"C28"`)

* `C31` (value: `"C31"`)

* `C32` (value: `"C32"`)

* `M10` (value: `"M10"`)

* `M49` (value: `"M49"`)

* `P01` (value: `"P01"`)

* `P03` (value: `"P03"`)

* `P04` (value: `"P04"`)

* `P05` (value: `"P05"`)

* `P07` (value: `"P07"`)

* `P08` (value: `"P08"`)

* `P22` (value: `"P22"`)

* `P23` (value: `"P23"`)

* `R03` (value: `"R03"`)

* `R13` (value: `"R13"`)

* `M01` (value: `"M01"`)

* `FR1` (value: `"FR1"`)

* `FR4` (value: `"FR4"`)

* `FR6` (value: `"FR6"`)

* `AL` (value: `"AL"`)

* `AP` (value: `"AP"`)

* `AW` (value: `"AW"`)

* `CA` (value: `"CA"`)

* `CD` (value: `"CD"`)

* `CR` (value: `"CR"`)

* `DA` (value: `"DA"`)

* `DP` (value: `"DP"`)

* `DP1` (value: `"DP1"`)

* `EX` (value: `"EX"`)

* `IC` (value: `"IC"`)

* `IN` (value: `"IN"`)

* `IS` (value: `"IS"`)

* `LP` (value: `"LP"`)

* `N` (value: `"N"`)

* `NA` (value: `"NA"`)

* `NC` (value: `"NC"`)

* `P` (value: `"P"`)

* `RG` (value: `"RG"`)

* `RM` (value: `"RM"`)

* `RN1` (value: `"RN1"`)

* `RN2` (value: `"RN2"`)

* `SV` (value: `"SV"`)

* `TF` (value: `"TF"`)

* `TNM` (value: `"TNM"`)

* `UA01` (value: `"UA01"`)

* `UA02` (value: `"UA02"`)

* `UA32` (value: `"UA32"`)

* `UA99` (value: `"UA99"`)

* `UA03` (value: `"UA03"`)

* `UA10` (value: `"UA10"`)

* `UA11` (value: `"UA11"`)

* `UA12` (value: `"UA12"`)

* `UA18` (value: `"UA18"`)

* `UA20` (value: `"UA20"`)

* `UA21` (value: `"UA21"`)

* `UA22` (value: `"UA22"`)

* `UA23` (value: `"UA23"`)

* `UA28` (value: `"UA28"`)

* `UA30` (value: `"UA30"`)

* `UA31` (value: `"UA31"`)

* `UA38` (value: `"UA38"`)

* `duplicate` (value: `"duplicate"`)

* `fraudulent` (value: `"fraudulent"`)

* `subscription_canceled` (value: `"subscription_canceled"`)

* `product_unacceptable` (value: `"product_unacceptable"`)

* `product_not_received` (value: `"product_not_received"`)

* `unrecognized` (value: `"unrecognized"`)

* `credit_not_processed` (value: `"credit_not_processed"`)

* `customer_initiated` (value: `"customer_initiated"`)

* `incorrect_account_details` (value: `"incorrect_account_details"`)

* `insufficient_funds` (value: `"insufficient_funds"`)

* `bank_cannot_process` (value: `"bank_cannot_process"`)

* `debit_not_authorized` (value: `"debit_not_authorized"`)

* `general` (value: `"general"`)

* `pre-chargeback-alert` (value: `"pre-chargeback-alert"`)

* `0` (value: `"0"`)

* `1` (value: `"1"`)

* `22` (value: `"2"`)

* `3` (value: `"3"`)

* `4` (value: `"4"`)

* `5` (value: `"5"`)

* `6` (value: `"6"`)

* `72` (value: `"7"`)

* `9` (value: `"9"`)

* `51` (value: `"51"`)

* `A` (value: `"A"`)

* `B` (value: `"B"`)





## Enum: StatusEnum


* `response-needed` (value: `"response-needed"`)

* `under-review` (value: `"under-review"`)

* `forfeited` (value: `"forfeited"`)

* `won` (value: `"won"`)

* `lost` (value: `"lost"`)

* `unknown` (value: `"unknown"`)





## Enum: TypeEnum


* `information-request` (value: `"information-request"`)

* `first-chargeback` (value: `"first-chargeback"`)

* `second-chargeback` (value: `"second-chargeback"`)

* `arbitration` (value: `"arbitration"`)

* `fraud` (value: `"fraud"`)

* `ethoca-alert` (value: `"ethoca-alert"`)

* `verifi-alert` (value: `"verifi-alert"`)




