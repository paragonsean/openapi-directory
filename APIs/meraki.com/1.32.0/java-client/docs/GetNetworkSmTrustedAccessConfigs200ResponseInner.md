

# GetNetworkSmTrustedAccessConfigs200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessEndAt** | **OffsetDateTime** | time that access ends |  [optional] |
|**accessStartAt** | **OffsetDateTime** | time that access starts |  [optional] |
|**id** | **String** | device ID |  [optional] |
|**name** | **String** | device name |  [optional] |
|**scope** | **String** | scope |  [optional] |
|**ssidName** | **String** | SSID name |  [optional] |
|**tags** | **List&lt;String&gt;** | device tags |  [optional] |
|**timeboundType** | [**TimeboundTypeEnum**](#TimeboundTypeEnum) | type of access period, either a static range or a dynamic period |  [optional] |



## Enum: TimeboundTypeEnum

| Name | Value |
|---- | -----|
| DYNAMIC | &quot;dynamic&quot; |
| STATIC | &quot;static&quot; |



