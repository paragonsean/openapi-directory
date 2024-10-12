# AwsServiceCatalogAppRegistry.DefaultApi

All URIs are relative to *http://servicecatalog-appregistry.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateAttributeGroup**](DefaultApi.md#associateAttributeGroup) | **PUT** /applications/{application}/attribute-groups/{attributeGroup} | 
[**associateResource**](DefaultApi.md#associateResource) | **PUT** /applications/{application}/resources/{resourceType}/{resource} | 
[**createApplication**](DefaultApi.md#createApplication) | **POST** /applications | 
[**createAttributeGroup**](DefaultApi.md#createAttributeGroup) | **POST** /attribute-groups | 
[**deleteApplication**](DefaultApi.md#deleteApplication) | **DELETE** /applications/{application} | 
[**deleteAttributeGroup**](DefaultApi.md#deleteAttributeGroup) | **DELETE** /attribute-groups/{attributeGroup} | 
[**disassociateAttributeGroup**](DefaultApi.md#disassociateAttributeGroup) | **DELETE** /applications/{application}/attribute-groups/{attributeGroup} | 
[**disassociateResource**](DefaultApi.md#disassociateResource) | **DELETE** /applications/{application}/resources/{resourceType}/{resource} | 
[**getApplication**](DefaultApi.md#getApplication) | **GET** /applications/{application} | 
[**getAssociatedResource**](DefaultApi.md#getAssociatedResource) | **GET** /applications/{application}/resources/{resourceType}/{resource} | 
[**getAttributeGroup**](DefaultApi.md#getAttributeGroup) | **GET** /attribute-groups/{attributeGroup} | 
[**getConfiguration**](DefaultApi.md#getConfiguration) | **GET** /configuration | 
[**listApplications**](DefaultApi.md#listApplications) | **GET** /applications | 
[**listAssociatedAttributeGroups**](DefaultApi.md#listAssociatedAttributeGroups) | **GET** /applications/{application}/attribute-groups | 
[**listAssociatedResources**](DefaultApi.md#listAssociatedResources) | **GET** /applications/{application}/resources | 
[**listAttributeGroups**](DefaultApi.md#listAttributeGroups) | **GET** /attribute-groups | 
[**listAttributeGroupsForApplication**](DefaultApi.md#listAttributeGroupsForApplication) | **GET** /applications/{application}/attribute-group-details | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**putConfiguration**](DefaultApi.md#putConfiguration) | **PUT** /configuration | 
[**syncResource**](DefaultApi.md#syncResource) | **POST** /sync/{resourceType}/{resource} | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateApplication**](DefaultApi.md#updateApplication) | **PATCH** /applications/{application} | 
[**updateAttributeGroup**](DefaultApi.md#updateAttributeGroup) | **PATCH** /attribute-groups/{attributeGroup} | 



## associateAttributeGroup

> AssociateAttributeGroupResponse associateAttributeGroup(application, attributeGroup, opts)



Associates an attribute group with an application to augment the application&#39;s metadata with the group&#39;s attributes. This feature enables applications to be described with user-defined details that are machine-readable, such as third-party integrations.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String |  The name, ID, or ARN of the application. 
let attributeGroup = "attributeGroup_example"; // String |  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateAttributeGroup(application, attributeGroup, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**|  The name, ID, or ARN of the application.  | 
 **attributeGroup** | **String**|  The name, ID, or ARN of the attribute group that holds the attributes to describe the application.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateAttributeGroupResponse**](AssociateAttributeGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## associateResource

> AssociateResourceResponse associateResource(application, resourceType, resource, opts)



 Associates a resource with an application. The resource can be specified by its ARN or name. The application can be specified by ARN, ID, or name. 

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String |  The name, ID, or ARN of the application. 
let resourceType = "resourceType_example"; // String | The type of resource of which the application will be associated.
let resource = "resource_example"; // String | The name or ID of the resource of which the application will be associated.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateResource(application, resourceType, resource, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**|  The name, ID, or ARN of the application.  | 
 **resourceType** | **String**| The type of resource of which the application will be associated. | 
 **resource** | **String**| The name or ID of the resource of which the application will be associated. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateResourceResponse**](AssociateResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createApplication

> CreateApplicationResponse createApplication(createApplicationRequest, opts)



Creates a new application that is the top-level node in a hierarchy of related cloud resource abstractions.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let createApplicationRequest = new AwsServiceCatalogAppRegistry.CreateApplicationRequest(); // CreateApplicationRequest | 
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

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAttributeGroup

> CreateAttributeGroupResponse createAttributeGroup(createAttributeGroupRequest, opts)



Creates a new attribute group as a container for user-defined attributes. This feature enables users to have full control over their cloud application&#39;s metadata in a rich machine-readable format to facilitate integration with automated workflows and third-party tools.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let createAttributeGroupRequest = new AwsServiceCatalogAppRegistry.CreateAttributeGroupRequest(); // CreateAttributeGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAttributeGroup(createAttributeGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAttributeGroupRequest** | [**CreateAttributeGroupRequest**](CreateAttributeGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAttributeGroupResponse**](CreateAttributeGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplication

> DeleteApplicationResponse deleteApplication(application, opts)



Deletes an application that is specified either by its application ID, name, or ARN. All associated attribute groups and resources must be disassociated from it before deleting an application.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String |  The name, ID, or ARN of the application. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplication(application, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**|  The name, ID, or ARN of the application.  | 
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


## deleteAttributeGroup

> DeleteAttributeGroupResponse deleteAttributeGroup(attributeGroup, opts)



Deletes an attribute group, specified either by its attribute group ID, name, or ARN.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let attributeGroup = "attributeGroup_example"; // String |  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAttributeGroup(attributeGroup, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributeGroup** | **String**|  The name, ID, or ARN of the attribute group that holds the attributes to describe the application.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteAttributeGroupResponse**](DeleteAttributeGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateAttributeGroup

> DisassociateAttributeGroupResponse disassociateAttributeGroup(application, attributeGroup, opts)



Disassociates an attribute group from an application to remove the extra attributes contained in the attribute group from the application&#39;s metadata. This operation reverts &lt;code&gt;AssociateAttributeGroup&lt;/code&gt;.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String |  The name, ID, or ARN of the application. 
let attributeGroup = "attributeGroup_example"; // String |  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateAttributeGroup(application, attributeGroup, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**|  The name, ID, or ARN of the application.  | 
 **attributeGroup** | **String**|  The name, ID, or ARN of the attribute group that holds the attributes to describe the application.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateAttributeGroupResponse**](DisassociateAttributeGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateResource

> DisassociateResourceResponse disassociateResource(application, resourceType, resource, opts)



Disassociates a resource from application. Both the resource and the application can be specified either by ID or name.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String | The name or ID of the application.
let resourceType = "resourceType_example"; // String | The type of the resource that is being disassociated.
let resource = "resource_example"; // String | The name or ID of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateResource(application, resourceType, resource, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**| The name or ID of the application. | 
 **resourceType** | **String**| The type of the resource that is being disassociated. | 
 **resource** | **String**| The name or ID of the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateResourceResponse**](DisassociateResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplication

> GetApplicationResponse getApplication(application, opts)



 Retrieves metadata information about one of your applications. The application can be specified by its ARN, ID, or name (which is unique within one account in one region at a given point in time). Specify by ARN or ID in automated workflows if you want to make sure that the exact same application is returned or a &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown, avoiding the ABA addressing problem. 

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String |  The name, ID, or ARN of the application. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApplication(application, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**|  The name, ID, or ARN of the application.  | 
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


## getAssociatedResource

> GetAssociatedResourceResponse getAssociatedResource(application, resourceType, resource, opts)



Gets the resource associated with the application.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String |  The name, ID, or ARN of the application. 
let resourceType = "resourceType_example"; // String | The type of resource associated with the application.
let resource = "resource_example"; // String | The name or ID of the resource associated with the application.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAssociatedResource(application, resourceType, resource, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**|  The name, ID, or ARN of the application.  | 
 **resourceType** | **String**| The type of resource associated with the application. | 
 **resource** | **String**| The name or ID of the resource associated with the application. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAssociatedResourceResponse**](GetAssociatedResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAttributeGroup

> GetAttributeGroupResponse getAttributeGroup(attributeGroup, opts)



 Retrieves an attribute group by its ARN, ID, or name. The attribute group can be specified by its ARN, ID, or name. 

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let attributeGroup = "attributeGroup_example"; // String |  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAttributeGroup(attributeGroup, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributeGroup** | **String**|  The name, ID, or ARN of the attribute group that holds the attributes to describe the application.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAttributeGroupResponse**](GetAttributeGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfiguration

> GetConfigurationResponse getConfiguration(opts)



 Retrieves a &lt;code&gt;TagKey&lt;/code&gt; configuration from an account. 

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getConfiguration(opts, (error, data, response) => {
  if (error) {
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

[**GetConfigurationResponse**](GetConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApplications

> ListApplicationsResponse listApplications(opts)



Retrieves a list of all of your applications. Results are paginated.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to use to get the next page of results after a previous API call. 
  'maxResults': 56 // Number | The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
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
 **nextToken** | **String**| The token to use to get the next page of results after a previous API call.  | [optional] 
 **maxResults** | **Number**| The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional. | [optional] 

### Return type

[**ListApplicationsResponse**](ListApplicationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssociatedAttributeGroups

> ListAssociatedAttributeGroupsResponse listAssociatedAttributeGroups(application, opts)



Lists all attribute groups that are associated with specified application. Results are paginated.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String | The name or ID of the application.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to use to get the next page of results after a previous API call. 
  'maxResults': 56 // Number | The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
};
apiInstance.listAssociatedAttributeGroups(application, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**| The name or ID of the application. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to use to get the next page of results after a previous API call.  | [optional] 
 **maxResults** | **Number**| The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional. | [optional] 

### Return type

[**ListAssociatedAttributeGroupsResponse**](ListAssociatedAttributeGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssociatedResources

> ListAssociatedResourcesResponse listAssociatedResources(application, opts)



&lt;p&gt; Lists all of the resources that are associated with the specified application. Results are paginated. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you share an application, and a consumer account associates a tag query to the application, all of the users who can access the application can also view the tag values in all accounts that are associated with it using this API. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String |  The name, ID, or ARN of the application. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to use to get the next page of results after a previous API call. 
  'maxResults': 56 // Number | The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
};
apiInstance.listAssociatedResources(application, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**|  The name, ID, or ARN of the application.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to use to get the next page of results after a previous API call.  | [optional] 
 **maxResults** | **Number**| The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional. | [optional] 

### Return type

[**ListAssociatedResourcesResponse**](ListAssociatedResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttributeGroups

> ListAttributeGroupsResponse listAttributeGroups(opts)



Lists all attribute groups which you have access to. Results are paginated.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to use to get the next page of results after a previous API call. 
  'maxResults': 56 // Number | The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
};
apiInstance.listAttributeGroups(opts, (error, data, response) => {
  if (error) {
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
 **nextToken** | **String**| The token to use to get the next page of results after a previous API call.  | [optional] 
 **maxResults** | **Number**| The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional. | [optional] 

### Return type

[**ListAttributeGroupsResponse**](ListAttributeGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttributeGroupsForApplication

> ListAttributeGroupsForApplicationResponse listAttributeGroupsForApplication(application, opts)



Lists the details of all attribute groups associated with a specific application. The results display in pages.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String | The name or ID of the application.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | This token retrieves the next page of results after a previous API call.
  'maxResults': 56 // Number | The upper bound of the number of results to return. The value cannot exceed 25. If you omit this parameter, it defaults to 25. This value is optional.
};
apiInstance.listAttributeGroupsForApplication(application, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**| The name or ID of the application. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| This token retrieves the next page of results after a previous API call. | [optional] 
 **maxResults** | **Number**| The upper bound of the number of results to return. The value cannot exceed 25. If you omit this parameter, it defaults to 25. This value is optional. | [optional] 

### Return type

[**ListAttributeGroupsForApplicationResponse**](ListAttributeGroupsForApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists all of the tags on the resource.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon resource name (ARN) that specifies the resource.
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
 **resourceArn** | **String**| The Amazon resource name (ARN) that specifies the resource. | 
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


## putConfiguration

> putConfiguration(putConfigurationRequest, opts)



 Associates a &lt;code&gt;TagKey&lt;/code&gt; configuration to an account. 

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let putConfigurationRequest = new AwsServiceCatalogAppRegistry.PutConfigurationRequest(); // PutConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putConfiguration(putConfigurationRequest, opts, (error, data, response) => {
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
 **putConfigurationRequest** | [**PutConfigurationRequest**](PutConfigurationRequest.md)|  | 
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


## syncResource

> SyncResourceResponse syncResource(resourceType, resource, opts)



&lt;p&gt;Syncs the resource with current AppRegistry records.&lt;/p&gt; &lt;p&gt;Specifically, the resource’s AppRegistry system tags sync with its associated application. We remove the resource&#39;s AppRegistry system tags if it does not associate with the application. The caller must have permissions to read and update the resource.&lt;/p&gt;

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let resourceType = "resourceType_example"; // String | The type of resource of which the application will be associated.
let resource = "resource_example"; // String | An entity you can work with and specify with a name or ID. Examples include an Amazon EC2 instance, an Amazon Web Services CloudFormation stack, or an Amazon S3 bucket.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.syncResource(resourceType, resource, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceType** | **String**| The type of resource of which the application will be associated. | 
 **resource** | **String**| An entity you can work with and specify with a name or ID. Examples include an Amazon EC2 instance, an Amazon Web Services CloudFormation stack, or an Amazon S3 bucket. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SyncResourceResponse**](SyncResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Assigns one or more tags (key-value pairs) to the specified resource.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and an optional value. If a tag with the same key is already associated with the resource, this action updates its value.&lt;/p&gt; &lt;p&gt;This operation returns an empty response if the call was successful.&lt;/p&gt;

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon resource name (ARN) that specifies the resource.
let tagResourceRequest = new AwsServiceCatalogAppRegistry.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon resource name (ARN) that specifies the resource. | 
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



&lt;p&gt;Removes tags from a resource.&lt;/p&gt; &lt;p&gt;This operation returns an empty response if the call was successful.&lt;/p&gt;

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon resource name (ARN) that specifies the resource.
let tagKeys = ["null"]; // [String] | A list of the tag keys to remove from the specified resource.
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
 **resourceArn** | **String**| The Amazon resource name (ARN) that specifies the resource. | 
 **tagKeys** | [**[String]**](String.md)| A list of the tag keys to remove from the specified resource. | 
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


## updateApplication

> UpdateApplicationResponse updateApplication(application, updateApplicationRequest, opts)



Updates an existing application with new attributes.

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let application = "application_example"; // String |  The name, ID, or ARN of the application that will be updated. 
let updateApplicationRequest = new AwsServiceCatalogAppRegistry.UpdateApplicationRequest(); // UpdateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApplication(application, updateApplicationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **String**|  The name, ID, or ARN of the application that will be updated.  | 
 **updateApplicationRequest** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApplicationResponse**](UpdateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAttributeGroup

> UpdateAttributeGroupResponse updateAttributeGroup(attributeGroup, updateAttributeGroupRequest, opts)



Updates an existing attribute group with new details. 

### Example

```javascript
import AwsServiceCatalogAppRegistry from 'aws_service_catalog_app_registry';
let defaultClient = AwsServiceCatalogAppRegistry.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServiceCatalogAppRegistry.DefaultApi();
let attributeGroup = "attributeGroup_example"; // String |  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
let updateAttributeGroupRequest = new AwsServiceCatalogAppRegistry.UpdateAttributeGroupRequest(); // UpdateAttributeGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAttributeGroup(attributeGroup, updateAttributeGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributeGroup** | **String**|  The name, ID, or ARN of the attribute group that holds the attributes to describe the application.  | 
 **updateAttributeGroupRequest** | [**UpdateAttributeGroupRequest**](UpdateAttributeGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAttributeGroupResponse**](UpdateAttributeGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

