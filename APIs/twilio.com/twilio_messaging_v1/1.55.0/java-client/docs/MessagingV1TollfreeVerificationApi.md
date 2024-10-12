# MessagingV1TollfreeVerificationApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#createTollfreeVerification) | **POST** /v1/Tollfree/Verifications |  |
| [**deleteTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#deleteTollfreeVerification) | **DELETE** /v1/Tollfree/Verifications/{Sid} |  |
| [**fetchTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#fetchTollfreeVerification) | **GET** /v1/Tollfree/Verifications/{Sid} |  |
| [**listTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#listTollfreeVerification) | **GET** /v1/Tollfree/Verifications |  |
| [**updateTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#updateTollfreeVerification) | **POST** /v1/Tollfree/Verifications/{Sid} |  |


<a id="createTollfreeVerification"></a>
# **createTollfreeVerification**
> MessagingV1TollfreeVerification createTollfreeVerification(businessName, businessWebsite, messageVolume, notificationEmail, optInImageUrls, optInType, productionMessageSample, tollfreePhoneNumberSid, useCaseCategories, useCaseSummary, additionalInformation, businessCity, businessContactEmail, businessContactFirstName, businessContactLastName, businessContactPhone, businessCountry, businessPostalCode, businessStateProvinceRegion, businessStreetAddress, businessStreetAddress2, customerProfileSid, externalReferenceId)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1TollfreeVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1TollfreeVerificationApi apiInstance = new MessagingV1TollfreeVerificationApi(defaultClient);
    String businessName = "businessName_example"; // String | The name of the business or organization using the Tollfree number.
    String businessWebsite = "businessWebsite_example"; // String | The website of the business or organization using the Tollfree number.
    String messageVolume = "messageVolume_example"; // String | Estimate monthly volume of messages from the Tollfree Number.
    String notificationEmail = "notificationEmail_example"; // String | The email address to receive the notification about the verification result. .
    List<String> optInImageUrls = Arrays.asList(); // List<String> | Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
    TollfreeVerificationEnumOptInType optInType = TollfreeVerificationEnumOptInType.fromValue("VERBAL"); // TollfreeVerificationEnumOptInType | 
    String productionMessageSample = "productionMessageSample_example"; // String | An example of message content, i.e. a sample message.
    String tollfreePhoneNumberSid = "tollfreePhoneNumberSid_example"; // String | The SID of the Phone Number associated with the Tollfree Verification.
    List<String> useCaseCategories = Arrays.asList(); // List<String> | The category of the use case for the Tollfree Number. List as many are applicable..
    String useCaseSummary = "useCaseSummary_example"; // String | Use this to further explain how messaging is used by the business or organization.
    String additionalInformation = "additionalInformation_example"; // String | Additional information to be provided for verification.
    String businessCity = "businessCity_example"; // String | The city of the business or organization using the Tollfree number.
    String businessContactEmail = "businessContactEmail_example"; // String | The email address of the contact for the business or organization using the Tollfree number.
    String businessContactFirstName = "businessContactFirstName_example"; // String | The first name of the contact for the business or organization using the Tollfree number.
    String businessContactLastName = "businessContactLastName_example"; // String | The last name of the contact for the business or organization using the Tollfree number.
    String businessContactPhone = "businessContactPhone_example"; // String | The E.164 formatted phone number of the contact for the business or organization using the Tollfree number.
    String businessCountry = "businessCountry_example"; // String | The country of the business or organization using the Tollfree number.
    String businessPostalCode = "businessPostalCode_example"; // String | The postal code of the business or organization using the Tollfree number.
    String businessStateProvinceRegion = "businessStateProvinceRegion_example"; // String | The state/province/region of the business or organization using the Tollfree number.
    String businessStreetAddress = "businessStreetAddress_example"; // String | The address of the business or organization using the Tollfree number.
    String businessStreetAddress2 = "businessStreetAddress2_example"; // String | The address of the business or organization using the Tollfree number.
    String customerProfileSid = "customerProfileSid_example"; // String | Customer's Profile Bundle BundleSid.
    String externalReferenceId = "externalReferenceId_example"; // String | An optional external reference ID supplied by customer and echoed back on status retrieval.
    try {
      MessagingV1TollfreeVerification result = apiInstance.createTollfreeVerification(businessName, businessWebsite, messageVolume, notificationEmail, optInImageUrls, optInType, productionMessageSample, tollfreePhoneNumberSid, useCaseCategories, useCaseSummary, additionalInformation, businessCity, businessContactEmail, businessContactFirstName, businessContactLastName, businessContactPhone, businessCountry, businessPostalCode, businessStateProvinceRegion, businessStreetAddress, businessStreetAddress2, customerProfileSid, externalReferenceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1TollfreeVerificationApi#createTollfreeVerification");
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
| **businessName** | **String**| The name of the business or organization using the Tollfree number. | |
| **businessWebsite** | **String**| The website of the business or organization using the Tollfree number. | |
| **messageVolume** | **String**| Estimate monthly volume of messages from the Tollfree Number. | |
| **notificationEmail** | **String**| The email address to receive the notification about the verification result. . | |
| **optInImageUrls** | [**List&lt;String&gt;**](String.md)| Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL. | |
| **optInType** | **TollfreeVerificationEnumOptInType**|  | [enum: VERBAL, WEB_FORM, PAPER_FORM, VIA_TEXT, MOBILE_QR_CODE] |
| **productionMessageSample** | **String**| An example of message content, i.e. a sample message. | |
| **tollfreePhoneNumberSid** | **String**| The SID of the Phone Number associated with the Tollfree Verification. | |
| **useCaseCategories** | [**List&lt;String&gt;**](String.md)| The category of the use case for the Tollfree Number. List as many are applicable.. | |
| **useCaseSummary** | **String**| Use this to further explain how messaging is used by the business or organization. | |
| **additionalInformation** | **String**| Additional information to be provided for verification. | [optional] |
| **businessCity** | **String**| The city of the business or organization using the Tollfree number. | [optional] |
| **businessContactEmail** | **String**| The email address of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessContactFirstName** | **String**| The first name of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessContactLastName** | **String**| The last name of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessContactPhone** | **String**| The E.164 formatted phone number of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessCountry** | **String**| The country of the business or organization using the Tollfree number. | [optional] |
| **businessPostalCode** | **String**| The postal code of the business or organization using the Tollfree number. | [optional] |
| **businessStateProvinceRegion** | **String**| The state/province/region of the business or organization using the Tollfree number. | [optional] |
| **businessStreetAddress** | **String**| The address of the business or organization using the Tollfree number. | [optional] |
| **businessStreetAddress2** | **String**| The address of the business or organization using the Tollfree number. | [optional] |
| **customerProfileSid** | **String**| Customer&#39;s Profile Bundle BundleSid. | [optional] |
| **externalReferenceId** | **String**| An optional external reference ID supplied by customer and echoed back on status retrieval. | [optional] |

### Return type

[**MessagingV1TollfreeVerification**](MessagingV1TollfreeVerification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteTollfreeVerification"></a>
# **deleteTollfreeVerification**
> deleteTollfreeVerification(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1TollfreeVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1TollfreeVerificationApi apiInstance = new MessagingV1TollfreeVerificationApi(defaultClient);
    String sid = "sid_example"; // String | The unique string to identify Tollfree Verification.
    try {
      apiInstance.deleteTollfreeVerification(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1TollfreeVerificationApi#deleteTollfreeVerification");
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
| **sid** | **String**| The unique string to identify Tollfree Verification. | |

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

<a id="fetchTollfreeVerification"></a>
# **fetchTollfreeVerification**
> MessagingV1TollfreeVerification fetchTollfreeVerification(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1TollfreeVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1TollfreeVerificationApi apiInstance = new MessagingV1TollfreeVerificationApi(defaultClient);
    String sid = "sid_example"; // String | The unique string to identify Tollfree Verification.
    try {
      MessagingV1TollfreeVerification result = apiInstance.fetchTollfreeVerification(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1TollfreeVerificationApi#fetchTollfreeVerification");
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
| **sid** | **String**| The unique string to identify Tollfree Verification. | |

### Return type

[**MessagingV1TollfreeVerification**](MessagingV1TollfreeVerification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTollfreeVerification"></a>
# **listTollfreeVerification**
> ListTollfreeVerificationResponse listTollfreeVerification(tollfreePhoneNumberSid, status, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1TollfreeVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1TollfreeVerificationApi apiInstance = new MessagingV1TollfreeVerificationApi(defaultClient);
    String tollfreePhoneNumberSid = "tollfreePhoneNumberSid_example"; // String | The SID of the Phone Number associated with the Tollfree Verification.
    TollfreeVerificationEnumStatus status = TollfreeVerificationEnumStatus.fromValue("PENDING_REVIEW"); // TollfreeVerificationEnumStatus | The compliance status of the Tollfree Verification record.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTollfreeVerificationResponse result = apiInstance.listTollfreeVerification(tollfreePhoneNumberSid, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1TollfreeVerificationApi#listTollfreeVerification");
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
| **tollfreePhoneNumberSid** | **String**| The SID of the Phone Number associated with the Tollfree Verification. | [optional] |
| **status** | **TollfreeVerificationEnumStatus**| The compliance status of the Tollfree Verification record. | [optional] [enum: PENDING_REVIEW, IN_REVIEW, TWILIO_APPROVED, TWILIO_REJECTED] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTollfreeVerificationResponse**](ListTollfreeVerificationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTollfreeVerification"></a>
# **updateTollfreeVerification**
> MessagingV1TollfreeVerification updateTollfreeVerification(sid, additionalInformation, businessCity, businessContactEmail, businessContactFirstName, businessContactLastName, businessContactPhone, businessCountry, businessName, businessPostalCode, businessStateProvinceRegion, businessStreetAddress, businessStreetAddress2, businessWebsite, editReason, messageVolume, notificationEmail, optInImageUrls, optInType, productionMessageSample, useCaseCategories, useCaseSummary)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1TollfreeVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1TollfreeVerificationApi apiInstance = new MessagingV1TollfreeVerificationApi(defaultClient);
    String sid = "sid_example"; // String | The unique string to identify Tollfree Verification.
    String additionalInformation = "additionalInformation_example"; // String | Additional information to be provided for verification.
    String businessCity = "businessCity_example"; // String | The city of the business or organization using the Tollfree number.
    String businessContactEmail = "businessContactEmail_example"; // String | The email address of the contact for the business or organization using the Tollfree number.
    String businessContactFirstName = "businessContactFirstName_example"; // String | The first name of the contact for the business or organization using the Tollfree number.
    String businessContactLastName = "businessContactLastName_example"; // String | The last name of the contact for the business or organization using the Tollfree number.
    String businessContactPhone = "businessContactPhone_example"; // String | The E.164 formatted phone number of the contact for the business or organization using the Tollfree number.
    String businessCountry = "businessCountry_example"; // String | The country of the business or organization using the Tollfree number.
    String businessName = "businessName_example"; // String | The name of the business or organization using the Tollfree number.
    String businessPostalCode = "businessPostalCode_example"; // String | The postal code of the business or organization using the Tollfree number.
    String businessStateProvinceRegion = "businessStateProvinceRegion_example"; // String | The state/province/region of the business or organization using the Tollfree number.
    String businessStreetAddress = "businessStreetAddress_example"; // String | The address of the business or organization using the Tollfree number.
    String businessStreetAddress2 = "businessStreetAddress2_example"; // String | The address of the business or organization using the Tollfree number.
    String businessWebsite = "businessWebsite_example"; // String | The website of the business or organization using the Tollfree number.
    String editReason = "editReason_example"; // String | Describe why the verification is being edited. If the verification was rejected because of a technical issue, such as the website being down, and the issue has been resolved this parameter should be set to something similar to 'Website fixed'.
    String messageVolume = "messageVolume_example"; // String | Estimate monthly volume of messages from the Tollfree Number.
    String notificationEmail = "notificationEmail_example"; // String | The email address to receive the notification about the verification result. .
    List<String> optInImageUrls = Arrays.asList(); // List<String> | Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
    TollfreeVerificationEnumOptInType optInType = TollfreeVerificationEnumOptInType.fromValue("VERBAL"); // TollfreeVerificationEnumOptInType | 
    String productionMessageSample = "productionMessageSample_example"; // String | An example of message content, i.e. a sample message.
    List<String> useCaseCategories = Arrays.asList(); // List<String> | The category of the use case for the Tollfree Number. List as many are applicable..
    String useCaseSummary = "useCaseSummary_example"; // String | Use this to further explain how messaging is used by the business or organization.
    try {
      MessagingV1TollfreeVerification result = apiInstance.updateTollfreeVerification(sid, additionalInformation, businessCity, businessContactEmail, businessContactFirstName, businessContactLastName, businessContactPhone, businessCountry, businessName, businessPostalCode, businessStateProvinceRegion, businessStreetAddress, businessStreetAddress2, businessWebsite, editReason, messageVolume, notificationEmail, optInImageUrls, optInType, productionMessageSample, useCaseCategories, useCaseSummary);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1TollfreeVerificationApi#updateTollfreeVerification");
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
| **sid** | **String**| The unique string to identify Tollfree Verification. | |
| **additionalInformation** | **String**| Additional information to be provided for verification. | [optional] |
| **businessCity** | **String**| The city of the business or organization using the Tollfree number. | [optional] |
| **businessContactEmail** | **String**| The email address of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessContactFirstName** | **String**| The first name of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessContactLastName** | **String**| The last name of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessContactPhone** | **String**| The E.164 formatted phone number of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessCountry** | **String**| The country of the business or organization using the Tollfree number. | [optional] |
| **businessName** | **String**| The name of the business or organization using the Tollfree number. | [optional] |
| **businessPostalCode** | **String**| The postal code of the business or organization using the Tollfree number. | [optional] |
| **businessStateProvinceRegion** | **String**| The state/province/region of the business or organization using the Tollfree number. | [optional] |
| **businessStreetAddress** | **String**| The address of the business or organization using the Tollfree number. | [optional] |
| **businessStreetAddress2** | **String**| The address of the business or organization using the Tollfree number. | [optional] |
| **businessWebsite** | **String**| The website of the business or organization using the Tollfree number. | [optional] |
| **editReason** | **String**| Describe why the verification is being edited. If the verification was rejected because of a technical issue, such as the website being down, and the issue has been resolved this parameter should be set to something similar to &#39;Website fixed&#39;. | [optional] |
| **messageVolume** | **String**| Estimate monthly volume of messages from the Tollfree Number. | [optional] |
| **notificationEmail** | **String**| The email address to receive the notification about the verification result. . | [optional] |
| **optInImageUrls** | [**List&lt;String&gt;**](String.md)| Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL. | [optional] |
| **optInType** | **TollfreeVerificationEnumOptInType**|  | [optional] [enum: VERBAL, WEB_FORM, PAPER_FORM, VIA_TEXT, MOBILE_QR_CODE] |
| **productionMessageSample** | **String**| An example of message content, i.e. a sample message. | [optional] |
| **useCaseCategories** | [**List&lt;String&gt;**](String.md)| The category of the use case for the Tollfree Number. List as many are applicable.. | [optional] |
| **useCaseSummary** | **String**| Use this to further explain how messaging is used by the business or organization. | [optional] |

### Return type

[**MessagingV1TollfreeVerification**](MessagingV1TollfreeVerification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

