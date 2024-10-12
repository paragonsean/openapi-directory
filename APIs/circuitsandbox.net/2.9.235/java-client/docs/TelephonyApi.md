# TelephonyApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getJournalEntries**](TelephonyApi.md#getJournalEntries) | **GET** /telephony/{telephonyConversationId}/journal | Get journal |
| [**v2GetDeviceInfos**](TelephonyApi.md#v2GetDeviceInfos) | **GET** /telephony/deviceInfos | Get devices infos |
| [**v2GetTelephonyConversationId**](TelephonyApi.md#v2GetTelephonyConversationId) | **GET** /telephony/telephonyConversationId | Get telephony conversation id |


<a id="getJournalEntries"></a>
# **getJournalEntries**
> List&lt;ConversationItem&gt; getJournalEntries(telephonyConversationId, timestamp, numberOfEntries, direction, journalFilter)

Get journal

Get telephony journal OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelephonyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TelephonyApi apiInstance = new TelephonyApi(defaultClient);
    String telephonyConversationId = "telephonyConversationId_example"; // String | The id of the telephony conversation
    BigDecimal timestamp = new BigDecimal("0"); // BigDecimal | A timestamp, default = 0
    BigDecimal numberOfEntries = new BigDecimal("25"); // BigDecimal | The number of entries, between 1 and 100, default = 25
    String direction = "AFTER"; // String | The direction (BEFORE||AFTER||BOTH), default = AFTER
    String journalFilter = "ALL"; // String | The filter, ALL||MISSED||DIALED||RECEIVED||DIVERTED||VOICEMAILS||UNHERAD_VOICEMAILS. default = ALL
    try {
      List<ConversationItem> result = apiInstance.getJournalEntries(telephonyConversationId, timestamp, numberOfEntries, direction, journalFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelephonyApi#getJournalEntries");
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
| **telephonyConversationId** | **String**| The id of the telephony conversation | |
| **timestamp** | **BigDecimal**| A timestamp, default &#x3D; 0 | [optional] [default to 0] |
| **numberOfEntries** | **BigDecimal**| The number of entries, between 1 and 100, default &#x3D; 25 | [optional] [default to 25] |
| **direction** | **String**| The direction (BEFORE||AFTER||BOTH), default &#x3D; AFTER | [optional] [default to AFTER] [enum: AFTER, BEFORE, BOTH] |
| **journalFilter** | **String**| The filter, ALL||MISSED||DIALED||RECEIVED||DIVERTED||VOICEMAILS||UNHERAD_VOICEMAILS. default &#x3D; ALL | [optional] [default to ALL] [enum: ALL, MISSED, DIALED, RECEIVED, DIVERTED, VOICEMAILS, UNHERAD_VOICEMAILS] |

### Return type

[**List&lt;ConversationItem&gt;**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Journal successfully retrieved |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="v2GetDeviceInfos"></a>
# **v2GetDeviceInfos**
> List&lt;V2DistributedClientInfo&gt; v2GetDeviceInfos()

Get devices infos

Get the device infos of the requesting user OauthScopes: READ_USER_PROFILE

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelephonyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TelephonyApi apiInstance = new TelephonyApi(defaultClient);
    try {
      List<V2DistributedClientInfo> result = apiInstance.v2GetDeviceInfos();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelephonyApi#v2GetDeviceInfos");
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

[**List&lt;V2DistributedClientInfo&gt;**](V2DistributedClientInfo.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Device infos successfully retrieved |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="v2GetTelephonyConversationId"></a>
# **v2GetTelephonyConversationId**
> v2GetTelephonyConversationId()

Get telephony conversation id

Get telephony conversation id for requesting client OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelephonyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TelephonyApi apiInstance = new TelephonyApi(defaultClient);
    try {
      apiInstance.v2GetTelephonyConversationId();
    } catch (ApiException e) {
      System.err.println("Exception when calling TelephonyApi#v2GetTelephonyConversationId");
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

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Telephony conversation id successfully retrieved |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

