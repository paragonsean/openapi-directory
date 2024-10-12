# CallsApi

All URIs are relative to *https://api.nexmo.com/v1/calls*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCall**](CallsApi.md#createCall) | **POST** / | Create an outbound call |
| [**getCall**](CallsApi.md#getCall) | **GET** /{uuid} | Get detail of a specific call |
| [**getCalls**](CallsApi.md#getCalls) | **GET** / | Get details of your calls |
| [**updateCall**](CallsApi.md#updateCall) | **PUT** /{uuid} | Modify an in progress call |


<a id="createCall"></a>
# **createCall**
> CreateCallResponse createCall(createCallRequest)

Create an outbound call

Create an outbound Call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/calls");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    CreateCallRequest createCallRequest = new CreateCallRequest(); // CreateCallRequest | Call Details
    try {
      CreateCallResponse result = apiInstance.createCall(createCallRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#createCall");
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
| **createCallRequest** | [**CreateCallRequest**](CreateCallRequest.md)| Call Details | [optional] |

### Return type

[**CreateCallResponse**](CreateCallResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="getCall"></a>
# **getCall**
> GetCallResponse getCall(uuid)

Get detail of a specific call

Get detail of a specific call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/calls");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call
    try {
      GetCallResponse result = apiInstance.getCall(uuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCall");
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
| **uuid** | **String**| UUID of the Call | |

### Return type

[**GetCallResponse**](GetCallResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |

<a id="getCalls"></a>
# **getCalls**
> GetCallsResponse getCalls(status, dateStart, dateEnd, pageSize, recordIndex, order, conversationUuid)

Get details of your calls

Get details of your calls

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/calls");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String status = "started"; // String | Filter by call status
    OffsetDateTime dateStart = OffsetDateTime.parse("2016-11-14T07:45:14Z"); // OffsetDateTime | Return the records that occurred after this point in time
    OffsetDateTime dateEnd = OffsetDateTime.parse("2016-11-14T07:45:14Z"); // OffsetDateTime | Return the records that occurred before this point in time
    Integer pageSize = 10; // Integer | Return this amount of records in the response
    Integer recordIndex = 0; // Integer | Return calls from this index in the response
    String order = "asc"; // String | Either ascending or  descending order.
    UUID conversationUuid = UUID.randomUUID(); // UUID | Return all the records associated with a specific conversation.
    try {
      GetCallsResponse result = apiInstance.getCalls(status, dateStart, dateEnd, pageSize, recordIndex, order, conversationUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCalls");
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
| **status** | **String**| Filter by call status | [optional] [enum: started, ringing, answered, machine, completed, busy, cancelled, failed, rejected, timeout, unanswered] |
| **dateStart** | **OffsetDateTime**| Return the records that occurred after this point in time | [optional] |
| **dateEnd** | **OffsetDateTime**| Return the records that occurred before this point in time | [optional] |
| **pageSize** | **Integer**| Return this amount of records in the response | [optional] [default to 10] |
| **recordIndex** | **Integer**| Return calls from this index in the response | [optional] [default to 0] |
| **order** | **String**| Either ascending or  descending order. | [optional] [default to asc] [enum: asc, desc] |
| **conversationUuid** | **UUID**| Return all the records associated with a specific conversation. | [optional] |

### Return type

[**GetCallsResponse**](GetCallsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateCall"></a>
# **updateCall**
> updateCall(uuid, updateCallRequest)

Modify an in progress call

Modify an in progress call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/calls");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call
    UpdateCallRequest updateCallRequest = new UpdateCallRequest(); // UpdateCallRequest | 
    try {
      apiInstance.updateCall(uuid, updateCallRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#updateCall");
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
| **uuid** | **String**| UUID of the Call | |
| **updateCallRequest** | [**UpdateCallRequest**](UpdateCallRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

