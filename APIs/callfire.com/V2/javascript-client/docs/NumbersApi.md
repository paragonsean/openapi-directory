# CallFireApiDocumentation.NumbersApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findNumberLeaseConfigs**](NumbersApi.md#findNumberLeaseConfigs) | **GET** /numbers/leases/configs | Find lease configs
[**findNumberLeases**](NumbersApi.md#findNumberLeases) | **GET** /numbers/leases | Find leases
[**findNumberRegions**](NumbersApi.md#findNumberRegions) | **GET** /numbers/regions | Find number regions
[**findNumbersLocal**](NumbersApi.md#findNumbersLocal) | **GET** /numbers/local | Find local numbers
[**findNumbersTollfree**](NumbersApi.md#findNumbersTollfree) | **GET** /numbers/tollfree | Find tollfree numbers
[**getNumberLease**](NumbersApi.md#getNumberLease) | **GET** /numbers/leases/{number} | Find a specific lease
[**getNumberLeaseConfig**](NumbersApi.md#getNumberLeaseConfig) | **GET** /numbers/leases/configs/{number} | Find a specific lease config
[**updateNumberLease**](NumbersApi.md#updateNumberLease) | **PUT** /numbers/leases/{number} | Update a lease
[**updateNumberLeaseConfig**](NumbersApi.md#updateNumberLeaseConfig) | **PUT** /numbers/leases/configs/{number} | Update a lease config



## findNumberLeaseConfigs

> NumberConfigPage findNumberLeaseConfigs(opts)

Find lease configs

Searches for all number lease configs for the user. Returns a paged list of NumberConfig

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.NumbersApi();
let opts = {
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'prefix': "prefix_example", // String | A 4-7 digit prefix
  'city': "city_example", // String | A city name
  'state': "state_example", // String | A two-letter state code. Example: CA, IL, etc.
  'zipcode': "zipcode_example", // String | A five-digit Zipcode
  'labelName': "labelName_example", // String | A label name
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findNumberLeaseConfigs(opts, (error, data, response) => {
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
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **prefix** | **String**| A 4-7 digit prefix | [optional] 
 **city** | **String**| A city name | [optional] 
 **state** | **String**| A two-letter state code. Example: CA, IL, etc. | [optional] 
 **zipcode** | **String**| A five-digit Zipcode | [optional] 
 **labelName** | **String**| A label name | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**NumberConfigPage**](NumberConfigPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findNumberLeases

> NumberLeasePage findNumberLeases(opts)

Find leases

Searches for all numbers leased by account user. This API is useful for finding all numbers currently owned by the user. Returns a paged list of number leases.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.NumbersApi();
let opts = {
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'prefix': "prefix_example", // String | A 4-7 digit prefix
  'city': "city_example", // String | A city name
  'state': "state_example", // String | A two-letter state code. Example: CA, IL, etc.
  'zipcode': "zipcode_example", // String | A five-digit Zipcode
  'labelName': "labelName_example", // String | A label name
  'tollFree': true, // Boolean | ~
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findNumberLeases(opts, (error, data, response) => {
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
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **prefix** | **String**| A 4-7 digit prefix | [optional] 
 **city** | **String**| A city name | [optional] 
 **state** | **String**| A two-letter state code. Example: CA, IL, etc. | [optional] 
 **zipcode** | **String**| A five-digit Zipcode | [optional] 
 **labelName** | **String**| A label name | [optional] 
 **tollFree** | **Boolean**| ~ | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**NumberLeasePage**](NumberLeasePage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findNumberRegions

> RegionPage findNumberRegions(opts)

Find number regions

Searches for region information. Use this API to obtain detailed region information that can be used to query for more specific phone numbers than a general query.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.NumbersApi();
let opts = {
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'prefix': "prefix_example", // String | A 4-7 digit prefix
  'city': "city_example", // String | A city name
  'cityPrefix': "cityPrefix_example", // String | ~
  'state': "state_example", // String | A two-letter state code. Example: CA, IL, etc.
  'zipcode': "zipcode_example", // String | A five-digit Zipcode
  'country': "country_example", // String | ~
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findNumberRegions(opts, (error, data, response) => {
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
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **prefix** | **String**| A 4-7 digit prefix | [optional] 
 **city** | **String**| A city name | [optional] 
 **cityPrefix** | **String**| ~ | [optional] 
 **state** | **String**| A two-letter state code. Example: CA, IL, etc. | [optional] 
 **zipcode** | **String**| A five-digit Zipcode | [optional] 
 **country** | **String**| ~ | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**RegionPage**](RegionPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findNumbersLocal

> NumberList findNumbersLocal(opts)

Find local numbers

Searches for numbers available for purchase in CallFire local numbers catalog . At least one additional parameter is required. User may filter local numbers by their region information. If all numbers with desirable zip code is already busy search will return available numbers with nearest zip code.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.NumbersApi();
let opts = {
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'prefix': "prefix_example", // String | A 4-7 digit prefix
  'city': "city_example", // String | A city name
  'state': "state_example", // String | A two-letter state code. Example: CA, IL, etc.
  'zipcode': "zipcode_example", // String | A five-digit Zipcode
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findNumbersLocal(opts, (error, data, response) => {
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
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **prefix** | **String**| A 4-7 digit prefix | [optional] 
 **city** | **String**| A city name | [optional] 
 **state** | **String**| A two-letter state code. Example: CA, IL, etc. | [optional] 
 **zipcode** | **String**| A five-digit Zipcode | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**NumberList**](NumberList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findNumbersTollfree

> NumberList findNumbersTollfree(opts)

Find tollfree numbers

Searches for the toll free numbers which are available for purchase in the CallFire catalog

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.NumbersApi();
let opts = {
  'pattern': "pattern_example", // String | Filter toll free numbers by prefix, pattern must be 3 char long and should end with '*'. Examples: 8**, 85*, 87* (but 855 will fail because pattern must end with '*').
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findNumbersTollfree(opts, (error, data, response) => {
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
 **pattern** | **String**| Filter toll free numbers by prefix, pattern must be 3 char long and should end with &#39;*&#39;. Examples: 8**, 85*, 87* (but 855 will fail because pattern must end with &#39;*&#39;). | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**NumberList**](NumberList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNumberLease

> NumberLease getNumberLease(number, opts)

Find a specific lease

Returns a single NumberLease instance for a given number

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.NumbersApi();
let number = "number_example"; // String | A phone number in E.164 format (11-digit). Example: 12132000384
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getNumberLease(number, opts, (error, data, response) => {
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
 **number** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384 | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**NumberLease**](NumberLease.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNumberLeaseConfig

> NumberConfig getNumberLeaseConfig(number, opts)

Find a specific lease config

Returns a single NumberConfig instance for a given number lease

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.NumbersApi();
let number = "number_example"; // String | A phone number in E.164 format (11-digit). Example: 12132000384
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getNumberLeaseConfig(number, opts, (error, data, response) => {
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
 **number** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384 | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**NumberConfig**](NumberConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNumberLease

> updateNumberLease(number, opts)

Update a lease

Updates a number lease instance. Ability to turn on/off autoRenew and toggle call/text features for a particular number

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.NumbersApi();
let number = "number_example"; // String | A phone number in E.164 format (11-digit). Example: 12132000384
let opts = {
  'numberLease': new CallFireApiDocumentation.NumberLease() // NumberLease | A NumberLease object to update
};
apiInstance.updateNumberLease(number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384 | 
 **numberLease** | [**NumberLease**](NumberLease.md)| A NumberLease object to update | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNumberLeaseConfig

> updateNumberLeaseConfig(number, opts)

Update a lease config

Updates a phone number lease configuration. Use this API endpoint to add an Inbound IVR or Call Tracking feature to a CallFire phone number. Call tracking configuration allows you to track the incoming calls, to analyze and to respond customers using sms or voice replies. For more information see [call tracking page](https://www.callfire.com/products/call-tracking)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.NumbersApi();
let number = "number_example"; // String | A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384
let opts = {
  'numberConfig': new CallFireApiDocumentation.NumberConfig() // NumberConfig | The configuration of a number lease object. There are two available types of configuration: IVR, TRACKING 
};
apiInstance.updateNumberLeaseConfig(number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **String**| A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384 | 
 **numberConfig** | [**NumberConfig**](NumberConfig.md)| The configuration of a number lease object. There are two available types of configuration: IVR, TRACKING  | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

