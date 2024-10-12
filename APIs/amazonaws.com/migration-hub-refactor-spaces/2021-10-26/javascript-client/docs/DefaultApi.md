# AwsMigrationHubRefactorSpaces.DefaultApi

All URIs are relative to *http://refactor-spaces.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApplication**](DefaultApi.md#createApplication) | **POST** /environments/{EnvironmentIdentifier}/applications | 
[**createEnvironment**](DefaultApi.md#createEnvironment) | **POST** /environments | 
[**createRoute**](DefaultApi.md#createRoute) | **POST** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier}/routes | 
[**createService**](DefaultApi.md#createService) | **POST** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier}/services | 
[**deleteApplication**](DefaultApi.md#deleteApplication) | **DELETE** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier} | 
[**deleteEnvironment**](DefaultApi.md#deleteEnvironment) | **DELETE** /environments/{EnvironmentIdentifier} | 
[**deleteResourcePolicy**](DefaultApi.md#deleteResourcePolicy) | **DELETE** /resourcepolicy/{Identifier} | 
[**deleteRoute**](DefaultApi.md#deleteRoute) | **DELETE** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier}/routes/{RouteIdentifier} | 
[**deleteService**](DefaultApi.md#deleteService) | **DELETE** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier}/services/{ServiceIdentifier} | 
[**getApplication**](DefaultApi.md#getApplication) | **GET** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier} | 
[**getEnvironment**](DefaultApi.md#getEnvironment) | **GET** /environments/{EnvironmentIdentifier} | 
[**getResourcePolicy**](DefaultApi.md#getResourcePolicy) | **GET** /resourcepolicy/{Identifier} | 
[**getRoute**](DefaultApi.md#getRoute) | **GET** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier}/routes/{RouteIdentifier} | 
[**getService**](DefaultApi.md#getService) | **GET** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier}/services/{ServiceIdentifier} | 
[**listApplications**](DefaultApi.md#listApplications) | **GET** /environments/{EnvironmentIdentifier}/applications | 
[**listEnvironmentVpcs**](DefaultApi.md#listEnvironmentVpcs) | **GET** /environments/{EnvironmentIdentifier}/vpcs | 
[**listEnvironments**](DefaultApi.md#listEnvironments) | **GET** /environments | 
[**listRoutes**](DefaultApi.md#listRoutes) | **GET** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier}/routes | 
[**listServices**](DefaultApi.md#listServices) | **GET** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier}/services | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**putResourcePolicy**](DefaultApi.md#putResourcePolicy) | **PUT** /resourcepolicy | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateRoute**](DefaultApi.md#updateRoute) | **PATCH** /environments/{EnvironmentIdentifier}/applications/{ApplicationIdentifier}/routes/{RouteIdentifier} | 



## createApplication

> CreateApplicationResponse createApplication(environmentIdentifier, createApplicationRequest, opts)



&lt;p&gt;Creates an Amazon Web Services Migration Hub Refactor Spaces application. The account that owns the environment also owns the applications created inside the environment, regardless of the account that creates the application. Refactor Spaces provisions an Amazon API Gateway, API Gateway VPC link, and Network Load Balancer for the application proxy inside your account.&lt;/p&gt; &lt;p&gt;In environments created with a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType\&quot;&gt;CreateEnvironment:NetworkFabricType&lt;/a&gt; of &lt;code&gt;NONE&lt;/code&gt; you need to configure &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html\&quot;&gt; VPC to VPC connectivity&lt;/a&gt; between your service VPC and the application proxy VPC to route traffic through the application proxy to a service with a private URL endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-application.html\&quot;&gt; Create an application&lt;/a&gt; in the &lt;i&gt;Refactor Spaces User Guide&lt;/i&gt;. &lt;/p&gt;

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let environmentIdentifier = "environmentIdentifier_example"; // String | The unique identifier of the environment.
let createApplicationRequest = new AwsMigrationHubRefactorSpaces.CreateApplicationRequest(); // CreateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApplication(environmentIdentifier, createApplicationRequest, opts, (error, data, response) => {
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
 **environmentIdentifier** | **String**| The unique identifier of the environment. | 
 **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEnvironment

> CreateEnvironmentResponse createEnvironment(createEnvironmentRequest, opts)



&lt;p&gt;Creates an Amazon Web Services Migration Hub Refactor Spaces environment. The caller owns the environment resource, and all Refactor Spaces applications, services, and routes created within the environment. They are referred to as the &lt;i&gt;environment owner&lt;/i&gt;. The environment owner has cross-account visibility and control of Refactor Spaces resources that are added to the environment by other accounts that the environment is shared with.&lt;/p&gt; &lt;p&gt;When creating an environment with a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType\&quot;&gt;CreateEnvironment:NetworkFabricType&lt;/a&gt; of &lt;code&gt;TRANSIT_GATEWAY&lt;/code&gt;, Refactor Spaces provisions a transit gateway to enable services in VPCs to communicate directly across accounts. If &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType\&quot;&gt;CreateEnvironment:NetworkFabricType&lt;/a&gt; is &lt;code&gt;NONE&lt;/code&gt;, Refactor Spaces does not create a transit gateway and you must use your network infrastructure to route traffic to services with private URL endpoints.&lt;/p&gt;

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let createEnvironmentRequest = new AwsMigrationHubRefactorSpaces.CreateEnvironmentRequest(); // CreateEnvironmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEnvironment(createEnvironmentRequest, opts, (error, data, response) => {
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
 **createEnvironmentRequest** | [**CreateEnvironmentRequest**](CreateEnvironmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateEnvironmentResponse**](CreateEnvironmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRoute

> CreateRouteResponse createRoute(applicationIdentifier, environmentIdentifier, createRouteRequest, opts)



&lt;p&gt;Creates an Amazon Web Services Migration Hub Refactor Spaces route. The account owner of the service resource is always the environment owner, regardless of which account creates the route. Routes target a service in the application. If an application does not have any routes, then the first route must be created as a &lt;code&gt;DEFAULT&lt;/code&gt; &lt;code&gt;RouteType&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When created, the default route defaults to an active state so state is not a required input. However, like all other state values the state of the default route can be updated after creation, but only when all other routes are also inactive. Conversely, no route can be active without the default route also being active.&lt;/p&gt; &lt;p&gt;When you create a route, Refactor Spaces configures the Amazon API Gateway to send traffic to the target service as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;URL Endpoints&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If the service has a URL endpoint, and the endpoint resolves to a private IP address, Refactor Spaces routes traffic using the API Gateway VPC link. If a service endpoint resolves to a public IP address, Refactor Spaces routes traffic over the public internet. Services can have HTTP or HTTPS URL endpoints. For HTTPS URLs, publicly-signed certificates are supported. Private Certificate Authorities (CAs) are permitted only if the CA&#39;s domain is also publicly resolvable. &lt;/p&gt; &lt;p&gt;Refactor Spaces automatically resolves the public Domain Name System (DNS) names that are set in &lt;code&gt;CreateService:UrlEndpoint &lt;/code&gt;when you create a service. The DNS names resolve when the DNS time-to-live (TTL) expires, or every 60 seconds for TTLs less than 60 seconds. This periodic DNS resolution ensures that the route configuration remains up-to-date. &lt;/p&gt; &lt;p/&gt; &lt;p&gt; &lt;b&gt;One-time health check&lt;/b&gt; &lt;/p&gt; &lt;p&gt;A one-time health check is performed on the service when either the route is updated from inactive to active, or when it is created with an active state. If the health check fails, the route transitions the route state to &lt;code&gt;FAILED&lt;/code&gt;, an error code of &lt;code&gt;SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE&lt;/code&gt; is provided, and no traffic is sent to the service.&lt;/p&gt; &lt;p&gt;For private URLs, a target group is created on the Network Load Balancer and the load balancer target group runs default target health checks. By default, the health check is run against the service endpoint URL. Optionally, the health check can be performed against a different protocol, port, and/or path using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateService.html#migrationhubrefactorspaces-CreateService-request-UrlEndpoint\&quot;&gt;CreateService:UrlEndpoint&lt;/a&gt; parameter. All other health check settings for the load balancer use the default values described in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html\&quot;&gt;Health checks for your target groups&lt;/a&gt; in the &lt;i&gt;Elastic Load Balancing guide&lt;/i&gt;. The health check is considered successful if at least one target within the target group transitions to a healthy state.&lt;/p&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Lambda function endpoints&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If the service has an Lambda function endpoint, then Refactor Spaces configures the Lambda function&#39;s resource policy to allow the application&#39;s API Gateway to invoke the function.&lt;/p&gt; &lt;p&gt;The Lambda function state is checked. If the function is not active, the function configuration is updated so that Lambda resources are provisioned. If the Lambda state is &lt;code&gt;Failed&lt;/code&gt;, then the route creation fails. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html#SSS-GetFunctionConfiguration-response-State\&quot;&gt;GetFunctionConfiguration&#39;s State response parameter&lt;/a&gt; in the &lt;i&gt;Lambda Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;A check is performed to determine that a Lambda function with the specified ARN exists. If it does not exist, the health check fails. For public URLs, a connection is opened to the public endpoint. If the URL is not reachable, the health check fails. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Environments without a network bridge&lt;/b&gt; &lt;/p&gt; &lt;p&gt;When you create environments without a network bridge (&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType\&quot;&gt;CreateEnvironment:NetworkFabricType&lt;/a&gt; is &lt;code&gt;NONE)&lt;/code&gt; and you use your own networking infrastructure, you need to configure &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html\&quot;&gt;VPC to VPC connectivity&lt;/a&gt; between your network and the application proxy VPC. Route creation from the application proxy to service endpoints will fail if your network is not configured to connect to the application proxy VPC. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-role.html\&quot;&gt; Create a route&lt;/a&gt; in the &lt;i&gt;Refactor Spaces User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt;

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | The ID of the application within which the route is being created.
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment in which the route is created.
let createRouteRequest = new AwsMigrationHubRefactorSpaces.CreateRouteRequest(); // CreateRouteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRoute(applicationIdentifier, environmentIdentifier, createRouteRequest, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| The ID of the application within which the route is being created. | 
 **environmentIdentifier** | **String**| The ID of the environment in which the route is created. | 
 **createRouteRequest** | [**CreateRouteRequest**](CreateRouteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRouteResponse**](CreateRouteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createService

> CreateServiceResponse createService(applicationIdentifier, environmentIdentifier, createServiceRequest, opts)



&lt;p&gt;Creates an Amazon Web Services Migration Hub Refactor Spaces service. The account owner of the service is always the environment owner, regardless of which account in the environment creates the service. Services have either a URL endpoint in a virtual private cloud (VPC), or a Lambda function endpoint.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If an Amazon Web Services resource is launched in a service VPC, and you want it to be accessible to all of an environment’s services with VPCs and routes, apply the &lt;code&gt;RefactorSpacesSecurityGroup&lt;/code&gt; to the resource. Alternatively, to add more cross-account constraints, apply your own security group.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | The ID of the application which the service is created.
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment in which the service is created.
let createServiceRequest = new AwsMigrationHubRefactorSpaces.CreateServiceRequest(); // CreateServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createService(applicationIdentifier, environmentIdentifier, createServiceRequest, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| The ID of the application which the service is created. | 
 **environmentIdentifier** | **String**| The ID of the environment in which the service is created. | 
 **createServiceRequest** | [**CreateServiceRequest**](CreateServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateServiceResponse**](CreateServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplication

> DeleteApplicationResponse deleteApplication(applicationIdentifier, environmentIdentifier, opts)



Deletes an Amazon Web Services Migration Hub Refactor Spaces application. Before you can delete an application, you must first delete any services or routes within the application.

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | The ID of the application.
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplication(applicationIdentifier, environmentIdentifier, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| The ID of the application. | 
 **environmentIdentifier** | **String**| The ID of the environment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApplicationResponse**](DeleteApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEnvironment

> DeleteEnvironmentResponse deleteEnvironment(environmentIdentifier, opts)



Deletes an Amazon Web Services Migration Hub Refactor Spaces environment. Before you can delete an environment, you must first delete any applications and services within the environment.

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEnvironment(environmentIdentifier, opts, (error, data, response) => {
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
 **environmentIdentifier** | **String**| The ID of the environment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteEnvironmentResponse**](DeleteEnvironmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteResourcePolicy

> Object deleteResourcePolicy(identifier, opts)



Deletes the resource policy set for the environment. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let identifier = "identifier_example"; // String | Amazon Resource Name (ARN) of the resource associated with the policy. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteResourcePolicy(identifier, opts, (error, data, response) => {
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
 **identifier** | **String**| Amazon Resource Name (ARN) of the resource associated with the policy.  | 
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


## deleteRoute

> DeleteRouteResponse deleteRoute(applicationIdentifier, environmentIdentifier, routeIdentifier, opts)



Deletes an Amazon Web Services Migration Hub Refactor Spaces route.

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | The ID of the application to delete the route from.
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment to delete the route from.
let routeIdentifier = "routeIdentifier_example"; // String | The ID of the route to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRoute(applicationIdentifier, environmentIdentifier, routeIdentifier, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| The ID of the application to delete the route from. | 
 **environmentIdentifier** | **String**| The ID of the environment to delete the route from. | 
 **routeIdentifier** | **String**| The ID of the route to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteRouteResponse**](DeleteRouteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteService

> DeleteServiceResponse deleteService(applicationIdentifier, environmentIdentifier, serviceIdentifier, opts)



Deletes an Amazon Web Services Migration Hub Refactor Spaces service. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | <p>Deletes a Refactor Spaces service.</p> <note> <p>The <code>RefactorSpacesSecurityGroup</code> security group must be removed from all Amazon Web Services resources in the virtual private cloud (VPC) prior to deleting a service with a URL endpoint in a VPC.</p> </note>
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment that the service is in.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID of the service to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteService(applicationIdentifier, environmentIdentifier, serviceIdentifier, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| &lt;p&gt;Deletes a Refactor Spaces service.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;RefactorSpacesSecurityGroup&lt;/code&gt; security group must be removed from all Amazon Web Services resources in the virtual private cloud (VPC) prior to deleting a service with a URL endpoint in a VPC.&lt;/p&gt; &lt;/note&gt; | 
 **environmentIdentifier** | **String**| The ID of the environment that the service is in. | 
 **serviceIdentifier** | **String**| The ID of the service to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteServiceResponse**](DeleteServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplication

> GetApplicationResponse getApplication(applicationIdentifier, environmentIdentifier, opts)



Gets an Amazon Web Services Migration Hub Refactor Spaces application.

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | The ID of the application.
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApplication(applicationIdentifier, environmentIdentifier, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| The ID of the application. | 
 **environmentIdentifier** | **String**| The ID of the environment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApplicationResponse**](GetApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEnvironment

> GetEnvironmentResponse getEnvironment(environmentIdentifier, opts)



Gets an Amazon Web Services Migration Hub Refactor Spaces environment.

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEnvironment(environmentIdentifier, opts, (error, data, response) => {
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
 **environmentIdentifier** | **String**| The ID of the environment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEnvironmentResponse**](GetEnvironmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResourcePolicy

> GetResourcePolicyResponse getResourcePolicy(identifier, opts)



Gets the resource-based permission policy that is set for the given environment. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let identifier = "identifier_example"; // String | The Amazon Resource Name (ARN) of the resource associated with the policy. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getResourcePolicy(identifier, opts, (error, data, response) => {
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
 **identifier** | **String**| The Amazon Resource Name (ARN) of the resource associated with the policy.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetResourcePolicyResponse**](GetResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRoute

> GetRouteResponse getRoute(applicationIdentifier, environmentIdentifier, routeIdentifier, opts)



Gets an Amazon Web Services Migration Hub Refactor Spaces route.

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | The ID of the application. 
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment.
let routeIdentifier = "routeIdentifier_example"; // String | The ID of the route.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRoute(applicationIdentifier, environmentIdentifier, routeIdentifier, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| The ID of the application.  | 
 **environmentIdentifier** | **String**| The ID of the environment. | 
 **routeIdentifier** | **String**| The ID of the route. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRouteResponse**](GetRouteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getService

> GetServiceResponse getService(applicationIdentifier, environmentIdentifier, serviceIdentifier, opts)



Gets an Amazon Web Services Migration Hub Refactor Spaces service. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | The ID of the application.
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment.
let serviceIdentifier = "serviceIdentifier_example"; // String | The ID of the service.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getService(applicationIdentifier, environmentIdentifier, serviceIdentifier, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| The ID of the application. | 
 **environmentIdentifier** | **String**| The ID of the environment. | 
 **serviceIdentifier** | **String**| The ID of the service. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceResponse**](GetServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApplications

> ListApplicationsResponse listApplications(environmentIdentifier, opts)



Lists all the Amazon Web Services Migration Hub Refactor Spaces applications within an environment. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.
  'nextToken': "nextToken_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listApplications(environmentIdentifier, opts, (error, data, response) => {
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
 **environmentIdentifier** | **String**| The ID of the environment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] 
 **nextToken** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListApplicationsResponse**](ListApplicationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEnvironmentVpcs

> ListEnvironmentVpcsResponse listEnvironmentVpcs(environmentIdentifier, opts)



Lists all Amazon Web Services Migration Hub Refactor Spaces service virtual private clouds (VPCs) that are part of the environment. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.
  'nextToken': "nextToken_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listEnvironmentVpcs(environmentIdentifier, opts, (error, data, response) => {
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
 **environmentIdentifier** | **String**| The ID of the environment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] 
 **nextToken** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListEnvironmentVpcsResponse**](ListEnvironmentVpcsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEnvironments

> ListEnvironmentsResponse listEnvironments(opts)



Lists Amazon Web Services Migration Hub Refactor Spaces environments owned by a caller account or shared with the caller account. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.
  'nextToken': "nextToken_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listEnvironments(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] 
 **nextToken** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListEnvironmentsResponse**](ListEnvironmentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoutes

> ListRoutesResponse listRoutes(applicationIdentifier, environmentIdentifier, opts)



Lists all the Amazon Web Services Migration Hub Refactor Spaces routes within an application. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | The ID of the application. 
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.
  'nextToken': "nextToken_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRoutes(applicationIdentifier, environmentIdentifier, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| The ID of the application.  | 
 **environmentIdentifier** | **String**| The ID of the environment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] 
 **nextToken** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRoutesResponse**](ListRoutesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServices

> ListServicesResponse listServices(applicationIdentifier, environmentIdentifier, opts)



Lists all the Amazon Web Services Migration Hub Refactor Spaces services within an application. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String | The ID of the application. 
let environmentIdentifier = "environmentIdentifier_example"; // String | The ID of the environment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.
  'nextToken': "nextToken_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listServices(applicationIdentifier, environmentIdentifier, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**| The ID of the application.  | 
 **environmentIdentifier** | **String**| The ID of the environment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] 
 **nextToken** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListServicesResponse**](ListServicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists the tags of a resource. The caller account must be the same as the resource’s &lt;code&gt;OwnerAccountId&lt;/code&gt;. Listing tags in other accounts is not supported. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putResourcePolicy

> Object putResourcePolicy(putResourcePolicyRequest, opts)



Attaches a resource-based permission policy to the Amazon Web Services Migration Hub Refactor Spaces environment. The policy must contain the same actions and condition statements as the &lt;code&gt;arn:aws:ram::aws:permission/AWSRAMDefaultPermissionRefactorSpacesEnvironment&lt;/code&gt; permission in Resource Access Manager. The policy must not contain new lines or blank lines. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let putResourcePolicyRequest = new AwsMigrationHubRefactorSpaces.PutResourcePolicyRequest(); // PutResourcePolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putResourcePolicy(putResourcePolicyRequest, opts, (error, data, response) => {
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
 **putResourcePolicyRequest** | [**PutResourcePolicyRequest**](PutResourcePolicyRequest.md)|  | 
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


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Removes the tags of a given resource. Tags are metadata which can be used to manage a resource. To tag a resource, the caller account must be the same as the resource’s &lt;code&gt;OwnerAccountId&lt;/code&gt;. Tagging resources in other accounts is not supported.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Web Services Migration Hub Refactor Spaces does not propagate tags to orchestrated resources, such as an environment’s transit gateway.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagResourceRequest = new AwsMigrationHubRefactorSpaces.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
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

> Object untagResource(resourceArn, tagKeys, opts)



Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource. To untag a resource, the caller account must be the same as the resource’s &lt;code&gt;OwnerAccountId&lt;/code&gt;. Untagging resources across accounts is not supported. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource. 
let tagKeys = ["null"]; // [String] | The list of keys of the tags to be removed from the resource. 
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
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource.  | 
 **tagKeys** | [**[String]**](String.md)| The list of keys of the tags to be removed from the resource.  | 
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


## updateRoute

> UpdateRouteResponse updateRoute(applicationIdentifier, environmentIdentifier, routeIdentifier, updateRouteRequest, opts)



 Updates an Amazon Web Services Migration Hub Refactor Spaces route. 

### Example

```javascript
import AwsMigrationHubRefactorSpaces from 'aws_migration_hub_refactor_spaces';
let defaultClient = AwsMigrationHubRefactorSpaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMigrationHubRefactorSpaces.DefaultApi();
let applicationIdentifier = "applicationIdentifier_example"; // String |  The ID of the application within which the route is being updated. 
let environmentIdentifier = "environmentIdentifier_example"; // String |  The ID of the environment in which the route is being updated. 
let routeIdentifier = "routeIdentifier_example"; // String |  The unique identifier of the route to update. 
let updateRouteRequest = new AwsMigrationHubRefactorSpaces.UpdateRouteRequest(); // UpdateRouteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoute(applicationIdentifier, environmentIdentifier, routeIdentifier, updateRouteRequest, opts, (error, data, response) => {
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
 **applicationIdentifier** | **String**|  The ID of the application within which the route is being updated.  | 
 **environmentIdentifier** | **String**|  The ID of the environment in which the route is being updated.  | 
 **routeIdentifier** | **String**|  The unique identifier of the route to update.  | 
 **updateRouteRequest** | [**UpdateRouteRequest**](UpdateRouteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRouteResponse**](UpdateRouteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

