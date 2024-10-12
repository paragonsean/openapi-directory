# NumbersV2HostedNumberOrderApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createHostedNumberOrder**](NumbersV2HostedNumberOrderApi.md#createHostedNumberOrder) | **POST** /v2/HostedNumber/Orders |  |
| [**deleteHostedNumberOrder**](NumbersV2HostedNumberOrderApi.md#deleteHostedNumberOrder) | **DELETE** /v2/HostedNumber/Orders/{Sid} |  |
| [**fetchHostedNumberOrder**](NumbersV2HostedNumberOrderApi.md#fetchHostedNumberOrder) | **GET** /v2/HostedNumber/Orders/{Sid} |  |
| [**listHostedNumberOrder**](NumbersV2HostedNumberOrderApi.md#listHostedNumberOrder) | **GET** /v2/HostedNumber/Orders |  |


<a id="createHostedNumberOrder"></a>
# **createHostedNumberOrder**
> NumbersV2HostedNumberOrder createHostedNumberOrder(addressSid, contactPhoneNumber, email, phoneNumber, accountSid, ccEmails, contactTitle, friendlyName, smsApplicationSid, smsCapability, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallbackMethod, statusCallbackUrl)



Host a phone number&#39;s capability on Twilio&#39;s platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2HostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2HostedNumberOrderApi apiInstance = new NumbersV2HostedNumberOrderApi(defaultClient);
    String addressSid = "addressSid_example"; // String | Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
    String contactPhoneNumber = "contactPhoneNumber_example"; // String | The contact phone number of the person authorized to sign the Authorization Document.
    String email = "email_example"; // String | Optional. Email of the owner of this phone number that is being hosted.
    String phoneNumber = "phoneNumber_example"; // String | The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format
    String accountSid = "accountSid_example"; // String | This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to.
    List<String> ccEmails = Arrays.asList(); // List<String> | Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to.
    String contactTitle = "contactTitle_example"; // String | The title of the person authorized to sign the Authorization Document for this phone number.
    String friendlyName = "friendlyName_example"; // String | A 128 character string that is a human readable text that describes this resource.
    String smsApplicationSid = "smsApplicationSid_example"; // String | Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a `SmsApplicationSid` is present, Twilio will ignore all of the SMS urls above and use those set on the application.
    Boolean smsCapability = true; // Boolean | Used to specify that the SMS capability will be hosted on Twilio's platform.
    String smsFallbackMethod = "HEAD"; // String | The HTTP method that should be used to request the SmsFallbackUrl. Must be either `GET` or `POST`. This will be copied onto the IncomingPhoneNumber resource.
    URI smsFallbackUrl = new URI(); // URI | A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
    String smsMethod = "HEAD"; // String | The HTTP method that should be used to request the SmsUrl. Must be either `GET` or `POST`.  This will be copied onto the IncomingPhoneNumber resource.
    URI smsUrl = new URI(); // URI | The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource.
    String statusCallbackMethod = "HEAD"; // String | Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
    URI statusCallbackUrl = new URI(); // URI | Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
    try {
      NumbersV2HostedNumberOrder result = apiInstance.createHostedNumberOrder(addressSid, contactPhoneNumber, email, phoneNumber, accountSid, ccEmails, contactTitle, friendlyName, smsApplicationSid, smsCapability, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallbackMethod, statusCallbackUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2HostedNumberOrderApi#createHostedNumberOrder");
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
| **addressSid** | **String**| Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number. | |
| **contactPhoneNumber** | **String**| The contact phone number of the person authorized to sign the Authorization Document. | |
| **email** | **String**| Optional. Email of the owner of this phone number that is being hosted. | |
| **phoneNumber** | **String**| The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format | |
| **accountSid** | **String**| This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to. | [optional] |
| **ccEmails** | [**List&lt;String&gt;**](String.md)| Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to. | [optional] |
| **contactTitle** | **String**| The title of the person authorized to sign the Authorization Document for this phone number. | [optional] |
| **friendlyName** | **String**| A 128 character string that is a human readable text that describes this resource. | [optional] |
| **smsApplicationSid** | **String**| Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a &#x60;SmsApplicationSid&#x60; is present, Twilio will ignore all of the SMS urls above and use those set on the application. | [optional] |
| **smsCapability** | **Boolean**| Used to specify that the SMS capability will be hosted on Twilio&#39;s platform. | [optional] |
| **smsFallbackMethod** | **String**| The HTTP method that should be used to request the SmsFallbackUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;. This will be copied onto the IncomingPhoneNumber resource. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**| A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource. | [optional] |
| **smsMethod** | **String**| The HTTP method that should be used to request the SmsUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;.  This will be copied onto the IncomingPhoneNumber resource. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsUrl** | **URI**| The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource. | [optional] |
| **statusCallbackMethod** | **String**| Optional. The Status Callback Method attached to the IncomingPhoneNumber resource. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **statusCallbackUrl** | **URI**| Optional. The Status Callback URL attached to the IncomingPhoneNumber resource. | [optional] |

### Return type

[**NumbersV2HostedNumberOrder**](NumbersV2HostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteHostedNumberOrder"></a>
# **deleteHostedNumberOrder**
> deleteHostedNumberOrder(sid)



Cancel the HostedNumberOrder (only available when the status is in &#x60;received&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2HostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2HostedNumberOrderApi apiInstance = new NumbersV2HostedNumberOrderApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
    try {
      apiInstance.deleteHostedNumberOrder(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2HostedNumberOrderApi#deleteHostedNumberOrder");
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
| **sid** | **String**| A 34 character string that uniquely identifies this HostedNumberOrder. | |

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

<a id="fetchHostedNumberOrder"></a>
# **fetchHostedNumberOrder**
> NumbersV2HostedNumberOrder fetchHostedNumberOrder(sid)



Fetch a specific HostedNumberOrder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2HostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2HostedNumberOrderApi apiInstance = new NumbersV2HostedNumberOrderApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
    try {
      NumbersV2HostedNumberOrder result = apiInstance.fetchHostedNumberOrder(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2HostedNumberOrderApi#fetchHostedNumberOrder");
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
| **sid** | **String**| A 34 character string that uniquely identifies this HostedNumberOrder. | |

### Return type

[**NumbersV2HostedNumberOrder**](NumbersV2HostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listHostedNumberOrder"></a>
# **listHostedNumberOrder**
> ListHostedNumberOrderResponse listHostedNumberOrder(status, smsCapability, phoneNumber, incomingPhoneNumberSid, friendlyName, pageSize, page, pageToken)



Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2HostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2HostedNumberOrderApi apiInstance = new NumbersV2HostedNumberOrderApi(defaultClient);
    HostedNumberOrderEnumStatus status = HostedNumberOrderEnumStatus.fromValue("received"); // HostedNumberOrderEnumStatus | The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
    Boolean smsCapability = true; // Boolean | Whether the SMS capability will be hosted on our platform. Can be `true` of `false`.
    String phoneNumber = "phoneNumber_example"; // String | An E164 formatted phone number hosted by this HostedNumberOrder.
    String incomingPhoneNumberSid = "incomingPhoneNumberSid_example"; // String | A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
    String friendlyName = "friendlyName_example"; // String | A human readable description of this resource, up to 128 characters.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListHostedNumberOrderResponse result = apiInstance.listHostedNumberOrder(status, smsCapability, phoneNumber, incomingPhoneNumberSid, friendlyName, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2HostedNumberOrderApi#listHostedNumberOrder");
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
| **status** | **HostedNumberOrderEnumStatus**| The Status of this HostedNumberOrder. One of &#x60;received&#x60;, &#x60;pending-verification&#x60;, &#x60;verified&#x60;, &#x60;pending-loa&#x60;, &#x60;carrier-processing&#x60;, &#x60;testing&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, or &#x60;action-required&#x60;. | [optional] [enum: received, verified, pending-loa, carrier-processing, completed, failed, action-required] |
| **smsCapability** | **Boolean**| Whether the SMS capability will be hosted on our platform. Can be &#x60;true&#x60; of &#x60;false&#x60;. | [optional] |
| **phoneNumber** | **String**| An E164 formatted phone number hosted by this HostedNumberOrder. | [optional] |
| **incomingPhoneNumberSid** | **String**| A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder. | [optional] |
| **friendlyName** | **String**| A human readable description of this resource, up to 128 characters. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListHostedNumberOrderResponse**](ListHostedNumberOrderResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

