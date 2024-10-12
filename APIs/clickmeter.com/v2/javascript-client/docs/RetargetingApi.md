# ClickMeterApi.RetargetingApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retargetingCount**](RetargetingApi.md#retargetingCount) | **GET** /retargeting/count | Retrieve count of retargeting scripts
[**retargetingDelete**](RetargetingApi.md#retargetingDelete) | **DELETE** /retargeting/{id} | Deletes a retargeting script (and remove associations)
[**retargetingGet**](RetargetingApi.md#retargetingGet) | **GET** /retargeting | List of all the retargeting scripts associated to the user
[**retargetingGetDatapoints**](RetargetingApi.md#retargetingGetDatapoints) | **GET** /retargeting/{id}/datapoints | List of all the datapoints associated to the retargeting script.
[**retargetingGetDatapointsCount**](RetargetingApi.md#retargetingGetDatapointsCount) | **GET** /retargeting/{id}/datapoints/count | Count the datapoints associated to the retargeting script.
[**retargetingIdGet**](RetargetingApi.md#retargetingIdGet) | **GET** /retargeting/{id} | Get a retargeting script object
[**retargetingPost**](RetargetingApi.md#retargetingPost) | **POST** /retargeting/{id} | Updates a retargeting script
[**retargetingPut**](RetargetingApi.md#retargetingPut) | **POST** /retargeting | Creates a retargeting script



## retargetingCount

> ApiCoreResponsesCountResponce retargetingCount()

Retrieve count of retargeting scripts

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.RetargetingApi();
apiInstance.retargetingCount((error, data, response) => {
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

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## retargetingDelete

> ApiCoreResponsesEntityUriSystemInt64 retargetingDelete(id)

Deletes a retargeting script (and remove associations)

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.RetargetingApi();
let id = 789; // Number | The id of the retargeting script
apiInstance.retargetingDelete(id, (error, data, response) => {
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
 **id** | **Number**| The id of the retargeting script | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## retargetingGet

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 retargetingGet(opts)

List of all the retargeting scripts associated to the user

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.RetargetingApi();
let opts = {
  'offset': 0, // Number | Where to start when retrieving elements. Default is 0 if not specified.
  'limit': 20 // Number | Maximum elements to retrieve. Default to 20 if not specified.
};
apiInstance.retargetingGet(opts, (error, data, response) => {
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
 **offset** | **Number**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0]
 **limit** | **Number**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20]

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## retargetingGetDatapoints

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 retargetingGetDatapoints(id, opts)

List of all the datapoints associated to the retargeting script.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.RetargetingApi();
let id = 789; // Number | Id of the retargeting script
let opts = {
  'offset': 0, // Number | Where to start when retrieving elements. Default is 0 if not specified.
  'limit': 20, // Number | Maximum elements to retrieve. Default to 20 if not specified.
  'status': "status_example", // String | Status of the datapoint
  'tags': "tags_example", // String | A comma separated list of tags you want to filter with.
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'onlyFavorites': true, // Boolean | Filter fields by favourite status
  'sortBy': "sortBy_example", // String | Field to sort by
  'sortDirection': "sortDirection_example", // String | Direction of sort \"asc\" or \"desc\"
  'createdAfter': "createdAfter_example", // String | Exclude datapoints created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude datapoints created after this date (YYYYMMDD)
};
apiInstance.retargetingGetDatapoints(id, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the retargeting script | 
 **offset** | **Number**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0]
 **limit** | **Number**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20]
 **status** | **String**| Status of the datapoint | [optional] 
 **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **onlyFavorites** | **Boolean**| Filter fields by favourite status | [optional] 
 **sortBy** | **String**| Field to sort by | [optional] 
 **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] 
 **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## retargetingGetDatapointsCount

> ApiCoreResponsesCountResponce retargetingGetDatapointsCount(id, opts)

Count the datapoints associated to the retargeting script.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.RetargetingApi();
let id = 789; // Number | Id of the group
let opts = {
  'status': "status_example", // String | Status of the datapoint
  'tags': "tags_example", // String | A comma separated list of tags you want to filter with.
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'onlyFavorites': true, // Boolean | Filter fields by favourite status
  'createdAfter': "createdAfter_example", // String | Exclude datapoints created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude datapoints created after this date (YYYYMMDD)
};
apiInstance.retargetingGetDatapointsCount(id, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the group | 
 **status** | **String**| Status of the datapoint | [optional] 
 **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **onlyFavorites** | **Boolean**| Filter fields by favourite status | [optional] 
 **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## retargetingIdGet

> ApiCoreDtoRetargetingRetargetingScript retargetingIdGet(id)

Get a retargeting script object

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.RetargetingApi();
let id = 789; // Number | The id of the retargeting script
apiInstance.retargetingIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The id of the retargeting script | 

### Return type

[**ApiCoreDtoRetargetingRetargetingScript**](ApiCoreDtoRetargetingRetargetingScript.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## retargetingPost

> ApiCoreResponsesEntityUriSystemInt64 retargetingPost(id, apiCoreDtoRetargetingRetargetingScript)

Updates a retargeting script

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.RetargetingApi();
let id = 789; // Number | The id of the retargeting script
let apiCoreDtoRetargetingRetargetingScript = new ClickMeterApi.ApiCoreDtoRetargetingRetargetingScript(); // ApiCoreDtoRetargetingRetargetingScript | The body of the retargeting script
apiInstance.retargetingPost(id, apiCoreDtoRetargetingRetargetingScript, (error, data, response) => {
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
 **id** | **Number**| The id of the retargeting script | 
 **apiCoreDtoRetargetingRetargetingScript** | [**ApiCoreDtoRetargetingRetargetingScript**](ApiCoreDtoRetargetingRetargetingScript.md)| The body of the retargeting script | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## retargetingPut

> ApiCoreResponsesEntityUriSystemInt64 retargetingPut(apiCoreDtoRetargetingRetargetingScript)

Creates a retargeting script

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.RetargetingApi();
let apiCoreDtoRetargetingRetargetingScript = new ClickMeterApi.ApiCoreDtoRetargetingRetargetingScript(); // ApiCoreDtoRetargetingRetargetingScript | The body of the retargeting script
apiInstance.retargetingPut(apiCoreDtoRetargetingRetargetingScript, (error, data, response) => {
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
 **apiCoreDtoRetargetingRetargetingScript** | [**ApiCoreDtoRetargetingRetargetingScript**](ApiCoreDtoRetargetingRetargetingScript.md)| The body of the retargeting script | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

