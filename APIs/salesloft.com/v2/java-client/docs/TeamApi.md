# TeamApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2TeamJsonGet**](TeamApi.md#v2TeamJsonGet) | **GET** /v2/team.json | Fetch current team |


<a id="v2TeamJsonGet"></a>
# **v2TeamJsonGet**
> Team v2TeamJsonGet()

Fetch current team

Fetches the team of the authenticated user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    TeamApi apiInstance = new TeamApi(defaultClient);
    try {
      Team result = apiInstance.v2TeamJsonGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#v2TeamJsonGet");
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

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

