# GoogleMyBusinessApi.ListBusinessCategoriesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**[Category]**](Category.md) | The categories. Categories are BASIC view. They don&#39;t contain any ServiceType information. | [optional] 
**nextPageToken** | **String** | If the number of categories exceeded the requested page size, this field will be populated with a token to fetch the next page of categories on a subsequent call to &#x60;ListBusinessCategories&#x60;. | [optional] 
**totalCategoryCount** | **Number** | The total number of categories for the request parameters. | [optional] 


