

# Images

Defines an image answer

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextOffset** | **Integer** | Used as part of deduping. Tells client the next offset that client should use in the next pagination request |  [optional] [readonly] |
|**pivotSuggestions** | [**List&lt;PivotSuggestions&gt;**](PivotSuggestions.md) | A list of segments in the original query. For example, if the query was Red Flowers, Bing might segment the query into Red and Flowers. The Flowers pivot may contain query suggestions such as Red Peonies and Red Daisies, and the Red pivot may contain query suggestions such as Green Flowers and Yellow Flowers. |  [optional] [readonly] |
|**queryExpansions** | [**List&lt;Query&gt;**](Query.md) | A list of expanded queries that narrows the original query. For example, if the query was Microsoft Surface, the expanded queries might be: Microsoft Surface Pro 3, Microsoft Surface RT, Microsoft Surface Phone, and Microsoft Surface Hub. |  [optional] [readonly] |
|**similarTerms** | [**List&lt;Query&gt;**](Query.md) | A list of terms that are similar in meaning to the user&#39;s query term. |  [optional] [readonly] |
|**value** | [**List&lt;ImageObject&gt;**](ImageObject.md) | A list of image objects that are relevant to the query. If there are no results, the List is empty. |  |



