# SharesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharesGet**](SharesApi.md#sharesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName} |  |
| [**sharesList**](SharesApi.md#sharesList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares |  |
| [**sharesListMetricDefinitions**](SharesApi.md#sharesListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/metricdefinitions |  |
| [**sharesListMetrics**](SharesApi.md#sharesListMetrics) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/metrics |  |


<a id="sharesGet"></a>
# **sharesGet**
> Share sharesGet(subscriptionId, resourceGroupName, farmId, shareName, apiVersion)



Returns a storage share.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String shareName = "shareName_example"; // String | Share name.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      Share result = apiInstance.sharesGet(subscriptionId, resourceGroupName, farmId, shareName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sharesGet");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **shareName** | **String**| Share name. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The storage share has been returned. |  -  |
| **404** | NOT FOUND -- The farm or storage share cannot be found. |  -  |

<a id="sharesList"></a>
# **sharesList**
> List&lt;Share&gt; sharesList(subscriptionId, resourceGroupName, farmId, apiVersion)



Returns a list of storage shares.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      List<Share> result = apiInstance.sharesList(subscriptionId, resourceGroupName, farmId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sharesList");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**List&lt;Share&gt;**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of storage shares has been returned. |  -  |
| **404** | NOT FOUND -- The farm cannot be found. |  -  |

<a id="sharesListMetricDefinitions"></a>
# **sharesListMetricDefinitions**
> SharesListMetricDefinitions200Response sharesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, shareName, apiVersion)



Returns a list of metric definitions for a storage share.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String shareName = "shareName_example"; // String | Share name.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      SharesListMetricDefinitions200Response result = apiInstance.sharesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, shareName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sharesListMetricDefinitions");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **shareName** | **String**| Share name. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**SharesListMetricDefinitions200Response**](SharesListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of metric definitions has been returned. |  -  |
| **404** | NOT FOUND -- The farm cannot be found. |  -  |

<a id="sharesListMetrics"></a>
# **sharesListMetrics**
> SharesListMetrics200Response sharesListMetrics(subscriptionId, resourceGroupName, farmId, shareName, apiVersion)



Returns a list of metrics for a storage share.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String shareName = "shareName_example"; // String | Share name.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      SharesListMetrics200Response result = apiInstance.sharesListMetrics(subscriptionId, resourceGroupName, farmId, shareName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sharesListMetrics");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **shareName** | **String**| Share name. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**SharesListMetrics200Response**](SharesListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of metrics has been returned. |  -  |
| **404** | NOT FOUND -- The farm or share cannot be found. |  -  |

