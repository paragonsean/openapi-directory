

# WritableDevice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetTag** | **String** | A unique tag used to identify this device |  [optional] |
|**cluster** | **Integer** |  |  [optional] |
|**comments** | **String** |  |  [optional] |
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
|**parentDevice** | **String** |  |  [optional] [readonly] |
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
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_0 | 0 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |



