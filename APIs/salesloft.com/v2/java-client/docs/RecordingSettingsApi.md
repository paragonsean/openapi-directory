# RecordingSettingsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2PhoneNumbersRecordingSettingsIdJsonGet**](RecordingSettingsApi.md#v2PhoneNumbersRecordingSettingsIdJsonGet) | **GET** /v2/phone_numbers/recording_settings/{id}.json | Fetch recording setting |


<a id="v2PhoneNumbersRecordingSettingsIdJsonGet"></a>
# **v2PhoneNumbersRecordingSettingsIdJsonGet**
> RecordingSetting v2PhoneNumbersRecordingSettingsIdJsonGet(id)

Fetch recording setting

Fetches the recording status for a given phone number, based on Do Not Record and Recording Governance for your team. Phone number should be in E.164 format. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordingSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    RecordingSettingsApi apiInstance = new RecordingSettingsApi(defaultClient);
    String id = "id_example"; // String | E.164 Phone Number
    try {
      RecordingSetting result = apiInstance.v2PhoneNumbersRecordingSettingsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordingSettingsApi#v2PhoneNumbersRecordingSettingsIdJsonGet");
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
| **id** | **String**| E.164 Phone Number | |

### Return type

[**RecordingSetting**](RecordingSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

