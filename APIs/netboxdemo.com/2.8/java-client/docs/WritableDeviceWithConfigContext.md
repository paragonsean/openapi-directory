

# WritableDeviceWithConfigContext


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetTag** | **String** | A unique tag used to identify this device |  [optional] |
|**cluster** | **Integer** |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**configContext** | **Map&lt;String, String&gt;** |  |  [optional] [readonly] |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**deviceRole** | **Integer** |  |  |
|**deviceType** | **Integer** |  |  |
|**displayName** | **String** |  |  [optional] [readonly] |
|**face** | [**FaceEnum**](#FaceEnum) |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**localContextData** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**parentDevice** | [**NestedDevice**](NestedDevice.md) |  |  [optional] |
|**platform** | **Integer** |  |  [optional] |
|**position** | **Integer** | The lowest-numbered unit occupied by the device |  [optional] |
|**primaryIp** | **String** |  |  [optional] [readonly] |
|**primaryIp4** | **Integer** |  |  [optional] |
|**primaryIp6** | **Integer** |  |  [optional] |
|**rack** | **Integer** |  |  [optional] |
|**serial** | **String** |  |  [optional] |
|**site** | **Integer** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**vcPosition** | **Integer** |  |  [optional] |
|**vcPriority** | **Integer** |  |  [optional] |
|**virtualChassis** | **Integer** |  |  [optional] |



## Enum: FaceEnum

| Name | Value |
|---- | -----|
| FRONT | &quot;front&quot; |
| REAR | &quot;rear&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OFFLINE | &quot;offline&quot; |
| ACTIVE | &quot;active&quot; |
| PLANNED | &quot;planned&quot; |
| STAGED | &quot;staged&quot; |
| FAILED | &quot;failed&quot; |
| INVENTORY | &quot;inventory&quot; |
| DECOMMISSIONING | &quot;decommissioning&quot; |



