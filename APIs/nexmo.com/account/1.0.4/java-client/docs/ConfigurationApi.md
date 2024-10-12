# ConfigurationApi

All URIs are relative to *https://api.nexmo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeAccountSettings**](ConfigurationApi.md#changeAccountSettings) | **POST** /account/settings | Change Account Settings |
| [**registerSender**](ConfigurationApi.md#registerSender) | **POST** /account/register-sender | Register an email sender |


<a id="changeAccountSettings"></a>
# **changeAccountSettings**
> AccountSettings changeAccountSettings(apiKey, apiSecret, drCallBackUrl, moCallBackUrl)

Change Account Settings

Update the default webhook URLs associated with your account:   * Callback URL for incoming SMS messages   * Callback URL for delivery receipts  Note that the URLs you provide must be valid and active. Vonage will check that they return a 200 OK response before the setting is saved.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String apiKey = "abcd1234"; // String | Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
    String apiSecret = "ABCDEFGH01234abc"; // String | Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
    String drCallBackUrl = "drCallBackUrl_example"; // String | The webhook URL that Vonage makes a request to when a delivery receipt is available  for an SMS sent by one of your Vonage numbers. Send an empty string to unset this value.
    String moCallBackUrl = "moCallBackUrl_example"; // String | The default webhook URL for inbound SMS. If an SMS is received at a Vonage number  that does not have its own inbound SMS webhook configured, Vonage makes a request here. Send an empty string to unset this value.
    try {
      AccountSettings result = apiInstance.changeAccountSettings(apiKey, apiSecret, drCallBackUrl, moCallBackUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#changeAccountSettings");
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
| **apiKey** | **String**| Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com) | |
| **apiSecret** | **String**| Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com) | |
| **drCallBackUrl** | **String**| The webhook URL that Vonage makes a request to when a delivery receipt is available  for an SMS sent by one of your Vonage numbers. Send an empty string to unset this value. | [optional] |
| **moCallBackUrl** | **String**| The default webhook URL for inbound SMS. If an SMS is received at a Vonage number  that does not have its own inbound SMS webhook configured, Vonage makes a request here. Send an empty string to unset this value. | [optional] |

### Return type

[**AccountSettings**](AccountSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Settings were updated if supplied, the details of the current settings are included in the response. |  -  |
| **401** | Not Authorised. You must supply your &#x60;api_key&#x60; and &#x60;api_secret&#x60; as query parameters to this request |  -  |

<a id="registerSender"></a>
# **registerSender**
> RegisterEmailResponse registerSender(apiKey, apiSecret, registerEmailRequest)

Register an email sender

Register an email sender with an API Key for using email with Verify V2.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String apiKey = "abcd1234"; // String | Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
    String apiSecret = "ABCDEFGH01234abc"; // String | Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
    RegisterEmailRequest registerEmailRequest = new RegisterEmailRequest(); // RegisterEmailRequest | 
    try {
      RegisterEmailResponse result = apiInstance.registerSender(apiKey, apiSecret, registerEmailRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#registerSender");
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
| **apiKey** | **String**| Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com) | |
| **apiSecret** | **String**| Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com) | |
| **registerEmailRequest** | [**RegisterEmailRequest**](RegisterEmailRequest.md)|  | |

### Return type

[**RegisterEmailResponse**](RegisterEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

