

# DeliverySchedule

Delivery Schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frequencyCap** | [**FrequencyCap**](FrequencyCap.md) |  |  [optional] |
|**hardCutoff** | **Boolean** | Whether or not hard cutoff is enabled. If true, the ad will not serve after the end date and time. Otherwise the ad will continue to be served until it has reached its delivery goals. |  [optional] |
|**impressionRatio** | **String** | Impression ratio for this ad. This ratio determines how often each ad is served relative to the others. For example, if ad A has an impression ratio of 1 and ad B has an impression ratio of 3, then Campaign Manager will serve ad B three times as often as ad A. Acceptable values are 1 to 10, inclusive. |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) | Serving priority of an ad, with respect to other ads. The lower the priority number, the greater the priority with which it is served. |  [optional] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| _01 | &quot;AD_PRIORITY_01&quot; |
| _02 | &quot;AD_PRIORITY_02&quot; |
| _03 | &quot;AD_PRIORITY_03&quot; |
| _04 | &quot;AD_PRIORITY_04&quot; |
| _05 | &quot;AD_PRIORITY_05&quot; |
| _06 | &quot;AD_PRIORITY_06&quot; |
| _07 | &quot;AD_PRIORITY_07&quot; |
| _08 | &quot;AD_PRIORITY_08&quot; |
| _09 | &quot;AD_PRIORITY_09&quot; |
| _10 | &quot;AD_PRIORITY_10&quot; |
| _11 | &quot;AD_PRIORITY_11&quot; |
| _12 | &quot;AD_PRIORITY_12&quot; |
| _13 | &quot;AD_PRIORITY_13&quot; |
| _14 | &quot;AD_PRIORITY_14&quot; |
| _15 | &quot;AD_PRIORITY_15&quot; |
| _16 | &quot;AD_PRIORITY_16&quot; |



