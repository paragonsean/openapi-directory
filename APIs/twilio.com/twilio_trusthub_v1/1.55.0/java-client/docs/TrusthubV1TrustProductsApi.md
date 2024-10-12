# TrusthubV1TrustProductsApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTrustProduct**](TrusthubV1TrustProductsApi.md#createTrustProduct) | **POST** /v1/TrustProducts |  |
| [**deleteTrustProduct**](TrusthubV1TrustProductsApi.md#deleteTrustProduct) | **DELETE** /v1/TrustProducts/{Sid} |  |
| [**fetchTrustProduct**](TrusthubV1TrustProductsApi.md#fetchTrustProduct) | **GET** /v1/TrustProducts/{Sid} |  |
| [**listTrustProduct**](TrusthubV1TrustProductsApi.md#listTrustProduct) | **GET** /v1/TrustProducts |  |
| [**updateTrustProduct**](TrusthubV1TrustProductsApi.md#updateTrustProduct) | **POST** /v1/TrustProducts/{Sid} |  |


<a id="createTrustProduct"></a>
# **createTrustProduct**
> TrusthubV1TrustProduct createTrustProduct(email, friendlyName, policySid, statusCallback)



Create a new Customer-Profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsApi apiInstance = new TrusthubV1TrustProductsApi(defaultClient);
    String email = "email_example"; // String | The email address that will receive updates when the Customer-Profile resource changes status.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String policySid = "policySid_example"; // String | The unique string of a policy that is associated to the Customer-Profile resource.
    URI statusCallback = new URI(); // URI | The URL we call to inform your application of status changes.
    try {
      TrusthubV1TrustProduct result = apiInstance.createTrustProduct(email, friendlyName, policySid, statusCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsApi#createTrustProduct");
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

[**TrusthubV1TrustProduct**](TrusthubV1TrustProduct.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteTrustProduct"></a>
# **deleteTrustProduct**
> deleteTrustProduct(sid)



Delete a specific Customer-Profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsApi apiInstance = new TrusthubV1TrustProductsApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Customer-Profile resource.
    try {
      apiInstance.deleteTrustProduct(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsApi#deleteTrustProduct");
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

<a id="fetchTrustProduct"></a>
# **fetchTrustProduct**
> TrusthubV1TrustProduct fetchTrustProduct(sid)



Fetch a specific Customer-Profile instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsApi apiInstance = new TrusthubV1TrustProductsApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Customer-Profile resource.
    try {
      TrusthubV1TrustProduct result = apiInstance.fetchTrustProduct(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsApi#fetchTrustProduct");
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

[**TrusthubV1TrustProduct**](TrusthubV1TrustProduct.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTrustProduct"></a>
# **listTrustProduct**
> ListTrustProductResponse listTrustProduct(status, friendlyName, policySid, pageSize, page, pageToken)



Retrieve a list of all Customer-Profiles for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsApi apiInstance = new TrusthubV1TrustProductsApi(defaultClient);
    TrustProductEnumStatus status = TrustProductEnumStatus.fromValue("draft"); // TrustProductEnumStatus | The verification status of the Customer-Profile resource.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String policySid = "policySid_example"; // String | The unique string of a policy that is associated to the Customer-Profile resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTrustProductResponse result = apiInstance.listTrustProduct(status, friendlyName, policySid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsApi#listTrustProduct");
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
| **status** | **TrustProductEnumStatus**| The verification status of the Customer-Profile resource. | [optional] [enum: draft, pending-review, in-review, twilio-rejected, twilio-approved] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |
| **policySid** | **String**| The unique string of a policy that is associated to the Customer-Profile resource. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTrustProductResponse**](ListTrustProductResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTrustProduct"></a>
# **updateTrustProduct**
> TrusthubV1TrustProduct updateTrustProduct(sid, email, friendlyName, status, statusCallback)



Updates a Customer-Profile in an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsApi apiInstance = new TrusthubV1TrustProductsApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Customer-Profile resource.
    String email = "email_example"; // String | The email address that will receive updates when the Customer-Profile resource changes status.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    TrustProductEnumStatus status = TrustProductEnumStatus.fromValue("draft"); // TrustProductEnumStatus | 
    URI statusCallback = new URI(); // URI | The URL we call to inform your application of status changes.
    try {
      TrusthubV1TrustProduct result = apiInstance.updateTrustProduct(sid, email, friendlyName, status, statusCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsApi#updateTrustProduct");
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
| **status** | **TrustProductEnumStatus**|  | [optional] [enum: draft, pending-review, in-review, twilio-rejected, twilio-approved] |
| **statusCallback** | **URI**| The URL we call to inform your application of status changes. | [optional] |

### Return type

[**TrusthubV1TrustProduct**](TrusthubV1TrustProduct.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

