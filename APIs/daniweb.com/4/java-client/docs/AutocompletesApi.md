# AutocompletesApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autocompletesGet**](AutocompletesApi.md#autocompletesGet) | **GET** /autocompletes |  |


<a id="autocompletesGet"></a>
# **autocompletesGet**
> EndpointGetAutocompletes autocompletesGet(query)



Retrieve an array of names and locations, filtered by category, that begin with the query string passed in. Ideally used for search autocomplete dropdowns, as the search functionality filters against name and location. The four potential categories are: &#x60;conversations&#x60; for names of users you are in existing conversations with; &#x60;matches&#x60; for names of users you have previously skipped over; &#x60;people&#x60; for names of all other users; &#x60;locations&#x60; for locations of users. Only users and their locations who exist with the current access token&#39;s bubble are considered.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutocompletesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    AutocompletesApi apiInstance = new AutocompletesApi(defaultClient);
    String query = "query_example"; // String | 
    try {
      EndpointGetAutocompletes result = apiInstance.autocompletesGet(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutocompletesApi#autocompletesGet");
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
| **query** | **String**|  | [optional] |

### Return type

[**EndpointGetAutocompletes**](EndpointGetAutocompletes.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

