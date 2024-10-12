# ReferenceDataApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**seatDetails**](ReferenceDataApi.md#seatDetails) | **GET** /references/seatdetails/{aircraftCode}/{cabinCode} | Seat Details |


<a id="seatDetails"></a>
# **seatDetails**
> String seatDetails(aircraftCode, accept, cabinCode, lang)

Seat Details

A description of all available seat details by aircraft type. You can retrieve the full set or details for a particular aircraft type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataApi apiInstance = new ReferenceDataApi(defaultClient);
    String aircraftCode = "aircraftCode_example"; // String | Aircraft type. 3-character IATA equipment code
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String cabinCode = "C"; // String | Cabin class: M, E, C, F (Acceptable values are: \"\", \"M\", \"E\", \"C\", \"F\")
    String lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
    try {
      String result = apiInstance.seatDetails(aircraftCode, accept, cabinCode, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataApi#seatDetails");
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
| **aircraftCode** | **String**| Aircraft type. 3-character IATA equipment code | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **cabinCode** | **String**| Cabin class: M, E, C, F (Acceptable values are: \&quot;\&quot;, \&quot;M\&quot;, \&quot;E\&quot;, \&quot;C\&quot;, \&quot;F\&quot;) | [default to C] |
| **lang** | **String**| 2-letter ISO 3166-1 language code | [optional] |

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

