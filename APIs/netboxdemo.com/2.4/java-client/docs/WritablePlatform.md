

# WritablePlatform


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** |  |  [optional] [readonly] |
|**manufacturer** | **Integer** | Optionally limit this platform to devices of a certain manufacturer |  [optional] |
|**name** | **String** |  |  |
|**napalmArgs** | **String** | Additional arguments to pass when initiating the NAPALM driver (JSON format) |  [optional] |
|**napalmDriver** | **String** | The name of the NAPALM driver to use when interacting with devices |  [optional] |
|**rpcClient** | [**RpcClientEnum**](#RpcClientEnum) |  |  [optional] |
|**slug** | **String** |  |  |



## Enum: RpcClientEnum

| Name | Value |
|---- | -----|
| JUNIPER_JUNOS | &quot;juniper-junos&quot; |
| CISCO_IOS | &quot;cisco-ios&quot; |
| OPENGEAR | &quot;opengear&quot; |



