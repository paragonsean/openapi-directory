# AttachmentApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAttachment**](AttachmentApi.md#createAttachment) | **POST** /buckets/{bucket_id}/collections/{collection_id}/records/{id}/attachment |  |
| [**deleteAttachment**](AttachmentApi.md#deleteAttachment) | **DELETE** /buckets/{bucket_id}/collections/{collection_id}/records/{id}/attachment |  |


<a id="createAttachment"></a>
# **createAttachment**
> createAttachment(bucketId, collectionId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    AttachmentApi apiInstance = new AttachmentApi(defaultClient);
    String bucketId = "bucketId_example"; // String | 
    String collectionId = "collectionId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.createAttachment(bucketId, collectionId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentApi#createAttachment");
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
| **bucketId** | **String**|  | |
| **collectionId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | UNDOCUMENTED RESPONSE |  -  |

<a id="deleteAttachment"></a>
# **deleteAttachment**
> deleteAttachment(bucketId, collectionId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    AttachmentApi apiInstance = new AttachmentApi(defaultClient);
    String bucketId = "bucketId_example"; // String | 
    String collectionId = "collectionId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteAttachment(bucketId, collectionId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentApi#deleteAttachment");
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
| **bucketId** | **String**|  | |
| **collectionId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | UNDOCUMENTED RESPONSE |  -  |

