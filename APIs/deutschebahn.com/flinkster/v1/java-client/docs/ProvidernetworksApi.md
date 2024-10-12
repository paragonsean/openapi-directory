# ProvidernetworksApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProviderNetwork**](ProvidernetworksApi.md#getProviderNetwork) | **GET** /providernetworks/{uid} | Get information about the ProviderNetworkResources. |


<a id="getProviderNetwork"></a>
# **getProviderNetwork**
> RentalObjectJO getProviderNetwork(uid)

Get information about the ProviderNetworkResources.

Get information about the ProviderNetworkResources. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidernetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/flinkster-api-ng/v1");

    ProvidernetworksApi apiInstance = new ProvidernetworksApi(defaultClient);
    String uid = "uid_example"; // String | 
    try {
      RentalObjectJO result = apiInstance.getProviderNetwork(uid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidernetworksApi#getProviderNetwork");
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
| **uid** | **String**|  | |

### Return type

[**RentalObjectJO**](RentalObjectJO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request One or more parameters have invalid values. |  -  |
| **403** | Forbidden Provider is not allowed to use this interface. |  -  |

