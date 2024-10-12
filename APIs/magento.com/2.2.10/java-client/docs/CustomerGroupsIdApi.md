# CustomerGroupsIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerGroupRepositoryV1DeleteByIdDelete**](CustomerGroupsIdApi.md#customerGroupRepositoryV1DeleteByIdDelete) | **DELETE** /V1/customerGroups/{id} | customerGroups/{id} |
| [**customerGroupRepositoryV1GetByIdGet**](CustomerGroupsIdApi.md#customerGroupRepositoryV1GetByIdGet) | **GET** /V1/customerGroups/{id} | customerGroups/{id} |
| [**customerGroupRepositoryV1SavePut**](CustomerGroupsIdApi.md#customerGroupRepositoryV1SavePut) | **PUT** /V1/customerGroups/{id} | customerGroups/{id} |


<a id="customerGroupRepositoryV1DeleteByIdDelete"></a>
# **customerGroupRepositoryV1DeleteByIdDelete**
> Boolean customerGroupRepositoryV1DeleteByIdDelete(id)

customerGroups/{id}

Delete customer group by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomerGroupsIdApi apiInstance = new CustomerGroupsIdApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      Boolean result = apiInstance.customerGroupRepositoryV1DeleteByIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsIdApi#customerGroupRepositoryV1DeleteByIdDelete");
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
| **id** | **Integer**|  | |

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

<a id="customerGroupRepositoryV1GetByIdGet"></a>
# **customerGroupRepositoryV1GetByIdGet**
> CustomerDataGroupInterface customerGroupRepositoryV1GetByIdGet(id)

customerGroups/{id}

Get customer group by group ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomerGroupsIdApi apiInstance = new CustomerGroupsIdApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      CustomerDataGroupInterface result = apiInstance.customerGroupRepositoryV1GetByIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsIdApi#customerGroupRepositoryV1GetByIdGet");
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
| **id** | **Integer**|  | |

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

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

<a id="customerGroupRepositoryV1SavePut"></a>
# **customerGroupRepositoryV1SavePut**
> CustomerDataGroupInterface customerGroupRepositoryV1SavePut(id, customerGroupRepositoryV1SavePostRequest)

customerGroups/{id}

Save customer group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomerGroupsIdApi apiInstance = new CustomerGroupsIdApi(defaultClient);
    String id = "id_example"; // String | 
    CustomerGroupRepositoryV1SavePostRequest customerGroupRepositoryV1SavePostRequest = new CustomerGroupRepositoryV1SavePostRequest(); // CustomerGroupRepositoryV1SavePostRequest | 
    try {
      CustomerDataGroupInterface result = apiInstance.customerGroupRepositoryV1SavePut(id, customerGroupRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsIdApi#customerGroupRepositoryV1SavePut");
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
| **id** | **String**|  | |
| **customerGroupRepositoryV1SavePostRequest** | [**CustomerGroupRepositoryV1SavePostRequest**](CustomerGroupRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

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

