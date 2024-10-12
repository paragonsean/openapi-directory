# PaymentsGatewayApi.ConfigurationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**affiliationById**](ConfigurationApi.md#affiliationById) | **GET** /api/pvt/affiliations/{affiliationId} | Affiliation By Id
[**affiliations**](ConfigurationApi.md#affiliations) | **GET** /api/pvt/affiliations | Affiliations
[**availablePaymentMethods**](ConfigurationApi.md#availablePaymentMethods) | **GET** /api/pvt/merchants/payment-systems | Available Payment Methods
[**insertAffiliation**](ConfigurationApi.md#insertAffiliation) | **POST** /api/pvt/affiliations | Insert Affiliation
[**insertRule**](ConfigurationApi.md#insertRule) | **POST** /api/pvt/rules | Insert Rule
[**putRuleById**](ConfigurationApi.md#putRuleById) | **PUT** /api/pvt/rules/{ruleId} | Rule By Id
[**rule**](ConfigurationApi.md#rule) | **DELETE** /api/pvt/rules/{ruleId} | Delete Rule
[**ruleById**](ConfigurationApi.md#ruleById) | **GET** /api/pvt/rules/{ruleId} | Rule By Id
[**rules**](ConfigurationApi.md#rules) | **GET** /api/pvt/rules | Rules
[**updateAffiliation**](ConfigurationApi.md#updateAffiliation) | **PUT** /api/pvt/affiliations/{affiliationId} | Update Affiliation



## affiliationById

> affiliationById(affiliationId, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept)

Affiliation By Id

Returns associated data for the specified affiliation Id, like name and implementation, for example.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let affiliationId = "e046d326-5421-45ab-95ae-f13d37f260b5"; // String | 
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
apiInstance.affiliationById(affiliationId, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, (error, data, response) => {
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
 **affiliationId** | **String**|  | 
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## affiliations

> affiliations(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept)

Affiliations

Returns all affiliations that your provider can handle.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
apiInstance.affiliations(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## availablePaymentMethods

> [PaymentSystemsResponse] availablePaymentMethods(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept)

Available Payment Methods

Returns enabled payment methods, like visa, master, bankissueinvoice that are shown for the final user and enabled to receive payment.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
apiInstance.availablePaymentMethods(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 

### Return type

[**[PaymentSystemsResponse]**](PaymentSystemsResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## insertAffiliation

> insertAffiliation(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, insertAffiliationRequest)

Insert Affiliation

Creates a new affiliation and returns a successful response.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let insertAffiliationRequest = {"configuration":[{"name":"HowTo","value":"https://developercielo.github.io/Habilitacao-meios-de-pagamento/"},{"name":"MerchantId","value":"sampleData"},{"name":"MerchantKey","value":"sampleData"},{"name":"softDescriptor","value":"teste"},{"name":"bankInvoiceProvider","value":"Disabled"},{"name":"bankIDebitProvider","value":"Disabled"},{"name":"useEarlySecurityCapture","value":"0"},{"name":"isProduction","value":"false"},{"name":"bankDebitProvider","value":"Disabled"},{"name":"Registered","value":"false"}],"implementation":"Vtex.PaymentGateway.Connectors.CieloV3Connector","isConfigured":true,"isdelivered":true,"name":"CieloV3 - Teste Ellen"}; // InsertAffiliationRequest | 
apiInstance.insertAffiliation(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, insertAffiliationRequest, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **insertAffiliationRequest** | [**InsertAffiliationRequest**](InsertAffiliationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## insertRule

> insertRule(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, insertRuleRequest)

Insert Rule

Creates a new rule and returns a successful response.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let insertRuleRequest = {"antifraud":{"affiliationId":null,"implementation":null},"beginDate":null,"condition":null,"connector":{"affiliationId":"e046d326-5421-45ab-95ae-f13d37f260b5","implementation":"Vtex.PaymentGateway.Connectors.PromissoryConnector"},"country":null,"dateIntervals":null,"enabled":true,"endDate":null,"installmentOptions":null,"installmentsService":null,"isDefault":false,"isSelfAuthorized":null,"issuer":{"name":null},"multiMerchantList":null,"name":"Cash - Custom","paymentSystem":{"id":47,"implementation":null,"name":"Cash"},"requiresAuthentication":null,"salesChannels":[{"id":":ALL:"}]}; // InsertRuleRequest | 
apiInstance.insertRule(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, insertRuleRequest, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **insertRuleRequest** | [**InsertRuleRequest**](InsertRuleRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putRuleById

> putRuleById(accept, contentType, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, ruleId, ruleByIdRequest)

Rule By Id

Update Rule.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let ruleId = "ruleId_example"; // String | 
let ruleByIdRequest = {"antifraud":{"affiliationId":"f952588c-8b41-41cc-a06f-c0f48f7320ef"},"beginDate":"0001-01-01T00:00:00","condition":null,"connector":{"affiliationId":"d0d7097e-0959-43dc-b335-852eda7b2992","implementation":"Vtex.PaymentGateway.Connectors.MundipaggConnector"},"country":null,"dateIntervals":null,"enabled":true,"endDate":"9999-12-31T23:59:59.9999999","id":"eff4f368-b671-443b-b5a9-82616e87ea1c","installmentOptions":{"interestRateMethod":null},"isDefault":null,"isSelfAuthorized":null,"issuer":{"name":null},"multiMerchantList":null,"name":"Visa gatewayqa","paymentSystem":{"id":2,"implementation":null,"name":"Visa"},"salesChannels":[{"id":"2"}]}; // RuleByIdRequest | 
apiInstance.putRuleById(accept, contentType, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, ruleId, ruleByIdRequest, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **ruleId** | **String**|  | 
 **ruleByIdRequest** | [**RuleByIdRequest**](RuleByIdRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## rule

> rule(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, ruleId)

Delete Rule

Deletes rules by specified Id.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let ruleId = "ruleId_example"; // String | 
apiInstance.rule(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, ruleId, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **ruleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ruleById

> ruleById(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, ruleId)

Rule By Id

Returns rule by specified RuleId.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let ruleId = "ruleId_example"; // String | 
apiInstance.ruleById(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, ruleId, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **ruleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## rules

> rules(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept)

Rules

Returns all rules conditions your provider can handle.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
apiInstance.rules(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateAffiliation

> updateAffiliation(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, affiliationId, updateAffiliationRequest)

Update Affiliation

Returns all affiliations.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.ConfigurationApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let affiliationId = "e046d326-5421-45ab-95ae-f13d37f260b5"; // String | 
let updateAffiliationRequest = {"configuration":[{"name":"HowTo","value":"https://developercielo.github.io/Habilitacao-meios-de-pagamento/"},{"name":"MerchantId","value":"DATA TEST"},{"name":"MerchantKey","value":"DATA TEST"},{"name":"softDescriptor","value":"teste"},{"name":"bankInvoiceProvider","value":"Disabled"},{"name":"bankIDebitProvider","value":"Disabled"},{"name":"useEarlySecurityCapture","value":"0"},{"name":"isProduction","value":"false"},{"name":"bankDebitProvider","value":"Disabled"},{"name":"Registered","value":"false"}],"id":"61c3b25b-554d-41a4-b989-a0ba215e4bba","implementation":"Vtex.PaymentGateway.Connectors.CieloV3Connector","isConfigured":true,"isdelivered":true,"name":"CieloV3 - Teste Ellen"}; // UpdateAffiliationRequest | 
apiInstance.updateAffiliation(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, affiliationId, updateAffiliationRequest, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **affiliationId** | **String**|  | 
 **updateAffiliationRequest** | [**UpdateAffiliationRequest**](UpdateAffiliationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

