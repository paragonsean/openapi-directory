# SupersimV1NetworkApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchNetwork**](SupersimV1NetworkApi.md#fetchNetwork) | **GET** /v1/Networks/{Sid} |  |
| [**listNetwork**](SupersimV1NetworkApi.md#listNetwork) | **GET** /v1/Networks |  |


<a id="fetchNetwork"></a>
# **fetchNetwork**
> SupersimV1Network fetchNetwork(sid)



Fetch a Network resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkApi apiInstance = new SupersimV1NetworkApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Network resource to fetch.
    try {
      SupersimV1Network result = apiInstance.fetchNetwork(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkApi#fetchNetwork");
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
| **sid** | **String**| The SID of the Network resource to fetch. | |

### Return type

[**SupersimV1Network**](SupersimV1Network.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listNetwork"></a>
# **listNetwork**
> ListNetworkResponse listNetwork(isoCountry, mcc, mnc, pageSize, page, pageToken)



Retrieve a list of Network resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkApi apiInstance = new SupersimV1NetworkApi(defaultClient);
    String isoCountry = "isoCountry_example"; // String | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
    String mcc = "mcc_example"; // String | The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
    String mnc = "mnc_example"; // String | The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListNetworkResponse result = apiInstance.listNetwork(isoCountry, mcc, mnc, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkApi#listNetwork");
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
| **isoCountry** | **String**| The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read. | [optional] |
| **mcc** | **String**| The &#39;mobile country code&#39; of a country. Network resources with this &#x60;mcc&#x60; in their &#x60;identifiers&#x60; will be read. | [optional] |
| **mnc** | **String**| The &#39;mobile network code&#39; of a mobile operator network. Network resources with this &#x60;mnc&#x60; in their &#x60;identifiers&#x60; will be read. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListNetworkResponse**](ListNetworkResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

