# Id4iApi.HistoryApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addItem**](HistoryApi.md#addItem) | **POST** /api/v1/history/{id4n} | Add history item
[**filteredList**](HistoryApi.md#filteredList) | **GET** /api/v1/history/{id4n} | List history
[**list**](HistoryApi.md#list) | **GET** /api/v1/history/{id4n}/{organizationId} | DEPRECATED - List history
[**retrieveItem**](HistoryApi.md#retrieveItem) | **GET** /api/v1/history/{id4n}/{organizationId}/{sequenceId} | Get history item
[**updateItem**](HistoryApi.md#updateItem) | **PATCH** /api/v1/history/{id4n}/{organizationId}/{sequenceId} | Update history item
[**updateItemVisibility**](HistoryApi.md#updateItemVisibility) | **PUT** /api/v1/history/{id4n}/{organizationId}/{sequenceId}/visibility | Set history item visibility



## addItem

> addItem(id4n, historyItem)

Add history item

Add a new history item

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.HistoryApi();
let id4n = "id4n_example"; // String | GUID to retrieve the history for
let historyItem = new Id4iApi.HistoryItem(); // HistoryItem | The history item to publish
apiInstance.addItem(id4n, historyItem, (error, data, response) => {
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
 **id4n** | **String**| GUID to retrieve the history for | 
 **historyItem** | [**HistoryItem**](HistoryItem.md)| The history item to publish | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## filteredList

> PaginatedResponseOfHistoryItem filteredList(id4n, opts)

List history

Lists the history of a GUID

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.HistoryApi();
let id4n = "id4n_example"; // String | GUID to retrieve the history for
let opts = {
  'includePrivate': true, // Boolean | Also return private history entries
  'organization': "organization_example", // String | Show only entries created by one of the given organizations. This parameter can be used multiple times.
  'type': ["null"], // [String] | Show only entries matching one of the given history item types. This parameter can be used multiple times.
  'qualifier': ["null"], // [String] | Show only entries matching one of the given history item qualifiers (additional property de.id4i.history.item.qualifier). This parameter can be used multiple times.
  'fromDate': new Date("2013-10-20T19:20:30+01:00"), // Date | From date time as UTC Date-Time format
  'toDate': new Date("2013-10-20T19:20:30+01:00"), // Date | To date time as UTC Date-Time format
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.filteredList(id4n, opts, (error, data, response) => {
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
 **id4n** | **String**| GUID to retrieve the history for | 
 **includePrivate** | **Boolean**| Also return private history entries | [optional] [default to true]
 **organization** | **String**| Show only entries created by one of the given organizations. This parameter can be used multiple times. | [optional] 
 **type** | [**[String]**](String.md)| Show only entries matching one of the given history item types. This parameter can be used multiple times. | [optional] 
 **qualifier** | [**[String]**](String.md)| Show only entries matching one of the given history item qualifiers (additional property de.id4i.history.item.qualifier). This parameter can be used multiple times. | [optional] 
 **fromDate** | **Date**| From date time as UTC Date-Time format | [optional] 
 **toDate** | **Date**| To date time as UTC Date-Time format | [optional] 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfHistoryItem**](PaginatedResponseOfHistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## list

> PaginatedResponseOfHistoryItem list(id4n, organizationId, opts)

DEPRECATED - List history

DEPRECATED - please use filteredList with organization parameter to achieve the same functionality

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.HistoryApi();
let id4n = "id4n_example"; // String | GUID to retrieve the history for
let organizationId = "organizationId_example"; // String | organizationId
let opts = {
  'includePrivate': true, // Boolean | Also return private history entries
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.list(id4n, organizationId, opts, (error, data, response) => {
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
 **id4n** | **String**| GUID to retrieve the history for | 
 **organizationId** | **String**| organizationId | 
 **includePrivate** | **Boolean**| Also return private history entries | [optional] [default to true]
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfHistoryItem**](PaginatedResponseOfHistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## retrieveItem

> HistoryItem retrieveItem(id4n, organizationId, sequenceId)

Get history item

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.HistoryApi();
let id4n = "id4n_example"; // String | GUID to retrieve the history for
let organizationId = "organizationId_example"; // String | organizationId
let sequenceId = 56; // Number | sequenceId
apiInstance.retrieveItem(id4n, organizationId, sequenceId, (error, data, response) => {
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
 **id4n** | **String**| GUID to retrieve the history for | 
 **organizationId** | **String**| organizationId | 
 **sequenceId** | **Number**| sequenceId | 

### Return type

[**HistoryItem**](HistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateItem

> HistoryItem updateItem(id4n, organizationId, sequenceId, historyItemUpdate)

Update history item

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.HistoryApi();
let id4n = "id4n_example"; // String | GUID to retrieve the history for
let organizationId = "organizationId_example"; // String | organizationId
let sequenceId = 56; // Number | sequenceId
let historyItemUpdate = new Id4iApi.HistoryItemUpdate(); // HistoryItemUpdate | update
apiInstance.updateItem(id4n, organizationId, sequenceId, historyItemUpdate, (error, data, response) => {
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
 **id4n** | **String**| GUID to retrieve the history for | 
 **organizationId** | **String**| organizationId | 
 **sequenceId** | **Number**| sequenceId | 
 **historyItemUpdate** | [**HistoryItemUpdate**](HistoryItemUpdate.md)| update | 

### Return type

[**HistoryItem**](HistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## updateItemVisibility

> HistoryItem updateItemVisibility(id4n, organizationId, sequenceId, visibility)

Set history item visibility

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.HistoryApi();
let id4n = "id4n_example"; // String | GUID to retrieve the history for
let organizationId = "organizationId_example"; // String | organizationId
let sequenceId = 56; // Number | sequenceId
let visibility = new Id4iApi.Visibility(); // Visibility | History item visibility restrictions
apiInstance.updateItemVisibility(id4n, organizationId, sequenceId, visibility, (error, data, response) => {
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
 **id4n** | **String**| GUID to retrieve the history for | 
 **organizationId** | **String**| organizationId | 
 **sequenceId** | **Number**| sequenceId | 
 **visibility** | [**Visibility**](Visibility.md)| History item visibility restrictions | 

### Return type

[**HistoryItem**](HistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

