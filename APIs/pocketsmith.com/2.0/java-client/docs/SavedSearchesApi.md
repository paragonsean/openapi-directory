# SavedSearchesApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersIdSavedSearchesGet**](SavedSearchesApi.md#usersIdSavedSearchesGet) | **GET** /users/{id}/saved_searches | List saved searches in user |


<a id="usersIdSavedSearchesGet"></a>
# **usersIdSavedSearchesGet**
> List&lt;SavedSearch&gt; usersIdSavedSearchesGet(id)

List saved searches in user

Lists saved searches belonging to a user by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedSearchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    SavedSearchesApi apiInstance = new SavedSearchesApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    try {
      List<SavedSearch> result = apiInstance.usersIdSavedSearchesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedSearchesApi#usersIdSavedSearchesGet");
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
| **id** | **Integer**| The unique identifier of the user. | |

### Return type

[**List&lt;SavedSearch&gt;**](SavedSearch.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

