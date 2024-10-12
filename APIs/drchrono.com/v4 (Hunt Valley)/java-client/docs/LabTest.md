

# LabTest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** |  |  [optional] |
|**collectionDate** | **String** | The date the specimen were collected |  [optional] |
|**description** | **String** | Short description of the ICD-10 code |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**internalNotes** | **String** | Notes which are meant for, and read by, the labs |  [optional] |
|**labOrder** | **Integer** | ID of associated lab order |  |
|**name** | **String** | Name for the test |  [optional] |
|**reportNotes** | **String** | Notes which are not meant for labs, but are copied on the results. |  [optional] |
|**specimenCondition** | **String** |  |  [optional] |
|**specimenSource** | **String** |  |  [optional] |
|**specimenTotalVolume** | **BigDecimal** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | One of &#x60;\&quot;preliminary\&quot;&#x60;, &#x60;\&quot;pending\&quot;&#x60;, &#x60;\&quot;correction\&quot;&#x60;, &#x60;\&quot;final\&quot;&#x60; or &#x60;\&quot;canceled\&quot;&#x60;. Defaults to &#x60;\&quot;preliminary\&quot;&#x60; |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| P | &quot;P&quot; |
| I | &quot;I&quot; |
| C | &quot;C&quot; |
| F | &quot;F&quot; |
| X | &quot;X&quot; |



