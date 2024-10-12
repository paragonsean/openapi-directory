# AccountingApi.JournalEntriesApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journalEntriesAdd**](JournalEntriesApi.md#journalEntriesAdd) | **POST** /accounting/journal-entries | Create Journal Entry
[**journalEntriesAll**](JournalEntriesApi.md#journalEntriesAll) | **GET** /accounting/journal-entries | List Journal Entries
[**journalEntriesDelete**](JournalEntriesApi.md#journalEntriesDelete) | **DELETE** /accounting/journal-entries/{id} | Delete Journal Entry
[**journalEntriesOne**](JournalEntriesApi.md#journalEntriesOne) | **GET** /accounting/journal-entries/{id} | Get Journal Entry
[**journalEntriesUpdate**](JournalEntriesApi.md#journalEntriesUpdate) | **PATCH** /accounting/journal-entries/{id} | Update Journal Entry



## journalEntriesAdd

> CreateJournalEntryResponse journalEntriesAdd(xApideckConsumerId, xApideckAppId, journalEntry, opts)

Create Journal Entry

Create Journal Entry

### Example

```javascript
import AccountingApi from 'accounting_api';
let defaultClient = AccountingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new AccountingApi.JournalEntriesApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let journalEntry = new AccountingApi.JournalEntry(); // JournalEntry | 
let opts = {
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example" // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
};
apiInstance.journalEntriesAdd(xApideckConsumerId, xApideckAppId, journalEntry, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **journalEntry** | [**JournalEntry**](JournalEntry.md)|  | 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 

### Return type

[**CreateJournalEntryResponse**](CreateJournalEntryResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## journalEntriesAll

> GetJournalEntriesResponse journalEntriesAll(xApideckConsumerId, xApideckAppId, opts)

List Journal Entries

List Journal Entries

### Example

```javascript
import AccountingApi from 'accounting_api';
let defaultClient = AccountingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new AccountingApi.JournalEntriesApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 20, // Number | Number of results to return. Minimum 1, Maximum 200, Default 20
  'passThrough': {key: {"search":"San Francisco"}}, // PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
  'fields': "id,updated_at" // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
};
apiInstance.journalEntriesAll(xApideckConsumerId, xApideckAppId, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20]
 **passThrough** | [**PassThroughQuery**](Object.md)| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional] 
 **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] 

### Return type

[**GetJournalEntriesResponse**](GetJournalEntriesResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## journalEntriesDelete

> DeleteJournalEntryResponse journalEntriesDelete(id, xApideckConsumerId, xApideckAppId, opts)

Delete Journal Entry

Delete Journal Entry

### Example

```javascript
import AccountingApi from 'accounting_api';
let defaultClient = AccountingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new AccountingApi.JournalEntriesApi();
let id = "id_example"; // String | ID of the record you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false // Boolean | Include raw response. Mostly used for debugging purposes
};
apiInstance.journalEntriesDelete(id, xApideckConsumerId, xApideckAppId, opts, (error, data, response) => {
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
 **id** | **String**| ID of the record you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]

### Return type

[**DeleteJournalEntryResponse**](DeleteJournalEntryResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## journalEntriesOne

> GetJournalEntryResponse journalEntriesOne(id, xApideckConsumerId, xApideckAppId, opts)

Get Journal Entry

Get Journal Entry

### Example

```javascript
import AccountingApi from 'accounting_api';
let defaultClient = AccountingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new AccountingApi.JournalEntriesApi();
let id = "id_example"; // String | ID of the record you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'fields': "id,updated_at" // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
};
apiInstance.journalEntriesOne(id, xApideckConsumerId, xApideckAppId, opts, (error, data, response) => {
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
 **id** | **String**| ID of the record you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] 

### Return type

[**GetJournalEntryResponse**](GetJournalEntryResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## journalEntriesUpdate

> UpdateJournalEntryResponse journalEntriesUpdate(id, xApideckConsumerId, xApideckAppId, journalEntry, opts)

Update Journal Entry

Update Journal Entry

### Example

```javascript
import AccountingApi from 'accounting_api';
let defaultClient = AccountingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new AccountingApi.JournalEntriesApi();
let id = "id_example"; // String | ID of the record you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let journalEntry = new AccountingApi.JournalEntry(); // JournalEntry | 
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false // Boolean | Include raw response. Mostly used for debugging purposes
};
apiInstance.journalEntriesUpdate(id, xApideckConsumerId, xApideckAppId, journalEntry, opts, (error, data, response) => {
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
 **id** | **String**| ID of the record you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **journalEntry** | [**JournalEntry**](JournalEntry.md)|  | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]

### Return type

[**UpdateJournalEntryResponse**](UpdateJournalEntryResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

