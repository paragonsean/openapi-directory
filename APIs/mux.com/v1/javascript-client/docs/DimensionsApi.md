# MuxApi.DimensionsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listDimensionValues**](DimensionsApi.md#listDimensionValues) | **GET** /data/v1/dimensions/{DIMENSION_ID} | Lists the values for a specific dimension
[**listDimensions**](DimensionsApi.md#listDimensions) | **GET** /data/v1/dimensions | List Dimensions



## listDimensionValues

> ListDimensionValuesResponse listDimensionValues(DIMENSION_ID, opts)

Lists the values for a specific dimension

Lists the values for a dimension along with a total count of related views.  Note: This API replaces the list-filter-values API call. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.DimensionsApi();
let DIMENSION_ID = "abcd1234"; // String | ID of the Dimension
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1, // Number | Offset by this many pages, of the size of `limit`
  'filters': ["null"], // [String] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
  'timeframe': ["null"] // [String] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days` 
};
apiInstance.listDimensionValues(DIMENSION_ID, opts, (error, data, response) => {
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
 **DIMENSION_ID** | **String**| ID of the Dimension | 
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **filters** | [**[String]**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **timeframe** | [**[String]**](String.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListDimensionValuesResponse**](ListDimensionValuesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDimensions

> ListDimensionsResponse listDimensions()

List Dimensions

List all available dimensions.  Note: This API replaces the list-filters API call. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.DimensionsApi();
apiInstance.listDimensions((error, data, response) => {
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

[**ListDimensionsResponse**](ListDimensionsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

