# ExtensionsApi

All URIs are relative to *https://watchful.li/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getExtensions**](ExtensionsApi.md#getExtensions) | **GET** /extensions | Get a list Extensions |
| [**getFieldsExtensions**](ExtensionsApi.md#getFieldsExtensions) | **GET** /extensions/metadata | Get the list of fields |
| [**ignoreExtensionUpdate**](ExtensionsApi.md#ignoreExtensionUpdate) | **POST** /extensions/{id}/ignore | Set &#39;ignore updates&#39; for a given extension / site_id |
| [**unignoreExtensionUpdate**](ExtensionsApi.md#unignoreExtensionUpdate) | **POST** /extensions/{id}/unignore | Remove &#39;ignore updates&#39; for a given extension |
| [**updateExtension**](ExtensionsApi.md#updateExtension) | **POST** /extensions/{id}/update | Update the extension on the remote site |


<a id="getExtensions"></a>
# **getExtensions**
> Extension getExtensions(extName, siteids, extPrefix, version, vUpdate, fields, limit, limitstart, order)

Get a list Extensions

Returns a list Extensions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    String extName = "extName_example"; // String | Do a 'LIKE' search, you can also use '%'
    String siteids = "siteids_example"; // String | List of sites id separated by comma
    String extPrefix = "extPrefix_example"; // String | Do a 'LIKE' search, you can also use '%'. technical name of the extension com_xxxx
    String version = "version_example"; // String | Do a 'LIKE' search, you can also use '%'
    Integer vUpdate = 1; // Integer | update available for this extension
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    try {
      Extension result = apiInstance.getExtensions(extName, siteids, extPrefix, version, vUpdate, fields, limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#getExtensions");
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
| **extName** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **siteids** | **String**| List of sites id separated by comma | [optional] |
| **extPrefix** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;. technical name of the extension com_xxxx | [optional] |
| **version** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **vUpdate** | **Integer**| update available for this extension | [optional] [enum: 1, 0] |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] |

### Return type

[**Extension**](Extension.md)

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
| **404** | Invalid |  -  |

<a id="getFieldsExtensions"></a>
# **getFieldsExtensions**
> String getFieldsExtensions()

Get the list of fields

Returns a list of fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    try {
      String result = apiInstance.getFieldsExtensions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#getFieldsExtensions");
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
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="ignoreExtensionUpdate"></a>
# **ignoreExtensionUpdate**
> String ignoreExtensionUpdate(id)

Set &#39;ignore updates&#39; for a given extension / site_id

Set &#39;ignore updates&#39; for a given extension / site_id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    Long id = 56L; // Long | ID of the extension
    try {
      String result = apiInstance.ignoreExtensionUpdate(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#ignoreExtensionUpdate");
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
| **id** | **Long**| ID of the extension | |

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
| **200** | Extension successfully updated |  -  |
| **404** | Update not found for the given extension |  -  |

<a id="unignoreExtensionUpdate"></a>
# **unignoreExtensionUpdate**
> String unignoreExtensionUpdate(id)

Remove &#39;ignore updates&#39; for a given extension

Remove &#39;ignore updates&#39; for a given extension

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    Long id = 56L; // Long | ID of the extension
    try {
      String result = apiInstance.unignoreExtensionUpdate(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#unignoreExtensionUpdate");
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
| **id** | **Long**| ID of the extension | |

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
| **200** | Extension successfully updated |  -  |
| **404** | Update not found for the given extension |  -  |

<a id="updateExtension"></a>
# **updateExtension**
> String updateExtension(id)

Update the extension on the remote site

Update the extension on the remote site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    Long id = 56L; // Long | ID of the extension
    try {
      String result = apiInstance.updateExtension(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#updateExtension");
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
| **id** | **Long**| ID of the extension | |

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
| **200** | Extension successfully updated |  -  |
| **404** | Update not found for the given extension |  -  |

