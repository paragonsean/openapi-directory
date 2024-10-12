# BouncesApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateBounce**](BouncesApiApi.md#activateBounce) | **PUT** /bounces/{bounceid}/activate | Activate a bounce |
| [**bouncesBounceidDumpGet**](BouncesApiApi.md#bouncesBounceidDumpGet) | **GET** /bounces/{bounceid}/dump | Get bounce dump |
| [**getBounces**](BouncesApiApi.md#getBounces) | **GET** /bounces | Get bounces |
| [**getDeliveryStats**](BouncesApiApi.md#getDeliveryStats) | **GET** /deliverystats | Get delivery stats |
| [**getSingleBounce**](BouncesApiApi.md#getSingleBounce) | **GET** /bounces/{bounceid} | Get a single bounce |


<a id="activateBounce"></a>
# **activateBounce**
> BounceActivationResponse activateBounce(xPostmarkServerToken, bounceid)

Activate a bounce

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BouncesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    BouncesApiApi apiInstance = new BouncesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Long bounceid = 56L; // Long | The ID of the Bounce to activate.
    try {
      BounceActivationResponse result = apiInstance.activateBounce(xPostmarkServerToken, bounceid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BouncesApiApi#activateBounce");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **bounceid** | **Long**| The ID of the Bounce to activate. | |

### Return type

[**BounceActivationResponse**](BounceActivationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="bouncesBounceidDumpGet"></a>
# **bouncesBounceidDumpGet**
> BounceDumpResponse bouncesBounceidDumpGet(xPostmarkServerToken, bounceid)

Get bounce dump

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BouncesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    BouncesApiApi apiInstance = new BouncesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Long bounceid = 56L; // Long | The ID for the bounce dump to retrieve.
    try {
      BounceDumpResponse result = apiInstance.bouncesBounceidDumpGet(xPostmarkServerToken, bounceid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BouncesApiApi#bouncesBounceidDumpGet");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **bounceid** | **Long**| The ID for the bounce dump to retrieve. | |

### Return type

[**BounceDumpResponse**](BounceDumpResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getBounces"></a>
# **getBounces**
> BounceSearchResponse getBounces(xPostmarkServerToken, count, offset, type, inactive, emailFilter, messageID, tag, todate, fromdate)

Get bounces

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BouncesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    BouncesApiApi apiInstance = new BouncesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Integer count = 56; // Integer | Number of bounces to return per request. Max 500.
    Integer offset = 56; // Integer | Number of bounces to skip.
    String type = "HardBounce"; // String | Filter by type of bounce
    Boolean inactive = true; // Boolean | Filter by emails that were deactivated by Postmark due to the bounce. Set to true or false. If this isn't specified it will return both active and inactive.
    String emailFilter = "emailFilter_example"; // String | Filter by email address
    String messageID = "messageID_example"; // String | Filter by messageID
    String tag = "tag_example"; // String | Filter by tag
    LocalDate todate = LocalDate.now(); // LocalDate | Filter messages up to the date specified. e.g. `2014-02-01`
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter messages starting from the date specified. e.g. `2014-02-01`
    try {
      BounceSearchResponse result = apiInstance.getBounces(xPostmarkServerToken, count, offset, type, inactive, emailFilter, messageID, tag, todate, fromdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BouncesApiApi#getBounces");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **count** | **Integer**| Number of bounces to return per request. Max 500. | |
| **offset** | **Integer**| Number of bounces to skip. | |
| **type** | **String**| Filter by type of bounce | [optional] [enum: HardBounce, Transient, Unsubscribe, Subscribe, AutoResponder, AddressChange, DnsError, SpamNotification, OpenRelayTest, Unknown, SoftBounce, VirusNotification, MailFrontier Matador., BadEmailAddress, SpamComplaint, ManuallyDeactivated, Unconfirmed, Blocked, SMTPApiError, InboundError, DMARCPolicy, TemplateRenderingFailed] |
| **inactive** | **Boolean**| Filter by emails that were deactivated by Postmark due to the bounce. Set to true or false. If this isn&#39;t specified it will return both active and inactive. | [optional] |
| **emailFilter** | **String**| Filter by email address | [optional] |
| **messageID** | **String**| Filter by messageID | [optional] |
| **tag** | **String**| Filter by tag | [optional] |
| **todate** | **LocalDate**| Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |
| **fromdate** | **LocalDate**| Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**BounceSearchResponse**](BounceSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getDeliveryStats"></a>
# **getDeliveryStats**
> DeliveryStatsResponse getDeliveryStats(xPostmarkServerToken)

Get delivery stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BouncesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    BouncesApiApi apiInstance = new BouncesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    try {
      DeliveryStatsResponse result = apiInstance.getDeliveryStats(xPostmarkServerToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BouncesApiApi#getDeliveryStats");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |

### Return type

[**DeliveryStatsResponse**](DeliveryStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getSingleBounce"></a>
# **getSingleBounce**
> BounceInfoResponse getSingleBounce(xPostmarkServerToken, bounceid)

Get a single bounce

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BouncesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    BouncesApiApi apiInstance = new BouncesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Long bounceid = 56L; // Long | The ID of the bounce to retrieve.
    try {
      BounceInfoResponse result = apiInstance.getSingleBounce(xPostmarkServerToken, bounceid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BouncesApiApi#getSingleBounce");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **bounceid** | **Long**| The ID of the bounce to retrieve. | |

### Return type

[**BounceInfoResponse**](BounceInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

