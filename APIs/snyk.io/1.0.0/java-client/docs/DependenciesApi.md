# DependenciesApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAllDependencies**](DependenciesApi.md#listAllDependencies) | **POST** /org/{orgId}/dependencies | List all dependencies |


<a id="listAllDependencies"></a>
# **listAllDependencies**
> ListAllDependencies200Response listAllDependencies(orgId, sortBy, order, page, perPage, listAllDependenciesRequest)

List all dependencies



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DependenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    DependenciesApi apiInstance = new DependenciesApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
    String sortBy = "projects"; // String | The field to sort results by.
    String order = "asc"; // String | The direction to sort results by.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page of results to fetch.
    BigDecimal perPage = new BigDecimal("20"); // BigDecimal | The number of results to fetch per page (maximum is 1000).
    ListAllDependenciesRequest listAllDependenciesRequest = new ListAllDependenciesRequest(); // ListAllDependenciesRequest | 
    try {
      ListAllDependencies200Response result = apiInstance.listAllDependencies(orgId, sortBy, order, page, perPage, listAllDependenciesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DependenciesApi#listAllDependencies");
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
| **sortBy** | **String**| The field to sort results by. | [optional] [default to dependency] [enum: projects, dependency, severity, dependenciesWithIssues] |
| **order** | **String**| The direction to sort results by. | [optional] [default to asc] [enum: asc, desc] |
| **page** | **BigDecimal**| The page of results to fetch. | [optional] [default to 1] |
| **perPage** | **BigDecimal**| The number of results to fetch per page (maximum is 1000). | [optional] [default to 20] |
| **listAllDependenciesRequest** | [**ListAllDependenciesRequest**](ListAllDependenciesRequest.md)|  | [optional] |

### Return type

[**ListAllDependencies200Response**](ListAllDependencies200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Link -  <br>  |

