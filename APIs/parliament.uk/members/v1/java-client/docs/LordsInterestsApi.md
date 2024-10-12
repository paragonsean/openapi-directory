# LordsInterestsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiLordsInterestsRegisterGet**](LordsInterestsApi.md#apiLordsInterestsRegisterGet) | **GET** /api/LordsInterests/Register | Returns a list of registered interests |
| [**apiLordsInterestsStaffGet**](LordsInterestsApi.md#apiLordsInterestsStaffGet) | **GET** /api/LordsInterests/Staff | Returns a list of staff |


<a id="apiLordsInterestsRegisterGet"></a>
# **apiLordsInterestsRegisterGet**
> MembersInterestsMembersServiceSearchResult apiLordsInterestsRegisterGet(searchTerm, page, includeDeleted)

Returns a list of registered interests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LordsInterestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LordsInterestsApi apiInstance = new LordsInterestsApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | Registered interests containing search term
    Integer page = 56; // Integer | Page of results to return, default 0. Results per page 20.
    Boolean includeDeleted = false; // Boolean | Registered interests that have been deleted
    try {
      MembersInterestsMembersServiceSearchResult result = apiInstance.apiLordsInterestsRegisterGet(searchTerm, page, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LordsInterestsApi#apiLordsInterestsRegisterGet");
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
| **searchTerm** | **String**| Registered interests containing search term | [optional] |
| **page** | **Integer**| Page of results to return, default 0. Results per page 20. | [optional] |
| **includeDeleted** | **Boolean**| Registered interests that have been deleted | [optional] [default to false] |

### Return type

[**MembersInterestsMembersServiceSearchResult**](MembersInterestsMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="apiLordsInterestsStaffGet"></a>
# **apiLordsInterestsStaffGet**
> MembersStaffMembersServiceSearchResult apiLordsInterestsStaffGet(searchTerm, page)

Returns a list of staff

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LordsInterestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LordsInterestsApi apiInstance = new LordsInterestsApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | Staff containing search term
    Integer page = 56; // Integer | Page of results to return, default 0. Results per page 20.
    try {
      MembersStaffMembersServiceSearchResult result = apiInstance.apiLordsInterestsStaffGet(searchTerm, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LordsInterestsApi#apiLordsInterestsStaffGet");
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
| **searchTerm** | **String**| Staff containing search term | [optional] |
| **page** | **Integer**| Page of results to return, default 0. Results per page 20. | [optional] |

### Return type

[**MembersStaffMembersServiceSearchResult**](MembersStaffMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

