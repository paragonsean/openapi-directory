# AddressesAddressIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAddressRepositoryV1DeleteByIdDelete**](AddressesAddressIdApi.md#customerAddressRepositoryV1DeleteByIdDelete) | **DELETE** /V1/addresses/{addressId} | addresses/{addressId} |


<a id="customerAddressRepositoryV1DeleteByIdDelete"></a>
# **customerAddressRepositoryV1DeleteByIdDelete**
> Boolean customerAddressRepositoryV1DeleteByIdDelete(addressId)

addresses/{addressId}

Delete customer address by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesAddressIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    AddressesAddressIdApi apiInstance = new AddressesAddressIdApi(defaultClient);
    Integer addressId = 56; // Integer | 
    try {
      Boolean result = apiInstance.customerAddressRepositoryV1DeleteByIdDelete(addressId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesAddressIdApi#customerAddressRepositoryV1DeleteByIdDelete");
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
| **addressId** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

