# CallFireApiDocumentation.KeywordsApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findKeywordLeaseConfigs**](KeywordsApi.md#findKeywordLeaseConfigs) | **GET** /keywords/leases/configs | Find keyword lease configs
[**findKeywordLeases**](KeywordsApi.md#findKeywordLeases) | **GET** /keywords/leases | Find keyword leases
[**findKeywords**](KeywordsApi.md#findKeywords) | **GET** /keywords | Find keywords
[**getKeywordLease**](KeywordsApi.md#getKeywordLease) | **GET** /keywords/leases/{keyword} | Find a specific lease
[**getKeywordLeaseById**](KeywordsApi.md#getKeywordLeaseById) | **GET** /keywords/leases/id/{id} | Find a keyword by id
[**getKeywordLeaseConfig**](KeywordsApi.md#getKeywordLeaseConfig) | **GET** /keywords/leases/configs/{keyword} | Find a specific keyword lease config
[**isKeywordAvailable**](KeywordsApi.md#isKeywordAvailable) | **GET** /keywords/{keyword}/available | Check for a specific keyword
[**updateKeywordLease**](KeywordsApi.md#updateKeywordLease) | **PUT** /keywords/leases/{keyword} | Update a lease
[**updateKeywordLeaseConfig**](KeywordsApi.md#updateKeywordLeaseConfig) | **PUT** /keywords/leases/configs/{keyword} | Update a keyword lease config



## findKeywordLeaseConfigs

> Page findKeywordLeaseConfigs(opts)

Find keyword lease configs

Searches for all keyword lease configs for the user. Returns a paged list of KeywordConfig

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.KeywordsApi();
let opts = {
  'limit': 20, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'filter': "filter_example", // String | Filter by part of Keyword name or Label name of Keyword
  'labelName': "labelName_example", // String | An exact label name to search by
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findKeywordLeaseConfigs(opts, (error, data, response) => {
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
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 20]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **filter** | **String**| Filter by part of Keyword name or Label name of Keyword | [optional] 
 **labelName** | **String**| An exact label name to search by | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findKeywordLeases

> KeywordLeasePage findKeywordLeases(opts)

Find keyword leases

Searches for all keywords owned by user. A keyword lease is the ownership information involving a keyword

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.KeywordsApi();
let opts = {
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'filter': "filter_example", // String | Filter by part of Keyword name or Label name of Keyword
  'labelName': "labelName_example", // String | An exact label name to search by
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findKeywordLeases(opts, (error, data, response) => {
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
 **filter** | **String**| Filter by part of Keyword name or Label name of Keyword | [optional] 
 **labelName** | **String**| An exact label name to search by | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**KeywordLeasePage**](KeywordLeasePage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findKeywords

> KeywordList findKeywords(opts)

Find keywords

Searches for all keywords available for purchase on the CallFire platform. If a keyword appears in the response, it is available for purchase. List the &#39;keywords&#39; in a query parameter to search for multiple keywords (at least one keyword should be sent in request). Keyword should only consist of uppercase and lowercase letters and numbers. Number of characters must be greater than 2, but less than 65.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.KeywordsApi();
let opts = {
  'keywords': ["null"] // [String] | A keyword to search for
};
apiInstance.findKeywords(opts, (error, data, response) => {
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
 **keywords** | [**[String]**](String.md)| A keyword to search for | [optional] 

### Return type

[**KeywordList**](KeywordList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKeywordLease

> KeywordLease getKeywordLease(keyword, opts)

Find a specific lease

Searches for all keywords owned by user

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.KeywordsApi();
let keyword = "keyword_example"; // String | Keyword text that a lease is desired for
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getKeywordLease(keyword, opts, (error, data, response) => {
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
 **keyword** | **String**| Keyword text that a lease is desired for | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**KeywordLease**](KeywordLease.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKeywordLeaseById

> KeywordLease getKeywordLeaseById(id, opts)

Find a keyword by id

Get keyword by id

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.KeywordsApi();
let id = 789; // Number | ~
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getKeywordLeaseById(id, opts, (error, data, response) => {
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
 **id** | **Number**| ~ | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**KeywordLease**](KeywordLease.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKeywordLeaseConfig

> KeywordConfig getKeywordLeaseConfig(keyword, opts)

Find a specific keyword lease config

Returns a single KeywordConfig instance for a given keyword lease

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.KeywordsApi();
let keyword = "keyword_example"; // String | A Keyword to get KeywordConfig by
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getKeywordLeaseConfig(keyword, opts, (error, data, response) => {
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
 **keyword** | **String**| A Keyword to get KeywordConfig by | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**KeywordConfig**](KeywordConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## isKeywordAvailable

> Boolean isKeywordAvailable(keyword)

Check for a specific keyword

Searches for the specific keyword to purchase on the CallFire platform. Returns &#39;true&#39; if keyword is available. Keyword should only consist of uppercase and lowercase letters and numbers. Number of characters must be greater than 2, but less than 65.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.KeywordsApi();
let keyword = "keyword_example"; // String | To specify a keyword to search for. Example: SUN, MOON
apiInstance.isKeywordAvailable(keyword, (error, data, response) => {
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
 **keyword** | **String**| To specify a keyword to search for. Example: SUN, MOON | 

### Return type

**Boolean**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateKeywordLease

> updateKeywordLease(keyword, opts)

Update a lease

Updates a keyword lease. Turns the autoRenew on/off. Configure double opt in feature. Add/remove contact list from keyword.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.KeywordsApi();
let keyword = "keyword_example"; // String | To update a keyword lease
let opts = {
  'keywordLease': new CallFireApiDocumentation.KeywordLease() // KeywordLease | A keyword lease object
};
apiInstance.updateKeywordLease(keyword, opts, (error, data, response) => {
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
 **keyword** | **String**| To update a keyword lease | 
 **keywordLease** | [**KeywordLease**](KeywordLease.md)| A keyword lease object | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateKeywordLeaseConfig

> updateKeywordLeaseConfig(keyword, opts)

Update a keyword lease config

Updates a keyword lease configuration. Use this API endpoint to enable/disable inbound SMS forwarding, set forward number. Forward number must be in E.164 format)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.KeywordsApi();
let keyword = "keyword_example"; // String | To update a keyword lease config
let opts = {
  'keywordConfig': new CallFireApiDocumentation.KeywordConfig() // KeywordConfig | The configuration of a keyword lease object.
};
apiInstance.updateKeywordLeaseConfig(keyword, opts, (error, data, response) => {
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
 **keyword** | **String**| To update a keyword lease config | 
 **keywordConfig** | [**KeywordConfig**](KeywordConfig.md)| The configuration of a keyword lease object. | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

