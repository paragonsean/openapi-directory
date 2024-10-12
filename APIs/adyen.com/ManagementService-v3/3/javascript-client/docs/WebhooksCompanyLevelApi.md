# ManagementApi.WebhooksCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCompaniesCompanyIdWebhooksWebhookId**](WebhooksCompanyLevelApi.md#deleteCompaniesCompanyIdWebhooksWebhookId) | **DELETE** /companies/{companyId}/webhooks/{webhookId} | Remove a webhook
[**getCompaniesCompanyIdWebhooks**](WebhooksCompanyLevelApi.md#getCompaniesCompanyIdWebhooks) | **GET** /companies/{companyId}/webhooks | List all webhooks
[**getCompaniesCompanyIdWebhooksWebhookId**](WebhooksCompanyLevelApi.md#getCompaniesCompanyIdWebhooksWebhookId) | **GET** /companies/{companyId}/webhooks/{webhookId} | Get a webhook
[**patchCompaniesCompanyIdWebhooksWebhookId**](WebhooksCompanyLevelApi.md#patchCompaniesCompanyIdWebhooksWebhookId) | **PATCH** /companies/{companyId}/webhooks/{webhookId} | Update a webhook
[**postCompaniesCompanyIdWebhooks**](WebhooksCompanyLevelApi.md#postCompaniesCompanyIdWebhooks) | **POST** /companies/{companyId}/webhooks | Set up a webhook
[**postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac**](WebhooksCompanyLevelApi.md#postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac) | **POST** /companies/{companyId}/webhooks/{webhookId}/generateHmac | Generate an HMAC key
[**postCompaniesCompanyIdWebhooksWebhookIdTest**](WebhooksCompanyLevelApi.md#postCompaniesCompanyIdWebhooksWebhookIdTest) | **POST** /companies/{companyId}/webhooks/{webhookId}/test | Test a webhook



## deleteCompaniesCompanyIdWebhooksWebhookId

> deleteCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId)

Remove a webhook

Remove the configuration for the webhook identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.WebhooksCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
apiInstance.deleteCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **webhookId** | **String**| Unique identifier of the webhook configuration. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdWebhooks

> ListWebhooksResponse getCompaniesCompanyIdWebhooks(companyId, opts)

List all webhooks

Lists all webhook configurations for the company account.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read * Management API—Webhooks read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.WebhooksCompanyLevelApi();
let companyId = "companyId_example"; // String | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56 // Number | The number of items to have on a page, maximum 100. The default is 10 items on a page.
};
apiInstance.getCompaniesCompanyIdWebhooks(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). | 
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 

### Return type

[**ListWebhooksResponse**](ListWebhooksResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdWebhooksWebhookId

> Webhook getCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId)

Get a webhook

Returns the configuration for the webhook identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read * Management API—Webhooks read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.WebhooksCompanyLevelApi();
let companyId = "companyId_example"; // String | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
let webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
apiInstance.getCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId, (error, data, response) => {
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
 **companyId** | **String**| Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). | 
 **webhookId** | **String**| Unique identifier of the webhook configuration. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchCompaniesCompanyIdWebhooksWebhookId

> Webhook patchCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId, opts)

Update a webhook

Make changes to the configuration of the webhook identified in the path. The request contains the new values you want to have in the webhook configuration. The response contains the full configuration for the webhook, which includes the new values from the request.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.WebhooksCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
let opts = {
  'updateCompanyWebhookRequest': new ManagementApi.UpdateCompanyWebhookRequest() // UpdateCompanyWebhookRequest | 
};
apiInstance.patchCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **webhookId** | **String**| Unique identifier of the webhook configuration. | 
 **updateCompanyWebhookRequest** | [**UpdateCompanyWebhookRequest**](UpdateCompanyWebhookRequest.md)|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCompaniesCompanyIdWebhooks

> Webhook postCompaniesCompanyIdWebhooks(companyId, opts)

Set up a webhook

Subscribe to receive webhook notifications about events related to your company account. You can add basic authentication to make sure the data is secure.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.WebhooksCompanyLevelApi();
let companyId = "companyId_example"; // String | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
let opts = {
  'createCompanyWebhookRequest': new ManagementApi.CreateCompanyWebhookRequest() // CreateCompanyWebhookRequest | 
};
apiInstance.postCompaniesCompanyIdWebhooks(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). | 
 **createCompanyWebhookRequest** | [**CreateCompanyWebhookRequest**](CreateCompanyWebhookRequest.md)|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac

> GenerateHmacKeyResponse postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac(companyId, webhookId)

Generate an HMAC key

Returns an [HMAC key](https://en.wikipedia.org/wiki/HMAC) for the webhook identified in the path. This key allows you to check the integrity and the origin of the notifications you receive.By creating an HMAC key, you start receiving [HMAC-signed notifications](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures#enable-hmac-signatures) from Adyen. Find out more about how to [verify HMAC signatures](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures).  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.WebhooksCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
apiInstance.postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac(companyId, webhookId, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **webhookId** | **String**| Unique identifier of the webhook configuration. | 

### Return type

[**GenerateHmacKeyResponse**](GenerateHmacKeyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postCompaniesCompanyIdWebhooksWebhookIdTest

> TestWebhookResponse postCompaniesCompanyIdWebhooksWebhookIdTest(companyId, webhookId, opts)

Test a webhook

Sends sample notifications to test if the webhook is set up correctly.  We send sample notifications for maximum 20 of the merchant accounts that the webhook is configured for. If the webhook is configured for more than 20 merchant accounts, use the &#x60;merchantIds&#x60; array to specify a subset of the merchant accounts for which to send test notifications.  We send four test notifications for each event code you choose. They cover success and failure scenarios for the hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom notifications, we only send the specified custom notification.  The response describes the result of the test. The &#x60;status&#x60; field tells you if the test was successful or not. You can use the other response fields to troubleshoot unsuccessful tests.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.WebhooksCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
let opts = {
  'testCompanyWebhookRequest': new ManagementApi.TestCompanyWebhookRequest() // TestCompanyWebhookRequest | 
};
apiInstance.postCompaniesCompanyIdWebhooksWebhookIdTest(companyId, webhookId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **webhookId** | **String**| Unique identifier of the webhook configuration. | 
 **testCompanyWebhookRequest** | [**TestCompanyWebhookRequest**](TestCompanyWebhookRequest.md)|  | [optional] 

### Return type

[**TestWebhookResponse**](TestWebhookResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

