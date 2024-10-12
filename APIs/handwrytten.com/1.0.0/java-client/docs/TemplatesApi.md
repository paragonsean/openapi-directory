# TemplatesApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTemplate**](TemplatesApi.md#createTemplate) | **POST** /templates/create | Creates a New Template in the User’s Account |
| [**deleteTemplate**](TemplatesApi.md#deleteTemplate) | **POST** /templates/delete | Deletes a users template |
| [**getTemplateCategories**](TemplatesApi.md#getTemplateCategories) | **GET** /templateCategories/list | List template categories |
| [**getTemplateCategoriesAuthorized**](TemplatesApi.md#getTemplateCategoriesAuthorized) | **POST** /templateCategories/list | List template categories |
| [**getTemplateDetail**](TemplatesApi.md#getTemplateDetail) | **POST** /templates/view | Get all info on a template |
| [**getTemplates**](TemplatesApi.md#getTemplates) | **GET** /templates/list | List template categories |
| [**getTemplatessAuthorized**](TemplatesApi.md#getTemplatessAuthorized) | **POST** /templates/list | List template categories |
| [**updateTemplate**](TemplatesApi.md#updateTemplate) | **POST** /templates/update | Updates an Existing Template in the User’s Account |


<a id="createTemplate"></a>
# **createTemplate**
> List&lt;Template&gt; createTemplate(body)

Creates a New Template in the User’s Account

Creates a new Template in the User’s Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    CreateTemplateRequest body = new CreateTemplateRequest(); // CreateTemplateRequest | additional parameters
    try {
      List<Template> result = apiInstance.createTemplate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#createTemplate");
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
| **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)| additional parameters | |

### Return type

[**List&lt;Template&gt;**](Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="deleteTemplate"></a>
# **deleteTemplate**
> ChangePassword200Response deleteTemplate(body)

Deletes a users template

Deletes a template in the User’s Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    DeleteTemplateRequest body = new DeleteTemplateRequest(); // DeleteTemplateRequest | additional parameters
    try {
      ChangePassword200Response result = apiInstance.deleteTemplate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#deleteTemplate");
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
| **body** | [**DeleteTemplateRequest**](DeleteTemplateRequest.md)| additional parameters | |

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful deletion |  -  |

<a id="getTemplateCategories"></a>
# **getTemplateCategories**
> List&lt;TemplateCategory&gt; getTemplateCategories()

List template categories

Lists the common template categories of all users. As you are not logged in, this is what you are limited to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    try {
      List<TemplateCategory> result = apiInstance.getTemplateCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplateCategories");
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

[**List&lt;TemplateCategory&gt;**](TemplateCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getTemplateCategoriesAuthorized"></a>
# **getTemplateCategoriesAuthorized**
> List&lt;TemplateCategory&gt; getTemplateCategoriesAuthorized(body)

List template categories

Lists the template categories of all users. By passing the optional UID, any custom template categories are also available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    GetTemplateCategoriesAuthorizedRequest body = new GetTemplateCategoriesAuthorizedRequest(); // GetTemplateCategoriesAuthorizedRequest | additional parameters
    try {
      List<TemplateCategory> result = apiInstance.getTemplateCategoriesAuthorized(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplateCategoriesAuthorized");
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
| **body** | [**GetTemplateCategoriesAuthorizedRequest**](GetTemplateCategoriesAuthorizedRequest.md)| additional parameters | [optional] |

### Return type

[**List&lt;TemplateCategory&gt;**](TemplateCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getTemplateDetail"></a>
# **getTemplateDetail**
> Template getTemplateDetail(body)

Get all info on a template

Provides all details on a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    GetTemplateDetailRequest body = new GetTemplateDetailRequest(); // GetTemplateDetailRequest | additional parameters
    try {
      Template result = apiInstance.getTemplateDetail(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplateDetail");
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
| **body** | [**GetTemplateDetailRequest**](GetTemplateDetailRequest.md)| additional parameters | |

### Return type

[**Template**](Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getTemplates"></a>
# **getTemplates**
> List&lt;Template&gt; getTemplates()

List template categories

Lists the common template categories of all users. As you are not logged in, this is what you are limited to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    try {
      List<Template> result = apiInstance.getTemplates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplates");
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

[**List&lt;Template&gt;**](Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getTemplatessAuthorized"></a>
# **getTemplatessAuthorized**
> List&lt;Template&gt; getTemplatessAuthorized(body)

List template categories

Lists the template categories of all users. By passing the optional UID, any custom template categories are also available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    GetTemplatessAuthorizedRequest body = new GetTemplatessAuthorizedRequest(); // GetTemplatessAuthorizedRequest | additional parameters
    try {
      List<Template> result = apiInstance.getTemplatessAuthorized(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getTemplatessAuthorized");
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
| **body** | [**GetTemplatessAuthorizedRequest**](GetTemplatessAuthorizedRequest.md)| additional parameters | [optional] |

### Return type

[**List&lt;Template&gt;**](Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="updateTemplate"></a>
# **updateTemplate**
> List&lt;Template&gt; updateTemplate(body)

Updates an Existing Template in the User’s Account

Updates an Existing Template in the User’s Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    UpdateTemplateRequest body = new UpdateTemplateRequest(); // UpdateTemplateRequest | additional parameters
    try {
      List<Template> result = apiInstance.updateTemplate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#updateTemplate");
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
| **body** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)| additional parameters | |

### Return type

[**List&lt;Template&gt;**](Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

