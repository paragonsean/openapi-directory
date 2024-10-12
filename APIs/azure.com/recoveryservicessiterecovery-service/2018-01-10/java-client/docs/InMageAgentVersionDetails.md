

# InMageAgentVersionDetails

InMage agent version details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiryDate** | **OffsetDateTime** | Version expiry date. |  [optional] |
|**postUpdateRebootStatus** | **String** | A value indicating whether reboot is required after update is applied. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A value indicating whether security update required. |  [optional] |
|**version** | **String** | The agent version. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUPPORTED | &quot;Supported&quot; |
| NOT_SUPPORTED | &quot;NotSupported&quot; |
| DEPRECATED | &quot;Deprecated&quot; |
| UPDATE_REQUIRED | &quot;UpdateRequired&quot; |
| SECURITY_UPDATE_REQUIRED | &quot;SecurityUpdateRequired&quot; |



