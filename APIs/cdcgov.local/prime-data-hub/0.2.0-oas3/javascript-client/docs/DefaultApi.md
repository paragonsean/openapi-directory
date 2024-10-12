# PrimeReportStream.DefaultApi

All URIs are relative to *http://cdcgov.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsPost**](DefaultApi.md#reportsPost) | **POST** /reports | Post a report to the data hub
[**settingsOrganizationsGet**](DefaultApi.md#settingsOrganizationsGet) | **GET** /settings/organizations | 
[**settingsOrganizationsHead**](DefaultApi.md#settingsOrganizationsHead) | **HEAD** /settings/organizations | 
[**settingsOrganizationsOrganizationNameDelete**](DefaultApi.md#settingsOrganizationsOrganizationNameDelete) | **DELETE** /settings/organizations/{organizationName} | 
[**settingsOrganizationsOrganizationNameGet**](DefaultApi.md#settingsOrganizationsOrganizationNameGet) | **GET** /settings/organizations/{organizationName} | 
[**settingsOrganizationsOrganizationNamePut**](DefaultApi.md#settingsOrganizationsOrganizationNamePut) | **PUT** /settings/organizations/{organizationName} | 
[**settingsOrganizationsOrganizationNameReceiversGet**](DefaultApi.md#settingsOrganizationsOrganizationNameReceiversGet) | **GET** /settings/organizations/{organizationName}/receivers | 
[**settingsOrganizationsOrganizationNameReceiversReceiverNameDelete**](DefaultApi.md#settingsOrganizationsOrganizationNameReceiversReceiverNameDelete) | **DELETE** /settings/organizations/{organizationName}/receivers/{receiverName} | 
[**settingsOrganizationsOrganizationNameReceiversReceiverNameGet**](DefaultApi.md#settingsOrganizationsOrganizationNameReceiversReceiverNameGet) | **GET** /settings/organizations/{organizationName}/receivers/{receiverName} | 
[**settingsOrganizationsOrganizationNameReceiversReceiverNamePut**](DefaultApi.md#settingsOrganizationsOrganizationNameReceiversReceiverNamePut) | **PUT** /settings/organizations/{organizationName}/receivers/{receiverName} | 
[**settingsOrganizationsOrganizationNameSendersGet**](DefaultApi.md#settingsOrganizationsOrganizationNameSendersGet) | **GET** /settings/organizations/{organizationName}/senders | 
[**settingsOrganizationsOrganizationNameSendersSenderNameDelete**](DefaultApi.md#settingsOrganizationsOrganizationNameSendersSenderNameDelete) | **DELETE** /settings/organizations/{organizationName}/senders/{senderName} | 
[**settingsOrganizationsOrganizationNameSendersSenderNameGet**](DefaultApi.md#settingsOrganizationsOrganizationNameSendersSenderNameGet) | **GET** /settings/organizations/{organizationName}/senders/{senderName} | 
[**settingsOrganizationsOrganizationNameSendersSenderNamePut**](DefaultApi.md#settingsOrganizationsOrganizationNameSendersSenderNamePut) | **PUT** /settings/organizations/{organizationName}/senders/{senderName} | 



## reportsPost

> Report reportsPost(client, body, opts)

Post a report to the data hub

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new PrimeReportStream.DefaultApi();
let client = "simple_report"; // String | The client's name that matches the client name in metadata
let body = header1, header2
value1, value2; // String | The public health information being routed
let opts = {
  'option': "ValidatePayload", // String | Optional ways to process the request
  '_default': ["null"], // [String] | Dynamic default values for an element. ':' or %3A is used to seperate element name and value
  'routeTo': ["null"] // [String] | A comma speparated list of receiver names. Limit the list of possible receivers to these receivers.
};
apiInstance.reportsPost(client, body, opts, (error, data, response) => {
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
 **client** | **String**| The client&#39;s name that matches the client name in metadata | 
 **body** | **String**| The public health information being routed | 
 **option** | **String**| Optional ways to process the request | [optional] 
 **_default** | [**[String]**](String.md)| Dynamic default values for an element. &#39;:&#39; or %3A is used to seperate element name and value | [optional] 
 **routeTo** | [**[String]**](String.md)| A comma speparated list of receiver names. Limit the list of possible receivers to these receivers. | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: text/csv
- **Accept**: application/json


## settingsOrganizationsGet

> [Organization] settingsOrganizationsGet()



The settings for all organizations of the system. Must have admin access.

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
apiInstance.settingsOrganizationsGet((error, data, response) => {
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

[**[Organization]**](Organization.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsOrganizationsHead

> settingsOrganizationsHead()



Retrived the last modified for all settings of the system. Must have admin access.

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
apiInstance.settingsOrganizationsHead((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## settingsOrganizationsOrganizationNameDelete

> Organization settingsOrganizationsOrganizationNameDelete(organizationName)



Delete an organization (and the associated receivers and senders)

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "organizationName_example"; // String | The name of the organization
apiInstance.settingsOrganizationsOrganizationNameDelete(organizationName, (error, data, response) => {
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
 **organizationName** | **String**| The name of the organization | 

### Return type

[**Organization**](Organization.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsOrganizationsOrganizationNameGet

> Organization settingsOrganizationsOrganizationNameGet(organizationName)



A single organization settings

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "organizationName_example"; // String | The name of the organization
apiInstance.settingsOrganizationsOrganizationNameGet(organizationName, (error, data, response) => {
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
 **organizationName** | **String**| The name of the organization | 

### Return type

[**Organization**](Organization.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsOrganizationsOrganizationNamePut

> Organization settingsOrganizationsOrganizationNamePut(organizationName, opts)



Create or update the direct settings associated with an organization

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "organizationName_example"; // String | The name of the organization
let opts = {
  'organization': new PrimeReportStream.Organization() // Organization | 
};
apiInstance.settingsOrganizationsOrganizationNamePut(organizationName, opts, (error, data, response) => {
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
 **organizationName** | **String**| The name of the organization | 
 **organization** | [**Organization**](Organization.md)|  | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## settingsOrganizationsOrganizationNameReceiversGet

> [Receiver] settingsOrganizationsOrganizationNameReceiversGet(organizationName)



A list of receivers and their current settings

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "az-phd"; // String | Fetch receivers with this organization name
apiInstance.settingsOrganizationsOrganizationNameReceiversGet(organizationName, (error, data, response) => {
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
 **organizationName** | **String**| Fetch receivers with this organization name | 

### Return type

[**[Receiver]**](Receiver.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsOrganizationsOrganizationNameReceiversReceiverNameDelete

> Receiver settingsOrganizationsOrganizationNameReceiversReceiverNameDelete(organizationName, receiverName)



Delete a receiver

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "az-phd"; // String | the organization name
let receiverName = "elr"; // String | The name of the receiver
apiInstance.settingsOrganizationsOrganizationNameReceiversReceiverNameDelete(organizationName, receiverName, (error, data, response) => {
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
 **organizationName** | **String**| the organization name | 
 **receiverName** | **String**| The name of the receiver | 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsOrganizationsOrganizationNameReceiversReceiverNameGet

> Receiver settingsOrganizationsOrganizationNameReceiversReceiverNameGet(organizationName, receiverName)



The settings of a single of receiver

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "az-phd"; // String | Create receivers under this organization name
let receiverName = "elr"; // String | The name of the receiver
apiInstance.settingsOrganizationsOrganizationNameReceiversReceiverNameGet(organizationName, receiverName, (error, data, response) => {
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
 **organizationName** | **String**| Create receivers under this organization name | 
 **receiverName** | **String**| The name of the receiver | 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsOrganizationsOrganizationNameReceiversReceiverNamePut

> Receiver settingsOrganizationsOrganizationNameReceiversReceiverNamePut(organizationName, receiverName, opts)



Update a single reciever

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "az-phd"; // String | Create receivers under this organization name
let receiverName = "elr"; // String | The name of the receiver
let opts = {
  'receiver': new PrimeReportStream.Receiver() // Receiver | 
};
apiInstance.settingsOrganizationsOrganizationNameReceiversReceiverNamePut(organizationName, receiverName, opts, (error, data, response) => {
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
 **organizationName** | **String**| Create receivers under this organization name | 
 **receiverName** | **String**| The name of the receiver | 
 **receiver** | [**Receiver**](Receiver.md)|  | [optional] 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## settingsOrganizationsOrganizationNameSendersGet

> [Sender] settingsOrganizationsOrganizationNameSendersGet(organizationName)



A list of senders

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "az-phd"; // String | Fetch senders with this organization name
apiInstance.settingsOrganizationsOrganizationNameSendersGet(organizationName, (error, data, response) => {
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
 **organizationName** | **String**| Fetch senders with this organization name | 

### Return type

[**[Sender]**](Sender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsOrganizationsOrganizationNameSendersSenderNameDelete

> Sender settingsOrganizationsOrganizationNameSendersSenderNameDelete(organizationName, senderName)



Delete a sender

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "az-phd"; // String | the organization name
let senderName = "default"; // String | The name of a sender to the data hub
apiInstance.settingsOrganizationsOrganizationNameSendersSenderNameDelete(organizationName, senderName, (error, data, response) => {
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
 **organizationName** | **String**| the organization name | 
 **senderName** | **String**| The name of a sender to the data hub | 

### Return type

[**Sender**](Sender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsOrganizationsOrganizationNameSendersSenderNameGet

> Sender settingsOrganizationsOrganizationNameSendersSenderNameGet(organizationName, senderName)



The settings of a single of sender

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "az-phd"; // String | Fetch senders with this organization name
let senderName = "default"; // String | The name of a sender to the data hub
apiInstance.settingsOrganizationsOrganizationNameSendersSenderNameGet(organizationName, senderName, (error, data, response) => {
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
 **organizationName** | **String**| Fetch senders with this organization name | 
 **senderName** | **String**| The name of a sender to the data hub | 

### Return type

[**Sender**](Sender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsOrganizationsOrganizationNameSendersSenderNamePut

> [Sender] settingsOrganizationsOrganizationNameSendersSenderNamePut(organizationName, senderName, opts)



Update a single sender

### Example

```javascript
import PrimeReportStream from 'prime_report_stream';
let defaultClient = PrimeReportStream.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PrimeReportStream.DefaultApi();
let organizationName = "az-phd"; // String | Fetch senders with this organization name
let senderName = "default"; // String | The name of a sender to the data hub
let opts = {
  'sender': new PrimeReportStream.Sender() // Sender | 
};
apiInstance.settingsOrganizationsOrganizationNameSendersSenderNamePut(organizationName, senderName, opts, (error, data, response) => {
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
 **organizationName** | **String**| Fetch senders with this organization name | 
 **senderName** | **String**| The name of a sender to the data hub | 
 **sender** | [**Sender**](Sender.md)|  | [optional] 

### Return type

[**[Sender]**](Sender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

