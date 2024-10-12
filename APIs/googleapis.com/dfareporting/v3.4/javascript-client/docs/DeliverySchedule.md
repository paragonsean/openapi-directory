# CampaignManager360Api.DeliverySchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequencyCap** | [**FrequencyCap**](FrequencyCap.md) |  | [optional] 
**hardCutoff** | **Boolean** | Whether or not hard cutoff is enabled. If true, the ad will not serve after the end date and time. Otherwise the ad will continue to be served until it has reached its delivery goals. | [optional] 
**impressionRatio** | **String** | Impression ratio for this ad. This ratio determines how often each ad is served relative to the others. For example, if ad A has an impression ratio of 1 and ad B has an impression ratio of 3, then Campaign Manager will serve ad B three times as often as ad A. Acceptable values are 1 to 10, inclusive. | [optional] 
**priority** | **String** | Serving priority of an ad, with respect to other ads. The lower the priority number, the greater the priority with which it is served. | [optional] 



## Enum: PriorityEnum


* `01` (value: `"AD_PRIORITY_01"`)

* `02` (value: `"AD_PRIORITY_02"`)

* `03` (value: `"AD_PRIORITY_03"`)

* `04` (value: `"AD_PRIORITY_04"`)

* `05` (value: `"AD_PRIORITY_05"`)

* `06` (value: `"AD_PRIORITY_06"`)

* `07` (value: `"AD_PRIORITY_07"`)

* `08` (value: `"AD_PRIORITY_08"`)

* `09` (value: `"AD_PRIORITY_09"`)

* `10` (value: `"AD_PRIORITY_10"`)

* `11` (value: `"AD_PRIORITY_11"`)

* `12` (value: `"AD_PRIORITY_12"`)

* `13` (value: `"AD_PRIORITY_13"`)

* `14` (value: `"AD_PRIORITY_14"`)

* `15` (value: `"AD_PRIORITY_15"`)

* `16` (value: `"AD_PRIORITY_16"`)




