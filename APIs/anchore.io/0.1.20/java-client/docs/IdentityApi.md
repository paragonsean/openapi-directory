# IdentityApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addCredential**](IdentityApi.md#addCredential) | **POST** /user/credentials | add/replace credential |
| [**getCredentials**](IdentityApi.md#getCredentials) | **GET** /user/credentials | Get current credential summary |
| [**getUser**](IdentityApi.md#getUser) | **GET** /user | List authenticated user info |
| [**getUsersAccount**](IdentityApi.md#getUsersAccount) | **GET** /account | List the account for the authenticated user |


<a id="addCredential"></a>
# **addCredential**
> User addCredential(accessCredential)

add/replace credential

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    AccessCredential accessCredential = new AccessCredential(); // AccessCredential | 
    try {
      User result = apiInstance.addCredential(accessCredential);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#addCredential");
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
| **accessCredential** | [**AccessCredential**](AccessCredential.md)|  | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Add a credential, overwritting if already exists |  -  |
| **500** | Internal error |  -  |

<a id="getCredentials"></a>
# **getCredentials**
> List&lt;AccessCredential&gt; getCredentials()

Get current credential summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    try {
      List<AccessCredential> result = apiInstance.getCredentials();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#getCredentials");
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

[**List&lt;AccessCredential&gt;**](AccessCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User credential listing |  -  |
| **500** | Internal error |  -  |

<a id="getUser"></a>
# **getUser**
> User getUser()

List authenticated user info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    try {
      User result = apiInstance.getUser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#getUser");
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

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User details for caller&#39;s user |  -  |
| **500** | Internal error |  -  |

<a id="getUsersAccount"></a>
# **getUsersAccount**
> Account getUsersAccount()

List the account for the authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    try {
      Account result = apiInstance.getUsersAccount();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#getUsersAccount");
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

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User details for caller&#39;s user |  -  |
| **500** | Internal error |  -  |

