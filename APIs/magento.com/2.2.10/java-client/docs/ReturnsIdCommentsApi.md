# ReturnsIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmaCommentManagementV1AddCommentPost**](ReturnsIdCommentsApi.md#rmaCommentManagementV1AddCommentPost) | **POST** /V1/returns/{id}/comments | returns/{id}/comments |
| [**rmaCommentManagementV1CommentsListGet**](ReturnsIdCommentsApi.md#rmaCommentManagementV1CommentsListGet) | **GET** /V1/returns/{id}/comments | returns/{id}/comments |


<a id="rmaCommentManagementV1AddCommentPost"></a>
# **rmaCommentManagementV1AddCommentPost**
> Boolean rmaCommentManagementV1AddCommentPost(id, rmaCommentManagementV1AddCommentPostRequest)

returns/{id}/comments

Add comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsIdCommentsApi apiInstance = new ReturnsIdCommentsApi(defaultClient);
    String id = "id_example"; // String | 
    RmaCommentManagementV1AddCommentPostRequest rmaCommentManagementV1AddCommentPostRequest = new RmaCommentManagementV1AddCommentPostRequest(); // RmaCommentManagementV1AddCommentPostRequest | 
    try {
      Boolean result = apiInstance.rmaCommentManagementV1AddCommentPost(id, rmaCommentManagementV1AddCommentPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsIdCommentsApi#rmaCommentManagementV1AddCommentPost");
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
| **rmaCommentManagementV1AddCommentPostRequest** | [**RmaCommentManagementV1AddCommentPostRequest**](RmaCommentManagementV1AddCommentPostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="rmaCommentManagementV1CommentsListGet"></a>
# **rmaCommentManagementV1CommentsListGet**
> RmaDataCommentSearchResultInterface rmaCommentManagementV1CommentsListGet(id)

returns/{id}/comments

Comments list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsIdCommentsApi apiInstance = new ReturnsIdCommentsApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      RmaDataCommentSearchResultInterface result = apiInstance.rmaCommentManagementV1CommentsListGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsIdCommentsApi#rmaCommentManagementV1CommentsListGet");
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

[**RmaDataCommentSearchResultInterface**](RmaDataCommentSearchResultInterface.md)

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

