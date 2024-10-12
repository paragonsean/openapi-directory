

# WritableDeviceWithConfigContext


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**airflow** | [**AirflowEnum**](#AirflowEnum) |  |  [optional] |
|**assetTag** | **String** | A unique tag used to identify this device |  [optional] |
|**cluster** | **Integer** |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**configContext** | **Object** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**deviceRole** | **Integer** |  |  |
|**deviceType** | **Integer** |  |  |
|**display** | **String** |  |  [optional] [readonly] |
|**face** | [**FaceEnum**](#FaceEnum) |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**localContextData** | **Object** |  |  [optional] |
|**location** | **Integer** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**parentDevice** | [**NestedDevice**](NestedDevice.md) |  |  [optional] |
|**platform** | **Integer** |  |  [optional] |
|**position** | **BigDecimal** |  |  [optional] |
|**primaryIp** | **String** |  |  [optional] [readonly] |
|**primaryIp4** | **Integer** |  |  [optional] |
|**primaryIp6** | **Integer** |  |  [optional] |
|**rack** | **Integer** |  |  [optional] |
|**serial** | **String** |  |  [optional] |
|**site** | **Integer** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**vcPosition** | **Integer** |  |  [optional] |
|**vcPriority** | **Integer** |  |  [optional] |
|**virtualChassis** | **Integer** |  |  [optional] |



## Enum: AirflowEnum

| Name | Value |
|---- | -----|
| FRONT_TO_REAR | &quot;front-to-rear&quot; |
| REAR_TO_FRONT | &quot;rear-to-front&quot; |
| LEFT_TO_RIGHT | &quot;left-to-right&quot; |
| RIGHT_TO_LEFT | &quot;right-to-left&quot; |
| SIDE_TO_REAR | &quot;side-to-rear&quot; |
| PASSIVE | &quot;passive&quot; |
| MIXED | &quot;mixed&quot; |



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



