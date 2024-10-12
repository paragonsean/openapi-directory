# ContentApi

All URIs are relative to *http://www.bclaws.ca/civix*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentAspectIdCivixDocumentIdGet**](ContentApi.md#contentAspectIdCivixDocumentIdGet) | **GET** /content/{aspectId}/{civixDocumentId} | Lists the metadata available for the specified index or directory from the BCLaws legislative respository |
| [**contentAspectIdGet**](ContentApi.md#contentAspectIdGet) | **GET** /content/{aspectId} | Describes the documents and directories available within a specific &#39;aspect&#39; (content group) of the BCLaws library |


<a id="contentAspectIdCivixDocumentIdGet"></a>
# **contentAspectIdCivixDocumentIdGet**
> contentAspectIdCivixDocumentIdGet(aspectId, civixDocumentId)

Lists the metadata available for the specified index or directory from the BCLaws legislative respository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.bclaws.ca/civix");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String aspectId = "complete"; // String | The identifier of the 'aspect' (content group) to search
    String civixDocumentId = "statreg"; // String | The document identification code for an index or directory
    try {
      apiInstance.contentAspectIdCivixDocumentIdGet(aspectId, civixDocumentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#contentAspectIdCivixDocumentIdGet");
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
| **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to complete] [enum: complete, corpreg, bcgaz1, bcgaz2, oic, psl, ecb, hscr, arch_oic] |
| **civixDocumentId** | **String**| The document identification code for an index or directory | [default to statreg] |

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
| **200** | List documents and directories within the aspect. |  -  |

<a id="contentAspectIdGet"></a>
# **contentAspectIdGet**
> contentAspectIdGet(aspectId)

Describes the documents and directories available within a specific &#39;aspect&#39; (content group) of the BCLaws library

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.bclaws.ca/civix");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String aspectId = "complete"; // String | The identifier of the 'aspect' (content group) to search
    try {
      apiInstance.contentAspectIdGet(aspectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#contentAspectIdGet");
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
| **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to complete] [enum: complete, corpreg, bcgaz1, bcgaz2, oic, psl, ecb, hscr, arch_oic] |

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
| **200** | List documents and directories within the aspect. |  -  |

