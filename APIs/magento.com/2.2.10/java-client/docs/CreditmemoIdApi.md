# CreditmemoIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesCreditmemoManagementV1CancelPut**](CreditmemoIdApi.md#salesCreditmemoManagementV1CancelPut) | **PUT** /V1/creditmemo/{id} | creditmemo/{id} |
| [**salesCreditmemoRepositoryV1GetGet**](CreditmemoIdApi.md#salesCreditmemoRepositoryV1GetGet) | **GET** /V1/creditmemo/{id} | creditmemo/{id} |


<a id="salesCreditmemoManagementV1CancelPut"></a>
# **salesCreditmemoManagementV1CancelPut**
> Boolean salesCreditmemoManagementV1CancelPut(id)

creditmemo/{id}

Cancels a specified credit memo.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditmemoIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CreditmemoIdApi apiInstance = new CreditmemoIdApi(defaultClient);
    Integer id = 56; // Integer | The credit memo ID.
    try {
      Boolean result = apiInstance.salesCreditmemoManagementV1CancelPut(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditmemoIdApi#salesCreditmemoManagementV1CancelPut");
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
| **id** | **Integer**| The credit memo ID. | |

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
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="salesCreditmemoRepositoryV1GetGet"></a>
# **salesCreditmemoRepositoryV1GetGet**
> SalesDataCreditmemoInterface salesCreditmemoRepositoryV1GetGet(id)

creditmemo/{id}

Loads a specified credit memo.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditmemoIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CreditmemoIdApi apiInstance = new CreditmemoIdApi(defaultClient);
    Integer id = 56; // Integer | The credit memo ID.
    try {
      SalesDataCreditmemoInterface result = apiInstance.salesCreditmemoRepositoryV1GetGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditmemoIdApi#salesCreditmemoRepositoryV1GetGet");
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
| **id** | **Integer**| The credit memo ID. | |

### Return type

[**SalesDataCreditmemoInterface**](SalesDataCreditmemoInterface.md)

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
| **0** | Unexpected error |  -  |

