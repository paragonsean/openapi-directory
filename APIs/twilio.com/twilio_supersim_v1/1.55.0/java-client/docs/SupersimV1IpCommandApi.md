# SupersimV1IpCommandApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIpCommand**](SupersimV1IpCommandApi.md#createIpCommand) | **POST** /v1/IpCommands |  |
| [**fetchIpCommand**](SupersimV1IpCommandApi.md#fetchIpCommand) | **GET** /v1/IpCommands/{Sid} |  |
| [**listIpCommand**](SupersimV1IpCommandApi.md#listIpCommand) | **GET** /v1/IpCommands |  |


<a id="createIpCommand"></a>
# **createIpCommand**
> SupersimV1IpCommand createIpCommand(devicePort, payload, sim, callbackMethod, callbackUrl, payloadType)



Send an IP Command to a Super SIM.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1IpCommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1IpCommandApi apiInstance = new SupersimV1IpCommandApi(defaultClient);
    Integer devicePort = 56; // Integer | The device port to which the IP Command will be sent.
    String payload = "payload_example"; // String | The data that will be sent to the device. The payload cannot exceed 1300 bytes. If the PayloadType is set to text, the payload is encoded in UTF-8. If PayloadType is set to binary, the payload is encoded in Base64.
    String sim = "sim_example"; // String | The `sid` or `unique_name` of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the IP Command to.
    String callbackMethod = "HEAD"; // String | The HTTP method we should use to call `callback_url`. Can be `GET` or `POST`, and the default is `POST`.
    URI callbackUrl = new URI(); // URI | The URL we should call using the `callback_method` after we have sent the IP Command.
    IpCommandEnumPayloadType payloadType = IpCommandEnumPayloadType.fromValue("text"); // IpCommandEnumPayloadType | 
    try {
      SupersimV1IpCommand result = apiInstance.createIpCommand(devicePort, payload, sim, callbackMethod, callbackUrl, payloadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1IpCommandApi#createIpCommand");
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
| **devicePort** | **Integer**| The device port to which the IP Command will be sent. | |
| **payload** | **String**| The data that will be sent to the device. The payload cannot exceed 1300 bytes. If the PayloadType is set to text, the payload is encoded in UTF-8. If PayloadType is set to binary, the payload is encoded in Base64. | |
| **sim** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the IP Command to. | |
| **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60;, and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **callbackUrl** | **URI**| The URL we should call using the &#x60;callback_method&#x60; after we have sent the IP Command. | [optional] |
| **payloadType** | **IpCommandEnumPayloadType**|  | [optional] [enum: text, binary] |

### Return type

[**SupersimV1IpCommand**](SupersimV1IpCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchIpCommand"></a>
# **fetchIpCommand**
> SupersimV1IpCommand fetchIpCommand(sid)



Fetch IP Command instance from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1IpCommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1IpCommandApi apiInstance = new SupersimV1IpCommandApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the IP Command resource to fetch.
    try {
      SupersimV1IpCommand result = apiInstance.fetchIpCommand(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1IpCommandApi#fetchIpCommand");
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
| **sid** | **String**| The SID of the IP Command resource to fetch. | |

### Return type

[**SupersimV1IpCommand**](SupersimV1IpCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listIpCommand"></a>
# **listIpCommand**
> ListIpCommandResponse listIpCommand(sim, simIccid, status, direction, pageSize, page, pageToken)



Retrieve a list of IP Commands from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1IpCommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1IpCommandApi apiInstance = new SupersimV1IpCommandApi(defaultClient);
    String sim = "sim_example"; // String | The SID or unique name of the Sim resource that IP Command was sent to or from.
    String simIccid = "simIccid_example"; // String | The ICCID of the Sim resource that IP Command was sent to or from.
    IpCommandEnumStatus status = IpCommandEnumStatus.fromValue("queued"); // IpCommandEnumStatus | The status of the IP Command. Can be: `queued`, `sent`, `received` or `failed`. See the [IP Command Status Values](https://www.twilio.com/docs/iot/supersim/api/ipcommand-resource#status-values) for a description of each.
    IpCommandEnumDirection direction = IpCommandEnumDirection.fromValue("to_sim"); // IpCommandEnumDirection | The direction of the IP Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListIpCommandResponse result = apiInstance.listIpCommand(sim, simIccid, status, direction, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1IpCommandApi#listIpCommand");
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
| **sim** | **String**| The SID or unique name of the Sim resource that IP Command was sent to or from. | [optional] |
| **simIccid** | **String**| The ICCID of the Sim resource that IP Command was sent to or from. | [optional] |
| **status** | **IpCommandEnumStatus**| The status of the IP Command. Can be: &#x60;queued&#x60;, &#x60;sent&#x60;, &#x60;received&#x60; or &#x60;failed&#x60;. See the [IP Command Status Values](https://www.twilio.com/docs/iot/supersim/api/ipcommand-resource#status-values) for a description of each. | [optional] [enum: queued, sent, received, failed] |
| **direction** | **IpCommandEnumDirection**| The direction of the IP Command. Can be &#x60;to_sim&#x60; or &#x60;from_sim&#x60;. The value of &#x60;to_sim&#x60; is synonymous with the term &#x60;mobile terminated&#x60;, and &#x60;from_sim&#x60; is synonymous with the term &#x60;mobile originated&#x60;. | [optional] [enum: to_sim, from_sim] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListIpCommandResponse**](ListIpCommandResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

