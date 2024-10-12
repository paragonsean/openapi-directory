# ServiceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceListAvailableSkus**](ServiceApi.md#serviceListAvailableSkus) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/availableSkus |  |
| [**serviceValidateAddress**](ServiceApi.md#serviceValidateAddress) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/validateAddress |  |


<a id="serviceListAvailableSkus"></a>
# **serviceListAvailableSkus**
> AvailableSkusResult serviceListAvailableSkus(subscriptionId, location, apiVersion, availableSkuRequest)



This method provides the list of available skus for the given subscription and location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String location = "location_example"; // String | The location of the resource
    String apiVersion = "apiVersion_example"; // String | The API Version
    AvailableSkuRequest availableSkuRequest = new AvailableSkuRequest(); // AvailableSkuRequest | Filters for showing the available skus.
    try {
      AvailableSkusResult result = apiInstance.serviceListAvailableSkus(subscriptionId, location, apiVersion, availableSkuRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#serviceListAvailableSkus");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **location** | **String**| The location of the resource | |
| **apiVersion** | **String**| The API Version | |
| **availableSkuRequest** | [**AvailableSkuRequest**](AvailableSkuRequest.md)| Filters for showing the available skus. | |

### Return type

[**AvailableSkusResult**](AvailableSkusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of available skus. |  -  |

<a id="serviceValidateAddress"></a>
# **serviceValidateAddress**
> AddressValidationOutput serviceValidateAddress(subscriptionId, location, apiVersion, validateAddress)



This method validates the customer shipping address and provide alternate addresses if any.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String location = "location_example"; // String | The location of the resource
    String apiVersion = "apiVersion_example"; // String | The API Version
    ValidateAddress validateAddress = new ValidateAddress(); // ValidateAddress | Shipping address of the customer.
    try {
      AddressValidationOutput result = apiInstance.serviceValidateAddress(subscriptionId, location, apiVersion, validateAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#serviceValidateAddress");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **location** | **String**| The location of the resource | |
| **apiVersion** | **String**| The API Version | |
| **validateAddress** | [**ValidateAddress**](ValidateAddress.md)| Shipping address of the customer. | |

### Return type

[**AddressValidationOutput**](AddressValidationOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The valid and alternate addresses. |  -  |

