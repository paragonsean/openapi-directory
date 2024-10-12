

# GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface

Logical interface.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Interface name. This is not a globally unique identifier. Name is unique only inside the ServerNetworkTemplate. This is of syntax or and forms part of the network template name. |  [optional] |
|**required** | **Boolean** | If true, interface must have network connected. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Interface type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INTERFACE_TYPE_UNSPECIFIED | &quot;INTERFACE_TYPE_UNSPECIFIED&quot; |
| BOND | &quot;BOND&quot; |
| NIC | &quot;NIC&quot; |



