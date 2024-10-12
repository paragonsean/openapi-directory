# CustomersMeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerCustomerRepositoryV1GetByIdGet**](CustomersMeApi.md#customerCustomerRepositoryV1GetByIdGet) | **GET** /V1/customers/me | customers/me |
| [**customerCustomerRepositoryV1SavePut**](CustomersMeApi.md#customerCustomerRepositoryV1SavePut) | **PUT** /V1/customers/me | customers/me |


<a id="customerCustomerRepositoryV1GetByIdGet"></a>
# **customerCustomerRepositoryV1GetByIdGet**
> CustomerDataCustomerInterface customerCustomerRepositoryV1GetByIdGet()

customers/me

Get customer by Customer ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersMeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersMeApi apiInstance = new CustomersMeApi(defaultClient);
    try {
      CustomerDataCustomerInterface result = apiInstance.customerCustomerRepositoryV1GetByIdGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersMeApi#customerCustomerRepositoryV1GetByIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

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

<a id="customerCustomerRepositoryV1SavePut"></a>
# **customerCustomerRepositoryV1SavePut**
> CustomerDataCustomerInterface customerCustomerRepositoryV1SavePut(customerCustomerRepositoryV1SavePutRequest)

customers/me

Create or update a customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersMeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersMeApi apiInstance = new CustomersMeApi(defaultClient);
    CustomerCustomerRepositoryV1SavePutRequest customerCustomerRepositoryV1SavePutRequest = new CustomerCustomerRepositoryV1SavePutRequest(); // CustomerCustomerRepositoryV1SavePutRequest | 
    try {
      CustomerDataCustomerInterface result = apiInstance.customerCustomerRepositoryV1SavePut(customerCustomerRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersMeApi#customerCustomerRepositoryV1SavePut");
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
| **customerCustomerRepositoryV1SavePutRequest** | [**CustomerCustomerRepositoryV1SavePutRequest**](CustomerCustomerRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

