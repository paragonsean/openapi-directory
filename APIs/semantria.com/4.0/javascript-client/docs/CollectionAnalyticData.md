# Semantria.CollectionAnalyticData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configId** | **String** | Unique configuration identifier. Usually 36 alphanumeric characters | 
**entities** | [**[Entity]**](Entity.md) | Returns the named entities and user defined entities from the text | 
**facets** | [**[Facet]**](Facet.md) | Returns the facets extracted across all documents in the collection | 
**id** | **String** | Unique collection identifier. Can be up to 36 alphanumeric characters | 
**jobId** | **String** | Specific marker of a job collection belongs to, can be used for collections ordering on client side. | 
**status** | **String** | Status of the collection | 
**tag** | **String** | Any text of up to 50 characters used like marker | 
**taxonomy** | [**[Topic]**](Topic.md) | Returns the taxonomy determined for the text | 
**themes** | [**[Theme]**](Theme.md) | Returns themes across the documents | 
**topics** | [**[Topic]**](Topic.md) | Returns the concept and query defined topics determined for the text | 



## Enum: StatusEnum


* `queued` (value: `"queued"`)

* `processed` (value: `"processed"`)

* `failed` (value: `"failed"`)




