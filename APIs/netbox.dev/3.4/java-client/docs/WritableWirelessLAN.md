

# WritableWirelessLAN


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authCipher** | [**AuthCipherEnum**](#AuthCipherEnum) |  |  [optional] |
|**authPsk** | **String** |  |  [optional] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**group** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**ssid** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**vlan** | **Integer** |  |  [optional] |



## Enum: AuthCipherEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| TKIP | &quot;tkip&quot; |
| AES | &quot;aes&quot; |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| WEP | &quot;wep&quot; |
| WPA_PERSONAL | &quot;wpa-personal&quot; |
| WPA_ENTERPRISE | &quot;wpa-enterprise&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| RESERVED | &quot;reserved&quot; |
| DISABLED | &quot;disabled&quot; |
| DEPRECATED | &quot;deprecated&quot; |



