# PricingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pricingsCreateOrUpdateResourceGroupPricing**](PricingsApi.md#pricingsCreateOrUpdateResourceGroupPricing) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/pricings/{pricingName} |  |
| [**pricingsGetResourceGroupPricing**](PricingsApi.md#pricingsGetResourceGroupPricing) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/pricings/{pricingName} |  |
| [**pricingsGetSubscriptionPricing**](PricingsApi.md#pricingsGetSubscriptionPricing) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName} |  |
| [**pricingsList**](PricingsApi.md#pricingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings |  |
| [**pricingsListByResourceGroup**](PricingsApi.md#pricingsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/pricings |  |
| [**pricingsUpdateSubscriptionPricing**](PricingsApi.md#pricingsUpdateSubscriptionPricing) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName} |  |


<a id="pricingsCreateOrUpdateResourceGroupPricing"></a>
# **pricingsCreateOrUpdateResourceGroupPricing**
> Pricing pricingsCreateOrUpdateResourceGroupPricing(apiVersion, subscriptionId, resourceGroupName, pricingName, pricing)



Security pricing configuration in the resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricingsApi apiInstance = new PricingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String pricingName = "pricingName_example"; // String | name of the pricing configuration
    Pricing pricing = new Pricing(); // Pricing | Pricing object
    try {
      Pricing result = apiInstance.pricingsCreateOrUpdateResourceGroupPricing(apiVersion, subscriptionId, resourceGroupName, pricingName, pricing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingsApi#pricingsCreateOrUpdateResourceGroupPricing");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **pricingName** | **String**| name of the pricing configuration | |
| **pricing** | [**Pricing**](Pricing.md)| Pricing object | |

### Return type

[**Pricing**](Pricing.md)

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

<a id="pricingsGetResourceGroupPricing"></a>
# **pricingsGetResourceGroupPricing**
> Pricing pricingsGetResourceGroupPricing(apiVersion, subscriptionId, resourceGroupName, pricingName)



Security pricing configuration in the resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricingsApi apiInstance = new PricingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String pricingName = "pricingName_example"; // String | name of the pricing configuration
    try {
      Pricing result = apiInstance.pricingsGetResourceGroupPricing(apiVersion, subscriptionId, resourceGroupName, pricingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingsApi#pricingsGetResourceGroupPricing");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **pricingName** | **String**| name of the pricing configuration | |

### Return type

[**Pricing**](Pricing.md)

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

<a id="pricingsGetSubscriptionPricing"></a>
# **pricingsGetSubscriptionPricing**
> Pricing pricingsGetSubscriptionPricing(apiVersion, subscriptionId, pricingName)



Security pricing configuration in the subscriptionSecurity pricing configuration in the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricingsApi apiInstance = new PricingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String pricingName = "pricingName_example"; // String | name of the pricing configuration
    try {
      Pricing result = apiInstance.pricingsGetSubscriptionPricing(apiVersion, subscriptionId, pricingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingsApi#pricingsGetSubscriptionPricing");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **pricingName** | **String**| name of the pricing configuration | |

### Return type

[**Pricing**](Pricing.md)

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

<a id="pricingsList"></a>
# **pricingsList**
> PricingList pricingsList(apiVersion, subscriptionId)



Security pricing configurations in the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricingsApi apiInstance = new PricingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      PricingList result = apiInstance.pricingsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingsApi#pricingsList");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**PricingList**](PricingList.md)

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

<a id="pricingsListByResourceGroup"></a>
# **pricingsListByResourceGroup**
> PricingList pricingsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Security pricing configurations in the resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricingsApi apiInstance = new PricingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    try {
      PricingList result = apiInstance.pricingsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingsApi#pricingsListByResourceGroup");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |

### Return type

[**PricingList**](PricingList.md)

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

<a id="pricingsUpdateSubscriptionPricing"></a>
# **pricingsUpdateSubscriptionPricing**
> Pricing pricingsUpdateSubscriptionPricing(apiVersion, subscriptionId, pricingName, pricing)



Security pricing configuration in the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricingsApi apiInstance = new PricingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String pricingName = "pricingName_example"; // String | name of the pricing configuration
    Pricing pricing = new Pricing(); // Pricing | Pricing object
    try {
      Pricing result = apiInstance.pricingsUpdateSubscriptionPricing(apiVersion, subscriptionId, pricingName, pricing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingsApi#pricingsUpdateSubscriptionPricing");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **pricingName** | **String**| name of the pricing configuration | |
| **pricing** | [**Pricing**](Pricing.md)| Pricing object | |

### Return type

[**Pricing**](Pricing.md)

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

