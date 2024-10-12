# TemplatesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDocumentsTemplatesID**](TemplatesApi.md#deleteDocumentsTemplatesID) | **DELETE** /documents/templates/{templateID} | Delete a template |
| [**deleteDocumentsTemplatesIDLabelsID**](TemplatesApi.md#deleteDocumentsTemplatesIDLabelsID) | **DELETE** /documents/templates/{templateID}/labels/{labelID} | Delete a label from a template |
| [**getDocumentsTemplates**](TemplatesApi.md#getDocumentsTemplates) | **GET** /documents/templates | List all templates |
| [**getDocumentsTemplatesID**](TemplatesApi.md#getDocumentsTemplatesID) | **GET** /documents/templates/{templateID} | Retrieve a template |
| [**getDocumentsTemplatesIDLabels**](TemplatesApi.md#getDocumentsTemplatesIDLabels) | **GET** /documents/templates/{templateID}/labels | List all labels for a template |
| [**postDocumentsTemplates**](TemplatesApi.md#postDocumentsTemplates) | **POST** /documents/templates | Create a template |
| [**postDocumentsTemplatesIDLabels**](TemplatesApi.md#postDocumentsTemplatesIDLabels) | **POST** /documents/templates/{templateID}/labels | Add a label to a template |
| [**putDocumentsTemplatesID**](TemplatesApi.md#putDocumentsTemplatesID) | **PUT** /documents/templates/{templateID} | Update a template |


<a id="deleteDocumentsTemplatesID"></a>
# **deleteDocumentsTemplatesID**
> deleteDocumentsTemplatesID(templateID, zapTraceSpan)

Delete a template

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
    defaultClient.setBasePath("/api/v2");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String templateID = "templateID_example"; // String | The template ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteDocumentsTemplatesID(templateID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#deleteDocumentsTemplatesID");
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
| **templateID** | **String**| The template ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteDocumentsTemplatesIDLabelsID"></a>
# **deleteDocumentsTemplatesIDLabelsID**
> deleteDocumentsTemplatesIDLabelsID(templateID, labelID, zapTraceSpan)

Delete a label from a template

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
    defaultClient.setBasePath("/api/v2");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String templateID = "templateID_example"; // String | The template ID.
    String labelID = "labelID_example"; // String | The label ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteDocumentsTemplatesIDLabelsID(templateID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#deleteDocumentsTemplatesIDLabelsID");
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
| **templateID** | **String**| The template ID. | |
| **labelID** | **String**| The label ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | Template not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getDocumentsTemplates"></a>
# **getDocumentsTemplates**
> Documents getDocumentsTemplates(zapTraceSpan, org, orgID)

List all templates

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
    defaultClient.setBasePath("/api/v2");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String org = "org_example"; // String | Specifies the name of the organization of the template.
    String orgID = "orgID_example"; // String | Specifies the organization ID of the template.
    try {
      Documents result = apiInstance.getDocumentsTemplates(zapTraceSpan, org, orgID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getDocumentsTemplates");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **org** | **String**| Specifies the name of the organization of the template. | [optional] |
| **orgID** | **String**| Specifies the organization ID of the template. | [optional] |

### Return type

[**Documents**](Documents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of template documents |  -  |
| **0** | Unexpected error |  -  |

<a id="getDocumentsTemplatesID"></a>
# **getDocumentsTemplatesID**
> Document getDocumentsTemplatesID(templateID, zapTraceSpan)

Retrieve a template

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
    defaultClient.setBasePath("/api/v2");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String templateID = "templateID_example"; // String | The template ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Document result = apiInstance.getDocumentsTemplatesID(templateID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getDocumentsTemplatesID");
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
| **templateID** | **String**| The template ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The template requested |  -  |
| **0** | Unexpected error |  -  |

<a id="getDocumentsTemplatesIDLabels"></a>
# **getDocumentsTemplatesIDLabels**
> LabelsResponse getDocumentsTemplatesIDLabels(templateID, zapTraceSpan)

List all labels for a template

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
    defaultClient.setBasePath("/api/v2");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String templateID = "templateID_example"; // String | The template ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getDocumentsTemplatesIDLabels(templateID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#getDocumentsTemplatesIDLabels");
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
| **templateID** | **String**| The template ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all labels for a template |  -  |
| **0** | Unexpected error |  -  |

<a id="postDocumentsTemplates"></a>
# **postDocumentsTemplates**
> Document postDocumentsTemplates(documentCreate, zapTraceSpan)

Create a template

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
    defaultClient.setBasePath("/api/v2");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    DocumentCreate documentCreate = new DocumentCreate(); // DocumentCreate | Template that will be created
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Document result = apiInstance.postDocumentsTemplates(documentCreate, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#postDocumentsTemplates");
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
| **documentCreate** | [**DocumentCreate**](DocumentCreate.md)| Template that will be created | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Template created |  -  |
| **0** | Unexpected error |  -  |

<a id="postDocumentsTemplatesIDLabels"></a>
# **postDocumentsTemplatesIDLabels**
> LabelResponse postDocumentsTemplatesIDLabels(templateID, labelMapping, zapTraceSpan)

Add a label to a template

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
    defaultClient.setBasePath("/api/v2");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String templateID = "templateID_example"; // String | The template ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postDocumentsTemplatesIDLabels(templateID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#postDocumentsTemplatesIDLabels");
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
| **templateID** | **String**| The template ID. | |
| **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The label added to the template |  -  |
| **0** | Unexpected error |  -  |

<a id="putDocumentsTemplatesID"></a>
# **putDocumentsTemplatesID**
> Document putDocumentsTemplatesID(templateID, documentUpdate, zapTraceSpan)

Update a template

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
    defaultClient.setBasePath("/api/v2");

    TemplatesApi apiInstance = new TemplatesApi(defaultClient);
    String templateID = "templateID_example"; // String | The template ID.
    DocumentUpdate documentUpdate = new DocumentUpdate(); // DocumentUpdate | Template that will be updated
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Document result = apiInstance.putDocumentsTemplatesID(templateID, documentUpdate, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemplatesApi#putDocumentsTemplatesID");
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
| **templateID** | **String**| The template ID. | |
| **documentUpdate** | [**DocumentUpdate**](DocumentUpdate.md)| Template that will be updated | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The newly updated template |  -  |
| **0** | Unexpected error |  -  |

