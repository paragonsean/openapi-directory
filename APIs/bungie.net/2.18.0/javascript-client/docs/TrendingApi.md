# BungieNetApi.TrendingApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trendingGetTrendingCategories**](TrendingApi.md#trendingGetTrendingCategories) | **GET** /Trending/Categories/ | 
[**trendingGetTrendingCategory**](TrendingApi.md#trendingGetTrendingCategory) | **GET** /Trending/Categories/{categoryId}/{pageNumber}/ | 
[**trendingGetTrendingEntryDetail**](TrendingApi.md#trendingGetTrendingEntryDetail) | **GET** /Trending/Details/{trendingEntryType}/{identifier}/ | 



## trendingGetTrendingCategories

> TrendingGetTrendingCategories200Response trendingGetTrendingCategories()



Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.TrendingApi();
apiInstance.trendingGetTrendingCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TrendingGetTrendingCategories200Response**](TrendingGetTrendingCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## trendingGetTrendingCategory

> TrendingGetTrendingCategory200Response trendingGetTrendingCategory(categoryId, pageNumber)



Returns paginated lists of trending items for a category.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.TrendingApi();
let categoryId = "categoryId_example"; // String | The ID of the category for whom you want additional results.
let pageNumber = 56; // Number | The page # of results to return.
apiInstance.trendingGetTrendingCategory(categoryId, pageNumber, (error, data, response) => {
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
 **categoryId** | **String**| The ID of the category for whom you want additional results. | 
 **pageNumber** | **Number**| The page # of results to return. | 

### Return type

[**TrendingGetTrendingCategory200Response**](TrendingGetTrendingCategory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## trendingGetTrendingEntryDetail

> TrendingGetTrendingEntryDetail200Response trendingGetTrendingEntryDetail(identifier, trendingEntryType)



Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.TrendingApi();
let identifier = "identifier_example"; // String | The identifier for the entity to be returned.
let trendingEntryType = 56; // Number | The type of entity to be returned.
apiInstance.trendingGetTrendingEntryDetail(identifier, trendingEntryType, (error, data, response) => {
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
 **identifier** | **String**| The identifier for the entity to be returned. | 
 **trendingEntryType** | **Number**| The type of entity to be returned. | 

### Return type

[**TrendingGetTrendingEntryDetail200Response**](TrendingGetTrendingEntryDetail200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

