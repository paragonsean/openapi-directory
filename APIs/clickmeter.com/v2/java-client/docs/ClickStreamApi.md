# ClickStreamApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clickStreamGet**](ClickStreamApi.md#clickStreamGet) | **GET** /clickstream | Retrieve the latest list of events of this account. Limited to last 100. |


<a id="clickStreamGet"></a>
# **clickStreamGet**
> ApiCoreResponsesEntitiesResponseApiCoreDtoClickStreamHit clickStreamGet(group, datapoint, conversion, pageSize, filter)

Retrieve the latest list of events of this account. Limited to last 100.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClickStreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClickStreamApi apiInstance = new ClickStreamApi(defaultClient);
    Long group = 56L; // Long | Filter by this group id (mutually exclusive with \"datapoint\" and \"conversion\")
    Long datapoint = 56L; // Long | Filter by this datapoint id (mutually exclusive with \"group\" and \"conversion\")
    Long conversion = 56L; // Long | Filter by this conversion id (mutually exclusive with \"datapoint\" and \"group\")
    Integer pageSize = 50; // Integer | Limit results to this number
    String filter = ""; // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoClickStreamHit result = apiInstance.clickStreamGet(group, datapoint, conversion, pageSize, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClickStreamApi#clickStreamGet");
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
| **group** | **Long**| Filter by this group id (mutually exclusive with \&quot;datapoint\&quot; and \&quot;conversion\&quot;) | [optional] |
| **datapoint** | **Long**| Filter by this datapoint id (mutually exclusive with \&quot;group\&quot; and \&quot;conversion\&quot;) | [optional] |
| **conversion** | **Long**| Filter by this conversion id (mutually exclusive with \&quot;datapoint\&quot; and \&quot;group\&quot;) | [optional] |
| **pageSize** | **Integer**| Limit results to this number | [optional] [default to 50] |
| **filter** | **String**| Filter event type (\&quot;spiders\&quot;/\&quot;uniques\&quot;/\&quot;nonuniques\&quot;/\&quot;conversions\&quot;) | [optional] [enum: , spiders, uniques, nonuniques, conversions] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoClickStreamHit**](ApiCoreResponsesEntitiesResponseApiCoreDtoClickStreamHit.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

