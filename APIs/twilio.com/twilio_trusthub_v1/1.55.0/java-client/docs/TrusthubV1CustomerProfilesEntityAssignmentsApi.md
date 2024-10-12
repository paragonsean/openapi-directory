# TrusthubV1CustomerProfilesEntityAssignmentsApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomerProfileEntityAssignment**](TrusthubV1CustomerProfilesEntityAssignmentsApi.md#createCustomerProfileEntityAssignment) | **POST** /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments |  |
| [**deleteCustomerProfileEntityAssignment**](TrusthubV1CustomerProfilesEntityAssignmentsApi.md#deleteCustomerProfileEntityAssignment) | **DELETE** /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid} |  |
| [**fetchCustomerProfileEntityAssignment**](TrusthubV1CustomerProfilesEntityAssignmentsApi.md#fetchCustomerProfileEntityAssignment) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid} |  |
| [**listCustomerProfileEntityAssignment**](TrusthubV1CustomerProfilesEntityAssignmentsApi.md#listCustomerProfileEntityAssignment) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments |  |


<a id="createCustomerProfileEntityAssignment"></a>
# **createCustomerProfileEntityAssignment**
> TrusthubV1CustomerProfileCustomerProfileEntityAssignment createCustomerProfileEntityAssignment(customerProfileSid, objectSid)



Create a new Assigned Item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesEntityAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesEntityAssignmentsApi apiInstance = new TrusthubV1CustomerProfilesEntityAssignmentsApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String objectSid = "objectSid_example"; // String | The SID of an object bag that holds information of the different items.
    try {
      TrusthubV1CustomerProfileCustomerProfileEntityAssignment result = apiInstance.createCustomerProfileEntityAssignment(customerProfileSid, objectSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesEntityAssignmentsApi#createCustomerProfileEntityAssignment");
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
| **objectSid** | **String**| The SID of an object bag that holds information of the different items. | |

### Return type

[**TrusthubV1CustomerProfileCustomerProfileEntityAssignment**](TrusthubV1CustomerProfileCustomerProfileEntityAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteCustomerProfileEntityAssignment"></a>
# **deleteCustomerProfileEntityAssignment**
> deleteCustomerProfileEntityAssignment(customerProfileSid, sid)



Remove an Assignment Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesEntityAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesEntityAssignmentsApi apiInstance = new TrusthubV1CustomerProfilesEntityAssignmentsApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
    try {
      apiInstance.deleteCustomerProfileEntityAssignment(customerProfileSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesEntityAssignmentsApi#deleteCustomerProfileEntityAssignment");
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
| **sid** | **String**| The unique string that we created to identify the Identity resource. | |

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

<a id="fetchCustomerProfileEntityAssignment"></a>
# **fetchCustomerProfileEntityAssignment**
> TrusthubV1CustomerProfileCustomerProfileEntityAssignment fetchCustomerProfileEntityAssignment(customerProfileSid, sid)



Fetch specific Assigned Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesEntityAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesEntityAssignmentsApi apiInstance = new TrusthubV1CustomerProfilesEntityAssignmentsApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
    try {
      TrusthubV1CustomerProfileCustomerProfileEntityAssignment result = apiInstance.fetchCustomerProfileEntityAssignment(customerProfileSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesEntityAssignmentsApi#fetchCustomerProfileEntityAssignment");
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
| **sid** | **String**| The unique string that we created to identify the Identity resource. | |

### Return type

[**TrusthubV1CustomerProfileCustomerProfileEntityAssignment**](TrusthubV1CustomerProfileCustomerProfileEntityAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listCustomerProfileEntityAssignment"></a>
# **listCustomerProfileEntityAssignment**
> ListCustomerProfileEntityAssignmentResponse listCustomerProfileEntityAssignment(customerProfileSid, pageSize, page, pageToken)



Retrieve a list of all Assigned Items for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesEntityAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesEntityAssignmentsApi apiInstance = new TrusthubV1CustomerProfilesEntityAssignmentsApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCustomerProfileEntityAssignmentResponse result = apiInstance.listCustomerProfileEntityAssignment(customerProfileSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesEntityAssignmentsApi#listCustomerProfileEntityAssignment");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListCustomerProfileEntityAssignmentResponse**](ListCustomerProfileEntityAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

