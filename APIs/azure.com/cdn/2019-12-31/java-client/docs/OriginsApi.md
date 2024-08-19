# OriginsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**originsCreate**](OriginsApi.md#originsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} |  |
| [**originsDelete**](OriginsApi.md#originsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} |  |
| [**originsGet**](OriginsApi.md#originsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} |  |
| [**originsListByEndpoint**](OriginsApi.md#originsListByEndpoint) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins |  |
| [**originsUpdate**](OriginsApi.md#originsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} |  |


<a id="originsCreate"></a>
# **originsCreate**
> Origin originsCreate(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion, origin)



Creates a new origin within the specified endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String originName = "originName_example"; // String | Name of the origin that is unique within the endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    Origin origin = new Origin(); // Origin | Origin properties
    try {
      Origin result = apiInstance.originsCreate(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion, origin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsCreate");
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
| **originName** | **String**| Name of the origin that is unique within the endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **origin** | [**Origin**](Origin.md)| Origin properties | |

### Return type

[**Origin**](Origin.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. The request has been fulfilled and a new origin has been created. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="originsDelete"></a>
# **originsDelete**
> originsDelete(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion)



Deletes an existing origin within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String originName = "originName_example"; // String | Name of the origin which is unique within the endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      apiInstance.originsDelete(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsDelete");
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
| **originName** | **String**| Name of the origin which is unique within the endpoint. | |
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

<a id="originsGet"></a>
# **originsGet**
> Origin originsGet(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion)



Gets an existing origin within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String originName = "originName_example"; // String | Name of the origin which is unique within the endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      Origin result = apiInstance.originsGet(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsGet");
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
| **originName** | **String**| Name of the origin which is unique within the endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

### Return type

[**Origin**](Origin.md)

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

<a id="originsListByEndpoint"></a>
# **originsListByEndpoint**
> OriginListResult originsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Lists all of the existing origins within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      OriginListResult result = apiInstance.originsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsListByEndpoint");
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

[**OriginListResult**](OriginListResult.md)

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

<a id="originsUpdate"></a>
# **originsUpdate**
> Origin originsUpdate(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion, originUpdateProperties)



Updates an existing origin within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String originName = "originName_example"; // String | Name of the origin which is unique within the endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    OriginUpdateParameters originUpdateProperties = new OriginUpdateParameters(); // OriginUpdateParameters | Origin properties
    try {
      Origin result = apiInstance.originsUpdate(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion, originUpdateProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsUpdate");
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
| **originName** | **String**| Name of the origin which is unique within the endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **originUpdateProperties** | [**OriginUpdateParameters**](OriginUpdateParameters.md)| Origin properties | |

### Return type

[**Origin**](Origin.md)

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

