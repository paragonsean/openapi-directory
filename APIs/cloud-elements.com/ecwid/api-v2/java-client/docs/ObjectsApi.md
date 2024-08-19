# ObjectsApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getObjects**](ObjectsApi.md#getObjects) | **GET** /objects | Get a list of all the available objects. |
| [**getObjectsObjectNameDocs**](ObjectsApi.md#getObjectsObjectNameDocs) | **GET** /objects/{objectName}/docs | Get swagger docs for an object. |
| [**getObjectsObjectNameMetadata**](ObjectsApi.md#getObjectsObjectNameMetadata) | **GET** /objects/{objectName}/metadata | Get a list of all the field for an object. |


<a id="getObjects"></a>
# **getObjects**
> List&lt;String&gt; getObjects(authorization, elementsVersion)

Get a list of all the available objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String elementsVersion = "Hydrogen"; // String | Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen
    try {
      List<String> result = apiInstance.getObjects(authorization, elementsVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#getObjects");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **elementsVersion** | **String**| Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen | [optional] [enum: Hydrogen, Helium] |

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
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getObjectsObjectNameDocs"></a>
# **getObjectsObjectNameDocs**
> SwaggerDocs getObjectsObjectNameDocs(authorization, objectName, discovery, resolveReferences, basic, version)

Get swagger docs for an object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    Boolean discovery = true; // Boolean | Include discovery metadata in definitions
    Boolean resolveReferences = true; // Boolean | Optionally resolve swagger references for an inline object definition
    Boolean basic = true; // Boolean | Include only OpenAPI / Swagger properties in definitions
    String version = "-1"; // String | The element swagger version to get the corresponding element swagger, Passing in \"-1\" gives latest element swagger
    try {
      SwaggerDocs result = apiInstance.getObjectsObjectNameDocs(authorization, objectName, discovery, resolveReferences, basic, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#getObjectsObjectNameDocs");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **discovery** | **Boolean**| Include discovery metadata in definitions | [optional] |
| **resolveReferences** | **Boolean**| Optionally resolve swagger references for an inline object definition | [optional] |
| **basic** | **Boolean**| Include only OpenAPI / Swagger properties in definitions | [optional] |
| **version** | **String**| The element swagger version to get the corresponding element swagger, Passing in \&quot;-1\&quot; gives latest element swagger | [optional] [default to -1] |

### Return type

[**SwaggerDocs**](SwaggerDocs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getObjectsObjectNameMetadata"></a>
# **getObjectsObjectNameMetadata**
> ObjectsMetadata getObjectsObjectNameMetadata(authorization, objectName, elementsVersion)

Get a list of all the field for an object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object
    String elementsVersion = "Hydrogen"; // String | Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen
    try {
      ObjectsMetadata result = apiInstance.getObjectsObjectNameMetadata(authorization, objectName, elementsVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#getObjectsObjectNameMetadata");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object | |
| **elementsVersion** | **String**| Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen | [optional] [enum: Hydrogen, Helium] |

### Return type

[**ObjectsMetadata**](ObjectsMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

