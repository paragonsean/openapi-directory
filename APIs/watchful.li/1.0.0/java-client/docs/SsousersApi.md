# SsousersApi

All URIs are relative to *https://watchful.li/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSsoUsers**](SsousersApi.md#createSsoUsers) | **POST** /ssousers | Create a SSO User |
| [**deleteSsoUserById**](SsousersApi.md#deleteSsoUserById) | **DELETE** /ssousers/{id} | Delete a specific SSO User |
| [**getSsoUsers**](SsousersApi.md#getSsoUsers) | **GET** /ssousers | Get a list of SSO Users |
| [**getSsoUsersById**](SsousersApi.md#getSsoUsersById) | **GET** /ssousers/{id} | Find SSO User by ID |
| [**updateSsoUsers**](SsousersApi.md#updateSsoUsers) | **PUT** /ssousers/{id} | Update a SSO User |


<a id="createSsoUsers"></a>
# **createSsoUsers**
> SsoUsers createSsoUsers(body)

Create a SSO User

Create a SSO User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsousersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SsousersApi apiInstance = new SsousersApi(defaultClient);
    SsoUsers body = new SsoUsers(); // SsoUsers | JSON object SsoUsers
    try {
      SsoUsers result = apiInstance.createSsoUsers(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsousersApi#createSsoUsers");
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
| **body** | [**SsoUsers**](SsoUsers.md)| JSON object SsoUsers | |

### Return type

[**SsoUsers**](SsoUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Saved successfully |  -  |
| **400** | Invalid data |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Not saved |  -  |

<a id="deleteSsoUserById"></a>
# **deleteSsoUserById**
> String deleteSsoUserById(id)

Delete a specific SSO User

Delete a specific SSO User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsousersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SsousersApi apiInstance = new SsousersApi(defaultClient);
    Long id = 56L; // Long | ID of SSO User that needs to be deleted
    try {
      String result = apiInstance.deleteSsoUserById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsousersApi#deleteSsoUserById");
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
| **id** | **Long**| ID of SSO User that needs to be deleted | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSO User correctly deleted |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getSsoUsers"></a>
# **getSsoUsers**
> SsoUsers getSsoUsers()

Get a list of SSO Users

Returns a list of SSO Users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsousersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SsousersApi apiInstance = new SsousersApi(defaultClient);
    try {
      SsoUsers result = apiInstance.getSsoUsers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsousersApi#getSsoUsers");
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

[**SsoUsers**](SsoUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |

<a id="getSsoUsersById"></a>
# **getSsoUsersById**
> SsoUsers getSsoUsersById(id, fields)

Find SSO User by ID

Returns a SSO User based on ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsousersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SsousersApi apiInstance = new SsousersApi(defaultClient);
    Long id = 56L; // Long | ID of SSO User that needs to be fetched
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    try {
      SsoUsers result = apiInstance.getSsoUsersById(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsousersApi#getSsoUsersById");
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
| **id** | **Long**| ID of SSO User that needs to be fetched | |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |

### Return type

[**SsoUsers**](SsoUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **400** | Invalid ID |  -  |
| **403** | Invalid API Key |  -  |

<a id="updateSsoUsers"></a>
# **updateSsoUsers**
> SsoUsers updateSsoUsers(id, body)

Update a SSO User

Update a SSO User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsousersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    SsousersApi apiInstance = new SsousersApi(defaultClient);
    Long id = 56L; // Long | ID of SSO User that needs to be updated
    SsoUsers body = new SsoUsers(); // SsoUsers | JSON object SsoUsers
    try {
      SsoUsers result = apiInstance.updateSsoUsers(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsousersApi#updateSsoUsers");
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
| **id** | **Long**| ID of SSO User that needs to be updated | |
| **body** | [**SsoUsers**](SsoUsers.md)| JSON object SsoUsers | |

### Return type

[**SsoUsers**](SsoUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Updated successfully |  -  |
| **400** | Invalid data |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Not saved |  -  |

