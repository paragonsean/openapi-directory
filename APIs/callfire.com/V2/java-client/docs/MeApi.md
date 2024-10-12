# MeApi

All URIs are relative to *https://api.callfire.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiCredential**](MeApi.md#createApiCredential) | **POST** /me/api/credentials | Create api credentials |
| [**deleteApiCredential**](MeApi.md#deleteApiCredential) | **DELETE** /me/api/credentials/{id} | Delete api credentials |
| [**disableApiCredentials**](MeApi.md#disableApiCredentials) | **POST** /me/api/credentials/{id}/disable | Disable specified API credentials |
| [**enableApiCredentials**](MeApi.md#enableApiCredentials) | **POST** /me/api/credentials/{id}/enable | Enable specified API credentials |
| [**findApiCredentials**](MeApi.md#findApiCredentials) | **GET** /me/api/credentials | Find api credentials |
| [**getAccount**](MeApi.md#getAccount) | **GET** /me/account | Find account details |
| [**getApiCredential**](MeApi.md#getApiCredential) | **GET** /me/api/credentials/{id} | Find a specific api credential |
| [**getBillingPlanUsage**](MeApi.md#getBillingPlanUsage) | **GET** /me/billing/plan-usage | Find plan usage |
| [**getCallerIds**](MeApi.md#getCallerIds) | **GET** /me/callerids | Find caller ids |
| [**getCreditUsage**](MeApi.md#getCreditUsage) | **GET** /me/billing/credit-usage | Find credit usage |
| [**sendVerificationCodeToCallerId**](MeApi.md#sendVerificationCodeToCallerId) | **POST** /me/callerids/{callerid} | Create a caller id |
| [**verifyCallerId**](MeApi.md#verifyCallerId) | **POST** /me/callerids/{callerid}/verification-code | Verify a caller id |


<a id="createApiCredential"></a>
# **createApiCredential**
> ApiCredential createApiCredential(apiCredential)

Create api credentials

Creates an API credentials for the CallFire API. This endpoint requires full CallFire account credentials to be used, authenticated using Basic Authentication. At the moment user provides only the name for the credentials. The generated credentials can be used to access any CallFire APIs. For authentication use account credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    ApiCredential apiCredential = new ApiCredential(); // ApiCredential | To create the API credentials
    try {
      ApiCredential result = apiInstance.createApiCredential(apiCredential);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#createApiCredential");
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
| **apiCredential** | [**ApiCredential**](ApiCredential.md)| To create the API credentials | [optional] |

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="deleteApiCredential"></a>
# **deleteApiCredential**
> deleteApiCredential(id)

Delete api credentials

Deletes a specified API credential. Currently, removes the ability to access the API. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    Long id = 56L; // Long | An id of an API credential
    try {
      apiInstance.deleteApiCredential(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#deleteApiCredential");
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
| **id** | **Long**| An id of an API credential | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="disableApiCredentials"></a>
# **disableApiCredentials**
> disableApiCredentials(id)

Disable specified API credentials

Disables a specified API credential. Currently, removes the ability to access the API. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    Long id = 56L; // Long | An id of an API credential
    try {
      apiInstance.disableApiCredentials(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#disableApiCredentials");
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
| **id** | **Long**| An id of an API credential | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="enableApiCredentials"></a>
# **enableApiCredentials**
> enableApiCredentials(id)

Enable specified API credentials

Enables a specified API credential. Currently, adds the ability to access the API. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    Long id = 56L; // Long | An id of an API credential
    try {
      apiInstance.enableApiCredentials(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#enableApiCredentials");
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
| **id** | **Long**| An id of an API credential | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="findApiCredentials"></a>
# **findApiCredentials**
> ApiCredentialPage findApiCredentials(name, fields, limit, offset)

Find api credentials

Searches for all credentials generated by user. Returns a paged list of the API credentials. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    String name = "name_example"; // String | Filter by name
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    try {
      ApiCredentialPage result = apiInstance.findApiCredentials(name, fields, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#findApiCredentials");
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
| **name** | **String**| Filter by name | [optional] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |

### Return type

[**ApiCredentialPage**](ApiCredentialPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getAccount"></a>
# **getAccount**
> Account getAccount(fields)

Find account details

Searches for the user account details. Details include name, email, and basic account permissions. For authentication use api credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      Account result = apiInstance.getAccount(fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#getAccount");
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
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**Account**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getApiCredential"></a>
# **getApiCredential**
> ApiCredential getApiCredential(id, fields)

Find a specific api credential

Returns an API credential instance for a given api credential id. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    Long id = 56L; // Long | An id of an API credential
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      ApiCredential result = apiInstance.getApiCredential(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#getApiCredential");
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
| **id** | **Long**| An id of an API credential | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getBillingPlanUsage"></a>
# **getBillingPlanUsage**
> BillingPlanUsage getBillingPlanUsage()

Find plan usage

Searches for the data of a billing plan usage for the user. Returns the data of a billing plan usage for the current month. For authentication use api credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    try {
      BillingPlanUsage result = apiInstance.getBillingPlanUsage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#getBillingPlanUsage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BillingPlanUsage**](BillingPlanUsage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallerIds"></a>
# **getCallerIds**
> CallerIdList getCallerIds()

Find caller ids

Returns a list of verified caller ids. If the number is not shown in the list, then it is not verified. In this case sending of a verification code is required. For authentication use api credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    try {
      CallerIdList result = apiInstance.getCallerIds();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#getCallerIds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CallerIdList**](CallerIdList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCreditUsage"></a>
# **getCreditUsage**
> CreditUsage getCreditUsage(intervalBegin, intervalEnd)

Find credit usage

Find credit usage for the user. Returns credits usage for time period specified or if unspecified then total for all time. For authentication use api credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    Long intervalBegin = 56L; // Long | Beginning of usage period formatted in unix time milliseconds. Example: 1473781817000
    Long intervalEnd = 56L; // Long | End of usage period formatted in unix time milliseconds. Example: 1473781817000
    try {
      CreditUsage result = apiInstance.getCreditUsage(intervalBegin, intervalEnd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#getCreditUsage");
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
| **intervalBegin** | **Long**| Beginning of usage period formatted in unix time milliseconds. Example: 1473781817000 | [optional] |
| **intervalEnd** | **Long**| End of usage period formatted in unix time milliseconds. Example: 1473781817000 | [optional] |

### Return type

[**CreditUsage**](CreditUsage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="sendVerificationCodeToCallerId"></a>
# **sendVerificationCodeToCallerId**
> sendVerificationCodeToCallerId(callerid)

Create a caller id

Generates and sends a verification code to the phone number provided in the path. The verification code is delivered via a phone call. This code needs to be submitted to the verify caller id API endpoint to complete verification. For authentication use api credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    String callerid = "callerid_example"; // String | A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384
    try {
      apiInstance.sendVerificationCodeToCallerId(callerid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#sendVerificationCodeToCallerId");
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
| **callerid** | **String**| A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384 | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="verifyCallerId"></a>
# **verifyCallerId**
> Boolean verifyCallerId(callerid, callerIdVerificationRequest)

Verify a caller id

With the verification code received from the Create caller id endpoint, a call to this endpoint is required to finish verification. For authentication use api credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    String callerid = "callerid_example"; // String | A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384
    CallerIdVerificationRequest callerIdVerificationRequest = new CallerIdVerificationRequest(); // CallerIdVerificationRequest | request
    try {
      Boolean result = apiInstance.verifyCallerId(callerid, callerIdVerificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#verifyCallerId");
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
| **callerid** | **String**| A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384 | |
| **callerIdVerificationRequest** | [**CallerIdVerificationRequest**](CallerIdVerificationRequest.md)| request | [optional] |

### Return type

**Boolean**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

