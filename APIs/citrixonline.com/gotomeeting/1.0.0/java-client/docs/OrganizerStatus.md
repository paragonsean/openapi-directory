

# OrganizerStatus

Describes the status of an organizer, i.e. whether they are able to host meetings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**productType** | **Product** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the organizer can be set to. Use &#39;suspended&#39; to remove all products. The formerly used status &#39;active&#39; is now DEPRECATED for this call. To activate the organizer please assign a product. In this case do not pass this parameter |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUSPENDED | &quot;suspended&quot; |



