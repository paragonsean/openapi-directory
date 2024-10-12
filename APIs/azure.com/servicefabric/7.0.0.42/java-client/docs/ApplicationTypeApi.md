# ApplicationTypeApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getApplicationManifest**](ApplicationTypeApi.md#getApplicationManifest) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetApplicationManifest | Gets the manifest describing an application type. |
| [**getApplicationTypeInfoList**](ApplicationTypeApi.md#getApplicationTypeInfoList) | **GET** /ApplicationTypes | Gets the list of application types in the Service Fabric cluster. |
| [**getApplicationTypeInfoListByName**](ApplicationTypeApi.md#getApplicationTypeInfoListByName) | **GET** /ApplicationTypes/{applicationTypeName} | Gets the list of application types in the Service Fabric cluster matching exactly the specified name. |
| [**provisionApplicationType**](ApplicationTypeApi.md#provisionApplicationType) | **POST** /ApplicationTypes/$/Provision | Provisions or registers a Service Fabric application type with the cluster using the &#39;.sfpkg&#39; package in the external store or using the application package in the image store. |
| [**unprovisionApplicationType**](ApplicationTypeApi.md#unprovisionApplicationType) | **POST** /ApplicationTypes/{applicationTypeName}/$/Unprovision | Removes or unregisters a Service Fabric application type from the cluster. |


<a id="getApplicationManifest"></a>
# **getApplicationManifest**
> ApplicationTypeManifest getApplicationManifest(apiVersion, applicationTypeName, applicationTypeVersion, timeout)

Gets the manifest describing an application type.

The response contains the application manifest XML as a string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationTypeApi apiInstance = new ApplicationTypeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
    String applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      ApplicationTypeManifest result = apiInstance.getApplicationManifest(apiVersion, applicationTypeName, applicationTypeVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeApi#getApplicationManifest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **applicationTypeName** | **String**| The name of the application type. | |
| **applicationTypeVersion** | **String**| The version of the application type. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**ApplicationTypeManifest**](ApplicationTypeManifest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the node. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getApplicationTypeInfoList"></a>
# **getApplicationTypeInfoList**
> PagedApplicationTypeInfoList getApplicationTypeInfoList(apiVersion, applicationTypeDefinitionKindFilter, excludeApplicationParameters, continuationToken, maxResults, timeout)

Gets the list of application types in the Service Fabric cluster.

Returns the information about the application types that are provisioned or in the process of being provisioned in the Service Fabric cluster. Each version of an application type is returned as one application type. The response includes the name, version, status, and other details about the application type. This is a paged query, meaning that if not all of the application types fit in a page, one page of results is returned as well as a continuation token, which can be used to get the next page. For example, if there are 10 application types but a page only fits the first three application types, or if max results is set to 3, then three is returned. To access the rest of the results, retrieve subsequent pages by using the returned continuation token in the next query. An empty continuation token is returned if there are no subsequent pages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationTypeApi apiInstance = new ApplicationTypeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    Integer applicationTypeDefinitionKindFilter = 0; // Integer | Used to filter on ApplicationTypeDefinitionKind which is the mechanism used to define a Service Fabric application type. - Default - Default value, which performs the same function as selecting \"All\". The value is 0. - All - Filter that matches input with any ApplicationTypeDefinitionKind value. The value is 65535. - ServiceFabricApplicationPackage - Filter that matches input with ApplicationTypeDefinitionKind value ServiceFabricApplicationPackage. The value is 1. - Compose - Filter that matches input with ApplicationTypeDefinitionKind value Compose. The value is 2.
    Boolean excludeApplicationParameters = false; // Boolean | The flag that specifies whether application parameters will be excluded from the result.
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PagedApplicationTypeInfoList result = apiInstance.getApplicationTypeInfoList(apiVersion, applicationTypeDefinitionKindFilter, excludeApplicationParameters, continuationToken, maxResults, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeApi#getApplicationTypeInfoList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **applicationTypeDefinitionKindFilter** | **Integer**| Used to filter on ApplicationTypeDefinitionKind which is the mechanism used to define a Service Fabric application type. - Default - Default value, which performs the same function as selecting \&quot;All\&quot;. The value is 0. - All - Filter that matches input with any ApplicationTypeDefinitionKind value. The value is 65535. - ServiceFabricApplicationPackage - Filter that matches input with ApplicationTypeDefinitionKind value ServiceFabricApplicationPackage. The value is 1. - Compose - Filter that matches input with ApplicationTypeDefinitionKind value Compose. The value is 2. | [optional] [default to 0] |
| **excludeApplicationParameters** | **Boolean**| The flag that specifies whether application parameters will be excluded from the result. | [optional] [default to false] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PagedApplicationTypeInfoList**](PagedApplicationTypeInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of application types in the cluster. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getApplicationTypeInfoListByName"></a>
# **getApplicationTypeInfoListByName**
> PagedApplicationTypeInfoList getApplicationTypeInfoListByName(apiVersion, applicationTypeName, applicationTypeVersion, excludeApplicationParameters, continuationToken, maxResults, timeout)

Gets the list of application types in the Service Fabric cluster matching exactly the specified name.

Returns the information about the application types that are provisioned or in the process of being provisioned in the Service Fabric cluster. These results are of application types whose name match exactly the one specified as the parameter, and which comply with the given query parameters. All versions of the application type matching the application type name are returned, with each version returned as one application type. The response includes the name, version, status, and other details about the application type. This is a paged query, meaning that if not all of the application types fit in a page, one page of results is returned as well as a continuation token, which can be used to get the next page. For example, if there are 10 application types but a page only fits the first three application types, or if max results is set to 3, then three is returned. To access the rest of the results, retrieve subsequent pages by using the returned continuation token in the next query. An empty continuation token is returned if there are no subsequent pages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationTypeApi apiInstance = new ApplicationTypeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
    String applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type.
    Boolean excludeApplicationParameters = false; // Boolean | The flag that specifies whether application parameters will be excluded from the result.
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PagedApplicationTypeInfoList result = apiInstance.getApplicationTypeInfoListByName(apiVersion, applicationTypeName, applicationTypeVersion, excludeApplicationParameters, continuationToken, maxResults, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeApi#getApplicationTypeInfoListByName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **applicationTypeName** | **String**| The name of the application type. | |
| **applicationTypeVersion** | **String**| The version of the application type. | [optional] |
| **excludeApplicationParameters** | **Boolean**| The flag that specifies whether application parameters will be excluded from the result. | [optional] [default to false] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PagedApplicationTypeInfoList**](PagedApplicationTypeInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of application types in the cluster. |  -  |
| **0** | The detailed error response. |  -  |

<a id="provisionApplicationType"></a>
# **provisionApplicationType**
> provisionApplicationType(apiVersion, provisionApplicationTypeDescriptionBaseRequiredBodyParam, timeout)

Provisions or registers a Service Fabric application type with the cluster using the &#39;.sfpkg&#39; package in the external store or using the application package in the image store.

Provisions a Service Fabric application type with the cluster. The provision is required before any new applications can be instantiated. The provision operation can be performed either on the application package specified by the relativePathInImageStore, or by using the URI of the external &#39;.sfpkg&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationTypeApi apiInstance = new ApplicationTypeApi(defaultClient);
    String apiVersion = "6.2"; // String | The version of the API. This parameter is required and its value must be '6.2'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    ProvisionApplicationTypeDescriptionBase provisionApplicationTypeDescriptionBaseRequiredBodyParam = new ProvisionApplicationTypeDescriptionBase(); // ProvisionApplicationTypeDescriptionBase | The base type of provision application type description which supports either image store-based provision or external store-based provision.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.provisionApplicationType(apiVersion, provisionApplicationTypeDescriptionBaseRequiredBodyParam, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeApi#provisionApplicationType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.2] [enum: 6.2] |
| **provisionApplicationTypeDescriptionBaseRequiredBodyParam** | [**ProvisionApplicationTypeDescriptionBase**](ProvisionApplicationTypeDescriptionBase.md)| The base type of provision application type description which supports either image store-based provision or external store-based provision. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful provision will return 200 status code. |  -  |
| **202** | A 202 status code indicates the operation was accepted and the provision operation has been initiated. |  -  |
| **0** | The detailed error response. |  -  |

<a id="unprovisionApplicationType"></a>
# **unprovisionApplicationType**
> unprovisionApplicationType(apiVersion, applicationTypeName, unprovisionApplicationTypeDescriptionInfo, timeout)

Removes or unregisters a Service Fabric application type from the cluster.

This operation can only be performed if all application instances of the application type have been deleted. Once the application type is unregistered, no new application instances can be created for this particular application type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationTypeApi apiInstance = new ApplicationTypeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
    UnprovisionApplicationTypeDescriptionInfo unprovisionApplicationTypeDescriptionInfo = new UnprovisionApplicationTypeDescriptionInfo(); // UnprovisionApplicationTypeDescriptionInfo | The relative path for the application package in the image store specified during the prior copy operation.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.unprovisionApplicationType(apiVersion, applicationTypeName, unprovisionApplicationTypeDescriptionInfo, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeApi#unprovisionApplicationType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **applicationTypeName** | **String**| The name of the application type. | |
| **unprovisionApplicationTypeDescriptionInfo** | [**UnprovisionApplicationTypeDescriptionInfo**](UnprovisionApplicationTypeDescriptionInfo.md)| The relative path for the application package in the image store specified during the prior copy operation. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful provision will return 200 status code. |  -  |
| **202** | A 202 status code indicates the operation was accepted. |  -  |
| **0** | The detailed error response. |  -  |

