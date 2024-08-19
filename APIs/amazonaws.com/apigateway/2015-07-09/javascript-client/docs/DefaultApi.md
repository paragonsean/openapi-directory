# AmazonApiGateway.DefaultApi

All URIs are relative to *http://apigateway.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApiKey**](DefaultApi.md#createApiKey) | **POST** /apikeys | 
[**createAuthorizer**](DefaultApi.md#createAuthorizer) | **POST** /restapis/{restapi_id}/authorizers | 
[**createBasePathMapping**](DefaultApi.md#createBasePathMapping) | **POST** /domainnames/{domain_name}/basepathmappings | 
[**createDeployment**](DefaultApi.md#createDeployment) | **POST** /restapis/{restapi_id}/deployments | 
[**createDocumentationPart**](DefaultApi.md#createDocumentationPart) | **POST** /restapis/{restapi_id}/documentation/parts | 
[**createDocumentationVersion**](DefaultApi.md#createDocumentationVersion) | **POST** /restapis/{restapi_id}/documentation/versions | 
[**createDomainName**](DefaultApi.md#createDomainName) | **POST** /domainnames | 
[**createModel**](DefaultApi.md#createModel) | **POST** /restapis/{restapi_id}/models | 
[**createRequestValidator**](DefaultApi.md#createRequestValidator) | **POST** /restapis/{restapi_id}/requestvalidators | 
[**createResource**](DefaultApi.md#createResource) | **POST** /restapis/{restapi_id}/resources/{parent_id} | 
[**createRestApi**](DefaultApi.md#createRestApi) | **POST** /restapis | 
[**createStage**](DefaultApi.md#createStage) | **POST** /restapis/{restapi_id}/stages | 
[**createUsagePlan**](DefaultApi.md#createUsagePlan) | **POST** /usageplans | 
[**createUsagePlanKey**](DefaultApi.md#createUsagePlanKey) | **POST** /usageplans/{usageplanId}/keys | 
[**createVpcLink**](DefaultApi.md#createVpcLink) | **POST** /vpclinks | 
[**deleteApiKey**](DefaultApi.md#deleteApiKey) | **DELETE** /apikeys/{api_Key} | 
[**deleteAuthorizer**](DefaultApi.md#deleteAuthorizer) | **DELETE** /restapis/{restapi_id}/authorizers/{authorizer_id} | 
[**deleteBasePathMapping**](DefaultApi.md#deleteBasePathMapping) | **DELETE** /domainnames/{domain_name}/basepathmappings/{base_path} | 
[**deleteClientCertificate**](DefaultApi.md#deleteClientCertificate) | **DELETE** /clientcertificates/{clientcertificate_id} | 
[**deleteDeployment**](DefaultApi.md#deleteDeployment) | **DELETE** /restapis/{restapi_id}/deployments/{deployment_id} | 
[**deleteDocumentationPart**](DefaultApi.md#deleteDocumentationPart) | **DELETE** /restapis/{restapi_id}/documentation/parts/{part_id} | 
[**deleteDocumentationVersion**](DefaultApi.md#deleteDocumentationVersion) | **DELETE** /restapis/{restapi_id}/documentation/versions/{doc_version} | 
[**deleteDomainName**](DefaultApi.md#deleteDomainName) | **DELETE** /domainnames/{domain_name} | 
[**deleteGatewayResponse**](DefaultApi.md#deleteGatewayResponse) | **DELETE** /restapis/{restapi_id}/gatewayresponses/{response_type} | 
[**deleteIntegration**](DefaultApi.md#deleteIntegration) | **DELETE** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/integration | 
[**deleteIntegrationResponse**](DefaultApi.md#deleteIntegrationResponse) | **DELETE** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/integration/responses/{status_code} | 
[**deleteMethod**](DefaultApi.md#deleteMethod) | **DELETE** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method} | 
[**deleteMethodResponse**](DefaultApi.md#deleteMethodResponse) | **DELETE** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/responses/{status_code} | 
[**deleteModel**](DefaultApi.md#deleteModel) | **DELETE** /restapis/{restapi_id}/models/{model_name} | 
[**deleteRequestValidator**](DefaultApi.md#deleteRequestValidator) | **DELETE** /restapis/{restapi_id}/requestvalidators/{requestvalidator_id} | 
[**deleteResource**](DefaultApi.md#deleteResource) | **DELETE** /restapis/{restapi_id}/resources/{resource_id} | 
[**deleteRestApi**](DefaultApi.md#deleteRestApi) | **DELETE** /restapis/{restapi_id} | 
[**deleteStage**](DefaultApi.md#deleteStage) | **DELETE** /restapis/{restapi_id}/stages/{stage_name} | 
[**deleteUsagePlan**](DefaultApi.md#deleteUsagePlan) | **DELETE** /usageplans/{usageplanId} | 
[**deleteUsagePlanKey**](DefaultApi.md#deleteUsagePlanKey) | **DELETE** /usageplans/{usageplanId}/keys/{keyId} | 
[**deleteVpcLink**](DefaultApi.md#deleteVpcLink) | **DELETE** /vpclinks/{vpclink_id} | 
[**flushStageAuthorizersCache**](DefaultApi.md#flushStageAuthorizersCache) | **DELETE** /restapis/{restapi_id}/stages/{stage_name}/cache/authorizers | 
[**flushStageCache**](DefaultApi.md#flushStageCache) | **DELETE** /restapis/{restapi_id}/stages/{stage_name}/cache/data | 
[**generateClientCertificate**](DefaultApi.md#generateClientCertificate) | **POST** /clientcertificates | 
[**getAccount**](DefaultApi.md#getAccount) | **GET** /account | 
[**getApiKey**](DefaultApi.md#getApiKey) | **GET** /apikeys/{api_Key} | 
[**getApiKeys**](DefaultApi.md#getApiKeys) | **GET** /apikeys | 
[**getAuthorizer**](DefaultApi.md#getAuthorizer) | **GET** /restapis/{restapi_id}/authorizers/{authorizer_id} | 
[**getAuthorizers**](DefaultApi.md#getAuthorizers) | **GET** /restapis/{restapi_id}/authorizers | 
[**getBasePathMapping**](DefaultApi.md#getBasePathMapping) | **GET** /domainnames/{domain_name}/basepathmappings/{base_path} | 
[**getBasePathMappings**](DefaultApi.md#getBasePathMappings) | **GET** /domainnames/{domain_name}/basepathmappings | 
[**getClientCertificate**](DefaultApi.md#getClientCertificate) | **GET** /clientcertificates/{clientcertificate_id} | 
[**getClientCertificates**](DefaultApi.md#getClientCertificates) | **GET** /clientcertificates | 
[**getDeployment**](DefaultApi.md#getDeployment) | **GET** /restapis/{restapi_id}/deployments/{deployment_id} | 
[**getDeployments**](DefaultApi.md#getDeployments) | **GET** /restapis/{restapi_id}/deployments | 
[**getDocumentationPart**](DefaultApi.md#getDocumentationPart) | **GET** /restapis/{restapi_id}/documentation/parts/{part_id} | 
[**getDocumentationParts**](DefaultApi.md#getDocumentationParts) | **GET** /restapis/{restapi_id}/documentation/parts | 
[**getDocumentationVersion**](DefaultApi.md#getDocumentationVersion) | **GET** /restapis/{restapi_id}/documentation/versions/{doc_version} | 
[**getDocumentationVersions**](DefaultApi.md#getDocumentationVersions) | **GET** /restapis/{restapi_id}/documentation/versions | 
[**getDomainName**](DefaultApi.md#getDomainName) | **GET** /domainnames/{domain_name} | 
[**getDomainNames**](DefaultApi.md#getDomainNames) | **GET** /domainnames | 
[**getExport**](DefaultApi.md#getExport) | **GET** /restapis/{restapi_id}/stages/{stage_name}/exports/{export_type} | 
[**getGatewayResponse**](DefaultApi.md#getGatewayResponse) | **GET** /restapis/{restapi_id}/gatewayresponses/{response_type} | 
[**getGatewayResponses**](DefaultApi.md#getGatewayResponses) | **GET** /restapis/{restapi_id}/gatewayresponses | 
[**getIntegration**](DefaultApi.md#getIntegration) | **GET** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/integration | 
[**getIntegrationResponse**](DefaultApi.md#getIntegrationResponse) | **GET** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/integration/responses/{status_code} | 
[**getMethod**](DefaultApi.md#getMethod) | **GET** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method} | 
[**getMethodResponse**](DefaultApi.md#getMethodResponse) | **GET** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/responses/{status_code} | 
[**getModel**](DefaultApi.md#getModel) | **GET** /restapis/{restapi_id}/models/{model_name} | 
[**getModelTemplate**](DefaultApi.md#getModelTemplate) | **GET** /restapis/{restapi_id}/models/{model_name}/default_template | 
[**getModels**](DefaultApi.md#getModels) | **GET** /restapis/{restapi_id}/models | 
[**getRequestValidator**](DefaultApi.md#getRequestValidator) | **GET** /restapis/{restapi_id}/requestvalidators/{requestvalidator_id} | 
[**getRequestValidators**](DefaultApi.md#getRequestValidators) | **GET** /restapis/{restapi_id}/requestvalidators | 
[**getResource**](DefaultApi.md#getResource) | **GET** /restapis/{restapi_id}/resources/{resource_id} | 
[**getResources**](DefaultApi.md#getResources) | **GET** /restapis/{restapi_id}/resources | 
[**getRestApi**](DefaultApi.md#getRestApi) | **GET** /restapis/{restapi_id} | 
[**getRestApis**](DefaultApi.md#getRestApis) | **GET** /restapis | 
[**getSdk**](DefaultApi.md#getSdk) | **GET** /restapis/{restapi_id}/stages/{stage_name}/sdks/{sdk_type} | 
[**getSdkType**](DefaultApi.md#getSdkType) | **GET** /sdktypes/{sdktype_id} | 
[**getSdkTypes**](DefaultApi.md#getSdkTypes) | **GET** /sdktypes | 
[**getStage**](DefaultApi.md#getStage) | **GET** /restapis/{restapi_id}/stages/{stage_name} | 
[**getStages**](DefaultApi.md#getStages) | **GET** /restapis/{restapi_id}/stages | 
[**getTags**](DefaultApi.md#getTags) | **GET** /tags/{resource_arn} | 
[**getUsage**](DefaultApi.md#getUsage) | **GET** /usageplans/{usageplanId}/usage#startDate&amp;endDate | 
[**getUsagePlan**](DefaultApi.md#getUsagePlan) | **GET** /usageplans/{usageplanId} | 
[**getUsagePlanKey**](DefaultApi.md#getUsagePlanKey) | **GET** /usageplans/{usageplanId}/keys/{keyId} | 
[**getUsagePlanKeys**](DefaultApi.md#getUsagePlanKeys) | **GET** /usageplans/{usageplanId}/keys | 
[**getUsagePlans**](DefaultApi.md#getUsagePlans) | **GET** /usageplans | 
[**getVpcLink**](DefaultApi.md#getVpcLink) | **GET** /vpclinks/{vpclink_id} | 
[**getVpcLinks**](DefaultApi.md#getVpcLinks) | **GET** /vpclinks | 
[**importApiKeys**](DefaultApi.md#importApiKeys) | **POST** /apikeys#mode&#x3D;import&amp;format | 
[**importDocumentationParts**](DefaultApi.md#importDocumentationParts) | **PUT** /restapis/{restapi_id}/documentation/parts | 
[**importRestApi**](DefaultApi.md#importRestApi) | **POST** /restapis#mode&#x3D;import | 
[**putGatewayResponse**](DefaultApi.md#putGatewayResponse) | **PUT** /restapis/{restapi_id}/gatewayresponses/{response_type} | 
[**putIntegration**](DefaultApi.md#putIntegration) | **PUT** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/integration | 
[**putIntegrationResponse**](DefaultApi.md#putIntegrationResponse) | **PUT** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/integration/responses/{status_code} | 
[**putMethod**](DefaultApi.md#putMethod) | **PUT** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method} | 
[**putMethodResponse**](DefaultApi.md#putMethodResponse) | **PUT** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/responses/{status_code} | 
[**putRestApi**](DefaultApi.md#putRestApi) | **PUT** /restapis/{restapi_id} | 
[**tagResource**](DefaultApi.md#tagResource) | **PUT** /tags/{resource_arn} | 
[**testInvokeAuthorizer**](DefaultApi.md#testInvokeAuthorizer) | **POST** /restapis/{restapi_id}/authorizers/{authorizer_id} | 
[**testInvokeMethod**](DefaultApi.md#testInvokeMethod) | **POST** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resource_arn}#tagKeys | 
[**updateAccount**](DefaultApi.md#updateAccount) | **PATCH** /account | 
[**updateApiKey**](DefaultApi.md#updateApiKey) | **PATCH** /apikeys/{api_Key} | 
[**updateAuthorizer**](DefaultApi.md#updateAuthorizer) | **PATCH** /restapis/{restapi_id}/authorizers/{authorizer_id} | 
[**updateBasePathMapping**](DefaultApi.md#updateBasePathMapping) | **PATCH** /domainnames/{domain_name}/basepathmappings/{base_path} | 
[**updateClientCertificate**](DefaultApi.md#updateClientCertificate) | **PATCH** /clientcertificates/{clientcertificate_id} | 
[**updateDeployment**](DefaultApi.md#updateDeployment) | **PATCH** /restapis/{restapi_id}/deployments/{deployment_id} | 
[**updateDocumentationPart**](DefaultApi.md#updateDocumentationPart) | **PATCH** /restapis/{restapi_id}/documentation/parts/{part_id} | 
[**updateDocumentationVersion**](DefaultApi.md#updateDocumentationVersion) | **PATCH** /restapis/{restapi_id}/documentation/versions/{doc_version} | 
[**updateDomainName**](DefaultApi.md#updateDomainName) | **PATCH** /domainnames/{domain_name} | 
[**updateGatewayResponse**](DefaultApi.md#updateGatewayResponse) | **PATCH** /restapis/{restapi_id}/gatewayresponses/{response_type} | 
[**updateIntegration**](DefaultApi.md#updateIntegration) | **PATCH** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/integration | 
[**updateIntegrationResponse**](DefaultApi.md#updateIntegrationResponse) | **PATCH** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/integration/responses/{status_code} | 
[**updateMethod**](DefaultApi.md#updateMethod) | **PATCH** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method} | 
[**updateMethodResponse**](DefaultApi.md#updateMethodResponse) | **PATCH** /restapis/{restapi_id}/resources/{resource_id}/methods/{http_method}/responses/{status_code} | 
[**updateModel**](DefaultApi.md#updateModel) | **PATCH** /restapis/{restapi_id}/models/{model_name} | 
[**updateRequestValidator**](DefaultApi.md#updateRequestValidator) | **PATCH** /restapis/{restapi_id}/requestvalidators/{requestvalidator_id} | 
[**updateResource**](DefaultApi.md#updateResource) | **PATCH** /restapis/{restapi_id}/resources/{resource_id} | 
[**updateRestApi**](DefaultApi.md#updateRestApi) | **PATCH** /restapis/{restapi_id} | 
[**updateStage**](DefaultApi.md#updateStage) | **PATCH** /restapis/{restapi_id}/stages/{stage_name} | 
[**updateUsage**](DefaultApi.md#updateUsage) | **PATCH** /usageplans/{usageplanId}/keys/{keyId}/usage | 
[**updateUsagePlan**](DefaultApi.md#updateUsagePlan) | **PATCH** /usageplans/{usageplanId} | 
[**updateVpcLink**](DefaultApi.md#updateVpcLink) | **PATCH** /vpclinks/{vpclink_id} | 



## createApiKey

> ApiKey createApiKey(createApiKeyRequest, opts)



Create an ApiKey resource. 

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let createApiKeyRequest = new AmazonApiGateway.CreateApiKeyRequest(); // CreateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApiKey(createApiKeyRequest, opts, (error, data, response) => {
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
 **createApiKeyRequest** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAuthorizer

> Authorizer createAuthorizer(restapiId, createAuthorizerRequest, opts)



Adds a new Authorizer resource to an existing RestApi resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let createAuthorizerRequest = new AmazonApiGateway.CreateAuthorizerRequest(); // CreateAuthorizerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAuthorizer(restapiId, createAuthorizerRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **createAuthorizerRequest** | [**CreateAuthorizerRequest**](CreateAuthorizerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Authorizer**](Authorizer.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBasePathMapping

> BasePathMapping createBasePathMapping(domainName, createBasePathMappingRequest, opts)



Creates a new BasePathMapping resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let domainName = "domainName_example"; // String | The domain name of the BasePathMapping resource to create.
let createBasePathMappingRequest = new AmazonApiGateway.CreateBasePathMappingRequest(); // CreateBasePathMappingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBasePathMapping(domainName, createBasePathMappingRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name of the BasePathMapping resource to create. | 
 **createBasePathMappingRequest** | [**CreateBasePathMappingRequest**](CreateBasePathMappingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BasePathMapping**](BasePathMapping.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDeployment

> Deployment createDeployment(restapiId, createDeploymentRequest, opts)



Creates a Deployment resource, which makes a specified RestApi callable over the internet.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let createDeploymentRequest = new AmazonApiGateway.CreateDeploymentRequest(); // CreateDeploymentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDeployment(restapiId, createDeploymentRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **createDeploymentRequest** | [**CreateDeploymentRequest**](CreateDeploymentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDocumentationPart

> DocumentationPart createDocumentationPart(restapiId, createDocumentationPartRequest, opts)



Creates a documentation part.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let createDocumentationPartRequest = new AmazonApiGateway.CreateDocumentationPartRequest(); // CreateDocumentationPartRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDocumentationPart(restapiId, createDocumentationPartRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **createDocumentationPartRequest** | [**CreateDocumentationPartRequest**](CreateDocumentationPartRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DocumentationPart**](DocumentationPart.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDocumentationVersion

> DocumentationVersion createDocumentationVersion(restapiId, createDocumentationVersionRequest, opts)



Creates a documentation version

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let createDocumentationVersionRequest = new AmazonApiGateway.CreateDocumentationVersionRequest(); // CreateDocumentationVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDocumentationVersion(restapiId, createDocumentationVersionRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **createDocumentationVersionRequest** | [**CreateDocumentationVersionRequest**](CreateDocumentationVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DocumentationVersion**](DocumentationVersion.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDomainName

> DomainName createDomainName(createDomainNameRequest, opts)



Creates a new domain name.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let createDomainNameRequest = new AmazonApiGateway.CreateDomainNameRequest(); // CreateDomainNameRequest | 
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

[**DomainName**](DomainName.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createModel

> Model createModel(restapiId, createModelRequest, opts)



Adds a new Model resource to an existing RestApi resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The RestApi identifier under which the Model will be created.
let createModelRequest = new AmazonApiGateway.CreateModelRequest(); // CreateModelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createModel(restapiId, createModelRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The RestApi identifier under which the Model will be created. | 
 **createModelRequest** | [**CreateModelRequest**](CreateModelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRequestValidator

> RequestValidator createRequestValidator(restapiId, createRequestValidatorRequest, opts)



Creates a RequestValidator of a given RestApi.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let createRequestValidatorRequest = new AmazonApiGateway.CreateRequestValidatorRequest(); // CreateRequestValidatorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRequestValidator(restapiId, createRequestValidatorRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **createRequestValidatorRequest** | [**CreateRequestValidatorRequest**](CreateRequestValidatorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RequestValidator**](RequestValidator.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createResource

> Resource createResource(restapiId, parentId, createResourceRequest, opts)



Creates a Resource resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let parentId = "parentId_example"; // String | The parent resource's identifier.
let createResourceRequest = new AmazonApiGateway.CreateResourceRequest(); // CreateResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createResource(restapiId, parentId, createResourceRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **parentId** | **String**| The parent resource&#39;s identifier. | 
 **createResourceRequest** | [**CreateResourceRequest**](CreateResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Resource**](Resource.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRestApi

> RestApi createRestApi(createRestApiRequest, opts)



Creates a new RestApi resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let createRestApiRequest = new AmazonApiGateway.CreateRestApiRequest(); // CreateRestApiRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRestApi(createRestApiRequest, opts, (error, data, response) => {
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
 **createRestApiRequest** | [**CreateRestApiRequest**](CreateRestApiRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RestApi**](RestApi.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStage

> Stage createStage(restapiId, createStageRequest, opts)



Creates a new Stage resource that references a pre-existing Deployment for the API. 

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let createStageRequest = new AmazonApiGateway.CreateStageRequest(); // CreateStageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStage(restapiId, createStageRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **createStageRequest** | [**CreateStageRequest**](CreateStageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Stage**](Stage.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUsagePlan

> UsagePlan createUsagePlan(createUsagePlanRequest, opts)



Creates a usage plan with the throttle and quota limits, as well as the associated API stages, specified in the payload. 

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let createUsagePlanRequest = new AmazonApiGateway.CreateUsagePlanRequest(); // CreateUsagePlanRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUsagePlan(createUsagePlanRequest, opts, (error, data, response) => {
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
 **createUsagePlanRequest** | [**CreateUsagePlanRequest**](CreateUsagePlanRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UsagePlan**](UsagePlan.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUsagePlanKey

> UsagePlanKey createUsagePlanKey(usageplanId, createUsagePlanKeyRequest, opts)



Creates a usage plan key for adding an existing API key to a usage plan.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let usageplanId = "usageplanId_example"; // String | The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer.
let createUsagePlanKeyRequest = new AmazonApiGateway.CreateUsagePlanKeyRequest(); // CreateUsagePlanKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUsagePlanKey(usageplanId, createUsagePlanKeyRequest, opts, (error, data, response) => {
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
 **usageplanId** | **String**| The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer. | 
 **createUsagePlanKeyRequest** | [**CreateUsagePlanKeyRequest**](CreateUsagePlanKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UsagePlanKey**](UsagePlanKey.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVpcLink

> VpcLink createVpcLink(createVpcLinkRequest, opts)



Creates a VPC link, under the caller&#39;s account in a selected region, in an asynchronous operation that typically takes 2-4 minutes to complete and become operational. The caller must have permissions to create and update VPC Endpoint services.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let createVpcLinkRequest = new AmazonApiGateway.CreateVpcLinkRequest(); // CreateVpcLinkRequest | 
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

[**VpcLink**](VpcLink.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApiKey

> deleteApiKey(apiKey, opts)



Deletes the ApiKey resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let apiKey = "apiKey_example"; // String | The identifier of the ApiKey resource to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApiKey(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| The identifier of the ApiKey resource to be deleted. | 
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

> deleteAuthorizer(restapiId, authorizerId, opts)



Deletes an existing Authorizer resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let authorizerId = "authorizerId_example"; // String | The identifier of the Authorizer resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAuthorizer(restapiId, authorizerId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **authorizerId** | **String**| The identifier of the Authorizer resource. | 
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


## deleteBasePathMapping

> deleteBasePathMapping(domainName, basePath, opts)



Deletes the BasePathMapping resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let domainName = "domainName_example"; // String | The domain name of the BasePathMapping resource to delete.
let basePath = "basePath_example"; // String | <p>The base path name of the BasePathMapping resource to delete.</p> <p>To specify an empty base path, set this parameter to <code>'(none)'</code>.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBasePathMapping(domainName, basePath, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name of the BasePathMapping resource to delete. | 
 **basePath** | **String**| &lt;p&gt;The base path name of the BasePathMapping resource to delete.&lt;/p&gt; &lt;p&gt;To specify an empty base path, set this parameter to &lt;code&gt;&#39;(none)&#39;&lt;/code&gt;.&lt;/p&gt; | 
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


## deleteClientCertificate

> deleteClientCertificate(clientcertificateId, opts)



Deletes the ClientCertificate resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let clientcertificateId = "clientcertificateId_example"; // String | The identifier of the ClientCertificate resource to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteClientCertificate(clientcertificateId, opts, (error, data, response) => {
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
 **clientcertificateId** | **String**| The identifier of the ClientCertificate resource to be deleted. | 
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

> deleteDeployment(restapiId, deploymentId, opts)



Deletes a Deployment resource. Deleting a deployment will only succeed if there are no Stage resources associated with it.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let deploymentId = "deploymentId_example"; // String | The identifier of the Deployment resource to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDeployment(restapiId, deploymentId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **deploymentId** | **String**| The identifier of the Deployment resource to delete. | 
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


## deleteDocumentationPart

> deleteDocumentationPart(restapiId, partId, opts)



Deletes a documentation part

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let partId = "partId_example"; // String | The identifier of the to-be-deleted documentation part.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDocumentationPart(restapiId, partId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **partId** | **String**| The identifier of the to-be-deleted documentation part. | 
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


## deleteDocumentationVersion

> deleteDocumentationVersion(restapiId, docVersion, opts)



Deletes a documentation version.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let docVersion = "docVersion_example"; // String | The version identifier of a to-be-deleted documentation snapshot.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDocumentationVersion(restapiId, docVersion, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **docVersion** | **String**| The version identifier of a to-be-deleted documentation snapshot. | 
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



Deletes the DomainName resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let domainName = "domainName_example"; // String | The name of the DomainName resource to be deleted.
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
 **domainName** | **String**| The name of the DomainName resource to be deleted. | 
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


## deleteGatewayResponse

> deleteGatewayResponse(restapiId, responseType, opts)



Clears any customization of a GatewayResponse of a specified response type on the given RestApi and resets it with the default settings.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let responseType = "responseType_example"; // String | The response type of the associated GatewayResponse.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteGatewayResponse(restapiId, responseType, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **responseType** | **String**| The response type of the associated GatewayResponse. | 
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

> deleteIntegration(restapiId, resourceId, httpMethod, opts)



Represents a delete integration.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | Specifies a delete integration request's resource identifier.
let httpMethod = "httpMethod_example"; // String | Specifies a delete integration request's HTTP method.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIntegration(restapiId, resourceId, httpMethod, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| Specifies a delete integration request&#39;s resource identifier. | 
 **httpMethod** | **String**| Specifies a delete integration request&#39;s HTTP method. | 
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

> deleteIntegrationResponse(restapiId, resourceId, httpMethod, statusCode, opts)



Represents a delete integration response.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | Specifies a delete integration response request's resource identifier.
let httpMethod = "httpMethod_example"; // String | Specifies a delete integration response request's HTTP method.
let statusCode = "statusCode_example"; // String | Specifies a delete integration response request's status code.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIntegrationResponse(restapiId, resourceId, httpMethod, statusCode, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| Specifies a delete integration response request&#39;s resource identifier. | 
 **httpMethod** | **String**| Specifies a delete integration response request&#39;s HTTP method. | 
 **statusCode** | **String**| Specifies a delete integration response request&#39;s status code. | 
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


## deleteMethod

> deleteMethod(restapiId, resourceId, httpMethod, opts)



Deletes an existing Method resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The Resource identifier for the Method resource.
let httpMethod = "httpMethod_example"; // String | The HTTP verb of the Method resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMethod(restapiId, resourceId, httpMethod, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The Resource identifier for the Method resource. | 
 **httpMethod** | **String**| The HTTP verb of the Method resource. | 
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


## deleteMethodResponse

> deleteMethodResponse(restapiId, resourceId, httpMethod, statusCode, opts)



Deletes an existing MethodResponse resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The Resource identifier for the MethodResponse resource.
let httpMethod = "httpMethod_example"; // String | The HTTP verb of the Method resource.
let statusCode = "statusCode_example"; // String | The status code identifier for the MethodResponse resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMethodResponse(restapiId, resourceId, httpMethod, statusCode, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The Resource identifier for the MethodResponse resource. | 
 **httpMethod** | **String**| The HTTP verb of the Method resource. | 
 **statusCode** | **String**| The status code identifier for the MethodResponse resource. | 
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

> deleteModel(restapiId, modelName, opts)



Deletes a model.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let modelName = "modelName_example"; // String | The name of the model to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteModel(restapiId, modelName, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **modelName** | **String**| The name of the model to delete. | 
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


## deleteRequestValidator

> deleteRequestValidator(restapiId, requestvalidatorId, opts)



Deletes a RequestValidator of a given RestApi.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let requestvalidatorId = "requestvalidatorId_example"; // String | The identifier of the RequestValidator to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRequestValidator(restapiId, requestvalidatorId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **requestvalidatorId** | **String**| The identifier of the RequestValidator to be deleted. | 
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


## deleteResource

> deleteResource(restapiId, resourceId, opts)



Deletes a Resource resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The identifier of the Resource resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteResource(restapiId, resourceId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The identifier of the Resource resource. | 
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


## deleteRestApi

> deleteRestApi(restapiId, opts)



Deletes the specified API.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRestApi(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
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

> deleteStage(restapiId, stageName, opts)



Deletes a Stage resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let stageName = "stageName_example"; // String | The name of the Stage resource to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteStage(restapiId, stageName, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **stageName** | **String**| The name of the Stage resource to delete. | 
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


## deleteUsagePlan

> deleteUsagePlan(usageplanId, opts)



Deletes a usage plan of a given plan Id.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let usageplanId = "usageplanId_example"; // String | The Id of the to-be-deleted usage plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteUsagePlan(usageplanId, opts, (error, data, response) => {
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
 **usageplanId** | **String**| The Id of the to-be-deleted usage plan. | 
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


## deleteUsagePlanKey

> deleteUsagePlanKey(usageplanId, keyId, opts)



Deletes a usage plan key and remove the underlying API key from the associated usage plan.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let usageplanId = "usageplanId_example"; // String | The Id of the UsagePlan resource representing the usage plan containing the to-be-deleted UsagePlanKey resource representing a plan customer.
let keyId = "keyId_example"; // String | The Id of the UsagePlanKey resource to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteUsagePlanKey(usageplanId, keyId, opts, (error, data, response) => {
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
 **usageplanId** | **String**| The Id of the UsagePlan resource representing the usage plan containing the to-be-deleted UsagePlanKey resource representing a plan customer. | 
 **keyId** | **String**| The Id of the UsagePlanKey resource to be deleted. | 
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

> deleteVpcLink(vpclinkId, opts)



Deletes an existing VpcLink of a specified identifier.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let vpclinkId = "vpclinkId_example"; // String | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVpcLink(vpclinkId, opts, (error, data, response) => {
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
 **vpclinkId** | **String**| The identifier of the VpcLink. It is used in an Integration to reference this VpcLink. | 
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


## flushStageAuthorizersCache

> flushStageAuthorizersCache(restapiId, stageName, opts)



Flushes all authorizer cache entries on a stage.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let stageName = "stageName_example"; // String | The name of the stage to flush.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.flushStageAuthorizersCache(restapiId, stageName, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **stageName** | **String**| The name of the stage to flush. | 
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


## flushStageCache

> flushStageCache(restapiId, stageName, opts)



Flushes a stage&#39;s cache.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let stageName = "stageName_example"; // String | The name of the stage to flush its cache.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.flushStageCache(restapiId, stageName, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **stageName** | **String**| The name of the stage to flush its cache. | 
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


## generateClientCertificate

> ClientCertificate generateClientCertificate(generateClientCertificateRequest, opts)



Generates a ClientCertificate resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let generateClientCertificateRequest = new AmazonApiGateway.GenerateClientCertificateRequest(); // GenerateClientCertificateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.generateClientCertificate(generateClientCertificateRequest, opts, (error, data, response) => {
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
 **generateClientCertificateRequest** | [**GenerateClientCertificateRequest**](GenerateClientCertificateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ClientCertificate**](ClientCertificate.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccount

> Account getAccount(opts)



Gets information about the current Account resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccount(opts, (error, data, response) => {
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

### Return type

[**Account**](Account.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApiKey

> ApiKey getApiKey(apiKey, opts)



Gets information about the current ApiKey resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let apiKey = "apiKey_example"; // String | The identifier of the ApiKey resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'includeValue': true // Boolean | A boolean flag to specify whether (<code>true</code>) or not (<code>false</code>) the result contains the key value.
};
apiInstance.getApiKey(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| The identifier of the ApiKey resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **includeValue** | **Boolean**| A boolean flag to specify whether (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) the result contains the key value. | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApiKeys

> ApiKeys getApiKeys(opts)



Gets information about the current ApiKeys resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56, // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
  'name': "name_example", // String | The name of queried API keys.
  'customerId': "customerId_example", // String | The identifier of a customer in AWS Marketplace or an external system, such as a developer portal.
  'includeValues': true // Boolean | A boolean flag to specify whether (<code>true</code>) or not (<code>false</code>) the result contains key values.
};
apiInstance.getApiKeys(opts, (error, data, response) => {
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
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 
 **name** | **String**| The name of queried API keys. | [optional] 
 **customerId** | **String**| The identifier of a customer in AWS Marketplace or an external system, such as a developer portal. | [optional] 
 **includeValues** | **Boolean**| A boolean flag to specify whether (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) the result contains key values. | [optional] 

### Return type

[**ApiKeys**](ApiKeys.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthorizer

> Authorizer getAuthorizer(restapiId, authorizerId, opts)



Describe an existing Authorizer resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let authorizerId = "authorizerId_example"; // String | The identifier of the Authorizer resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAuthorizer(restapiId, authorizerId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **authorizerId** | **String**| The identifier of the Authorizer resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Authorizer**](Authorizer.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthorizers

> Authorizers getAuthorizers(restapiId, opts)



Describe an existing Authorizers resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getAuthorizers(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**Authorizers**](Authorizers.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBasePathMapping

> BasePathMapping getBasePathMapping(domainName, basePath, opts)



Describe a BasePathMapping resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let domainName = "domainName_example"; // String | The domain name of the BasePathMapping resource to be described.
let basePath = "basePath_example"; // String | The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify '(none)' if you do not want callers to specify any base path name after the domain name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBasePathMapping(domainName, basePath, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name of the BasePathMapping resource to be described. | 
 **basePath** | **String**| The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify &#39;(none)&#39; if you do not want callers to specify any base path name after the domain name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BasePathMapping**](BasePathMapping.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBasePathMappings

> BasePathMappings getBasePathMappings(domainName, opts)



Represents a collection of BasePathMapping resources.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let domainName = "domainName_example"; // String | The domain name of a BasePathMapping resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getBasePathMappings(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name of a BasePathMapping resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**BasePathMappings**](BasePathMappings.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClientCertificate

> ClientCertificate getClientCertificate(clientcertificateId, opts)



Gets information about the current ClientCertificate resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let clientcertificateId = "clientcertificateId_example"; // String | The identifier of the ClientCertificate resource to be described.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getClientCertificate(clientcertificateId, opts, (error, data, response) => {
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
 **clientcertificateId** | **String**| The identifier of the ClientCertificate resource to be described. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ClientCertificate**](ClientCertificate.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClientCertificates

> ClientCertificates getClientCertificates(opts)



Gets a collection of ClientCertificate resources.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getClientCertificates(opts, (error, data, response) => {
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
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**ClientCertificates**](ClientCertificates.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeployment

> Deployment getDeployment(restapiId, deploymentId, opts)



Gets information about a Deployment resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let deploymentId = "deploymentId_example"; // String | The identifier of the Deployment resource to get information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'embed': ["null"] // [String] | A query parameter to retrieve the specified embedded resources of the returned Deployment resource in the response. In a REST API call, this <code>embed</code> parameter value is a list of comma-separated strings, as in <code>GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=var1,var2</code>. The SDK and other platform-dependent libraries might use a different format for the list. Currently, this request supports only retrieval of the embedded API summary this way. Hence, the parameter value must be a single-valued list containing only the <code>\"apisummary\"</code> string. For example, <code>GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=apisummary</code>.
};
apiInstance.getDeployment(restapiId, deploymentId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **deploymentId** | **String**| The identifier of the Deployment resource to get information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **embed** | [**[String]**](String.md)| A query parameter to retrieve the specified embedded resources of the returned Deployment resource in the response. In a REST API call, this &lt;code&gt;embed&lt;/code&gt; parameter value is a list of comma-separated strings, as in &lt;code&gt;GET /restapis/{restapi_id}/deployments/{deployment_id}?embed&#x3D;var1,var2&lt;/code&gt;. The SDK and other platform-dependent libraries might use a different format for the list. Currently, this request supports only retrieval of the embedded API summary this way. Hence, the parameter value must be a single-valued list containing only the &lt;code&gt;\&quot;apisummary\&quot;&lt;/code&gt; string. For example, &lt;code&gt;GET /restapis/{restapi_id}/deployments/{deployment_id}?embed&#x3D;apisummary&lt;/code&gt;. | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeployments

> Deployments getDeployments(restapiId, opts)



Gets information about a Deployments collection.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getDeployments(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**Deployments**](Deployments.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentationPart

> DocumentationPart getDocumentationPart(restapiId, partId, opts)



Gets a documentation part.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let partId = "partId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDocumentationPart(restapiId, partId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **partId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DocumentationPart**](DocumentationPart.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentationParts

> DocumentationParts getDocumentationParts(restapiId, opts)



Gets documentation parts.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'type': "type_example", // String | The type of API entities of the to-be-retrieved documentation parts. 
  'name': "name_example", // String | The name of API entities of the to-be-retrieved documentation parts.
  'path': "path_example", // String | The path of API entities of the to-be-retrieved documentation parts.
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56, // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
  'locationStatus': "locationStatus_example" // String | The status of the API documentation parts to retrieve. Valid values are <code>DOCUMENTED</code> for retrieving DocumentationPart resources with content and <code>UNDOCUMENTED</code> for DocumentationPart resources without content.
};
apiInstance.getDocumentationParts(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **type** | **String**| The type of API entities of the to-be-retrieved documentation parts.  | [optional] 
 **name** | **String**| The name of API entities of the to-be-retrieved documentation parts. | [optional] 
 **path** | **String**| The path of API entities of the to-be-retrieved documentation parts. | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 
 **locationStatus** | **String**| The status of the API documentation parts to retrieve. Valid values are &lt;code&gt;DOCUMENTED&lt;/code&gt; for retrieving DocumentationPart resources with content and &lt;code&gt;UNDOCUMENTED&lt;/code&gt; for DocumentationPart resources without content. | [optional] 

### Return type

[**DocumentationParts**](DocumentationParts.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentationVersion

> DocumentationVersion getDocumentationVersion(restapiId, docVersion, opts)



Gets a documentation version.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let docVersion = "docVersion_example"; // String | The version identifier of the to-be-retrieved documentation snapshot.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDocumentationVersion(restapiId, docVersion, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **docVersion** | **String**| The version identifier of the to-be-retrieved documentation snapshot. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DocumentationVersion**](DocumentationVersion.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentationVersions

> DocumentationVersions getDocumentationVersions(restapiId, opts)



Gets documentation versions.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getDocumentationVersions(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**DocumentationVersions**](DocumentationVersions.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainName

> DomainName getDomainName(domainName, opts)



Represents a domain name that is contained in a simpler, more intuitive URL that can be called.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let domainName = "domainName_example"; // String | The name of the DomainName resource.
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
 **domainName** | **String**| The name of the DomainName resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DomainName**](DomainName.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainNames

> DomainNames getDomainNames(opts)



Represents a collection of DomainName resources.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
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
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**DomainNames**](DomainNames.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExport

> ExportResponse getExport(restapiId, stageName, exportType, opts)



Exports a deployed version of a RestApi in a specified format.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let stageName = "stageName_example"; // String | The name of the Stage that will be exported.
let exportType = "exportType_example"; // String | The type of export. Acceptable values are 'oas30' for OpenAPI 3.0.x and 'swagger' for Swagger/OpenAPI 2.0.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'parameters': {key: "null"}, // {String: String} | A key-value map of query string parameters that specify properties of the export, depending on the requested <code>exportType</code>. For <code>exportType</code> <code>oas30</code> and <code>swagger</code>, any combination of the following parameters are supported: <code>extensions='integrations'</code> or <code>extensions='apigateway'</code> will export the API with x-amazon-apigateway-integration extensions. <code>extensions='authorizers'</code> will export the API with x-amazon-apigateway-authorizer extensions. <code>postman</code> will export the API with Postman extensions, allowing for import to the Postman tool
  'accept': "accept_example" // String | The content-type of the export, for example <code>application/json</code>. Currently <code>application/json</code> and <code>application/yaml</code> are supported for <code>exportType</code> of<code>oas30</code> and <code>swagger</code>. This should be specified in the <code>Accept</code> header for direct API requests.
};
apiInstance.getExport(restapiId, stageName, exportType, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **stageName** | **String**| The name of the Stage that will be exported. | 
 **exportType** | **String**| The type of export. Acceptable values are &#39;oas30&#39; for OpenAPI 3.0.x and &#39;swagger&#39; for Swagger/OpenAPI 2.0. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **parameters** | [**{String: String}**](String.md)| A key-value map of query string parameters that specify properties of the export, depending on the requested &lt;code&gt;exportType&lt;/code&gt;. For &lt;code&gt;exportType&lt;/code&gt; &lt;code&gt;oas30&lt;/code&gt; and &lt;code&gt;swagger&lt;/code&gt;, any combination of the following parameters are supported: &lt;code&gt;extensions&#x3D;&#39;integrations&#39;&lt;/code&gt; or &lt;code&gt;extensions&#x3D;&#39;apigateway&#39;&lt;/code&gt; will export the API with x-amazon-apigateway-integration extensions. &lt;code&gt;extensions&#x3D;&#39;authorizers&#39;&lt;/code&gt; will export the API with x-amazon-apigateway-authorizer extensions. &lt;code&gt;postman&lt;/code&gt; will export the API with Postman extensions, allowing for import to the Postman tool | [optional] 
 **accept** | **String**| The content-type of the export, for example &lt;code&gt;application/json&lt;/code&gt;. Currently &lt;code&gt;application/json&lt;/code&gt; and &lt;code&gt;application/yaml&lt;/code&gt; are supported for &lt;code&gt;exportType&lt;/code&gt; of&lt;code&gt;oas30&lt;/code&gt; and &lt;code&gt;swagger&lt;/code&gt;. This should be specified in the &lt;code&gt;Accept&lt;/code&gt; header for direct API requests. | [optional] 

### Return type

[**ExportResponse**](ExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGatewayResponse

> GatewayResponse getGatewayResponse(restapiId, responseType, opts)



Gets a GatewayResponse of a specified response type on the given RestApi.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let responseType = "responseType_example"; // String | The response type of the associated GatewayResponse.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGatewayResponse(restapiId, responseType, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **responseType** | **String**| The response type of the associated GatewayResponse. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GatewayResponse**](GatewayResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGatewayResponses

> GatewayResponses getGatewayResponses(restapiId, opts)



Gets the GatewayResponses collection on the given RestApi. If an API developer has not added any definitions for gateway responses, the result will be the API Gateway-generated default GatewayResponses collection for the supported response types.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set. The GatewayResponse collection does not support pagination and the position does not apply here.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. The GatewayResponses collection does not support pagination and the limit does not apply here.
};
apiInstance.getGatewayResponses(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| The current pagination position in the paged result set. The GatewayResponse collection does not support pagination and the position does not apply here. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. The GatewayResponses collection does not support pagination and the limit does not apply here. | [optional] 

### Return type

[**GatewayResponses**](GatewayResponses.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegration

> Integration getIntegration(restapiId, resourceId, httpMethod, opts)



Get the integration settings.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | Specifies a get integration request's resource identifier
let httpMethod = "httpMethod_example"; // String | Specifies a get integration request's HTTP method.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIntegration(restapiId, resourceId, httpMethod, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| Specifies a get integration request&#39;s resource identifier | 
 **httpMethod** | **String**| Specifies a get integration request&#39;s HTTP method. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Integration**](Integration.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegrationResponse

> IntegrationResponse getIntegrationResponse(restapiId, resourceId, httpMethod, statusCode, opts)



Represents a get integration response.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | Specifies a get integration response request's resource identifier.
let httpMethod = "httpMethod_example"; // String | Specifies a get integration response request's HTTP method.
let statusCode = "statusCode_example"; // String | Specifies a get integration response request's status code.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIntegrationResponse(restapiId, resourceId, httpMethod, statusCode, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| Specifies a get integration response request&#39;s resource identifier. | 
 **httpMethod** | **String**| Specifies a get integration response request&#39;s HTTP method. | 
 **statusCode** | **String**| Specifies a get integration response request&#39;s status code. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMethod

> Method getMethod(restapiId, resourceId, httpMethod, opts)



Describe an existing Method resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The Resource identifier for the Method resource.
let httpMethod = "httpMethod_example"; // String | Specifies the method request's HTTP method type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMethod(restapiId, resourceId, httpMethod, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The Resource identifier for the Method resource. | 
 **httpMethod** | **String**| Specifies the method request&#39;s HTTP method type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Method**](Method.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMethodResponse

> MethodResponse getMethodResponse(restapiId, resourceId, httpMethod, statusCode, opts)



Describes a MethodResponse resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The Resource identifier for the MethodResponse resource.
let httpMethod = "httpMethod_example"; // String | The HTTP verb of the Method resource.
let statusCode = "statusCode_example"; // String | The status code for the MethodResponse resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMethodResponse(restapiId, resourceId, httpMethod, statusCode, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The Resource identifier for the MethodResponse resource. | 
 **httpMethod** | **String**| The HTTP verb of the Method resource. | 
 **statusCode** | **String**| The status code for the MethodResponse resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**MethodResponse**](MethodResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModel

> Model getModel(restapiId, modelName, opts)



Describes an existing model defined for a RestApi resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The RestApi identifier under which the Model exists.
let modelName = "modelName_example"; // String | The name of the model as an identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'flatten': true // Boolean | A query parameter of a Boolean value to resolve (<code>true</code>) all external model references and returns a flattened model schema or not (<code>false</code>) The default is <code>false</code>.
};
apiInstance.getModel(restapiId, modelName, opts, (error, data, response) => {
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
 **restapiId** | **String**| The RestApi identifier under which the Model exists. | 
 **modelName** | **String**| The name of the model as an identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **flatten** | **Boolean**| A query parameter of a Boolean value to resolve (&lt;code&gt;true&lt;/code&gt;) all external model references and returns a flattened model schema or not (&lt;code&gt;false&lt;/code&gt;) The default is &lt;code&gt;false&lt;/code&gt;. | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelTemplate

> Template getModelTemplate(restapiId, modelName, opts)



Generates a sample mapping template that can be used to transform a payload into the structure of a model.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let modelName = "modelName_example"; // String | The name of the model for which to generate a template.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getModelTemplate(restapiId, modelName, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **modelName** | **String**| The name of the model for which to generate a template. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModels

> Models getModels(restapiId, opts)



Describes existing Models defined for a RestApi resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getModels(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**Models**](Models.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRequestValidator

> RequestValidator getRequestValidator(restapiId, requestvalidatorId, opts)



Gets a RequestValidator of a given RestApi.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let requestvalidatorId = "requestvalidatorId_example"; // String | The identifier of the RequestValidator to be retrieved.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRequestValidator(restapiId, requestvalidatorId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **requestvalidatorId** | **String**| The identifier of the RequestValidator to be retrieved. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RequestValidator**](RequestValidator.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRequestValidators

> RequestValidators getRequestValidators(restapiId, opts)



Gets the RequestValidators collection of a given RestApi.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getRequestValidators(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**RequestValidators**](RequestValidators.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResource

> Resource getResource(restapiId, resourceId, opts)



Lists information about a resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The identifier for the Resource resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'embed': ["null"] // [String] | A query parameter to retrieve the specified resources embedded in the returned Resource representation in the response. This <code>embed</code> parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the <code>\"methods\"</code> string. For example, <code>GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods</code>.
};
apiInstance.getResource(restapiId, resourceId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The identifier for the Resource resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **embed** | [**[String]**](String.md)| A query parameter to retrieve the specified resources embedded in the returned Resource representation in the response. This &lt;code&gt;embed&lt;/code&gt; parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the &lt;code&gt;\&quot;methods\&quot;&lt;/code&gt; string. For example, &lt;code&gt;GET /restapis/{restapi_id}/resources/{resource_id}?embed&#x3D;methods&lt;/code&gt;. | [optional] 

### Return type

[**Resource**](Resource.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResources

> Resources getResources(restapiId, opts)



Lists information about a collection of Resource resources.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56, // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
  'embed': ["null"] // [String] | A query parameter used to retrieve the specified resources embedded in the returned Resources resource in the response. This <code>embed</code> parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the <code>\"methods\"</code> string. For example, <code>GET /restapis/{restapi_id}/resources?embed=methods</code>.
};
apiInstance.getResources(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 
 **embed** | [**[String]**](String.md)| A query parameter used to retrieve the specified resources embedded in the returned Resources resource in the response. This &lt;code&gt;embed&lt;/code&gt; parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the &lt;code&gt;\&quot;methods\&quot;&lt;/code&gt; string. For example, &lt;code&gt;GET /restapis/{restapi_id}/resources?embed&#x3D;methods&lt;/code&gt;. | [optional] 

### Return type

[**Resources**](Resources.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRestApi

> RestApi getRestApi(restapiId, opts)



Lists the RestApi resource in the collection.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRestApi(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RestApi**](RestApi.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRestApis

> RestApis getRestApis(opts)



Lists the RestApis resources for your collection.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getRestApis(opts, (error, data, response) => {
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
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**RestApis**](RestApis.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSdk

> SdkResponse getSdk(restapiId, stageName, sdkType, opts)



Generates a client SDK for a RestApi and Stage.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let stageName = "stageName_example"; // String | The name of the Stage that the SDK will use.
let sdkType = "sdkType_example"; // String | The language for the generated SDK. Currently <code>java</code>, <code>javascript</code>, <code>android</code>, <code>objectivec</code> (for iOS), <code>swift</code> (for iOS), and <code>ruby</code> are supported.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'parameters': {key: "null"} // {String: String} | A string-to-string key-value map of query parameters <code>sdkType</code>-dependent properties of the SDK. For <code>sdkType</code> of <code>objectivec</code> or <code>swift</code>, a parameter named <code>classPrefix</code> is required. For <code>sdkType</code> of <code>android</code>, parameters named <code>groupId</code>, <code>artifactId</code>, <code>artifactVersion</code>, and <code>invokerPackage</code> are required. For <code>sdkType</code> of <code>java</code>, parameters named <code>serviceName</code> and <code>javaPackageName</code> are required. 
};
apiInstance.getSdk(restapiId, stageName, sdkType, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **stageName** | **String**| The name of the Stage that the SDK will use. | 
 **sdkType** | **String**| The language for the generated SDK. Currently &lt;code&gt;java&lt;/code&gt;, &lt;code&gt;javascript&lt;/code&gt;, &lt;code&gt;android&lt;/code&gt;, &lt;code&gt;objectivec&lt;/code&gt; (for iOS), &lt;code&gt;swift&lt;/code&gt; (for iOS), and &lt;code&gt;ruby&lt;/code&gt; are supported. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **parameters** | [**{String: String}**](String.md)| A string-to-string key-value map of query parameters &lt;code&gt;sdkType&lt;/code&gt;-dependent properties of the SDK. For &lt;code&gt;sdkType&lt;/code&gt; of &lt;code&gt;objectivec&lt;/code&gt; or &lt;code&gt;swift&lt;/code&gt;, a parameter named &lt;code&gt;classPrefix&lt;/code&gt; is required. For &lt;code&gt;sdkType&lt;/code&gt; of &lt;code&gt;android&lt;/code&gt;, parameters named &lt;code&gt;groupId&lt;/code&gt;, &lt;code&gt;artifactId&lt;/code&gt;, &lt;code&gt;artifactVersion&lt;/code&gt;, and &lt;code&gt;invokerPackage&lt;/code&gt; are required. For &lt;code&gt;sdkType&lt;/code&gt; of &lt;code&gt;java&lt;/code&gt;, parameters named &lt;code&gt;serviceName&lt;/code&gt; and &lt;code&gt;javaPackageName&lt;/code&gt; are required.  | [optional] 

### Return type

[**SdkResponse**](SdkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSdkType

> SdkType getSdkType(sdktypeId, opts)



Gets an SDK type.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let sdktypeId = "sdktypeId_example"; // String | The identifier of the queried SdkType instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSdkType(sdktypeId, opts, (error, data, response) => {
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
 **sdktypeId** | **String**| The identifier of the queried SdkType instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SdkType**](SdkType.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSdkTypes

> SdkTypes getSdkTypes(opts)



Gets SDK types

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getSdkTypes(opts, (error, data, response) => {
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
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**SdkTypes**](SdkTypes.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStage

> Stage getStage(restapiId, stageName, opts)



Gets information about a Stage resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let stageName = "stageName_example"; // String | The name of the Stage resource to get information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStage(restapiId, stageName, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **stageName** | **String**| The name of the Stage resource to get information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Stage**](Stage.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStages

> Stages getStages(restapiId, opts)



Gets information about one or more Stage resources.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'deploymentId': "deploymentId_example" // String | The stages' deployment identifiers.
};
apiInstance.getStages(restapiId, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **deploymentId** | **String**| The stages&#39; deployment identifiers. | [optional] 

### Return type

[**Stages**](Stages.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTags

> Tags getTags(resourceArn, opts)



Gets the Tags collection for a given resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of a resource that can be tagged.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | (Not currently supported) The current pagination position in the paged result set.
  'limit': 56 // Number | (Not currently supported) The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
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
 **resourceArn** | **String**| The ARN of a resource that can be tagged. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| (Not currently supported) The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| (Not currently supported) The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**Tags**](Tags.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsage

> Usage getUsage(usageplanId, startDate, endDate, opts)



Gets the usage data of a usage plan in a specified time interval.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let usageplanId = "usageplanId_example"; // String | The Id of the usage plan associated with the usage data.
let startDate = "startDate_example"; // String | The starting date (e.g., 2016-01-01) of the usage data.
let endDate = "endDate_example"; // String | The ending date (e.g., 2016-12-31) of the usage data.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'keyId': "keyId_example", // String | The Id of the API key associated with the resultant usage data.
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getUsage(usageplanId, startDate, endDate, opts, (error, data, response) => {
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
 **usageplanId** | **String**| The Id of the usage plan associated with the usage data. | 
 **startDate** | **String**| The starting date (e.g., 2016-01-01) of the usage data. | 
 **endDate** | **String**| The ending date (e.g., 2016-12-31) of the usage data. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **keyId** | **String**| The Id of the API key associated with the resultant usage data. | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**Usage**](Usage.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsagePlan

> UsagePlan getUsagePlan(usageplanId, opts)



Gets a usage plan of a given plan identifier.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let usageplanId = "usageplanId_example"; // String | The identifier of the UsagePlan resource to be retrieved.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getUsagePlan(usageplanId, opts, (error, data, response) => {
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
 **usageplanId** | **String**| The identifier of the UsagePlan resource to be retrieved. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UsagePlan**](UsagePlan.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsagePlanKey

> UsagePlanKey getUsagePlanKey(usageplanId, keyId, opts)



Gets a usage plan key of a given key identifier.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let usageplanId = "usageplanId_example"; // String | The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
let keyId = "keyId_example"; // String | The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getUsagePlanKey(usageplanId, keyId, opts, (error, data, response) => {
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
 **usageplanId** | **String**| The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer. | 
 **keyId** | **String**| The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UsagePlanKey**](UsagePlanKey.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsagePlanKeys

> UsagePlanKeys getUsagePlanKeys(usageplanId, opts)



Gets all the usage plan keys representing the API keys added to a specified usage plan.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let usageplanId = "usageplanId_example"; // String | The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56, // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
  'name': "name_example" // String | A query parameter specifying the name of the to-be-returned usage plan keys.
};
apiInstance.getUsagePlanKeys(usageplanId, opts, (error, data, response) => {
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
 **usageplanId** | **String**| The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 
 **name** | **String**| A query parameter specifying the name of the to-be-returned usage plan keys. | [optional] 

### Return type

[**UsagePlanKeys**](UsagePlanKeys.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsagePlans

> UsagePlans getUsagePlans(opts)



Gets all the usage plans of the caller&#39;s account.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'keyId': "keyId_example", // String | The identifier of the API key associated with the usage plans.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
};
apiInstance.getUsagePlans(opts, (error, data, response) => {
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
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **keyId** | **String**| The identifier of the API key associated with the usage plans. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**UsagePlans**](UsagePlans.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVpcLink

> VpcLink getVpcLink(vpclinkId, opts)



Gets a specified VPC link under the caller&#39;s account in a region.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let vpclinkId = "vpclinkId_example"; // String | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVpcLink(vpclinkId, opts, (error, data, response) => {
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
 **vpclinkId** | **String**| The identifier of the VpcLink. It is used in an Integration to reference this VpcLink. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**VpcLink**](VpcLink.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVpcLinks

> VpcLinks getVpcLinks(opts)



Gets the VpcLinks collection under the caller&#39;s account in a selected region.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'position': "position_example", // String | The current pagination position in the paged result set.
  'limit': 56 // Number | The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
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
 **position** | **String**| The current pagination position in the paged result set. | [optional] 
 **limit** | **Number**| The maximum number of returned results per page. The default value is 25 and the maximum value is 500. | [optional] 

### Return type

[**VpcLinks**](VpcLinks.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importApiKeys

> ApiKeyIds importApiKeys(format, mode, importApiKeysRequest, opts)



Import API keys from an external source, such as a CSV-formatted file.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let format = "format_example"; // String | A query parameter to specify the input format to imported API keys. Currently, only the <code>csv</code> format is supported.
let mode = "mode_example"; // String | 
let importApiKeysRequest = new AmazonApiGateway.ImportApiKeysRequest(); // ImportApiKeysRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'failonwarnings': true // Boolean | A query parameter to indicate whether to rollback ApiKey importation (<code>true</code>) or not (<code>false</code>) when error is encountered.
};
apiInstance.importApiKeys(format, mode, importApiKeysRequest, opts, (error, data, response) => {
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
 **format** | **String**| A query parameter to specify the input format to imported API keys. Currently, only the &lt;code&gt;csv&lt;/code&gt; format is supported. | 
 **mode** | **String**|  | 
 **importApiKeysRequest** | [**ImportApiKeysRequest**](ImportApiKeysRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **failonwarnings** | **Boolean**| A query parameter to indicate whether to rollback ApiKey importation (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) when error is encountered. | [optional] 

### Return type

[**ApiKeyIds**](ApiKeyIds.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importDocumentationParts

> DocumentationPartIds importDocumentationParts(restapiId, importDocumentationPartsRequest, opts)



Imports documentation parts

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let importDocumentationPartsRequest = new AmazonApiGateway.ImportDocumentationPartsRequest(); // ImportDocumentationPartsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'mode': "mode_example", // String | A query parameter to indicate whether to overwrite (<code>OVERWRITE</code>) any existing DocumentationParts definition or to merge (<code>MERGE</code>) the new definition into the existing one. The default value is <code>MERGE</code>.
  'failonwarnings': true // Boolean | A query parameter to specify whether to rollback the documentation importation (<code>true</code>) or not (<code>false</code>) when a warning is encountered. The default value is <code>false</code>.
};
apiInstance.importDocumentationParts(restapiId, importDocumentationPartsRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **importDocumentationPartsRequest** | [**ImportDocumentationPartsRequest**](ImportDocumentationPartsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **mode** | **String**| A query parameter to indicate whether to overwrite (&lt;code&gt;OVERWRITE&lt;/code&gt;) any existing DocumentationParts definition or to merge (&lt;code&gt;MERGE&lt;/code&gt;) the new definition into the existing one. The default value is &lt;code&gt;MERGE&lt;/code&gt;. | [optional] 
 **failonwarnings** | **Boolean**| A query parameter to specify whether to rollback the documentation importation (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) when a warning is encountered. The default value is &lt;code&gt;false&lt;/code&gt;. | [optional] 

### Return type

[**DocumentationPartIds**](DocumentationPartIds.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importRestApi

> RestApi importRestApi(mode, importRestApiRequest, opts)



A feature of the API Gateway control service for creating a new API from an external API definition file.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let mode = "mode_example"; // String | 
let importRestApiRequest = new AmazonApiGateway.ImportRestApiRequest(); // ImportRestApiRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'failonwarnings': true, // Boolean | A query parameter to indicate whether to rollback the API creation (<code>true</code>) or not (<code>false</code>) when a warning is encountered. The default value is <code>false</code>.
  'parameters': {key: "null"} // {String: String} | <p>A key-value map of context-specific query string parameters specifying the behavior of different API importing operations. The following shows operation-specific parameters and their supported values.</p> <p> To exclude DocumentationParts from the import, set <code>parameters</code> as <code>ignore=documentation</code>.</p> <p> To configure the endpoint type, set <code>parameters</code> as <code>endpointConfigurationTypes=EDGE</code>, <code>endpointConfigurationTypes=REGIONAL</code>, or <code>endpointConfigurationTypes=PRIVATE</code>. The default endpoint type is <code>EDGE</code>.</p> <p> To handle imported <code>basepath</code>, set <code>parameters</code> as <code>basepath=ignore</code>, <code>basepath=prepend</code> or <code>basepath=split</code>.</p> <p>For example, the AWS CLI command to exclude documentation from the imported API is:</p> <p>The AWS CLI command to set the regional endpoint on the imported API is:</p>
};
apiInstance.importRestApi(mode, importRestApiRequest, opts, (error, data, response) => {
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
 **mode** | **String**|  | 
 **importRestApiRequest** | [**ImportRestApiRequest**](ImportRestApiRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **failonwarnings** | **Boolean**| A query parameter to indicate whether to rollback the API creation (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) when a warning is encountered. The default value is &lt;code&gt;false&lt;/code&gt;. | [optional] 
 **parameters** | [**{String: String}**](String.md)| &lt;p&gt;A key-value map of context-specific query string parameters specifying the behavior of different API importing operations. The following shows operation-specific parameters and their supported values.&lt;/p&gt; &lt;p&gt; To exclude DocumentationParts from the import, set &lt;code&gt;parameters&lt;/code&gt; as &lt;code&gt;ignore&#x3D;documentation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; To configure the endpoint type, set &lt;code&gt;parameters&lt;/code&gt; as &lt;code&gt;endpointConfigurationTypes&#x3D;EDGE&lt;/code&gt;, &lt;code&gt;endpointConfigurationTypes&#x3D;REGIONAL&lt;/code&gt;, or &lt;code&gt;endpointConfigurationTypes&#x3D;PRIVATE&lt;/code&gt;. The default endpoint type is &lt;code&gt;EDGE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; To handle imported &lt;code&gt;basepath&lt;/code&gt;, set &lt;code&gt;parameters&lt;/code&gt; as &lt;code&gt;basepath&#x3D;ignore&lt;/code&gt;, &lt;code&gt;basepath&#x3D;prepend&lt;/code&gt; or &lt;code&gt;basepath&#x3D;split&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For example, the AWS CLI command to exclude documentation from the imported API is:&lt;/p&gt; &lt;p&gt;The AWS CLI command to set the regional endpoint on the imported API is:&lt;/p&gt; | [optional] 

### Return type

[**RestApi**](RestApi.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putGatewayResponse

> GatewayResponse putGatewayResponse(restapiId, responseType, putGatewayResponseRequest, opts)



Creates a customization of a GatewayResponse of a specified response type and status code on the given RestApi.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let responseType = "responseType_example"; // String | The response type of the associated GatewayResponse
let putGatewayResponseRequest = new AmazonApiGateway.PutGatewayResponseRequest(); // PutGatewayResponseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putGatewayResponse(restapiId, responseType, putGatewayResponseRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **responseType** | **String**| The response type of the associated GatewayResponse | 
 **putGatewayResponseRequest** | [**PutGatewayResponseRequest**](PutGatewayResponseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GatewayResponse**](GatewayResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putIntegration

> Integration putIntegration(restapiId, resourceId, httpMethod, putIntegrationRequest, opts)



Sets up a method&#39;s integration.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | Specifies a put integration request's resource ID.
let httpMethod = "httpMethod_example"; // String | Specifies the HTTP method for the integration.
let putIntegrationRequest = new AmazonApiGateway.PutIntegrationRequest(); // PutIntegrationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putIntegration(restapiId, resourceId, httpMethod, putIntegrationRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| Specifies a put integration request&#39;s resource ID. | 
 **httpMethod** | **String**| Specifies the HTTP method for the integration. | 
 **putIntegrationRequest** | [**PutIntegrationRequest**](PutIntegrationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Integration**](Integration.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putIntegrationResponse

> IntegrationResponse putIntegrationResponse(restapiId, resourceId, httpMethod, statusCode, putIntegrationResponseRequest, opts)



Represents a put integration.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | Specifies a put integration response request's resource identifier.
let httpMethod = "httpMethod_example"; // String | Specifies a put integration response request's HTTP method.
let statusCode = "statusCode_example"; // String | Specifies the status code that is used to map the integration response to an existing MethodResponse.
let putIntegrationResponseRequest = new AmazonApiGateway.PutIntegrationResponseRequest(); // PutIntegrationResponseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putIntegrationResponse(restapiId, resourceId, httpMethod, statusCode, putIntegrationResponseRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| Specifies a put integration response request&#39;s resource identifier. | 
 **httpMethod** | **String**| Specifies a put integration response request&#39;s HTTP method. | 
 **statusCode** | **String**| Specifies the status code that is used to map the integration response to an existing MethodResponse. | 
 **putIntegrationResponseRequest** | [**PutIntegrationResponseRequest**](PutIntegrationResponseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putMethod

> Method putMethod(restapiId, resourceId, httpMethod, putMethodRequest, opts)



Add a method to an existing Resource resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The Resource identifier for the new Method resource.
let httpMethod = "httpMethod_example"; // String | Specifies the method request's HTTP method type.
let putMethodRequest = new AmazonApiGateway.PutMethodRequest(); // PutMethodRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putMethod(restapiId, resourceId, httpMethod, putMethodRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The Resource identifier for the new Method resource. | 
 **httpMethod** | **String**| Specifies the method request&#39;s HTTP method type. | 
 **putMethodRequest** | [**PutMethodRequest**](PutMethodRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Method**](Method.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putMethodResponse

> MethodResponse putMethodResponse(restapiId, resourceId, httpMethod, statusCode, putMethodResponseRequest, opts)



Adds a MethodResponse to an existing Method resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The Resource identifier for the Method resource.
let httpMethod = "httpMethod_example"; // String | The HTTP verb of the Method resource.
let statusCode = "statusCode_example"; // String | The method response's status code.
let putMethodResponseRequest = new AmazonApiGateway.PutMethodResponseRequest(); // PutMethodResponseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putMethodResponse(restapiId, resourceId, httpMethod, statusCode, putMethodResponseRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The Resource identifier for the Method resource. | 
 **httpMethod** | **String**| The HTTP verb of the Method resource. | 
 **statusCode** | **String**| The method response&#39;s status code. | 
 **putMethodResponseRequest** | [**PutMethodResponseRequest**](PutMethodResponseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**MethodResponse**](MethodResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putRestApi

> RestApi putRestApi(restapiId, putRestApiRequest, opts)



A feature of the API Gateway control service for updating an existing API with an input of external API definitions. The update can take the form of merging the supplied definition into the existing API or overwriting the existing API.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let putRestApiRequest = new AmazonApiGateway.PutRestApiRequest(); // PutRestApiRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'mode': "mode_example", // String | The <code>mode</code> query parameter to specify the update mode. Valid values are \"merge\" and \"overwrite\". By default, the update mode is \"merge\".
  'failonwarnings': true, // Boolean | A query parameter to indicate whether to rollback the API update (<code>true</code>) or not (<code>false</code>) when a warning is encountered. The default value is <code>false</code>.
  'parameters': {key: "null"} // {String: String} | Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set <code>ignore=documentation</code> as a <code>parameters</code> value, as in the AWS CLI command of <code>aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json'</code>.
};
apiInstance.putRestApi(restapiId, putRestApiRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **putRestApiRequest** | [**PutRestApiRequest**](PutRestApiRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **mode** | **String**| The &lt;code&gt;mode&lt;/code&gt; query parameter to specify the update mode. Valid values are \&quot;merge\&quot; and \&quot;overwrite\&quot;. By default, the update mode is \&quot;merge\&quot;. | [optional] 
 **failonwarnings** | **Boolean**| A query parameter to indicate whether to rollback the API update (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) when a warning is encountered. The default value is &lt;code&gt;false&lt;/code&gt;. | [optional] 
 **parameters** | [**{String: String}**](String.md)| Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set &lt;code&gt;ignore&#x3D;documentation&lt;/code&gt; as a &lt;code&gt;parameters&lt;/code&gt; value, as in the AWS CLI command of &lt;code&gt;aws apigateway import-rest-api --parameters ignore&#x3D;documentation --body &#39;file:///path/to/imported-api-body.json&#39;&lt;/code&gt;. | [optional] 

### Return type

[**RestApi**](RestApi.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> tagResource(resourceArn, tagResourceRequest, opts)



Adds or updates a tag on a given resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of a resource that can be tagged.
let tagResourceRequest = new AmazonApiGateway.TagResourceRequest(); // TagResourceRequest | 
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
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The ARN of a resource that can be tagged. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
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


## testInvokeAuthorizer

> TestInvokeAuthorizerResponse testInvokeAuthorizer(restapiId, authorizerId, testInvokeAuthorizerRequest, opts)



Simulate the execution of an Authorizer in your RestApi with headers, parameters, and an incoming request body.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let authorizerId = "authorizerId_example"; // String | Specifies a test invoke authorizer request's Authorizer ID.
let testInvokeAuthorizerRequest = new AmazonApiGateway.TestInvokeAuthorizerRequest(); // TestInvokeAuthorizerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.testInvokeAuthorizer(restapiId, authorizerId, testInvokeAuthorizerRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **authorizerId** | **String**| Specifies a test invoke authorizer request&#39;s Authorizer ID. | 
 **testInvokeAuthorizerRequest** | [**TestInvokeAuthorizerRequest**](TestInvokeAuthorizerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TestInvokeAuthorizerResponse**](TestInvokeAuthorizerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## testInvokeMethod

> TestInvokeMethodResponse testInvokeMethod(restapiId, resourceId, httpMethod, testInvokeMethodRequest, opts)



Simulate the invocation of a Method in your RestApi with headers, parameters, and an incoming request body.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | Specifies a test invoke method request's resource ID.
let httpMethod = "httpMethod_example"; // String | Specifies a test invoke method request's HTTP method.
let testInvokeMethodRequest = new AmazonApiGateway.TestInvokeMethodRequest(); // TestInvokeMethodRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.testInvokeMethod(restapiId, resourceId, httpMethod, testInvokeMethodRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| Specifies a test invoke method request&#39;s resource ID. | 
 **httpMethod** | **String**| Specifies a test invoke method request&#39;s HTTP method. | 
 **testInvokeMethodRequest** | [**TestInvokeMethodRequest**](TestInvokeMethodRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TestInvokeMethodResponse**](TestInvokeMethodResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> untagResource(resourceArn, tagKeys, opts)



Removes a tag from a given resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of a resource that can be tagged.
let tagKeys = ["null"]; // [String] | The Tag keys to delete.
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
 **resourceArn** | **String**| The ARN of a resource that can be tagged. | 
 **tagKeys** | [**[String]**](String.md)| The Tag keys to delete. | 
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


## updateAccount

> Account updateAccount(updateApiKeyRequest, opts)



Changes information about the current Account resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccount(updateApiKeyRequest, opts, (error, data, response) => {
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
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApiKey

> ApiKey updateApiKey(apiKey, updateApiKeyRequest, opts)



Changes information about an ApiKey resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let apiKey = "apiKey_example"; // String | The identifier of the ApiKey resource to be updated.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApiKey(apiKey, updateApiKeyRequest, opts, (error, data, response) => {
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
 **apiKey** | **String**| The identifier of the ApiKey resource to be updated. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAuthorizer

> Authorizer updateAuthorizer(restapiId, authorizerId, updateApiKeyRequest, opts)



Updates an existing Authorizer resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let authorizerId = "authorizerId_example"; // String | The identifier of the Authorizer resource.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAuthorizer(restapiId, authorizerId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **authorizerId** | **String**| The identifier of the Authorizer resource. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Authorizer**](Authorizer.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBasePathMapping

> BasePathMapping updateBasePathMapping(domainName, basePath, updateApiKeyRequest, opts)



Changes information about the BasePathMapping resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let domainName = "domainName_example"; // String | The domain name of the BasePathMapping resource to change.
let basePath = "basePath_example"; // String | <p>The base path of the BasePathMapping resource to change.</p> <p>To specify an empty base path, set this parameter to <code>'(none)'</code>.</p>
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBasePathMapping(domainName, basePath, updateApiKeyRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name of the BasePathMapping resource to change. | 
 **basePath** | **String**| &lt;p&gt;The base path of the BasePathMapping resource to change.&lt;/p&gt; &lt;p&gt;To specify an empty base path, set this parameter to &lt;code&gt;&#39;(none)&#39;&lt;/code&gt;.&lt;/p&gt; | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BasePathMapping**](BasePathMapping.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateClientCertificate

> ClientCertificate updateClientCertificate(clientcertificateId, updateApiKeyRequest, opts)



Changes information about an ClientCertificate resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let clientcertificateId = "clientcertificateId_example"; // String | The identifier of the ClientCertificate resource to be updated.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateClientCertificate(clientcertificateId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **clientcertificateId** | **String**| The identifier of the ClientCertificate resource to be updated. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ClientCertificate**](ClientCertificate.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeployment

> Deployment updateDeployment(restapiId, deploymentId, updateApiKeyRequest, opts)



Changes information about a Deployment resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let deploymentId = "deploymentId_example"; // String | The replacement identifier for the Deployment resource to change information about.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDeployment(restapiId, deploymentId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **deploymentId** | **String**| The replacement identifier for the Deployment resource to change information about. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDocumentationPart

> DocumentationPart updateDocumentationPart(restapiId, partId, updateApiKeyRequest, opts)



Updates a documentation part.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let partId = "partId_example"; // String | The identifier of the to-be-updated documentation part.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDocumentationPart(restapiId, partId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **partId** | **String**| The identifier of the to-be-updated documentation part. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DocumentationPart**](DocumentationPart.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDocumentationVersion

> DocumentationVersion updateDocumentationVersion(restapiId, docVersion, updateApiKeyRequest, opts)



Updates a documentation version.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi..
let docVersion = "docVersion_example"; // String | The version identifier of the to-be-updated documentation version.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDocumentationVersion(restapiId, docVersion, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi.. | 
 **docVersion** | **String**| The version identifier of the to-be-updated documentation version. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DocumentationVersion**](DocumentationVersion.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDomainName

> DomainName updateDomainName(domainName, updateApiKeyRequest, opts)



Changes information about the DomainName resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let domainName = "domainName_example"; // String | The name of the DomainName resource to be changed.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDomainName(domainName, updateApiKeyRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The name of the DomainName resource to be changed. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DomainName**](DomainName.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGatewayResponse

> GatewayResponse updateGatewayResponse(restapiId, responseType, updateApiKeyRequest, opts)



Updates a GatewayResponse of a specified response type on the given RestApi.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let responseType = "responseType_example"; // String | The response type of the associated GatewayResponse.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGatewayResponse(restapiId, responseType, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **responseType** | **String**| The response type of the associated GatewayResponse. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GatewayResponse**](GatewayResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateIntegration

> Integration updateIntegration(restapiId, resourceId, httpMethod, updateApiKeyRequest, opts)



Represents an update integration.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | Represents an update integration request's resource identifier.
let httpMethod = "httpMethod_example"; // String | Represents an update integration request's HTTP method.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateIntegration(restapiId, resourceId, httpMethod, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| Represents an update integration request&#39;s resource identifier. | 
 **httpMethod** | **String**| Represents an update integration request&#39;s HTTP method. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Integration**](Integration.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateIntegrationResponse

> IntegrationResponse updateIntegrationResponse(restapiId, resourceId, httpMethod, statusCode, updateApiKeyRequest, opts)



Represents an update integration response.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | Specifies an update integration response request's resource identifier.
let httpMethod = "httpMethod_example"; // String | Specifies an update integration response request's HTTP method.
let statusCode = "statusCode_example"; // String | Specifies an update integration response request's status code.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateIntegrationResponse(restapiId, resourceId, httpMethod, statusCode, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| Specifies an update integration response request&#39;s resource identifier. | 
 **httpMethod** | **String**| Specifies an update integration response request&#39;s HTTP method. | 
 **statusCode** | **String**| Specifies an update integration response request&#39;s status code. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMethod

> Method updateMethod(restapiId, resourceId, httpMethod, updateApiKeyRequest, opts)



Updates an existing Method resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The Resource identifier for the Method resource.
let httpMethod = "httpMethod_example"; // String | The HTTP verb of the Method resource.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMethod(restapiId, resourceId, httpMethod, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The Resource identifier for the Method resource. | 
 **httpMethod** | **String**| The HTTP verb of the Method resource. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Method**](Method.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMethodResponse

> MethodResponse updateMethodResponse(restapiId, resourceId, httpMethod, statusCode, updateApiKeyRequest, opts)



Updates an existing MethodResponse resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The Resource identifier for the MethodResponse resource.
let httpMethod = "httpMethod_example"; // String | The HTTP verb of the Method resource.
let statusCode = "statusCode_example"; // String | The status code for the MethodResponse resource.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMethodResponse(restapiId, resourceId, httpMethod, statusCode, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The Resource identifier for the MethodResponse resource. | 
 **httpMethod** | **String**| The HTTP verb of the Method resource. | 
 **statusCode** | **String**| The status code for the MethodResponse resource. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**MethodResponse**](MethodResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateModel

> Model updateModel(restapiId, modelName, updateApiKeyRequest, opts)



Changes information about a model.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let modelName = "modelName_example"; // String | The name of the model to update.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateModel(restapiId, modelName, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **modelName** | **String**| The name of the model to update. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRequestValidator

> RequestValidator updateRequestValidator(restapiId, requestvalidatorId, updateApiKeyRequest, opts)



Updates a RequestValidator of a given RestApi.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let requestvalidatorId = "requestvalidatorId_example"; // String | The identifier of RequestValidator to be updated.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRequestValidator(restapiId, requestvalidatorId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **requestvalidatorId** | **String**| The identifier of RequestValidator to be updated. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RequestValidator**](RequestValidator.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateResource

> Resource updateResource(restapiId, resourceId, updateApiKeyRequest, opts)



Changes information about a Resource resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let resourceId = "resourceId_example"; // String | The identifier of the Resource resource.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateResource(restapiId, resourceId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **resourceId** | **String**| The identifier of the Resource resource. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Resource**](Resource.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRestApi

> RestApi updateRestApi(restapiId, updateApiKeyRequest, opts)



Changes information about the specified API.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRestApi(restapiId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RestApi**](RestApi.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStage

> Stage updateStage(restapiId, stageName, updateApiKeyRequest, opts)



Changes information about a Stage resource.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let restapiId = "restapiId_example"; // String | The string identifier of the associated RestApi.
let stageName = "stageName_example"; // String | The name of the Stage resource to change information about.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateStage(restapiId, stageName, updateApiKeyRequest, opts, (error, data, response) => {
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
 **restapiId** | **String**| The string identifier of the associated RestApi. | 
 **stageName** | **String**| The name of the Stage resource to change information about. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Stage**](Stage.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUsage

> Usage updateUsage(usageplanId, keyId, updateApiKeyRequest, opts)



Grants a temporary extension to the remaining quota of a usage plan associated with a specified API key.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let usageplanId = "usageplanId_example"; // String | The Id of the usage plan associated with the usage data.
let keyId = "keyId_example"; // String | The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUsage(usageplanId, keyId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **usageplanId** | **String**| The Id of the usage plan associated with the usage data. | 
 **keyId** | **String**| The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Usage**](Usage.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUsagePlan

> UsagePlan updateUsagePlan(usageplanId, updateApiKeyRequest, opts)



Updates a usage plan of a given plan Id.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let usageplanId = "usageplanId_example"; // String | The Id of the to-be-updated usage plan.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUsagePlan(usageplanId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **usageplanId** | **String**| The Id of the to-be-updated usage plan. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UsagePlan**](UsagePlan.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVpcLink

> VpcLink updateVpcLink(vpclinkId, updateApiKeyRequest, opts)



Updates an existing VpcLink of a specified identifier.

### Example

```javascript
import AmazonApiGateway from 'amazon_api_gateway';
let defaultClient = AmazonApiGateway.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonApiGateway.DefaultApi();
let vpclinkId = "vpclinkId_example"; // String | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
let updateApiKeyRequest = new AmazonApiGateway.UpdateApiKeyRequest(); // UpdateApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVpcLink(vpclinkId, updateApiKeyRequest, opts, (error, data, response) => {
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
 **vpclinkId** | **String**| The identifier of the VpcLink. It is used in an Integration to reference this VpcLink. | 
 **updateApiKeyRequest** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**VpcLink**](VpcLink.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

