

# InboundNatPool


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendPort** | **Integer** | This must be unique within a Batch pool. Acceptable values are between 1 and 65535 except for 22, 3389, 29876 and 29877 as these are reserved. If any reserved values are provided the request fails with HTTP status code 400. |  |
|**frontendPortRangeEnd** | **Integer** | Acceptable values range between 1 and 65534 except ports from 50000 to 55000 which are reserved by the Batch service. All ranges within a pool must be distinct and cannot overlap. If any reserved or overlapping values are provided the request fails with HTTP status code 400. |  |
|**frontendPortRangeStart** | **Integer** | Acceptable values range between 1 and 65534 except ports from 50000 to 55000 which are reserved. All ranges within a pool must be distinct and cannot overlap. If any reserved or overlapping values are provided the request fails with HTTP status code 400. |  |
|**name** | **String** | The name must be unique within a Batch pool, can contain letters, numbers, underscores, periods, and hyphens. Names must start with a letter or number, must end with a letter, number, or underscore, and cannot exceed 77 characters.  If any invalid values are provided the request fails with HTTP status code 400. |  |
|**networkSecurityGroupRules** | [**List&lt;NetworkSecurityGroupRule&gt;**](NetworkSecurityGroupRule.md) | The maximum number of rules that can be specified across all the endpoints on a Batch pool is 25. If no network security group rules are specified, a default rule will be created to allow inbound access to the specified backendPort. If the maximum number of network security group rules is exceeded the request fails with HTTP status code 400. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) |  |  |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;TCP&quot; |
| UDP | &quot;UDP&quot; |



