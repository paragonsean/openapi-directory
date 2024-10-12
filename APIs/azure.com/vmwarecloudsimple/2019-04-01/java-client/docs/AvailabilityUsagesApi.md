# AvailabilityUsagesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**skusAvailabilityList**](AvailabilityUsagesApi.md#skusAvailabilityList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/availabilities | Implements SkuAvailability List method |
| [**usagesList**](AvailabilityUsagesApi.md#usagesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/usages | Implements Usages List method |


<a id="skusAvailabilityList"></a>
# **skusAvailabilityList**
> SkuAvailabilityListResponse skusAvailabilityList(subscriptionId, regionId, apiVersion, skuId)

Implements SkuAvailability List method

Returns list of available resources in region

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityUsagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AvailabilityUsagesApi apiInstance = new AvailabilityUsagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String skuId = "skuId_example"; // String | sku id, if no sku is passed availability for all skus will be returned
    try {
      SkuAvailabilityListResponse result = apiInstance.skusAvailabilityList(subscriptionId, regionId, apiVersion, skuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityUsagesApi#skusAvailabilityList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **apiVersion** | **String**| Client API version. | |
| **skuId** | **String**| sku id, if no sku is passed availability for all skus will be returned | [optional] |

### Return type

[**SkuAvailabilityListResponse**](SkuAvailabilityListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="usagesList"></a>
# **usagesList**
> UsageListResponse usagesList(subscriptionId, regionId, apiVersion, $filter)

Implements Usages List method

Returns list of usage in region

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityUsagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AvailabilityUsagesApi apiInstance = new AvailabilityUsagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the list operation. only name.value is allowed here as a filter e.g. $filter=name.value eq 'xxxx'
    try {
      UsageListResponse result = apiInstance.usagesList(subscriptionId, regionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityUsagesApi#usagesList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **apiVersion** | **String**| Client API version. | |
| **$filter** | **String**| The filter to apply on the list operation. only name.value is allowed here as a filter e.g. $filter&#x3D;name.value eq &#39;xxxx&#39; | [optional] |

### Return type

[**UsageListResponse**](UsageListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

