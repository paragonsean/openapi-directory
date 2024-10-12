

# ScoutingObservationAttachment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | **String** | The content type of the attachment, e.g. image/png. |  |
|**id** | **UUID** | id of the attachment |  |
|**length** | **Long** | The number of bytes in the attachment. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the attachment. For example : ACTIVE, DELETED |  |
|**updatedAt** | **OffsetDateTime** | The time the attachment was last updated. Time in ISO 8601 format with UTC timezone, 3 fractional seconds. (https://tools.ietf.org/html/rfc3339)  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| DELETED | &quot;DELETED&quot; |



