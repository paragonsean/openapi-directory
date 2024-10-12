

# PreValidateEnableBackupResponse

Response contract for enable backup validation request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerName** | **String** | Specifies the product specific container name. E.g. iaasvmcontainer;iaasvmcontainer;rgname;vmname. This is required  for portal |  [optional] |
|**errorCode** | **String** | Response error code |  [optional] |
|**errorMessage** | **String** | Response error message |  [optional] |
|**protectedItemName** | **String** | Specifies the product specific ds name. E.g. vm;iaasvmcontainer;rgname;vmname. This is required for portal |  [optional] |
|**recommendation** | **String** | Recommended action for user |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Validation Status |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |



