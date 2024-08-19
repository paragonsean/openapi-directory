# TransportForLondonUnifiedApi.SearchApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchBusSchedules**](SearchApi.md#searchBusSchedules) | **GET** /Search/BusSchedules | Searches the bus schedules folder on S3 for a given bus number.
[**searchGet**](SearchApi.md#searchGet) | **GET** /Search | Search the site for occurrences of the query string. The maximum number of results returned is equal to the maximum page size              of 100. To return subsequent pages, use the paginated overload.
[**searchMetaCategories**](SearchApi.md#searchMetaCategories) | **GET** /Search/Meta/Categories | Gets the available search categories.
[**searchMetaSearchProviders**](SearchApi.md#searchMetaSearchProviders) | **GET** /Search/Meta/SearchProviders | Gets the available searchProvider names.
[**searchMetaSorts**](SearchApi.md#searchMetaSorts) | **GET** /Search/Meta/Sorts | Gets the available sorting options.



## searchBusSchedules

> TflApiPresentationEntitiesSearchResponse searchBusSchedules(query)

Searches the bus schedules folder on S3 for a given bus number.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.SearchApi();
let query = "query_example"; // String | The search query
apiInstance.searchBusSchedules(query, (error, data, response) => {
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
 **query** | **String**| The search query | 

### Return type

[**TflApiPresentationEntitiesSearchResponse**](TflApiPresentationEntitiesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## searchGet

> TflApiPresentationEntitiesSearchResponse searchGet(query)

Search the site for occurrences of the query string. The maximum number of results returned is equal to the maximum page size              of 100. To return subsequent pages, use the paginated overload.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.SearchApi();
let query = "query_example"; // String | The search query
apiInstance.searchGet(query, (error, data, response) => {
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
 **query** | **String**| The search query | 

### Return type

[**TflApiPresentationEntitiesSearchResponse**](TflApiPresentationEntitiesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## searchMetaCategories

> [String] searchMetaCategories()

Gets the available search categories.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.SearchApi();
apiInstance.searchMetaCategories((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## searchMetaSearchProviders

> [String] searchMetaSearchProviders()

Gets the available searchProvider names.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.SearchApi();
apiInstance.searchMetaSearchProviders((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## searchMetaSorts

> [String] searchMetaSorts()

Gets the available sorting options.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.SearchApi();
apiInstance.searchMetaSorts((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

