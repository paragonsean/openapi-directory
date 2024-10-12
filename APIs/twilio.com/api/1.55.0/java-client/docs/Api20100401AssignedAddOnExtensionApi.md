# Api20100401AssignedAddOnExtensionApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchIncomingPhoneNumberAssignedAddOnExtension**](Api20100401AssignedAddOnExtensionApi.md#fetchIncomingPhoneNumberAssignedAddOnExtension) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions/{Sid}.json |  |
| [**listIncomingPhoneNumberAssignedAddOnExtension**](Api20100401AssignedAddOnExtensionApi.md#listIncomingPhoneNumberAssignedAddOnExtension) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions.json |  |


<a id="fetchIncomingPhoneNumberAssignedAddOnExtension"></a>
# **fetchIncomingPhoneNumberAssignedAddOnExtension**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension fetchIncomingPhoneNumberAssignedAddOnExtension(accountSid, resourceSid, assignedAddOnSid, sid)



Fetch an instance of an Extension for the Assigned Add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AssignedAddOnExtensionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AssignedAddOnExtensionApi apiInstance = new Api20100401AssignedAddOnExtensionApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
    String resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
    String assignedAddOnSid = "assignedAddOnSid_example"; // String | The SID that uniquely identifies the assigned Add-on installation.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the resource to fetch.
    try {
      ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension result = apiInstance.fetchIncomingPhoneNumberAssignedAddOnExtension(accountSid, resourceSid, assignedAddOnSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AssignedAddOnExtensionApi#fetchIncomingPhoneNumberAssignedAddOnExtension");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch. | |
| **resourceSid** | **String**| The SID of the Phone Number to which the Add-on is assigned. | |
| **assignedAddOnSid** | **String**| The SID that uniquely identifies the assigned Add-on installation. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the resource to fetch. | |

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listIncomingPhoneNumberAssignedAddOnExtension"></a>
# **listIncomingPhoneNumberAssignedAddOnExtension**
> ListIncomingPhoneNumberAssignedAddOnExtensionResponse listIncomingPhoneNumberAssignedAddOnExtension(accountSid, resourceSid, assignedAddOnSid, pageSize, page, pageToken)



Retrieve a list of Extensions for the Assigned Add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AssignedAddOnExtensionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AssignedAddOnExtensionApi apiInstance = new Api20100401AssignedAddOnExtensionApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    String resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
    String assignedAddOnSid = "assignedAddOnSid_example"; // String | The SID that uniquely identifies the assigned Add-on installation.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListIncomingPhoneNumberAssignedAddOnExtensionResponse result = apiInstance.listIncomingPhoneNumberAssignedAddOnExtension(accountSid, resourceSid, assignedAddOnSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AssignedAddOnExtensionApi#listIncomingPhoneNumberAssignedAddOnExtension");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. | |
| **resourceSid** | **String**| The SID of the Phone Number to which the Add-on is assigned. | |
| **assignedAddOnSid** | **String**| The SID that uniquely identifies the assigned Add-on installation. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListIncomingPhoneNumberAssignedAddOnExtensionResponse**](ListIncomingPhoneNumberAssignedAddOnExtensionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

