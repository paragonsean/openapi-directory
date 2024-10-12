# AwsAmplifyUiBuilder.DefaultApi

All URIs are relative to *http://amplifyuibuilder.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createComponent**](DefaultApi.md#createComponent) | **POST** /app/{appId}/environment/{environmentName}/components | 
[**createForm**](DefaultApi.md#createForm) | **POST** /app/{appId}/environment/{environmentName}/forms | 
[**createTheme**](DefaultApi.md#createTheme) | **POST** /app/{appId}/environment/{environmentName}/themes | 
[**deleteComponent**](DefaultApi.md#deleteComponent) | **DELETE** /app/{appId}/environment/{environmentName}/components/{id} | 
[**deleteForm**](DefaultApi.md#deleteForm) | **DELETE** /app/{appId}/environment/{environmentName}/forms/{id} | 
[**deleteTheme**](DefaultApi.md#deleteTheme) | **DELETE** /app/{appId}/environment/{environmentName}/themes/{id} | 
[**exchangeCodeForToken**](DefaultApi.md#exchangeCodeForToken) | **POST** /tokens/{provider} | 
[**exportComponents**](DefaultApi.md#exportComponents) | **GET** /export/app/{appId}/environment/{environmentName}/components | 
[**exportForms**](DefaultApi.md#exportForms) | **GET** /export/app/{appId}/environment/{environmentName}/forms | 
[**exportThemes**](DefaultApi.md#exportThemes) | **GET** /export/app/{appId}/environment/{environmentName}/themes | 
[**getCodegenJob**](DefaultApi.md#getCodegenJob) | **GET** /app/{appId}/environment/{environmentName}/codegen-jobs/{id} | 
[**getComponent**](DefaultApi.md#getComponent) | **GET** /app/{appId}/environment/{environmentName}/components/{id} | 
[**getForm**](DefaultApi.md#getForm) | **GET** /app/{appId}/environment/{environmentName}/forms/{id} | 
[**getMetadata**](DefaultApi.md#getMetadata) | **GET** /app/{appId}/environment/{environmentName}/metadata | 
[**getTheme**](DefaultApi.md#getTheme) | **GET** /app/{appId}/environment/{environmentName}/themes/{id} | 
[**listCodegenJobs**](DefaultApi.md#listCodegenJobs) | **GET** /app/{appId}/environment/{environmentName}/codegen-jobs | 
[**listComponents**](DefaultApi.md#listComponents) | **GET** /app/{appId}/environment/{environmentName}/components | 
[**listForms**](DefaultApi.md#listForms) | **GET** /app/{appId}/environment/{environmentName}/forms | 
[**listThemes**](DefaultApi.md#listThemes) | **GET** /app/{appId}/environment/{environmentName}/themes | 
[**putMetadataFlag**](DefaultApi.md#putMetadataFlag) | **PUT** /app/{appId}/environment/{environmentName}/metadata/features/{featureName} | 
[**refreshToken**](DefaultApi.md#refreshToken) | **POST** /tokens/{provider}/refresh | 
[**startCodegenJob**](DefaultApi.md#startCodegenJob) | **POST** /app/{appId}/environment/{environmentName}/codegen-jobs | 
[**updateComponent**](DefaultApi.md#updateComponent) | **PATCH** /app/{appId}/environment/{environmentName}/components/{id} | 
[**updateForm**](DefaultApi.md#updateForm) | **PATCH** /app/{appId}/environment/{environmentName}/forms/{id} | 
[**updateTheme**](DefaultApi.md#updateTheme) | **PATCH** /app/{appId}/environment/{environmentName}/themes/{id} | 



## createComponent

> CreateComponentResponse createComponent(appId, environmentName, createComponentRequest, opts)



Creates a new component for an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app to associate with the component.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let createComponentRequest = new AwsAmplifyUiBuilder.CreateComponentRequest(); // CreateComponentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | The unique client token.
};
apiInstance.createComponent(appId, environmentName, createComponentRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app to associate with the component. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **createComponentRequest** | [**CreateComponentRequest**](CreateComponentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| The unique client token. | [optional] 

### Return type

[**CreateComponentResponse**](CreateComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createForm

> CreateFormResponse createForm(appId, environmentName, createFormRequest, opts)



Creates a new form for an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app to associate with the form.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let createFormRequest = new AwsAmplifyUiBuilder.CreateFormRequest(); // CreateFormRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | The unique client token.
};
apiInstance.createForm(appId, environmentName, createFormRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app to associate with the form. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **createFormRequest** | [**CreateFormRequest**](CreateFormRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| The unique client token. | [optional] 

### Return type

[**CreateFormResponse**](CreateFormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTheme

> CreateThemeResponse createTheme(appId, environmentName, createThemeRequest, opts)



Creates a theme to apply to the components in an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app associated with the theme.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let createThemeRequest = new AwsAmplifyUiBuilder.CreateThemeRequest(); // CreateThemeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | The unique client token.
};
apiInstance.createTheme(appId, environmentName, createThemeRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app associated with the theme. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **createThemeRequest** | [**CreateThemeRequest**](CreateThemeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| The unique client token. | [optional] 

### Return type

[**CreateThemeResponse**](CreateThemeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteComponent

> deleteComponent(appId, environmentName, id, opts)



Deletes a component from an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app associated with the component to delete.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let id = "id_example"; // String | The unique ID of the component to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteComponent(appId, environmentName, id, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app associated with the component to delete. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **id** | **String**| The unique ID of the component to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteForm

> deleteForm(appId, environmentName, id, opts)



Deletes a form from an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app associated with the form to delete.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let id = "id_example"; // String | The unique ID of the form to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteForm(appId, environmentName, id, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app associated with the form to delete. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **id** | **String**| The unique ID of the form to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTheme

> deleteTheme(appId, environmentName, id, opts)



Deletes a theme from an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app associated with the theme to delete.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let id = "id_example"; // String | The unique ID of the theme to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTheme(appId, environmentName, id, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app associated with the theme to delete. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **id** | **String**| The unique ID of the theme to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exchangeCodeForToken

> ExchangeCodeForTokenResponse exchangeCodeForToken(provider, exchangeCodeForTokenRequest, opts)



Exchanges an access code for a token.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let provider = "provider_example"; // String | The third-party provider for the token. The only valid value is <code>figma</code>.
let exchangeCodeForTokenRequest = new AwsAmplifyUiBuilder.ExchangeCodeForTokenRequest(); // ExchangeCodeForTokenRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.exchangeCodeForToken(provider, exchangeCodeForTokenRequest, opts, (error, data, response) => {
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
 **provider** | **String**| The third-party provider for the token. The only valid value is &lt;code&gt;figma&lt;/code&gt;. | 
 **exchangeCodeForTokenRequest** | [**ExchangeCodeForTokenRequest**](ExchangeCodeForTokenRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ExchangeCodeForTokenResponse**](ExchangeCodeForTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## exportComponents

> ExportComponentsResponse exportComponents(appId, environmentName, opts)



Exports component configurations to code that is ready to integrate into an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app to export components to.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | The token to request the next page of results.
};
apiInstance.exportComponents(appId, environmentName, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app to export components to. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to request the next page of results. | [optional] 

### Return type

[**ExportComponentsResponse**](ExportComponentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportForms

> ExportFormsResponse exportForms(appId, environmentName, opts)



Exports form configurations to code that is ready to integrate into an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app to export forms to.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | The token to request the next page of results.
};
apiInstance.exportForms(appId, environmentName, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app to export forms to. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to request the next page of results. | [optional] 

### Return type

[**ExportFormsResponse**](ExportFormsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportThemes

> ExportThemesResponse exportThemes(appId, environmentName, opts)



Exports theme configurations to code that is ready to integrate into an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app to export the themes to.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is part of the Amplify app.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | The token to request the next page of results.
};
apiInstance.exportThemes(appId, environmentName, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app to export the themes to. | 
 **environmentName** | **String**| The name of the backend environment that is part of the Amplify app. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to request the next page of results. | [optional] 

### Return type

[**ExportThemesResponse**](ExportThemesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCodegenJob

> GetCodegenJobResponse getCodegenJob(appId, environmentName, id, opts)



Returns an existing code generation job.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app associated with the code generation job.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app associated with the code generation job.
let id = "id_example"; // String | The unique ID of the code generation job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCodegenJob(appId, environmentName, id, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app associated with the code generation job. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app associated with the code generation job. | 
 **id** | **String**| The unique ID of the code generation job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCodegenJobResponse**](GetCodegenJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getComponent

> GetComponentResponse getComponent(appId, environmentName, id, opts)



Returns an existing component for an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is part of the Amplify app.
let id = "id_example"; // String | The unique ID of the component.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getComponent(appId, environmentName, id, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is part of the Amplify app. | 
 **id** | **String**| The unique ID of the component. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetComponentResponse**](GetComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getForm

> GetFormResponse getForm(appId, environmentName, id, opts)



Returns an existing form for an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is part of the Amplify app.
let id = "id_example"; // String | The unique ID of the form.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getForm(appId, environmentName, id, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is part of the Amplify app. | 
 **id** | **String**| The unique ID of the form. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFormResponse**](GetFormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetadata

> GetMetadataResponse getMetadata(appId, environmentName, opts)



Returns existing metadata for an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is part of the Amplify app.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMetadata(appId, environmentName, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is part of the Amplify app. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMetadataResponse**](GetMetadataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTheme

> GetThemeResponse getTheme(appId, environmentName, id, opts)



Returns an existing theme for an Amplify app.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID of the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is part of the Amplify app.
let id = "id_example"; // String | The unique ID for the theme.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTheme(appId, environmentName, id, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID of the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is part of the Amplify app. | 
 **id** | **String**| The unique ID for the theme. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetThemeResponse**](GetThemeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCodegenJobs

> ListCodegenJobsResponse listCodegenJobs(appId, environmentName, opts)



Retrieves a list of code generation jobs for a specified Amplify app and backend environment.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID for the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to request the next page of results.
  'maxResults': 56 // Number | The maximum number of jobs to retrieve.
};
apiInstance.listCodegenJobs(appId, environmentName, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID for the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to request the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of jobs to retrieve. | [optional] 

### Return type

[**ListCodegenJobsResponse**](ListCodegenJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listComponents

> ListComponentsResponse listComponents(appId, environmentName, opts)



Retrieves a list of components for a specified Amplify app and backend environment.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID for the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to request the next page of results.
  'maxResults': 56 // Number | The maximum number of components to retrieve.
};
apiInstance.listComponents(appId, environmentName, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID for the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to request the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of components to retrieve. | [optional] 

### Return type

[**ListComponentsResponse**](ListComponentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listForms

> ListFormsResponse listForms(appId, environmentName, opts)



Retrieves a list of forms for a specified Amplify app and backend environment.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID for the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to request the next page of results.
  'maxResults': 56 // Number | The maximum number of forms to retrieve.
};
apiInstance.listForms(appId, environmentName, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID for the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to request the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of forms to retrieve. | [optional] 

### Return type

[**ListFormsResponse**](ListFormsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listThemes

> ListThemesResponse listThemes(appId, environmentName, opts)



Retrieves a list of themes for a specified Amplify app and backend environment.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID for the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to request the next page of results.
  'maxResults': 56 // Number | The maximum number of theme results to return in the response.
};
apiInstance.listThemes(appId, environmentName, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID for the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to request the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of theme results to return in the response. | [optional] 

### Return type

[**ListThemesResponse**](ListThemesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putMetadataFlag

> putMetadataFlag(appId, environmentName, featureName, putMetadataFlagRequest, opts)



Stores the metadata information about a feature on a form.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID for the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is part of the Amplify app.
let featureName = "featureName_example"; // String | The name of the feature associated with the metadata.
let putMetadataFlagRequest = new AwsAmplifyUiBuilder.PutMetadataFlagRequest(); // PutMetadataFlagRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putMetadataFlag(appId, environmentName, featureName, putMetadataFlagRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID for the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is part of the Amplify app. | 
 **featureName** | **String**| The name of the feature associated with the metadata. | 
 **putMetadataFlagRequest** | [**PutMetadataFlagRequest**](PutMetadataFlagRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## refreshToken

> RefreshTokenResponse refreshToken(provider, refreshTokenRequest, opts)



Refreshes a previously issued access token that might have expired.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let provider = "provider_example"; // String | The third-party provider for the token. The only valid value is <code>figma</code>.
let refreshTokenRequest = new AwsAmplifyUiBuilder.RefreshTokenRequest(); // RefreshTokenRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.refreshToken(provider, refreshTokenRequest, opts, (error, data, response) => {
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
 **provider** | **String**| The third-party provider for the token. The only valid value is &lt;code&gt;figma&lt;/code&gt;. | 
 **refreshTokenRequest** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RefreshTokenResponse**](RefreshTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startCodegenJob

> StartCodegenJobResponse startCodegenJob(appId, environmentName, startCodegenJobRequest, opts)



Starts a code generation job for a specified Amplify app and backend environment.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID for the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is a part of the Amplify app.
let startCodegenJobRequest = new AwsAmplifyUiBuilder.StartCodegenJobRequest(); // StartCodegenJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | The idempotency token used to ensure that the code generation job request completes only once.
};
apiInstance.startCodegenJob(appId, environmentName, startCodegenJobRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID for the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is a part of the Amplify app. | 
 **startCodegenJobRequest** | [**StartCodegenJobRequest**](StartCodegenJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| The idempotency token used to ensure that the code generation job request completes only once. | [optional] 

### Return type

[**StartCodegenJobResponse**](StartCodegenJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateComponent

> UpdateComponentResponse updateComponent(appId, environmentName, id, updateComponentRequest, opts)



Updates an existing component.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID for the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is part of the Amplify app.
let id = "id_example"; // String | The unique ID for the component.
let updateComponentRequest = new AwsAmplifyUiBuilder.UpdateComponentRequest(); // UpdateComponentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | The unique client token.
};
apiInstance.updateComponent(appId, environmentName, id, updateComponentRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID for the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is part of the Amplify app. | 
 **id** | **String**| The unique ID for the component. | 
 **updateComponentRequest** | [**UpdateComponentRequest**](UpdateComponentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| The unique client token. | [optional] 

### Return type

[**UpdateComponentResponse**](UpdateComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateForm

> UpdateFormResponse updateForm(appId, environmentName, id, updateFormRequest, opts)



Updates an existing form.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID for the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is part of the Amplify app.
let id = "id_example"; // String | The unique ID for the form.
let updateFormRequest = new AwsAmplifyUiBuilder.UpdateFormRequest(); // UpdateFormRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | The unique client token.
};
apiInstance.updateForm(appId, environmentName, id, updateFormRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID for the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is part of the Amplify app. | 
 **id** | **String**| The unique ID for the form. | 
 **updateFormRequest** | [**UpdateFormRequest**](UpdateFormRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| The unique client token. | [optional] 

### Return type

[**UpdateFormResponse**](UpdateFormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTheme

> UpdateThemeResponse updateTheme(appId, environmentName, id, updateThemeRequest, opts)



Updates an existing theme.

### Example

```javascript
import AwsAmplifyUiBuilder from 'aws_amplify_ui_builder';
let defaultClient = AwsAmplifyUiBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAmplifyUiBuilder.DefaultApi();
let appId = "appId_example"; // String | The unique ID for the Amplify app.
let environmentName = "environmentName_example"; // String | The name of the backend environment that is part of the Amplify app.
let id = "id_example"; // String | The unique ID for the theme.
let updateThemeRequest = new AwsAmplifyUiBuilder.UpdateThemeRequest(); // UpdateThemeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | The unique client token.
};
apiInstance.updateTheme(appId, environmentName, id, updateThemeRequest, opts, (error, data, response) => {
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
 **appId** | **String**| The unique ID for the Amplify app. | 
 **environmentName** | **String**| The name of the backend environment that is part of the Amplify app. | 
 **id** | **String**| The unique ID for the theme. | 
 **updateThemeRequest** | [**UpdateThemeRequest**](UpdateThemeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| The unique client token. | [optional] 

### Return type

[**UpdateThemeResponse**](UpdateThemeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

