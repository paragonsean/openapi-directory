# ReturnsApi

All URIs are relative to *https://api.fulfillment.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReturns**](ReturnsApi.md#getReturns) | **GET** /returns | List Returns |
| [**putReturns**](ReturnsApi.md#putReturns) | **PUT** /returns | Inform us of an RMA |


<a id="getReturns"></a>
# **getReturns**
> ReturnsArrayV2 getReturns(fromDate, toDate, page, limit)

List Returns

Retrieves summary return activity during the queried timespan. Although return knowledge can be learned from &#x60;GET /orders/{id}&#x60; it can take an unknown amount of time for an order that is refused or undeliverable to return to an FDC facility. Instead we recommend regularly querying this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReturnsApi apiInstance = new ReturnsApi(defaultClient);
    String fromDate = "fromDate_example"; // String | Date-time in ISO 8601 format for selecting orders after, or at, the specified time
    String toDate = "toDate_example"; // String | Date-time in ISO 8601 format for selecting orders before, or at, the specified time
    Integer page = 1; // Integer | A multiplier of the number of items (limit parameter) to skip before returning results
    Integer limit = 80; // Integer | The numbers of items to return
    try {
      ReturnsArrayV2 result = apiInstance.getReturns(fromDate, toDate, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsApi#getReturns");
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
| **fromDate** | **String**| Date-time in ISO 8601 format for selecting orders after, or at, the specified time | |
| **toDate** | **String**| Date-time in ISO 8601 format for selecting orders before, or at, the specified time | |
| **page** | **Integer**| A multiplier of the number of items (limit parameter) to skip before returning results | [optional] [default to 1] |
| **limit** | **Integer**| The numbers of items to return | [optional] [default to 80] |

### Return type

[**ReturnsArrayV2**](ReturnsArrayV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns |  -  |

<a id="putReturns"></a>
# **putReturns**
> RmaResponseV2 putReturns(rmaRequestV2)

Inform us of an RMA

Inform FDC of an expected return.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReturnsApi apiInstance = new ReturnsApi(defaultClient);
    RmaRequestV2 rmaRequestV2 = new RmaRequestV2(); // RmaRequestV2 | RMA
    try {
      RmaResponseV2 result = apiInstance.putReturns(rmaRequestV2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsApi#putReturns");
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
| **rmaRequestV2** | [**RmaRequestV2**](RmaRequestV2.md)| RMA | |

### Return type

[**RmaResponseV2**](RmaResponseV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | RMA Created |  -  |
| **202** | RMA Updated |  -  |
| **404** | A Component of Your Request Was Not Found |  -  |
| **409** | RMA Already Processed |  -  |

