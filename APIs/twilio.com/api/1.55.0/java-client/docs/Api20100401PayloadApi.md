# Api20100401PayloadApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteRecordingAddOnResultPayload**](Api20100401PayloadApi.md#deleteRecordingAddOnResultPayload) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json |  |
| [**fetchRecordingAddOnResultPayload**](Api20100401PayloadApi.md#fetchRecordingAddOnResultPayload) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json |  |
| [**listRecordingAddOnResultPayload**](Api20100401PayloadApi.md#listRecordingAddOnResultPayload) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads.json |  |


<a id="deleteRecordingAddOnResultPayload"></a>
# **deleteRecordingAddOnResultPayload**
> deleteRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, sid)



Delete a payload from the result along with all associated Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401PayloadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401PayloadApi apiInstance = new Api20100401PayloadApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to delete.
    String referenceSid = "referenceSid_example"; // String | The SID of the recording to which the AddOnResult resource that contains the payloads to delete belongs.
    String addOnResultSid = "addOnResultSid_example"; // String | The SID of the AddOnResult to which the payloads to delete belongs.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to delete.
    try {
      apiInstance.deleteRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401PayloadApi#deleteRecordingAddOnResultPayload");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to delete. | |
| **referenceSid** | **String**| The SID of the recording to which the AddOnResult resource that contains the payloads to delete belongs. | |
| **addOnResultSid** | **String**| The SID of the AddOnResult to which the payloads to delete belongs. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to delete. | |

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

<a id="fetchRecordingAddOnResultPayload"></a>
# **fetchRecordingAddOnResultPayload**
> ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload fetchRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, sid)



Fetch an instance of a result payload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401PayloadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401PayloadApi apiInstance = new Api20100401PayloadApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resource to fetch.
    String referenceSid = "referenceSid_example"; // String | The SID of the recording to which the AddOnResult resource that contains the payload to fetch belongs.
    String addOnResultSid = "addOnResultSid_example"; // String | The SID of the AddOnResult to which the payload to fetch belongs.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch.
    try {
      ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload result = apiInstance.fetchRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401PayloadApi#fetchRecordingAddOnResultPayload");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resource to fetch. | |
| **referenceSid** | **String**| The SID of the recording to which the AddOnResult resource that contains the payload to fetch belongs. | |
| **addOnResultSid** | **String**| The SID of the AddOnResult to which the payload to fetch belongs. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch. | |

### Return type

[**ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload**](ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRecordingAddOnResultPayload"></a>
# **listRecordingAddOnResultPayload**
> ListRecordingAddOnResultPayloadResponse listRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, pageSize, page, pageToken)



Retrieve a list of payloads belonging to the AddOnResult

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401PayloadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401PayloadApi apiInstance = new Api20100401PayloadApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to read.
    String referenceSid = "referenceSid_example"; // String | The SID of the recording to which the AddOnResult resource that contains the payloads to read belongs.
    String addOnResultSid = "addOnResultSid_example"; // String | The SID of the AddOnResult to which the payloads to read belongs.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRecordingAddOnResultPayloadResponse result = apiInstance.listRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401PayloadApi#listRecordingAddOnResultPayload");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to read. | |
| **referenceSid** | **String**| The SID of the recording to which the AddOnResult resource that contains the payloads to read belongs. | |
| **addOnResultSid** | **String**| The SID of the AddOnResult to which the payloads to read belongs. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRecordingAddOnResultPayloadResponse**](ListRecordingAddOnResultPayloadResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

