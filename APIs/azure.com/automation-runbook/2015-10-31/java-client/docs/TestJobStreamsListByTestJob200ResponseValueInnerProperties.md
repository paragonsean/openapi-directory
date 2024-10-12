

# TestJobStreamsListByTestJob200ResponseValueInnerProperties

Definition of the job stream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobStreamId** | **String** | Gets or sets the id of the job stream. |  [optional] |
|**streamText** | **String** | Gets or sets the stream text. |  [optional] |
|**streamType** | [**StreamTypeEnum**](#StreamTypeEnum) | Gets or sets the stream type. |  [optional] |
|**summary** | **String** | Gets or sets the summary. |  [optional] |
|**time** | **OffsetDateTime** | Gets or sets the creation time of the job. |  [optional] |
|**value** | **Map&lt;String, Object&gt;** | Gets or sets the values of the job stream. |  [optional] |



## Enum: StreamTypeEnum

| Name | Value |
|---- | -----|
| PROGRESS | &quot;Progress&quot; |
| OUTPUT | &quot;Output&quot; |
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |
| DEBUG | &quot;Debug&quot; |
| VERBOSE | &quot;Verbose&quot; |
| ANY | &quot;Any&quot; |



