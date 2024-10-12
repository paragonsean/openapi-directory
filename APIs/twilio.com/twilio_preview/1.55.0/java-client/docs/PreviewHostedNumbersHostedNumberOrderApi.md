# PreviewHostedNumbersHostedNumberOrderApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#createHostedNumbersHostedNumberOrder) | **POST** /HostedNumbers/HostedNumberOrders |  |
| [**deleteHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#deleteHostedNumbersHostedNumberOrder) | **DELETE** /HostedNumbers/HostedNumberOrders/{Sid} |  |
| [**fetchHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#fetchHostedNumbersHostedNumberOrder) | **GET** /HostedNumbers/HostedNumberOrders/{Sid} |  |
| [**listHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#listHostedNumbersHostedNumberOrder) | **GET** /HostedNumbers/HostedNumberOrders |  |
| [**updateHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#updateHostedNumbersHostedNumberOrder) | **POST** /HostedNumbers/HostedNumberOrders/{Sid} |  |


<a id="createHostedNumbersHostedNumberOrder"></a>
# **createHostedNumbersHostedNumberOrder**
> PreviewHostedNumbersHostedNumberOrder createHostedNumbersHostedNumberOrder(phoneNumber, smsCapability, accountSid, addressSid, ccEmails, email, friendlyName, smsApplicationSid, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallbackMethod, statusCallbackUrl, uniqueName, verificationDocumentSid, verificationType)



Host a phone number&#39;s capability on Twilio&#39;s platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewHostedNumbersHostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewHostedNumbersHostedNumberOrderApi apiInstance = new PreviewHostedNumbersHostedNumberOrderApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format
    Boolean smsCapability = true; // Boolean | Used to specify that the SMS capability will be hosted on Twilio's platform.
    String accountSid = "accountSid_example"; // String | This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to.
    String addressSid = "addressSid_example"; // String | Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
    List<String> ccEmails = Arrays.asList(); // List<String> | Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to.
    String email = "email_example"; // String | Optional. Email of the owner of this phone number that is being hosted.
    String friendlyName = "friendlyName_example"; // String | A 64 character string that is a human readable text that describes this resource.
    String smsApplicationSid = "smsApplicationSid_example"; // String | Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a `SmsApplicationSid` is present, Twilio will ignore all of the SMS urls above and use those set on the application.
    String smsFallbackMethod = "HEAD"; // String | The HTTP method that should be used to request the SmsFallbackUrl. Must be either `GET` or `POST`. This will be copied onto the IncomingPhoneNumber resource.
    URI smsFallbackUrl = new URI(); // URI | A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
    String smsMethod = "HEAD"; // String | The HTTP method that should be used to request the SmsUrl. Must be either `GET` or `POST`.  This will be copied onto the IncomingPhoneNumber resource.
    URI smsUrl = new URI(); // URI | The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource.
    String statusCallbackMethod = "HEAD"; // String | Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
    URI statusCallbackUrl = new URI(); // URI | Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
    String uniqueName = "uniqueName_example"; // String | Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
    String verificationDocumentSid = "verificationDocumentSid_example"; // String | Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill.
    HostedNumberOrderEnumVerificationType verificationType = HostedNumberOrderEnumVerificationType.fromValue("phone-call"); // HostedNumberOrderEnumVerificationType | 
    try {
      PreviewHostedNumbersHostedNumberOrder result = apiInstance.createHostedNumbersHostedNumberOrder(phoneNumber, smsCapability, accountSid, addressSid, ccEmails, email, friendlyName, smsApplicationSid, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallbackMethod, statusCallbackUrl, uniqueName, verificationDocumentSid, verificationType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewHostedNumbersHostedNumberOrderApi#createHostedNumbersHostedNumberOrder");
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
| **phoneNumber** | **String**| The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format | |
| **smsCapability** | **Boolean**| Used to specify that the SMS capability will be hosted on Twilio&#39;s platform. | |
| **accountSid** | **String**| This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to. | [optional] |
| **addressSid** | **String**| Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number. | [optional] |
| **ccEmails** | [**List&lt;String&gt;**](String.md)| Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to. | [optional] |
| **email** | **String**| Optional. Email of the owner of this phone number that is being hosted. | [optional] |
| **friendlyName** | **String**| A 64 character string that is a human readable text that describes this resource. | [optional] |
| **smsApplicationSid** | **String**| Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a &#x60;SmsApplicationSid&#x60; is present, Twilio will ignore all of the SMS urls above and use those set on the application. | [optional] |
| **smsFallbackMethod** | **String**| The HTTP method that should be used to request the SmsFallbackUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;. This will be copied onto the IncomingPhoneNumber resource. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**| A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource. | [optional] |
| **smsMethod** | **String**| The HTTP method that should be used to request the SmsUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;.  This will be copied onto the IncomingPhoneNumber resource. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsUrl** | **URI**| The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource. | [optional] |
| **statusCallbackMethod** | **String**| Optional. The Status Callback Method attached to the IncomingPhoneNumber resource. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **statusCallbackUrl** | **URI**| Optional. The Status Callback URL attached to the IncomingPhoneNumber resource. | [optional] |
| **uniqueName** | **String**| Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID. | [optional] |
| **verificationDocumentSid** | **String**| Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill. | [optional] |
| **verificationType** | **HostedNumberOrderEnumVerificationType**|  | [optional] [enum: phone-call, phone-bill] |

### Return type

[**PreviewHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteHostedNumbersHostedNumberOrder"></a>
# **deleteHostedNumbersHostedNumberOrder**
> deleteHostedNumbersHostedNumberOrder(sid)



Cancel the HostedNumberOrder (only available when the status is in &#x60;received&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewHostedNumbersHostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewHostedNumbersHostedNumberOrderApi apiInstance = new PreviewHostedNumbersHostedNumberOrderApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
    try {
      apiInstance.deleteHostedNumbersHostedNumberOrder(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewHostedNumbersHostedNumberOrderApi#deleteHostedNumbersHostedNumberOrder");
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

<a id="fetchHostedNumbersHostedNumberOrder"></a>
# **fetchHostedNumbersHostedNumberOrder**
> PreviewHostedNumbersHostedNumberOrder fetchHostedNumbersHostedNumberOrder(sid)



Fetch a specific HostedNumberOrder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewHostedNumbersHostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewHostedNumbersHostedNumberOrderApi apiInstance = new PreviewHostedNumbersHostedNumberOrderApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
    try {
      PreviewHostedNumbersHostedNumberOrder result = apiInstance.fetchHostedNumbersHostedNumberOrder(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewHostedNumbersHostedNumberOrderApi#fetchHostedNumbersHostedNumberOrder");
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

[**PreviewHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listHostedNumbersHostedNumberOrder"></a>
# **listHostedNumbersHostedNumberOrder**
> ListHostedNumbersHostedNumberOrderResponse listHostedNumbersHostedNumberOrder(status, phoneNumber, incomingPhoneNumberSid, friendlyName, uniqueName, pageSize, page, pageToken)



Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewHostedNumbersHostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewHostedNumbersHostedNumberOrderApi apiInstance = new PreviewHostedNumbersHostedNumberOrderApi(defaultClient);
    HostedNumberOrderEnumStatus status = HostedNumberOrderEnumStatus.fromValue("received"); // HostedNumberOrderEnumStatus | The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
    String phoneNumber = "phoneNumber_example"; // String | An E164 formatted phone number hosted by this HostedNumberOrder.
    String incomingPhoneNumberSid = "incomingPhoneNumberSid_example"; // String | A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
    String friendlyName = "friendlyName_example"; // String | A human readable description of this resource, up to 64 characters.
    String uniqueName = "uniqueName_example"; // String | Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListHostedNumbersHostedNumberOrderResponse result = apiInstance.listHostedNumbersHostedNumberOrder(status, phoneNumber, incomingPhoneNumberSid, friendlyName, uniqueName, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewHostedNumbersHostedNumberOrderApi#listHostedNumbersHostedNumberOrder");
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
| **status** | **HostedNumberOrderEnumStatus**| The Status of this HostedNumberOrder. One of &#x60;received&#x60;, &#x60;pending-verification&#x60;, &#x60;verified&#x60;, &#x60;pending-loa&#x60;, &#x60;carrier-processing&#x60;, &#x60;testing&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, or &#x60;action-required&#x60;. | [optional] [enum: received, pending-verification, verified, pending-loa, carrier-processing, testing, completed, failed, action-required] |
| **phoneNumber** | **String**| An E164 formatted phone number hosted by this HostedNumberOrder. | [optional] |
| **incomingPhoneNumberSid** | **String**| A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder. | [optional] |
| **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] |
| **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListHostedNumbersHostedNumberOrderResponse**](ListHostedNumbersHostedNumberOrderResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateHostedNumbersHostedNumberOrder"></a>
# **updateHostedNumbersHostedNumberOrder**
> PreviewHostedNumbersHostedNumberOrder updateHostedNumbersHostedNumberOrder(sid, callDelay, ccEmails, email, extension, friendlyName, status, uniqueName, verificationCode, verificationDocumentSid, verificationType)



Updates a specific HostedNumberOrder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewHostedNumbersHostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewHostedNumbersHostedNumberOrderApi apiInstance = new PreviewHostedNumbersHostedNumberOrderApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
    Integer callDelay = 56; // Integer | The number of seconds, between 0 and 60, to delay before initiating the verification call. Defaults to 0.
    List<String> ccEmails = Arrays.asList(); // List<String> | Optional. A list of emails that LOA document for this HostedNumberOrder will be carbon copied to.
    String email = "email_example"; // String | Email of the owner of this phone number that is being hosted.
    String extension = "extension_example"; // String | Digits to dial after connecting the verification call.
    String friendlyName = "friendlyName_example"; // String | A 64 character string that is a human readable text that describes this resource.
    HostedNumberOrderEnumStatus status = HostedNumberOrderEnumStatus.fromValue("received"); // HostedNumberOrderEnumStatus | 
    String uniqueName = "uniqueName_example"; // String | Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
    String verificationCode = "verificationCode_example"; // String | A verification code that is given to the user via a phone call to the phone number that is being hosted.
    String verificationDocumentSid = "verificationDocumentSid_example"; // String | Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill.
    HostedNumberOrderEnumVerificationType verificationType = HostedNumberOrderEnumVerificationType.fromValue("phone-call"); // HostedNumberOrderEnumVerificationType | 
    try {
      PreviewHostedNumbersHostedNumberOrder result = apiInstance.updateHostedNumbersHostedNumberOrder(sid, callDelay, ccEmails, email, extension, friendlyName, status, uniqueName, verificationCode, verificationDocumentSid, verificationType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewHostedNumbersHostedNumberOrderApi#updateHostedNumbersHostedNumberOrder");
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
| **callDelay** | **Integer**| The number of seconds, between 0 and 60, to delay before initiating the verification call. Defaults to 0. | [optional] |
| **ccEmails** | [**List&lt;String&gt;**](String.md)| Optional. A list of emails that LOA document for this HostedNumberOrder will be carbon copied to. | [optional] |
| **email** | **String**| Email of the owner of this phone number that is being hosted. | [optional] |
| **extension** | **String**| Digits to dial after connecting the verification call. | [optional] |
| **friendlyName** | **String**| A 64 character string that is a human readable text that describes this resource. | [optional] |
| **status** | **HostedNumberOrderEnumStatus**|  | [optional] [enum: received, pending-verification, verified, pending-loa, carrier-processing, testing, completed, failed, action-required] |
| **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID. | [optional] |
| **verificationCode** | **String**| A verification code that is given to the user via a phone call to the phone number that is being hosted. | [optional] |
| **verificationDocumentSid** | **String**| Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill. | [optional] |
| **verificationType** | **HostedNumberOrderEnumVerificationType**|  | [optional] [enum: phone-call, phone-bill] |

### Return type

[**PreviewHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

