# NumbersV2AuthorizationDocumentApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAuthorizationDocument**](NumbersV2AuthorizationDocumentApi.md#createAuthorizationDocument) | **POST** /v2/HostedNumber/AuthorizationDocuments |  |
| [**deleteAuthorizationDocument**](NumbersV2AuthorizationDocumentApi.md#deleteAuthorizationDocument) | **DELETE** /v2/HostedNumber/AuthorizationDocuments/{Sid} |  |
| [**fetchAuthorizationDocument**](NumbersV2AuthorizationDocumentApi.md#fetchAuthorizationDocument) | **GET** /v2/HostedNumber/AuthorizationDocuments/{Sid} |  |
| [**listAuthorizationDocument**](NumbersV2AuthorizationDocumentApi.md#listAuthorizationDocument) | **GET** /v2/HostedNumber/AuthorizationDocuments |  |


<a id="createAuthorizationDocument"></a>
# **createAuthorizationDocument**
> NumbersV2AuthorizationDocument createAuthorizationDocument(addressSid, contactPhoneNumber, email, hostedNumberOrderSids, ccEmails, contactTitle)



Create an AuthorizationDocument for authorizing the hosting of phone number capabilities on Twilio&#39;s platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2AuthorizationDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2AuthorizationDocumentApi apiInstance = new NumbersV2AuthorizationDocumentApi(defaultClient);
    String addressSid = "addressSid_example"; // String | A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
    String contactPhoneNumber = "contactPhoneNumber_example"; // String | The contact phone number of the person authorized to sign the Authorization Document.
    String email = "email_example"; // String | Email that this AuthorizationDocument will be sent to for signing.
    List<String> hostedNumberOrderSids = Arrays.asList(); // List<String> | A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
    List<String> ccEmails = Arrays.asList(); // List<String> | Email recipients who will be informed when an Authorization Document has been sent and signed.
    String contactTitle = "contactTitle_example"; // String | The title of the person authorized to sign the Authorization Document for this phone number.
    try {
      NumbersV2AuthorizationDocument result = apiInstance.createAuthorizationDocument(addressSid, contactPhoneNumber, email, hostedNumberOrderSids, ccEmails, contactTitle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2AuthorizationDocumentApi#createAuthorizationDocument");
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
| **email** | **String**| Email that this AuthorizationDocument will be sent to for signing. | |
| **hostedNumberOrderSids** | [**List&lt;String&gt;**](String.md)| A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio&#39;s platform. | |
| **ccEmails** | [**List&lt;String&gt;**](String.md)| Email recipients who will be informed when an Authorization Document has been sent and signed. | [optional] |
| **contactTitle** | **String**| The title of the person authorized to sign the Authorization Document for this phone number. | [optional] |

### Return type

[**NumbersV2AuthorizationDocument**](NumbersV2AuthorizationDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteAuthorizationDocument"></a>
# **deleteAuthorizationDocument**
> deleteAuthorizationDocument(sid)



Cancel the AuthorizationDocument request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2AuthorizationDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2AuthorizationDocumentApi apiInstance = new NumbersV2AuthorizationDocumentApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this AuthorizationDocument.
    try {
      apiInstance.deleteAuthorizationDocument(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2AuthorizationDocumentApi#deleteAuthorizationDocument");
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

<a id="fetchAuthorizationDocument"></a>
# **fetchAuthorizationDocument**
> NumbersV2AuthorizationDocument fetchAuthorizationDocument(sid)



Fetch a specific AuthorizationDocument.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2AuthorizationDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2AuthorizationDocumentApi apiInstance = new NumbersV2AuthorizationDocumentApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this AuthorizationDocument.
    try {
      NumbersV2AuthorizationDocument result = apiInstance.fetchAuthorizationDocument(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2AuthorizationDocumentApi#fetchAuthorizationDocument");
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

[**NumbersV2AuthorizationDocument**](NumbersV2AuthorizationDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAuthorizationDocument"></a>
# **listAuthorizationDocument**
> ListAuthorizationDocumentResponse listAuthorizationDocument(email, status, pageSize, page, pageToken)



Retrieve a list of AuthorizationDocuments belonging to the account initiating the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2AuthorizationDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2AuthorizationDocumentApi apiInstance = new NumbersV2AuthorizationDocumentApi(defaultClient);
    String email = "email_example"; // String | Email that this AuthorizationDocument will be sent to for signing.
    AuthorizationDocumentEnumStatus status = AuthorizationDocumentEnumStatus.fromValue("opened"); // AuthorizationDocumentEnumStatus | Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListAuthorizationDocumentResponse result = apiInstance.listAuthorizationDocument(email, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2AuthorizationDocumentApi#listAuthorizationDocument");
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

[**ListAuthorizationDocumentResponse**](ListAuthorizationDocumentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

