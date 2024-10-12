# DefaultApi

All URIs are relative to *https://rest.nexmo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**buyANumber**](DefaultApi.md#buyANumber) | **POST** /number/buy | Buy a number |
| [**cancelANumber**](DefaultApi.md#cancelANumber) | **POST** /number/cancel | Cancel a number |
| [**getAvailableNumbers**](DefaultApi.md#getAvailableNumbers) | **GET** /number/search | Search available numbers |
| [**getOwnedNumbers**](DefaultApi.md#getOwnedNumbers) | **GET** /account/numbers | List the numbers you own |
| [**updateANumber**](DefaultApi.md#updateANumber) | **POST** /number/update | Update a number |


<a id="buyANumber"></a>
# **buyANumber**
> Response buyANumber(country, msisdn, targetApiKey)

Buy a number

Request to purchase a specific inbound number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.nexmo.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String country = "country_example"; // String | The two character country code in ISO 3166-1 alpha-2 format
    String msisdn = "msisdn_example"; // String | An available inbound virtual number.
    String targetApiKey = "targetApiKey_example"; // String | If you’d like to perform an action on a subaccount, provide the `api_key` of that account here. If you’d like to perform an action on your own account, you do not need to provide this field.
    try {
      Response result = apiInstance.buyANumber(country, msisdn, targetApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#buyANumber");
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
| **country** | **String**| The two character country code in ISO 3166-1 alpha-2 format | |
| **msisdn** | **String**| An available inbound virtual number. | |
| **targetApiKey** | **String**| If you’d like to perform an action on a subaccount, provide the &#x60;api_key&#x60; of that account here. If you’d like to perform an action on your own account, you do not need to provide this field. | [optional] |

### Return type

[**Response**](Response.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **420** | Action failed |  -  |

<a id="cancelANumber"></a>
# **cancelANumber**
> Response cancelANumber(country, msisdn, targetApiKey)

Cancel a number

Cancel your subscription for a specific inbound number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.nexmo.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String country = "country_example"; // String | The two character country code in ISO 3166-1 alpha-2 format
    String msisdn = "msisdn_example"; // String | An available inbound virtual number.
    String targetApiKey = "targetApiKey_example"; // String | If you’d like to perform an action on a subaccount, provide the `api_key` of that account here. If you’d like to perform an action on your own account, you do not need to provide this field.
    try {
      Response result = apiInstance.cancelANumber(country, msisdn, targetApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cancelANumber");
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
| **country** | **String**| The two character country code in ISO 3166-1 alpha-2 format | |
| **msisdn** | **String**| An available inbound virtual number. | |
| **targetApiKey** | **String**| If you’d like to perform an action on a subaccount, provide the &#x60;api_key&#x60; of that account here. If you’d like to perform an action on your own account, you do not need to provide this field. | [optional] |

### Return type

[**Response**](Response.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

<a id="getAvailableNumbers"></a>
# **getAvailableNumbers**
> AvailableNumbers getAvailableNumbers(country, type, pattern, searchPattern, features, size, index)

Search available numbers

Retrieve inbound numbers that are available for the specified country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.nexmo.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String country = "country_example"; // String | The two character country code to filter on (in ISO 3166-1 alpha-2 format)
    String type = "landline"; // String | Set this parameter to filter the type of number, such as mobile or landline
    String pattern = "12345"; // String | The number pattern you want to search for. Use in conjunction with `search_pattern`.
    Integer searchPattern = 0; // Integer | The strategy you want to use for matching:   * `0` - Search for numbers that start with `pattern` (Note: all numbers are in E.164 format, so the starting pattern includes the country code, such as 1 for USA) * `1` - Search for numbers that contain `pattern` * `2` - Search for numbers that end with `pattern` 
    String features = "SMS"; // String | Available features are `SMS`, `VOICE` and `MMS`. To look for numbers that support multiple features, use a comma-separated value: `SMS,MMS,VOICE`.
    Integer size = 10; // Integer | Page size
    Integer index = 1; // Integer | Page index
    try {
      AvailableNumbers result = apiInstance.getAvailableNumbers(country, type, pattern, searchPattern, features, size, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAvailableNumbers");
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
| **country** | **String**| The two character country code to filter on (in ISO 3166-1 alpha-2 format) | |
| **type** | **String**| Set this parameter to filter the type of number, such as mobile or landline | [optional] [enum: landline, mobile-lvn, landline-toll-free] |
| **pattern** | **String**| The number pattern you want to search for. Use in conjunction with &#x60;search_pattern&#x60;. | [optional] |
| **searchPattern** | **Integer**| The strategy you want to use for matching:   * &#x60;0&#x60; - Search for numbers that start with &#x60;pattern&#x60; (Note: all numbers are in E.164 format, so the starting pattern includes the country code, such as 1 for USA) * &#x60;1&#x60; - Search for numbers that contain &#x60;pattern&#x60; * &#x60;2&#x60; - Search for numbers that end with &#x60;pattern&#x60;  | [optional] [default to 0] [enum: 0, 1, 2] |
| **features** | **String**| Available features are &#x60;SMS&#x60;, &#x60;VOICE&#x60; and &#x60;MMS&#x60;. To look for numbers that support multiple features, use a comma-separated value: &#x60;SMS,MMS,VOICE&#x60;. | [optional] [enum: SMS, VOICE, SMS,VOICE, MMS, SMS,MMS, VOICE,MMS, SMS,MMS,VOICE] |
| **size** | **Integer**| Page size | [optional] [default to 10] |
| **index** | **Integer**| Page index | [optional] [default to 1] |

### Return type

[**AvailableNumbers**](AvailableNumbers.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

<a id="getOwnedNumbers"></a>
# **getOwnedNumbers**
> InboundNumbers getOwnedNumbers(applicationId, hasApplication, country, pattern, searchPattern, size, index)

List the numbers you own

Retrieve all the inbound numbers associated with your Vonage account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.nexmo.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The Application that you want to return the numbers for.
    Boolean hasApplication = false; // Boolean | Set this optional field to `true` to restrict your results to numbers associated with an Application (any Application). Set to `false` to find all numbers not associated with any Application. Omit the field to avoid filtering on whether or not the number is assigned to an Application. 
    String country = "country_example"; // String | 
    String pattern = "12345"; // String | The number pattern you want to search for. Use in conjunction with `search_pattern`.
    Integer searchPattern = 0; // Integer | The strategy you want to use for matching:   * `0` - Search for numbers that start with `pattern` (Note: all numbers are in E.164 format, so the starting pattern includes the country code, such as 1 for USA) * `1` - Search for numbers that contain `pattern` * `2` - Search for numbers that end with `pattern` 
    Integer size = 10; // Integer | Page size
    Integer index = 1; // Integer | Page index
    try {
      InboundNumbers result = apiInstance.getOwnedNumbers(applicationId, hasApplication, country, pattern, searchPattern, size, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOwnedNumbers");
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
| **applicationId** | **String**| The Application that you want to return the numbers for. | [optional] |
| **hasApplication** | **Boolean**| Set this optional field to &#x60;true&#x60; to restrict your results to numbers associated with an Application (any Application). Set to &#x60;false&#x60; to find all numbers not associated with any Application. Omit the field to avoid filtering on whether or not the number is assigned to an Application.  | [optional] |
| **country** | **String**|  | [optional] |
| **pattern** | **String**| The number pattern you want to search for. Use in conjunction with &#x60;search_pattern&#x60;. | [optional] |
| **searchPattern** | **Integer**| The strategy you want to use for matching:   * &#x60;0&#x60; - Search for numbers that start with &#x60;pattern&#x60; (Note: all numbers are in E.164 format, so the starting pattern includes the country code, such as 1 for USA) * &#x60;1&#x60; - Search for numbers that contain &#x60;pattern&#x60; * &#x60;2&#x60; - Search for numbers that end with &#x60;pattern&#x60;  | [optional] [default to 0] [enum: 0, 1, 2] |
| **size** | **Integer**| Page size | [optional] [default to 10] |
| **index** | **Integer**| Page index | [optional] [default to 1] |

### Return type

[**InboundNumbers**](InboundNumbers.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

<a id="updateANumber"></a>
# **updateANumber**
> Response updateANumber(country, msisdn, appId, messagesCallbackType, messagesCallbackValue, moHttpUrl, moSmppSysType, voiceCallbackType, voiceCallbackValue, voiceStatusCallback)

Update a number

Change the behaviour of a number that you own.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.nexmo.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String country = "country_example"; // String | The two character country code in ISO 3166-1 alpha-2 format
    String msisdn = "msisdn_example"; // String | An available inbound virtual number.
    String appId = "appId_example"; // String | The Application that will handle inbound traffic to this number.
    String messagesCallbackType = "app"; // String | <strong>DEPRECATED</strong> - We recommend that you use `app_id` instead.  Specifies the Messages webhook type (always `app`) associated with this number and must be used with the `messagesCallbackValue` parameter. 
    String messagesCallbackValue = "messagesCallbackValue_example"; // String | <strong>DEPRECATED</strong> - We recommend that you use `app_id` instead.  Specifies the Application ID of your Messages application. It must be used with the `messagesCallbackType` parameter. 
    String moHttpUrl = "moHttpUrl_example"; // String | An URL-encoded URI to the webhook endpoint that handles inbound messages. Your webhook endpoint must be active before you make this request. Vonage makes a `GET` request to the endpoint and checks that it returns a `200 OK` response. Set this parameter's value to an empty string to remove the webhook.
    String moSmppSysType = "moSmppSysType_example"; // String | The associated system type for your SMPP client
    String voiceCallbackType = "sip"; // String | Specify whether inbound voice calls on your number are forwarded to a SIP or a telephone number.  This must be used with the `voiceCallbackValue` parameter. If set, `sip` or `tel` are prioritized over the Voice capability in your Application.  *Note: The `app` value is deprecated and will be removed in future.* 
    String voiceCallbackValue = "voiceCallbackValue_example"; // String | A SIP URI or telephone number. Must be used with the `voiceCallbackType` parameter.
    String voiceStatusCallback = "voiceStatusCallback_example"; // String | A webhook URI for Vonage to send a request to when a call ends
    try {
      Response result = apiInstance.updateANumber(country, msisdn, appId, messagesCallbackType, messagesCallbackValue, moHttpUrl, moSmppSysType, voiceCallbackType, voiceCallbackValue, voiceStatusCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateANumber");
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
| **country** | **String**| The two character country code in ISO 3166-1 alpha-2 format | |
| **msisdn** | **String**| An available inbound virtual number. | |
| **appId** | **String**| The Application that will handle inbound traffic to this number. | [optional] |
| **messagesCallbackType** | **String**| &lt;strong&gt;DEPRECATED&lt;/strong&gt; - We recommend that you use &#x60;app_id&#x60; instead.  Specifies the Messages webhook type (always &#x60;app&#x60;) associated with this number and must be used with the &#x60;messagesCallbackValue&#x60; parameter.  | [optional] [enum: app] |
| **messagesCallbackValue** | **String**| &lt;strong&gt;DEPRECATED&lt;/strong&gt; - We recommend that you use &#x60;app_id&#x60; instead.  Specifies the Application ID of your Messages application. It must be used with the &#x60;messagesCallbackType&#x60; parameter.  | [optional] |
| **moHttpUrl** | **String**| An URL-encoded URI to the webhook endpoint that handles inbound messages. Your webhook endpoint must be active before you make this request. Vonage makes a &#x60;GET&#x60; request to the endpoint and checks that it returns a &#x60;200 OK&#x60; response. Set this parameter&#39;s value to an empty string to remove the webhook. | [optional] |
| **moSmppSysType** | **String**| The associated system type for your SMPP client | [optional] |
| **voiceCallbackType** | **String**| Specify whether inbound voice calls on your number are forwarded to a SIP or a telephone number.  This must be used with the &#x60;voiceCallbackValue&#x60; parameter. If set, &#x60;sip&#x60; or &#x60;tel&#x60; are prioritized over the Voice capability in your Application.  *Note: The &#x60;app&#x60; value is deprecated and will be removed in future.*  | [optional] [enum: sip, tel, app] |
| **voiceCallbackValue** | **String**| A SIP URI or telephone number. Must be used with the &#x60;voiceCallbackType&#x60; parameter. | [optional] |
| **voiceStatusCallback** | **String**| A webhook URI for Vonage to send a request to when a call ends | [optional] |

### Return type

[**Response**](Response.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

