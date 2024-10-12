

# UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication

APN authentication configurations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**password** | **String** | APN password, if type is set (if APN password is not supplied, the password is left unchanged). |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | APN auth type. |  [optional] |
|**username** | **String** | APN username, if type is set. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CHAP | &quot;chap&quot; |
| NONE | &quot;none&quot; |
| PAP | &quot;pap&quot; |



