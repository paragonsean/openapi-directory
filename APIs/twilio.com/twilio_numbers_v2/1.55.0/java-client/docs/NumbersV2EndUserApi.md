# NumbersV2EndUserApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEndUser**](NumbersV2EndUserApi.md#createEndUser) | **POST** /v2/RegulatoryCompliance/EndUsers |  |
| [**deleteEndUser**](NumbersV2EndUserApi.md#deleteEndUser) | **DELETE** /v2/RegulatoryCompliance/EndUsers/{Sid} |  |
| [**fetchEndUser**](NumbersV2EndUserApi.md#fetchEndUser) | **GET** /v2/RegulatoryCompliance/EndUsers/{Sid} |  |
| [**listEndUser**](NumbersV2EndUserApi.md#listEndUser) | **GET** /v2/RegulatoryCompliance/EndUsers |  |
| [**updateEndUser**](NumbersV2EndUserApi.md#updateEndUser) | **POST** /v2/RegulatoryCompliance/EndUsers/{Sid} |  |


<a id="createEndUser"></a>
# **createEndUser**
> NumbersV2RegulatoryComplianceEndUser createEndUser(friendlyName, type, attributes)



Create a new End User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2EndUserApi apiInstance = new NumbersV2EndUserApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    EndUserEnumType type = EndUserEnumType.fromValue("individual"); // EndUserEnumType | 
    Object attributes = null; // Object | The set of parameters that are the attributes of the End User resource which are derived End User Types.
    try {
      NumbersV2RegulatoryComplianceEndUser result = apiInstance.createEndUser(friendlyName, type, attributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2EndUserApi#createEndUser");
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
| **friendlyName** | **String**| The string that you assigned to describe the resource. | |
| **type** | **EndUserEnumType**|  | [enum: individual, business] |
| **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the End User resource which are derived End User Types. | [optional] |

### Return type

[**NumbersV2RegulatoryComplianceEndUser**](NumbersV2RegulatoryComplianceEndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteEndUser"></a>
# **deleteEndUser**
> deleteEndUser(sid)



Delete a specific End User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2EndUserApi apiInstance = new NumbersV2EndUserApi(defaultClient);
    String sid = "sid_example"; // String | The unique string created by Twilio to identify the End User resource.
    try {
      apiInstance.deleteEndUser(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2EndUserApi#deleteEndUser");
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
| **sid** | **String**| The unique string created by Twilio to identify the End User resource. | |

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

<a id="fetchEndUser"></a>
# **fetchEndUser**
> NumbersV2RegulatoryComplianceEndUser fetchEndUser(sid)



Fetch specific End User Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2EndUserApi apiInstance = new NumbersV2EndUserApi(defaultClient);
    String sid = "sid_example"; // String | The unique string created by Twilio to identify the End User resource.
    try {
      NumbersV2RegulatoryComplianceEndUser result = apiInstance.fetchEndUser(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2EndUserApi#fetchEndUser");
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
| **sid** | **String**| The unique string created by Twilio to identify the End User resource. | |

### Return type

[**NumbersV2RegulatoryComplianceEndUser**](NumbersV2RegulatoryComplianceEndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listEndUser"></a>
# **listEndUser**
> ListEndUserResponse listEndUser(pageSize, page, pageToken)



Retrieve a list of all End User for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2EndUserApi apiInstance = new NumbersV2EndUserApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListEndUserResponse result = apiInstance.listEndUser(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2EndUserApi#listEndUser");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListEndUserResponse**](ListEndUserResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateEndUser"></a>
# **updateEndUser**
> NumbersV2RegulatoryComplianceEndUser updateEndUser(sid, attributes, friendlyName)



Update an existing End User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2EndUserApi apiInstance = new NumbersV2EndUserApi(defaultClient);
    String sid = "sid_example"; // String | The unique string created by Twilio to identify the End User resource.
    Object attributes = null; // Object | The set of parameters that are the attributes of the End User resource which are derived End User Types.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    try {
      NumbersV2RegulatoryComplianceEndUser result = apiInstance.updateEndUser(sid, attributes, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2EndUserApi#updateEndUser");
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
| **sid** | **String**| The unique string created by Twilio to identify the End User resource. | |
| **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the End User resource which are derived End User Types. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |

### Return type

[**NumbersV2RegulatoryComplianceEndUser**](NumbersV2RegulatoryComplianceEndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

