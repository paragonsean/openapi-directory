

# ListContainerSasInput

The parameters to the list SAS request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiryTime** | **OffsetDateTime** | The SAS URL expiration time.  This must be less than 24 hours from the current time. |  [optional] |
|**permissions** | [**PermissionsEnum**](#PermissionsEnum) | The permissions to set on the SAS URL. |  [optional] |



## Enum: PermissionsEnum

| Name | Value |
|---- | -----|
| READ | &quot;Read&quot; |
| READ_WRITE | &quot;ReadWrite&quot; |
| READ_WRITE_DELETE | &quot;ReadWriteDelete&quot; |



