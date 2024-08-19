

# TrackingOption


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the tracking option e.g. Marketing, East (max length &#x3D; 100) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of a tracking option |  [optional] |
|**trackingCategoryID** | **UUID** | Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 |  [optional] |
|**trackingOptionID** | **UUID** | The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |
| DELETED | &quot;DELETED&quot; |



