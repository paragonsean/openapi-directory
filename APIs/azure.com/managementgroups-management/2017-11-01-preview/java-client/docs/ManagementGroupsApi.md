# ManagementGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managementGroupSubscriptionsCreate**](ManagementGroupsApi.md#managementGroupSubscriptionsCreate) | **PUT** /providers/Microsoft.Management/managementGroups/{groupId}/subscriptions/{subscriptionId} |  |
| [**managementGroupSubscriptionsDelete**](ManagementGroupsApi.md#managementGroupSubscriptionsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{groupId}/subscriptions/{subscriptionId} |  |
| [**managementGroupsCreateOrUpdate**](ManagementGroupsApi.md#managementGroupsCreateOrUpdate) | **PUT** /providers/Microsoft.Management/managementGroups/{groupId} |  |
| [**managementGroupsDelete**](ManagementGroupsApi.md#managementGroupsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{groupId} |  |
| [**managementGroupsGet**](ManagementGroupsApi.md#managementGroupsGet) | **GET** /providers/Microsoft.Management/managementGroups/{groupId} |  |
| [**managementGroupsList**](ManagementGroupsApi.md#managementGroupsList) | **GET** /providers/Microsoft.Management/managementGroups |  |
| [**managementGroupsUpdate**](ManagementGroupsApi.md#managementGroupsUpdate) | **PATCH** /providers/Microsoft.Management/managementGroups/{groupId} |  |


<a id="managementGroupSubscriptionsCreate"></a>
# **managementGroupSubscriptionsCreate**
> managementGroupSubscriptionsCreate(groupId, subscriptionId, apiVersion, cacheControl)



Associates existing subscription with the management group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsApi apiInstance = new ManagementGroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | Management Group ID.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    String cacheControl = "no-cache"; // String | Indicates that the request shouldn't utilize any caches.
    try {
      apiInstance.managementGroupSubscriptionsCreate(groupId, subscriptionId, apiVersion, cacheControl);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsApi#managementGroupSubscriptionsCreate");
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
| **groupId** | **String**| Management Group ID. | |
| **subscriptionId** | **String**| Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-01-preview. | |
| **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to no-cache] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error |  -  |

<a id="managementGroupSubscriptionsDelete"></a>
# **managementGroupSubscriptionsDelete**
> managementGroupSubscriptionsDelete(groupId, subscriptionId, apiVersion, cacheControl)



De-associates subscription from the management group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsApi apiInstance = new ManagementGroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | Management Group ID.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    String cacheControl = "no-cache"; // String | Indicates that the request shouldn't utilize any caches.
    try {
      apiInstance.managementGroupSubscriptionsDelete(groupId, subscriptionId, apiVersion, cacheControl);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsApi#managementGroupSubscriptionsDelete");
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
| **groupId** | **String**| Management Group ID. | |
| **subscriptionId** | **String**| Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-01-preview. | |
| **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to no-cache] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content - subscription deleted successfully |  -  |
| **0** | Error |  -  |

<a id="managementGroupsCreateOrUpdate"></a>
# **managementGroupsCreateOrUpdate**
> ManagementGroup managementGroupsCreateOrUpdate(groupId, apiVersion, createManagementGroupRequest, cacheControl)



Create or update a management group. If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsApi apiInstance = new ManagementGroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | Management Group ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    CreateManagementGroupRequest createManagementGroupRequest = new CreateManagementGroupRequest(); // CreateManagementGroupRequest | Management group creation parameters.
    String cacheControl = "no-cache"; // String | Indicates that the request shouldn't utilize any caches.
    try {
      ManagementGroup result = apiInstance.managementGroupsCreateOrUpdate(groupId, apiVersion, createManagementGroupRequest, cacheControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsApi#managementGroupsCreateOrUpdate");
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
| **groupId** | **String**| Management Group ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-01-preview. | |
| **createManagementGroupRequest** | [**CreateManagementGroupRequest**](CreateManagementGroupRequest.md)| Management group creation parameters. | |
| **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to no-cache] |

### Return type

[**ManagementGroup**](ManagementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="managementGroupsDelete"></a>
# **managementGroupsDelete**
> managementGroupsDelete(groupId, apiVersion, cacheControl)



Delete management group. If a management group contains child resources, the request will fail. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsApi apiInstance = new ManagementGroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | Management Group ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    String cacheControl = "no-cache"; // String | Indicates that the request shouldn't utilize any caches.
    try {
      apiInstance.managementGroupsDelete(groupId, apiVersion, cacheControl);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsApi#managementGroupsDelete");
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
| **groupId** | **String**| Management Group ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-01-preview. | |
| **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to no-cache] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - management group deleted successfully |  -  |
| **204** | NoContent - management group does not exist |  -  |
| **0** | Error |  -  |

<a id="managementGroupsGet"></a>
# **managementGroupsGet**
> ManagementGroup managementGroupsGet(groupId, apiVersion, $expand, $recurse, cacheControl)



Get the details of the management group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsApi apiInstance = new ManagementGroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | Management Group ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    String $expand = "children"; // String | The $expand=children query string parameter allows clients to request inclusion of children in the response payload.
    Boolean $recurse = true; // Boolean | The $recurse=true query string parameter allows clients to request inclusion of entire hierarchy in the response payload.
    String cacheControl = "no-cache"; // String | Indicates that the request shouldn't utilize any caches.
    try {
      ManagementGroup result = apiInstance.managementGroupsGet(groupId, apiVersion, $expand, $recurse, cacheControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsApi#managementGroupsGet");
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
| **groupId** | **String**| Management Group ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-01-preview. | |
| **$expand** | **String**| The $expand&#x3D;children query string parameter allows clients to request inclusion of children in the response payload. | [optional] [enum: children] |
| **$recurse** | **Boolean**| The $recurse&#x3D;true query string parameter allows clients to request inclusion of entire hierarchy in the response payload. | [optional] |
| **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to no-cache] |

### Return type

[**ManagementGroup**](ManagementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="managementGroupsList"></a>
# **managementGroupsList**
> ManagementGroupListResult managementGroupsList(apiVersion, cacheControl, $skiptoken)



List management groups for the authenticated user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsApi apiInstance = new ManagementGroupsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    String cacheControl = "no-cache"; // String | Indicates that the request shouldn't utilize any caches.
    String $skiptoken = "$skiptoken_example"; // String | Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. 
    try {
      ManagementGroupListResult result = apiInstance.managementGroupsList(apiVersion, cacheControl, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsApi#managementGroupsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-01-preview. | |
| **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to no-cache] |
| **$skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.  | [optional] |

### Return type

[**ManagementGroupListResult**](ManagementGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="managementGroupsUpdate"></a>
# **managementGroupsUpdate**
> ManagementGroup managementGroupsUpdate(groupId, apiVersion, createManagementGroupRequest, cacheControl)



Update a management group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementGroupsApi apiInstance = new ManagementGroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | Management Group ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    CreateManagementGroupRequest createManagementGroupRequest = new CreateManagementGroupRequest(); // CreateManagementGroupRequest | Management group creation parameters.
    String cacheControl = "no-cache"; // String | Indicates that the request shouldn't utilize any caches.
    try {
      ManagementGroup result = apiInstance.managementGroupsUpdate(groupId, apiVersion, createManagementGroupRequest, cacheControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementGroupsApi#managementGroupsUpdate");
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
| **groupId** | **String**| Management Group ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-01-preview. | |
| **createManagementGroupRequest** | [**CreateManagementGroupRequest**](CreateManagementGroupRequest.md)| Management group creation parameters. | |
| **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to no-cache] |

### Return type

[**ManagementGroup**](ManagementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

