# CustomersAddressesAddressIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAddressRepositoryV1GetByIdGet**](CustomersAddressesAddressIdApi.md#customerAddressRepositoryV1GetByIdGet) | **GET** /V1/customers/addresses/{addressId} | customers/addresses/{addressId} |


<a id="customerAddressRepositoryV1GetByIdGet"></a>
# **customerAddressRepositoryV1GetByIdGet**
> CustomerDataAddressInterface customerAddressRepositoryV1GetByIdGet(addressId)

customers/addresses/{addressId}

Retrieve customer address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersAddressesAddressIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersAddressesAddressIdApi apiInstance = new CustomersAddressesAddressIdApi(defaultClient);
    Integer addressId = 56; // Integer | 
    try {
      CustomerDataAddressInterface result = apiInstance.customerAddressRepositoryV1GetByIdGet(addressId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersAddressesAddressIdApi#customerAddressRepositoryV1GetByIdGet");
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

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

