

# OriginProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostName** | **String** | The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported. |  |
|**httpPort** | **Integer** | The value of the HTTP port. Must be between 1 and 65535. |  [optional] |
|**httpsPort** | **Integer** | The value of the https port. Must be between 1 and 65535. |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**resourceState** | [**ResourceStateEnum**](#ResourceStateEnum) | Resource status of the origin. |  [optional] [readonly] |



## Enum: ResourceStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| ACTIVE | &quot;Active&quot; |
| DELETING | &quot;Deleting&quot; |



