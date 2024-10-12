# AnalysisRulePlugInApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analysisRulePlugInGet**](AnalysisRulePlugInApi.md#analysisRulePlugInGet) | **GET** /analysisruleplugins/{webId} | Retrieve an Analysis Rule Plug-in. |
| [**analysisRulePlugInGetByPath**](AnalysisRulePlugInApi.md#analysisRulePlugInGetByPath) | **GET** /analysisruleplugins | Retrieve an Analysis Rule Plug-in by path. |


<a id="analysisRulePlugInGet"></a>
# **analysisRulePlugInGet**
> AnalysisRulePlugIn analysisRulePlugInGet(webId, selectedFields, webIdType)

Retrieve an Analysis Rule Plug-in.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisRulePlugInApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AnalysisRulePlugInApi apiInstance = new AnalysisRulePlugInApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the Analysis Rule Plug-in.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      AnalysisRulePlugIn result = apiInstance.analysisRulePlugInGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisRulePlugInApi#analysisRulePlugInGet");
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
| **webId** | **String**| The ID of the Analysis Rule Plug-in. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**AnalysisRulePlugIn**](AnalysisRulePlugIn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified Analysis Rule Plug-in. |  -  |

<a id="analysisRulePlugInGetByPath"></a>
# **analysisRulePlugInGetByPath**
> AnalysisRulePlugIn analysisRulePlugInGetByPath(path, selectedFields, webIdType)

Retrieve an Analysis Rule Plug-in by path.

This method returns an Analysis Rule Plug-in based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisRulePlugInApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    AnalysisRulePlugInApi apiInstance = new AnalysisRulePlugInApi(defaultClient);
    String path = "path_example"; // String | The path to the Analysis Rule Plug-in.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      AnalysisRulePlugIn result = apiInstance.analysisRulePlugInGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisRulePlugInApi#analysisRulePlugInGetByPath");
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
| **path** | **String**| The path to the Analysis Rule Plug-in. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**AnalysisRulePlugIn**](AnalysisRulePlugIn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified Analysis Rule Plug-in. |  -  |

