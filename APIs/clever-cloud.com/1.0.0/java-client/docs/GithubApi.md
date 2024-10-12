# GithubApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteGithubLink_0**](GithubApi.md#deleteGithubLink_0) | **DELETE** /github/link |  |
| [**getGithubApplications_1**](GithubApi.md#getGithubApplications_1) | **GET** /github/applications |  |
| [**getGithubCallback_0**](GithubApi.md#getGithubCallback_0) | **GET** /github/callback |  |
| [**getGithubEmails_0**](GithubApi.md#getGithubEmails_0) | **GET** /github/emails |  |
| [**getGithubKeys_0**](GithubApi.md#getGithubKeys_0) | **GET** /github/keys |  |
| [**getGithubLink_0**](GithubApi.md#getGithubLink_0) | **GET** /github/link |  |
| [**getGithubLogin_0**](GithubApi.md#getGithubLogin_0) | **GET** /github/login |  |
| [**getGithubSignup_0**](GithubApi.md#getGithubSignup_0) | **GET** /github/signup |  |
| [**getGithubUsername_0**](GithubApi.md#getGithubUsername_0) | **GET** /github/username |  |
| [**getGithub_0**](GithubApi.md#getGithub_0) | **GET** /github |  |
| [**postGithubRedeploy_0**](GithubApi.md#postGithubRedeploy_0) | **POST** /github/redeploy |  |
| [**postGithubSignup_0**](GithubApi.md#postGithubSignup_0) | **POST** /github/signup |  |


<a id="deleteGithubLink_0"></a>
# **deleteGithubLink_0**
> deleteGithubLink_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    try {
      apiInstance.deleteGithubLink_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#deleteGithubLink_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unlinkGithub |  -  |

<a id="getGithubApplications_1"></a>
# **getGithubApplications_1**
> List&lt;Application&gt; getGithubApplications_1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    try {
      List<Application> result = apiInstance.getGithubApplications_1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#getGithubApplications_1");
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

[**List&lt;Application&gt;**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getGithubApplications |  -  |

<a id="getGithubCallback_0"></a>
# **getGithubCallback_0**
> getGithubCallback_0(code, state, error, errorDescription, errorUri, cookie)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    String code = "code_example"; // String | 
    String state = "state_example"; // String | 
    String error = "error_example"; // String | 
    String errorDescription = "errorDescription_example"; // String | 
    String errorUri = "errorUri_example"; // String | 
    String cookie = "cookie_example"; // String | 
    try {
      apiInstance.getGithubCallback_0(code, state, error, errorDescription, errorUri, cookie);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#getGithubCallback_0");
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
| **code** | **String**|  | [optional] |
| **state** | **String**|  | [optional] |
| **error** | **String**|  | [optional] |
| **errorDescription** | **String**|  | [optional] |
| **errorUri** | **String**|  | [optional] |
| **cookie** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | githubCallback |  -  |

<a id="getGithubEmails_0"></a>
# **getGithubEmails_0**
> List&lt;String&gt; getGithubEmails_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    try {
      List<String> result = apiInstance.getGithubEmails_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#getGithubEmails_0");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getGithubEmails |  -  |

<a id="getGithubKeys_0"></a>
# **getGithubKeys_0**
> List&lt;Key&gt; getGithubKeys_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    try {
      List<Key> result = apiInstance.getGithubKeys_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#getGithubKeys_0");
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

[**List&lt;Key&gt;**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getGithubKeys |  -  |

<a id="getGithubLink_0"></a>
# **getGithubLink_0**
> getGithubLink_0(transactionId, redirectUrl)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    String transactionId = "transactionId_example"; // String | From GET /github
    String redirectUrl = "redirectUrl_example"; // String | 
    try {
      apiInstance.getGithubLink_0(transactionId, redirectUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#getGithubLink_0");
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
| **transactionId** | **String**| From GET /github | [optional] |
| **redirectUrl** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | linkGithub |  -  |

<a id="getGithubLogin_0"></a>
# **getGithubLogin_0**
> getGithubLogin_0(redirectUrl, fromAuthorize)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    String redirectUrl = "redirectUrl_example"; // String | 
    String fromAuthorize = "fromAuthorize_example"; // String | 
    try {
      apiInstance.getGithubLogin_0(redirectUrl, fromAuthorize);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#getGithubLogin_0");
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
| **redirectUrl** | **String**|  | [optional] |
| **fromAuthorize** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | githubLogin |  -  |

<a id="getGithubSignup_0"></a>
# **getGithubSignup_0**
> getGithubSignup_0(redirectUrl, fromAuthorize)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    String redirectUrl = "redirectUrl_example"; // String | 
    String fromAuthorize = "fromAuthorize_example"; // String | 
    try {
      apiInstance.getGithubSignup_0(redirectUrl, fromAuthorize);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#getGithubSignup_0");
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
| **redirectUrl** | **String**|  | [optional] |
| **fromAuthorize** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | githubSignup |  -  |

<a id="getGithubUsername_0"></a>
# **getGithubUsername_0**
> String getGithubUsername_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    try {
      String result = apiInstance.getGithubUsername_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#getGithubUsername_0");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getGithubUsername |  -  |

<a id="getGithub_0"></a>
# **getGithub_0**
> TransactionId getGithub_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    try {
      TransactionId result = apiInstance.getGithub_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#getGithub_0");
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

[**TransactionId**](TransactionId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | startGithub |  -  |

<a id="postGithubRedeploy_0"></a>
# **postGithubRedeploy_0**
> postGithubRedeploy_0(userAgent, xGithubEvent, xHubSignature)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    String userAgent = "userAgent_example"; // String | 
    String xGithubEvent = "xGithubEvent_example"; // String | 
    String xHubSignature = "xHubSignature_example"; // String | 
    try {
      apiInstance.postGithubRedeploy_0(userAgent, xGithubEvent, xHubSignature);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#postGithubRedeploy_0");
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
| **userAgent** | **String**|  | [optional] |
| **xGithubEvent** | **String**|  | [optional] |
| **xHubSignature** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | redeployApp |  -  |

<a id="postGithubSignup_0"></a>
# **postGithubSignup_0**
> postGithubSignup_0(transactionId, name, otherId, otherEmail, password, autoLink, terms)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GithubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    GithubApi apiInstance = new GithubApi(defaultClient);
    String transactionId = "transactionId_example"; // String | 
    String name = "name_example"; // String | 
    String otherId = "otherId_example"; // String | 
    String otherEmail = "otherEmail_example"; // String | 
    String password = "password_example"; // String | 
    String autoLink = "autoLink_example"; // String | 
    String terms = "terms_example"; // String | 
    try {
      apiInstance.postGithubSignup_0(transactionId, name, otherId, otherEmail, password, autoLink, terms);
    } catch (ApiException e) {
      System.err.println("Exception when calling GithubApi#postGithubSignup_0");
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
| **transactionId** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **otherId** | **String**|  | [optional] |
| **otherEmail** | **String**|  | [optional] |
| **password** | **String**|  | [optional] |
| **autoLink** | **String**|  | [optional] |
| **terms** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | finsihGithubSignup |  -  |

