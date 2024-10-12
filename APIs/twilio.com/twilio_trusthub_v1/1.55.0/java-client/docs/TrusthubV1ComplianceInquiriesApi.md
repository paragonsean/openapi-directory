# TrusthubV1ComplianceInquiriesApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createComplianceInquiry**](TrusthubV1ComplianceInquiriesApi.md#createComplianceInquiry) | **POST** /v1/ComplianceInquiries/Customers/Initialize |  |
| [**updateComplianceInquiry**](TrusthubV1ComplianceInquiriesApi.md#updateComplianceInquiry) | **POST** /v1/ComplianceInquiries/Customers/{CustomerId}/Initialize |  |


<a id="createComplianceInquiry"></a>
# **createComplianceInquiry**
> TrusthubV1ComplianceInquiry createComplianceInquiry(primaryProfileSid, notificationEmail)



Create a new Compliance Inquiry for the authenticated account. This is necessary to start a new embedded session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1ComplianceInquiriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1ComplianceInquiriesApi apiInstance = new TrusthubV1ComplianceInquiriesApi(defaultClient);
    String primaryProfileSid = "primaryProfileSid_example"; // String | The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile.
    String notificationEmail = "notificationEmail_example"; // String | The email address that approval status updates will be sent to. If not specified, the email address associated with your primary customer profile will be used.
    try {
      TrusthubV1ComplianceInquiry result = apiInstance.createComplianceInquiry(primaryProfileSid, notificationEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1ComplianceInquiriesApi#createComplianceInquiry");
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
| **primaryProfileSid** | **String**| The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile. | |
| **notificationEmail** | **String**| The email address that approval status updates will be sent to. If not specified, the email address associated with your primary customer profile will be used. | [optional] |

### Return type

[**TrusthubV1ComplianceInquiry**](TrusthubV1ComplianceInquiry.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="updateComplianceInquiry"></a>
# **updateComplianceInquiry**
> TrusthubV1ComplianceInquiry updateComplianceInquiry(customerId, primaryProfileSid)



Resume a specific Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry for editing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1ComplianceInquiriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1ComplianceInquiriesApi apiInstance = new TrusthubV1ComplianceInquiriesApi(defaultClient);
    String customerId = "customerId_example"; // String | The unique CustomerId matching the Customer Profile/Compliance Inquiry that should be resumed or resubmitted. This value will have been returned by the initial Compliance Inquiry creation call.
    String primaryProfileSid = "primaryProfileSid_example"; // String | The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile.
    try {
      TrusthubV1ComplianceInquiry result = apiInstance.updateComplianceInquiry(customerId, primaryProfileSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1ComplianceInquiriesApi#updateComplianceInquiry");
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
| **customerId** | **String**| The unique CustomerId matching the Customer Profile/Compliance Inquiry that should be resumed or resubmitted. This value will have been returned by the initial Compliance Inquiry creation call. | |
| **primaryProfileSid** | **String**| The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile. | |

### Return type

[**TrusthubV1ComplianceInquiry**](TrusthubV1ComplianceInquiry.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

