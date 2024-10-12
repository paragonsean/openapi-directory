# BaggageApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**baggageTripAndContact**](BaggageApi.md#baggageTripAndContact) | **GET** /baggage/baggagetripandcontact/{searchID} | Baggage Trip and Contact |


<a id="baggageTripAndContact"></a>
# **baggageTripAndContact**
> String baggageTripAndContact(searchID, accept)

Baggage Trip and Contact

Retrieve passenger trip, contact and baggage details. This service is only accessible for LH privileged partners

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BaggageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    BaggageApi apiInstance = new BaggageApi(defaultClient);
    String searchID = "searchID_example"; // String | Bag tag number, PNR, boarding card or FQTV ID
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    try {
      String result = apiInstance.baggageTripAndContact(searchID, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BaggageApi#baggageTripAndContact");
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
| **searchID** | **String**| Bag tag number, PNR, boarding card or FQTV ID | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |

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

