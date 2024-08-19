

# NHArtwork


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artName** | **String** | The name of the real-life analog to the artwork. |  [optional] |
|**artStyle** | **String** | The art style of the artwork. |  [optional] |
|**artType** | [**ArtTypeEnum**](#ArtTypeEnum) | The type of artwork (either a painting or statue). |  [optional] |
|**author** | **String** | The author of the real-life analog to the artwork. |  [optional] |
|**availability** | **String** | The availability of the artwork. |  [optional] |
|**buy** | **Integer** | The number of Bells the artwork may be purchased for. |  [optional] |
|**fakeInfo** | [**NHArtworkFakeInfo**](NHArtworkFakeInfo.md) |  |  [optional] |
|**hasFake** | **Boolean** | Whether the artwork has a fake or not. |  [optional] |
|**length** | **Float** | The length of the artwork. |  [optional] |
|**name** | **String** | Name of the artwork. |  [optional] |
|**realInfo** | [**NHArtworkRealInfo**](NHArtworkRealInfo.md) |  |  [optional] |
|**sell** | **Integer** | The number of Bells the artwork can be sold to Nook&#39;s store for, when it is genuine. |  [optional] |
|**url** | **String** | Link to the respective Nookipedia article. |  [optional] |
|**width** | **Float** | The width of the artwork. |  [optional] |
|**year** | **String** | The year that the real-life analog was made. May be an exact year, an estimate (\&quot;circa\&quot;), or a range. |  [optional] |



## Enum: ArtTypeEnum

| Name | Value |
|---- | -----|
| PAINTING | &quot;Painting&quot; |
| STATUE | &quot;Statue&quot; |



