# ContributorApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getContributor**](ContributorApi.md#getContributor) | **GET** /contributor/{contributorId} | Contributor Detail |
| [**listContributor**](ContributorApi.md#listContributor) | **GET** /contributor | Contributor Collection |


<a id="getContributor"></a>
# **getContributor**
> Object getContributor(contributorId, aliases)

Contributor Detail

Return the content of the selected contributor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ContributorApi apiInstance = new ContributorApi(defaultClient);
    String contributorId = "contributorId_example"; // String | Filter the schedule items by contributor ID
    Boolean aliases = true; // Boolean | Flag to display Legacy and Provider Ids.
    try {
      Object result = apiInstance.getContributor(contributorId, aliases);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributorApi#getContributor");
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
| **contributorId** | **String**| Filter the schedule items by contributor ID | |
| **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listContributor"></a>
# **listContributor**
> Object listContributor(updatedAfter, limit, aliases)

Contributor Collection

Return a collection of Contributors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ContributorApi apiInstance = new ContributorApi(defaultClient);
    String updatedAfter = "2015-05-05T00:00:00.000Z"; // String | Updated After
    Integer limit = 100; // Integer | Limit the the number of items to be returned per page. For example: 5.
    Boolean aliases = true; // Boolean | Flag to display Legacy and Provider Ids.
    try {
      Object result = apiInstance.listContributor(updatedAfter, limit, aliases);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributorApi#listContributor");
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
| **updatedAfter** | **String**| Updated After | [optional] [default to 2015-05-05T00:00:00.000Z] |
| **limit** | **Integer**| Limit the the number of items to be returned per page. For example: 5. | [optional] [default to 100] |
| **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

