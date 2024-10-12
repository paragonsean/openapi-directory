# DownloadedProductsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadedProductsCreate**](DownloadedProductsApi.md#downloadedProductsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/downloadedProducts/{productName} |  |
| [**downloadedProductsDelete**](DownloadedProductsApi.md#downloadedProductsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/downloadedProducts/{productName} |  |
| [**downloadedProductsGet**](DownloadedProductsApi.md#downloadedProductsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/downloadedProducts/{productName} |  |
| [**downloadedProductsList**](DownloadedProductsApi.md#downloadedProductsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/downloadedProducts |  |


<a id="downloadedProductsCreate"></a>
# **downloadedProductsCreate**
> DownloadedProductsGet200Response downloadedProductsCreate(subscriptionId, resourceGroup, activationName, productName, apiVersion, downloadedProduct)



Creates a downloaded product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadedProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DownloadedProductsApi apiInstance = new DownloadedProductsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String productName = "productName_example"; // String | Name of the product.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    DownloadedProductsGet200Response downloadedProduct = new DownloadedProductsGet200Response(); // DownloadedProductsGet200Response | Downloaded product resource definition.
    try {
      DownloadedProductsGet200Response result = apiInstance.downloadedProductsCreate(subscriptionId, resourceGroup, activationName, productName, apiVersion, downloadedProduct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadedProductsApi#downloadedProductsCreate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| The resource group the resource is located under. | |
| **activationName** | **String**| Name of the activation. | |
| **productName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2016-01-01] |
| **downloadedProduct** | [**DownloadedProductsGet200Response**](DownloadedProductsGet200Response.md)| Downloaded product resource definition. | |

### Return type

[**DownloadedProductsGet200Response**](DownloadedProductsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="downloadedProductsDelete"></a>
# **downloadedProductsDelete**
> DownloadedProductsGet200Response downloadedProductsDelete(subscriptionId, resourceGroup, activationName, productName, apiVersion)



Delete a downloaded product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadedProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DownloadedProductsApi apiInstance = new DownloadedProductsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String productName = "productName_example"; // String | Name of the product.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    try {
      DownloadedProductsGet200Response result = apiInstance.downloadedProductsDelete(subscriptionId, resourceGroup, activationName, productName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadedProductsApi#downloadedProductsDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| The resource group the resource is located under. | |
| **activationName** | **String**| Name of the activation. | |
| **productName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2016-01-01] |

### Return type

[**DownloadedProductsGet200Response**](DownloadedProductsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accepted |  -  |
| **202** | Accepted |  -  |
| **404** | Not Found |  -  |

<a id="downloadedProductsGet"></a>
# **downloadedProductsGet**
> DownloadedProductsGet200Response downloadedProductsGet(subscriptionId, resourceGroup, activationName, productName, apiVersion)



Get a downloaded product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadedProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DownloadedProductsApi apiInstance = new DownloadedProductsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String productName = "productName_example"; // String | Name of the product.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    try {
      DownloadedProductsGet200Response result = apiInstance.downloadedProductsGet(subscriptionId, resourceGroup, activationName, productName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadedProductsApi#downloadedProductsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| The resource group the resource is located under. | |
| **activationName** | **String**| Name of the activation. | |
| **productName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2016-01-01] |

### Return type

[**DownloadedProductsGet200Response**](DownloadedProductsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="downloadedProductsList"></a>
# **downloadedProductsList**
> DownloadedProductResourcesPage downloadedProductsList(subscriptionId, resourceGroup, activationName, apiVersion)



Get a list of downloaded products.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadedProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DownloadedProductsApi apiInstance = new DownloadedProductsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    try {
      DownloadedProductResourcesPage result = apiInstance.downloadedProductsList(subscriptionId, resourceGroup, activationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadedProductsApi#downloadedProductsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| The resource group the resource is located under. | |
| **activationName** | **String**| Name of the activation. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2016-01-01] |

### Return type

[**DownloadedProductResourcesPage**](DownloadedProductResourcesPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

