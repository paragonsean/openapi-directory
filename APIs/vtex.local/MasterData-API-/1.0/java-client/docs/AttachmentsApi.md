# AttachmentsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveattachment**](AttachmentsApi.md#retrieveattachment) | **GET** /api/dataentities/{acronym}/documents/{id}/{field}/attachments/{file-name} | Retrieve attachment |
| [**saveattachment**](AttachmentsApi.md#saveattachment) | **POST** /api/dataentities/{acronym}/documents/{id}/{field}/attachments | Save attachment |


<a id="retrieveattachment"></a>
# **retrieveattachment**
> retrieveattachment(acronym, id, field, fileName)

Retrieve attachment

Use this API to retrieve a file.    Be sure to include the file extension in the name. Like in this example:  &#x60;&#x60;&#x60;  /dataentities/CL/documents/123/file/attachments/image.png  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    String field = "{{field}}"; // String | Field to attach the file to, as described in admin
    String fileName = "{{file-name}}"; // String | 
    try {
      apiInstance.retrieveattachment(acronym, id, field, fileName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#retrieveattachment");
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
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |
| **field** | **String**| Field to attach the file to, as described in admin | [default to {{field}}] |
| **fileName** | **String**|  | [default to {{file-name}}] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="saveattachment"></a>
# **saveattachment**
> saveattachment(acronym, id, field, _file)

Save attachment

This API allows you to save a file in a field of type &#x60;File&#x60;.    When using in javascript, you must add the header &#x60;content-type&#x60; with value &#x60;multipart/form-data;&#x60;    You can upload more than one file. Just add a new field in the &#x60;form-data&#x60; with type &#x60;File&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    String field = "{{field}}"; // String | Field to attach the file to, as described in admin
    List<File> _file = Arrays.asList(); // List<File> | 
    try {
      apiInstance.saveattachment(acronym, id, field, _file);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#saveattachment");
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
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |
| **field** | **String**| Field to attach the file to, as described in admin | [default to {{field}}] |
| **_file** | **List&lt;File&gt;**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

