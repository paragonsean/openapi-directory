# GovernmentOrganisationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganisations**](GovernmentOrganisationApi.md#getOrganisations) | **GET** /api/GovernmentOrganisation | Returns all government organisations. |


<a id="getOrganisations"></a>
# **getOrganisations**
> GovernmentOrganisationResourceCollection getOrganisations()

Returns all government organisations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GovernmentOrganisationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    GovernmentOrganisationApi apiInstance = new GovernmentOrganisationApi(defaultClient);
    try {
      GovernmentOrganisationResourceCollection result = apiInstance.getOrganisations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GovernmentOrganisationApi#getOrganisations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GovernmentOrganisationResourceCollection**](GovernmentOrganisationResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

