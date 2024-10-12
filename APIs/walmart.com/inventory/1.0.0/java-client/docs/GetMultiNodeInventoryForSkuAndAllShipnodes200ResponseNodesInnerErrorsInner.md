

# GetMultiNodeInventoryForSkuAndAllShipnodes200ResponseNodesInnerErrorsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) |  |  [optional] |
|**causes** | [**List&lt;GetMultiNodeInventoryForSkuAndAllShipnodes200ResponseNodesInnerErrorsInnerCausesInner&gt;**](GetMultiNodeInventoryForSkuAndAllShipnodes200ResponseNodesInnerErrorsInnerCausesInner.md) |  |  [optional] |
|**code** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**errorIdentifiers** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**field** | **String** |  |  [optional] |
|**info** | **String** |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| APPLICATION | &quot;APPLICATION&quot; |
| SYSTEM | &quot;SYSTEM&quot; |
| REQUEST | &quot;REQUEST&quot; |
| DATA | &quot;DATA&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFO | &quot;INFO&quot; |
| WARN | &quot;WARN&quot; |
| ERROR | &quot;ERROR&quot; |



