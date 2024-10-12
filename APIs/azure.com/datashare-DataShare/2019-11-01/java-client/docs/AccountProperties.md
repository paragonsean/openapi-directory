

# AccountProperties

Account property bag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Time at which the account was created. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the Account |  [optional] [readonly] |
|**userEmail** | **String** | Email of the user who created the resource |  [optional] [readonly] |
|**userName** | **String** | Name of the user who created the resource |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| MOVING | &quot;Moving&quot; |
| FAILED | &quot;Failed&quot; |



