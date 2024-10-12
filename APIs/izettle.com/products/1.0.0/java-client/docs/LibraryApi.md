# LibraryApi

All URIs are relative to *https://products.izettle.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLibrary**](LibraryApi.md#getLibrary) | **GET** /organizations/{organizationUuid}/library | Retrieve the entire library |


<a id="getLibrary"></a>
# **getLibrary**
> LibraryResponse getLibrary(organizationUuid, eventLogUuid, limit, offset, all)

Retrieve the entire library

Will return the entire library for the authenticated user. If size of the library exceeds server preferences (normally 500) or the value of the optional limit parameter, the result will be paginated. Paginated responses return a Link header, indicating the next URI to fetch. The resulting header value will look something like:  &lt;https://products.izettle.com/organizations/self/library?limit&#x3D;X&amp;offset&#x3D;Y&gt;; rel&#x3D;\&quot;next\&quot;  where limit is number of items in response, and offset is the current position in pagination. The rel-part in the header is the links relation to the data previously recieved. The idea is that as long as this header is present there are still items remaining to be fetched. When either the header is not present or it&#39;s value doesn&#39;t contain any \&quot;next\&quot; value, all items have been sent to the client.  Note: The client should NOT try to extract query parameters from the URI, but rather use it as-is for the next request. Also, clients should be perpared that one Link header might contain multiple other IRIs that are not \&quot;next\&quot; (there will never be more than one \&quot;next\&quot; though). See more at:      IETF: https://tools.ietf.org/html/rfc5988     GitHub: https://developer.github.com/guides/traversing-with-pagination/  If eventLogUuid is provided, the response will only include events affecting the library since that event. Such responses are normally quite small and would be a preferred method for most fat clients after retrieving the initial full library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID eventLogUuid = UUID.randomUUID(); // UUID | 
    Integer limit = 500; // Integer | 
    String offset = "offset_example"; // String | 
    Boolean all = true; // Boolean | 
    try {
      LibraryResponse result = apiInstance.getLibrary(organizationUuid, eventLogUuid, limit, offset, all);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#getLibrary");
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
| **organizationUuid** | **UUID**|  | |
| **eventLogUuid** | **UUID**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 500] |
| **offset** | **String**|  | [optional] |
| **all** | **Boolean**|  | [optional] |

### Return type

[**LibraryResponse**](LibraryResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of library items |  * Link - If the response is paginated this header will contain the URI for the next page. See more at: https://tools.ietf.org/html/rfc5988 <br>  |
| **412** | Invalid event log uuid. If the eventLogUuid query parameter was provided a 412 response indicates that the number of changes in the product exceeds the limit since that particular event (currently 500 changes).  When this happens, the client should remove the eventLogUuid query parameters and try again. |  -  |

