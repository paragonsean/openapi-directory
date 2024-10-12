# Api20100401ShortCodeApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchShortCode**](Api20100401ShortCodeApi.md#fetchShortCode) | **GET** /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json |  |
| [**listShortCode**](Api20100401ShortCodeApi.md#listShortCode) | **GET** /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes.json |  |
| [**updateShortCode**](Api20100401ShortCodeApi.md#updateShortCode) | **POST** /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json |  |


<a id="fetchShortCode"></a>
# **fetchShortCode**
> ApiV2010AccountShortCode fetchShortCode(accountSid, sid)



Fetch an instance of a short code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ShortCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ShortCodeApi apiInstance = new Api20100401ShortCodeApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ShortCode resource to fetch
    try {
      ApiV2010AccountShortCode result = apiInstance.fetchShortCode(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ShortCodeApi#fetchShortCode");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the ShortCode resource to fetch | |

### Return type

[**ApiV2010AccountShortCode**](ApiV2010AccountShortCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listShortCode"></a>
# **listShortCode**
> ListShortCodeResponse listShortCode(accountSid, friendlyName, shortCode, pageSize, page, pageToken)



Retrieve a list of short-codes belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ShortCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ShortCodeApi apiInstance = new Api20100401ShortCodeApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to read.
    String friendlyName = "friendlyName_example"; // String | The string that identifies the ShortCode resources to read.
    String shortCode = "shortCode_example"; // String | Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListShortCodeResponse result = apiInstance.listShortCode(accountSid, friendlyName, shortCode, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ShortCodeApi#listShortCode");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to read. | |
| **friendlyName** | **String**| The string that identifies the ShortCode resources to read. | [optional] |
| **shortCode** | **String**| Only show the ShortCode resources that match this pattern. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListShortCodeResponse**](ListShortCodeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateShortCode"></a>
# **updateShortCode**
> ApiV2010AccountShortCode updateShortCode(accountSid, sid, apiVersion, friendlyName, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl)



Update a short code with the following parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ShortCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ShortCodeApi apiInstance = new Api20100401ShortCodeApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ShortCode resource to update
    String apiVersion = "apiVersion_example"; // String | The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the `FriendlyName` is the short code.
    String smsFallbackMethod = "HEAD"; // String | The HTTP method that we should use to call the `sms_fallback_url`. Can be: `GET` or `POST`.
    URI smsFallbackUrl = new URI(); // URI | The URL that we should call if an error occurs while retrieving or executing the TwiML from `sms_url`.
    String smsMethod = "HEAD"; // String | The HTTP method we should use when calling the `sms_url`. Can be: `GET` or `POST`.
    URI smsUrl = new URI(); // URI | The URL we should call when receiving an incoming SMS message to this short code.
    try {
      ApiV2010AccountShortCode result = apiInstance.updateShortCode(accountSid, sid, apiVersion, friendlyName, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ShortCodeApi#updateShortCode");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the ShortCode resource to update | |
| **apiVersion** | **String**| The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. | [optional] |
| **friendlyName** | **String**| A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the &#x60;FriendlyName&#x60; is the short code. | [optional] |
| **smsFallbackMethod** | **String**| The HTTP method that we should use to call the &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**| The URL that we should call if an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional] |
| **smsMethod** | **String**| The HTTP method we should use when calling the &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsUrl** | **URI**| The URL we should call when receiving an incoming SMS message to this short code. | [optional] |

### Return type

[**ApiV2010AccountShortCode**](ApiV2010AccountShortCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

