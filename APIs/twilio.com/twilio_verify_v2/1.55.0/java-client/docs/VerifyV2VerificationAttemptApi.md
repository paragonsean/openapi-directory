# VerifyV2VerificationAttemptApi

All URIs are relative to *https://verify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchVerificationAttempt**](VerifyV2VerificationAttemptApi.md#fetchVerificationAttempt) | **GET** /v2/Attempts/{Sid} |  |
| [**listVerificationAttempt**](VerifyV2VerificationAttemptApi.md#listVerificationAttempt) | **GET** /v2/Attempts |  |


<a id="fetchVerificationAttempt"></a>
# **fetchVerificationAttempt**
> VerifyV2VerificationAttempt fetchVerificationAttempt(sid)



Fetch a specific verification attempt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2VerificationAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2VerificationAttemptApi apiInstance = new VerifyV2VerificationAttemptApi(defaultClient);
    String sid = "sid_example"; // String | The unique SID identifier of a Verification Attempt
    try {
      VerifyV2VerificationAttempt result = apiInstance.fetchVerificationAttempt(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2VerificationAttemptApi#fetchVerificationAttempt");
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
| **sid** | **String**| The unique SID identifier of a Verification Attempt | |

### Return type

[**VerifyV2VerificationAttempt**](VerifyV2VerificationAttempt.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listVerificationAttempt"></a>
# **listVerificationAttempt**
> ListVerificationAttemptResponse listVerificationAttempt(dateCreatedAfter, dateCreatedBefore, channelDataTo, country, channel, verifyServiceSid, verificationSid, status, pageSize, page, pageToken)



List all the verification attempts for a given Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2VerificationAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2VerificationAttemptApi apiInstance = new VerifyV2VerificationAttemptApi(defaultClient);
    OffsetDateTime dateCreatedAfter = OffsetDateTime.now(); // OffsetDateTime | Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
    OffsetDateTime dateCreatedBefore = OffsetDateTime.now(); // OffsetDateTime | Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
    String channelDataTo = "channelDataTo_example"; // String | Destination of a verification. It is phone number in E.164 format.
    String country = "country_example"; // String | Filter used to query Verification Attempts sent to the specified destination country.
    VerificationAttemptEnumChannels channel = VerificationAttemptEnumChannels.fromValue("sms"); // VerificationAttemptEnumChannels | Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
    String verifyServiceSid = "verifyServiceSid_example"; // String | Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
    String verificationSid = "verificationSid_example"; // String | Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
    VerificationAttemptEnumConversionStatus status = VerificationAttemptEnumConversionStatus.fromValue("converted"); // VerificationAttemptEnumConversionStatus | Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListVerificationAttemptResponse result = apiInstance.listVerificationAttempt(dateCreatedAfter, dateCreatedBefore, channelDataTo, country, channel, verifyServiceSid, verificationSid, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2VerificationAttemptApi#listVerificationAttempt");
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
| **dateCreatedAfter** | **OffsetDateTime**| Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z. | [optional] |
| **dateCreatedBefore** | **OffsetDateTime**| Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z. | [optional] |
| **channelDataTo** | **String**| Destination of a verification. It is phone number in E.164 format. | [optional] |
| **country** | **String**| Filter used to query Verification Attempts sent to the specified destination country. | [optional] |
| **channel** | **VerificationAttemptEnumChannels**| Filter used to query Verification Attempts by communication channel. Valid values are &#x60;SMS&#x60; and &#x60;CALL&#x60; | [optional] [enum: sms, call, email, whatsapp] |
| **verifyServiceSid** | **String**| Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned. | [optional] |
| **verificationSid** | **String**| Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned. | [optional] |
| **status** | **VerificationAttemptEnumConversionStatus**| Filter used to query Verification Attempts by conversion status. Valid values are &#x60;UNCONVERTED&#x60;, for attempts that were not converted, and &#x60;CONVERTED&#x60;, for attempts that were confirmed. | [optional] [enum: converted, unconverted] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListVerificationAttemptResponse**](ListVerificationAttemptResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

