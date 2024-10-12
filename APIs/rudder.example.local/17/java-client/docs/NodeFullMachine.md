

# NodeFullMachine

Information about the underlying machine

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Rudder unique identifier for the machine |  [optional] |
|**manufacturer** | **String** | Information about machine manufacturer |  [optional] |
|**provider** | **String** | In the case of VM, the VM technology |  [optional] |
|**serialNumber** | **String** | If available, a unique identifier provided by the machine |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the machine |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PHYSICAL | &quot;Physical&quot; |
| VIRTUAL | &quot;Virtual&quot; |



