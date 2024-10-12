# ServiceFabricClientApis.ApplicationTypeApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getApplicationManifest**](ApplicationTypeApi.md#getApplicationManifest) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetApplicationManifest | Gets the manifest describing an application type.
[**getApplicationTypeInfoList**](ApplicationTypeApi.md#getApplicationTypeInfoList) | **GET** /ApplicationTypes | Gets the list of application types in the Service Fabric cluster.
[**getApplicationTypeInfoListByName**](ApplicationTypeApi.md#getApplicationTypeInfoListByName) | **GET** /ApplicationTypes/{applicationTypeName} | Gets the list of application types in the Service Fabric cluster matching exactly the specified name.
[**provisionApplicationType**](ApplicationTypeApi.md#provisionApplicationType) | **POST** /ApplicationTypes/$/Provision | Provisions or registers a Service Fabric application type with the cluster.
[**unprovisionApplicationType**](ApplicationTypeApi.md#unprovisionApplicationType) | **POST** /ApplicationTypes/{applicationTypeName}/$/Unprovision | Removes or unregisters a Service Fabric application type from the cluster.



## getApplicationManifest

> ApplicationTypeManifest getApplicationManifest(apiVersion, applicationTypeName, applicationTypeVersion, opts)

Gets the manifest describing an application type.

Gets the manifest describing an application type. The response contains the application manifest XML as a string.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationTypeApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
let applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getApplicationManifest(apiVersion, applicationTypeName, applicationTypeVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **applicationTypeName** | **String**| The name of the application type. | 
 **applicationTypeVersion** | **String**| The version of the application type. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ApplicationTypeManifest**](ApplicationTypeManifest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationTypeInfoList

> PagedApplicationTypeInfoList getApplicationTypeInfoList(apiVersion, opts)

Gets the list of application types in the Service Fabric cluster.

Returns the information about the application types that are provisioned or in the process of being provisioned in the Service Fabric cluster. Each version of an application type is returned as one application type. The response includes the name, version, status and other details about the application type. This is a paged query, meaning that if not all of the application types fit in a page, one page of results is returned as well as a continuation token which can be used to get the next page. For example, if there are 10 application types but a page only fits the first 3 application types, or if max results is set to 3, then 3 is returned. To access the rest of the results, retrieve subsequent pages by using the returned continuation token in the next query. An empty continuation token is returned if there are no subsequent pages.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationTypeApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let opts = {
  'applicationTypeDefinitionKindFilter': 0, // Number | Used to filter on ApplicationTypeDefinitionKind for application type query operations. - Default - Default value, which performs the same function as selecting \"All\". The value is 0. - All - Filter that matches input with any ApplicationTypeDefinitionKind value. The value is 65535. - ServiceFabricApplicationPackage - Filter that matches input with ApplicationTypeDefinitionKind value ServiceFabricApplicationPackage. The value is 1. - Compose - Filter that matches input with ApplicationTypeDefinitionKind value Compose. The value is 2. 
  'excludeApplicationParameters': false, // Boolean | The flag that specifies whether application parameters will be excluded from the result.
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0, // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged queries includes as much results as possible that fit in the return message.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getApplicationTypeInfoList(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **applicationTypeDefinitionKindFilter** | **Number**| Used to filter on ApplicationTypeDefinitionKind for application type query operations. - Default - Default value, which performs the same function as selecting \&quot;All\&quot;. The value is 0. - All - Filter that matches input with any ApplicationTypeDefinitionKind value. The value is 65535. - ServiceFabricApplicationPackage - Filter that matches input with ApplicationTypeDefinitionKind value ServiceFabricApplicationPackage. The value is 1. - Compose - Filter that matches input with ApplicationTypeDefinitionKind value Compose. The value is 2.  | [optional] [default to 0]
 **excludeApplicationParameters** | **Boolean**| The flag that specifies whether application parameters will be excluded from the result. | [optional] [default to false]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged queries includes as much results as possible that fit in the return message. | [optional] [default to 0]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedApplicationTypeInfoList**](PagedApplicationTypeInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationTypeInfoListByName

> PagedApplicationTypeInfoList getApplicationTypeInfoListByName(apiVersion, applicationTypeName, opts)

Gets the list of application types in the Service Fabric cluster matching exactly the specified name.

Returns the information about the application types that are provisioned or in the process of being provisioned in the Service Fabric cluster. These results are of application types whose name match exactly the one specified as the parameter, and which comply with the given query parameters. All versions of the application type matching the application type name are returned, with each version returned as one application type. The response includes the name, version, status and other details about the application type. This is a paged query, meaning that if not all of the application types fit in a page, one page of results is returned as well as a continuation token which can be used to get the next page. For example, if there are 10 application types but a page only fits the first 3 application types, or if max results is set to 3, then 3 is returned. To access the rest of the results, retrieve subsequent pages by using the returned continuation token in the next query. An empty continuation token is returned if there are no subsequent pages.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationTypeApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
let opts = {
  'applicationTypeVersion': "applicationTypeVersion_example", // String | The version of the application type.
  'excludeApplicationParameters': false, // Boolean | The flag that specifies whether application parameters will be excluded from the result.
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0, // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged queries includes as much results as possible that fit in the return message.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getApplicationTypeInfoListByName(apiVersion, applicationTypeName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **applicationTypeName** | **String**| The name of the application type. | 
 **applicationTypeVersion** | **String**| The version of the application type. | [optional] 
 **excludeApplicationParameters** | **Boolean**| The flag that specifies whether application parameters will be excluded from the result. | [optional] [default to false]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged queries includes as much results as possible that fit in the return message. | [optional] [default to 0]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedApplicationTypeInfoList**](PagedApplicationTypeInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## provisionApplicationType

> provisionApplicationType(apiVersion, applicationTypeImageStorePath, opts)

Provisions or registers a Service Fabric application type with the cluster.

Provisions or registers a Service Fabric application type with the cluster. This is required before any new applications can be instantiated.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationTypeApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let applicationTypeImageStorePath = new ServiceFabricClientApis.ApplicationTypeImageStorePath(); // ApplicationTypeImageStorePath | The relative path for the application package in the image store specified during the prior copy operation.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.provisionApplicationType(apiVersion, applicationTypeImageStorePath, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **applicationTypeImageStorePath** | [**ApplicationTypeImageStorePath**](ApplicationTypeImageStorePath.md)| The relative path for the application package in the image store specified during the prior copy operation. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unprovisionApplicationType

> unprovisionApplicationType(apiVersion, applicationTypeName, applicationTypeImageStoreVersion, opts)

Removes or unregisters a Service Fabric application type from the cluster.

Removes or unregisters a Service Fabric application type from the cluster. This operation can only be performed if all application instance of the application type has been deleted. Once the application type is unregistered, no new application instance can be created for this particular application type.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationTypeApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
let applicationTypeImageStoreVersion = new ServiceFabricClientApis.ApplicationTypeImageStoreVersion(); // ApplicationTypeImageStoreVersion | The version of the application type in the image store.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.unprovisionApplicationType(apiVersion, applicationTypeName, applicationTypeImageStoreVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **applicationTypeName** | **String**| The name of the application type. | 
 **applicationTypeImageStoreVersion** | [**ApplicationTypeImageStoreVersion**](ApplicationTypeImageStoreVersion.md)| The version of the application type in the image store. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

