# ArtistInformationApi

All URIs are relative to *https://rest.bandsintown.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**artist**](ArtistInformationApi.md#artist) | **GET** /artists/{artistname} | Get artist information |


<a id="artist"></a>
# **artist**
> ArtistData artist(artistname, appId)

Get artist information

Get artist information 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtistInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.bandsintown.com");

    ArtistInformationApi apiInstance = new ArtistInformationApi(defaultClient);
    String artistname = "artistname_example"; // String | The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \" use %27C
    String appId = "appId_example"; // String | The application ID assigned to you by Bandsintown
    try {
      ArtistData result = apiInstance.artist(artistname, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtistInformationApi#artist");
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
| **artistname** | **String**| The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \&quot; use %27C | |
| **appId** | **String**| The application ID assigned to you by Bandsintown | |

### Return type

[**ArtistData**](ArtistData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 response |  -  |

