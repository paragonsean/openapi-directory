# LookupsV1PhoneNumberApi

All URIs are relative to *https://lookups.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchPhoneNumber**](LookupsV1PhoneNumberApi.md#fetchPhoneNumber) | **GET** /v1/PhoneNumbers/{PhoneNumber} |  |


<a id="fetchPhoneNumber"></a>
# **fetchPhoneNumber**
> LookupsV1PhoneNumber fetchPhoneNumber(phoneNumber, countryCode, type, addOns, addOnsData)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupsV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lookups.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    LookupsV1PhoneNumberApi apiInstance = new LookupsV1PhoneNumberApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | The phone number to lookup in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    String countryCode = "countryCode_example"; // String | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the phone number to fetch. This is used to specify the country when the phone number is provided in a national format.
    List<String> type = Arrays.asList(); // List<String> | The type of information to return. Can be: `carrier` or `caller-name`. The default is null.  Carrier information costs $0.005 per phone number looked up.  Caller Name information is currently available only in the US and costs $0.01 per phone number looked up.  To retrieve both types on information, specify this parameter twice; once with `carrier` and once with `caller-name` as the value.
    List<String> addOns = Arrays.asList(); // List<String> | The `unique_name` of an Add-on you would like to invoke. Can be the `unique_name` of an Add-on that is installed on your account. You can specify multiple instances of this parameter to invoke multiple Add-ons. For more information about  Add-ons, see the [Add-ons documentation](https://www.twilio.com/docs/add-ons).
    Object addOnsData = null; // Object | Data specific to the add-on you would like to invoke. The content and format of this value depends on the add-on.
    try {
      LookupsV1PhoneNumber result = apiInstance.fetchPhoneNumber(phoneNumber, countryCode, type, addOns, addOnsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsV1PhoneNumberApi#fetchPhoneNumber");
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
| **phoneNumber** | **String**| The phone number to lookup in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | |
| **countryCode** | **String**| The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the phone number to fetch. This is used to specify the country when the phone number is provided in a national format. | [optional] |
| **type** | [**List&lt;String&gt;**](String.md)| The type of information to return. Can be: &#x60;carrier&#x60; or &#x60;caller-name&#x60;. The default is null.  Carrier information costs $0.005 per phone number looked up.  Caller Name information is currently available only in the US and costs $0.01 per phone number looked up.  To retrieve both types on information, specify this parameter twice; once with &#x60;carrier&#x60; and once with &#x60;caller-name&#x60; as the value. | [optional] |
| **addOns** | [**List&lt;String&gt;**](String.md)| The &#x60;unique_name&#x60; of an Add-on you would like to invoke. Can be the &#x60;unique_name&#x60; of an Add-on that is installed on your account. You can specify multiple instances of this parameter to invoke multiple Add-ons. For more information about  Add-ons, see the [Add-ons documentation](https://www.twilio.com/docs/add-ons). | [optional] |
| **addOnsData** | [**Object**](.md)| Data specific to the add-on you would like to invoke. The content and format of this value depends on the add-on. | [optional] |

### Return type

[**LookupsV1PhoneNumber**](LookupsV1PhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

