

# MediaGraphProperties

Class for Media Graph properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | Date the Media Graph was created |  [optional] [readonly] |
|**description** | **String** | Media Graph  description |  [optional] |
|**lastModified** | **OffsetDateTime** | Date the Media Graph was last modified |  [optional] [readonly] |
|**sinks** | [**List&lt;MediaGraphSink&gt;**](MediaGraphSink.md) | Media Graph sinks |  |
|**sources** | [**List&lt;MediaGraphSource&gt;**](MediaGraphSource.md) | Media Graph sources |  |
|**state** | [**StateEnum**](#StateEnum) | Media Graph state |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| STARTING | &quot;Starting&quot; |
| STOPPED | &quot;Stopped&quot; |
| STOPPING | &quot;Stopping&quot; |



