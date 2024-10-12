# CreditmemoIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesCreditmemoCommentRepositoryV1SavePost**](CreditmemoIdCommentsApi.md#salesCreditmemoCommentRepositoryV1SavePost) | **POST** /V1/creditmemo/{id}/comments | creditmemo/{id}/comments |
| [**salesCreditmemoManagementV1GetCommentsListGet**](CreditmemoIdCommentsApi.md#salesCreditmemoManagementV1GetCommentsListGet) | **GET** /V1/creditmemo/{id}/comments | creditmemo/{id}/comments |


<a id="salesCreditmemoCommentRepositoryV1SavePost"></a>
# **salesCreditmemoCommentRepositoryV1SavePost**
> SalesDataCreditmemoCommentInterface salesCreditmemoCommentRepositoryV1SavePost(id, salesCreditmemoCommentRepositoryV1SavePostRequest)

creditmemo/{id}/comments

Performs persist operations for a specified entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditmemoIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CreditmemoIdCommentsApi apiInstance = new CreditmemoIdCommentsApi(defaultClient);
    String id = "id_example"; // String | 
    SalesCreditmemoCommentRepositoryV1SavePostRequest salesCreditmemoCommentRepositoryV1SavePostRequest = new SalesCreditmemoCommentRepositoryV1SavePostRequest(); // SalesCreditmemoCommentRepositoryV1SavePostRequest | 
    try {
      SalesDataCreditmemoCommentInterface result = apiInstance.salesCreditmemoCommentRepositoryV1SavePost(id, salesCreditmemoCommentRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditmemoIdCommentsApi#salesCreditmemoCommentRepositoryV1SavePost");
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
| **salesCreditmemoCommentRepositoryV1SavePostRequest** | [**SalesCreditmemoCommentRepositoryV1SavePostRequest**](SalesCreditmemoCommentRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesDataCreditmemoCommentInterface**](SalesDataCreditmemoCommentInterface.md)

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
| **0** | Unexpected error |  -  |

<a id="salesCreditmemoManagementV1GetCommentsListGet"></a>
# **salesCreditmemoManagementV1GetCommentsListGet**
> SalesDataCreditmemoCommentSearchResultInterface salesCreditmemoManagementV1GetCommentsListGet(id)

creditmemo/{id}/comments

Lists comments for a specified credit memo.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditmemoIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CreditmemoIdCommentsApi apiInstance = new CreditmemoIdCommentsApi(defaultClient);
    Integer id = 56; // Integer | The credit memo ID.
    try {
      SalesDataCreditmemoCommentSearchResultInterface result = apiInstance.salesCreditmemoManagementV1GetCommentsListGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditmemoIdCommentsApi#salesCreditmemoManagementV1GetCommentsListGet");
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

[**SalesDataCreditmemoCommentSearchResultInterface**](SalesDataCreditmemoCommentSearchResultInterface.md)

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

