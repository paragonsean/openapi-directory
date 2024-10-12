# WirelessV1SimApi

All URIs are relative to *https://wireless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSim**](WirelessV1SimApi.md#deleteSim) | **DELETE** /v1/Sims/{Sid} |  |
| [**fetchSim**](WirelessV1SimApi.md#fetchSim) | **GET** /v1/Sims/{Sid} |  |
| [**listSim**](WirelessV1SimApi.md#listSim) | **GET** /v1/Sims |  |
| [**updateSim**](WirelessV1SimApi.md#updateSim) | **POST** /v1/Sims/{Sid} |  |


<a id="deleteSim"></a>
# **deleteSim**
> deleteSim(sid)



Delete a Sim resource on your Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1SimApi apiInstance = new WirelessV1SimApi(defaultClient);
    String sid = "sid_example"; // String | The SID or the `unique_name` of the Sim resource to delete.
    try {
      apiInstance.deleteSim(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1SimApi#deleteSim");
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
| **sid** | **String**| The SID or the &#x60;unique_name&#x60; of the Sim resource to delete. | |

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

<a id="fetchSim"></a>
# **fetchSim**
> WirelessV1Sim fetchSim(sid)



Fetch a Sim resource on your Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1SimApi apiInstance = new WirelessV1SimApi(defaultClient);
    String sid = "sid_example"; // String | The SID or the `unique_name` of the Sim resource to fetch.
    try {
      WirelessV1Sim result = apiInstance.fetchSim(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1SimApi#fetchSim");
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
| **sid** | **String**| The SID or the &#x60;unique_name&#x60; of the Sim resource to fetch. | |

### Return type

[**WirelessV1Sim**](WirelessV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSim"></a>
# **listSim**
> ListSimResponse listSim(status, iccid, ratePlan, eid, simRegistrationCode, pageSize, page, pageToken)



Retrieve a list of Sim resources on your Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1SimApi apiInstance = new WirelessV1SimApi(defaultClient);
    SimEnumStatus status = SimEnumStatus.fromValue("new"); // SimEnumStatus | Only return Sim resources with this status.
    String iccid = "iccid_example"; // String | Only return Sim resources with this ICCID. This will return a list with a maximum size of 1.
    String ratePlan = "ratePlan_example"; // String | The SID or unique name of a [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource). Only return Sim resources assigned to this RatePlan resource.
    String eid = "eid_example"; // String | Deprecated.
    String simRegistrationCode = "simRegistrationCode_example"; // String | Only return Sim resources with this registration code. This will return a list with a maximum size of 1.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSimResponse result = apiInstance.listSim(status, iccid, ratePlan, eid, simRegistrationCode, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1SimApi#listSim");
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
| **status** | **SimEnumStatus**| Only return Sim resources with this status. | [optional] [enum: new, ready, active, suspended, deactivated, canceled, scheduled, updating] |
| **iccid** | **String**| Only return Sim resources with this ICCID. This will return a list with a maximum size of 1. | [optional] |
| **ratePlan** | **String**| The SID or unique name of a [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource). Only return Sim resources assigned to this RatePlan resource. | [optional] |
| **eid** | **String**| Deprecated. | [optional] |
| **simRegistrationCode** | **String**| Only return Sim resources with this registration code. This will return a list with a maximum size of 1. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSimResponse**](ListSimResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSim"></a>
# **updateSim**
> WirelessV1Sim updateSim(sid, accountSid, callbackMethod, callbackUrl, commandsCallbackMethod, commandsCallbackUrl, friendlyName, ratePlan, resetStatus, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, status, uniqueName, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl)



Updates the given properties of a Sim resource on your Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1SimApi apiInstance = new WirelessV1SimApi(defaultClient);
    String sid = "sid_example"; // String | The SID or the `unique_name` of the Sim resource to update.
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a [Subaccount](https://www.twilio.com/docs/iam/api/subaccounts) of the requesting Account. Only valid when the Sim resource's status is `new`. For more information, see the [Move SIMs between Subaccounts documentation](https://www.twilio.com/docs/iot/wireless/api/sim-resource#move-sims-between-subaccounts).
    String callbackMethod = "HEAD"; // String | The HTTP method we should use to call `callback_url`. Can be: `POST` or `GET`. The default is `POST`.
    URI callbackUrl = new URI(); // URI | The URL we should call using the `callback_url` when the SIM has finished updating. When the SIM transitions from `new` to `ready` or from any status to `deactivated`, we call this URL when the status changes to an intermediate status (`ready` or `deactivated`) and again when the status changes to its final status (`active` or `canceled`).
    String commandsCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `commands_callback_url`. Can be: `POST` or `GET`. The default is `POST`.
    URI commandsCallbackUrl = new URI(); // URI | The URL we should call using the `commands_callback_method` when the SIM sends a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource). Your server should respond with an HTTP status code in the 200 range; any response body is ignored.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Sim resource. It does not need to be unique.
    String ratePlan = "ratePlan_example"; // String | The SID or unique name of the [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource) to which the Sim resource should be assigned.
    SimEnumResetStatus resetStatus = SimEnumResetStatus.fromValue("resetting"); // SimEnumResetStatus | 
    String smsFallbackMethod = "HEAD"; // String | The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`. Default is `POST`.
    URI smsFallbackUrl = new URI(); // URI | The URL we should call using the `sms_fallback_method` when an error occurs while retrieving or executing the TwiML requested from `sms_url`.
    String smsMethod = "HEAD"; // String | The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`. Default is `POST`.
    URI smsUrl = new URI(); // URI | The URL we should call using the `sms_method` when the SIM-connected device sends an SMS message that is not a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource).
    SimEnumStatus status = SimEnumStatus.fromValue("new"); // SimEnumStatus | 
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used in place of the `sid` in the URL path to address the resource.
    String voiceFallbackMethod = "HEAD"; // String | Deprecated.
    URI voiceFallbackUrl = new URI(); // URI | Deprecated.
    String voiceMethod = "HEAD"; // String | Deprecated.
    URI voiceUrl = new URI(); // URI | Deprecated.
    try {
      WirelessV1Sim result = apiInstance.updateSim(sid, accountSid, callbackMethod, callbackUrl, commandsCallbackMethod, commandsCallbackUrl, friendlyName, ratePlan, resetStatus, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, status, uniqueName, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1SimApi#updateSim");
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
| **sid** | **String**| The SID or the &#x60;unique_name&#x60; of the Sim resource to update. | |
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a [Subaccount](https://www.twilio.com/docs/iam/api/subaccounts) of the requesting Account. Only valid when the Sim resource&#39;s status is &#x60;new&#x60;. For more information, see the [Move SIMs between Subaccounts documentation](https://www.twilio.com/docs/iot/wireless/api/sim-resource#move-sims-between-subaccounts). | [optional] |
| **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;. The default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **callbackUrl** | **URI**| The URL we should call using the &#x60;callback_url&#x60; when the SIM has finished updating. When the SIM transitions from &#x60;new&#x60; to &#x60;ready&#x60; or from any status to &#x60;deactivated&#x60;, we call this URL when the status changes to an intermediate status (&#x60;ready&#x60; or &#x60;deactivated&#x60;) and again when the status changes to its final status (&#x60;active&#x60; or &#x60;canceled&#x60;). | [optional] |
| **commandsCallbackMethod** | **String**| The HTTP method we should use to call &#x60;commands_callback_url&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;. The default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **commandsCallbackUrl** | **URI**| The URL we should call using the &#x60;commands_callback_method&#x60; when the SIM sends a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource). Your server should respond with an HTTP status code in the 200 range; any response body is ignored. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the Sim resource. It does not need to be unique. | [optional] |
| **ratePlan** | **String**| The SID or unique name of the [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource) to which the Sim resource should be assigned. | [optional] |
| **resetStatus** | **SimEnumResetStatus**|  | [optional] [enum: resetting] |
| **smsFallbackMethod** | **String**| The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**| The URL we should call using the &#x60;sms_fallback_method&#x60; when an error occurs while retrieving or executing the TwiML requested from &#x60;sms_url&#x60;. | [optional] |
| **smsMethod** | **String**| The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsUrl** | **URI**| The URL we should call using the &#x60;sms_method&#x60; when the SIM-connected device sends an SMS message that is not a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource). | [optional] |
| **status** | **SimEnumStatus**|  | [optional] [enum: new, ready, active, suspended, deactivated, canceled, scheduled, updating] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the &#x60;sid&#x60; in the URL path to address the resource. | [optional] |
| **voiceFallbackMethod** | **String**| Deprecated. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| Deprecated. | [optional] |
| **voiceMethod** | **String**| Deprecated. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceUrl** | **URI**| Deprecated. | [optional] |

### Return type

[**WirelessV1Sim**](WirelessV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

