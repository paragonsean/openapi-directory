# OrganizationsApi

All URIs are relative to *https://api.configcat.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizations**](OrganizationsApi.md#getOrganizations) | **GET** /v1/organizations | List Organizations |


<a id="getOrganizations"></a>
# **getOrganizations**
> List&lt;OrganizationModelHaljson&gt; getOrganizations()

List Organizations

This endpoint returns the list of the Organizations that belongs to the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    try {
      List<OrganizationModelHaljson> result = apiInstance.getOrganizations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#getOrganizations");
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

[**List&lt;OrganizationModelHaljson&gt;**](OrganizationModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

