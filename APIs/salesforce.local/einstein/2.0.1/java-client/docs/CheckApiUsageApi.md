# CheckApiUsageApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getApiUsagePlansV2**](CheckApiUsageApi.md#getApiUsagePlansV2) | **GET** /v2/apiusage | Get API Isage |


<a id="getApiUsagePlansV2"></a>
# **getApiUsagePlansV2**
> ApiUsageList getApiUsagePlansV2()

Get API Isage

Returns prediction usage on a monthly basis for the current calendar month and future months. Each apiusage object in the response corresponds to a calendar month in your plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckApiUsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    CheckApiUsageApi apiInstance = new CheckApiUsageApi(defaultClient);
    try {
      ApiUsageList result = apiInstance.getApiUsagePlansV2();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckApiUsageApi#getApiUsagePlansV2");
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

[**ApiUsageList**](ApiUsageList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | api usage |  -  |

