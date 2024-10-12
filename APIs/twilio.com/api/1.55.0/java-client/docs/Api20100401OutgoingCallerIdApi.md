# Api20100401OutgoingCallerIdApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteOutgoingCallerId**](Api20100401OutgoingCallerIdApi.md#deleteOutgoingCallerId) | **DELETE** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json |  |
| [**fetchOutgoingCallerId**](Api20100401OutgoingCallerIdApi.md#fetchOutgoingCallerId) | **GET** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json |  |
| [**listOutgoingCallerId**](Api20100401OutgoingCallerIdApi.md#listOutgoingCallerId) | **GET** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json |  |
| [**updateOutgoingCallerId**](Api20100401OutgoingCallerIdApi.md#updateOutgoingCallerId) | **POST** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json |  |


<a id="deleteOutgoingCallerId"></a>
# **deleteOutgoingCallerId**
> deleteOutgoingCallerId(accountSid, sid)



Delete the caller-id specified from the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401OutgoingCallerIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401OutgoingCallerIdApi apiInstance = new Api20100401OutgoingCallerIdApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to delete.
    try {
      apiInstance.deleteOutgoingCallerId(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401OutgoingCallerIdApi#deleteOutgoingCallerId");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to delete. | |

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

<a id="fetchOutgoingCallerId"></a>
# **fetchOutgoingCallerId**
> ApiV2010AccountOutgoingCallerId fetchOutgoingCallerId(accountSid, sid)



Fetch an outgoing-caller-id belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401OutgoingCallerIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401OutgoingCallerIdApi apiInstance = new Api20100401OutgoingCallerIdApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to fetch.
    try {
      ApiV2010AccountOutgoingCallerId result = apiInstance.fetchOutgoingCallerId(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401OutgoingCallerIdApi#fetchOutgoingCallerId");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to fetch. | |

### Return type

[**ApiV2010AccountOutgoingCallerId**](ApiV2010AccountOutgoingCallerId.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listOutgoingCallerId"></a>
# **listOutgoingCallerId**
> ListOutgoingCallerIdResponse listOutgoingCallerId(accountSid, phoneNumber, friendlyName, pageSize, page, pageToken)



Retrieve a list of outgoing-caller-ids belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401OutgoingCallerIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401OutgoingCallerIdApi apiInstance = new Api20100401OutgoingCallerIdApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to read.
    String phoneNumber = "phoneNumber_example"; // String | The phone number of the OutgoingCallerId resources to read.
    String friendlyName = "friendlyName_example"; // String | The string that identifies the OutgoingCallerId resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListOutgoingCallerIdResponse result = apiInstance.listOutgoingCallerId(accountSid, phoneNumber, friendlyName, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401OutgoingCallerIdApi#listOutgoingCallerId");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to read. | |
| **phoneNumber** | **String**| The phone number of the OutgoingCallerId resources to read. | [optional] |
| **friendlyName** | **String**| The string that identifies the OutgoingCallerId resources to read. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListOutgoingCallerIdResponse**](ListOutgoingCallerIdResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateOutgoingCallerId"></a>
# **updateOutgoingCallerId**
> ApiV2010AccountOutgoingCallerId updateOutgoingCallerId(accountSid, sid, friendlyName)



Updates the caller-id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401OutgoingCallerIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401OutgoingCallerIdApi apiInstance = new Api20100401OutgoingCallerIdApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    try {
      ApiV2010AccountOutgoingCallerId result = apiInstance.updateOutgoingCallerId(accountSid, sid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401OutgoingCallerIdApi#updateOutgoingCallerId");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |

### Return type

[**ApiV2010AccountOutgoingCallerId**](ApiV2010AccountOutgoingCallerId.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

