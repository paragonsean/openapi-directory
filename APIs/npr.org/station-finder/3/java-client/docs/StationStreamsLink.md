

# StationStreamsLink

A link to an audio stream related to the station

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**href** | **URI** | The link to be followed |  |
|**guid** | **String** | The system&#39;s internal unique identifier for a link, not typically used by consumers |  [optional] |
|**title** | **String** | The link text, provided by the station, for the URL |  [optional] |
|**typeName** | **String** | The semantic name corresponding to the &#x60;typeId&#x60; |  |
|**isPrimaryStream** | **Boolean** | Whether or not this stream is considered the station&#39;s primary stream |  [optional] |
|**typeId** | [**TypeIdEnum**](#TypeIdEnum) | An identifier for the type of stream |  |



## Enum: TypeIdEnum

| Name | Value |
|---- | -----|
| _10 | &quot;10&quot; |
| _11 | &quot;11&quot; |
| _12 | &quot;12&quot; |
| _13 | &quot;13&quot; |



