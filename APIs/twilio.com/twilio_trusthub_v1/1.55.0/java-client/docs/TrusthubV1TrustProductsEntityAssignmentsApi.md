# TrusthubV1TrustProductsEntityAssignmentsApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTrustProductEntityAssignment**](TrusthubV1TrustProductsEntityAssignmentsApi.md#createTrustProductEntityAssignment) | **POST** /v1/TrustProducts/{TrustProductSid}/EntityAssignments |  |
| [**deleteTrustProductEntityAssignment**](TrusthubV1TrustProductsEntityAssignmentsApi.md#deleteTrustProductEntityAssignment) | **DELETE** /v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid} |  |
| [**fetchTrustProductEntityAssignment**](TrusthubV1TrustProductsEntityAssignmentsApi.md#fetchTrustProductEntityAssignment) | **GET** /v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid} |  |
| [**listTrustProductEntityAssignment**](TrusthubV1TrustProductsEntityAssignmentsApi.md#listTrustProductEntityAssignment) | **GET** /v1/TrustProducts/{TrustProductSid}/EntityAssignments |  |


<a id="createTrustProductEntityAssignment"></a>
# **createTrustProductEntityAssignment**
> TrusthubV1TrustProductTrustProductEntityAssignment createTrustProductEntityAssignment(trustProductSid, objectSid)



Create a new Assigned Item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsEntityAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsEntityAssignmentsApi apiInstance = new TrusthubV1TrustProductsEntityAssignmentsApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the TrustProduct resource.
    String objectSid = "objectSid_example"; // String | The SID of an object bag that holds information of the different items.
    try {
      TrusthubV1TrustProductTrustProductEntityAssignment result = apiInstance.createTrustProductEntityAssignment(trustProductSid, objectSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsEntityAssignmentsApi#createTrustProductEntityAssignment");
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
| **trustProductSid** | **String**| The unique string that we created to identify the TrustProduct resource. | |
| **objectSid** | **String**| The SID of an object bag that holds information of the different items. | |

### Return type

[**TrusthubV1TrustProductTrustProductEntityAssignment**](TrusthubV1TrustProductTrustProductEntityAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteTrustProductEntityAssignment"></a>
# **deleteTrustProductEntityAssignment**
> deleteTrustProductEntityAssignment(trustProductSid, sid)



Remove an Assignment Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsEntityAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsEntityAssignmentsApi apiInstance = new TrusthubV1TrustProductsEntityAssignmentsApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the TrustProduct resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
    try {
      apiInstance.deleteTrustProductEntityAssignment(trustProductSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsEntityAssignmentsApi#deleteTrustProductEntityAssignment");
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
| **trustProductSid** | **String**| The unique string that we created to identify the TrustProduct resource. | |
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

<a id="fetchTrustProductEntityAssignment"></a>
# **fetchTrustProductEntityAssignment**
> TrusthubV1TrustProductTrustProductEntityAssignment fetchTrustProductEntityAssignment(trustProductSid, sid)



Fetch specific Assigned Item Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsEntityAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsEntityAssignmentsApi apiInstance = new TrusthubV1TrustProductsEntityAssignmentsApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the TrustProduct resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
    try {
      TrusthubV1TrustProductTrustProductEntityAssignment result = apiInstance.fetchTrustProductEntityAssignment(trustProductSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsEntityAssignmentsApi#fetchTrustProductEntityAssignment");
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
| **trustProductSid** | **String**| The unique string that we created to identify the TrustProduct resource. | |
| **sid** | **String**| The unique string that we created to identify the Identity resource. | |

### Return type

[**TrusthubV1TrustProductTrustProductEntityAssignment**](TrusthubV1TrustProductTrustProductEntityAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTrustProductEntityAssignment"></a>
# **listTrustProductEntityAssignment**
> ListTrustProductEntityAssignmentResponse listTrustProductEntityAssignment(trustProductSid, pageSize, page, pageToken)



Retrieve a list of all Assigned Items for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsEntityAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsEntityAssignmentsApi apiInstance = new TrusthubV1TrustProductsEntityAssignmentsApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the TrustProduct resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTrustProductEntityAssignmentResponse result = apiInstance.listTrustProductEntityAssignment(trustProductSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsEntityAssignmentsApi#listTrustProductEntityAssignment");
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
| **trustProductSid** | **String**| The unique string that we created to identify the TrustProduct resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTrustProductEntityAssignmentResponse**](ListTrustProductEntityAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

