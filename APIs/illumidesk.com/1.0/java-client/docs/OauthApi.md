# OauthApi

All URIs are relative to *https://api.illumidesk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oauthApplicationCreate**](OauthApi.md#oauthApplicationCreate) | **POST** /v1/{namespace}/oauth/applications/ | Create a new OAuth2 application |
| [**oauthApplicationDelete**](OauthApi.md#oauthApplicationDelete) | **DELETE** /v1/{namespace}/oauth/applications/{application}/ | Delete an application by id |
| [**oauthApplicationRead**](OauthApi.md#oauthApplicationRead) | **GET** /v1/{namespace}/oauth/applications/{application}/ | Get an application by id |
| [**oauthApplicationReplace**](OauthApi.md#oauthApplicationReplace) | **PUT** /v1/{namespace}/oauth/applications/{application}/ | Replace an application by id |
| [**oauthApplicationUpdate**](OauthApi.md#oauthApplicationUpdate) | **PATCH** /v1/{namespace}/oauth/applications/{application}/ | Update an application by id |
| [**oauthApplicationsList**](OauthApi.md#oauthApplicationsList) | **GET** /v1/{namespace}/oauth/applications/ | Retrieve oauth applications |


<a id="oauthApplicationCreate"></a>
# **oauthApplicationCreate**
> Application oauthApplicationCreate(namespace, applicationData)

Create a new OAuth2 application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    ApplicationData applicationData = new ApplicationData(); // ApplicationData | 
    try {
      Application result = apiInstance.oauthApplicationCreate(namespace, applicationData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthApplicationCreate");
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
| **namespace** | **String**| User or team name. | |
| **applicationData** | [**ApplicationData**](ApplicationData.md)|  | [optional] |

### Return type

[**Application**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Application created. |  -  |
| **400** | Invalid data supplied |  -  |

<a id="oauthApplicationDelete"></a>
# **oauthApplicationDelete**
> oauthApplicationDelete(namespace, application)

Delete an application by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String application = "application_example"; // String | Application unique identifier expressed as UUID or name.
    try {
      apiInstance.oauthApplicationDelete(namespace, application);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthApplicationDelete");
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
| **namespace** | **String**| User or team name. | |
| **application** | **String**| Application unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Application deleted. |  -  |
| **404** | Application not found. |  -  |

<a id="oauthApplicationRead"></a>
# **oauthApplicationRead**
> Application oauthApplicationRead(namespace, application)

Get an application by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String application = "application_example"; // String | Application unique identifier expressed as UUID or name.
    try {
      Application result = apiInstance.oauthApplicationRead(namespace, application);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthApplicationRead");
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
| **namespace** | **String**| User or team name. | |
| **application** | **String**| Application unique identifier expressed as UUID or name. | |

### Return type

[**Application**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Application retrieved. |  -  |
| **404** | Application not found. |  -  |

<a id="oauthApplicationReplace"></a>
# **oauthApplicationReplace**
> Application oauthApplicationReplace(namespace, application, oauthApplicationData)

Replace an application by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String application = "application_example"; // String | Application unique identifier expressed as UUID or name.
    ApplicationData oauthApplicationData = new ApplicationData(); // ApplicationData | 
    try {
      Application result = apiInstance.oauthApplicationReplace(namespace, application, oauthApplicationData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthApplicationReplace");
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
| **namespace** | **String**| User or team name. | |
| **application** | **String**| Application unique identifier expressed as UUID or name. | |
| **oauthApplicationData** | [**ApplicationData**](ApplicationData.md)|  | [optional] |

### Return type

[**Application**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Application replaced. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | Application not found |  -  |

<a id="oauthApplicationUpdate"></a>
# **oauthApplicationUpdate**
> Application oauthApplicationUpdate(namespace, application, applicationData)

Update an application by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String application = "application_example"; // String | Application unique identifier expressed as UUID or name.
    ApplicationData applicationData = new ApplicationData(); // ApplicationData | 
    try {
      Application result = apiInstance.oauthApplicationUpdate(namespace, application, applicationData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthApplicationUpdate");
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
| **namespace** | **String**| User or team name. | |
| **application** | **String**| Application unique identifier expressed as UUID or name. | |
| **applicationData** | [**ApplicationData**](ApplicationData.md)|  | [optional] |

### Return type

[**Application**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Application updated. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | Application not found. |  -  |

<a id="oauthApplicationsList"></a>
# **oauthApplicationsList**
> List&lt;Application&gt; oauthApplicationsList(namespace, limit, offset, ordering)

Retrieve oauth applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Set limit when retrieving items.
    String offset = "offset_example"; // String | Offset when retrieving items.
    String ordering = "ordering_example"; // String | Set order when retrieving items.
    try {
      List<Application> result = apiInstance.oauthApplicationsList(namespace, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthApplicationsList");
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
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Set limit when retrieving items. | [optional] |
| **offset** | **String**| Offset when retrieving items. | [optional] |
| **ordering** | **String**| Set order when retrieving items. | [optional] |

### Return type

[**List&lt;Application&gt;**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth2 application list |  -  |

