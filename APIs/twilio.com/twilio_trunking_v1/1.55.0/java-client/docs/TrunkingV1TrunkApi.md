# TrunkingV1TrunkApi

All URIs are relative to *https://trunking.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTrunk**](TrunkingV1TrunkApi.md#createTrunk) | **POST** /v1/Trunks |  |
| [**deleteTrunk**](TrunkingV1TrunkApi.md#deleteTrunk) | **DELETE** /v1/Trunks/{Sid} |  |
| [**fetchTrunk**](TrunkingV1TrunkApi.md#fetchTrunk) | **GET** /v1/Trunks/{Sid} |  |
| [**listTrunk**](TrunkingV1TrunkApi.md#listTrunk) | **GET** /v1/Trunks |  |
| [**updateTrunk**](TrunkingV1TrunkApi.md#updateTrunk) | **POST** /v1/Trunks/{Sid} |  |


<a id="createTrunk"></a>
# **createTrunk**
> TrunkingV1Trunk createTrunk(cnamLookupEnabled, disasterRecoveryMethod, disasterRecoveryUrl, domainName, friendlyName, secure, transferCallerId, transferMode)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1TrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1TrunkApi apiInstance = new TrunkingV1TrunkApi(defaultClient);
    Boolean cnamLookupEnabled = true; // Boolean | Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    String disasterRecoveryMethod = "HEAD"; // String | The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
    URI disasterRecoveryUrl = new URI(); // URI | The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
    String domainName = "domainName_example"; // String | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    Boolean secure = true; // Boolean | Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
    TrunkEnumTransferCallerId transferCallerId = TrunkEnumTransferCallerId.fromValue("from-transferee"); // TrunkEnumTransferCallerId | 
    TrunkEnumTransferSetting transferMode = TrunkEnumTransferSetting.fromValue("disable-all"); // TrunkEnumTransferSetting | 
    try {
      TrunkingV1Trunk result = apiInstance.createTrunk(cnamLookupEnabled, disasterRecoveryMethod, disasterRecoveryUrl, domainName, friendlyName, secure, transferCallerId, transferMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1TrunkApi#createTrunk");
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
| **cnamLookupEnabled** | **Boolean**| Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] |
| **disasterRecoveryMethod** | **String**| The HTTP method we should use to call the &#x60;disaster_recovery_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **disasterRecoveryUrl** | **URI**| The URL we should call using the &#x60;disaster_recovery_method&#x60; if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information. | [optional] |
| **domainName** | **String**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and &#x60;-&#x60; and must end with &#x60;pstn.twilio.com&#x60;. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **secure** | **Boolean**| Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information. | [optional] |
| **transferCallerId** | **TrunkEnumTransferCallerId**|  | [optional] [enum: from-transferee, from-transferor] |
| **transferMode** | **TrunkEnumTransferSetting**|  | [optional] [enum: disable-all, enable-all, sip-only] |

### Return type

[**TrunkingV1Trunk**](TrunkingV1Trunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteTrunk"></a>
# **deleteTrunk**
> deleteTrunk(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1TrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1TrunkApi apiInstance = new TrunkingV1TrunkApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Trunk resource to delete.
    try {
      apiInstance.deleteTrunk(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1TrunkApi#deleteTrunk");
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
| **sid** | **String**| The unique string that we created to identify the Trunk resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchTrunk"></a>
# **fetchTrunk**
> TrunkingV1Trunk fetchTrunk(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1TrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1TrunkApi apiInstance = new TrunkingV1TrunkApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Trunk resource to fetch.
    try {
      TrunkingV1Trunk result = apiInstance.fetchTrunk(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1TrunkApi#fetchTrunk");
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
| **sid** | **String**| The unique string that we created to identify the Trunk resource to fetch. | |

### Return type

[**TrunkingV1Trunk**](TrunkingV1Trunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTrunk"></a>
# **listTrunk**
> ListTrunkResponse listTrunk(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1TrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1TrunkApi apiInstance = new TrunkingV1TrunkApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTrunkResponse result = apiInstance.listTrunk(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1TrunkApi#listTrunk");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTrunkResponse**](ListTrunkResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTrunk"></a>
# **updateTrunk**
> TrunkingV1Trunk updateTrunk(sid, cnamLookupEnabled, disasterRecoveryMethod, disasterRecoveryUrl, domainName, friendlyName, secure, transferCallerId, transferMode)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1TrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1TrunkApi apiInstance = new TrunkingV1TrunkApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the OriginationUrl resource to update.
    Boolean cnamLookupEnabled = true; // Boolean | Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    String disasterRecoveryMethod = "HEAD"; // String | The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
    URI disasterRecoveryUrl = new URI(); // URI | The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
    String domainName = "domainName_example"; // String | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    Boolean secure = true; // Boolean | Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
    TrunkEnumTransferCallerId transferCallerId = TrunkEnumTransferCallerId.fromValue("from-transferee"); // TrunkEnumTransferCallerId | 
    TrunkEnumTransferSetting transferMode = TrunkEnumTransferSetting.fromValue("disable-all"); // TrunkEnumTransferSetting | 
    try {
      TrunkingV1Trunk result = apiInstance.updateTrunk(sid, cnamLookupEnabled, disasterRecoveryMethod, disasterRecoveryUrl, domainName, friendlyName, secure, transferCallerId, transferMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1TrunkApi#updateTrunk");
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
| **sid** | **String**| The unique string that we created to identify the OriginationUrl resource to update. | |
| **cnamLookupEnabled** | **Boolean**| Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] |
| **disasterRecoveryMethod** | **String**| The HTTP method we should use to call the &#x60;disaster_recovery_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **disasterRecoveryUrl** | **URI**| The URL we should call using the &#x60;disaster_recovery_method&#x60; if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information. | [optional] |
| **domainName** | **String**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and &#x60;-&#x60; and must end with &#x60;pstn.twilio.com&#x60;. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **secure** | **Boolean**| Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information. | [optional] |
| **transferCallerId** | **TrunkEnumTransferCallerId**|  | [optional] [enum: from-transferee, from-transferor] |
| **transferMode** | **TrunkEnumTransferSetting**|  | [optional] [enum: disable-all, enable-all, sip-only] |

### Return type

[**TrunkingV1Trunk**](TrunkingV1Trunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

