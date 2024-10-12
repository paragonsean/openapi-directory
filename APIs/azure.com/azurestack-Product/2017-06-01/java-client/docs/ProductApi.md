# ProductApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsGet**](ProductApi.md#productsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/{productName} |  |
| [**productsGetProduct**](ProductApi.md#productsGetProduct) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/{productName}/GetProduct |  |
| [**productsGetProducts**](ProductApi.md#productsGetProducts) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/_all/GetProducts |  |
| [**productsList**](ProductApi.md#productsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products |  |
| [**productsListDetails**](ProductApi.md#productsListDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/{productName}/listDetails |  |
| [**productsUploadLog**](ProductApi.md#productsUploadLog) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/{productName}/uploadProductLog |  |


<a id="productsGet"></a>
# **productsGet**
> Product productsGet(subscriptionId, resourceGroup, registrationName, productName, apiVersion)



Returns the specified product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String productName = "productName_example"; // String | Name of the product.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      Product result = apiInstance.productsGet(subscriptionId, resourceGroup, registrationName, productName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **productName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

### Return type

[**Product**](Product.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productsGetProduct"></a>
# **productsGetProduct**
> Product productsGetProduct(subscriptionId, resourceGroup, registrationName, productName, apiVersion, deviceConfiguration)



Returns the specified product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String productName = "productName_example"; // String | Name of the product.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    DeviceConfiguration deviceConfiguration = new DeviceConfiguration(); // DeviceConfiguration | Device configuration.
    try {
      Product result = apiInstance.productsGetProduct(subscriptionId, resourceGroup, registrationName, productName, apiVersion, deviceConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productsGetProduct");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **productName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |
| **deviceConfiguration** | [**DeviceConfiguration**](DeviceConfiguration.md)| Device configuration. | [optional] |

### Return type

[**Product**](Product.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productsGetProducts"></a>
# **productsGetProducts**
> ProductList productsGetProducts(subscriptionId, resourceGroup, registrationName, apiVersion, deviceConfiguration)



Returns a list of products.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    DeviceConfiguration deviceConfiguration = new DeviceConfiguration(); // DeviceConfiguration | Device configuration.
    try {
      ProductList result = apiInstance.productsGetProducts(subscriptionId, resourceGroup, registrationName, apiVersion, deviceConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productsGetProducts");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |
| **deviceConfiguration** | [**DeviceConfiguration**](DeviceConfiguration.md)| Device configuration. | [optional] |

### Return type

[**ProductList**](ProductList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productsList"></a>
# **productsList**
> ProductList productsList(subscriptionId, resourceGroup, registrationName, apiVersion)



Returns a list of products.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      ProductList result = apiInstance.productsList(subscriptionId, resourceGroup, registrationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

### Return type

[**ProductList**](ProductList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productsListDetails"></a>
# **productsListDetails**
> ExtendedProduct productsListDetails(subscriptionId, resourceGroup, registrationName, productName, apiVersion)



Returns the extended properties of a product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String productName = "productName_example"; // String | Name of the product.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      ExtendedProduct result = apiInstance.productsListDetails(subscriptionId, resourceGroup, registrationName, productName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productsListDetails");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **productName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

### Return type

[**ExtendedProduct**](ExtendedProduct.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productsUploadLog"></a>
# **productsUploadLog**
> ProductLog productsUploadLog(subscriptionId, resourceGroup, registrationName, productName, apiVersion, marketplaceProductLogUpdate)



Returns the specified product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String productName = "productName_example"; // String | Name of the product.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    MarketplaceProductLogUpdate marketplaceProductLogUpdate = new MarketplaceProductLogUpdate(); // MarketplaceProductLogUpdate | Update details for product log.
    try {
      ProductLog result = apiInstance.productsUploadLog(subscriptionId, resourceGroup, registrationName, productName, apiVersion, marketplaceProductLogUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productsUploadLog");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **productName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |
| **marketplaceProductLogUpdate** | [**MarketplaceProductLogUpdate**](MarketplaceProductLogUpdate.md)| Update details for product log. | [optional] |

### Return type

[**ProductLog**](ProductLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

