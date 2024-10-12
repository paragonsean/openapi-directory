# Api20100401AssignedAddOnApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIncomingPhoneNumberAssignedAddOn**](Api20100401AssignedAddOnApi.md#createIncomingPhoneNumberAssignedAddOn) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json |  |
| [**deleteIncomingPhoneNumberAssignedAddOn**](Api20100401AssignedAddOnApi.md#deleteIncomingPhoneNumberAssignedAddOn) | **DELETE** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json |  |
| [**fetchIncomingPhoneNumberAssignedAddOn**](Api20100401AssignedAddOnApi.md#fetchIncomingPhoneNumberAssignedAddOn) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json |  |
| [**listIncomingPhoneNumberAssignedAddOn**](Api20100401AssignedAddOnApi.md#listIncomingPhoneNumberAssignedAddOn) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json |  |


<a id="createIncomingPhoneNumberAssignedAddOn"></a>
# **createIncomingPhoneNumberAssignedAddOn**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn createIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, installedAddOnSid)



Assign an Add-on installation to the Number specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AssignedAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AssignedAddOnApi apiInstance = new Api20100401AssignedAddOnApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to assign the Add-on.
    String installedAddOnSid = "installedAddOnSid_example"; // String | The SID that identifies the Add-on installation.
    try {
      ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn result = apiInstance.createIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, installedAddOnSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AssignedAddOnApi#createIncomingPhoneNumberAssignedAddOn");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | |
| **resourceSid** | **String**| The SID of the Phone Number to assign the Add-on. | |
| **installedAddOnSid** | **String**| The SID that identifies the Add-on installation. | |

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteIncomingPhoneNumberAssignedAddOn"></a>
# **deleteIncomingPhoneNumberAssignedAddOn**
> deleteIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, sid)



Remove the assignment of an Add-on installation from the Number specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AssignedAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AssignedAddOnApi apiInstance = new Api20100401AssignedAddOnApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to delete.
    String resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the resource to delete.
    try {
      apiInstance.deleteIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AssignedAddOnApi#deleteIncomingPhoneNumberAssignedAddOn");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to delete. | |
| **resourceSid** | **String**| The SID of the Phone Number to which the Add-on is assigned. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the resource to delete. | |

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

<a id="fetchIncomingPhoneNumberAssignedAddOn"></a>
# **fetchIncomingPhoneNumberAssignedAddOn**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn fetchIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, sid)



Fetch an instance of an Add-on installation currently assigned to this Number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AssignedAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AssignedAddOnApi apiInstance = new Api20100401AssignedAddOnApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
    String resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the resource to fetch.
    try {
      ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn result = apiInstance.fetchIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AssignedAddOnApi#fetchIncomingPhoneNumberAssignedAddOn");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the resource to fetch. | |

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listIncomingPhoneNumberAssignedAddOn"></a>
# **listIncomingPhoneNumberAssignedAddOn**
> ListIncomingPhoneNumberAssignedAddOnResponse listIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, pageSize, page, pageToken)



Retrieve a list of Add-on installations currently assigned to this Number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AssignedAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AssignedAddOnApi apiInstance = new Api20100401AssignedAddOnApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    String resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListIncomingPhoneNumberAssignedAddOnResponse result = apiInstance.listIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AssignedAddOnApi#listIncomingPhoneNumberAssignedAddOn");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListIncomingPhoneNumberAssignedAddOnResponse**](ListIncomingPhoneNumberAssignedAddOnResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

