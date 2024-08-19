# OriginGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**originGroupsCreate**](OriginGroupsApi.md#originGroupsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups/{originGroupName} |  |
| [**originGroupsDelete**](OriginGroupsApi.md#originGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups/{originGroupName} |  |
| [**originGroupsGet**](OriginGroupsApi.md#originGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups/{originGroupName} |  |
| [**originGroupsListByEndpoint**](OriginGroupsApi.md#originGroupsListByEndpoint) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups |  |
| [**originGroupsUpdate**](OriginGroupsApi.md#originGroupsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups/{originGroupName} |  |


<a id="originGroupsCreate"></a>
# **originGroupsCreate**
> OriginGroup originGroupsCreate(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, originGroup)



Creates a new origin group within the specified endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginGroupsApi apiInstance = new OriginGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String originGroupName = "originGroupName_example"; // String | Name of the origin group which is unique within the endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    OriginGroup originGroup = new OriginGroup(); // OriginGroup | Origin group properties
    try {
      OriginGroup result = apiInstance.originGroupsCreate(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, originGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginGroupsApi#originGroupsCreate");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **originGroupName** | **String**| Name of the origin group which is unique within the endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **originGroup** | [**OriginGroup**](OriginGroup.md)| Origin group properties | |

### Return type

[**OriginGroup**](OriginGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. The request has been fulfilled and a new origin group has been created. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="originGroupsDelete"></a>
# **originGroupsDelete**
> originGroupsDelete(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion)



Deletes an existing origin group within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginGroupsApi apiInstance = new OriginGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String originGroupName = "originGroupName_example"; // String | Name of the origin group which is unique within the endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      apiInstance.originGroupsDelete(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginGroupsApi#originGroupsDelete");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **originGroupName** | **String**| Name of the origin group which is unique within the endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

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
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | No Content. The request has been accepted but the origin was not found. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="originGroupsGet"></a>
# **originGroupsGet**
> OriginGroup originGroupsGet(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion)



Gets an existing origin group within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginGroupsApi apiInstance = new OriginGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String originGroupName = "originGroupName_example"; // String | Name of the origin group which is unique within the endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      OriginGroup result = apiInstance.originGroupsGet(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginGroupsApi#originGroupsGet");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **originGroupName** | **String**| Name of the origin group which is unique within the endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

### Return type

[**OriginGroup**](OriginGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="originGroupsListByEndpoint"></a>
# **originGroupsListByEndpoint**
> OriginGroupListResult originGroupsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Lists all of the existing origin groups within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginGroupsApi apiInstance = new OriginGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      OriginGroupListResult result = apiInstance.originGroupsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginGroupsApi#originGroupsListByEndpoint");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

### Return type

[**OriginGroupListResult**](OriginGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="originGroupsUpdate"></a>
# **originGroupsUpdate**
> OriginGroup originGroupsUpdate(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, originGroupUpdateProperties)



Updates an existing origin group within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginGroupsApi apiInstance = new OriginGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String originGroupName = "originGroupName_example"; // String | Name of the origin group which is unique within the endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    OriginGroupUpdateParameters originGroupUpdateProperties = new OriginGroupUpdateParameters(); // OriginGroupUpdateParameters | Origin group properties
    try {
      OriginGroup result = apiInstance.originGroupsUpdate(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, originGroupUpdateProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginGroupsApi#originGroupsUpdate");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **originGroupName** | **String**| Name of the origin group which is unique within the endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **originGroupUpdateProperties** | [**OriginGroupUpdateParameters**](OriginGroupUpdateParameters.md)| Origin group properties | |

### Return type

[**OriginGroup**](OriginGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

