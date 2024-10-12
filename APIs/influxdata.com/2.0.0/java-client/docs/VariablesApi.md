# VariablesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteVariablesID**](VariablesApi.md#deleteVariablesID) | **DELETE** /variables/{variableID} | Delete a variable |
| [**deleteVariablesIDLabelsID**](VariablesApi.md#deleteVariablesIDLabelsID) | **DELETE** /variables/{variableID}/labels/{labelID} | Delete a label from a variable |
| [**getVariables**](VariablesApi.md#getVariables) | **GET** /variables | List all variables |
| [**getVariablesID**](VariablesApi.md#getVariablesID) | **GET** /variables/{variableID} | Retrieve a variable |
| [**getVariablesIDLabels**](VariablesApi.md#getVariablesIDLabels) | **GET** /variables/{variableID}/labels | List all labels for a variable |
| [**patchVariablesID**](VariablesApi.md#patchVariablesID) | **PATCH** /variables/{variableID} | Update a variable |
| [**postVariables**](VariablesApi.md#postVariables) | **POST** /variables | Create a variable |
| [**postVariablesIDLabels**](VariablesApi.md#postVariablesIDLabels) | **POST** /variables/{variableID}/labels | Add a label to a variable |
| [**putVariablesID**](VariablesApi.md#putVariablesID) | **PUT** /variables/{variableID} | Replace a variable |


<a id="deleteVariablesID"></a>
# **deleteVariablesID**
> deleteVariablesID(variableID, zapTraceSpan)

Delete a variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    VariablesApi apiInstance = new VariablesApi(defaultClient);
    String variableID = "variableID_example"; // String | The variable ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteVariablesID(variableID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariablesApi#deleteVariablesID");
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
| **variableID** | **String**| The variable ID. | |
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
| **204** | Variable deleted |  -  |
| **0** | Non 2XX error response from server. |  -  |

<a id="deleteVariablesIDLabelsID"></a>
# **deleteVariablesIDLabelsID**
> deleteVariablesIDLabelsID(variableID, labelID, zapTraceSpan)

Delete a label from a variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    VariablesApi apiInstance = new VariablesApi(defaultClient);
    String variableID = "variableID_example"; // String | The variable ID.
    String labelID = "labelID_example"; // String | The label ID to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteVariablesIDLabelsID(variableID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariablesApi#deleteVariablesIDLabelsID");
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
| **variableID** | **String**| The variable ID. | |
| **labelID** | **String**| The label ID to delete. | |
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
| **404** | Variable not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getVariables"></a>
# **getVariables**
> Variables getVariables(zapTraceSpan, org, orgID)

List all variables

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    VariablesApi apiInstance = new VariablesApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String org = "org_example"; // String | The name of the organization.
    String orgID = "orgID_example"; // String | The organization ID.
    try {
      Variables result = apiInstance.getVariables(zapTraceSpan, org, orgID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariablesApi#getVariables");
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
| **org** | **String**| The name of the organization. | [optional] |
| **orgID** | **String**| The organization ID. | [optional] |

### Return type

[**Variables**](Variables.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of variables for an organization |  -  |
| **400** | Non 2XX error response from server. |  -  |
| **0** | Non 2XX error response from server. |  -  |

<a id="getVariablesID"></a>
# **getVariablesID**
> Variable getVariablesID(variableID, zapTraceSpan)

Retrieve a variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    VariablesApi apiInstance = new VariablesApi(defaultClient);
    String variableID = "variableID_example"; // String | The variable ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Variable result = apiInstance.getVariablesID(variableID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariablesApi#getVariablesID");
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
| **variableID** | **String**| The variable ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Variable found |  -  |
| **404** | Non 2XX error response from server. |  -  |
| **0** | Non 2XX error response from server. |  -  |

<a id="getVariablesIDLabels"></a>
# **getVariablesIDLabels**
> LabelsResponse getVariablesIDLabels(variableID, zapTraceSpan)

List all labels for a variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    VariablesApi apiInstance = new VariablesApi(defaultClient);
    String variableID = "variableID_example"; // String | The variable ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getVariablesIDLabels(variableID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariablesApi#getVariablesIDLabels");
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
| **variableID** | **String**| The variable ID. | |
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
| **200** | A list of all labels for a variable |  -  |
| **0** | Unexpected error |  -  |

<a id="patchVariablesID"></a>
# **patchVariablesID**
> Variable patchVariablesID(variableID, variable, zapTraceSpan)

Update a variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    VariablesApi apiInstance = new VariablesApi(defaultClient);
    String variableID = "variableID_example"; // String | The variable ID.
    Variable variable = new Variable(); // Variable | Variable update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Variable result = apiInstance.patchVariablesID(variableID, variable, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariablesApi#patchVariablesID");
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
| **variableID** | **String**| The variable ID. | |
| **variable** | [**Variable**](Variable.md)| Variable update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Variable updated |  -  |
| **0** | Non 2XX error response from server. |  -  |

<a id="postVariables"></a>
# **postVariables**
> Variable postVariables(variable, zapTraceSpan)

Create a variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    VariablesApi apiInstance = new VariablesApi(defaultClient);
    Variable variable = new Variable(); // Variable | Variable to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Variable result = apiInstance.postVariables(variable, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariablesApi#postVariables");
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
| **variable** | [**Variable**](Variable.md)| Variable to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Variable created |  -  |
| **0** | Non 2XX error response from server. |  -  |

<a id="postVariablesIDLabels"></a>
# **postVariablesIDLabels**
> LabelResponse postVariablesIDLabels(variableID, labelMapping, zapTraceSpan)

Add a label to a variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    VariablesApi apiInstance = new VariablesApi(defaultClient);
    String variableID = "variableID_example"; // String | The variable ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postVariablesIDLabels(variableID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariablesApi#postVariablesIDLabels");
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
| **variableID** | **String**| The variable ID. | |
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
| **201** | The newly added label |  -  |
| **0** | Unexpected error |  -  |

<a id="putVariablesID"></a>
# **putVariablesID**
> Variable putVariablesID(variableID, variable, zapTraceSpan)

Replace a variable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    VariablesApi apiInstance = new VariablesApi(defaultClient);
    String variableID = "variableID_example"; // String | The variable ID.
    Variable variable = new Variable(); // Variable | Variable to replace
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Variable result = apiInstance.putVariablesID(variableID, variable, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariablesApi#putVariablesID");
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
| **variableID** | **String**| The variable ID. | |
| **variable** | [**Variable**](Variable.md)| Variable to replace | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Variable updated |  -  |
| **0** | Non 2XX error response from server. |  -  |

