

# ImageInsights

The top-level object that the response includes when an image insights request succeeds. For information about requesting image insights, see the [insightsToken](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#insightstoken) query parameter. The modules query parameter affects the fields that Bing includes in the response. If you set [modules](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#modulesrequested) to only Caption, then this object includes only the imageCaption field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bestRepresentativeQuery** | [**Query**](Query.md) |  |  [optional] |
|**imageCaption** | [**ImageInsightsImageCaption**](ImageInsightsImageCaption.md) |  |  [optional] |
|**imageInsightsToken** | **String** | A token that you use in a subsequent call to the Image Search API to get more information about the image. For information about using this token, see the insightsToken query parameter. This token has the same usage as the token in the Image object. |  [optional] [readonly] |
|**imageTags** | [**ImageTagsModule**](ImageTagsModule.md) |  |  [optional] |
|**pagesIncluding** | [**ImagesModule**](ImagesModule.md) |  |  [optional] |
|**recipes** | [**RecipesModule**](RecipesModule.md) |  |  [optional] |
|**recognizedEntityGroups** | [**RecognizedEntitiesModule**](RecognizedEntitiesModule.md) |  |  [optional] |
|**relatedCollections** | [**RelatedCollectionsModule**](RelatedCollectionsModule.md) |  |  [optional] |
|**relatedSearches** | [**RelatedSearchesModule**](RelatedSearchesModule.md) |  |  [optional] |
|**shoppingSources** | [**AggregateOffer**](AggregateOffer.md) |  |  [optional] |
|**visuallySimilarImages** | [**ImagesModule**](ImagesModule.md) |  |  [optional] |
|**visuallySimilarProducts** | [**ImagesModule**](ImagesModule.md) |  |  [optional] |



