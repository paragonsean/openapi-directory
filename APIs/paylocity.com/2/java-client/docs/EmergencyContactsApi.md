# EmergencyContactsApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addOrUpdateEmergencyContacts**](EmergencyContactsApi.md#addOrUpdateEmergencyContacts) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/emergencyContacts | Add/update emergency contacts |


<a id="addOrUpdateEmergencyContacts"></a>
# **addOrUpdateEmergencyContacts**
> addOrUpdateEmergencyContacts(companyId, employeeId, emergencyContact)

Add/update emergency contacts

Sends new or updated employee emergency contacts directly to Web Pay.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmergencyContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    EmergencyContactsApi apiInstance = new EmergencyContactsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    EmergencyContact emergencyContact = new EmergencyContact(); // EmergencyContact | Emergency Contact Model
    try {
      apiInstance.addOrUpdateEmergencyContacts(companyId, employeeId, emergencyContact);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmergencyContactsApi#addOrUpdateEmergencyContacts");
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
| **companyId** | **String**| Company Id | |
| **employeeId** | **String**| Employee Id | |
| **emergencyContact** | [**EmergencyContact**](EmergencyContact.md)| Emergency Contact Model | |

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added or updated |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

