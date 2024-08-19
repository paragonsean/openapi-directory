# MyBusinessBusinessInformationApi.AccountsApi

All URIs are relative to *https://mybusinessbusinessinformation.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinessbusinessinformationAccountsLocationsCreate**](AccountsApi.md#mybusinessbusinessinformationAccountsLocationsCreate) | **POST** /v1/{parent}/locations | 
[**mybusinessbusinessinformationAccountsLocationsList**](AccountsApi.md#mybusinessbusinessinformationAccountsLocationsList) | **GET** /v1/{parent}/locations | 



## mybusinessbusinessinformationAccountsLocationsCreate

> Location mybusinessbusinessinformationAccountsLocationsCreate(parent, opts)



Creates a new Location that will be owned by the logged in user.

### Example

```javascript
import MyBusinessBusinessInformationApi from 'my_business_business_information_api';

let apiInstance = new MyBusinessBusinessInformationApi.AccountsApi();
let parent = "parent_example"; // String | Required. The name of the account in which to create this location.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'requestId': "requestId_example", // String | Optional. A unique request ID for the server to detect duplicated requests. We recommend using UUIDs. Max length is 50 characters.
  'validateOnly': true, // Boolean | Optional. If true, the request is validated without actually creating the location.
  'location': new MyBusinessBusinessInformationApi.Location() // Location | 
};
apiInstance.mybusinessbusinessinformationAccountsLocationsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The name of the account in which to create this location. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **requestId** | **String**| Optional. A unique request ID for the server to detect duplicated requests. We recommend using UUIDs. Max length is 50 characters. | [optional] 
 **validateOnly** | **Boolean**| Optional. If true, the request is validated without actually creating the location. | [optional] 
 **location** | [**Location**](Location.md)|  | [optional] 

### Return type

[**Location**](Location.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mybusinessbusinessinformationAccountsLocationsList

> ListLocationsResponse mybusinessbusinessinformationAccountsLocationsList(parent, opts)



Lists the locations for the specified account.

### Example

```javascript
import MyBusinessBusinessInformationApi from 'my_business_business_information_api';

let apiInstance = new MyBusinessBusinessInformationApi.AccountsApi();
let parent = "parent_example"; // String | Required. The name of the account to fetch locations from. If the parent Account is of AccountType PERSONAL, only Locations that are directly owned by the Account are returned, otherwise it will return all accessible locations from the Account, either directly or indirectly.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. A filter constraining the locations to return. The response includes only entries that match the filter. If `filter` is empty, then constraints are applied and all locations (paginated) are retrieved for the requested account. For more information about valid fields and example usage, see [Work with Location Data Guide](https://developers.google.com/my-business/content/location-data#filter_results_when_you_list_locations).
  'orderBy': "orderBy_example", // String | Optional. Sorting order for the request. Multiple fields should be comma-separated, following SQL syntax. The default sorting order is ascending. To specify descending order, a suffix \" desc\" should be added. Valid fields to order_by are title and store_code. For example: \"title, store_code desc\" or \"title\" or \"store_code desc\"
  'pageSize': 56, // Number | Optional. How many locations to fetch per page. Default value is 10 if not set. Minimum is 1, and maximum page size is 100.
  'pageToken': "pageToken_example", // String | Optional. If specified, it fetches the next `page` of locations. The page token is returned by previous calls to `ListLocations` when there were more locations than could fit in the requested page size.
  'readMask': "readMask_example" // String | Required. Read mask to specify what fields will be returned in the response.
};
apiInstance.mybusinessbusinessinformationAccountsLocationsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The name of the account to fetch locations from. If the parent Account is of AccountType PERSONAL, only Locations that are directly owned by the Account are returned, otherwise it will return all accessible locations from the Account, either directly or indirectly. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. A filter constraining the locations to return. The response includes only entries that match the filter. If &#x60;filter&#x60; is empty, then constraints are applied and all locations (paginated) are retrieved for the requested account. For more information about valid fields and example usage, see [Work with Location Data Guide](https://developers.google.com/my-business/content/location-data#filter_results_when_you_list_locations). | [optional] 
 **orderBy** | **String**| Optional. Sorting order for the request. Multiple fields should be comma-separated, following SQL syntax. The default sorting order is ascending. To specify descending order, a suffix \&quot; desc\&quot; should be added. Valid fields to order_by are title and store_code. For example: \&quot;title, store_code desc\&quot; or \&quot;title\&quot; or \&quot;store_code desc\&quot; | [optional] 
 **pageSize** | **Number**| Optional. How many locations to fetch per page. Default value is 10 if not set. Minimum is 1, and maximum page size is 100. | [optional] 
 **pageToken** | **String**| Optional. If specified, it fetches the next &#x60;page&#x60; of locations. The page token is returned by previous calls to &#x60;ListLocations&#x60; when there were more locations than could fit in the requested page size. | [optional] 
 **readMask** | **String**| Required. Read mask to specify what fields will be returned in the response. | [optional] 

### Return type

[**ListLocationsResponse**](ListLocationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

