# ManagementApi.WebhooksMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMerchantsMerchantIdWebhooksWebhookId**](WebhooksMerchantLevelApi.md#deleteMerchantsMerchantIdWebhooksWebhookId) | **DELETE** /merchants/{merchantId}/webhooks/{webhookId} | Remove a webhook
[**getMerchantsMerchantIdWebhooks**](WebhooksMerchantLevelApi.md#getMerchantsMerchantIdWebhooks) | **GET** /merchants/{merchantId}/webhooks | List all webhooks
[**getMerchantsMerchantIdWebhooksWebhookId**](WebhooksMerchantLevelApi.md#getMerchantsMerchantIdWebhooksWebhookId) | **GET** /merchants/{merchantId}/webhooks/{webhookId} | Get a webhook
[**patchMerchantsMerchantIdWebhooksWebhookId**](WebhooksMerchantLevelApi.md#patchMerchantsMerchantIdWebhooksWebhookId) | **PATCH** /merchants/{merchantId}/webhooks/{webhookId} | Update a webhook
[**postMerchantsMerchantIdWebhooks**](WebhooksMerchantLevelApi.md#postMerchantsMerchantIdWebhooks) | **POST** /merchants/{merchantId}/webhooks | Set up a webhook
[**postMerchantsMerchantIdWebhooksWebhookIdGenerateHmac**](WebhooksMerchantLevelApi.md#postMerchantsMerchantIdWebhooksWebhookIdGenerateHmac) | **POST** /merchants/{merchantId}/webhooks/{webhookId}/generateHmac | Generate an HMAC key
[**postMerchantsMerchantIdWebhooksWebhookIdTest**](WebhooksMerchantLevelApi.md#postMerchantsMerchantIdWebhooksWebhookIdTest) | **POST** /merchants/{merchantId}/webhooks/{webhookId}/test | Test a webhook



## deleteMerchantsMerchantIdWebhooksWebhookId

> deleteMerchantsMerchantIdWebhooksWebhookId(merchantId, webhookId)

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

let apiInstance = new ManagementApi.WebhooksMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
apiInstance.deleteMerchantsMerchantIdWebhooksWebhookId(merchantId, webhookId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **webhookId** | **String**| Unique identifier of the webhook configuration. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdWebhooks

> ListWebhooksResponse getMerchantsMerchantIdWebhooks(merchantId, opts)

List all webhooks

Lists all webhook configurations for the merchant account.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read * Management API—Webhooks read and write

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

let apiInstance = new ManagementApi.WebhooksMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56 // Number | The number of items to have on a page, maximum 100. The default is 10 items on a page.
};
apiInstance.getMerchantsMerchantIdWebhooks(merchantId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 

### Return type

[**ListWebhooksResponse**](ListWebhooksResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdWebhooksWebhookId

> Webhook getMerchantsMerchantIdWebhooksWebhookId(merchantId, webhookId)

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

let apiInstance = new ManagementApi.WebhooksMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
apiInstance.getMerchantsMerchantIdWebhooksWebhookId(merchantId, webhookId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **webhookId** | **String**| Unique identifier of the webhook configuration. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchMerchantsMerchantIdWebhooksWebhookId

> Webhook patchMerchantsMerchantIdWebhooksWebhookId(merchantId, webhookId, opts)

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

let apiInstance = new ManagementApi.WebhooksMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
let opts = {
  'updateMerchantWebhookRequest': new ManagementApi.UpdateMerchantWebhookRequest() // UpdateMerchantWebhookRequest | 
};
apiInstance.patchMerchantsMerchantIdWebhooksWebhookId(merchantId, webhookId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **webhookId** | **String**| Unique identifier of the webhook configuration. | 
 **updateMerchantWebhookRequest** | [**UpdateMerchantWebhookRequest**](UpdateMerchantWebhookRequest.md)|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdWebhooks

> Webhook postMerchantsMerchantIdWebhooks(merchantId, opts)

Set up a webhook

Subscribe to receive webhook notifications about events related to your merchant account. You can add basic authentication to make sure the data is secure.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

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

let apiInstance = new ManagementApi.WebhooksMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'createMerchantWebhookRequest': new ManagementApi.CreateMerchantWebhookRequest() // CreateMerchantWebhookRequest | 
};
apiInstance.postMerchantsMerchantIdWebhooks(merchantId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **createMerchantWebhookRequest** | [**CreateMerchantWebhookRequest**](CreateMerchantWebhookRequest.md)|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdWebhooksWebhookIdGenerateHmac

> GenerateHmacKeyResponse postMerchantsMerchantIdWebhooksWebhookIdGenerateHmac(merchantId, webhookId)

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

let apiInstance = new ManagementApi.WebhooksMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let webhookId = "webhookId_example"; // String | 
apiInstance.postMerchantsMerchantIdWebhooksWebhookIdGenerateHmac(merchantId, webhookId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **webhookId** | **String**|  | 

### Return type

[**GenerateHmacKeyResponse**](GenerateHmacKeyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postMerchantsMerchantIdWebhooksWebhookIdTest

> TestWebhookResponse postMerchantsMerchantIdWebhooksWebhookIdTest(merchantId, webhookId, opts)

Test a webhook

Sends sample notifications to test if the webhook is set up correctly.  We send four test notifications for each event code you choose. They cover success and failure scenarios for the hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom notifications, we only send the specified custom notification.  The response describes the result of the test. The &#x60;status&#x60; field tells you if the test was successful or not. You can use the other fields to troubleshoot unsuccessful tests.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

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

let apiInstance = new ManagementApi.WebhooksMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
let opts = {
  'testWebhookRequest': new ManagementApi.TestWebhookRequest() // TestWebhookRequest | 
};
apiInstance.postMerchantsMerchantIdWebhooksWebhookIdTest(merchantId, webhookId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **webhookId** | **String**| Unique identifier of the webhook configuration. | 
 **testWebhookRequest** | [**TestWebhookRequest**](TestWebhookRequest.md)|  | [optional] 

### Return type

[**TestWebhookResponse**](TestWebhookResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

