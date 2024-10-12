

# Group

Groups represent organizations using Increase. You can retrieve information about your own organization via the API, or (more commonly) OAuth platforms can retrieve information about the organizations that have granted them access.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**achDebitStatus** | [**AchDebitStatusEnum**](#AchDebitStatusEnum) | If the Group is allowed to create ACH debits. |  |
|**activationStatus** | [**ActivationStatusEnum**](#ActivationStatusEnum) | If the Group is activated or not. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Group was created. |  |
|**id** | **String** | The Group identifier. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;group&#x60;. |  |



## Enum: AchDebitStatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;disabled&quot; |
| ENABLED | &quot;enabled&quot; |



## Enum: ActivationStatusEnum

| Name | Value |
|---- | -----|
| UNACTIVATED | &quot;unactivated&quot; |
| ACTIVATED | &quot;activated&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GROUP | &quot;group&quot; |



