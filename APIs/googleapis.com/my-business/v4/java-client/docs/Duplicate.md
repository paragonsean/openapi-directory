

# Duplicate

Information about the location that this location duplicates.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Indicates whether the user has access to the location it duplicates. |  [optional] |
|**locationName** | **String** | The resource name of the location that this duplicates. Only populated if the authenticated user has access rights to that location and that location is not deleted. |  [optional] |
|**placeId** | **String** | The place ID of the location that this duplicates. |  [optional] |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| ACCESS_UNSPECIFIED | &quot;ACCESS_UNSPECIFIED&quot; |
| ACCESS_UNKNOWN | &quot;ACCESS_UNKNOWN&quot; |
| ALLOWED | &quot;ALLOWED&quot; |
| INSUFFICIENT | &quot;INSUFFICIENT&quot; |



