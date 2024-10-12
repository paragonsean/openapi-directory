# EavAttributeSetsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eavAttributeSetManagementV1CreatePost**](EavAttributeSetsApi.md#eavAttributeSetManagementV1CreatePost) | **POST** /V1/eav/attribute-sets | eav/attribute-sets |


<a id="eavAttributeSetManagementV1CreatePost"></a>
# **eavAttributeSetManagementV1CreatePost**
> EavDataAttributeSetInterface eavAttributeSetManagementV1CreatePost(eavAttributeSetManagementV1CreatePostRequest)

eav/attribute-sets

Create attribute set from data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EavAttributeSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    EavAttributeSetsApi apiInstance = new EavAttributeSetsApi(defaultClient);
    EavAttributeSetManagementV1CreatePostRequest eavAttributeSetManagementV1CreatePostRequest = new EavAttributeSetManagementV1CreatePostRequest(); // EavAttributeSetManagementV1CreatePostRequest | 
    try {
      EavDataAttributeSetInterface result = apiInstance.eavAttributeSetManagementV1CreatePost(eavAttributeSetManagementV1CreatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EavAttributeSetsApi#eavAttributeSetManagementV1CreatePost");
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
| **eavAttributeSetManagementV1CreatePostRequest** | [**EavAttributeSetManagementV1CreatePostRequest**](EavAttributeSetManagementV1CreatePostRequest.md)|  | [optional] |

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

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

