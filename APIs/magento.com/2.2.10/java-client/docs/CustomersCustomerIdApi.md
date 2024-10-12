# CustomersCustomerIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerCustomerRepositoryV1DeleteByIdDelete**](CustomersCustomerIdApi.md#customerCustomerRepositoryV1DeleteByIdDelete) | **DELETE** /V1/customers/{customerId} | customers/{customerId} |
| [**v1CustomersCustomerIdGet**](CustomersCustomerIdApi.md#v1CustomersCustomerIdGet) | **GET** /V1/customers/{customerId} | customers/{customerId} |
| [**v1CustomersCustomerIdPut**](CustomersCustomerIdApi.md#v1CustomersCustomerIdPut) | **PUT** /V1/customers/{customerId} | customers/{customerId} |


<a id="customerCustomerRepositoryV1DeleteByIdDelete"></a>
# **customerCustomerRepositoryV1DeleteByIdDelete**
> Boolean customerCustomerRepositoryV1DeleteByIdDelete(customerId)

customers/{customerId}

Delete customer by Customer ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersCustomerIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersCustomerIdApi apiInstance = new CustomersCustomerIdApi(defaultClient);
    Integer customerId = 56; // Integer | 
    try {
      Boolean result = apiInstance.customerCustomerRepositoryV1DeleteByIdDelete(customerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersCustomerIdApi#customerCustomerRepositoryV1DeleteByIdDelete");
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
| **customerId** | **Integer**|  | |

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

<a id="v1CustomersCustomerIdGet"></a>
# **v1CustomersCustomerIdGet**
> CustomerDataCustomerInterface v1CustomersCustomerIdGet(customerId)

customers/{customerId}

Get customer by Customer ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersCustomerIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersCustomerIdApi apiInstance = new CustomersCustomerIdApi(defaultClient);
    Integer customerId = 56; // Integer | 
    try {
      CustomerDataCustomerInterface result = apiInstance.v1CustomersCustomerIdGet(customerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersCustomerIdApi#v1CustomersCustomerIdGet");
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
| **customerId** | **Integer**|  | |

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

<a id="v1CustomersCustomerIdPut"></a>
# **v1CustomersCustomerIdPut**
> CustomerDataCustomerInterface v1CustomersCustomerIdPut(customerId, customerCustomerRepositoryV1SavePutRequest)

customers/{customerId}

Create or update a customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersCustomerIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersCustomerIdApi apiInstance = new CustomersCustomerIdApi(defaultClient);
    String customerId = "customerId_example"; // String | 
    CustomerCustomerRepositoryV1SavePutRequest customerCustomerRepositoryV1SavePutRequest = new CustomerCustomerRepositoryV1SavePutRequest(); // CustomerCustomerRepositoryV1SavePutRequest | 
    try {
      CustomerDataCustomerInterface result = apiInstance.v1CustomersCustomerIdPut(customerId, customerCustomerRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersCustomerIdApi#v1CustomersCustomerIdPut");
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
| **customerId** | **String**|  | |
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

