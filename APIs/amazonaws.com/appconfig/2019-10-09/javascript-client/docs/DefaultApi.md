# AmazonAppConfig.DefaultApi

All URIs are relative to *http://appconfig.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApplication**](DefaultApi.md#createApplication) | **POST** /applications | 
[**createConfigurationProfile**](DefaultApi.md#createConfigurationProfile) | **POST** /applications/{ApplicationId}/configurationprofiles | 
[**createDeploymentStrategy**](DefaultApi.md#createDeploymentStrategy) | **POST** /deploymentstrategies | 
[**createEnvironment**](DefaultApi.md#createEnvironment) | **POST** /applications/{ApplicationId}/environments | 
[**createExtension**](DefaultApi.md#createExtension) | **POST** /extensions | 
[**createExtensionAssociation**](DefaultApi.md#createExtensionAssociation) | **POST** /extensionassociations | 
[**createHostedConfigurationVersion**](DefaultApi.md#createHostedConfigurationVersion) | **POST** /applications/{ApplicationId}/configurationprofiles/{ConfigurationProfileId}/hostedconfigurationversions#Content-Type | 
[**deleteApplication**](DefaultApi.md#deleteApplication) | **DELETE** /applications/{ApplicationId} | 
[**deleteConfigurationProfile**](DefaultApi.md#deleteConfigurationProfile) | **DELETE** /applications/{ApplicationId}/configurationprofiles/{ConfigurationProfileId} | 
[**deleteDeploymentStrategy**](DefaultApi.md#deleteDeploymentStrategy) | **DELETE** /deployementstrategies/{DeploymentStrategyId} | 
[**deleteEnvironment**](DefaultApi.md#deleteEnvironment) | **DELETE** /applications/{ApplicationId}/environments/{EnvironmentId} | 
[**deleteExtension**](DefaultApi.md#deleteExtension) | **DELETE** /extensions/{ExtensionIdentifier} | 
[**deleteExtensionAssociation**](DefaultApi.md#deleteExtensionAssociation) | **DELETE** /extensionassociations/{ExtensionAssociationId} | 
[**deleteHostedConfigurationVersion**](DefaultApi.md#deleteHostedConfigurationVersion) | **DELETE** /applications/{ApplicationId}/configurationprofiles/{ConfigurationProfileId}/hostedconfigurationversions/{VersionNumber} | 
[**getApplication**](DefaultApi.md#getApplication) | **GET** /applications/{ApplicationId} | 
[**getConfiguration**](DefaultApi.md#getConfiguration) | **GET** /applications/{Application}/environments/{Environment}/configurations/{Configuration}#client_id | 
[**getConfigurationProfile**](DefaultApi.md#getConfigurationProfile) | **GET** /applications/{ApplicationId}/configurationprofiles/{ConfigurationProfileId} | 
[**getDeployment**](DefaultApi.md#getDeployment) | **GET** /applications/{ApplicationId}/environments/{EnvironmentId}/deployments/{DeploymentNumber} | 
[**getDeploymentStrategy**](DefaultApi.md#getDeploymentStrategy) | **GET** /deploymentstrategies/{DeploymentStrategyId} | 
[**getEnvironment**](DefaultApi.md#getEnvironment) | **GET** /applications/{ApplicationId}/environments/{EnvironmentId} | 
[**getExtension**](DefaultApi.md#getExtension) | **GET** /extensions/{ExtensionIdentifier} | 
[**getExtensionAssociation**](DefaultApi.md#getExtensionAssociation) | **GET** /extensionassociations/{ExtensionAssociationId} | 
[**getHostedConfigurationVersion**](DefaultApi.md#getHostedConfigurationVersion) | **GET** /applications/{ApplicationId}/configurationprofiles/{ConfigurationProfileId}/hostedconfigurationversions/{VersionNumber} | 
[**listApplications**](DefaultApi.md#listApplications) | **GET** /applications | 
[**listConfigurationProfiles**](DefaultApi.md#listConfigurationProfiles) | **GET** /applications/{ApplicationId}/configurationprofiles | 
[**listDeploymentStrategies**](DefaultApi.md#listDeploymentStrategies) | **GET** /deploymentstrategies | 
[**listDeployments**](DefaultApi.md#listDeployments) | **GET** /applications/{ApplicationId}/environments/{EnvironmentId}/deployments | 
[**listEnvironments**](DefaultApi.md#listEnvironments) | **GET** /applications/{ApplicationId}/environments | 
[**listExtensionAssociations**](DefaultApi.md#listExtensionAssociations) | **GET** /extensionassociations | 
[**listExtensions**](DefaultApi.md#listExtensions) | **GET** /extensions | 
[**listHostedConfigurationVersions**](DefaultApi.md#listHostedConfigurationVersions) | **GET** /applications/{ApplicationId}/configurationprofiles/{ConfigurationProfileId}/hostedconfigurationversions | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**startDeployment**](DefaultApi.md#startDeployment) | **POST** /applications/{ApplicationId}/environments/{EnvironmentId}/deployments | 
[**stopDeployment**](DefaultApi.md#stopDeployment) | **DELETE** /applications/{ApplicationId}/environments/{EnvironmentId}/deployments/{DeploymentNumber} | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateApplication**](DefaultApi.md#updateApplication) | **PATCH** /applications/{ApplicationId} | 
[**updateConfigurationProfile**](DefaultApi.md#updateConfigurationProfile) | **PATCH** /applications/{ApplicationId}/configurationprofiles/{ConfigurationProfileId} | 
[**updateDeploymentStrategy**](DefaultApi.md#updateDeploymentStrategy) | **PATCH** /deploymentstrategies/{DeploymentStrategyId} | 
[**updateEnvironment**](DefaultApi.md#updateEnvironment) | **PATCH** /applications/{ApplicationId}/environments/{EnvironmentId} | 
[**updateExtension**](DefaultApi.md#updateExtension) | **PATCH** /extensions/{ExtensionIdentifier} | 
[**updateExtensionAssociation**](DefaultApi.md#updateExtensionAssociation) | **PATCH** /extensionassociations/{ExtensionAssociationId} | 
[**validateConfiguration**](DefaultApi.md#validateConfiguration) | **POST** /applications/{ApplicationId}/configurationprofiles/{ConfigurationProfileId}/validators#configuration_version | 



## createApplication

> Application createApplication(createApplicationRequest, opts)



Creates an application. In AppConfig, an application is simply an organizational construct like a folder. This organizational construct has a relationship with some unit of executable code. For example, you could create an application called MyMobileApp to organize and manage configuration data for a mobile application installed by your users.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let createApplicationRequest = new AmazonAppConfig.CreateApplicationRequest(); // CreateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApplication(createApplicationRequest, opts, (error, data, response) => {
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
 **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createConfigurationProfile

> ConfigurationProfile createConfigurationProfile(applicationId, createConfigurationProfileRequest, opts)



&lt;p&gt;Creates a configuration profile, which is information that enables AppConfig to access the configuration source. Valid configuration sources include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Configuration data in YAML, JSON, and other formats stored in the AppConfig hosted configuration store&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Configuration data stored as objects in an Amazon Simple Storage Service (Amazon S3) bucket&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Pipelines stored in CodePipeline&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Secrets stored in Secrets Manager&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Standard and secure string parameters stored in Amazon Web Services Systems Manager Parameter Store&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Configuration data in SSM documents stored in the Systems Manager document store&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;A configuration profile includes the following information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The URI location of the configuration data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Identity and Access Management (IAM) role that provides access to the configuration data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A validator for the configuration data. Available validators include either a JSON Schema or an Amazon Web Services Lambda function.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html\&quot;&gt;Create a Configuration and a Configuration Profile&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let createConfigurationProfileRequest = new AmazonAppConfig.CreateConfigurationProfileRequest(); // CreateConfigurationProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createConfigurationProfile(applicationId, createConfigurationProfileRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **createConfigurationProfileRequest** | [**CreateConfigurationProfileRequest**](CreateConfigurationProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ConfigurationProfile**](ConfigurationProfile.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDeploymentStrategy

> DeploymentStrategy createDeploymentStrategy(createDeploymentStrategyRequest, opts)



Creates a deployment strategy that defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let createDeploymentStrategyRequest = new AmazonAppConfig.CreateDeploymentStrategyRequest(); // CreateDeploymentStrategyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDeploymentStrategy(createDeploymentStrategyRequest, opts, (error, data, response) => {
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
 **createDeploymentStrategyRequest** | [**CreateDeploymentStrategyRequest**](CreateDeploymentStrategyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeploymentStrategy**](DeploymentStrategy.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEnvironment

> Environment createEnvironment(applicationId, createEnvironmentRequest, opts)



Creates an environment. For each application, you define one or more environments. An environment is a deployment group of AppConfig targets, such as applications in a &lt;code&gt;Beta&lt;/code&gt; or &lt;code&gt;Production&lt;/code&gt; environment. You can also define environments for application subcomponents such as the &lt;code&gt;Web&lt;/code&gt;, &lt;code&gt;Mobile&lt;/code&gt; and &lt;code&gt;Back-end&lt;/code&gt; components for your application. You can configure Amazon CloudWatch alarms for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let createEnvironmentRequest = new AmazonAppConfig.CreateEnvironmentRequest(); // CreateEnvironmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEnvironment(applicationId, createEnvironmentRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **createEnvironmentRequest** | [**CreateEnvironmentRequest**](CreateEnvironmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Environment**](Environment.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createExtension

> Extension createExtension(createExtensionRequest, opts)



&lt;p&gt;Creates an AppConfig extension. An extension augments your ability to inject logic or behavior at different points during the AppConfig workflow of creating or deploying a configuration.&lt;/p&gt; &lt;p&gt;You can create your own extensions or use the Amazon Web Services authored extensions provided by AppConfig. For most use cases, to create your own extension, you must create an Lambda function to perform any computation and processing defined in the extension. For more information about extensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let createExtensionRequest = new AmazonAppConfig.CreateExtensionRequest(); // CreateExtensionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'latestVersionNumber': 56 // Number | You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.
};
apiInstance.createExtension(createExtensionRequest, opts, (error, data, response) => {
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
 **createExtensionRequest** | [**CreateExtensionRequest**](CreateExtensionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **latestVersionNumber** | **Number**| You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. | [optional] 

### Return type

[**Extension**](Extension.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createExtensionAssociation

> ExtensionAssociation createExtensionAssociation(createExtensionAssociationRequest, opts)



When you create an extension or configure an Amazon Web Services authored extension, you associate the extension with an AppConfig application, environment, or configuration profile. For example, you can choose to run the &lt;code&gt;AppConfig deployment events to Amazon SNS&lt;/code&gt; Amazon Web Services authored extension and receive notifications on an Amazon SNS topic anytime a configuration deployment is started for a specific application. Defining which extension to associate with an AppConfig resource is called an &lt;i&gt;extension association&lt;/i&gt;. An extension association is a specified relationship between an extension and an AppConfig resource, such as an application or a configuration profile. For more information about extensions and associations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let createExtensionAssociationRequest = new AmazonAppConfig.CreateExtensionAssociationRequest(); // CreateExtensionAssociationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createExtensionAssociation(createExtensionAssociationRequest, opts, (error, data, response) => {
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
 **createExtensionAssociationRequest** | [**CreateExtensionAssociationRequest**](CreateExtensionAssociationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ExtensionAssociation**](ExtensionAssociation.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createHostedConfigurationVersion

> HostedConfigurationVersion createHostedConfigurationVersion(applicationId, configurationProfileId, contentType, createHostedConfigurationVersionRequest, opts)



Creates a new configuration in the AppConfig hosted configuration store.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let configurationProfileId = "configurationProfileId_example"; // String | The configuration profile ID.
let contentType = "contentType_example"; // String | A standard MIME type describing the format of the configuration content. For more information, see <a href=\"https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17\">Content-Type</a>.
let createHostedConfigurationVersionRequest = new AmazonAppConfig.CreateHostedConfigurationVersionRequest(); // CreateHostedConfigurationVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'description': "description_example", // String | A description of the configuration.
  'latestVersionNumber': 56, // Number | An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.
  'versionLabel': "versionLabel_example" // String | An optional, user-defined label for the AppConfig hosted configuration version. This value must contain at least one non-numeric character. For example, \"v2.2.0\".
};
apiInstance.createHostedConfigurationVersion(applicationId, configurationProfileId, contentType, createHostedConfigurationVersionRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **configurationProfileId** | **String**| The configuration profile ID. | 
 **contentType** | **String**| A standard MIME type describing the format of the configuration content. For more information, see &lt;a href&#x3D;\&quot;https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17\&quot;&gt;Content-Type&lt;/a&gt;. | 
 **createHostedConfigurationVersionRequest** | [**CreateHostedConfigurationVersionRequest**](CreateHostedConfigurationVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **description** | **String**| A description of the configuration. | [optional] 
 **latestVersionNumber** | **Number**| An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version. | [optional] 
 **versionLabel** | **String**| An optional, user-defined label for the AppConfig hosted configuration version. This value must contain at least one non-numeric character. For example, \&quot;v2.2.0\&quot;. | [optional] 

### Return type

[**HostedConfigurationVersion**](HostedConfigurationVersion.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplication

> deleteApplication(applicationId, opts)



Deletes an application. Deleting an application does not delete a configuration from a host.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The ID of the application to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplication(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The ID of the application to delete. | 
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


## deleteConfigurationProfile

> deleteConfigurationProfile(applicationId, configurationProfileId, opts)



Deletes a configuration profile. Deleting a configuration profile does not delete a configuration from a host.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID that includes the configuration profile you want to delete.
let configurationProfileId = "configurationProfileId_example"; // String | The ID of the configuration profile you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteConfigurationProfile(applicationId, configurationProfileId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID that includes the configuration profile you want to delete. | 
 **configurationProfileId** | **String**| The ID of the configuration profile you want to delete. | 
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


## deleteDeploymentStrategy

> deleteDeploymentStrategy(deploymentStrategyId, opts)



Deletes a deployment strategy. Deleting a deployment strategy does not delete a configuration from a host.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let deploymentStrategyId = "deploymentStrategyId_example"; // String | The ID of the deployment strategy you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDeploymentStrategy(deploymentStrategyId, opts, (error, data, response) => {
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
 **deploymentStrategyId** | **String**| The ID of the deployment strategy you want to delete. | 
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


## deleteEnvironment

> deleteEnvironment(applicationId, environmentId, opts)



Deletes an environment. Deleting an environment does not delete a configuration from a host.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID that includes the environment that you want to delete.
let environmentId = "environmentId_example"; // String | The ID of the environment that you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEnvironment(applicationId, environmentId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID that includes the environment that you want to delete. | 
 **environmentId** | **String**| The ID of the environment that you want to delete. | 
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


## deleteExtension

> deleteExtension(extensionIdentifier, opts)



Deletes an AppConfig extension. You must delete all associations to an extension before you delete the extension.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let extensionIdentifier = "extensionIdentifier_example"; // String | The name, ID, or Amazon Resource Name (ARN) of the extension you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': 56 // Number | A specific version of an extension to delete. If omitted, the highest version is deleted.
};
apiInstance.deleteExtension(extensionIdentifier, opts, (error, data, response) => {
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
 **extensionIdentifier** | **String**| The name, ID, or Amazon Resource Name (ARN) of the extension you want to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **Number**| A specific version of an extension to delete. If omitted, the highest version is deleted. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteExtensionAssociation

> deleteExtensionAssociation(extensionAssociationId, opts)



Deletes an extension association. This action doesn&#39;t delete extensions defined in the association.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let extensionAssociationId = "extensionAssociationId_example"; // String | The ID of the extension association to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteExtensionAssociation(extensionAssociationId, opts, (error, data, response) => {
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
 **extensionAssociationId** | **String**| The ID of the extension association to delete. | 
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


## deleteHostedConfigurationVersion

> deleteHostedConfigurationVersion(applicationId, configurationProfileId, versionNumber, opts)



Deletes a version of a configuration from the AppConfig hosted configuration store.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let configurationProfileId = "configurationProfileId_example"; // String | The configuration profile ID.
let versionNumber = 56; // Number | The versions number to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteHostedConfigurationVersion(applicationId, configurationProfileId, versionNumber, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **configurationProfileId** | **String**| The configuration profile ID. | 
 **versionNumber** | **Number**| The versions number to delete. | 
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


## getApplication

> Application getApplication(applicationId, opts)



Retrieves information about an application.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The ID of the application you want to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApplication(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The ID of the application you want to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfiguration

> Configuration getConfiguration(application, environment, configuration, clientId, opts)



&lt;p&gt;(Deprecated) Retrieves the latest deployed configuration.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Note the following important information.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This API action is deprecated. Calls to receive configuration data should use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html\&quot;&gt;StartConfigurationSession&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html\&quot;&gt;GetLatestConfiguration&lt;/a&gt; APIs instead. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetConfiguration&lt;/code&gt; is a priced call. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/systems-manager/pricing/\&quot;&gt;Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt;

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let application = "application_example"; // String | The application to get. Specify either the application name or the application ID.
let environment = "environment_example"; // String | The environment to get. Specify either the environment name or the environment ID.
let configuration = "configuration_example"; // String | The configuration to get. Specify either the configuration name or the configuration ID.
let clientId = "clientId_example"; // String | The clientId parameter in the following command is a unique, user-specified ID to identify the client for the configuration. This ID enables AppConfig to deploy the configuration in intervals, as defined in the deployment strategy. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientConfigurationVersion': "clientConfigurationVersion_example" // String | <p>The configuration version returned in the most recent <code>GetConfiguration</code> response.</p> <important> <p>AppConfig uses the value of the <code>ClientConfigurationVersion</code> parameter to identify the configuration version on your clients. If you don’t send <code>ClientConfigurationVersion</code> with each call to <code>GetConfiguration</code>, your clients receive the current configuration. You are charged each time your clients receive a configuration.</p> <p>To avoid excess charges, we recommend you use the <a href=\"https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/StartConfigurationSession.html\">StartConfigurationSession</a> and <a href=\"https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/GetLatestConfiguration.html\">GetLatestConfiguration</a> APIs, which track the client configuration version on your behalf. If you choose to continue using <code>GetConfiguration</code>, we recommend that you include the <code>ClientConfigurationVersion</code> value with every call to <code>GetConfiguration</code>. The value to use for <code>ClientConfigurationVersion</code> comes from the <code>ConfigurationVersion</code> attribute returned by <code>GetConfiguration</code> when there is new or updated data, and should be saved for subsequent calls to <code>GetConfiguration</code>.</p> </important> <p>For more information about working with configurations, see <a href=\"http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration.html\">Retrieving the Configuration</a> in the <i>AppConfig User Guide</i>.</p>
};
apiInstance.getConfiguration(application, environment, configuration, clientId, opts, (error, data, response) => {
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
 **application** | **String**| The application to get. Specify either the application name or the application ID. | 
 **environment** | **String**| The environment to get. Specify either the environment name or the environment ID. | 
 **configuration** | **String**| The configuration to get. Specify either the configuration name or the configuration ID. | 
 **clientId** | **String**| The clientId parameter in the following command is a unique, user-specified ID to identify the client for the configuration. This ID enables AppConfig to deploy the configuration in intervals, as defined in the deployment strategy.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientConfigurationVersion** | **String**| &lt;p&gt;The configuration version returned in the most recent &lt;code&gt;GetConfiguration&lt;/code&gt; response.&lt;/p&gt; &lt;important&gt; &lt;p&gt;AppConfig uses the value of the &lt;code&gt;ClientConfigurationVersion&lt;/code&gt; parameter to identify the configuration version on your clients. If you don’t send &lt;code&gt;ClientConfigurationVersion&lt;/code&gt; with each call to &lt;code&gt;GetConfiguration&lt;/code&gt;, your clients receive the current configuration. You are charged each time your clients receive a configuration.&lt;/p&gt; &lt;p&gt;To avoid excess charges, we recommend you use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/StartConfigurationSession.html\&quot;&gt;StartConfigurationSession&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/GetLatestConfiguration.html\&quot;&gt;GetLatestConfiguration&lt;/a&gt; APIs, which track the client configuration version on your behalf. If you choose to continue using &lt;code&gt;GetConfiguration&lt;/code&gt;, we recommend that you include the &lt;code&gt;ClientConfigurationVersion&lt;/code&gt; value with every call to &lt;code&gt;GetConfiguration&lt;/code&gt;. The value to use for &lt;code&gt;ClientConfigurationVersion&lt;/code&gt; comes from the &lt;code&gt;ConfigurationVersion&lt;/code&gt; attribute returned by &lt;code&gt;GetConfiguration&lt;/code&gt; when there is new or updated data, and should be saved for subsequent calls to &lt;code&gt;GetConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about working with configurations, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration.html\&quot;&gt;Retrieving the Configuration&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.&lt;/p&gt; | [optional] 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfigurationProfile

> ConfigurationProfile getConfigurationProfile(applicationId, configurationProfileId, opts)



Retrieves information about a configuration profile.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The ID of the application that includes the configuration profile you want to get.
let configurationProfileId = "configurationProfileId_example"; // String | The ID of the configuration profile that you want to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getConfigurationProfile(applicationId, configurationProfileId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The ID of the application that includes the configuration profile you want to get. | 
 **configurationProfileId** | **String**| The ID of the configuration profile that you want to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ConfigurationProfile**](ConfigurationProfile.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeployment

> Deployment getDeployment(applicationId, environmentId, deploymentNumber, opts)



Retrieves information about a configuration deployment.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The ID of the application that includes the deployment you want to get. 
let environmentId = "environmentId_example"; // String | The ID of the environment that includes the deployment you want to get. 
let deploymentNumber = 56; // Number | The sequence number of the deployment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDeployment(applicationId, environmentId, deploymentNumber, opts, (error, data, response) => {
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
 **applicationId** | **String**| The ID of the application that includes the deployment you want to get.  | 
 **environmentId** | **String**| The ID of the environment that includes the deployment you want to get.  | 
 **deploymentNumber** | **Number**| The sequence number of the deployment. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeploymentStrategy

> DeploymentStrategy getDeploymentStrategy(deploymentStrategyId, opts)



Retrieves information about a deployment strategy. A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let deploymentStrategyId = "deploymentStrategyId_example"; // String | The ID of the deployment strategy to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDeploymentStrategy(deploymentStrategyId, opts, (error, data, response) => {
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
 **deploymentStrategyId** | **String**| The ID of the deployment strategy to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeploymentStrategy**](DeploymentStrategy.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEnvironment

> Environment getEnvironment(applicationId, environmentId, opts)



Retrieves information about an environment. An environment is a deployment group of AppConfig applications, such as applications in a &lt;code&gt;Production&lt;/code&gt; environment or in an &lt;code&gt;EU_Region&lt;/code&gt; environment. Each configuration deployment targets an environment. You can enable one or more Amazon CloudWatch alarms for an environment. If an alarm is triggered during a deployment, AppConfig roles back the configuration.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The ID of the application that includes the environment you want to get.
let environmentId = "environmentId_example"; // String | The ID of the environment that you want to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEnvironment(applicationId, environmentId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The ID of the application that includes the environment you want to get. | 
 **environmentId** | **String**| The ID of the environment that you want to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Environment**](Environment.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExtension

> Extension getExtension(extensionIdentifier, opts)



Returns information about an AppConfig extension.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let extensionIdentifier = "extensionIdentifier_example"; // String | The name, the ID, or the Amazon Resource Name (ARN) of the extension.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'versionNumber': 56 // Number | The extension version number. If no version number was defined, AppConfig uses the highest version.
};
apiInstance.getExtension(extensionIdentifier, opts, (error, data, response) => {
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
 **extensionIdentifier** | **String**| The name, the ID, or the Amazon Resource Name (ARN) of the extension. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **versionNumber** | **Number**| The extension version number. If no version number was defined, AppConfig uses the highest version. | [optional] 

### Return type

[**Extension**](Extension.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExtensionAssociation

> ExtensionAssociation getExtensionAssociation(extensionAssociationId, opts)



Returns information about an AppConfig extension association. For more information about extensions and associations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let extensionAssociationId = "extensionAssociationId_example"; // String | The extension association ID to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getExtensionAssociation(extensionAssociationId, opts, (error, data, response) => {
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
 **extensionAssociationId** | **String**| The extension association ID to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ExtensionAssociation**](ExtensionAssociation.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHostedConfigurationVersion

> HostedConfigurationVersion getHostedConfigurationVersion(applicationId, configurationProfileId, versionNumber, opts)



Retrieves information about a specific configuration version.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let configurationProfileId = "configurationProfileId_example"; // String | The configuration profile ID.
let versionNumber = 56; // Number | The version.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getHostedConfigurationVersion(applicationId, configurationProfileId, versionNumber, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **configurationProfileId** | **String**| The configuration profile ID. | 
 **versionNumber** | **Number**| The version. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**HostedConfigurationVersion**](HostedConfigurationVersion.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApplications

> Applications listApplications(opts)



Lists all applications in your Amazon Web Services account.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
  'nextToken': "nextToken_example", // String | A token to start the list. Next token is a pagination token generated by AppConfig to describe what page the previous List call ended on. For the first List request, the nextToken should not be set. On subsequent calls, the nextToken parameter should be set to the previous responses nextToken value. Use this token to get the next set of results. 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listApplications(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. | [optional] 
 **nextToken** | **String**| A token to start the list. Next token is a pagination token generated by AppConfig to describe what page the previous List call ended on. For the first List request, the nextToken should not be set. On subsequent calls, the nextToken parameter should be set to the previous responses nextToken value. Use this token to get the next set of results.  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**Applications**](Applications.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigurationProfiles

> ConfigurationProfiles listConfigurationProfiles(applicationId, opts)



Lists the configuration profiles for an application.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
  'nextToken': "nextToken_example", // String | A token to start the list. Use this token to get the next set of results.
  'type': "type_example", // String | A filter based on the type of configurations that the configuration profile contains. A configuration can be a feature flag or a freeform configuration.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listConfigurationProfiles(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. | [optional] 
 **nextToken** | **String**| A token to start the list. Use this token to get the next set of results. | [optional] 
 **type** | **String**| A filter based on the type of configurations that the configuration profile contains. A configuration can be a feature flag or a freeform configuration. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ConfigurationProfiles**](ConfigurationProfiles.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeploymentStrategies

> DeploymentStrategies listDeploymentStrategies(opts)



Lists deployment strategies.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
  'nextToken': "nextToken_example", // String | A token to start the list. Use this token to get the next set of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listDeploymentStrategies(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. | [optional] 
 **nextToken** | **String**| A token to start the list. Use this token to get the next set of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**DeploymentStrategies**](DeploymentStrategies.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeployments

> Deployments listDeployments(applicationId, environmentId, opts)



Lists the deployments for an environment in descending deployment number order.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let environmentId = "environmentId_example"; // String | The environment ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of items that may be returned for this call. If there are items that have not yet been returned, the response will include a non-null <code>NextToken</code> that you can provide in a subsequent call to get the next set of results.
  'nextToken': "nextToken_example", // String | The token returned by a prior call to this operation indicating the next set of results to be returned. If not specified, the operation will return the first set of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listDeployments(applicationId, environmentId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **environmentId** | **String**| The environment ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of items that may be returned for this call. If there are items that have not yet been returned, the response will include a non-null &lt;code&gt;NextToken&lt;/code&gt; that you can provide in a subsequent call to get the next set of results. | [optional] 
 **nextToken** | **String**| The token returned by a prior call to this operation indicating the next set of results to be returned. If not specified, the operation will return the first set of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**Deployments**](Deployments.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEnvironments

> Environments listEnvironments(applicationId, opts)



Lists the environments for an application.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
  'nextToken': "nextToken_example", // String | A token to start the list. Use this token to get the next set of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listEnvironments(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. | [optional] 
 **nextToken** | **String**| A token to start the list. Use this token to get the next set of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**Environments**](Environments.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listExtensionAssociations

> ExtensionAssociations listExtensionAssociations(opts)



Lists all AppConfig extension associations in the account. For more information about extensions and associations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'resourceIdentifier': "resourceIdentifier_example", // String | The ARN of an application, configuration profile, or environment.
  'extensionIdentifier': "extensionIdentifier_example", // String | The name, the ID, or the Amazon Resource Name (ARN) of the extension.
  'extensionVersionNumber': 56, // Number | The version number for the extension defined in the association.
  'maxResults': 56, // Number | The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
  'nextToken': "nextToken_example", // String | A token to start the list. Use this token to get the next set of results or pass null to get the first set of results. 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listExtensionAssociations(opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**| The ARN of an application, configuration profile, or environment. | [optional] 
 **extensionIdentifier** | **String**| The name, the ID, or the Amazon Resource Name (ARN) of the extension. | [optional] 
 **extensionVersionNumber** | **Number**| The version number for the extension defined in the association. | [optional] 
 **maxResults** | **Number**| The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. | [optional] 
 **nextToken** | **String**| A token to start the list. Use this token to get the next set of results or pass null to get the first set of results.  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ExtensionAssociations**](ExtensionAssociations.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listExtensions

> Extensions listExtensions(opts)



Lists all custom and Amazon Web Services authored AppConfig extensions in the account. For more information about extensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
  'nextToken': "nextToken_example", // String | A token to start the list. Use this token to get the next set of results. 
  'name': "name_example", // String | The extension name.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listExtensions(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. | [optional] 
 **nextToken** | **String**| A token to start the list. Use this token to get the next set of results.  | [optional] 
 **name** | **String**| The extension name. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**Extensions**](Extensions.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHostedConfigurationVersions

> HostedConfigurationVersions listHostedConfigurationVersions(applicationId, configurationProfileId, opts)



Lists configurations stored in the AppConfig hosted configuration store by version.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let configurationProfileId = "configurationProfileId_example"; // String | The configuration profile ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
  'nextToken': "nextToken_example", // String | A token to start the list. Use this token to get the next set of results. 
  'versionLabel': "versionLabel_example", // String | An optional filter that can be used to specify the version label of an AppConfig hosted configuration version. This parameter supports filtering by prefix using a wildcard, for example \"v2*\". If you don't specify an asterisk at the end of the value, only an exact match is returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listHostedConfigurationVersions(applicationId, configurationProfileId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **configurationProfileId** | **String**| The configuration profile ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. | [optional] 
 **nextToken** | **String**| A token to start the list. Use this token to get the next set of results.  | [optional] 
 **versionLabel** | **String**| An optional filter that can be used to specify the version label of an AppConfig hosted configuration version. This parameter supports filtering by prefix using a wildcard, for example \&quot;v2*\&quot;. If you don&#39;t specify an asterisk at the end of the value, only an exact match is returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**HostedConfigurationVersions**](HostedConfigurationVersions.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ResourceTags listTagsForResource(resourceArn, opts)



Retrieves the list of key-value tags assigned to the resource.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource ARN.
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
 **resourceArn** | **String**| The resource ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ResourceTags**](ResourceTags.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startDeployment

> Deployment startDeployment(applicationId, environmentId, startDeploymentRequest, opts)



Starts a deployment.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let environmentId = "environmentId_example"; // String | The environment ID.
let startDeploymentRequest = new AmazonAppConfig.StartDeploymentRequest(); // StartDeploymentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startDeployment(applicationId, environmentId, startDeploymentRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **environmentId** | **String**| The environment ID. | 
 **startDeploymentRequest** | [**StartDeploymentRequest**](StartDeploymentRequest.md)|  | 
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


## stopDeployment

> Deployment stopDeployment(applicationId, environmentId, deploymentNumber, opts)



Stops a deployment. This API action works only on deployments that have a status of &lt;code&gt;DEPLOYING&lt;/code&gt;. This action moves the deployment to a status of &lt;code&gt;ROLLED_BACK&lt;/code&gt;.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let environmentId = "environmentId_example"; // String | The environment ID.
let deploymentNumber = 56; // Number | The sequence number of the deployment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopDeployment(applicationId, environmentId, deploymentNumber, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **environmentId** | **String**| The environment ID. | 
 **deploymentNumber** | **Number**| The sequence number of the deployment. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## tagResource

> tagResource(resourceArn, tagResourceRequest, opts)



Assigns metadata to an AppConfig resource. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource for which to retrieve tags.
let tagResourceRequest = new AmazonAppConfig.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The ARN of the resource for which to retrieve tags. | 
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


## untagResource

> untagResource(resourceArn, tagKeys, opts)



Deletes a tag key and value from an AppConfig resource.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource for which to remove tags.
let tagKeys = ["null"]; // [String] | The tag keys to delete.
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
 **resourceArn** | **String**| The ARN of the resource for which to remove tags. | 
 **tagKeys** | [**[String]**](String.md)| The tag keys to delete. | 
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


## updateApplication

> Application updateApplication(applicationId, updateApplicationRequest, opts)



Updates an application.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let updateApplicationRequest = new AmazonAppConfig.UpdateApplicationRequest(); // UpdateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApplication(applicationId, updateApplicationRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **updateApplicationRequest** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateConfigurationProfile

> ConfigurationProfile updateConfigurationProfile(applicationId, configurationProfileId, updateConfigurationProfileRequest, opts)



Updates a configuration profile.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let configurationProfileId = "configurationProfileId_example"; // String | The ID of the configuration profile.
let updateConfigurationProfileRequest = new AmazonAppConfig.UpdateConfigurationProfileRequest(); // UpdateConfigurationProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateConfigurationProfile(applicationId, configurationProfileId, updateConfigurationProfileRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **configurationProfileId** | **String**| The ID of the configuration profile. | 
 **updateConfigurationProfileRequest** | [**UpdateConfigurationProfileRequest**](UpdateConfigurationProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ConfigurationProfile**](ConfigurationProfile.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeploymentStrategy

> DeploymentStrategy updateDeploymentStrategy(deploymentStrategyId, updateDeploymentStrategyRequest, opts)



Updates a deployment strategy.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let deploymentStrategyId = "deploymentStrategyId_example"; // String | The deployment strategy ID.
let updateDeploymentStrategyRequest = new AmazonAppConfig.UpdateDeploymentStrategyRequest(); // UpdateDeploymentStrategyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDeploymentStrategy(deploymentStrategyId, updateDeploymentStrategyRequest, opts, (error, data, response) => {
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
 **deploymentStrategyId** | **String**| The deployment strategy ID. | 
 **updateDeploymentStrategyRequest** | [**UpdateDeploymentStrategyRequest**](UpdateDeploymentStrategyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeploymentStrategy**](DeploymentStrategy.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEnvironment

> Environment updateEnvironment(applicationId, environmentId, updateEnvironmentRequest, opts)



Updates an environment.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let environmentId = "environmentId_example"; // String | The environment ID.
let updateEnvironmentRequest = new AmazonAppConfig.UpdateEnvironmentRequest(); // UpdateEnvironmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEnvironment(applicationId, environmentId, updateEnvironmentRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **environmentId** | **String**| The environment ID. | 
 **updateEnvironmentRequest** | [**UpdateEnvironmentRequest**](UpdateEnvironmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Environment**](Environment.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateExtension

> Extension updateExtension(extensionIdentifier, updateExtensionRequest, opts)



Updates an AppConfig extension. For more information about extensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let extensionIdentifier = "extensionIdentifier_example"; // String | The name, the ID, or the Amazon Resource Name (ARN) of the extension.
let updateExtensionRequest = new AmazonAppConfig.UpdateExtensionRequest(); // UpdateExtensionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateExtension(extensionIdentifier, updateExtensionRequest, opts, (error, data, response) => {
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
 **extensionIdentifier** | **String**| The name, the ID, or the Amazon Resource Name (ARN) of the extension. | 
 **updateExtensionRequest** | [**UpdateExtensionRequest**](UpdateExtensionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**Extension**](Extension.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateExtensionAssociation

> ExtensionAssociation updateExtensionAssociation(extensionAssociationId, updateExtensionAssociationRequest, opts)



Updates an association. For more information about extensions and associations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let extensionAssociationId = "extensionAssociationId_example"; // String | The system-generated ID for the association.
let updateExtensionAssociationRequest = new AmazonAppConfig.UpdateExtensionAssociationRequest(); // UpdateExtensionAssociationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateExtensionAssociation(extensionAssociationId, updateExtensionAssociationRequest, opts, (error, data, response) => {
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
 **extensionAssociationId** | **String**| The system-generated ID for the association. | 
 **updateExtensionAssociationRequest** | [**UpdateExtensionAssociationRequest**](UpdateExtensionAssociationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ExtensionAssociation**](ExtensionAssociation.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validateConfiguration

> validateConfiguration(applicationId, configurationProfileId, configurationVersion, opts)



Uses the validators in a configuration profile to validate a configuration.

### Example

```javascript
import AmazonAppConfig from 'amazon_app_config';
let defaultClient = AmazonAppConfig.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonAppConfig.DefaultApi();
let applicationId = "applicationId_example"; // String | The application ID.
let configurationProfileId = "configurationProfileId_example"; // String | The configuration profile ID.
let configurationVersion = "configurationVersion_example"; // String | The version of the configuration to validate.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.validateConfiguration(applicationId, configurationProfileId, configurationVersion, opts, (error, data, response) => {
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
 **applicationId** | **String**| The application ID. | 
 **configurationProfileId** | **String**| The configuration profile ID. | 
 **configurationVersion** | **String**| The version of the configuration to validate. | 
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

