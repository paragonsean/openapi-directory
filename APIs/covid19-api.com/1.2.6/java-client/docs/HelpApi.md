# HelpApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getListOfCountries**](HelpApi.md#getListOfCountries) | **GET** /help/countries | getListOfCountries |


<a id="getListOfCountries"></a>
# **getListOfCountries**
> List&lt;GetListOfCountries200ResponseInner&gt; getListOfCountries(format)

getListOfCountries

Get name name, alpha-2, alpha-3 code, latitude and longitude for every country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HelpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HelpApi apiInstance = new HelpApi(defaultClient);
    String format = "json"; // String | Format of the response
    try {
      List<GetListOfCountries200ResponseInner> result = apiInstance.getListOfCountries(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HelpApi#getListOfCountries");
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
| **format** | **String**| Format of the response | [optional] [default to json] [enum: json, xml] |

### Return type

[**List&lt;GetListOfCountries200ResponseInner&gt;**](GetListOfCountries200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get name name, alpha-2, alpha-3 code, latitude and longitude for every country |  -  |

