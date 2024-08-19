# TemplatesApi

All URIs are relative to *https://api.sakari.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**templatesCreate**](TemplatesApi.md#templatesCreate) | **POST** /v1/accounts/{accountId}/templates | Create template |
| [**templatesFetch**](TemplatesApi.md#templatesFetch) | **GET** /v1/accounts/{accountId}/templates/{templateId} | Fetch template by ID |
| [**templatesFetchAll**](TemplatesApi.md#templatesFetchAll) | **GET** /v1/accounts/{accountId}/templates | Fetch templates |
| [**templatesRemove**](TemplatesApi.md#templatesRemove) | **DELETE** /v1/accounts/{accountId}/templates/{templateId} | Deletes a template |
| [**templatesUpdate**](TemplatesApi.md#templatesUpdate) | **PUT** /v1/accounts/{accountId}/templates/{templateId} | Updates a template |


<a id="templatesCreate"></a>
# **templatesCreate**
> TemplatesResponse templatesCreate(accountId, templateRequest)

Create template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    TemplateRequest templateRequest = new TemplateRequest(); // TemplateRequest | 
    try {
      TemplatesResponse result = apiInstance.templatesCreate(accountId, templateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#templatesCreate");
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
| **accountId** | **String**| Account to apply operations to | |
| **templateRequest** | [**TemplateRequest**](TemplateRequest.md)|  | [optional] |

### Return type

[**TemplatesResponse**](TemplatesResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |

<a id="templatesFetch"></a>
# **templatesFetch**
> TemplateResponse templatesFetch(accountId, templateId)

Fetch template by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String templateId = "templateId_example"; // String | ID of template to return
    try {
      TemplateResponse result = apiInstance.templatesFetch(accountId, templateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#templatesFetch");
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
| **accountId** | **String**| Account to apply operations to | |
| **templateId** | **String**| ID of template to return | |

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="templatesFetchAll"></a>
# **templatesFetchAll**
> TemplatesResponse templatesFetchAll(accountId, offset, limit, name)

Fetch templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    Long offset = 56L; // Long | Results to skip when paginating through a result set
    Long limit = 56L; // Long | Maximum number of results to return
    String name = "name_example"; // String | Filter by name or part of
    try {
      TemplatesResponse result = apiInstance.templatesFetchAll(accountId, offset, limit, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#templatesFetchAll");
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
| **accountId** | **String**| Account to apply operations to | |
| **offset** | **Long**| Results to skip when paginating through a result set | [optional] |
| **limit** | **Long**| Maximum number of results to return | [optional] |
| **name** | **String**| Filter by name or part of | [optional] |

### Return type

[**TemplatesResponse**](TemplatesResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **4XX** | invalid request |  -  |
| **5XX** | invalid request |  -  |

<a id="templatesRemove"></a>
# **templatesRemove**
> CampaignsRemove200Response templatesRemove(accountId, templateId)

Deletes a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String templateId = "templateId_example"; // String | Template id to delete
    try {
      CampaignsRemove200Response result = apiInstance.templatesRemove(accountId, templateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#templatesRemove");
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
| **accountId** | **String**| Account to apply operations to | |
| **templateId** | **String**| Template id to delete | |

### Return type

[**CampaignsRemove200Response**](CampaignsRemove200Response.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="templatesUpdate"></a>
# **templatesUpdate**
> TemplateResponse templatesUpdate(accountId, templateId)

Updates a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String templateId = "templateId_example"; // String | ID of template
    try {
      TemplateResponse result = apiInstance.templatesUpdate(accountId, templateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#templatesUpdate");
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
| **accountId** | **String**| Account to apply operations to | |
| **templateId** | **String**| ID of template | |

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

