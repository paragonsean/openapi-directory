# AmazonApiGatewayV2.DefaultApi

All URIs are relative to *http://apigateway.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApi**](DefaultApi.md#createApi) | **POST** /v2/apis | 
[**createApiMapping**](DefaultApi.md#createApiMapping) | **POST** /v2/domainnames/{domainName}/apimappings | 
[**createAuthorizer**](DefaultApi.md#createAuthorizer) | **POST** /v2/apis/{apiId}/authorizers | 
[**createDeployment**](DefaultApi.md#createDeployment) | **POST** /v2/apis/{apiId}/deployments | 
[**createDomainName**](DefaultApi.md#createDomainName) | **POST** /v2/domainnames | 
[**createIntegration**](DefaultApi.md#createIntegration) | **POST** /v2/apis/{apiId}/integrations | 
[**createIntegrationResponse**](DefaultApi.md#createIntegrationResponse) | **POST** /v2/apis/{apiId}/integrations/{integrationId}/integrationresponses | 
[**createModel**](DefaultApi.md#createModel) | **POST** /v2/apis/{apiId}/models | 
[**createRoute**](DefaultApi.md#createRoute) | **POST** /v2/apis/{apiId}/routes | 
[**createRouteResponse**](DefaultApi.md#createRouteResponse) | **POST** /v2/apis/{apiId}/routes/{routeId}/routeresponses | 
[**createStage**](DefaultApi.md#createStage) | **POST** /v2/apis/{apiId}/stages | 
[**createVpcLink**](DefaultApi.md#createVpcLink) | **POST** /v2/vpclinks | 
[**deleteAccessLogSettings**](DefaultApi.md#deleteAccessLogSettings) | **DELETE** /v2/apis/{apiId}/stages/{stageName}/accesslogsettings | 
[**deleteApi**](DefaultApi.md#deleteApi) | **DELETE** /v2/apis/{apiId} | 
[**deleteApiMapping**](DefaultApi.md#deleteApiMapping) | **DELETE** /v2/domainnames/{domainName}/apimappings/{apiMappingId} | 
[**deleteAuthorizer**](DefaultApi.md#deleteAuthorizer) | **DELETE** /v2/apis/{apiId}/authorizers/{authorizerId} | 
[**deleteCorsConfiguration**](DefaultApi.md#deleteCorsConfiguration) | **DELETE** /v2/apis/{apiId}/cors | 
[**deleteDeployment**](DefaultApi.md#deleteDeployment) | **DELETE** /v2/apis/{apiId}/deployments/{deploymentId} | 
[**deleteDomainName**](DefaultApi.md#deleteDomainName) | **DELETE** /v2/domainnames/{domainName} | 
[**deleteIntegration**](DefaultApi.md#deleteIntegration) | **DELETE** /v2/apis/{apiId}/integrations/{integrationId} | 
[**deleteIntegrationResponse**](DefaultApi.md#deleteIntegrationResponse) | **DELETE** /v2/apis/{apiId}/integrations/{integrationId}/integrationresponses/{integrationResponseId} | 
[**deleteModel**](DefaultApi.md#deleteModel) | **DELETE** /v2/apis/{apiId}/models/{modelId} | 
[**deleteRoute**](DefaultApi.md#deleteRoute) | **DELETE** /v2/apis/{apiId}/routes/{routeId} | 
[**deleteRouteRequestParameter**](DefaultApi.md#deleteRouteRequestParameter) | **DELETE** /v2/apis/{apiId}/routes/{routeId}/requestparameters/{requestParameterKey} | 
[**deleteRouteResponse**](DefaultApi.md#deleteRouteResponse) | **DELETE** /v2/apis/{apiId}/routes/{routeId}/routeresponses/{routeResponseId} | 
[**deleteRouteSettings**](DefaultApi.md#deleteRouteSettings) | **DELETE** /v2/apis/{apiId}/stages/{stageName}/routesettings/{routeKey} | 
[**deleteStage**](DefaultApi.md#deleteStage) | **DELETE** /v2/apis/{apiId}/stages/{stageName} | 
[**deleteVpcLink**](DefaultApi.md#deleteVpcLink) | **DELETE** /v2/vpclinks/{vpcLinkId} | 
[**exportApi**](DefaultApi.md#exportApi) | **GET** /v2/apis/{apiId}/exports/{specification}#outputType | 
[**getApi**](DefaultApi.md#getApi) | **GET** /v2/apis/{apiId} | 
[**getApiMapping**](DefaultApi.md#getApiMapping) | **GET** /v2/domainnames/{domainName}/apimappings/{apiMappingId} | 
[**getApiMappings**](DefaultApi.md#getApiMappings) | **GET** /v2/domainnames/{domainName}/apimappings | 
[**getApis**](DefaultApi.md#getApis) | **GET** /v2/apis | 
[**getAuthorizer**](DefaultApi.md#getAuthorizer) | **GET** /v2/apis/{apiId}/authorizers/{authorizerId} | 
[**getAuthorizers**](DefaultApi.md#getAuthorizers) | **GET** /v2/apis/{apiId}/authorizers | 
[**getDeployment**](DefaultApi.md#getDeployment) | **GET** /v2/apis/{apiId}/deployments/{deploymentId} | 
[**getDeployments**](DefaultApi.md#getDeployments) | **GET** /v2/apis/{apiId}/deployments | 
[**getDomainName**](DefaultApi.md#getDomainName) | **GET** /v2/domainnames/{domainName} | 
[**getDomainNames**](DefaultApi.md#getDomainNames) | **GET** /v2/domainnames | 
[**getIntegration**](DefaultApi.md#getIntegration) | **GET** /v2/apis/{apiId}/integrations/{integrationId} | 
[**getIntegrationResponse**](DefaultApi.md#getIntegrationResponse) | **GET** /v2/apis/{apiId}/integrations/{integrationId}/integrationresponses/{integrationResponseId} | 
[**getIntegrationResponses**](DefaultApi.md#getIntegrationResponses) | **GET** /v2/apis/{apiId}/integrations/{integrationId}/integrationresponses | 
[**getIntegrations**](DefaultApi.md#getIntegrations) | **GET** /v2/apis/{apiId}/integrations | 
[**getModel**](DefaultApi.md#getModel) | **GET** /v2/apis/{apiId}/models/{modelId} | 
[**getModelTemplate**](DefaultApi.md#getModelTemplate) | **GET** /v2/apis/{apiId}/models/{modelId}/template | 
[**getModels**](DefaultApi.md#getModels) | **GET** /v2/apis/{apiId}/models | 
[**getRoute**](DefaultApi.md#getRoute) | **GET** /v2/apis/{apiId}/routes/{routeId} | 
[**getRouteResponse**](DefaultApi.md#getRouteResponse) | **GET** /v2/apis/{apiId}/routes/{routeId}/routeresponses/{routeResponseId} | 
[**getRouteResponses**](DefaultApi.md#getRouteResponses) | **GET** /v2/apis/{apiId}/routes/{routeId}/routeresponses | 
[**getRoutes**](DefaultApi.md#getRoutes) | **GET** /v2/apis/{apiId}/routes | 
[**getStage**](DefaultApi.md#getStage) | **GET** /v2/apis/{apiId}/stages/{stageName} | 
[**getStages**](DefaultApi.md#getStages) | **GET** /v2/apis/{apiId}/stages | 
[**getTags**](DefaultApi.md#getTags) | **GET** /v2/tags/{resource-arn} | 
[**getVpcLink**](DefaultApi.md#getVpcLink) | **GET** /v2/vpclinks/{vpcLinkId} | 
[**getVpcLinks**](DefaultApi.md#getVpcLinks) | **GET** /v2/vpclinks | 
[**importApi**](DefaultApi.md#importApi) | **PUT** /v2/apis | 
[**reimportApi**](DefaultApi.md#reimportApi) | **PUT** /v2/apis/{apiId} | 
[**resetAuthorizersCache**](DefaultApi.md#resetAuthorizersCache) | **DELETE** /v2/apis/{apiId}/stages/{stageName}/cache/authorizers | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /v2/tags/{resource-arn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /v2/tags/{resource-arn}#tagKeys | 
[**updateApi**](DefaultApi.md#updateApi) | **PATCH** /v2/apis/{apiId} | 
[**updateApiMapping**](DefaultApi.md#updateApiMapping) | **PATCH** /v2/domainnames/{domainName}/apimappings/{apiMappingId} | 
[**updateAuthorizer**](DefaultApi.md#updateAuthorizer) | **PATCH** /v2/apis/{apiId}/authorizers/{authorizerId} | 
[**updateDeployment**](DefaultApi.md#updateDeployment) | **PATCH** /v2/apis/{apiId}/deployments/{deploymentId} | 
[**updateDomainName**](DefaultApi.md#updateDomainName) | **PATCH** /v2/domainnames/{domainName} | 
[**updateIntegration**](DefaultApi.md#updateIntegration) | **PATCH** /v2/apis/{apiId}/integrations/{integrationId} | 
[**updateIntegrationResponse**](DefaultApi.md#updateIntegrationResponse) | **PATCH** /v2/apis/{apiId}/integrations/{integrationId}/integrationresponses/{integrationResponseId} | 
[**updateModel**](DefaultApi.md#updateModel) | **PATCH** /v2/apis/{apiId}/models/{modelId} | 
[**updateRoute**](DefaultApi.md#updateRoute) | **PATCH** /v2/apis/{apiId}/routes/{routeId} | 
[**updateRouteResponse**](DefaultApi.md#updateRouteResponse) | **PATCH** /v2/apis/{apiId}/routes/{routeId}/routeresponses/{routeResponseId} | 
[**updateStage**](DefaultApi.md#updateStage) | **PATCH** /v2/apis/{apiId}/stages/{stageName} | 
[**updateVpcLink**](DefaultApi.md#updateVpcLink) | **PATCH** /v2/vpclinks/{vpcLinkId} | 



## createApi

> CreateApiResponse createApi(createApiRequest, opts)



Creates an Api resource.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let createApiRequest = new AmazonApiGatewayV2.CreateApiRequest(); // CreateApiRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApi(createApiRequest, opts, (error, data, response) => {
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
 **createApiRequest** | [**CreateApiRequest**](CreateApiRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateApiResponse**](CreateApiResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createApiMapping

> CreateApiMappingResponse createApiMapping(domainName, createApiMappingRequest, opts)



Creates an API mapping.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let domainName = "domainName_example"; // String | The domain name.
let createApiMappingRequest = new AmazonApiGatewayV2.CreateApiMappingRequest(); // CreateApiMappingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApiMapping(domainName, createApiMappingRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
 **createApiMappingRequest** | [**CreateApiMappingRequest**](CreateApiMappingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateApiMappingResponse**](CreateApiMappingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAuthorizer

> CreateAuthorizerResponse createAuthorizer(apiId, createAuthorizerRequest, opts)



Creates an Authorizer for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let createAuthorizerRequest = new AmazonApiGatewayV2.CreateAuthorizerRequest(); // CreateAuthorizerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAuthorizer(apiId, createAuthorizerRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **createAuthorizerRequest** | [**CreateAuthorizerRequest**](CreateAuthorizerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAuthorizerResponse**](CreateAuthorizerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDeployment

> CreateDeploymentResponse createDeployment(apiId, createDeploymentRequest, opts)



Creates a Deployment for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let createDeploymentRequest = new AmazonApiGatewayV2.CreateDeploymentRequest(); // CreateDeploymentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDeployment(apiId, createDeploymentRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **createDeploymentRequest** | [**CreateDeploymentRequest**](CreateDeploymentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDeploymentResponse**](CreateDeploymentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDomainName

> CreateDomainNameResponse createDomainName(createDomainNameRequest, opts)



Creates a domain name.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let createDomainNameRequest = new AmazonApiGatewayV2.CreateDomainNameRequest(); // CreateDomainNameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDomainName(createDomainNameRequest, opts, (error, data, response) => {
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
 **createDomainNameRequest** | [**CreateDomainNameRequest**](CreateDomainNameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDomainNameResponse**](CreateDomainNameResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createIntegration

> CreateIntegrationResult createIntegration(apiId, createIntegrationRequest, opts)



Creates an Integration.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let createIntegrationRequest = new AmazonApiGatewayV2.CreateIntegrationRequest(); // CreateIntegrationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIntegration(apiId, createIntegrationRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **createIntegrationRequest** | [**CreateIntegrationRequest**](CreateIntegrationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateIntegrationResult**](CreateIntegrationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createIntegrationResponse

> CreateIntegrationResponseResponse createIntegrationResponse(apiId, integrationId, createIntegrationResponseRequest, opts)



Creates an IntegrationResponses.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let integrationId = "integrationId_example"; // String | The integration ID.
let createIntegrationResponseRequest = new AmazonApiGatewayV2.CreateIntegrationResponseRequest(); // CreateIntegrationResponseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIntegrationResponse(apiId, integrationId, createIntegrationResponseRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **integrationId** | **String**| The integration ID. | 
 **createIntegrationResponseRequest** | [**CreateIntegrationResponseRequest**](CreateIntegrationResponseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateIntegrationResponseResponse**](CreateIntegrationResponseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createModel

> CreateModelResponse createModel(apiId, createModelRequest, opts)



Creates a Model for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let createModelRequest = new AmazonApiGatewayV2.CreateModelRequest(); // CreateModelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createModel(apiId, createModelRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **createModelRequest** | [**CreateModelRequest**](CreateModelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateModelResponse**](CreateModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRoute

> CreateRouteResult createRoute(apiId, createRouteRequest, opts)



Creates a Route for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let createRouteRequest = new AmazonApiGatewayV2.CreateRouteRequest(); // CreateRouteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRoute(apiId, createRouteRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **createRouteRequest** | [**CreateRouteRequest**](CreateRouteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRouteResult**](CreateRouteResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRouteResponse

> CreateRouteResponseResponse createRouteResponse(apiId, routeId, createRouteResponseRequest, opts)



Creates a RouteResponse for a Route.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let routeId = "routeId_example"; // String | The route ID.
let createRouteResponseRequest = new AmazonApiGatewayV2.CreateRouteResponseRequest(); // CreateRouteResponseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRouteResponse(apiId, routeId, createRouteResponseRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **routeId** | **String**| The route ID. | 
 **createRouteResponseRequest** | [**CreateRouteResponseRequest**](CreateRouteResponseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRouteResponseResponse**](CreateRouteResponseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStage

> CreateStageResponse createStage(apiId, createStageRequest, opts)



Creates a Stage for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let createStageRequest = new AmazonApiGatewayV2.CreateStageRequest(); // CreateStageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStage(apiId, createStageRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **createStageRequest** | [**CreateStageRequest**](CreateStageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateStageResponse**](CreateStageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVpcLink

> CreateVpcLinkResponse createVpcLink(createVpcLinkRequest, opts)



Creates a VPC link.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let createVpcLinkRequest = new AmazonApiGatewayV2.CreateVpcLinkRequest(); // CreateVpcLinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVpcLink(createVpcLinkRequest, opts, (error, data, response) => {
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
 **createVpcLinkRequest** | [**CreateVpcLinkRequest**](CreateVpcLinkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVpcLinkResponse**](CreateVpcLinkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccessLogSettings

> deleteAccessLogSettings(apiId, stageName, opts)



Deletes the AccessLogSettings for a Stage. To disable access logging for a Stage, delete its AccessLogSettings.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let stageName = "stageName_example"; // String | The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAccessLogSettings(apiId, stageName, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **stageName** | **String**| The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters. | 
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


## deleteApi

> deleteApi(apiId, opts)



Deletes an Api resource.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApi(apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
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


## deleteApiMapping

> deleteApiMapping(apiMappingId, domainName, opts)



Deletes an API mapping.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiMappingId = "apiMappingId_example"; // String | The API mapping identifier.
let domainName = "domainName_example"; // String | The domain name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApiMapping(apiMappingId, domainName, opts, (error, data, response) => {
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
 **apiMappingId** | **String**| The API mapping identifier. | 
 **domainName** | **String**| The domain name. | 
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


## deleteAuthorizer

> deleteAuthorizer(apiId, authorizerId, opts)



Deletes an Authorizer.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let authorizerId = "authorizerId_example"; // String | The authorizer identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAuthorizer(apiId, authorizerId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **authorizerId** | **String**| The authorizer identifier. | 
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


## deleteCorsConfiguration

> deleteCorsConfiguration(apiId, opts)



Deletes a CORS configuration.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCorsConfiguration(apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
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


## deleteDeployment

> deleteDeployment(apiId, deploymentId, opts)



Deletes a Deployment.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let deploymentId = "deploymentId_example"; // String | The deployment ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDeployment(apiId, deploymentId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **deploymentId** | **String**| The deployment ID. | 
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


## deleteDomainName

> deleteDomainName(domainName, opts)



Deletes a domain name.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let domainName = "domainName_example"; // String | The domain name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDomainName(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
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


## deleteIntegration

> deleteIntegration(apiId, integrationId, opts)



Deletes an Integration.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let integrationId = "integrationId_example"; // String | The integration ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIntegration(apiId, integrationId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **integrationId** | **String**| The integration ID. | 
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


## deleteIntegrationResponse

> deleteIntegrationResponse(apiId, integrationId, integrationResponseId, opts)



Deletes an IntegrationResponses.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let integrationId = "integrationId_example"; // String | The integration ID.
let integrationResponseId = "integrationResponseId_example"; // String | The integration response ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIntegrationResponse(apiId, integrationId, integrationResponseId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **integrationId** | **String**| The integration ID. | 
 **integrationResponseId** | **String**| The integration response ID. | 
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


## deleteModel

> deleteModel(apiId, modelId, opts)



Deletes a Model.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let modelId = "modelId_example"; // String | The model ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteModel(apiId, modelId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **modelId** | **String**| The model ID. | 
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


## deleteRoute

> deleteRoute(apiId, routeId, opts)



Deletes a Route.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let routeId = "routeId_example"; // String | The route ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRoute(apiId, routeId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **routeId** | **String**| The route ID. | 
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


## deleteRouteRequestParameter

> deleteRouteRequestParameter(apiId, requestParameterKey, routeId, opts)



Deletes a route request parameter. Supported only for WebSocket APIs.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let requestParameterKey = "requestParameterKey_example"; // String | The route request parameter key.
let routeId = "routeId_example"; // String | The route ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRouteRequestParameter(apiId, requestParameterKey, routeId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **requestParameterKey** | **String**| The route request parameter key. | 
 **routeId** | **String**| The route ID. | 
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


## deleteRouteResponse

> deleteRouteResponse(apiId, routeId, routeResponseId, opts)



Deletes a RouteResponse.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let routeId = "routeId_example"; // String | The route ID.
let routeResponseId = "routeResponseId_example"; // String | The route response ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRouteResponse(apiId, routeId, routeResponseId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **routeId** | **String**| The route ID. | 
 **routeResponseId** | **String**| The route response ID. | 
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


## deleteRouteSettings

> deleteRouteSettings(apiId, routeKey, stageName, opts)



Deletes the RouteSettings for a stage.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let routeKey = "routeKey_example"; // String | The route key.
let stageName = "stageName_example"; // String | The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRouteSettings(apiId, routeKey, stageName, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **routeKey** | **String**| The route key. | 
 **stageName** | **String**| The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters. | 
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


## deleteStage

> deleteStage(apiId, stageName, opts)



Deletes a Stage.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let stageName = "stageName_example"; // String | The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteStage(apiId, stageName, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **stageName** | **String**| The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters. | 
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


## deleteVpcLink

> Object deleteVpcLink(vpcLinkId, opts)



Deletes a VPC link.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let vpcLinkId = "vpcLinkId_example"; // String | The ID of the VPC link.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVpcLink(vpcLinkId, opts, (error, data, response) => {
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
 **vpcLinkId** | **String**| The ID of the VPC link. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportApi

> ExportApiResponse exportApi(apiId, outputType, specification, opts)





### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let outputType = "outputType_example"; // String | The output type of the exported definition file. Valid values are JSON and YAML.
let specification = "specification_example"; // String | The version of the API specification to use. OAS30, for OpenAPI 3.0, is the only supported value.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'exportVersion': "exportVersion_example", // String | The version of the API Gateway export algorithm. API Gateway uses the latest version by default. Currently, the only supported version is 1.0.
  'includeExtensions': true, // Boolean | Specifies whether to include <a href=\"https://docs.aws.amazon.com//apigateway/latest/developerguide/api-gateway-swagger-extensions.html\">API Gateway extensions</a> in the exported API definition. API Gateway extensions are included by default.
  'stageName': "stageName_example" // String | The name of the API stage to export. If you don't specify this property, a representation of the latest API configuration is exported.
};
apiInstance.exportApi(apiId, outputType, specification, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **outputType** | **String**| The output type of the exported definition file. Valid values are JSON and YAML. | 
 **specification** | **String**| The version of the API specification to use. OAS30, for OpenAPI 3.0, is the only supported value. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **exportVersion** | **String**| The version of the API Gateway export algorithm. API Gateway uses the latest version by default. Currently, the only supported version is 1.0. | [optional] 
 **includeExtensions** | **Boolean**| Specifies whether to include &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com//apigateway/latest/developerguide/api-gateway-swagger-extensions.html\&quot;&gt;API Gateway extensions&lt;/a&gt; in the exported API definition. API Gateway extensions are included by default. | [optional] 
 **stageName** | **String**| The name of the API stage to export. If you don&#39;t specify this property, a representation of the latest API configuration is exported. | [optional] 

### Return type

[**ExportApiResponse**](ExportApiResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApi

> GetApiResponse getApi(apiId, opts)



Gets an Api resource.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApi(apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApiResponse**](GetApiResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApiMapping

> GetApiMappingResponse getApiMapping(apiMappingId, domainName, opts)



Gets an API mapping.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiMappingId = "apiMappingId_example"; // String | The API mapping identifier.
let domainName = "domainName_example"; // String | The domain name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApiMapping(apiMappingId, domainName, opts, (error, data, response) => {
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
 **apiMappingId** | **String**| The API mapping identifier. | 
 **domainName** | **String**| The domain name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApiMappingResponse**](GetApiMappingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApiMappings

> GetApiMappingsResponse getApiMappings(domainName, opts)



Gets API mappings.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let domainName = "domainName_example"; // String | The domain name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getApiMappings(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetApiMappingsResponse**](GetApiMappingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApis

> GetApisResponse getApis(opts)



Gets a collection of Api resources.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getApis(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetApisResponse**](GetApisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthorizer

> GetAuthorizerResponse getAuthorizer(apiId, authorizerId, opts)



Gets an Authorizer.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let authorizerId = "authorizerId_example"; // String | The authorizer identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAuthorizer(apiId, authorizerId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **authorizerId** | **String**| The authorizer identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAuthorizerResponse**](GetAuthorizerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthorizers

> GetAuthorizersResponse getAuthorizers(apiId, opts)



Gets the Authorizers for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getAuthorizers(apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetAuthorizersResponse**](GetAuthorizersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeployment

> GetDeploymentResponse getDeployment(apiId, deploymentId, opts)



Gets a Deployment.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let deploymentId = "deploymentId_example"; // String | The deployment ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDeployment(apiId, deploymentId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **deploymentId** | **String**| The deployment ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDeploymentResponse**](GetDeploymentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeployments

> GetDeploymentsResponse getDeployments(apiId, opts)



Gets the Deployments for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getDeployments(apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetDeploymentsResponse**](GetDeploymentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainName

> GetDomainNameResponse getDomainName(domainName, opts)



Gets a domain name.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let domainName = "domainName_example"; // String | The domain name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDomainName(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDomainNameResponse**](GetDomainNameResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainNames

> GetDomainNamesResponse getDomainNames(opts)



Gets the domain names for an AWS account.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getDomainNames(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetDomainNamesResponse**](GetDomainNamesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegration

> GetIntegrationResult getIntegration(apiId, integrationId, opts)



Gets an Integration.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let integrationId = "integrationId_example"; // String | The integration ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIntegration(apiId, integrationId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **integrationId** | **String**| The integration ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIntegrationResult**](GetIntegrationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegrationResponse

> GetIntegrationResponseResponse getIntegrationResponse(apiId, integrationId, integrationResponseId, opts)



Gets an IntegrationResponses.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let integrationId = "integrationId_example"; // String | The integration ID.
let integrationResponseId = "integrationResponseId_example"; // String | The integration response ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIntegrationResponse(apiId, integrationId, integrationResponseId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **integrationId** | **String**| The integration ID. | 
 **integrationResponseId** | **String**| The integration response ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIntegrationResponseResponse**](GetIntegrationResponseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegrationResponses

> GetIntegrationResponsesResponse getIntegrationResponses(apiId, integrationId, opts)



Gets the IntegrationResponses for an Integration.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let integrationId = "integrationId_example"; // String | The integration ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getIntegrationResponses(apiId, integrationId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **integrationId** | **String**| The integration ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetIntegrationResponsesResponse**](GetIntegrationResponsesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegrations

> GetIntegrationsResponse getIntegrations(apiId, opts)



Gets the Integrations for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getIntegrations(apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetIntegrationsResponse**](GetIntegrationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModel

> GetModelResponse getModel(apiId, modelId, opts)



Gets a Model.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let modelId = "modelId_example"; // String | The model ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getModel(apiId, modelId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **modelId** | **String**| The model ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetModelResponse**](GetModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelTemplate

> GetModelTemplateResponse getModelTemplate(apiId, modelId, opts)



Gets a model template.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let modelId = "modelId_example"; // String | The model ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getModelTemplate(apiId, modelId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **modelId** | **String**| The model ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetModelTemplateResponse**](GetModelTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModels

> GetModelsResponse getModels(apiId, opts)



Gets the Models for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getModels(apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetModelsResponse**](GetModelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRoute

> GetRouteResult getRoute(apiId, routeId, opts)



Gets a Route.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let routeId = "routeId_example"; // String | The route ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRoute(apiId, routeId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **routeId** | **String**| The route ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRouteResult**](GetRouteResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRouteResponse

> GetRouteResponseResponse getRouteResponse(apiId, routeId, routeResponseId, opts)



Gets a RouteResponse.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let routeId = "routeId_example"; // String | The route ID.
let routeResponseId = "routeResponseId_example"; // String | The route response ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRouteResponse(apiId, routeId, routeResponseId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **routeId** | **String**| The route ID. | 
 **routeResponseId** | **String**| The route response ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRouteResponseResponse**](GetRouteResponseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRouteResponses

> GetRouteResponsesResponse getRouteResponses(apiId, routeId, opts)



Gets the RouteResponses for a Route.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let routeId = "routeId_example"; // String | The route ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getRouteResponses(apiId, routeId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **routeId** | **String**| The route ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetRouteResponsesResponse**](GetRouteResponsesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRoutes

> GetRoutesResponse getRoutes(apiId, opts)



Gets the Routes for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getRoutes(apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetRoutesResponse**](GetRoutesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStage

> GetStageResponse getStage(apiId, stageName, opts)



Gets a Stage.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let stageName = "stageName_example"; // String | The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStage(apiId, stageName, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **stageName** | **String**| The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStageResponse**](GetStageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStages

> GetStagesResponse getStages(apiId, opts)



Gets the Stages for an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getStages(apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetStagesResponse**](GetStagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTags

> GetTagsResponse getTags(resourceArn, opts)



Gets a collection of Tag resources.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource ARN for the tag.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTags(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The resource ARN for the tag. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTagsResponse**](GetTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVpcLink

> GetVpcLinkResponse getVpcLink(vpcLinkId, opts)



Gets a VPC link.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let vpcLinkId = "vpcLinkId_example"; // String | The ID of the VPC link.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVpcLink(vpcLinkId, opts, (error, data, response) => {
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
 **vpcLinkId** | **String**| The ID of the VPC link. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVpcLinkResponse**](GetVpcLinkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVpcLinks

> GetVpcLinksResponse getVpcLinks(opts)



Gets a collection of VPC links.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | The maximum number of elements to be returned for this resource.
  'nextToken': "nextToken_example" // String | The next page of elements from this collection. Not valid for the last element of the collection.
};
apiInstance.getVpcLinks(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| The maximum number of elements to be returned for this resource. | [optional] 
 **nextToken** | **String**| The next page of elements from this collection. Not valid for the last element of the collection. | [optional] 

### Return type

[**GetVpcLinksResponse**](GetVpcLinksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importApi

> ImportApiResponse importApi(importApiRequest, opts)



Imports an API.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let importApiRequest = new AmazonApiGatewayV2.ImportApiRequest(); // ImportApiRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'basepath': "basepath_example", // String | Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html\">Set the OpenAPI basePath Property</a>. Supported only for HTTP APIs.
  'failOnWarnings': true // Boolean | Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.
};
apiInstance.importApi(importApiRequest, opts, (error, data, response) => {
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
 **importApiRequest** | [**ImportApiRequest**](ImportApiRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **basepath** | **String**| Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html\&quot;&gt;Set the OpenAPI basePath Property&lt;/a&gt;. Supported only for HTTP APIs. | [optional] 
 **failOnWarnings** | **Boolean**| Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered. | [optional] 

### Return type

[**ImportApiResponse**](ImportApiResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reimportApi

> ReimportApiResponse reimportApi(apiId, importApiRequest, opts)



Puts an Api resource.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let importApiRequest = new AmazonApiGatewayV2.ImportApiRequest(); // ImportApiRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'basepath': "basepath_example", // String | Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html\">Set the OpenAPI basePath Property</a>. Supported only for HTTP APIs.
  'failOnWarnings': true // Boolean | Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.
};
apiInstance.reimportApi(apiId, importApiRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **importApiRequest** | [**ImportApiRequest**](ImportApiRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **basepath** | **String**| Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html\&quot;&gt;Set the OpenAPI basePath Property&lt;/a&gt;. Supported only for HTTP APIs. | [optional] 
 **failOnWarnings** | **Boolean**| Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered. | [optional] 

### Return type

[**ReimportApiResponse**](ReimportApiResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetAuthorizersCache

> resetAuthorizersCache(apiId, stageName, opts)



Resets all authorizer cache entries on a stage. Supported only for HTTP APIs.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let stageName = "stageName_example"; // String | The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resetAuthorizersCache(apiId, stageName, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **stageName** | **String**| The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters. | 
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


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Creates a new Tag resource to represent a tag.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource ARN for the tag.
let tagResourceRequest = new AmazonApiGatewayV2.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The resource ARN for the tag. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> untagResource(resourceArn, tagKeys, opts)



Deletes a Tag.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource ARN for the tag.
let tagKeys = ["null"]; // [String] | The Tag keys to delete
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The resource ARN for the tag. | 
 **tagKeys** | [**[String]**](String.md)| The Tag keys to delete | 
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


## updateApi

> UpdateApiResponse updateApi(apiId, updateApiRequest, opts)



Updates an Api resource.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let updateApiRequest = new AmazonApiGatewayV2.UpdateApiRequest(); // UpdateApiRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApi(apiId, updateApiRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **updateApiRequest** | [**UpdateApiRequest**](UpdateApiRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApiResponse**](UpdateApiResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApiMapping

> UpdateApiMappingResponse updateApiMapping(apiMappingId, domainName, updateApiMappingRequest, opts)



The API mapping.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiMappingId = "apiMappingId_example"; // String | The API mapping identifier.
let domainName = "domainName_example"; // String | The domain name.
let updateApiMappingRequest = new AmazonApiGatewayV2.UpdateApiMappingRequest(); // UpdateApiMappingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApiMapping(apiMappingId, domainName, updateApiMappingRequest, opts, (error, data, response) => {
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
 **apiMappingId** | **String**| The API mapping identifier. | 
 **domainName** | **String**| The domain name. | 
 **updateApiMappingRequest** | [**UpdateApiMappingRequest**](UpdateApiMappingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApiMappingResponse**](UpdateApiMappingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAuthorizer

> UpdateAuthorizerResponse updateAuthorizer(apiId, authorizerId, updateAuthorizerRequest, opts)



Updates an Authorizer.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let authorizerId = "authorizerId_example"; // String | The authorizer identifier.
let updateAuthorizerRequest = new AmazonApiGatewayV2.UpdateAuthorizerRequest(); // UpdateAuthorizerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAuthorizer(apiId, authorizerId, updateAuthorizerRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **authorizerId** | **String**| The authorizer identifier. | 
 **updateAuthorizerRequest** | [**UpdateAuthorizerRequest**](UpdateAuthorizerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAuthorizerResponse**](UpdateAuthorizerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeployment

> UpdateDeploymentResponse updateDeployment(apiId, deploymentId, updateDeploymentRequest, opts)



Updates a Deployment.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let deploymentId = "deploymentId_example"; // String | The deployment ID.
let updateDeploymentRequest = new AmazonApiGatewayV2.UpdateDeploymentRequest(); // UpdateDeploymentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDeployment(apiId, deploymentId, updateDeploymentRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **deploymentId** | **String**| The deployment ID. | 
 **updateDeploymentRequest** | [**UpdateDeploymentRequest**](UpdateDeploymentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateDeploymentResponse**](UpdateDeploymentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDomainName

> UpdateDomainNameResponse updateDomainName(domainName, updateDomainNameRequest, opts)



Updates a domain name.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let domainName = "domainName_example"; // String | The domain name.
let updateDomainNameRequest = new AmazonApiGatewayV2.UpdateDomainNameRequest(); // UpdateDomainNameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDomainName(domainName, updateDomainNameRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name. | 
 **updateDomainNameRequest** | [**UpdateDomainNameRequest**](UpdateDomainNameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateDomainNameResponse**](UpdateDomainNameResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateIntegration

> UpdateIntegrationResult updateIntegration(apiId, integrationId, updateIntegrationRequest, opts)



Updates an Integration.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let integrationId = "integrationId_example"; // String | The integration ID.
let updateIntegrationRequest = new AmazonApiGatewayV2.UpdateIntegrationRequest(); // UpdateIntegrationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateIntegration(apiId, integrationId, updateIntegrationRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **integrationId** | **String**| The integration ID. | 
 **updateIntegrationRequest** | [**UpdateIntegrationRequest**](UpdateIntegrationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateIntegrationResult**](UpdateIntegrationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateIntegrationResponse

> UpdateIntegrationResponseResponse updateIntegrationResponse(apiId, integrationId, integrationResponseId, updateIntegrationResponseRequest, opts)



Updates an IntegrationResponses.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let integrationId = "integrationId_example"; // String | The integration ID.
let integrationResponseId = "integrationResponseId_example"; // String | The integration response ID.
let updateIntegrationResponseRequest = new AmazonApiGatewayV2.UpdateIntegrationResponseRequest(); // UpdateIntegrationResponseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateIntegrationResponse(apiId, integrationId, integrationResponseId, updateIntegrationResponseRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **integrationId** | **String**| The integration ID. | 
 **integrationResponseId** | **String**| The integration response ID. | 
 **updateIntegrationResponseRequest** | [**UpdateIntegrationResponseRequest**](UpdateIntegrationResponseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateIntegrationResponseResponse**](UpdateIntegrationResponseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateModel

> UpdateModelResponse updateModel(apiId, modelId, updateModelRequest, opts)



Updates a Model.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let modelId = "modelId_example"; // String | The model ID.
let updateModelRequest = new AmazonApiGatewayV2.UpdateModelRequest(); // UpdateModelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateModel(apiId, modelId, updateModelRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **modelId** | **String**| The model ID. | 
 **updateModelRequest** | [**UpdateModelRequest**](UpdateModelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateModelResponse**](UpdateModelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoute

> UpdateRouteResult updateRoute(apiId, routeId, updateRouteRequest, opts)



Updates a Route.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let routeId = "routeId_example"; // String | The route ID.
let updateRouteRequest = new AmazonApiGatewayV2.UpdateRouteRequest(); // UpdateRouteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoute(apiId, routeId, updateRouteRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **routeId** | **String**| The route ID. | 
 **updateRouteRequest** | [**UpdateRouteRequest**](UpdateRouteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRouteResult**](UpdateRouteResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRouteResponse

> UpdateRouteResponseResponse updateRouteResponse(apiId, routeId, routeResponseId, updateRouteResponseRequest, opts)



Updates a RouteResponse.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let routeId = "routeId_example"; // String | The route ID.
let routeResponseId = "routeResponseId_example"; // String | The route response ID.
let updateRouteResponseRequest = new AmazonApiGatewayV2.UpdateRouteResponseRequest(); // UpdateRouteResponseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRouteResponse(apiId, routeId, routeResponseId, updateRouteResponseRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **routeId** | **String**| The route ID. | 
 **routeResponseId** | **String**| The route response ID. | 
 **updateRouteResponseRequest** | [**UpdateRouteResponseRequest**](UpdateRouteResponseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRouteResponseResponse**](UpdateRouteResponseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStage

> UpdateStageResponse updateStage(apiId, stageName, updateStageRequest, opts)



Updates a Stage.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let apiId = "apiId_example"; // String | The API identifier.
let stageName = "stageName_example"; // String | The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters.
let updateStageRequest = new AmazonApiGatewayV2.UpdateStageRequest(); // UpdateStageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateStage(apiId, stageName, updateStageRequest, opts, (error, data, response) => {
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
 **apiId** | **String**| The API identifier. | 
 **stageName** | **String**| The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters. | 
 **updateStageRequest** | [**UpdateStageRequest**](UpdateStageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateStageResponse**](UpdateStageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVpcLink

> UpdateVpcLinkResponse updateVpcLink(vpcLinkId, updateVpcLinkRequest, opts)



Updates a VPC link.

### Example

```javascript
import AmazonApiGatewayV2 from 'amazon_api_gateway_v2';
let defaultClient = AmazonApiGatewayV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGatewayV2.DefaultApi();
let vpcLinkId = "vpcLinkId_example"; // String | The ID of the VPC link.
let updateVpcLinkRequest = new AmazonApiGatewayV2.UpdateVpcLinkRequest(); // UpdateVpcLinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVpcLink(vpcLinkId, updateVpcLinkRequest, opts, (error, data, response) => {
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
 **vpcLinkId** | **String**| The ID of the VPC link. | 
 **updateVpcLinkRequest** | [**UpdateVpcLinkRequest**](UpdateVpcLinkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVpcLinkResponse**](UpdateVpcLinkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

