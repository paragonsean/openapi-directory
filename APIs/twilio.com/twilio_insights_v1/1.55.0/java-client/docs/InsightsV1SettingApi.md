# InsightsV1SettingApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAccountSettings**](InsightsV1SettingApi.md#fetchAccountSettings) | **GET** /v1/Voice/Settings |  |
| [**updateAccountSettings**](InsightsV1SettingApi.md#updateAccountSettings) | **POST** /v1/Voice/Settings |  |


<a id="fetchAccountSettings"></a>
# **fetchAccountSettings**
> InsightsV1AccountSettings fetchAccountSettings(subaccountSid)



Get the Voice Insights Settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1SettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1SettingApi apiInstance = new InsightsV1SettingApi(defaultClient);
    String subaccountSid = "subaccountSid_example"; // String | The unique SID identifier of the Subaccount.
    try {
      InsightsV1AccountSettings result = apiInstance.fetchAccountSettings(subaccountSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1SettingApi#fetchAccountSettings");
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
| **subaccountSid** | **String**| The unique SID identifier of the Subaccount. | [optional] |

### Return type

[**InsightsV1AccountSettings**](InsightsV1AccountSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateAccountSettings"></a>
# **updateAccountSettings**
> InsightsV1AccountSettings updateAccountSettings(advancedFeatures, subaccountSid, voiceTrace)



Update a specific Voice Insights Setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1SettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1SettingApi apiInstance = new InsightsV1SettingApi(defaultClient);
    Boolean advancedFeatures = true; // Boolean | A boolean flag to enable Advanced Features for Voice Insights.
    String subaccountSid = "subaccountSid_example"; // String | The unique SID identifier of the Subaccount.
    Boolean voiceTrace = true; // Boolean | A boolean flag to enable Voice Trace.
    try {
      InsightsV1AccountSettings result = apiInstance.updateAccountSettings(advancedFeatures, subaccountSid, voiceTrace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1SettingApi#updateAccountSettings");
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
| **advancedFeatures** | **Boolean**| A boolean flag to enable Advanced Features for Voice Insights. | [optional] |
| **subaccountSid** | **String**| The unique SID identifier of the Subaccount. | [optional] |
| **voiceTrace** | **Boolean**| A boolean flag to enable Voice Trace. | [optional] |

### Return type

[**InsightsV1AccountSettings**](InsightsV1AccountSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

