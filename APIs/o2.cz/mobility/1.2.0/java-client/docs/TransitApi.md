# TransitApi

All URIs are relative to *https://developer.o2.cz/mobility/sandbox/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transit**](TransitApi.md#transit) | **GET** /transit/{from}/{to} | Transit between basic residential units |


<a id="transit"></a>
# **transit**
> CountResult transit(from, to, uniques, fromType, toType)

Transit between basic residential units

Get count of objects that were moving between basic residential units or objects that were visiting these basic residential units. Specific object&#39;s occurence type in the base residential unit can be requested. If none occurence type is present in the request or both occurence types are zero, the result will be aggregation of all types of occurence for given base residential units. More about base residential units can be found at https://www.czso.cz/csu/rso/zsj_rso (czech).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.o2.cz/mobility/sandbox/api");

    TransitApi apiInstance = new TransitApi(defaultClient);
    String from = "127752"; // String | source basic residential unit
    String to = "127761"; // String | destination basic residential unit
    String uniques = "0"; // String | all or only uniques (0 - all, 1 - uniques)
    String fromType = "fromType_example"; // String | occurence type in the source basic residential unit (1 - transit, 2 - visit, 0 - both)
    String toType = "toType_example"; // String | occurence type in the destination basic residential unit (1 - transit, 2 - visit, 0 - both)
    try {
      CountResult result = apiInstance.transit(from, to, uniques, fromType, toType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransitApi#transit");
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
| **from** | **String**| source basic residential unit | |
| **to** | **String**| destination basic residential unit | |
| **uniques** | **String**| all or only uniques (0 - all, 1 - uniques) | |
| **fromType** | **String**| occurence type in the source basic residential unit (1 - transit, 2 - visit, 0 - both) | [optional] |
| **toType** | **String**| occurence type in the destination basic residential unit (1 - transit, 2 - visit, 0 - both) | [optional] |

### Return type

[**CountResult**](CountResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response with the requested content. |  -  |
| **204** | The request is valid, but the platform is not able to serve the data. The reason may be restriction (e.g. differential privacy) or no data were found. |  -  |
| **400** | Invalid request provided, missing or invalid parameter. |  -  |
| **500** | Internal server error. |  -  |

