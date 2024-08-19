# AttributeTemplateApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attributeTemplateCreateAttributeTemplate**](AttributeTemplateApi.md#attributeTemplateCreateAttributeTemplate) | **POST** /attributetemplates/{webId}/attributetemplates | Create an attribute template as a child of another attribute template. |
| [**attributeTemplateDelete**](AttributeTemplateApi.md#attributeTemplateDelete) | **DELETE** /attributetemplates/{webId} | Delete an attribute template. |
| [**attributeTemplateGet**](AttributeTemplateApi.md#attributeTemplateGet) | **GET** /attributetemplates/{webId} | Retrieve an attribute template. |
| [**attributeTemplateGetAttributeTemplates**](AttributeTemplateApi.md#attributeTemplateGetAttributeTemplates) | **GET** /attributetemplates/{webId}/attributetemplates | Retrieve an attribute template&#39;s child attribute templates. |
| [**attributeTemplateGetByPath**](AttributeTemplateApi.md#attributeTemplateGetByPath) | **GET** /attributetemplates | Retrieve an attribute template by path. |
| [**attributeTemplateGetCategories**](AttributeTemplateApi.md#attributeTemplateGetCategories) | **GET** /attributetemplates/{webId}/categories | Get an attribute template&#39;s categories. |
| [**attributeTemplateUpdate**](AttributeTemplateApi.md#attributeTemplateUpdate) | **PATCH** /attributetemplates/{webId} | Update an existing attribute template by replacing items in its definition. |


<a id="attributeTemplateCreateAttributeTemplate"></a>
# **attributeTemplateCreateAttributeTemplate**
> attributeTemplateCreateAttributeTemplate(webId, template, webIdType)

Create an attribute template as a child of another attribute template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeTemplateApi apiInstance = new AttributeTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the parent attribute template on which to create the attribute template.
    AttributeTemplate template = new AttributeTemplate(); // AttributeTemplate | The attribute template definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.attributeTemplateCreateAttributeTemplate(webId, template, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeTemplateApi#attributeTemplateCreateAttributeTemplate");
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
| **webId** | **String**| The ID of the parent attribute template on which to create the attribute template. | |
| **template** | [**AttributeTemplate**](AttributeTemplate.md)| The attribute template definition. | |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The attribute template was created. The response&#39;s Location header is a link to the created resource. |  -  |

<a id="attributeTemplateDelete"></a>
# **attributeTemplateDelete**
> attributeTemplateDelete(webId)

Delete an attribute template.

Deleting an attribute template will delete the attributes that were created based on the template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeTemplateApi apiInstance = new AttributeTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute template.
    try {
      apiInstance.attributeTemplateDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeTemplateApi#attributeTemplateDelete");
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
| **webId** | **String**| The ID of the attribute template. | |

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
| **204** | The attribute template was deleted. |  -  |

<a id="attributeTemplateGet"></a>
# **attributeTemplateGet**
> AttributeTemplate attributeTemplateGet(webId, selectedFields, webIdType)

Retrieve an attribute template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeTemplateApi apiInstance = new AttributeTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      AttributeTemplate result = apiInstance.attributeTemplateGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeTemplateApi#attributeTemplateGet");
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
| **webId** | **String**| The ID of the attribute template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**AttributeTemplate**](AttributeTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified attribute template. |  -  |

<a id="attributeTemplateGetAttributeTemplates"></a>
# **attributeTemplateGetAttributeTemplates**
> ItemsAttributeTemplate attributeTemplateGetAttributeTemplates(webId, selectedFields, webIdType)

Retrieve an attribute template&#39;s child attribute templates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeTemplateApi apiInstance = new AttributeTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttributeTemplate result = apiInstance.attributeTemplateGetAttributeTemplates(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeTemplateApi#attributeTemplateGetAttributeTemplates");
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
| **webId** | **String**| The ID of the attribute template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAttributeTemplate**](ItemsAttributeTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of child attribute templates. |  -  |

<a id="attributeTemplateGetByPath"></a>
# **attributeTemplateGetByPath**
> AttributeTemplate attributeTemplateGetByPath(path, selectedFields, webIdType)

Retrieve an attribute template by path.

This method returns an attribute template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeTemplateApi apiInstance = new AttributeTemplateApi(defaultClient);
    String path = "path_example"; // String | The path to the attribute template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      AttributeTemplate result = apiInstance.attributeTemplateGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeTemplateApi#attributeTemplateGetByPath");
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
| **path** | **String**| The path to the attribute template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**AttributeTemplate**](AttributeTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified attribute template. |  -  |

<a id="attributeTemplateGetCategories"></a>
# **attributeTemplateGetCategories**
> ItemsAttributeCategory attributeTemplateGetCategories(webId, selectedFields, webIdType)

Get an attribute template&#39;s categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeTemplateApi apiInstance = new AttributeTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute template.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttributeCategory result = apiInstance.attributeTemplateGetCategories(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeTemplateApi#attributeTemplateGetCategories");
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
| **webId** | **String**| The ID of the attribute template. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAttributeCategory**](ItemsAttributeCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of categories. |  -  |

<a id="attributeTemplateUpdate"></a>
# **attributeTemplateUpdate**
> attributeTemplateUpdate(webId, template)

Update an existing attribute template by replacing items in its definition.

Updating an attribute template will propagate changes to the attributes that were created based on the template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AttributeTemplateApi apiInstance = new AttributeTemplateApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the attribute template.
    AttributeTemplate template = new AttributeTemplate(); // AttributeTemplate | A partial attribute template containing the desired changes.
    try {
      apiInstance.attributeTemplateUpdate(webId, template);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeTemplateApi#attributeTemplateUpdate");
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
| **webId** | **String**| The ID of the attribute template. | |
| **template** | [**AttributeTemplate**](AttributeTemplate.md)| A partial attribute template containing the desired changes. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The attribute template was updated. |  -  |

