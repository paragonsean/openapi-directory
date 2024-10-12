

# CreateDeviceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**pushProvider** | [**PushProviderEnum**](#PushProviderEnum) |  |  [optional] |
|**pushProviderName** | **String** |  |  [optional] |
|**user** | **UserObjectRequest** |  |  [optional] |
|**userId** | **String** | **Server-side only**. User ID which server acts upon |  [optional] |



## Enum: PushProviderEnum

| Name | Value |
|---- | -----|
| FIREBASE | &quot;firebase&quot; |
| APN | &quot;apn&quot; |
| HUAWEI | &quot;huawei&quot; |
| XIAOMI | &quot;xiaomi&quot; |



