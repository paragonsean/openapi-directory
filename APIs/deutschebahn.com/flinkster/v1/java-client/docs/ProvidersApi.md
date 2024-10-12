# ProvidersApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProvider**](ProvidersApi.md#getProvider) | **GET** /providers/{uid} | Get information about the ProviderResourceImpl. |


<a id="getProvider"></a>
# **getProvider**
> RentalObjectJO getProvider(uid)

Get information about the ProviderResourceImpl.

Get information about the ProviderResourcesCtrl. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/flinkster-api-ng/v1");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    String uid = "uid_example"; // String | 
    try {
      RentalObjectJO result = apiInstance.getProvider(uid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#getProvider");
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

