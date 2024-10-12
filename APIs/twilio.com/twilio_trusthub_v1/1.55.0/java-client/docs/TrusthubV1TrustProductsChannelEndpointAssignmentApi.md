# TrusthubV1TrustProductsChannelEndpointAssignmentApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductsChannelEndpointAssignmentApi.md#createTrustProductChannelEndpointAssignment) | **POST** /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments |  |
| [**deleteTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductsChannelEndpointAssignmentApi.md#deleteTrustProductChannelEndpointAssignment) | **DELETE** /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments/{Sid} |  |
| [**fetchTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductsChannelEndpointAssignmentApi.md#fetchTrustProductChannelEndpointAssignment) | **GET** /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments/{Sid} |  |
| [**listTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductsChannelEndpointAssignmentApi.md#listTrustProductChannelEndpointAssignment) | **GET** /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments |  |


<a id="createTrustProductChannelEndpointAssignment"></a>
# **createTrustProductChannelEndpointAssignment**
> TrusthubV1TrustProductTrustProductChannelEndpointAssignment createTrustProductChannelEndpointAssignment(trustProductSid, channelEndpointSid, channelEndpointType)



Create a new Assigned Item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsChannelEndpointAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsChannelEndpointAssignmentApi apiInstance = new TrusthubV1TrustProductsChannelEndpointAssignmentApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String channelEndpointSid = "channelEndpointSid_example"; // String | The SID of an channel endpoint
    String channelEndpointType = "channelEndpointType_example"; // String | The type of channel endpoint. eg: phone-number
    try {
      TrusthubV1TrustProductTrustProductChannelEndpointAssignment result = apiInstance.createTrustProductChannelEndpointAssignment(trustProductSid, channelEndpointSid, channelEndpointType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsChannelEndpointAssignmentApi#createTrustProductChannelEndpointAssignment");
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
| **trustProductSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
| **channelEndpointSid** | **String**| The SID of an channel endpoint | |
| **channelEndpointType** | **String**| The type of channel endpoint. eg: phone-number | |

### Return type

[**TrusthubV1TrustProductTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductTrustProductChannelEndpointAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteTrustProductChannelEndpointAssignment"></a>
# **deleteTrustProductChannelEndpointAssignment**
> deleteTrustProductChannelEndpointAssignment(trustProductSid, sid)



Remove an Assignment Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsChannelEndpointAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsChannelEndpointAssignmentApi apiInstance = new TrusthubV1TrustProductsChannelEndpointAssignmentApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the resource.
    try {
      apiInstance.deleteTrustProductChannelEndpointAssignment(trustProductSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsChannelEndpointAssignmentApi#deleteTrustProductChannelEndpointAssignment");
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
| **trustProductSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
| **sid** | **String**| The unique string that we created to identify the resource. | |

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

<a id="fetchTrustProductChannelEndpointAssignment"></a>
# **fetchTrustProductChannelEndpointAssignment**
> TrusthubV1TrustProductTrustProductChannelEndpointAssignment fetchTrustProductChannelEndpointAssignment(trustProductSid, sid)



Fetch specific Assigned Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsChannelEndpointAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsChannelEndpointAssignmentApi apiInstance = new TrusthubV1TrustProductsChannelEndpointAssignmentApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the resource.
    try {
      TrusthubV1TrustProductTrustProductChannelEndpointAssignment result = apiInstance.fetchTrustProductChannelEndpointAssignment(trustProductSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsChannelEndpointAssignmentApi#fetchTrustProductChannelEndpointAssignment");
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
| **trustProductSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
| **sid** | **String**| The unique string that we created to identify the resource. | |

### Return type

[**TrusthubV1TrustProductTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductTrustProductChannelEndpointAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTrustProductChannelEndpointAssignment"></a>
# **listTrustProductChannelEndpointAssignment**
> ListTrustProductChannelEndpointAssignmentResponse listTrustProductChannelEndpointAssignment(trustProductSid, channelEndpointSid, channelEndpointSids, pageSize, page, pageToken)



Retrieve a list of all Assigned Items for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsChannelEndpointAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsChannelEndpointAssignmentApi apiInstance = new TrusthubV1TrustProductsChannelEndpointAssignmentApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String channelEndpointSid = "channelEndpointSid_example"; // String | The SID of an channel endpoint
    String channelEndpointSids = "channelEndpointSids_example"; // String | comma separated list of channel endpoint sids
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTrustProductChannelEndpointAssignmentResponse result = apiInstance.listTrustProductChannelEndpointAssignment(trustProductSid, channelEndpointSid, channelEndpointSids, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsChannelEndpointAssignmentApi#listTrustProductChannelEndpointAssignment");
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
| **trustProductSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
| **channelEndpointSid** | **String**| The SID of an channel endpoint | [optional] |
| **channelEndpointSids** | **String**| comma separated list of channel endpoint sids | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTrustProductChannelEndpointAssignmentResponse**](ListTrustProductChannelEndpointAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

