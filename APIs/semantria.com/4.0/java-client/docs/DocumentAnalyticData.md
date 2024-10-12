

# DocumentAnalyticData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoCategories** | [**List&lt;AutoCategory&gt;**](AutoCategory.md) | Auto-generated categories applicable for the document |  |
|**configId** | **String** | Unique configuration identifier. Usually 36 alphanumeric characters |  |
|**details** | [**List&lt;Details&gt;**](Details.md) | Returns sentences from the original document with POS tags within |  |
|**entities** | [**List&lt;Entity&gt;**](Entity.md) | Returns the named entities and user defined entities from the text |  |
|**id** | **String** | Unique document identifier. Can be up to 36 alphanumeric characters |  |
|**intentions** | [**List&lt;Intention&gt;**](Intention.md) | Returns intentions list detected by the engine |  |
|**jobId** | **String** | Specific marker of a job document belongs to, can be used for documents ordering on client side |  |
|**language** | **String** | Determined language of source text |  |
|**languageScore** | **Double** | The percentage score of the best match of language among detected languages |  |
|**modelSentiment** | [**ModelSentiment**](ModelSentiment.md) |  |  |
|**opinions** | [**List&lt;Opinion&gt;**](Opinion.md) | Returns the list of opinions extracted from the source text |  |
|**phrases** | [**List&lt;Phrase&gt;**](Phrase.md) | Returns sentiment-bearing phrases of the document |  |
|**relations** | [**List&lt;Relation&gt;**](Relation.md) | Returns relations which represent a connection between one or more Entity objects |  |
|**sentimentPolarity** | [**SentimentPolarityEnum**](#SentimentPolarityEnum) | Verbal representation of sentiment score. Can be \&quot;negative\&quot;, \&quot;positive\&quot; or \&quot;neutral\&quot; |  |
|**sentimentScore** | **Double** | A sentiment analysis of the document text |  |
|**sourceText** | **String** | Original source text passed by client for this document |  |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the document |  |
|**summary** | **String** | A summary of the document text |  |
|**taxonomy** | [**List&lt;Topic&gt;**](Topic.md) | Returns the taxonomy determined for the text |  |
|**themes** | [**List&lt;Theme&gt;**](Theme.md) | Returns themes of the document |  |
|**topics** | [**List&lt;Topic&gt;**](Topic.md) | Returns the concept and query defined topics determined for the text |  |



## Enum: SentimentPolarityEnum

| Name | Value |
|---- | -----|
| NEGATIVE | &quot;negative&quot; |
| POSITIVE | &quot;positive&quot; |
| NEUTRAL | &quot;neutral&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| PROCESSED | &quot;processed&quot; |
| FAILED | &quot;failed&quot; |



