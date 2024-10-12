# SupersimV1SmsCommandApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSmsCommand**](SupersimV1SmsCommandApi.md#createSmsCommand) | **POST** /v1/SmsCommands |  |
| [**fetchSmsCommand**](SupersimV1SmsCommandApi.md#fetchSmsCommand) | **GET** /v1/SmsCommands/{Sid} |  |
| [**listSmsCommand**](SupersimV1SmsCommandApi.md#listSmsCommand) | **GET** /v1/SmsCommands |  |


<a id="createSmsCommand"></a>
# **createSmsCommand**
> SupersimV1SmsCommand createSmsCommand(payload, sim, callbackMethod, callbackUrl)



Send SMS Command to a Sim.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1SmsCommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1SmsCommandApi apiInstance = new SupersimV1SmsCommandApi(defaultClient);
    String payload = "payload_example"; // String | The message body of the SMS Command.
    String sim = "sim_example"; // String | The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the SMS Command to.
    String callbackMethod = "HEAD"; // String | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
    URI callbackUrl = new URI(); // URI | The URL we should call using the `callback_method` after we have sent the command.
    try {
      SupersimV1SmsCommand result = apiInstance.createSmsCommand(payload, sim, callbackMethod, callbackUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1SmsCommandApi#createSmsCommand");
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
| **payload** | **String**| The message body of the SMS Command. | |
| **sim** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the SMS Command to. | |
| **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is POST. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **callbackUrl** | **URI**| The URL we should call using the &#x60;callback_method&#x60; after we have sent the command. | [optional] |

### Return type

[**SupersimV1SmsCommand**](SupersimV1SmsCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchSmsCommand"></a>
# **fetchSmsCommand**
> SupersimV1SmsCommand fetchSmsCommand(sid)



Fetch SMS Command instance from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1SmsCommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1SmsCommandApi apiInstance = new SupersimV1SmsCommandApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the SMS Command resource to fetch.
    try {
      SupersimV1SmsCommand result = apiInstance.fetchSmsCommand(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1SmsCommandApi#fetchSmsCommand");
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
| **sid** | **String**| The SID of the SMS Command resource to fetch. | |

### Return type

[**SupersimV1SmsCommand**](SupersimV1SmsCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSmsCommand"></a>
# **listSmsCommand**
> ListSmsCommandResponse listSmsCommand(sim, status, direction, pageSize, page, pageToken)



Retrieve a list of SMS Commands from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1SmsCommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1SmsCommandApi apiInstance = new SupersimV1SmsCommandApi(defaultClient);
    String sim = "sim_example"; // String | The SID or unique name of the Sim resource that SMS Command was sent to or from.
    SmsCommandEnumStatus status = SmsCommandEnumStatus.fromValue("queued"); // SmsCommandEnumStatus | The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
    SmsCommandEnumDirection direction = SmsCommandEnumDirection.fromValue("to_sim"); // SmsCommandEnumDirection | The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSmsCommandResponse result = apiInstance.listSmsCommand(sim, status, direction, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1SmsCommandApi#listSmsCommand");
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
| **sim** | **String**| The SID or unique name of the Sim resource that SMS Command was sent to or from. | [optional] |
| **status** | **SmsCommandEnumStatus**| The status of the SMS Command. Can be: &#x60;queued&#x60;, &#x60;sent&#x60;, &#x60;delivered&#x60;, &#x60;received&#x60; or &#x60;failed&#x60;. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each. | [optional] [enum: queued, sent, delivered, received, failed] |
| **direction** | **SmsCommandEnumDirection**| The direction of the SMS Command. Can be &#x60;to_sim&#x60; or &#x60;from_sim&#x60;. The value of &#x60;to_sim&#x60; is synonymous with the term &#x60;mobile terminated&#x60;, and &#x60;from_sim&#x60; is synonymous with the term &#x60;mobile originated&#x60;. | [optional] [enum: to_sim, from_sim] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSmsCommandResponse**](ListSmsCommandResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

