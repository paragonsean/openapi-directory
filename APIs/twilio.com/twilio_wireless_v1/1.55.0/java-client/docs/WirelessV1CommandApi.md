# WirelessV1CommandApi

All URIs are relative to *https://wireless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCommand**](WirelessV1CommandApi.md#createCommand) | **POST** /v1/Commands |  |
| [**deleteCommand**](WirelessV1CommandApi.md#deleteCommand) | **DELETE** /v1/Commands/{Sid} |  |
| [**fetchCommand**](WirelessV1CommandApi.md#fetchCommand) | **GET** /v1/Commands/{Sid} |  |
| [**listCommand**](WirelessV1CommandApi.md#listCommand) | **GET** /v1/Commands |  |


<a id="createCommand"></a>
# **createCommand**
> WirelessV1Command createCommand(command, callbackMethod, callbackUrl, commandMode, deliveryReceiptRequested, includeSid, sim)



Send a Command to a Sim.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1CommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1CommandApi apiInstance = new WirelessV1CommandApi(defaultClient);
    String command = "command_example"; // String | The message body of the Command. Can be plain text in text mode or a Base64 encoded byte string in binary mode.
    String callbackMethod = "HEAD"; // String | The HTTP method we use to call `callback_url`. Can be: `POST` or `GET`, and the default is `POST`.
    URI callbackUrl = new URI(); // URI | The URL we call using the `callback_url` when the Command has finished sending, whether the command was delivered or it failed.
    CommandEnumCommandMode commandMode = CommandEnumCommandMode.fromValue("text"); // CommandEnumCommandMode | 
    Boolean deliveryReceiptRequested = true; // Boolean | Whether to request delivery receipt from the recipient. For Commands that request delivery receipt, the Command state transitions to 'delivered' once the server has received a delivery receipt from the device. The default value is `true`.
    String includeSid = "includeSid_example"; // String | Whether to include the SID of the command in the message body. Can be: `none`, `start`, or `end`, and the default behavior is `none`. When sending a Command to a SIM in text mode, we can automatically include the SID of the Command in the message body, which could be used to ensure that the device does not process the same Command more than once.  A value of `start` will prepend the message with the Command SID, and `end` will append it to the end, separating the Command SID from the message body with a space. The length of the Command SID is included in the 160 character limit so the SMS body must be 128 characters or less before the Command SID is included.
    String sim = "sim_example"; // String | The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to send the Command to.
    try {
      WirelessV1Command result = apiInstance.createCommand(command, callbackMethod, callbackUrl, commandMode, deliveryReceiptRequested, includeSid, sim);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1CommandApi#createCommand");
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
| **command** | **String**| The message body of the Command. Can be plain text in text mode or a Base64 encoded byte string in binary mode. | |
| **callbackMethod** | **String**| The HTTP method we use to call &#x60;callback_url&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;, and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **callbackUrl** | **URI**| The URL we call using the &#x60;callback_url&#x60; when the Command has finished sending, whether the command was delivered or it failed. | [optional] |
| **commandMode** | **CommandEnumCommandMode**|  | [optional] [enum: text, binary] |
| **deliveryReceiptRequested** | **Boolean**| Whether to request delivery receipt from the recipient. For Commands that request delivery receipt, the Command state transitions to &#39;delivered&#39; once the server has received a delivery receipt from the device. The default value is &#x60;true&#x60;. | [optional] |
| **includeSid** | **String**| Whether to include the SID of the command in the message body. Can be: &#x60;none&#x60;, &#x60;start&#x60;, or &#x60;end&#x60;, and the default behavior is &#x60;none&#x60;. When sending a Command to a SIM in text mode, we can automatically include the SID of the Command in the message body, which could be used to ensure that the device does not process the same Command more than once.  A value of &#x60;start&#x60; will prepend the message with the Command SID, and &#x60;end&#x60; will append it to the end, separating the Command SID from the message body with a space. The length of the Command SID is included in the 160 character limit so the SMS body must be 128 characters or less before the Command SID is included. | [optional] |
| **sim** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [SIM](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to send the Command to. | [optional] |

### Return type

[**WirelessV1Command**](WirelessV1Command.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteCommand"></a>
# **deleteCommand**
> deleteCommand(sid)



Delete a Command instance from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1CommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1CommandApi apiInstance = new WirelessV1CommandApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Command resource to delete.
    try {
      apiInstance.deleteCommand(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1CommandApi#deleteCommand");
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
| **sid** | **String**| The SID of the Command resource to delete. | |

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

<a id="fetchCommand"></a>
# **fetchCommand**
> WirelessV1Command fetchCommand(sid)



Fetch a Command instance from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1CommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1CommandApi apiInstance = new WirelessV1CommandApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Command resource to fetch.
    try {
      WirelessV1Command result = apiInstance.fetchCommand(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1CommandApi#fetchCommand");
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
| **sid** | **String**| The SID of the Command resource to fetch. | |

### Return type

[**WirelessV1Command**](WirelessV1Command.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listCommand"></a>
# **listCommand**
> ListCommandResponse listCommand(sim, status, direction, transport, pageSize, page, pageToken)



Retrieve a list of Commands from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1CommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1CommandApi apiInstance = new WirelessV1CommandApi(defaultClient);
    String sim = "sim_example"; // String | The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read.
    CommandEnumStatus status = CommandEnumStatus.fromValue("queued"); // CommandEnumStatus | The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
    CommandEnumDirection direction = CommandEnumDirection.fromValue("from_sim"); // CommandEnumDirection | Only return Commands with this direction value.
    CommandEnumTransport transport = CommandEnumTransport.fromValue("sms"); // CommandEnumTransport | Only return Commands with this transport value. Can be: `sms` or `ip`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCommandResponse result = apiInstance.listCommand(sim, status, direction, transport, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1CommandApi#listCommand");
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
| **sim** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read. | [optional] |
| **status** | **CommandEnumStatus**| The status of the resources to read. Can be: &#x60;queued&#x60;, &#x60;sent&#x60;, &#x60;delivered&#x60;, &#x60;received&#x60;, or &#x60;failed&#x60;. | [optional] [enum: queued, sent, delivered, received, failed] |
| **direction** | **CommandEnumDirection**| Only return Commands with this direction value. | [optional] [enum: from_sim, to_sim] |
| **transport** | **CommandEnumTransport**| Only return Commands with this transport value. Can be: &#x60;sms&#x60; or &#x60;ip&#x60;. | [optional] [enum: sms, ip] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListCommandResponse**](ListCommandResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

