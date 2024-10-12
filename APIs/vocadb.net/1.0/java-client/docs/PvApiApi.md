# PvApiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPvsForSongsGet**](PvApiApi.md#apiPvsForSongsGet) | **GET** /api/pvs/for-songs |  |


<a id="apiPvsForSongsGet"></a>
# **apiPvsForSongsGet**
> PVForSongContractPartialFindResult apiPvsForSongsGet(name, author, service, maxResults, getTotalCount, lang)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PvApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PvApiApi apiInstance = new PvApiApi(defaultClient);
    String name = "name_example"; // String | 
    String author = "author_example"; // String | 
    PVService service = PVService.fromValue("NicoNicoDouga"); // PVService | 
    Integer maxResults = 10; // Integer | 
    Boolean getTotalCount = false; // Boolean | 
    ContentLanguagePreference lang = ContentLanguagePreference.fromValue("Default"); // ContentLanguagePreference | 
    try {
      PVForSongContractPartialFindResult result = apiInstance.apiPvsForSongsGet(name, author, service, maxResults, getTotalCount, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PvApiApi#apiPvsForSongsGet");
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
| **name** | **String**|  | [optional] |
| **author** | **String**|  | [optional] |
| **service** | [**PVService**](.md)|  | [optional] [enum: NicoNicoDouga, Youtube, SoundCloud, Vimeo, Piapro, Bilibili, File, LocalFile, Creofuga, Bandcamp] |
| **maxResults** | **Integer**|  | [optional] [default to 10] |
| **getTotalCount** | **Boolean**|  | [optional] [default to false] |
| **lang** | [**ContentLanguagePreference**](.md)|  | [optional] [enum: Default, Japanese, Romaji, English] |

### Return type

[**PVForSongContractPartialFindResult**](PVForSongContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

