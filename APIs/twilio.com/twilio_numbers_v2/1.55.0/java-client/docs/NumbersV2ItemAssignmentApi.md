# NumbersV2ItemAssignmentApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createItemAssignment**](NumbersV2ItemAssignmentApi.md#createItemAssignment) | **POST** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments |  |
| [**deleteItemAssignment**](NumbersV2ItemAssignmentApi.md#deleteItemAssignment) | **DELETE** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid} |  |
| [**fetchItemAssignment**](NumbersV2ItemAssignmentApi.md#fetchItemAssignment) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid} |  |
| [**listItemAssignment**](NumbersV2ItemAssignmentApi.md#listItemAssignment) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments |  |


<a id="createItemAssignment"></a>
# **createItemAssignment**
> NumbersV2RegulatoryComplianceBundleItemAssignment createItemAssignment(bundleSid, objectSid)



Create a new Assigned Item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2ItemAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2ItemAssignmentApi apiInstance = new NumbersV2ItemAssignmentApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
    String objectSid = "objectSid_example"; // String | The SID of an object bag that holds information of the different items.
    try {
      NumbersV2RegulatoryComplianceBundleItemAssignment result = apiInstance.createItemAssignment(bundleSid, objectSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2ItemAssignmentApi#createItemAssignment");
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
| **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | |
| **objectSid** | **String**| The SID of an object bag that holds information of the different items. | |

### Return type

[**NumbersV2RegulatoryComplianceBundleItemAssignment**](NumbersV2RegulatoryComplianceBundleItemAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteItemAssignment"></a>
# **deleteItemAssignment**
> deleteItemAssignment(bundleSid, sid)



Remove an Assignment Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2ItemAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2ItemAssignmentApi apiInstance = new NumbersV2ItemAssignmentApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
    try {
      apiInstance.deleteItemAssignment(bundleSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2ItemAssignmentApi#deleteItemAssignment");
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
| **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | |
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

<a id="fetchItemAssignment"></a>
# **fetchItemAssignment**
> NumbersV2RegulatoryComplianceBundleItemAssignment fetchItemAssignment(bundleSid, sid)



Fetch specific Assigned Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2ItemAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2ItemAssignmentApi apiInstance = new NumbersV2ItemAssignmentApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
    try {
      NumbersV2RegulatoryComplianceBundleItemAssignment result = apiInstance.fetchItemAssignment(bundleSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2ItemAssignmentApi#fetchItemAssignment");
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
| **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | |
| **sid** | **String**| The unique string that we created to identify the Identity resource. | |

### Return type

[**NumbersV2RegulatoryComplianceBundleItemAssignment**](NumbersV2RegulatoryComplianceBundleItemAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listItemAssignment"></a>
# **listItemAssignment**
> ListItemAssignmentResponse listItemAssignment(bundleSid, pageSize, page, pageToken)



Retrieve a list of all Assigned Items for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2ItemAssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2ItemAssignmentApi apiInstance = new NumbersV2ItemAssignmentApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListItemAssignmentResponse result = apiInstance.listItemAssignment(bundleSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2ItemAssignmentApi#listItemAssignment");
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
| **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListItemAssignmentResponse**](ListItemAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

