# RatGenomeDatabaseRestApi.PathwayApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPathwaysWithDiagramsForCategoryUsingGET**](PathwayApi.md#getPathwaysWithDiagramsForCategoryUsingGET) | **GET** /pathways/diagramsForCategory/{category} | Return a list of pathways based on category provided
[**searchPathwaysUsingGET**](PathwayApi.md#searchPathwaysUsingGET) | **GET** /pathways/diagrams/search/{searchString} | Return a list of pathways based on search term



## getPathwaysWithDiagramsForCategoryUsingGET

> [Pathway] getPathwaysWithDiagramsForCategoryUsingGET(category)

Return a list of pathways based on category provided

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.PathwayApi();
let category = "category_example"; // String | Pathway Category
apiInstance.getPathwaysWithDiagramsForCategoryUsingGET(category, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **String**| Pathway Category | 

### Return type

[**[Pathway]**](Pathway.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## searchPathwaysUsingGET

> [Pathway] searchPathwaysUsingGET(searchString)

Return a list of pathways based on search term

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.PathwayApi();
let searchString = "searchString_example"; // String | Free text search string
apiInstance.searchPathwaysUsingGET(searchString, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchString** | **String**| Free text search string | 

### Return type

[**[Pathway]**](Pathway.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

