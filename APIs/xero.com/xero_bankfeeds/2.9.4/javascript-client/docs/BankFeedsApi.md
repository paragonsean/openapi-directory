# XeroBankFeedsApi.BankFeedsApi

All URIs are relative to *https://api.xero.com/bankfeeds.xro/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFeedConnections**](BankFeedsApi.md#createFeedConnections) | **POST** /FeedConnections | Create one or more new feed connection
[**createStatements**](BankFeedsApi.md#createStatements) | **POST** /Statements | Creates one or more new statements
[**deleteFeedConnections**](BankFeedsApi.md#deleteFeedConnections) | **POST** /FeedConnections/DeleteRequests | Delete an existing feed connection
[**getFeedConnection**](BankFeedsApi.md#getFeedConnection) | **GET** /FeedConnections/{id} | Retrieve single feed connection based on a unique id provided
[**getFeedConnections**](BankFeedsApi.md#getFeedConnections) | **GET** /FeedConnections | Searches for feed connections
[**getStatement**](BankFeedsApi.md#getStatement) | **GET** /Statements/{statementID} | Retrieve single statement based on unique id provided
[**getStatements**](BankFeedsApi.md#getStatements) | **GET** /Statements | Retrieve all statements



## createFeedConnections

> FeedConnections createFeedConnections(xeroTenantId, feedConnections)

Create one or more new feed connection

By passing in the FeedConnections array object in the body, you can create one or more new feed connections

### Example

```javascript
import XeroBankFeedsApi from 'xero_bank_feeds_api';
let defaultClient = XeroBankFeedsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroBankFeedsApi.BankFeedsApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let feedConnections = {"items":[{"accountName":"SDK Bank 90861","accountNumber":"123458637","accountToken":"foobar71760","accountType":"BANK","currency":"GBP"}]}; // FeedConnections | Feed Connection(s) array object in the body
apiInstance.createFeedConnections(xeroTenantId, feedConnections, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **feedConnections** | [**FeedConnections**](FeedConnections.md)| Feed Connection(s) array object in the body | 

### Return type

[**FeedConnections**](FeedConnections.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStatements

> Statements createStatements(xeroTenantId, opts)

Creates one or more new statements

### Example

```javascript
import XeroBankFeedsApi from 'xero_bank_feeds_api';
let defaultClient = XeroBankFeedsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroBankFeedsApi.BankFeedsApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'statements': {"items":[{"endBalance":{"amount":"150","creditDebitIndicator":"CREDIT"},"endDate":"2019-08-11","feedConnectionId":"6a4b9ff5-3a5f-4321-936b-4796163550f6","startBalance":{"amount":"100","creditDebitIndicator":"CREDIT"},"startDate":"2019-08-11","statementLines":[{"amount":"50","chequeNumber":"12379009","creditDebitIndicator":"CREDIT","description":"My new line","payeeName":"StarLord90315","postedDate":"2019-08-11","reference":"Foobar95578","transactionId":"123446422"}]},{"endBalance":{"amount":"150","creditDebitIndicator":"CREDIT"},"endDate":"2019-08-11","feedConnectionId":"2ebe6393-f3bb-48ab-9a0e-b04fa8585a70","startBalance":{"amount":"100","creditDebitIndicator":"CREDIT"},"startDate":"2019-08-11","statementLines":[{"amount":"50","chequeNumber":"12379350","creditDebitIndicator":"CREDIT","description":"My new line","payeeName":"StarLord56705","postedDate":"2019-08-11","reference":"Foobar67355","transactionId":"123449402"}]}]} // Statements | Statements array of objects in the body
};
apiInstance.createStatements(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **statements** | [**Statements**](Statements.md)| Statements array of objects in the body | [optional] 

### Return type

[**Statements**](Statements.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## deleteFeedConnections

> FeedConnections deleteFeedConnections(xeroTenantId, feedConnections)

Delete an existing feed connection

By passing in FeedConnections array object in the body, you can delete a feed connection.

### Example

```javascript
import XeroBankFeedsApi from 'xero_bank_feeds_api';
let defaultClient = XeroBankFeedsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroBankFeedsApi.BankFeedsApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let feedConnections = {"items":[{"id":"b4cc693b-24d9-42ec-a6d4-2943d253ff63"}]}; // FeedConnections | Feed Connections array object in the body
apiInstance.deleteFeedConnections(xeroTenantId, feedConnections, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **feedConnections** | [**FeedConnections**](FeedConnections.md)| Feed Connections array object in the body | 

### Return type

[**FeedConnections**](FeedConnections.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getFeedConnection

> FeedConnection getFeedConnection(xeroTenantId, id)

Retrieve single feed connection based on a unique id provided

By passing in a FeedConnection Id options, you can search for matching feed connections

### Example

```javascript
import XeroBankFeedsApi from 'xero_bank_feeds_api';
let defaultClient = XeroBankFeedsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroBankFeedsApi.BankFeedsApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let id = "id_example"; // String | Unique identifier for retrieving single object
apiInstance.getFeedConnection(xeroTenantId, id, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **id** | **String**| Unique identifier for retrieving single object | 

### Return type

[**FeedConnection**](FeedConnection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFeedConnections

> FeedConnections getFeedConnections(xeroTenantId, opts)

Searches for feed connections

By passing in the appropriate options, you can search for available feed connections in the system.

### Example

```javascript
import XeroBankFeedsApi from 'xero_bank_feeds_api';
let defaultClient = XeroBankFeedsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroBankFeedsApi.BankFeedsApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'page': 1, // Number | Page number which specifies the set of records to retrieve. By default the number of the records per set is 10. Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?page=1 to get the second set of the records. When page value is not a number or a negative number, by default, the first set of records is returned.
  'pageSize': 100 // Number | Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?pageSize=100 to specify page size of 100.
};
apiInstance.getFeedConnections(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **page** | **Number**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 10. Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?page&#x3D;1 to get the second set of the records. When page value is not a number or a negative number, by default, the first set of records is returned. | [optional] 
 **pageSize** | **Number**| Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?pageSize&#x3D;100 to specify page size of 100. | [optional] 

### Return type

[**FeedConnections**](FeedConnections.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStatement

> Statement getStatement(xeroTenantId, statementId, statementID)

Retrieve single statement based on unique id provided

By passing in a statement id, you can search for matching statements

### Example

```javascript
import XeroBankFeedsApi from 'xero_bank_feeds_api';
let defaultClient = XeroBankFeedsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroBankFeedsApi.BankFeedsApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let statementId = "statementId_example"; // String | statement id for single object
let statementID = "statementID_example"; // String | 
apiInstance.getStatement(xeroTenantId, statementId, statementID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **statementId** | **String**| statement id for single object | 
 **statementID** | **String**|  | 

### Return type

[**Statement**](Statement.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStatements

> Statements getStatements(xeroTenantId, opts)

Retrieve all statements

By passing in parameters, you can search for matching statements

### Example

```javascript
import XeroBankFeedsApi from 'xero_bank_feeds_api';
let defaultClient = XeroBankFeedsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroBankFeedsApi.BankFeedsApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'page': 56, // Number | unique id for single object
  'pageSize': 56, // Number | Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/Statements?pageSize=100 to specify page size of 100.
  'xeroApplicationId': "'00000000-0000-0000-0000-0000000010000'", // String | 
  'xeroUserId': "'00000000-0000-0000-0000-0000030000000'" // String | 
};
apiInstance.getStatements(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **page** | **Number**| unique id for single object | [optional] 
 **pageSize** | **Number**| Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/Statements?pageSize&#x3D;100 to specify page size of 100. | [optional] 
 **xeroApplicationId** | **String**|  | [optional] [default to &#39;00000000-0000-0000-0000-0000000010000&#39;]
 **xeroUserId** | **String**|  | [optional] [default to &#39;00000000-0000-0000-0000-0000030000000&#39;]

### Return type

[**Statements**](Statements.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

