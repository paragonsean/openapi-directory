# Apacta.CompaniesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet**](CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet) | **GET** /companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id} | View a company integration feature setting
[**companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut**](CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut) | **PUT** /companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id} | Edit a company integration feature setting
[**companiesCompanyIdCompaniesIntegrationFeatureSettingsGet**](CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsGet) | **GET** /companies/{company_id}/companies_integration_feature_settings | List a company integration feature settings
[**companiesCompanyIdCompaniesIntegrationFeatureSettingsPost**](CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsPost) | **POST** /companies/{company_id}/companies_integration_feature_settings | Add a company integration feature setting
[**companiesCompanyIdFormTemplatesFormTemplateIdDelete**](CompaniesApi.md#companiesCompanyIdFormTemplatesFormTemplateIdDelete) | **DELETE** /companies/{company_id}/form_templates/{form_template_id} | Delete a form template company
[**companiesCompanyIdFormTemplatesFormTemplateIdGet**](CompaniesApi.md#companiesCompanyIdFormTemplatesFormTemplateIdGet) | **GET** /companies/{company_id}/form_templates/{form_template_id} | Get a company form template
[**companiesCompanyIdFormTemplatesGet**](CompaniesApi.md#companiesCompanyIdFormTemplatesGet) | **GET** /companies/{company_id}/form_templates/ | Get a list of company form templates
[**companiesCompanyIdGet**](CompaniesApi.md#companiesCompanyIdGet) | **GET** /companies/{company_id} | Details of 1 company
[**companiesCompanyIdIntegrationFeatureSettingsGet**](CompaniesApi.md#companiesCompanyIdIntegrationFeatureSettingsGet) | **GET** /companies/{company_id}/integration_feature_settings | Get a list of integration feature settings
[**companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet**](CompaniesApi.md#companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet) | **GET** /companies/{company_id}/integration_feature_settings/{integration_feature_setting_id} | Show details of 1 integration feature setting
[**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete) | **DELETE** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Delete a company integration setting
[**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet) | **GET** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Get a company integration setting
[**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut) | **PUT** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Edit a company integration setting
[**companiesCompanyIdIntegrationSettingsGet**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsGet) | **GET** /companies/{company_id}/integration_settings | Get a list of company integration settings
[**companiesCompanyIdIntegrationSettingsPost**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsPost) | **POST** /companies/{company_id}/integration_settings | Add a company integration setting
[**companiesCompanyIdPriceMarginsPriceMarginsIdDelete**](CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdDelete) | **DELETE** /companies/{company_id}/price_margins/{price_margins_id} | Delete a company price margin
[**companiesCompanyIdPriceMarginsPriceMarginsIdGet**](CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdGet) | **GET** /companies/{company_id}/price_margins/{price_margins_id} | Get a list of company price margins
[**companiesCompanyIdPriceMarginsPriceMarginsIdPost**](CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdPost) | **POST** /companies/{company_id}/price_margins/{price_margins_id} | Add a company price margin
[**companiesGet**](CompaniesApi.md#companiesGet) | **GET** /companies | Get a list of companies
[**companiesSubscriptionSelfServiceGet**](CompaniesApi.md#companiesSubscriptionSelfServiceGet) | **GET** /companies/subscription_self_service | URL for subscription selfservice



## companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet

> CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(companyId, cIntegrationFeatureSettingId)

View a company integration feature setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let cIntegrationFeatureSettingId = "cIntegrationFeatureSettingId_example"; // String | 
apiInstance.companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(companyId, cIntegrationFeatureSettingId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **cIntegrationFeatureSettingId** | **String**|  | 

### Return type

[**CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response**](CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut

> CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(companyId, cIntegrationFeatureSettingId)

Edit a company integration feature setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let cIntegrationFeatureSettingId = "cIntegrationFeatureSettingId_example"; // String | 
apiInstance.companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(companyId, cIntegrationFeatureSettingId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **cIntegrationFeatureSettingId** | **String**|  | 

### Return type

[**CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response**](CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdCompaniesIntegrationFeatureSettingsGet

> CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(companyId)

List a company integration feature settings

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
apiInstance.companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(companyId, (error, data, response) => {
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
 **companyId** | **String**|  | 

### Return type

[**CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response**](CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdCompaniesIntegrationFeatureSettingsPost

> CreateSuccessResponse companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(companyId, opts)

Add a company integration feature setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let opts = {
  'companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest': new Apacta.CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest() // CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest | 
};
apiInstance.companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest** | [**CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest**](CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest.md)|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companiesCompanyIdFormTemplatesFormTemplateIdDelete

> EmptySuccessResponse companiesCompanyIdFormTemplatesFormTemplateIdDelete(companyId, formTemplateId)

Delete a form template company

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let formTemplateId = "formTemplateId_example"; // String | Automatically added
apiInstance.companiesCompanyIdFormTemplatesFormTemplateIdDelete(companyId, formTemplateId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **formTemplateId** | **String**| Automatically added | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdFormTemplatesFormTemplateIdGet

> CompaniesCompanyIdFormTemplatesGet200Response companiesCompanyIdFormTemplatesFormTemplateIdGet(companyId, id, formTemplateId)

Get a company form template

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let id = "id_example"; // String | 
let formTemplateId = "formTemplateId_example"; // String | Automatically added
apiInstance.companiesCompanyIdFormTemplatesFormTemplateIdGet(companyId, id, formTemplateId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **id** | **String**|  | 
 **formTemplateId** | **String**| Automatically added | 

### Return type

[**CompaniesCompanyIdFormTemplatesGet200Response**](CompaniesCompanyIdFormTemplatesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdFormTemplatesGet

> CompaniesCompanyIdFormTemplatesGet200Response companiesCompanyIdFormTemplatesGet(companyId, formTemplateId)

Get a list of company form templates

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let formTemplateId = "formTemplateId_example"; // String | 
apiInstance.companiesCompanyIdFormTemplatesGet(companyId, formTemplateId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **formTemplateId** | **String**|  | 

### Return type

[**CompaniesCompanyIdFormTemplatesGet200Response**](CompaniesCompanyIdFormTemplatesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdGet

> CompaniesCompanyIdGet200Response companiesCompanyIdGet(companyId)

Details of 1 company

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
apiInstance.companiesCompanyIdGet(companyId, (error, data, response) => {
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
 **companyId** | **String**|  | 

### Return type

[**CompaniesCompanyIdGet200Response**](CompaniesCompanyIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdIntegrationFeatureSettingsGet

> CompaniesCompanyIdIntegrationFeatureSettingsGet200Response companiesCompanyIdIntegrationFeatureSettingsGet(companyId)

Get a list of integration feature settings

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
apiInstance.companiesCompanyIdIntegrationFeatureSettingsGet(companyId, (error, data, response) => {
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
 **companyId** | **String**|  | 

### Return type

[**CompaniesCompanyIdIntegrationFeatureSettingsGet200Response**](CompaniesCompanyIdIntegrationFeatureSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet

> CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(companyId, integrationFeatureSettingId)

Show details of 1 integration feature setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let integrationFeatureSettingId = "integrationFeatureSettingId_example"; // String | 
apiInstance.companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(companyId, integrationFeatureSettingId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **integrationFeatureSettingId** | **String**|  | 

### Return type

[**CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response**](CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete

> EmptySuccessResponse companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(companyId, companiesIntegrationSettingId)

Delete a company integration setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let companiesIntegrationSettingId = "companiesIntegrationSettingId_example"; // String | 
apiInstance.companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(companyId, companiesIntegrationSettingId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **companiesIntegrationSettingId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet

> CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(companyId, companiesIntegrationSettingId)

Get a company integration setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let companiesIntegrationSettingId = "companiesIntegrationSettingId_example"; // String | 
apiInstance.companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(companyId, companiesIntegrationSettingId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **companiesIntegrationSettingId** | **String**|  | 

### Return type

[**CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response**](CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut

> EmptySuccessResponse companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(companyId, companiesIntegrationSettingId)

Edit a company integration setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let companiesIntegrationSettingId = "companiesIntegrationSettingId_example"; // String | 
apiInstance.companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(companyId, companiesIntegrationSettingId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **companiesIntegrationSettingId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdIntegrationSettingsGet

> CompaniesCompanyIdIntegrationSettingsGet200Response companiesCompanyIdIntegrationSettingsGet(companyId, opts)

Get a list of company integration settings

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let opts = {
  'identifier': "identifier_example" // String | The identifier of an ERP integration
};
apiInstance.companiesCompanyIdIntegrationSettingsGet(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **identifier** | **String**| The identifier of an ERP integration | [optional] 

### Return type

[**CompaniesCompanyIdIntegrationSettingsGet200Response**](CompaniesCompanyIdIntegrationSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdIntegrationSettingsPost

> CreateSuccessResponse companiesCompanyIdIntegrationSettingsPost(companyId, opts)

Add a company integration setting

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let opts = {
  'companiesCompanyIdIntegrationSettingsPostRequest': new Apacta.CompaniesCompanyIdIntegrationSettingsPostRequest() // CompaniesCompanyIdIntegrationSettingsPostRequest | 
};
apiInstance.companiesCompanyIdIntegrationSettingsPost(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **companiesCompanyIdIntegrationSettingsPostRequest** | [**CompaniesCompanyIdIntegrationSettingsPostRequest**](CompaniesCompanyIdIntegrationSettingsPostRequest.md)|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companiesCompanyIdPriceMarginsPriceMarginsIdDelete

> EmptySuccessResponse companiesCompanyIdPriceMarginsPriceMarginsIdDelete(companyId, priceMarginId, priceMarginsId)

Delete a company price margin

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let priceMarginId = "priceMarginId_example"; // String | 
let priceMarginsId = "priceMarginsId_example"; // String | Automatically added
apiInstance.companiesCompanyIdPriceMarginsPriceMarginsIdDelete(companyId, priceMarginId, priceMarginsId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **priceMarginId** | **String**|  | 
 **priceMarginsId** | **String**| Automatically added | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdPriceMarginsPriceMarginsIdGet

> CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response companiesCompanyIdPriceMarginsPriceMarginsIdGet(companyId, priceMarginsId)

Get a list of company price margins

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let priceMarginsId = "priceMarginsId_example"; // String | Automatically added
apiInstance.companiesCompanyIdPriceMarginsPriceMarginsIdGet(companyId, priceMarginsId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **priceMarginsId** | **String**| Automatically added | 

### Return type

[**CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response**](CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesCompanyIdPriceMarginsPriceMarginsIdPost

> CreateSuccessResponse companiesCompanyIdPriceMarginsPriceMarginsIdPost(companyId, priceMarginsId, opts)

Add a company price margin

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
let companyId = "companyId_example"; // String | 
let priceMarginsId = "priceMarginsId_example"; // String | Automatically added
let opts = {
  'companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest': new Apacta.CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest() // CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest | 
};
apiInstance.companiesCompanyIdPriceMarginsPriceMarginsIdPost(companyId, priceMarginsId, opts, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **priceMarginsId** | **String**| Automatically added | 
 **companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest** | [**CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest**](CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest.md)|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companiesGet

> CompaniesGet200Response companiesGet()

Get a list of companies

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
apiInstance.companiesGet((error, data, response) => {
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

[**CompaniesGet200Response**](CompaniesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companiesSubscriptionSelfServiceGet

> CompaniesSubscriptionSelfServiceGet200Response companiesSubscriptionSelfServiceGet()

URL for subscription selfservice

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CompaniesApi();
apiInstance.companiesSubscriptionSelfServiceGet((error, data, response) => {
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

[**CompaniesSubscriptionSelfServiceGet200Response**](CompaniesSubscriptionSelfServiceGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

