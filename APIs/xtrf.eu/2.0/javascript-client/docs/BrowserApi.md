# XtrfHomePortalApi.BrowserApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browseCSV**](BrowserApi.md#browseCSV) | **GET** /browser/csv | Searches for data (ie. customer, task, etc) and returns it in a CSV form.
[**browseJSON**](BrowserApi.md#browseJSON) | **GET** /browser | Searches for data (ie. customer, task, etc) and returns it in a tabular form.
[**callDelete**](BrowserApi.md#callDelete) | **DELETE** /browser/views/{viewId} | Removes a view.
[**create**](BrowserApi.md#create) | **POST** /browser/views/for/{className} | Creates view for given class.
[**deleteColumn**](BrowserApi.md#deleteColumn) | **DELETE** /browser/views/{viewId}/columns/{columnName} | Deletes a single column from view.
[**get**](BrowserApi.md#get) | **GET** /browser/views/{viewId} | Returns all view&#39;s information.
[**getColumnSettings**](BrowserApi.md#getColumnSettings) | **GET** /browser/views/{viewId}/columns/{columnName}/settings | Returns column&#39;s specific settings.
[**getColumns**](BrowserApi.md#getColumns) | **GET** /browser/views/{viewId}/columns | Returns columns defined in view.
[**getCurrentViewDetails**](BrowserApi.md#getCurrentViewDetails) | **GET** /browser/views/details/for/{className} | Returns current view&#39;s detailed information, suitable for browser.
[**getFilter**](BrowserApi.md#getFilter) | **GET** /browser/views/{viewId}/filter | Returns view&#39;s filter.
[**getLocalSettings**](BrowserApi.md#getLocalSettings) | **GET** /browser/views/{viewId}/settings/local | Returns view&#39;s local settings (for current user).
[**getOrder**](BrowserApi.md#getOrder) | **GET** /browser/views/{viewId}/order | Returns view&#39;s order settings.
[**getPermissions**](BrowserApi.md#getPermissions) | **GET** /browser/views/{viewId}/permissions | Returns view&#39;s permissions.
[**getSettings**](BrowserApi.md#getSettings) | **GET** /browser/views/{viewId}/settings | Returns view&#39;s settings.
[**getViewDetails**](BrowserApi.md#getViewDetails) | **GET** /browser/views/details/for/{className}/{viewId} | Returns view&#39;s detailed information, suitable for browser.
[**getViewsBrief**](BrowserApi.md#getViewsBrief) | **GET** /browser/views/for/{className} | Returns views&#39; brief.
[**selectViewAndGetItsDetails**](BrowserApi.md#selectViewAndGetItsDetails) | **POST** /browser/views/details/for/{className}/{viewId} | Selects given view as current and returns its detailed information, suitable for browser.
[**update**](BrowserApi.md#update) | **PUT** /browser/views/{viewId} | Updates all view&#39;s information.
[**updateColumnSettings**](BrowserApi.md#updateColumnSettings) | **PUT** /browser/views/{viewId}/columns/{columnName}/settings | Updates column&#39;s specific settings.
[**updateColumns**](BrowserApi.md#updateColumns) | **PUT** /browser/views/{viewId}/columns | Updates columns in view.
[**updateFilter**](BrowserApi.md#updateFilter) | **PUT** /browser/views/{viewId}/filter | Updates view&#39;s filter.
[**updateFilterProperty**](BrowserApi.md#updateFilterProperty) | **PUT** /browser/views/{viewId}/filter/{filterProperty} | Updates view&#39;s filter property.
[**updateLocalSettings**](BrowserApi.md#updateLocalSettings) | **PUT** /browser/views/{viewId}/settings/local | Updates view&#39;s local settings (for current user).
[**updateOrder**](BrowserApi.md#updateOrder) | **PUT** /browser/views/{viewId}/order | Updates view&#39;s order settings.
[**updatePermissions**](BrowserApi.md#updatePermissions) | **PUT** /browser/views/{viewId}/permissions | Updates view&#39;s permissions.
[**updateSettings**](BrowserApi.md#updateSettings) | **PUT** /browser/views/{viewId}/settings | Updates view&#39;s settings.



## browseCSV

> Object browseCSV(opts)

Searches for data (ie. customer, task, etc) and returns it in a CSV form.

Searches for data (ie. customer, task, etc) and returns it in a CSV form.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let opts = {
  'viewId': 789, // Number | view's identifier
  'separator': "separator_example", // String | csv field separator
  'secondarySeparator': "secondarySeparator_example", // String | secondary csv field separator
  'additionalOrder': "additionalOrder_example" // String | 
};
apiInstance.browseCSV(opts, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | [optional] 
 **separator** | **String**| csv field separator | [optional] 
 **secondarySeparator** | **String**| secondary csv field separator | [optional] 
 **additionalOrder** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## browseJSON

> Object browseJSON(opts)

Searches for data (ie. customer, task, etc) and returns it in a tabular form.

Searches for data (ie. customer, task, etc) and returns it in a tabular form.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let opts = {
  'viewId': 789, // Number | view's identifier
  'page': 0, // Number | 
  'additionalOrder': "additionalOrder_example", // String | 
  'useDeferredColumns': "useDeferredColumns_example", // String | 
  'maxRows': 0 // Number | overrides view's default rows limit, supported values 10 to 1000
};
apiInstance.browseJSON(opts, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | [optional] 
 **page** | **Number**|  | [optional] [default to 0]
 **additionalOrder** | **String**|  | [optional] 
 **useDeferredColumns** | **String**|  | [optional] 
 **maxRows** | **Number**| overrides view&#39;s default rows limit, supported values 10 to 1000 | [optional] [default to 0]

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## callDelete

> callDelete(viewId)

Removes a view.

Removes a view. No content is returned upon success (204).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's internal identifier
apiInstance.callDelete(viewId, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## create

> ViewWithIdDTO create(className, viewDTO)

Creates view for given class.

Creates view for given class.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let className = "className_example"; // String | view's class name
let viewDTO = new XtrfHomePortalApi.ViewDTO(); // ViewDTO | Created view for given class.
apiInstance.create(className, viewDTO, (error, data, response) => {
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
 **className** | **String**| view&#39;s class name | 
 **viewDTO** | [**ViewDTO**](ViewDTO.md)| Created view for given class. | 

### Return type

[**ViewWithIdDTO**](ViewWithIdDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## deleteColumn

> [ColumnDTO] deleteColumn(viewId, columnName)

Deletes a single column from view.

Deletes a single column from view.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let columnName = "columnName_example"; // String | column's name
apiInstance.deleteColumn(viewId, columnName, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **columnName** | **String**| column&#39;s name | 

### Return type

[**[ColumnDTO]**](ColumnDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## get

> ViewDTO get(viewId)

Returns all view&#39;s information.

Returns all view&#39;s information (ie. name, columns, filters, etc).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
apiInstance.get(viewId, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 

### Return type

[**ViewDTO**](ViewDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getColumnSettings

> Object getColumnSettings(viewId, columnName)

Returns column&#39;s specific settings.

Returns column&#39;s specific settings. For example when column describes money amount we can decide whether it should display currency or not.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let columnName = "columnName_example"; // String | column's name
apiInstance.getColumnSettings(viewId, columnName, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **columnName** | **String**| column&#39;s name | 

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getColumns

> [ColumnDTO] getColumns(viewId)

Returns columns defined in view.

Returns columns defined in view.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
apiInstance.getColumns(viewId, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 

### Return type

[**[ColumnDTO]**](ColumnDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCurrentViewDetails

> ViewDetailsDTO getCurrentViewDetails(className, opts)

Returns current view&#39;s detailed information, suitable for browser.

Returns current view&#39;s detailed information, suitable for browser.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let className = "className_example"; // String | views' class name
let opts = {
  'placeName': "'default'" // String | place name (denotes specific place in system with the table)
};
apiInstance.getCurrentViewDetails(className, opts, (error, data, response) => {
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
 **className** | **String**| views&#39; class name | 
 **placeName** | **String**| place name (denotes specific place in system with the table) | [optional] [default to &#39;default&#39;]

### Return type

[**ViewDetailsDTO**](ViewDetailsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getFilter

> FilterDTO getFilter(viewId)

Returns view&#39;s filter.

Returns view&#39;s filter.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
apiInstance.getFilter(viewId, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 

### Return type

[**FilterDTO**](FilterDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getLocalSettings

> LocalSettingsDTO getLocalSettings(viewId)

Returns view&#39;s local settings (for current user).

Returns view&#39;s local settings (for current user).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
apiInstance.getLocalSettings(viewId, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 

### Return type

[**LocalSettingsDTO**](LocalSettingsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getOrder

> OrderDTO getOrder(viewId)

Returns view&#39;s order settings.

Returns view&#39;s order settings.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
apiInstance.getOrder(viewId, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 

### Return type

[**OrderDTO**](OrderDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getPermissions

> PermissionsDTO getPermissions(viewId)

Returns view&#39;s permissions.

Returns view&#39;s permissions.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
apiInstance.getPermissions(viewId, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 

### Return type

[**PermissionsDTO**](PermissionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getSettings

> SettingsDTO getSettings(viewId)

Returns view&#39;s settings.

Returns view&#39;s settings (ie. name).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
apiInstance.getSettings(viewId, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 

### Return type

[**SettingsDTO**](SettingsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getViewDetails

> ViewDetailsDTO getViewDetails(className, viewId, opts)

Returns view&#39;s detailed information, suitable for browser.

Returns view&#39;s detailed information, suitable for browser.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let className = "className_example"; // String | views' class name
let viewId = 789; // Number | 
let opts = {
  'placeName': "'default'" // String | place name (denotes specific place in system with the table)
};
apiInstance.getViewDetails(className, viewId, opts, (error, data, response) => {
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
 **className** | **String**| views&#39; class name | 
 **viewId** | **Number**|  | 
 **placeName** | **String**| place name (denotes specific place in system with the table) | [optional] [default to &#39;default&#39;]

### Return type

[**ViewDetailsDTO**](ViewDetailsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getViewsBrief

> ViewsBriefDTO getViewsBrief(className, opts)

Returns views&#39; brief.

Returns views&#39; brief.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let className = "className_example"; // String | views' class name
let opts = {
  'placeName': "'default'" // String | place name (denotes specific place in system with the table)
};
apiInstance.getViewsBrief(className, opts, (error, data, response) => {
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
 **className** | **String**| views&#39; class name | 
 **placeName** | **String**| place name (denotes specific place in system with the table) | [optional] [default to &#39;default&#39;]

### Return type

[**ViewsBriefDTO**](ViewsBriefDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## selectViewAndGetItsDetails

> ViewDetailsDTO selectViewAndGetItsDetails(className, viewId, opts)

Selects given view as current and returns its detailed information, suitable for browser.

Selects given view as current and returns its detailed information, suitable for browser.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let className = "className_example"; // String | views' class name
let viewId = 789; // Number | 
let opts = {
  'placeNameDenotesSpecificPlaceInSystemWithTheTable': "'default'" // String | 
};
apiInstance.selectViewAndGetItsDetails(className, viewId, opts, (error, data, response) => {
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
 **className** | **String**| views&#39; class name | 
 **viewId** | **Number**|  | 
 **placeNameDenotesSpecificPlaceInSystemWithTheTable** | **String**|  | [optional] [default to &#39;default&#39;]

### Return type

[**ViewDetailsDTO**](ViewDetailsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## update

> ViewDTO update(viewId, viewDTO)

Updates all view&#39;s information.

Updates all view&#39;s information (ie. name, columns, filters, etc).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let viewDTO = new XtrfHomePortalApi.ViewDTO(); // ViewDTO | Updated all view's information.
apiInstance.update(viewId, viewDTO, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **viewDTO** | [**ViewDTO**](ViewDTO.md)| Updated all view&#39;s information. | 

### Return type

[**ViewDTO**](ViewDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateColumnSettings

> Object updateColumnSettings(viewId, columnName, body)

Updates column&#39;s specific settings.

Updates column&#39;s specific settings. For example when column describes money amount we can decide whether it should display currency or not.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let columnName = "columnName_example"; // String | column's name
let body = /home-api/assets/examples/browsers/views/updateColumnSettings.json#requestBody; // Object | Updated column's specific settings.
apiInstance.updateColumnSettings(viewId, columnName, body, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **columnName** | **String**| column&#39;s name | 
 **body** | **Object**| Updated column&#39;s specific settings. | 

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateColumns

> [ColumnDTO] updateColumns(viewId, columnDTO)

Updates columns in view.

Updates columns in view.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let columnDTO = /home-api/assets/examples/browsers/views/updateColumns.json#requestBody; // [ColumnDTO] | Updated columns in view.
apiInstance.updateColumns(viewId, columnDTO, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **columnDTO** | [**[ColumnDTO]**](ColumnDTO.md)| Updated columns in view. | 

### Return type

[**[ColumnDTO]**](ColumnDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateFilter

> FilterDTO updateFilter(viewId, filterPropertyDTO)

Updates view&#39;s filter.

Updates view&#39;s filter.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let filterPropertyDTO = /home-api/assets/examples/browsers/views/updateFilter.json#requestBody; // [FilterPropertyDTO] | Updated view's filter.
apiInstance.updateFilter(viewId, filterPropertyDTO, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **filterPropertyDTO** | [**[FilterPropertyDTO]**](FilterPropertyDTO.md)| Updated view&#39;s filter. | 

### Return type

[**FilterDTO**](FilterDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateFilterProperty

> Object updateFilterProperty(viewId, filterProperty, filterPropertyDTO)

Updates view&#39;s filter property.

Updates view&#39;s filter property.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let filterProperty = "filterProperty_example"; // String | view's filter property name
let filterPropertyDTO = /home-api/assets/examples/browsers/views/updateFilterProperty.json#requestBody; // FilterPropertyDTO | Updated view's filter property.
apiInstance.updateFilterProperty(viewId, filterProperty, filterPropertyDTO, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **filterProperty** | **String**| view&#39;s filter property name | 
 **filterPropertyDTO** | [**FilterPropertyDTO**](FilterPropertyDTO.md)| Updated view&#39;s filter property. | 

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateLocalSettings

> LocalSettingsDTO updateLocalSettings(viewId, localSettingsDTO)

Updates view&#39;s local settings (for current user).

Updates view&#39;s local settings (for current user).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let localSettingsDTO = /home-api/assets/examples/browsers/views/updateLocalSettings.json#requestBody; // LocalSettingsDTO | Updated view's local settings (for current user).
apiInstance.updateLocalSettings(viewId, localSettingsDTO, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **localSettingsDTO** | [**LocalSettingsDTO**](LocalSettingsDTO.md)| Updated view&#39;s local settings (for current user). | 

### Return type

[**LocalSettingsDTO**](LocalSettingsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateOrder

> OrderDTO updateOrder(viewId, orderDTO)

Updates view&#39;s order settings.

Updates view&#39;s order settings.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let orderDTO = /home-api/assets/examples/browsers/views/updateOrder.json#requestBody; // OrderDTO | Updated view's order settings.
apiInstance.updateOrder(viewId, orderDTO, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **orderDTO** | [**OrderDTO**](OrderDTO.md)| Updated view&#39;s order settings. | 

### Return type

[**OrderDTO**](OrderDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updatePermissions

> PermissionsDTO updatePermissions(viewId, permissionsDTO)

Updates view&#39;s permissions.

Updates view&#39;s permissions.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let permissionsDTO = /home-api/assets/examples/browsers/views/updatePermissions.json#requestBody; // PermissionsDTO | Updated view's permissions.
apiInstance.updatePermissions(viewId, permissionsDTO, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **permissionsDTO** | [**PermissionsDTO**](PermissionsDTO.md)| Updated view&#39;s permissions. | 

### Return type

[**PermissionsDTO**](PermissionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateSettings

> SettingsDTO updateSettings(viewId, settingsDTO)

Updates view&#39;s settings.

Updates view&#39;s settings.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.BrowserApi();
let viewId = 789; // Number | view's identifier
let settingsDTO = /home-api/assets/examples/browsers/views/updateSettings.json#requestBody; // SettingsDTO | Updated view's settings.
apiInstance.updateSettings(viewId, settingsDTO, (error, data, response) => {
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
 **viewId** | **Number**| view&#39;s identifier | 
 **settingsDTO** | [**SettingsDTO**](SettingsDTO.md)| Updated view&#39;s settings. | 

### Return type

[**SettingsDTO**](SettingsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

