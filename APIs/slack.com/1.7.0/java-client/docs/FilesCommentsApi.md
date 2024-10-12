# FilesCommentsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filesCommentsDelete**](FilesCommentsApi.md#filesCommentsDelete) | **POST** /files.comments.delete |  |


<a id="filesCommentsDelete"></a>
# **filesCommentsDelete**
> FilesCommentsDeleteSchema filesCommentsDelete(token, _file, id)



Deletes an existing comment on a file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    FilesCommentsApi apiInstance = new FilesCommentsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `files:write:user`
    String _file = "_file_example"; // String | File to delete a comment from.
    String id = "id_example"; // String | The comment to delete.
    try {
      FilesCommentsDeleteSchema result = apiInstance.filesCommentsDelete(token, _file, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesCommentsApi#filesCommentsDelete");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] |
| **_file** | **String**| File to delete a comment from. | [optional] |
| **id** | **String**| The comment to delete. | [optional] |

### Return type

[**FilesCommentsDeleteSchema**](FilesCommentsDeleteSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standard success response is very simple |  -  |
| **0** | Standard failure response when used with an invalid token |  -  |

