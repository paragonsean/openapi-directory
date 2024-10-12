# AuthenticationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expireAllApiV1AuthAppAppIdExpireAllPost**](AuthenticationApi.md#expireAllApiV1AuthAppAppIdExpireAllPost) | **POST** /api/v1/auth/app/{app_id}/expire-all/ | Expire All |
| [**getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost**](AuthenticationApi.md#getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost) | **POST** /api/v1/auth/app-portal-access/{app_id}/ | Get Consumer App Portal Access |
| [**getDashboardAccessApiV1AuthDashboardAccessAppIdPost**](AuthenticationApi.md#getDashboardAccessApiV1AuthDashboardAccessAppIdPost) | **POST** /api/v1/auth/dashboard-access/{app_id}/ | Get Dashboard Access |
| [**logoutApiV1AuthLogoutPost**](AuthenticationApi.md#logoutApiV1AuthLogoutPost) | **POST** /api/v1/auth/logout/ | Logout |


<a id="expireAllApiV1AuthAppAppIdExpireAllPost"></a>
# **expireAllApiV1AuthAppAppIdExpireAllPost**
> expireAllApiV1AuthAppAppIdExpireAllPost(appId, applicationTokenExpireIn, idempotencyKey)

Expire All

Expire all of the tokens associated with a specific Application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    ApplicationTokenExpireIn applicationTokenExpireIn = new ApplicationTokenExpireIn(); // ApplicationTokenExpireIn | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      apiInstance.expireAllApiV1AuthAppAppIdExpireAllPost(appId, applicationTokenExpireIn, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#expireAllApiV1AuthAppAppIdExpireAllPost");
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
| **appId** | **String**|  | |
| **applicationTokenExpireIn** | [**ApplicationTokenExpireIn**](ApplicationTokenExpireIn.md)|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost"></a>
# **getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost**
> AppPortalAccessOut getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost(appId, appPortalAccessIn, idempotencyKey)

Get Consumer App Portal Access

Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    AppPortalAccessIn appPortalAccessIn = new AppPortalAccessIn(); // AppPortalAccessIn | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      AppPortalAccessOut result = apiInstance.getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost(appId, appPortalAccessIn, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost");
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
| **appId** | **String**|  | |
| **appPortalAccessIn** | [**AppPortalAccessIn**](AppPortalAccessIn.md)|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**AppPortalAccessOut**](AppPortalAccessOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="getDashboardAccessApiV1AuthDashboardAccessAppIdPost"></a>
# **getDashboardAccessApiV1AuthDashboardAccessAppIdPost**
> DashboardAccessOut getDashboardAccessApiV1AuthDashboardAccessAppIdPost(appId, idempotencyKey)

Get Dashboard Access

DEPRECATED: Please use &#x60;app-portal-access&#x60; instead.  Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      DashboardAccessOut result = apiInstance.getDashboardAccessApiV1AuthDashboardAccessAppIdPost(appId, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#getDashboardAccessApiV1AuthDashboardAccessAppIdPost");
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
| **appId** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**DashboardAccessOut**](DashboardAccessOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="logoutApiV1AuthLogoutPost"></a>
# **logoutApiV1AuthLogoutPost**
> logoutApiV1AuthLogoutPost(idempotencyKey)

Logout

Logout an app token.  Trying to log out other tokens will fail.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      apiInstance.logoutApiV1AuthLogoutPost(idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#logoutApiV1AuthLogoutPost");
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
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

