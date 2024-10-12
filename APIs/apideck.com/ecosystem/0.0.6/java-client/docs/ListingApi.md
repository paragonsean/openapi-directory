# ListingApi

All URIs are relative to *https://api.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listingsAll**](ListingApi.md#listingsAll) | **GET** /ecosystems/{ecosystem_id}/listings | List listings |
| [**listingsOne**](ListingApi.md#listingsOne) | **GET** /ecosystems/{ecosystem_id}/listings/{id} | Get listing |


<a id="listingsAll"></a>
# **listingsAll**
> GetListingsResponse listingsAll(ecosystemId, cursor, limit, externalId)

List listings

List listings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    ListingApi apiInstance = new ListingApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 50; // Integer | Number of records to return
    String externalId = "externalId_example"; // String | Filter on external_id
    try {
      GetListingsResponse result = apiInstance.listingsAll(ecosystemId, cursor, limit, externalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingApi#listingsAll");
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
| **ecosystemId** | **String**|  | |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **limit** | **Integer**| Number of records to return | [optional] [default to 50] |
| **externalId** | **String**| Filter on external_id | [optional] |

### Return type

[**GetListingsResponse**](GetListingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listings |  -  |

<a id="listingsOne"></a>
# **listingsOne**
> GetListingResponse listingsOne(ecosystemId, id)

Get listing

Get listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    ListingApi apiInstance = new ListingApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String id = "id_example"; // String | ID of the record you are acting upon.
    try {
      GetListingResponse result = apiInstance.listingsOne(ecosystemId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingApi#listingsOne");
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
| **ecosystemId** | **String**|  | |
| **id** | **String**| ID of the record you are acting upon. | |

### Return type

[**GetListingResponse**](GetListingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listing |  -  |

