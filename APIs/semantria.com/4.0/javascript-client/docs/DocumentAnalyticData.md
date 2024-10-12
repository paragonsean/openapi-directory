# Semantria.DocumentAnalyticData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoCategories** | [**[AutoCategory]**](AutoCategory.md) | Auto-generated categories applicable for the document | 
**configId** | **String** | Unique configuration identifier. Usually 36 alphanumeric characters | 
**details** | [**[Details]**](Details.md) | Returns sentences from the original document with POS tags within | 
**entities** | [**[Entity]**](Entity.md) | Returns the named entities and user defined entities from the text | 
**id** | **String** | Unique document identifier. Can be up to 36 alphanumeric characters | 
**intentions** | [**[Intention]**](Intention.md) | Returns intentions list detected by the engine | 
**jobId** | **String** | Specific marker of a job document belongs to, can be used for documents ordering on client side | 
**language** | **String** | Determined language of source text | 
**languageScore** | **Number** | The percentage score of the best match of language among detected languages | 
**modelSentiment** | [**ModelSentiment**](ModelSentiment.md) |  | 
**opinions** | [**[Opinion]**](Opinion.md) | Returns the list of opinions extracted from the source text | 
**phrases** | [**[Phrase]**](Phrase.md) | Returns sentiment-bearing phrases of the document | 
**relations** | [**[Relation]**](Relation.md) | Returns relations which represent a connection between one or more Entity objects | 
**sentimentPolarity** | **String** | Verbal representation of sentiment score. Can be \&quot;negative\&quot;, \&quot;positive\&quot; or \&quot;neutral\&quot; | 
**sentimentScore** | **Number** | A sentiment analysis of the document text | 
**sourceText** | **String** | Original source text passed by client for this document | 
**status** | **String** | Status of the document | 
**summary** | **String** | A summary of the document text | 
**taxonomy** | [**[Topic]**](Topic.md) | Returns the taxonomy determined for the text | 
**themes** | [**[Theme]**](Theme.md) | Returns themes of the document | 
**topics** | [**[Topic]**](Topic.md) | Returns the concept and query defined topics determined for the text | 



## Enum: SentimentPolarityEnum


* `negative` (value: `"negative"`)

* `positive` (value: `"positive"`)

* `neutral` (value: `"neutral"`)





## Enum: StatusEnum


* `queued` (value: `"queued"`)

* `processed` (value: `"processed"`)

* `failed` (value: `"failed"`)




