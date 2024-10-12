# PayorsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPayorByIdV1**](PayorsApi.md#getPayorByIdV1) | **GET** /v1/payors/{payorId} | Get Payor |
| [**getPayorByIdV2**](PayorsApi.md#getPayorByIdV2) | **GET** /v2/payors/{payorId} | Get Payor |
| [**payorAddPayorLogoV1**](PayorsApi.md#payorAddPayorLogoV1) | **POST** /v1/payors/{payorId}/branding/logos | Add Logo |
| [**payorCreateApiKeyV1**](PayorsApi.md#payorCreateApiKeyV1) | **POST** /v1/payors/{payorId}/applications/{applicationId}/keys | Create API Key |
| [**payorCreateApplicationV1**](PayorsApi.md#payorCreateApplicationV1) | **POST** /v1/payors/{payorId}/applications | Create Application |
| [**payorEmailOptOut**](PayorsApi.md#payorEmailOptOut) | **POST** /v1/payors/{payorId}/reminderEmailsUpdate | Reminder Email Opt-Out |
| [**payorGetBranding**](PayorsApi.md#payorGetBranding) | **GET** /v1/payors/{payorId}/branding | Get Branding |


<a id="getPayorByIdV1"></a>
# **getPayorByIdV1**
> PayorV1 getPayorByIdV1(payorId)

Get Payor

&lt;p&gt;Get a Single Payor by Id.&lt;/p&gt; &lt;p&gt;deprecated since v2.10 - Use /v2/payors 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayorsApi apiInstance = new PayorsApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor Id
    try {
      PayorV1 result = apiInstance.getPayorByIdV1(payorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayorsApi#getPayorByIdV1");
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
| **payorId** | **UUID**| The Payor Id | |

### Return type

[**PayorV1**](PayorV1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Payor Details |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | Payor Id Not Found |  -  |

<a id="getPayorByIdV2"></a>
# **getPayorByIdV2**
> PayorV2 getPayorByIdV2(payorId)

Get Payor

Get a Single Payor by Id. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayorsApi apiInstance = new PayorsApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor Id
    try {
      PayorV2 result = apiInstance.getPayorByIdV2(payorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayorsApi#getPayorByIdV2");
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
| **payorId** | **UUID**| The Payor Id | |

### Return type

[**PayorV2**](PayorV2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Payor Details |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | Payor Id Not Found |  -  |

<a id="payorAddPayorLogoV1"></a>
# **payorAddPayorLogoV1**
> payorAddPayorLogoV1(payorId, logo)

Add Logo

&lt;p&gt;Add Payor Logo&lt;/p&gt; &lt;p&gt;Logo file is used in your branding and emails sent to payees&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayorsApi apiInstance = new PayorsApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor Id
    File logo = new File("/path/to/file"); // File | 
    try {
      apiInstance.payorAddPayorLogoV1(payorId, logo);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayorsApi#payorAddPayorLogoV1");
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
| **payorId** | **UUID**| The Payor Id | |
| **logo** | **File**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="payorCreateApiKeyV1"></a>
# **payorCreateApiKeyV1**
> PayorCreateApiKeyResponse payorCreateApiKeyV1(payorId, applicationId, payorCreateApiKeyRequest)

Create API Key

&lt;p&gt;Create an an API key for the given payor Id and application Id&lt;/p&gt; &lt;p&gt;You can create multiple API Keys for a given application&lt;/p&gt; &lt;p&gt;API Keys are programmatic users for integrating your application with the Velo platform&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayorsApi apiInstance = new PayorsApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor Id
    UUID applicationId = UUID.randomUUID(); // UUID | Application ID
    PayorCreateApiKeyRequest payorCreateApiKeyRequest = new PayorCreateApiKeyRequest(); // PayorCreateApiKeyRequest | Details of application API key to create
    try {
      PayorCreateApiKeyResponse result = apiInstance.payorCreateApiKeyV1(payorId, applicationId, payorCreateApiKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayorsApi#payorCreateApiKeyV1");
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
| **payorId** | **UUID**| The Payor Id | |
| **applicationId** | **UUID**| Application ID | |
| **payorCreateApiKeyRequest** | [**PayorCreateApiKeyRequest**](PayorCreateApiKeyRequest.md)| Details of application API key to create | |

### Return type

[**PayorCreateApiKeyResponse**](PayorCreateApiKeyResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HTTP Ok, key created |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="payorCreateApplicationV1"></a>
# **payorCreateApplicationV1**
> payorCreateApplicationV1(payorId, payorCreateApplicationRequest)

Create Application

&lt;p&gt;Create an application for the given Payor ID.&lt;/p&gt; &lt;p&gt;Applications provide a means to group your API Keys&lt;/p&gt; &lt;p&gt;For example you might have an SAP application that you wish to integrate with Velo&lt;/p&gt; &lt;p&gt;You can create an application and then create one or more API keys for the application&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayorsApi apiInstance = new PayorsApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor Id
    PayorCreateApplicationRequest payorCreateApplicationRequest = new PayorCreateApplicationRequest(); // PayorCreateApplicationRequest | Details of application to create
    try {
      apiInstance.payorCreateApplicationV1(payorId, payorCreateApplicationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayorsApi#payorCreateApplicationV1");
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
| **payorId** | **UUID**| The Payor Id | |
| **payorCreateApplicationRequest** | [**PayorCreateApplicationRequest**](PayorCreateApplicationRequest.md)| Details of application to create | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  * Location - location <br>  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="payorEmailOptOut"></a>
# **payorEmailOptOut**
> payorEmailOptOut(payorId, payorEmailOptOutRequest)

Reminder Email Opt-Out

Update the emailRemindersOptOut field for a Payor. This API can be used to opt out or opt into Payor Reminder emails. These emails are typically around payee events such as payees registering and onboarding. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayorsApi apiInstance = new PayorsApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor Id
    PayorEmailOptOutRequest payorEmailOptOutRequest = new PayorEmailOptOutRequest(); // PayorEmailOptOutRequest | Reminder Emails Opt-Out Request
    try {
      apiInstance.payorEmailOptOut(payorId, payorEmailOptOutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayorsApi#payorEmailOptOut");
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
| **payorId** | **UUID**| The Payor Id | |
| **payorEmailOptOutRequest** | [**PayorEmailOptOutRequest**](PayorEmailOptOutRequest.md)| Reminder Emails Opt-Out Request | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | HTTP Accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | Payor Id Not Found |  -  |

<a id="payorGetBranding"></a>
# **payorGetBranding**
> PayorBrandingResponse payorGetBranding(payorId)

Get Branding

Get the payor branding details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayorsApi apiInstance = new PayorsApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor Id
    try {
      PayorBrandingResponse result = apiInstance.payorGetBranding(payorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayorsApi#payorGetBranding");
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
| **payorId** | **UUID**| The Payor Id | |

### Return type

[**PayorBrandingResponse**](PayorBrandingResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HTTP Ok, key created |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | Payor Id Not Found |  -  |

