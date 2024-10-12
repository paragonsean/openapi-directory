# CallerIdsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2PhoneNumbersCallerIdsJsonGet**](CallerIdsApi.md#v2PhoneNumbersCallerIdsJsonGet) | **GET** /v2/phone_numbers/caller_ids.json | List caller ids |


<a id="v2PhoneNumbersCallerIdsJsonGet"></a>
# **v2PhoneNumbersCallerIdsJsonGet**
> List&lt;CallerId&gt; v2PhoneNumbersCallerIdsJsonGet(phoneNumber)

List caller ids

Each entry is a possible caller ID match for the number. Multiple entries may be returned if the phone number is present on more than one person in the system.  Phone number should be in E.164 format. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallerIdsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CallerIdsApi apiInstance = new CallerIdsApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | E.164 Phone Number
    try {
      List<CallerId> result = apiInstance.v2PhoneNumbersCallerIdsJsonGet(phoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallerIdsApi#v2PhoneNumbersCallerIdsJsonGet");
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
| **phoneNumber** | **String**| E.164 Phone Number | |

### Return type

[**List&lt;CallerId&gt;**](CallerId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

