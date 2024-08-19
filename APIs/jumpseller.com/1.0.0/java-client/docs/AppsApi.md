# AppsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jsappsCodeJsonDelete**](AppsApi.md#jsappsCodeJsonDelete) | **DELETE** /jsapps/{code}.json | Delete an existing JSApp. |
| [**jsappsCodeJsonGet**](AppsApi.md#jsappsCodeJsonGet) | **GET** /jsapps/{code}.json | Retrieve a JSApp. |
| [**jsappsJsonGet**](AppsApi.md#jsappsJsonGet) | **GET** /jsapps.json | Retrieve all the Store&#39;s JSApps. |
| [**jsappsJsonPost**](AppsApi.md#jsappsJsonPost) | **POST** /jsapps.json | Create a Store JSApp. |


<a id="jsappsCodeJsonDelete"></a>
# **jsappsCodeJsonDelete**
> String jsappsCodeJsonDelete(login, authtoken, code)

Delete an existing JSApp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String code = "code_example"; // String | Code of the App
    try {
      String result = apiInstance.jsappsCodeJsonDelete(login, authtoken, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#jsappsCodeJsonDelete");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **code** | **String**| Code of the App | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | App Not Found. |  -  |

<a id="jsappsCodeJsonGet"></a>
# **jsappsCodeJsonGet**
> JSApp jsappsCodeJsonGet(login, authtoken, code)

Retrieve a JSApp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String code = "code_example"; // String | Code of the App
    try {
      JSApp result = apiInstance.jsappsCodeJsonGet(login, authtoken, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#jsappsCodeJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **code** | **String**| Code of the App | |

### Return type

[**JSApp**](JSApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="jsappsJsonGet"></a>
# **jsappsJsonGet**
> App jsappsJsonGet(login, authtoken)

Retrieve all the Store&#39;s JSApps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    try {
      App result = apiInstance.jsappsJsonGet(login, authtoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#jsappsJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |

### Return type

[**App**](App.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="jsappsJsonPost"></a>
# **jsappsJsonPost**
> JSApp jsappsJsonPost(login, authtoken, jsAppEdit)

Create a Store JSApp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    JSAppEdit jsAppEdit = new JSAppEdit(); // JSAppEdit | JSApp parameters to create
    try {
      JSApp result = apiInstance.jsappsJsonPost(login, authtoken, jsAppEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#jsappsJsonPost");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **jsAppEdit** | [**JSAppEdit**](JSAppEdit.md)| JSApp parameters to create | |

### Return type

[**JSApp**](JSApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

