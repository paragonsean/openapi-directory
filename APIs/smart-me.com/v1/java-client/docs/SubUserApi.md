# SubUserApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subUserDelete**](SubUserApi.md#subUserDelete) | **DELETE** /api/SubUser/{id} | Delete a subuser |
| [**subUserGet**](SubUserApi.md#subUserGet) | **GET** /api/SubUser/{id} | Get a sub user. The user must be assigend to the user that makes this call. |
| [**subUserPost**](SubUserApi.md#subUserPost) | **POST** /api/SubUser | Creates or updates a subuser.              To create a new user set no ID (empty) |


<a id="subUserDelete"></a>
# **subUserDelete**
> subUserDelete(id)

Delete a subuser

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    SubUserApi apiInstance = new SubUserApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.subUserDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubUserApi#subUserDelete");
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
| **id** | **String**|  | |

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
| **204** | No Content |  -  |

<a id="subUserGet"></a>
# **subUserGet**
> SubUserData subUserGet(id)

Get a sub user. The user must be assigend to the user that makes this call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    SubUserApi apiInstance = new SubUserApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      SubUserData result = apiInstance.subUserGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubUserApi#subUserGet");
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
| **id** | **String**|  | |

### Return type

[**SubUserData**](SubUserData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="subUserPost"></a>
# **subUserPost**
> subUserPost(subUserData)

Creates or updates a subuser.              To create a new user set no ID (empty)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    SubUserApi apiInstance = new SubUserApi(defaultClient);
    SubUserData subUserData = new SubUserData(); // SubUserData | 
    try {
      apiInstance.subUserPost(subUserData);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubUserApi#subUserPost");
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
| **subUserData** | [**SubUserData**](SubUserData.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

