# ProductsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsDownload**](ProductsApi.md#productsDownload) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/products/{productName}/download |  |
| [**productsGet**](ProductsApi.md#productsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/products/{productName} |  |
| [**productsList**](ProductsApi.md#productsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/products |  |


<a id="productsDownload"></a>
# **productsDownload**
> ProductsDownload200Response productsDownload(subscriptionId, resourceGroup, activationName, productName, apiVersion)



Downloads a product from azure marketplace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String productName = "productName_example"; // String | Name of the product.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    try {
      ProductsDownload200Response result = apiInstance.productsDownload(subscriptionId, resourceGroup, activationName, productName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsDownload");
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

[**ProductsDownload200Response**](ProductsDownload200Response.md)

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

<a id="productsGet"></a>
# **productsGet**
> ProductResource productsGet(subscriptionId, resourceGroup, activationName, productName, apiVersion)



Return product name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String productName = "productName_example"; // String | Name of the product.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    try {
      ProductResource result = apiInstance.productsGet(subscriptionId, resourceGroup, activationName, productName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsGet");
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

[**ProductResource**](ProductResource.md)

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

<a id="productsList"></a>
# **productsList**
> ProductResourcesPage productsList(subscriptionId, resourceGroup, activationName, apiVersion)



Return product name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
    String activationName = "activationName_example"; // String | Name of the activation.
    String apiVersion = "2016-01-01"; // String | Client Api Version.
    try {
      ProductResourcesPage result = apiInstance.productsList(subscriptionId, resourceGroup, activationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsList");
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

[**ProductResourcesPage**](ProductResourcesPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

