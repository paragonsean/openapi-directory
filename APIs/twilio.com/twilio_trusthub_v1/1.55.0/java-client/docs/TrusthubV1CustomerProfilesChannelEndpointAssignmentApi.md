# TrusthubV1CustomerProfilesChannelEndpointAssignmentApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfilesChannelEndpointAssignmentApi.md#createCustomerProfileChannelEndpointAssignment) | **POST** /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments |  |
| [**deleteCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfilesChannelEndpointAssignmentApi.md#deleteCustomerProfileChannelEndpointAssignment) | **DELETE** /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid} |  |
| [**fetchCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfilesChannelEndpointAssignmentApi.md#fetchCustomerProfileChannelEndpointAssignment) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid} |  |
| [**listCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfilesChannelEndpointAssignmentApi.md#listCustomerProfileChannelEndpointAssignment) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments |  |


<a id="createCustomerProfileChannelEndpointAssignment"></a>
# **createCustomerProfileChannelEndpointAssignment**
> TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment createCustomerProfileChannelEndpointAssignment(customerProfileSid, channelEndpointSid, channelEndpointType)



Create a new Assigned Item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesChannelEndpointAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesChannelEndpointAssignmentApi apiInstance = new TrusthubV1CustomerProfilesChannelEndpointAssignmentApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String channelEndpointSid = "channelEndpointSid_example"; // String | The SID of an channel endpoint
    String channelEndpointType = "channelEndpointType_example"; // String | The type of channel endpoint. eg: phone-number
    try {
      TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment result = apiInstance.createCustomerProfileChannelEndpointAssignment(customerProfileSid, channelEndpointSid, channelEndpointType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesChannelEndpointAssignmentApi#createCustomerProfileChannelEndpointAssignment");
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
| **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
| **channelEndpointSid** | **String**| The SID of an channel endpoint | |
| **channelEndpointType** | **String**| The type of channel endpoint. eg: phone-number | |

### Return type

[**TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteCustomerProfileChannelEndpointAssignment"></a>
# **deleteCustomerProfileChannelEndpointAssignment**
> deleteCustomerProfileChannelEndpointAssignment(customerProfileSid, sid)



Remove an Assignment Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesChannelEndpointAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesChannelEndpointAssignmentApi apiInstance = new TrusthubV1CustomerProfilesChannelEndpointAssignmentApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the resource.
    try {
      apiInstance.deleteCustomerProfileChannelEndpointAssignment(customerProfileSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesChannelEndpointAssignmentApi#deleteCustomerProfileChannelEndpointAssignment");
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
| **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
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

<a id="fetchCustomerProfileChannelEndpointAssignment"></a>
# **fetchCustomerProfileChannelEndpointAssignment**
> TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment fetchCustomerProfileChannelEndpointAssignment(customerProfileSid, sid)



Fetch specific Assigned Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesChannelEndpointAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesChannelEndpointAssignmentApi apiInstance = new TrusthubV1CustomerProfilesChannelEndpointAssignmentApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the resource.
    try {
      TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment result = apiInstance.fetchCustomerProfileChannelEndpointAssignment(customerProfileSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesChannelEndpointAssignmentApi#fetchCustomerProfileChannelEndpointAssignment");
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
| **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
| **sid** | **String**| The unique string that we created to identify the resource. | |

### Return type

[**TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listCustomerProfileChannelEndpointAssignment"></a>
# **listCustomerProfileChannelEndpointAssignment**
> ListCustomerProfileChannelEndpointAssignmentResponse listCustomerProfileChannelEndpointAssignment(customerProfileSid, channelEndpointSid, channelEndpointSids, pageSize, page, pageToken)



Retrieve a list of all Assigned Items for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesChannelEndpointAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesChannelEndpointAssignmentApi apiInstance = new TrusthubV1CustomerProfilesChannelEndpointAssignmentApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String channelEndpointSid = "channelEndpointSid_example"; // String | The SID of an channel endpoint
    String channelEndpointSids = "channelEndpointSids_example"; // String | comma separated list of channel endpoint sids
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCustomerProfileChannelEndpointAssignmentResponse result = apiInstance.listCustomerProfileChannelEndpointAssignment(customerProfileSid, channelEndpointSid, channelEndpointSids, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesChannelEndpointAssignmentApi#listCustomerProfileChannelEndpointAssignment");
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
| **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
| **channelEndpointSid** | **String**| The SID of an channel endpoint | [optional] |
| **channelEndpointSids** | **String**| comma separated list of channel endpoint sids | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListCustomerProfileChannelEndpointAssignmentResponse**](ListCustomerProfileChannelEndpointAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

