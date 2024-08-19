# LicensesApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAllLicenses**](LicensesApi.md#listAllLicenses) | **POST** /org/{orgId}/licenses | List all licenses |


<a id="listAllLicenses"></a>
# **listAllLicenses**
> ListAllLicenses200Response listAllLicenses(orgId, sortBy, order, listAllLicensesRequest)

List all licenses



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
    String sortBy = "license"; // String | The field to sort results by.
    String order = "asc"; // String | The direction to sort results by.
    ListAllLicensesRequest listAllLicensesRequest = new ListAllLicensesRequest(); // ListAllLicensesRequest | 
    try {
      ListAllLicenses200Response result = apiInstance.listAllLicenses(orgId, sortBy, order, listAllLicensesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#listAllLicenses");
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
| **orgId** | **String**| The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **sortBy** | **String**| The field to sort results by. | [optional] [default to license] [enum: license, dependencies, projects, severity] |
| **order** | **String**| The direction to sort results by. | [optional] [default to asc] [enum: asc, desc] |
| **listAllLicensesRequest** | [**ListAllLicensesRequest**](ListAllLicensesRequest.md)|  | [optional] |

### Return type

[**ListAllLicenses200Response**](ListAllLicenses200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

