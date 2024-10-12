

# CollectionAnalyticData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configId** | **String** | Unique configuration identifier. Usually 36 alphanumeric characters |  |
|**entities** | [**List&lt;Entity&gt;**](Entity.md) | Returns the named entities and user defined entities from the text |  |
|**facets** | [**List&lt;Facet&gt;**](Facet.md) | Returns the facets extracted across all documents in the collection |  |
|**id** | **String** | Unique collection identifier. Can be up to 36 alphanumeric characters |  |
|**jobId** | **String** | Specific marker of a job collection belongs to, can be used for collections ordering on client side. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the collection |  |
|**tag** | **String** | Any text of up to 50 characters used like marker |  |
|**taxonomy** | [**List&lt;Topic&gt;**](Topic.md) | Returns the taxonomy determined for the text |  |
|**themes** | [**List&lt;Theme&gt;**](Theme.md) | Returns themes across the documents |  |
|**topics** | [**List&lt;Topic&gt;**](Topic.md) | Returns the concept and query defined topics determined for the text |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| PROCESSED | &quot;processed&quot; |
| FAILED | &quot;failed&quot; |



