

# TrackingCategory


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the tracking category e.g. Department, Region (max length &#x3D; 100) |  [optional] |
|**option** | **String** | The option name of the tracking option e.g. East, West (max length &#x3D; 100) |  [optional] |
|**options** | [**List&lt;TrackingOption&gt;**](TrackingOption.md) | See Tracking Options |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of a tracking category |  [optional] |
|**trackingCategoryID** | **UUID** | The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 |  [optional] |
|**trackingOptionID** | **UUID** | The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |
| DELETED | &quot;DELETED&quot; |



