# AppsApi

All URIs are relative to *https://control.ably.net/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsAccountIdAppsGet**](AppsApi.md#accountsAccountIdAppsGet) | **GET** /accounts/{account_id}/apps | Lists apps |
| [**accountsAccountIdAppsPost**](AppsApi.md#accountsAccountIdAppsPost) | **POST** /accounts/{account_id}/apps | Creates an app |
| [**appsIdDelete**](AppsApi.md#appsIdDelete) | **DELETE** /apps/{id} | Deletes an app |
| [**appsIdPatch**](AppsApi.md#appsIdPatch) | **PATCH** /apps/{id} | Updates an app |
| [**appsIdPkcs12Post**](AppsApi.md#appsIdPkcs12Post) | **POST** /apps/{id}/pkcs12 | Updates app&#39;s APNs info from a &#x60;.p12&#x60; file |


<a id="accountsAccountIdAppsGet"></a>
# **accountsAccountIdAppsGet**
> List&lt;AppResponse&gt; accountsAccountIdAppsGet(accountId)

Lists apps

List all applications for the specified account ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accountId = "accountId_example"; // String | The account ID for which to retrieve the associated applications.
    try {
      List<AppResponse> result = apiInstance.accountsAccountIdAppsGet(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#accountsAccountIdAppsGet");
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
| **accountId** | **String**| The account ID for which to retrieve the associated applications. | |

### Return type

[**List&lt;AppResponse&gt;**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of apps for the specified account are returned |  -  |
| **401** | Authentication failed |  -  |
| **404** | Account not found |  -  |
| **500** | Internal server error |  -  |

<a id="accountsAccountIdAppsPost"></a>
# **accountsAccountIdAppsPost**
> AppResponse accountsAccountIdAppsPost(accountId, appPost)

Creates an app

Creates an application with the specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accountId = "accountId_example"; // String | The account ID of the account in which to create the application.
    AppPost appPost = new AppPost(); // AppPost | 
    try {
      AppResponse result = apiInstance.accountsAccountIdAppsPost(accountId, appPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#accountsAccountIdAppsPost");
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
| **accountId** | **String**| The account ID of the account in which to create the application. | |
| **appPost** | [**AppPost**](AppPost.md)|  | [optional] |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | App created |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | Account not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |

<a id="appsIdDelete"></a>
# **appsIdDelete**
> appsIdDelete(id)

Deletes an app

Deletes the application with the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | The ID of the application to be deleted.
    try {
      apiInstance.appsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsIdDelete");
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
| **id** | **String**| The ID of the application to be deleted. | |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | App deleted |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |

<a id="appsIdPatch"></a>
# **appsIdPatch**
> AppResponse appsIdPatch(id, appPatch)

Updates an app

Updates the application with the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | The ID of application to be updated.
    AppPatch appPatch = new AppPatch(); // AppPatch | 
    try {
      AppResponse result = apiInstance.appsIdPatch(id, appPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsIdPatch");
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
| **id** | **String**| The ID of application to be updated. | |
| **appPatch** | [**AppPatch**](AppPatch.md)|  | [optional] |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | App updated |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |

<a id="appsIdPkcs12Post"></a>
# **appsIdPkcs12Post**
> AppResponse appsIdPkcs12Post(id, p12File, p12Pass)

Updates app&#39;s APNs info from a &#x60;.p12&#x60; file

Updates the application&#39;s Apple Push Notification service (APNs) information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | The application ID.
    File p12File = new File("/path/to/file"); // File | The `.p12` file containing the app's APNs information.
    String p12Pass = "p12Pass_example"; // String | The password for the corresponding `.p12` file.
    try {
      AppResponse result = apiInstance.appsIdPkcs12Post(id, p12File, p12Pass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsIdPkcs12Post");
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
| **id** | **String**| The application ID. | |
| **p12File** | **File**| The &#x60;.p12&#x60; file containing the app&#39;s APNs information. | |
| **p12Pass** | **String**| The password for the corresponding &#x60;.p12&#x60; file. | |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | App updated |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |

