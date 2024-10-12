# PreviewHostedNumbersAuthorizationDocumentApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocumentApi.md#createHostedNumbersAuthorizationDocument) | **POST** /HostedNumbers/AuthorizationDocuments |  |
| [**fetchHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocumentApi.md#fetchHostedNumbersAuthorizationDocument) | **GET** /HostedNumbers/AuthorizationDocuments/{Sid} |  |
| [**listHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocumentApi.md#listHostedNumbersAuthorizationDocument) | **GET** /HostedNumbers/AuthorizationDocuments |  |
| [**updateHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocumentApi.md#updateHostedNumbersAuthorizationDocument) | **POST** /HostedNumbers/AuthorizationDocuments/{Sid} |  |


<a id="createHostedNumbersAuthorizationDocument"></a>
# **createHostedNumbersAuthorizationDocument**
> PreviewHostedNumbersAuthorizationDocument createHostedNumbersAuthorizationDocument(addressSid, contactPhoneNumber, contactTitle, email, hostedNumberOrderSids, ccEmails)



Create an AuthorizationDocument for authorizing the hosting of phone number capabilities on Twilio&#39;s platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewHostedNumbersAuthorizationDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewHostedNumbersAuthorizationDocumentApi apiInstance = new PreviewHostedNumbersAuthorizationDocumentApi(defaultClient);
    String addressSid = "addressSid_example"; // String | A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
    String contactPhoneNumber = "contactPhoneNumber_example"; // String | The contact phone number of the person authorized to sign the Authorization Document.
    String contactTitle = "contactTitle_example"; // String | The title of the person authorized to sign the Authorization Document for this phone number.
    String email = "email_example"; // String | Email that this AuthorizationDocument will be sent to for signing.
    List<String> hostedNumberOrderSids = Arrays.asList(); // List<String> | A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
    List<String> ccEmails = Arrays.asList(); // List<String> | Email recipients who will be informed when an Authorization Document has been sent and signed.
    try {
      PreviewHostedNumbersAuthorizationDocument result = apiInstance.createHostedNumbersAuthorizationDocument(addressSid, contactPhoneNumber, contactTitle, email, hostedNumberOrderSids, ccEmails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewHostedNumbersAuthorizationDocumentApi#createHostedNumbersAuthorizationDocument");
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
| **addressSid** | **String**| A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument. | |
| **contactPhoneNumber** | **String**| The contact phone number of the person authorized to sign the Authorization Document. | |
| **contactTitle** | **String**| The title of the person authorized to sign the Authorization Document for this phone number. | |
| **email** | **String**| Email that this AuthorizationDocument will be sent to for signing. | |
| **hostedNumberOrderSids** | [**List&lt;String&gt;**](String.md)| A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio&#39;s platform. | |
| **ccEmails** | [**List&lt;String&gt;**](String.md)| Email recipients who will be informed when an Authorization Document has been sent and signed. | [optional] |

### Return type

[**PreviewHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchHostedNumbersAuthorizationDocument"></a>
# **fetchHostedNumbersAuthorizationDocument**
> PreviewHostedNumbersAuthorizationDocument fetchHostedNumbersAuthorizationDocument(sid)



Fetch a specific AuthorizationDocument.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewHostedNumbersAuthorizationDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewHostedNumbersAuthorizationDocumentApi apiInstance = new PreviewHostedNumbersAuthorizationDocumentApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this AuthorizationDocument.
    try {
      PreviewHostedNumbersAuthorizationDocument result = apiInstance.fetchHostedNumbersAuthorizationDocument(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewHostedNumbersAuthorizationDocumentApi#fetchHostedNumbersAuthorizationDocument");
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
| **sid** | **String**| A 34 character string that uniquely identifies this AuthorizationDocument. | |

### Return type

[**PreviewHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listHostedNumbersAuthorizationDocument"></a>
# **listHostedNumbersAuthorizationDocument**
> ListHostedNumbersAuthorizationDocumentResponse listHostedNumbersAuthorizationDocument(email, status, pageSize, page, pageToken)



Retrieve a list of AuthorizationDocuments belonging to the account initiating the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewHostedNumbersAuthorizationDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewHostedNumbersAuthorizationDocumentApi apiInstance = new PreviewHostedNumbersAuthorizationDocumentApi(defaultClient);
    String email = "email_example"; // String | Email that this AuthorizationDocument will be sent to for signing.
    AuthorizationDocumentEnumStatus status = AuthorizationDocumentEnumStatus.fromValue("opened"); // AuthorizationDocumentEnumStatus | Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListHostedNumbersAuthorizationDocumentResponse result = apiInstance.listHostedNumbersAuthorizationDocument(email, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewHostedNumbersAuthorizationDocumentApi#listHostedNumbersAuthorizationDocument");
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
| **email** | **String**| Email that this AuthorizationDocument will be sent to for signing. | [optional] |
| **status** | **AuthorizationDocumentEnumStatus**| Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses. | [optional] [enum: opened, signing, signed, canceled, failed] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListHostedNumbersAuthorizationDocumentResponse**](ListHostedNumbersAuthorizationDocumentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateHostedNumbersAuthorizationDocument"></a>
# **updateHostedNumbersAuthorizationDocument**
> PreviewHostedNumbersAuthorizationDocument updateHostedNumbersAuthorizationDocument(sid, addressSid, ccEmails, contactPhoneNumber, contactTitle, email, hostedNumberOrderSids, status)



Updates a specific AuthorizationDocument.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewHostedNumbersAuthorizationDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewHostedNumbersAuthorizationDocumentApi apiInstance = new PreviewHostedNumbersAuthorizationDocumentApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this AuthorizationDocument.
    String addressSid = "addressSid_example"; // String | A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
    List<String> ccEmails = Arrays.asList(); // List<String> | Email recipients who will be informed when an Authorization Document has been sent and signed
    String contactPhoneNumber = "contactPhoneNumber_example"; // String | The contact phone number of the person authorized to sign the Authorization Document.
    String contactTitle = "contactTitle_example"; // String | The title of the person authorized to sign the Authorization Document for this phone number.
    String email = "email_example"; // String | Email that this AuthorizationDocument will be sent to for signing.
    List<String> hostedNumberOrderSids = Arrays.asList(); // List<String> | A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
    AuthorizationDocumentEnumStatus status = AuthorizationDocumentEnumStatus.fromValue("opened"); // AuthorizationDocumentEnumStatus | 
    try {
      PreviewHostedNumbersAuthorizationDocument result = apiInstance.updateHostedNumbersAuthorizationDocument(sid, addressSid, ccEmails, contactPhoneNumber, contactTitle, email, hostedNumberOrderSids, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewHostedNumbersAuthorizationDocumentApi#updateHostedNumbersAuthorizationDocument");
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
| **sid** | **String**| A 34 character string that uniquely identifies this AuthorizationDocument. | |
| **addressSid** | **String**| A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument. | [optional] |
| **ccEmails** | [**List&lt;String&gt;**](String.md)| Email recipients who will be informed when an Authorization Document has been sent and signed | [optional] |
| **contactPhoneNumber** | **String**| The contact phone number of the person authorized to sign the Authorization Document. | [optional] |
| **contactTitle** | **String**| The title of the person authorized to sign the Authorization Document for this phone number. | [optional] |
| **email** | **String**| Email that this AuthorizationDocument will be sent to for signing. | [optional] |
| **hostedNumberOrderSids** | [**List&lt;String&gt;**](String.md)| A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio&#39;s platform. | [optional] |
| **status** | **AuthorizationDocumentEnumStatus**|  | [optional] [enum: opened, signing, signed, canceled, failed] |

### Return type

[**PreviewHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

