# InfluxDbTemplatesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applyTemplate**](InfluxDbTemplatesApi.md#applyTemplate) | **POST** /templates/apply | Apply or dry-run an InfluxDB Template |
| [**createStack**](InfluxDbTemplatesApi.md#createStack) | **POST** /stacks | Create a new stack |
| [**deleteStack**](InfluxDbTemplatesApi.md#deleteStack) | **DELETE** /stacks/{stack_id} | Delete a stack and associated resources |
| [**exportTemplate**](InfluxDbTemplatesApi.md#exportTemplate) | **POST** /templates/export | Export a new Influx Template |
| [**listStacks**](InfluxDbTemplatesApi.md#listStacks) | **GET** /stacks | List all installed InfluxDB templates |
| [**readStack**](InfluxDbTemplatesApi.md#readStack) | **GET** /stacks/{stack_id} | Retrieve a stack |
| [**uninstallStack**](InfluxDbTemplatesApi.md#uninstallStack) | **POST** /stacks/{stack_id}/uninstall | Uninstall an InfluxDB Stack |
| [**updateStack**](InfluxDbTemplatesApi.md#updateStack) | **PATCH** /stacks/{stack_id} | Update an InfluxDB Stack |


<a id="applyTemplate"></a>
# **applyTemplate**
> TemplateSummary applyTemplate(templateApply)

Apply or dry-run an InfluxDB Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfluxDbTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    InfluxDbTemplatesApi apiInstance = new InfluxDbTemplatesApi(defaultClient);
    TemplateApply templateApply = new TemplateApply(); // TemplateApply | 
    try {
      TemplateSummary result = apiInstance.applyTemplate(templateApply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfluxDbTemplatesApi#applyTemplate");
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
| **templateApply** | [**TemplateApply**](TemplateApply.md)|  | |

### Return type

[**TemplateSummary**](TemplateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-jsonnet, text/yml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Influx package dry-run successful, no new resources created. The provided diff and summary will not have IDs for resources that do not exist at the time of the dry run.  |  -  |
| **201** | Influx package applied successfully. Newly created resources created available in summary. The diff compares the state of the world before the package is applied with the changes the application will impose. This corresponds to &#x60;\&quot;dryRun\&quot;: true&#x60;  |  -  |
| **0** | Unexpected error |  -  |

<a id="createStack"></a>
# **createStack**
> Stack createStack(postStackRequest)

Create a new stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfluxDbTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    InfluxDbTemplatesApi apiInstance = new InfluxDbTemplatesApi(defaultClient);
    PostStackRequest postStackRequest = new PostStackRequest(); // PostStackRequest | Stack to create.
    try {
      Stack result = apiInstance.createStack(postStackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfluxDbTemplatesApi#createStack");
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
| **postStackRequest** | [**PostStackRequest**](PostStackRequest.md)| Stack to create. | |

### Return type

[**Stack**](Stack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | InfluxDB Stack created |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteStack"></a>
# **deleteStack**
> deleteStack(stackId, orgID)

Delete a stack and associated resources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfluxDbTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    InfluxDbTemplatesApi apiInstance = new InfluxDbTemplatesApi(defaultClient);
    String stackId = "stackId_example"; // String | Theidentifier of the stack.
    String orgID = "orgID_example"; // String | The identifier of the organization.
    try {
      apiInstance.deleteStack(stackId, orgID);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfluxDbTemplatesApi#deleteStack");
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
| **stackId** | **String**| Theidentifier of the stack. | |
| **orgID** | **String**| The identifier of the organization. | |

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
| **204** | The stack and its associated resources are deleted |  -  |
| **0** | Unexpected error |  -  |

<a id="exportTemplate"></a>
# **exportTemplate**
> List&lt;TemplateInner&gt; exportTemplate(exportTemplateRequest)

Export a new Influx Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfluxDbTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    InfluxDbTemplatesApi apiInstance = new InfluxDbTemplatesApi(defaultClient);
    ExportTemplateRequest exportTemplateRequest = new ExportTemplateRequest(); // ExportTemplateRequest | Export resources as an InfluxDB template.
    try {
      List<TemplateInner> result = apiInstance.exportTemplate(exportTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfluxDbTemplatesApi#exportTemplate");
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
| **exportTemplateRequest** | [**ExportTemplateRequest**](ExportTemplateRequest.md)| Export resources as an InfluxDB template. | [optional] |

### Return type

[**List&lt;TemplateInner&gt;**](TemplateInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InfluxDB template created |  -  |
| **0** | Unexpected error |  -  |

<a id="listStacks"></a>
# **listStacks**
> ListStacks200Response listStacks(orgID, name, stackID)

List all installed InfluxDB templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfluxDbTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    InfluxDbTemplatesApi apiInstance = new InfluxDbTemplatesApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization id of the stacks
    String name = "name_example"; // String | A collection of names to filter the list by.
    String stackID = "stackID_example"; // String | A collection of stackIDs to filter the list by.
    try {
      ListStacks200Response result = apiInstance.listStacks(orgID, name, stackID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfluxDbTemplatesApi#listStacks");
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
| **orgID** | **String**| The organization id of the stacks | |
| **name** | **String**| A collection of names to filter the list by. | [optional] |
| **stackID** | **String**| A collection of stackIDs to filter the list by. | [optional] |

### Return type

[**ListStacks200Response**](ListStacks200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Influx stacks found |  -  |
| **0** | Unexpected error |  -  |

<a id="readStack"></a>
# **readStack**
> Stack readStack(stackId)

Retrieve a stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfluxDbTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    InfluxDbTemplatesApi apiInstance = new InfluxDbTemplatesApi(defaultClient);
    String stackId = "stackId_example"; // String | Theidentifier of the stack.
    try {
      Stack result = apiInstance.readStack(stackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfluxDbTemplatesApi#readStack");
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
| **stackId** | **String**| Theidentifier of the stack. | |

### Return type

[**Stack**](Stack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The InfluxDB stack |  -  |
| **0** | Unexpected error |  -  |

<a id="uninstallStack"></a>
# **uninstallStack**
> Stack uninstallStack(stackId)

Uninstall an InfluxDB Stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfluxDbTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    InfluxDbTemplatesApi apiInstance = new InfluxDbTemplatesApi(defaultClient);
    String stackId = "stackId_example"; // String | The stack id
    try {
      Stack result = apiInstance.uninstallStack(stackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfluxDbTemplatesApi#uninstallStack");
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
| **stackId** | **String**| The stack id | |

### Return type

[**Stack**](Stack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Influx stack uninstalled |  -  |
| **0** | Unexpected error |  -  |

<a id="updateStack"></a>
# **updateStack**
> Stack updateStack(stackId, patchStackRequest)

Update an InfluxDB Stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfluxDbTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    InfluxDbTemplatesApi apiInstance = new InfluxDbTemplatesApi(defaultClient);
    String stackId = "stackId_example"; // String | Theidentifier of the stack.
    PatchStackRequest patchStackRequest = new PatchStackRequest(); // PatchStackRequest | Influx stack to update.
    try {
      Stack result = apiInstance.updateStack(stackId, patchStackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfluxDbTemplatesApi#updateStack");
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
| **stackId** | **String**| Theidentifier of the stack. | |
| **patchStackRequest** | [**PatchStackRequest**](PatchStackRequest.md)| Influx stack to update. | |

### Return type

[**Stack**](Stack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Influx stack updated |  -  |
| **0** | Unexpected error |  -  |

