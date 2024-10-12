# TrusthubV1CustomerProfilesApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomerProfile**](TrusthubV1CustomerProfilesApi.md#createCustomerProfile) | **POST** /v1/CustomerProfiles |  |
| [**deleteCustomerProfile**](TrusthubV1CustomerProfilesApi.md#deleteCustomerProfile) | **DELETE** /v1/CustomerProfiles/{Sid} |  |
| [**fetchCustomerProfile**](TrusthubV1CustomerProfilesApi.md#fetchCustomerProfile) | **GET** /v1/CustomerProfiles/{Sid} |  |
| [**listCustomerProfile**](TrusthubV1CustomerProfilesApi.md#listCustomerProfile) | **GET** /v1/CustomerProfiles |  |
| [**updateCustomerProfile**](TrusthubV1CustomerProfilesApi.md#updateCustomerProfile) | **POST** /v1/CustomerProfiles/{Sid} |  |


<a id="createCustomerProfile"></a>
# **createCustomerProfile**
> TrusthubV1CustomerProfile createCustomerProfile(email, friendlyName, policySid, statusCallback)



Create a new Customer-Profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesApi apiInstance = new TrusthubV1CustomerProfilesApi(defaultClient);
    String email = "email_example"; // String | The email address that will receive updates when the Customer-Profile resource changes status.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String policySid = "policySid_example"; // String | The unique string of a policy that is associated to the Customer-Profile resource.
    URI statusCallback = new URI(); // URI | The URL we call to inform your application of status changes.
    try {
      TrusthubV1CustomerProfile result = apiInstance.createCustomerProfile(email, friendlyName, policySid, statusCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesApi#createCustomerProfile");
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
| **email** | **String**| The email address that will receive updates when the Customer-Profile resource changes status. | |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | |
| **policySid** | **String**| The unique string of a policy that is associated to the Customer-Profile resource. | |
| **statusCallback** | **URI**| The URL we call to inform your application of status changes. | [optional] |

### Return type

[**TrusthubV1CustomerProfile**](TrusthubV1CustomerProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteCustomerProfile"></a>
# **deleteCustomerProfile**
> deleteCustomerProfile(sid)



Delete a specific Customer-Profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesApi apiInstance = new TrusthubV1CustomerProfilesApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Customer-Profile resource.
    try {
      apiInstance.deleteCustomerProfile(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesApi#deleteCustomerProfile");
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
| **sid** | **String**| The unique string that we created to identify the Customer-Profile resource. | |

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

<a id="fetchCustomerProfile"></a>
# **fetchCustomerProfile**
> TrusthubV1CustomerProfile fetchCustomerProfile(sid)



Fetch a specific Customer-Profile instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesApi apiInstance = new TrusthubV1CustomerProfilesApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Customer-Profile resource.
    try {
      TrusthubV1CustomerProfile result = apiInstance.fetchCustomerProfile(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesApi#fetchCustomerProfile");
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
| **sid** | **String**| The unique string that we created to identify the Customer-Profile resource. | |

### Return type

[**TrusthubV1CustomerProfile**](TrusthubV1CustomerProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listCustomerProfile"></a>
# **listCustomerProfile**
> ListCustomerProfileResponse listCustomerProfile(status, friendlyName, policySid, pageSize, page, pageToken)



Retrieve a list of all Customer-Profiles for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesApi apiInstance = new TrusthubV1CustomerProfilesApi(defaultClient);
    CustomerProfileEnumStatus status = CustomerProfileEnumStatus.fromValue("draft"); // CustomerProfileEnumStatus | The verification status of the Customer-Profile resource.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String policySid = "policySid_example"; // String | The unique string of a policy that is associated to the Customer-Profile resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCustomerProfileResponse result = apiInstance.listCustomerProfile(status, friendlyName, policySid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesApi#listCustomerProfile");
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
| **status** | **CustomerProfileEnumStatus**| The verification status of the Customer-Profile resource. | [optional] [enum: draft, pending-review, in-review, twilio-rejected, twilio-approved] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |
| **policySid** | **String**| The unique string of a policy that is associated to the Customer-Profile resource. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListCustomerProfileResponse**](ListCustomerProfileResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateCustomerProfile"></a>
# **updateCustomerProfile**
> TrusthubV1CustomerProfile updateCustomerProfile(sid, email, friendlyName, status, statusCallback)



Updates a Customer-Profile in an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesApi apiInstance = new TrusthubV1CustomerProfilesApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Customer-Profile resource.
    String email = "email_example"; // String | The email address that will receive updates when the Customer-Profile resource changes status.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    CustomerProfileEnumStatus status = CustomerProfileEnumStatus.fromValue("draft"); // CustomerProfileEnumStatus | 
    URI statusCallback = new URI(); // URI | The URL we call to inform your application of status changes.
    try {
      TrusthubV1CustomerProfile result = apiInstance.updateCustomerProfile(sid, email, friendlyName, status, statusCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesApi#updateCustomerProfile");
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
| **sid** | **String**| The unique string that we created to identify the Customer-Profile resource. | |
| **email** | **String**| The email address that will receive updates when the Customer-Profile resource changes status. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |
| **status** | **CustomerProfileEnumStatus**|  | [optional] [enum: draft, pending-review, in-review, twilio-rejected, twilio-approved] |
| **statusCallback** | **URI**| The URL we call to inform your application of status changes. | [optional] |

### Return type

[**TrusthubV1CustomerProfile**](TrusthubV1CustomerProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

