# EventFrameApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventFrameAcknowledge**](EventFrameApi.md#eventFrameAcknowledge) | **PATCH** /eventframes/{webId}/acknowledge | Calls the EventFrame&#39;s Acknowledge method. |
| [**eventFrameCaptureValues**](EventFrameApi.md#eventFrameCaptureValues) | **POST** /eventframes/{webId}/attributes/capture | Calls the EventFrame&#39;s CaptureValues method. |
| [**eventFrameCreateAnnotation**](EventFrameApi.md#eventFrameCreateAnnotation) | **POST** /eventframes/{webId}/annotations | Create an annotation on an event frame. |
| [**eventFrameCreateAttribute**](EventFrameApi.md#eventFrameCreateAttribute) | **POST** /eventframes/{webId}/attributes | Create a new attribute of the specified event frame. |
| [**eventFrameCreateConfig**](EventFrameApi.md#eventFrameCreateConfig) | **POST** /eventframes/{webId}/config | Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children. |
| [**eventFrameCreateEventFrame**](EventFrameApi.md#eventFrameCreateEventFrame) | **POST** /eventframes/{webId}/eventframes | Create an event frame as a child of the specified event frame. |
| [**eventFrameCreateSearchByAttribute**](EventFrameApi.md#eventFrameCreateSearchByAttribute) | **POST** /eventframes/searchbyattribute | Create a link for a \&quot;Search EventFrames By Attribute Value\&quot; operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators. |
| [**eventFrameCreateSecurityEntry**](EventFrameApi.md#eventFrameCreateSecurityEntry) | **POST** /eventframes/{webId}/securityentries | Create a security entry owned by the event frame. |
| [**eventFrameDelete**](EventFrameApi.md#eventFrameDelete) | **DELETE** /eventframes/{webId} | Delete an event frame. |
| [**eventFrameDeleteAnnotation**](EventFrameApi.md#eventFrameDeleteAnnotation) | **DELETE** /eventframes/{webId}/annotations/{id} | Delete an annotation on an event frame. If the annotation has attached media, the attached media will also be deleted. |
| [**eventFrameDeleteAnnotationAttachmentMediaById**](EventFrameApi.md#eventFrameDeleteAnnotationAttachmentMediaById) | **DELETE** /eventframes/{webId}/annotations/{id}/attachment/media | Delete attached media from an annotation on an event frame. |
| [**eventFrameDeleteSecurityEntry**](EventFrameApi.md#eventFrameDeleteSecurityEntry) | **DELETE** /eventframes/{webId}/securityentries/{name} | Delete a security entry owned by the event frame. |
| [**eventFrameExecuteSearchByAttribute**](EventFrameApi.md#eventFrameExecuteSearchByAttribute) | **GET** /eventframes/searchbyattribute/{searchId} | Execute a \&quot;Search EventFrames By Attribute Value\&quot; operation. |
| [**eventFrameFindEventFrameAttributes**](EventFrameApi.md#eventFrameFindEventFrameAttributes) | **GET** /eventframes/{webId}/eventframeattributes | Retrieves a list of event frame attributes matching the specified filters from the specified event frame. |
| [**eventFrameGet**](EventFrameApi.md#eventFrameGet) | **GET** /eventframes/{webId} | Retrieve an event frame. |
| [**eventFrameGetAnnotationAttachmentMediaMetadataById**](EventFrameApi.md#eventFrameGetAnnotationAttachmentMediaMetadataById) | **GET** /eventframes/{webId}/annotations/{id}/attachment/media/metadata | Gets the metadata of the media attached to the specified annotation. |
| [**eventFrameGetAnnotationById**](EventFrameApi.md#eventFrameGetAnnotationById) | **GET** /eventframes/{webId}/annotations/{id} | Get a specific annotation on an event frame. |
| [**eventFrameGetAnnotations**](EventFrameApi.md#eventFrameGetAnnotations) | **GET** /eventframes/{webId}/annotations | Get an event frame&#39;s annotations. |
| [**eventFrameGetAttributes**](EventFrameApi.md#eventFrameGetAttributes) | **GET** /eventframes/{webId}/attributes | Get the attributes of the specified event frame. |
| [**eventFrameGetByPath**](EventFrameApi.md#eventFrameGetByPath) | **GET** /eventframes | Retrieve an event frame by path. |
| [**eventFrameGetCategories**](EventFrameApi.md#eventFrameGetCategories) | **GET** /eventframes/{webId}/categories | Get an event frame&#39;s categories. |
| [**eventFrameGetEventFrames**](EventFrameApi.md#eventFrameGetEventFrames) | **GET** /eventframes/{webId}/eventframes | Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame that have been active in the past 8 hours. |
| [**eventFrameGetEventFramesQuery**](EventFrameApi.md#eventFrameGetEventFramesQuery) | **GET** /eventframes/search | Retrieve event frames based on the specified conditions. Returns event frames using the specified search query string. |
| [**eventFrameGetMultiple**](EventFrameApi.md#eventFrameGetMultiple) | **GET** /eventframes/multiple | Retrieve multiple event frames by web ids or paths. |
| [**eventFrameGetReferencedElements**](EventFrameApi.md#eventFrameGetReferencedElements) | **GET** /eventframes/{webId}/referencedelements | Retrieve the event frame&#39;s referenced elements. |
| [**eventFrameGetSecurity**](EventFrameApi.md#eventFrameGetSecurity) | **GET** /eventframes/{webId}/security | Get the security information of the specified security item associated with the event frame for a specified user. |
| [**eventFrameGetSecurityEntries**](EventFrameApi.md#eventFrameGetSecurityEntries) | **GET** /eventframes/{webId}/securityentries | Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned. |
| [**eventFrameGetSecurityEntryByName**](EventFrameApi.md#eventFrameGetSecurityEntryByName) | **GET** /eventframes/{webId}/securityentries/{name} | Retrieve the security entry associated with the event frame with the specified name. |
| [**eventFrameUpdate**](EventFrameApi.md#eventFrameUpdate) | **PATCH** /eventframes/{webId} | Update an event frame by replacing items in its definition. |
| [**eventFrameUpdateAnnotation**](EventFrameApi.md#eventFrameUpdateAnnotation) | **PATCH** /eventframes/{webId}/annotations/{id} | Update an annotation on an event frame by replacing items in its definition. |
| [**eventFrameUpdateSecurityEntry**](EventFrameApi.md#eventFrameUpdateSecurityEntry) | **PUT** /eventframes/{webId}/securityentries/{name} | Update a security entry owned by the event frame. |


<a id="eventFrameAcknowledge"></a>
# **eventFrameAcknowledge**
> eventFrameAcknowledge(webId)

Calls the EventFrame&#39;s Acknowledge method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame.
    try {
      apiInstance.eventFrameAcknowledge(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameAcknowledge");
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
| **webId** | **String**| The ID of the event frame. | |

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
| **204** | The event frame has been acknowledged. |  -  |

<a id="eventFrameCaptureValues"></a>
# **eventFrameCaptureValues**
> eventFrameCaptureValues(webId)

Calls the EventFrame&#39;s CaptureValues method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame.
    try {
      apiInstance.eventFrameCaptureValues(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameCaptureValues");
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
| **webId** | **String**| The ID of the event frame. | |

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
| **204** | The event frame attribute&#39;s values were captured. |  -  |

<a id="eventFrameCreateAnnotation"></a>
# **eventFrameCreateAnnotation**
> eventFrameCreateAnnotation(webId, annotation, webIdType)

Create an annotation on an event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the owner event frame on which to create the annotation.
    Annotation annotation = new Annotation(); // Annotation | The new annotation definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.eventFrameCreateAnnotation(webId, annotation, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameCreateAnnotation");
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
| **webId** | **String**| The ID of the owner event frame on which to create the annotation. | |
| **annotation** | [**Annotation**](Annotation.md)| The new annotation definition. | |
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
| **201** | The annotation was created. The response&#39;s Location header is a link to the annotation. |  -  |

<a id="eventFrameCreateAttribute"></a>
# **eventFrameCreateAttribute**
> eventFrameCreateAttribute(webId, attribute, webIdType)

Create a new attribute of the specified event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame on which to create the attribute.
    Attribute attribute = new Attribute(); // Attribute | The definition of the new attribute.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.eventFrameCreateAttribute(webId, attribute, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameCreateAttribute");
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
| **webId** | **String**| The ID of the event frame on which to create the attribute. | |
| **attribute** | [**Attribute**](Attribute.md)| The definition of the new attribute. | |
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
| **201** | The attribute was created. The response&#39;s Location header is a link to the created attribute. |  -  |

<a id="eventFrameCreateConfig"></a>
# **eventFrameCreateConfig**
> eventFrameCreateConfig(webId, includeChildElements)

Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame.
    Boolean includeChildElements = true; // Boolean | If true, includes the child event frames of the specified event frame.
    try {
      apiInstance.eventFrameCreateConfig(webId, includeChildElements);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameCreateConfig");
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
| **webId** | **String**| The ID of the event frame. | |
| **includeChildElements** | **Boolean**| If true, includes the child event frames of the specified event frame. | [optional] |

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
| **200** | Process log of operations. Operations completed with no errors. |  -  |
| **207** | Process log of operations. Operations completed with errors. |  -  |

<a id="eventFrameCreateEventFrame"></a>
# **eventFrameCreateEventFrame**
> eventFrameCreateEventFrame(webId, eventFrame, webIdType)

Create an event frame as a child of the specified event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the parent event frame on which to create the event frame.
    EventFrame eventFrame = new EventFrame(); // EventFrame | The new event frame definition.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.eventFrameCreateEventFrame(webId, eventFrame, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameCreateEventFrame");
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
| **webId** | **String**| The ID of the parent event frame on which to create the event frame. | |
| **eventFrame** | [**EventFrame**](EventFrame.md)| The new event frame definition. | |
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
| **201** | The event frame was created. The response&#39;s Location header is a link to the event frame. |  -  |

<a id="eventFrameCreateSearchByAttribute"></a>
# **eventFrameCreateSearchByAttribute**
> ItemsEventFrame eventFrameCreateSearchByAttribute(query, noResults, selectedFields, webIdType)

Create a link for a \&quot;Search EventFrames By Attribute Value\&quot; operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    SearchByAttribute query = new SearchByAttribute(); // SearchByAttribute | The query of search by attribute.
    Boolean noResults = true; // Boolean | If false, the response content will contain the first page of the search results. If true, the response content will be empty. The default is false.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsEventFrame result = apiInstance.eventFrameCreateSearchByAttribute(query, noResults, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameCreateSearchByAttribute");
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
| **query** | [**SearchByAttribute**](SearchByAttribute.md)| The query of search by attribute. | |
| **noResults** | **Boolean**| If false, the response content will contain the first page of the search results. If true, the response content will be empty. The default is false. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The link is stored in the response&#39;s \&quot;Location\&quot; header. The response content is the first page of the search result by the default parameters. |  -  |
| **400** | Empty or invalid request content. |  -  |
| **413** | Request content is too large. |  -  |

<a id="eventFrameCreateSecurityEntry"></a>
# **eventFrameCreateSecurityEntry**
> eventFrameCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType)

Create a security entry owned by the event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame where the security entry will be created.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.eventFrameCreateSecurityEntry(webId, securityEntry, applyToChildren, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameCreateSecurityEntry");
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
| **webId** | **String**| The ID of the event frame where the security entry will be created. | |
| **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | |
| **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] |
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
| **201** | The security entry was created. The response&#39;s Location header is a link to the security entry. |  -  |

<a id="eventFrameDelete"></a>
# **eventFrameDelete**
> eventFrameDelete(webId)

Delete an event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame to delete.
    try {
      apiInstance.eventFrameDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameDelete");
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
| **webId** | **String**| The ID of the event frame to delete. | |

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
| **204** | The event frame was deleted. |  -  |

<a id="eventFrameDeleteAnnotation"></a>
# **eventFrameDeleteAnnotation**
> eventFrameDeleteAnnotation(id, webId)

Delete an annotation on an event frame. If the annotation has attached media, the attached media will also be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String id = "id_example"; // String | The Annotation identifier of the annotation to be deleted.
    String webId = "webId_example"; // String | The ID of the owner event frame of the annotation to delete.
    try {
      apiInstance.eventFrameDeleteAnnotation(id, webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameDeleteAnnotation");
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
| **id** | **String**| The Annotation identifier of the annotation to be deleted. | |
| **webId** | **String**| The ID of the owner event frame of the annotation to delete. | |

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
| **204** | The annotation was deleted. |  -  |

<a id="eventFrameDeleteAnnotationAttachmentMediaById"></a>
# **eventFrameDeleteAnnotationAttachmentMediaById**
> eventFrameDeleteAnnotationAttachmentMediaById(id, webId)

Delete attached media from an annotation on an event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String id = "id_example"; // String | The Annotation identifier of the annotation to delete the attached media of.
    String webId = "webId_example"; // String | The ID of the owner event frame of the annotation to delete the attached media of.
    try {
      apiInstance.eventFrameDeleteAnnotationAttachmentMediaById(id, webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameDeleteAnnotationAttachmentMediaById");
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
| **id** | **String**| The Annotation identifier of the annotation to delete the attached media of. | |
| **webId** | **String**| The ID of the owner event frame of the annotation to delete the attached media of. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The attached media was deleted. |  -  |
| **404** | The specified annotation did not have any attached media to delete. |  -  |

<a id="eventFrameDeleteSecurityEntry"></a>
# **eventFrameDeleteSecurityEntry**
> eventFrameDeleteSecurityEntry(name, webId, applyToChildren)

Delete a security entry owned by the event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the event frame where the security entry will be deleted.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.eventFrameDeleteSecurityEntry(name, webId, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameDeleteSecurityEntry");
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
| **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | |
| **webId** | **String**| The ID of the event frame where the security entry will be deleted. | |
| **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] |

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
| **204** | The security entry was deleted. |  -  |

<a id="eventFrameExecuteSearchByAttribute"></a>
# **eventFrameExecuteSearchByAttribute**
> ItemsEventFrame eventFrameExecuteSearchByAttribute(searchId, canBeAcknowledged, endTime, isAcknowledged, maxCount, nameFilter, referencedElementNameFilter, searchFullHierarchy, searchMode, selectedFields, severity, sortField, sortOrder, startIndex, startTime, webIdType)

Execute a \&quot;Search EventFrames By Attribute Value\&quot; operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String searchId = "searchId_example"; // String | The encoded search Id of the \"Search EventFrames By Attribute Value\" operation.
    Boolean canBeAcknowledged = true; // Boolean | Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter.
    String endTime = "endTime_example"; // String | The ending time for the search. endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*'.
    Boolean isAcknowledged = true; // Boolean | Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String nameFilter = "nameFilter_example"; // String | The name query string used for finding event frames. The default is no filter.
    String referencedElementNameFilter = "referencedElementNameFilter_example"; // String | The name query string which must match the name of a referenced element. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies whether the search should include objects nested further than the immediate children of the search root. The default is 'false'.
    String searchMode = "searchMode_example"; // String | Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. The default is 'Overlapped'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    List<String> severity = Arrays.asList(); // List<String> | Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String startTime = "startTime_example"; // String | The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*-8h'.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsEventFrame result = apiInstance.eventFrameExecuteSearchByAttribute(searchId, canBeAcknowledged, endTime, isAcknowledged, maxCount, nameFilter, referencedElementNameFilter, searchFullHierarchy, searchMode, selectedFields, severity, sortField, sortOrder, startIndex, startTime, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameExecuteSearchByAttribute");
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
| **searchId** | **String**| The encoded search Id of the \&quot;Search EventFrames By Attribute Value\&quot; operation. | |
| **canBeAcknowledged** | **Boolean**| Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter. | [optional] |
| **endTime** | **String**| The ending time for the search. endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39;. | [optional] |
| **isAcknowledged** | **Boolean**| Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **nameFilter** | **String**| The name query string used for finding event frames. The default is no filter. | [optional] |
| **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;. | [optional] |
| **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. The default is &#39;Overlapped&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **severity** | [**List&lt;String&gt;**](String.md)| Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **startTime** | **String**| The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a list of matching EventFrames. |  -  |
| **400** | Invalid search Id or search parameters. |  -  |

<a id="eventFrameFindEventFrameAttributes"></a>
# **eventFrameFindEventFrameAttributes**
> ItemsAttribute eventFrameFindEventFrameAttributes(webId, associations, attributeCategory, attributeDescriptionFilter, attributeNameFilter, attributeType, endTime, eventFrameCategory, eventFrameDescriptionFilter, eventFrameNameFilter, eventFrameTemplate, maxCount, referencedElementNameFilter, searchFullHierarchy, searchMode, selectedFields, sortField, sortOrder, startIndex, startTime, webIdType)

Retrieves a list of event frame attributes matching the specified filters from the specified event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame to use as the root of the search.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    String attributeCategory = "attributeCategory_example"; // String | Specify that returned attributes must have this category. The default is no filter.
    String attributeDescriptionFilter = "attributeDescriptionFilter_example"; // String | The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    String attributeNameFilter = "attributeNameFilter_example"; // String | The attribute name filter string used for finding objects. The default is no filter.
    String attributeType = "attributeType_example"; // String | Specify that returned attributes' value type must be this value type. The default is no filter.
    String endTime = "endTime_example"; // String | A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is '*'.
    String eventFrameCategory = "eventFrameCategory_example"; // String | Specify that the owner of the returned attributes must have this category. The default is no filter.
    String eventFrameDescriptionFilter = "eventFrameDescriptionFilter_example"; // String | The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    String eventFrameNameFilter = "eventFrameNameFilter_example"; // String | The event frame name filter string used for finding objects. The default is no filter.
    String eventFrameTemplate = "eventFrameTemplate_example"; // String | Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned (the page size). The default is 1000.
    String referencedElementNameFilter = "referencedElementNameFilter_example"; // String | The name query string which must match the name of a referenced element. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'.
    String searchMode = "searchMode_example"; // String | Determines how the startTime and endTime parameters are treated when searching for event frames. The default is 'Overlapped'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String startTime = "startTime_example"; // String | A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is '*-8h'.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttribute result = apiInstance.eventFrameFindEventFrameAttributes(webId, associations, attributeCategory, attributeDescriptionFilter, attributeNameFilter, attributeType, endTime, eventFrameCategory, eventFrameDescriptionFilter, eventFrameNameFilter, eventFrameTemplate, maxCount, referencedElementNameFilter, searchFullHierarchy, searchMode, selectedFields, sortField, sortOrder, startIndex, startTime, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameFindEventFrameAttributes");
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
| **webId** | **String**| The ID of the event frame to use as the root of the search. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] |
| **attributeCategory** | **String**| Specify that returned attributes must have this category. The default is no filter. | [optional] |
| **attributeDescriptionFilter** | **String**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] |
| **attributeNameFilter** | **String**| The attribute name filter string used for finding objects. The default is no filter. | [optional] |
| **attributeType** | **String**| Specify that returned attributes&#39; value type must be this value type. The default is no filter. | [optional] |
| **endTime** | **String**| A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is &#39;*&#39;. | [optional] |
| **eventFrameCategory** | **String**| Specify that the owner of the returned attributes must have this category. The default is no filter. | [optional] |
| **eventFrameDescriptionFilter** | **String**| The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] |
| **eventFrameNameFilter** | **String**| The event frame name filter string used for finding objects. The default is no filter. | [optional] |
| **eventFrameTemplate** | **String**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned (the page size). The default is 1000. | [optional] |
| **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;. | [optional] |
| **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frames. The default is &#39;Overlapped&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **startTime** | **String**| A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is &#39;*-8h&#39;. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAttribute**](ItemsAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a list of matching attributes. |  -  |

<a id="eventFrameGet"></a>
# **eventFrameGet**
> EventFrame eventFrameGet(webId, selectedFields, webIdType)

Retrieve an event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      EventFrame result = apiInstance.eventFrameGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGet");
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
| **webId** | **String**| The ID of the event frame. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**EventFrame**](EventFrame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified event frame. |  -  |

<a id="eventFrameGetAnnotationAttachmentMediaMetadataById"></a>
# **eventFrameGetAnnotationAttachmentMediaMetadataById**
> MediaMetadata eventFrameGetAnnotationAttachmentMediaMetadataById(id, webId, selectedFields, webIdType)

Gets the metadata of the media attached to the specified annotation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String id = "id_example"; // String | The Annotation identifier of the specific annotation.
    String webId = "webId_example"; // String | The ID of the owner event frame.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      MediaMetadata result = apiInstance.eventFrameGetAnnotationAttachmentMediaMetadataById(id, webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetAnnotationAttachmentMediaMetadataById");
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
| **id** | **String**| The Annotation identifier of the specific annotation. | |
| **webId** | **String**| The ID of the owner event frame. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**MediaMetadata**](MediaMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested metadata. |  -  |
| **400** | The supplied Web ID could not be parsed, or the request was somehow otherwise invalid. |  -  |
| **404** | The specified Event Frame did not exist, the specified annotation was not found, or the annotation did not have attached media. |  -  |

<a id="eventFrameGetAnnotationById"></a>
# **eventFrameGetAnnotationById**
> Annotation eventFrameGetAnnotationById(id, webId, selectedFields, webIdType)

Get a specific annotation on an event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String id = "id_example"; // String | The Annotation identifier of the specific annotation.
    String webId = "webId_example"; // String | The ID of the owner event frame.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      Annotation result = apiInstance.eventFrameGetAnnotationById(id, webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetAnnotationById");
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
| **id** | **String**| The Annotation identifier of the specific annotation. | |
| **webId** | **String**| The ID of the owner event frame. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested annotation. |  -  |

<a id="eventFrameGetAnnotations"></a>
# **eventFrameGetAnnotations**
> ItemsAnnotation eventFrameGetAnnotations(webId, selectedFields, webIdType)

Get an event frame&#39;s annotations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the owner event frame.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAnnotation result = apiInstance.eventFrameGetAnnotations(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetAnnotations");
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
| **webId** | **String**| The ID of the owner event frame. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAnnotation**](ItemsAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of annotations. |  -  |

<a id="eventFrameGetAttributes"></a>
# **eventFrameGetAttributes**
> ItemsAttribute eventFrameGetAttributes(webId, associations, categoryName, maxCount, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startIndex, templateName, trait, traitCategory, valueType, webIdType)

Get the attributes of the specified event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    String categoryName = "categoryName_example"; // String | Specify that returned attributes must have this category. The default is no category filter.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String nameFilter = "nameFilter_example"; // String | The name query string used for finding attributes. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String templateName = "templateName_example"; // String | Specify that returned attributes must be members of this template. The default is no template filter.
    List<String> trait = Arrays.asList(); // List<String> | The name of the attribute trait. Multiple traits may be specified with multiple instances of the parameter.
    List<String> traitCategory = Arrays.asList(); // List<String> | The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \"all\", then all attribute traits of all categories will be returned.
    String valueType = "valueType_example"; // String | Specify that returned attributes' value type must be the given value type. The default is no value type filter.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsAttribute result = apiInstance.eventFrameGetAttributes(webId, associations, categoryName, maxCount, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startIndex, templateName, trait, traitCategory, valueType, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetAttributes");
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
| **webId** | **String**| The ID of the event frame. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] |
| **categoryName** | **String**| Specify that returned attributes must have this category. The default is no category filter. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **nameFilter** | **String**| The name query string used for finding attributes. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **templateName** | **String**| Specify that returned attributes must be members of this template. The default is no template filter. | [optional] |
| **trait** | [**List&lt;String&gt;**](String.md)| The name of the attribute trait. Multiple traits may be specified with multiple instances of the parameter. | [optional] |
| **traitCategory** | [**List&lt;String&gt;**](String.md)| The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \&quot;all\&quot;, then all attribute traits of all categories will be returned. | [optional] |
| **valueType** | **String**| Specify that returned attributes&#39; value type must be the given value type. The default is no value type filter. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsAttribute**](ItemsAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of child attributes. |  -  |

<a id="eventFrameGetByPath"></a>
# **eventFrameGetByPath**
> EventFrame eventFrameGetByPath(path, selectedFields, webIdType)

Retrieve an event frame by path.

This method returns an event frame based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String path = "path_example"; // String | The path to the event frame.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      EventFrame result = apiInstance.eventFrameGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetByPath");
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
| **path** | **String**| The path to the event frame. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**EventFrame**](EventFrame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified event frame. |  -  |

<a id="eventFrameGetCategories"></a>
# **eventFrameGetCategories**
> ItemsElementCategory eventFrameGetCategories(webId, selectedFields, webIdType)

Get an event frame&#39;s categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsElementCategory result = apiInstance.eventFrameGetCategories(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetCategories");
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
| **webId** | **String**| The ID of the event frame. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsElementCategory**](ItemsElementCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of categories. |  -  |

<a id="eventFrameGetEventFrames"></a>
# **eventFrameGetEventFrames**
> ItemsEventFrame eventFrameGetEventFrames(webId, canBeAcknowledged, categoryName, endTime, isAcknowledged, maxCount, nameFilter, referencedElementNameFilter, referencedElementTemplateName, searchFullHierarchy, searchMode, selectedFields, severity, sortField, sortOrder, startIndex, startTime, templateName, webIdType)

Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame that have been active in the past 8 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame to use as the root of the search.
    Boolean canBeAcknowledged = true; // Boolean | Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter.
    String categoryName = "categoryName_example"; // String | Specify that returned event frames must have this category. The default is no category filter.
    String endTime = "endTime_example"; // String | The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*' if searchMode is not one of the 'Backward*' or 'Forward*' values.
    Boolean isAcknowledged = true; // Boolean | Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String nameFilter = "nameFilter_example"; // String | The name query string used for finding event frames. The default is no filter.
    String referencedElementNameFilter = "referencedElementNameFilter_example"; // String | The name query string which must match the name of a referenced element. The default is no filter.
    String referencedElementTemplateName = "referencedElementTemplateName_example"; // String | Specify that returned event frames must have an element in the event frame's referenced elements collection that derives from the template. Specify this parameter by name.
    Boolean searchFullHierarchy = true; // Boolean | Specifies whether the search should include objects nested further than the immediate children of the search root. The default is 'false'.
    String searchMode = "searchMode_example"; // String | Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the 'Backward*' or 'Forward*' values, none of endTime, sortField, or sortOrder may be specified. The default is 'Overlapped'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    List<String> severity = Arrays.asList(); // List<String> | Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. The default is 'Name' if searchMode is not one of the 'Backward*' or 'Forward*' values.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending' if searchMode is not one of the 'Backward*' or 'Forward*' values.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String startTime = "startTime_example"; // String | The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*-8h'.
    String templateName = "templateName_example"; // String | Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsEventFrame result = apiInstance.eventFrameGetEventFrames(webId, canBeAcknowledged, categoryName, endTime, isAcknowledged, maxCount, nameFilter, referencedElementNameFilter, referencedElementTemplateName, searchFullHierarchy, searchMode, selectedFields, severity, sortField, sortOrder, startIndex, startTime, templateName, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetEventFrames");
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
| **webId** | **String**| The ID of the event frame to use as the root of the search. | |
| **canBeAcknowledged** | **Boolean**| Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter. | [optional] |
| **categoryName** | **String**| Specify that returned event frames must have this category. The default is no category filter. | [optional] |
| **endTime** | **String**| The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] |
| **isAcknowledged** | **Boolean**| Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **nameFilter** | **String**| The name query string used for finding event frames. The default is no filter. | [optional] |
| **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] |
| **referencedElementTemplateName** | **String**| Specify that returned event frames must have an element in the event frame&#39;s referenced elements collection that derives from the template. Specify this parameter by name. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;. | [optional] |
| **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the &#39;Backward*&#39; or &#39;Forward*&#39; values, none of endTime, sortField, or sortOrder may be specified. The default is &#39;Overlapped&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **severity** | [**List&lt;String&gt;**](String.md)| Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **startTime** | **String**| The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;. | [optional] |
| **templateName** | **String**| Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of event frames matching the specified conditions. |  -  |

<a id="eventFrameGetEventFramesQuery"></a>
# **eventFrameGetEventFramesQuery**
> ItemsEventFrame eventFrameGetEventFramesQuery(databaseWebId, maxCount, query, selectedFields, startIndex, webIdType)

Retrieve event frames based on the specified conditions. Returns event frames using the specified search query string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String databaseWebId = "databaseWebId_example"; // String | The ID of the asset database to use as the root of the query.
    Integer maxCount = 56; // Integer | The maximum number of objects to be returned per call (page size). The default is 1000.
    String query = "query_example"; // String | The query string is a list of filters used to perform an AFSearch for the eventframes in the asset database. An example would be: \"query=Name:=MyEventFrame* Category:=MyCategory Template:=EFTemplate\".
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Integer startIndex = 56; // Integer | The starting index (zero based) of the items to be returned. The default is 0.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsEventFrame result = apiInstance.eventFrameGetEventFramesQuery(databaseWebId, maxCount, query, selectedFields, startIndex, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetEventFramesQuery");
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
| **databaseWebId** | **String**| The ID of the asset database to use as the root of the query. | [optional] |
| **maxCount** | **Integer**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] |
| **query** | **String**| The query string is a list of filters used to perform an AFSearch for the eventframes in the asset database. An example would be: \&quot;query&#x3D;Name:&#x3D;MyEventFrame* Category:&#x3D;MyCategory Template:&#x3D;EFTemplate\&quot;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startIndex** | **Integer**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of event frames matching the specified conditions. |  -  |

<a id="eventFrameGetMultiple"></a>
# **eventFrameGetMultiple**
> ItemsItemEventFrame eventFrameGetMultiple(asParallel, includeMode, path, selectedFields, webId, webIdType)

Retrieve multiple event frames by web ids or paths.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    Boolean asParallel = true; // Boolean | Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is 'false'.
    String includeMode = "includeMode_example"; // String | The include mode for the return list. The default is 'All'.
    List<String> path = Arrays.asList(); // List<String> | The path of an event frame. Multiple event frames may be specified with multiple instances of the parameter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    List<String> webId = Arrays.asList(); // List<String> | The ID of an event frame. Multiple event frames may be specified with multiple instances of the parameter.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsItemEventFrame result = apiInstance.eventFrameGetMultiple(asParallel, includeMode, path, selectedFields, webId, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetMultiple");
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
| **asParallel** | **Boolean**| Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is &#39;false&#39;. | [optional] |
| **includeMode** | **String**| The include mode for the return list. The default is &#39;All&#39;. | [optional] |
| **path** | [**List&lt;String&gt;**](String.md)| The path of an event frame. Multiple event frames may be specified with multiple instances of the parameter. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of an event frame. Multiple event frames may be specified with multiple instances of the parameter. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsItemEventFrame**](ItemsItemEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested event frames |  -  |
| **207** | Some or all items contain exceptions. |  -  |

<a id="eventFrameGetReferencedElements"></a>
# **eventFrameGetReferencedElements**
> ItemsElement eventFrameGetReferencedElements(webId, associations, selectedFields, webIdType)

Retrieve the event frame&#39;s referenced elements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame whose referenced elements should be retrieved.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsElement result = apiInstance.eventFrameGetReferencedElements(webId, associations, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetReferencedElements");
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
| **webId** | **String**| The ID of the event frame whose referenced elements should be retrieved. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsElement**](ItemsElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of referenced elements. |  -  |

<a id="eventFrameGetSecurity"></a>
# **eventFrameGetSecurity**
> ItemsSecurityRights eventFrameGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType)

Get the security information of the specified security item associated with the event frame for a specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame for the security to be checked.
    List<String> userIdentity = Arrays.asList(); // List<String> | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
    Boolean forceRefresh = true; // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityRights result = apiInstance.eventFrameGetSecurity(webId, userIdentity, forceRefresh, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetSecurity");
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
| **webId** | **String**| The ID of the event frame for the security to be checked. | |
| **userIdentity** | [**List&lt;String&gt;**](String.md)| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user&#39;s security rights will be returned. | |
| **forceRefresh** | **Boolean**| Indicates if the security cache should be refreshed before getting security information. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsSecurityRights**](ItemsSecurityRights.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Security rights. |  -  |
| **400** | An invalid or local account is specified as the user identity. |  -  |
| **401** | Access denied for the specified user identity. |  -  |
| **409** | Unsupported when using Anonymous authentication method. |  -  |
| **502** | Failed to retrieve the specified user identity. |  -  |

<a id="eventFrameGetSecurityEntries"></a>
# **eventFrameGetSecurityEntries**
> ItemsSecurityEntry eventFrameGetSecurityEntries(webId, nameFilter, selectedFields, webIdType)

Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering security entries. The default is no filter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsSecurityEntry result = apiInstance.eventFrameGetSecurityEntries(webId, nameFilter, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetSecurityEntries");
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
| **webId** | **String**| The ID of the event frame. | |
| **nameFilter** | **String**| The name query string used for filtering security entries. The default is no filter. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsSecurityEntry**](ItemsSecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of security entries matching the specified condition. |  -  |

<a id="eventFrameGetSecurityEntryByName"></a>
# **eventFrameGetSecurityEntryByName**
> SecurityEntry eventFrameGetSecurityEntryByName(name, webId, selectedFields, webIdType)

Retrieve the security entry associated with the event frame with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    String webId = "webId_example"; // String | The ID of the event frame.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      SecurityEntry result = apiInstance.eventFrameGetSecurityEntryByName(name, webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameGetSecurityEntryByName");
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
| **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | |
| **webId** | **String**| The ID of the event frame. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**SecurityEntry**](SecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The security entry matching the specified condition. |  -  |
| **404** | The security entry with the specified name is not found. |  -  |

<a id="eventFrameUpdate"></a>
# **eventFrameUpdate**
> eventFrameUpdate(webId, eventFrame)

Update an event frame by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the event frame to update.
    EventFrame eventFrame = new EventFrame(); // EventFrame | A partial event frame containing the desired changes.
    try {
      apiInstance.eventFrameUpdate(webId, eventFrame);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameUpdate");
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
| **webId** | **String**| The ID of the event frame to update. | |
| **eventFrame** | [**EventFrame**](EventFrame.md)| A partial event frame containing the desired changes. | |

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
| **204** | The event frame was updated. |  -  |

<a id="eventFrameUpdateAnnotation"></a>
# **eventFrameUpdateAnnotation**
> eventFrameUpdateAnnotation(id, webId, annotation)

Update an annotation on an event frame by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String id = "id_example"; // String | The Annotation identifier of the annotation to be updated.
    String webId = "webId_example"; // String | The ID of the owner event frame of the annotation to update.
    Annotation annotation = new Annotation(); // Annotation | A partial annotation containing the desired changes.
    try {
      apiInstance.eventFrameUpdateAnnotation(id, webId, annotation);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameUpdateAnnotation");
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
| **id** | **String**| The Annotation identifier of the annotation to be updated. | |
| **webId** | **String**| The ID of the owner event frame of the annotation to update. | |
| **annotation** | [**Annotation**](Annotation.md)| A partial annotation containing the desired changes. | |

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
| **204** | The annotation was updated. |  -  |

<a id="eventFrameUpdateSecurityEntry"></a>
# **eventFrameUpdateSecurityEntry**
> eventFrameUpdateSecurityEntry(name, webId, securityEntry, applyToChildren)

Update a security entry owned by the event frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventFrameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    EventFrameApi apiInstance = new EventFrameApi(defaultClient);
    String name = "name_example"; // String | The name of the security entry.
    String webId = "webId_example"; // String | The ID of the event frame where the security entry will be updated.
    SecurityEntry securityEntry = new SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    Boolean applyToChildren = true; // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    try {
      apiInstance.eventFrameUpdateSecurityEntry(name, webId, securityEntry, applyToChildren);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventFrameApi#eventFrameUpdateSecurityEntry");
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
| **name** | **String**| The name of the security entry. | |
| **webId** | **String**| The ID of the event frame where the security entry will be updated. | |
| **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | |
| **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] |

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
| **204** | The security entry was updated. |  -  |

