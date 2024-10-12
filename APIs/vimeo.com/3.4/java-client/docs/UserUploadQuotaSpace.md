

# UserUploadQuotaSpace

Information about the user's upload space remaining for the current period.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**free** | **BigDecimal** | The number of bytes remaining in your upload quota. |  |
|**max** | **BigDecimal** | The maximum number of bytes allotted to your upload quota. |  |
|**showing** | [**ShowingEnum**](#ShowingEnum) | Whether the values of the upload_quota.space fields are for the lifetime quota or the periodic quota. |  |
|**used** | **BigDecimal** | The number of bytes that you&#39;ve already uploaded against your quota. |  |



## Enum: ShowingEnum

| Name | Value |
|---- | -----|
| LIFETIME | &quot;lifetime&quot; |
| PERIODIC | &quot;periodic&quot; |



