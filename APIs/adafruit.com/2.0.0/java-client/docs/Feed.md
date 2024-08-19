

# Feed


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**details** | [**FeedDetails**](FeedDetails.md) |  |  [optional] |
|**enabled** | **Boolean** |  |  [optional] [readonly] |
|**group** | [**Map&lt;String, ShallowGroup&gt;**](ShallowGroup.md) |  |  [optional] [readonly] |
|**groups** | [**List&lt;ShallowGroup&gt;**](ShallowGroup.md) |  |  [optional] [readonly] |
|**history** | **Boolean** |  |  [optional] |
|**id** | **BigDecimal** |  |  [optional] [readonly] |
|**key** | **String** |  |  [optional] |
|**lastValue** | **String** |  |  [optional] [readonly] |
|**license** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**status** | **String** |  |  [optional] [readonly] |
|**statusNotify** | **Boolean** | Is status notification active? |  [optional] |
|**statusTimeout** | **Integer** | Status notification timeout in minutes. |  [optional] |
|**unitSymbol** | **String** |  |  [optional] |
|**unitType** | **String** |  |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) |  |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| PRIVATE | &quot;private&quot; |
| PUBLIC | &quot;public&quot; |



