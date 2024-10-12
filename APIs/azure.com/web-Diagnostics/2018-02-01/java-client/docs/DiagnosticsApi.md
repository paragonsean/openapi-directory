# DiagnosticsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**diagnosticsExecuteSiteAnalysis**](DiagnosticsApi.md#diagnosticsExecuteSiteAnalysis) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/analyses/{analysisName}/execute | Execute Analysis |
| [**diagnosticsExecuteSiteAnalysisSlot**](DiagnosticsApi.md#diagnosticsExecuteSiteAnalysisSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/analyses/{analysisName}/execute | Execute Analysis |
| [**diagnosticsExecuteSiteDetector**](DiagnosticsApi.md#diagnosticsExecuteSiteDetector) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/detectors/{detectorName}/execute | Execute Detector |
| [**diagnosticsExecuteSiteDetectorSlot**](DiagnosticsApi.md#diagnosticsExecuteSiteDetectorSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/detectors/{detectorName}/execute | Execute Detector |
| [**diagnosticsGetHostingEnvironmentDetectorResponse**](DiagnosticsApi.md#diagnosticsGetHostingEnvironmentDetectorResponse) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/detectors/{detectorName} | Get Hosting Environment Detector Response |
| [**diagnosticsGetSiteAnalysis**](DiagnosticsApi.md#diagnosticsGetSiteAnalysis) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/analyses/{analysisName} | Get Site Analysis |
| [**diagnosticsGetSiteAnalysisSlot**](DiagnosticsApi.md#diagnosticsGetSiteAnalysisSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/analyses/{analysisName} | Get Site Analysis |
| [**diagnosticsGetSiteDetector**](DiagnosticsApi.md#diagnosticsGetSiteDetector) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/detectors/{detectorName} | Get Detector |
| [**diagnosticsGetSiteDetectorResponse**](DiagnosticsApi.md#diagnosticsGetSiteDetectorResponse) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/detectors/{detectorName} | Get site detector response |
| [**diagnosticsGetSiteDetectorResponseSlot**](DiagnosticsApi.md#diagnosticsGetSiteDetectorResponseSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/detectors/{detectorName} | Get site detector response |
| [**diagnosticsGetSiteDetectorSlot**](DiagnosticsApi.md#diagnosticsGetSiteDetectorSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/detectors/{detectorName} | Get Detector |
| [**diagnosticsGetSiteDiagnosticCategory**](DiagnosticsApi.md#diagnosticsGetSiteDiagnosticCategory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory} | Get Diagnostics Category |
| [**diagnosticsGetSiteDiagnosticCategorySlot**](DiagnosticsApi.md#diagnosticsGetSiteDiagnosticCategorySlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory} | Get Diagnostics Category |
| [**diagnosticsListHostingEnvironmentDetectorResponses**](DiagnosticsApi.md#diagnosticsListHostingEnvironmentDetectorResponses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/detectors | List Hosting Environment Detector Responses |
| [**diagnosticsListSiteAnalyses**](DiagnosticsApi.md#diagnosticsListSiteAnalyses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/analyses | Get Site Analyses |
| [**diagnosticsListSiteAnalysesSlot**](DiagnosticsApi.md#diagnosticsListSiteAnalysesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/analyses | Get Site Analyses |
| [**diagnosticsListSiteDetectorResponses**](DiagnosticsApi.md#diagnosticsListSiteDetectorResponses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/detectors | List Site Detector Responses |
| [**diagnosticsListSiteDetectorResponsesSlot**](DiagnosticsApi.md#diagnosticsListSiteDetectorResponsesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/detectors | List Site Detector Responses |
| [**diagnosticsListSiteDetectors**](DiagnosticsApi.md#diagnosticsListSiteDetectors) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/detectors | Get Detectors |
| [**diagnosticsListSiteDetectorsSlot**](DiagnosticsApi.md#diagnosticsListSiteDetectorsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/detectors | Get Detectors |
| [**diagnosticsListSiteDiagnosticCategories**](DiagnosticsApi.md#diagnosticsListSiteDiagnosticCategories) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics | Get Diagnostics Categories |
| [**diagnosticsListSiteDiagnosticCategoriesSlot**](DiagnosticsApi.md#diagnosticsListSiteDiagnosticCategoriesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics | Get Diagnostics Categories |


<a id="diagnosticsExecuteSiteAnalysis"></a>
# **diagnosticsExecuteSiteAnalysis**
> DiagnosticAnalysis diagnosticsExecuteSiteAnalysis(resourceGroupName, siteName, diagnosticCategory, analysisName, subscriptionId, apiVersion, startTime, endTime, timeGrain)

Execute Analysis

Execute Analysis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Category Name
    String analysisName = "analysisName_example"; // String | Analysis Resource Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start Time
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End Time
    String timeGrain = "timeGrain_example"; // String | Time Grain
    try {
      DiagnosticAnalysis result = apiInstance.diagnosticsExecuteSiteAnalysis(resourceGroupName, siteName, diagnosticCategory, analysisName, subscriptionId, apiVersion, startTime, endTime, timeGrain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsExecuteSiteAnalysis");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Category Name | |
| **analysisName** | **String**| Analysis Resource Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **OffsetDateTime**| Start Time | [optional] |
| **endTime** | **OffsetDateTime**| End Time | [optional] |
| **timeGrain** | **String**| Time Grain | [optional] |

### Return type

[**DiagnosticAnalysis**](DiagnosticAnalysis.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsExecuteSiteAnalysisSlot"></a>
# **diagnosticsExecuteSiteAnalysisSlot**
> DiagnosticAnalysis diagnosticsExecuteSiteAnalysisSlot(resourceGroupName, siteName, diagnosticCategory, analysisName, slot, subscriptionId, apiVersion, startTime, endTime, timeGrain)

Execute Analysis

Execute Analysis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Category Name
    String analysisName = "analysisName_example"; // String | Analysis Resource Name
    String slot = "slot_example"; // String | Slot Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start Time
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End Time
    String timeGrain = "timeGrain_example"; // String | Time Grain
    try {
      DiagnosticAnalysis result = apiInstance.diagnosticsExecuteSiteAnalysisSlot(resourceGroupName, siteName, diagnosticCategory, analysisName, slot, subscriptionId, apiVersion, startTime, endTime, timeGrain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsExecuteSiteAnalysisSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Category Name | |
| **analysisName** | **String**| Analysis Resource Name | |
| **slot** | **String**| Slot Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **OffsetDateTime**| Start Time | [optional] |
| **endTime** | **OffsetDateTime**| End Time | [optional] |
| **timeGrain** | **String**| Time Grain | [optional] |

### Return type

[**DiagnosticAnalysis**](DiagnosticAnalysis.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsExecuteSiteDetector"></a>
# **diagnosticsExecuteSiteDetector**
> DiagnosticDetectorResponse diagnosticsExecuteSiteDetector(resourceGroupName, siteName, detectorName, diagnosticCategory, subscriptionId, apiVersion, startTime, endTime, timeGrain)

Execute Detector

Execute Detector

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String detectorName = "detectorName_example"; // String | Detector Resource Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Category Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start Time
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End Time
    String timeGrain = "timeGrain_example"; // String | Time Grain
    try {
      DiagnosticDetectorResponse result = apiInstance.diagnosticsExecuteSiteDetector(resourceGroupName, siteName, detectorName, diagnosticCategory, subscriptionId, apiVersion, startTime, endTime, timeGrain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsExecuteSiteDetector");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **detectorName** | **String**| Detector Resource Name | |
| **diagnosticCategory** | **String**| Category Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **OffsetDateTime**| Start Time | [optional] |
| **endTime** | **OffsetDateTime**| End Time | [optional] |
| **timeGrain** | **String**| Time Grain | [optional] |

### Return type

[**DiagnosticDetectorResponse**](DiagnosticDetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsExecuteSiteDetectorSlot"></a>
# **diagnosticsExecuteSiteDetectorSlot**
> DiagnosticDetectorResponse diagnosticsExecuteSiteDetectorSlot(resourceGroupName, siteName, detectorName, diagnosticCategory, slot, subscriptionId, apiVersion, startTime, endTime, timeGrain)

Execute Detector

Execute Detector

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String detectorName = "detectorName_example"; // String | Detector Resource Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Category Name
    String slot = "slot_example"; // String | Slot Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start Time
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End Time
    String timeGrain = "timeGrain_example"; // String | Time Grain
    try {
      DiagnosticDetectorResponse result = apiInstance.diagnosticsExecuteSiteDetectorSlot(resourceGroupName, siteName, detectorName, diagnosticCategory, slot, subscriptionId, apiVersion, startTime, endTime, timeGrain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsExecuteSiteDetectorSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **detectorName** | **String**| Detector Resource Name | |
| **diagnosticCategory** | **String**| Category Name | |
| **slot** | **String**| Slot Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **OffsetDateTime**| Start Time | [optional] |
| **endTime** | **OffsetDateTime**| End Time | [optional] |
| **timeGrain** | **String**| Time Grain | [optional] |

### Return type

[**DiagnosticDetectorResponse**](DiagnosticDetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsGetHostingEnvironmentDetectorResponse"></a>
# **diagnosticsGetHostingEnvironmentDetectorResponse**
> DetectorResponse diagnosticsGetHostingEnvironmentDetectorResponse(resourceGroupName, name, detectorName, subscriptionId, apiVersion, startTime, endTime, timeGrain)

Get Hosting Environment Detector Response

Get Hosting Environment Detector Response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | App Service Environment Name
    String detectorName = "detectorName_example"; // String | Detector Resource Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start Time
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End Time
    String timeGrain = "timeGrain_example"; // String | Time Grain
    try {
      DetectorResponse result = apiInstance.diagnosticsGetHostingEnvironmentDetectorResponse(resourceGroupName, name, detectorName, subscriptionId, apiVersion, startTime, endTime, timeGrain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsGetHostingEnvironmentDetectorResponse");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| App Service Environment Name | |
| **detectorName** | **String**| Detector Resource Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **OffsetDateTime**| Start Time | [optional] |
| **endTime** | **OffsetDateTime**| End Time | [optional] |
| **timeGrain** | **String**| Time Grain | [optional] |

### Return type

[**DetectorResponse**](DetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsGetSiteAnalysis"></a>
# **diagnosticsGetSiteAnalysis**
> DiagnosticAnalysis diagnosticsGetSiteAnalysis(resourceGroupName, siteName, diagnosticCategory, analysisName, subscriptionId, apiVersion)

Get Site Analysis

Get Site Analysis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String analysisName = "analysisName_example"; // String | Analysis Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticAnalysis result = apiInstance.diagnosticsGetSiteAnalysis(resourceGroupName, siteName, diagnosticCategory, analysisName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsGetSiteAnalysis");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **analysisName** | **String**| Analysis Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticAnalysis**](DiagnosticAnalysis.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsGetSiteAnalysisSlot"></a>
# **diagnosticsGetSiteAnalysisSlot**
> DiagnosticAnalysis diagnosticsGetSiteAnalysisSlot(resourceGroupName, siteName, diagnosticCategory, analysisName, slot, subscriptionId, apiVersion)

Get Site Analysis

Get Site Analysis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String analysisName = "analysisName_example"; // String | Analysis Name
    String slot = "slot_example"; // String | Slot - optional
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticAnalysis result = apiInstance.diagnosticsGetSiteAnalysisSlot(resourceGroupName, siteName, diagnosticCategory, analysisName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsGetSiteAnalysisSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **analysisName** | **String**| Analysis Name | |
| **slot** | **String**| Slot - optional | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticAnalysis**](DiagnosticAnalysis.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsGetSiteDetector"></a>
# **diagnosticsGetSiteDetector**
> DiagnosticDetectorCollection diagnosticsGetSiteDetector(resourceGroupName, siteName, diagnosticCategory, detectorName, subscriptionId, apiVersion)

Get Detector

Get Detector

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String detectorName = "detectorName_example"; // String | Detector Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticDetectorCollection result = apiInstance.diagnosticsGetSiteDetector(resourceGroupName, siteName, diagnosticCategory, detectorName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsGetSiteDetector");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **detectorName** | **String**| Detector Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticDetectorCollection**](DiagnosticDetectorCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsGetSiteDetectorResponse"></a>
# **diagnosticsGetSiteDetectorResponse**
> DetectorResponse diagnosticsGetSiteDetectorResponse(resourceGroupName, siteName, detectorName, subscriptionId, apiVersion, startTime, endTime, timeGrain)

Get site detector response

Get site detector response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String detectorName = "detectorName_example"; // String | Detector Resource Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start Time
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End Time
    String timeGrain = "timeGrain_example"; // String | Time Grain
    try {
      DetectorResponse result = apiInstance.diagnosticsGetSiteDetectorResponse(resourceGroupName, siteName, detectorName, subscriptionId, apiVersion, startTime, endTime, timeGrain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsGetSiteDetectorResponse");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **detectorName** | **String**| Detector Resource Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **OffsetDateTime**| Start Time | [optional] |
| **endTime** | **OffsetDateTime**| End Time | [optional] |
| **timeGrain** | **String**| Time Grain | [optional] |

### Return type

[**DetectorResponse**](DetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsGetSiteDetectorResponseSlot"></a>
# **diagnosticsGetSiteDetectorResponseSlot**
> DetectorResponse diagnosticsGetSiteDetectorResponseSlot(resourceGroupName, siteName, detectorName, slot, subscriptionId, apiVersion, startTime, endTime, timeGrain)

Get site detector response

Get site detector response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String detectorName = "detectorName_example"; // String | Detector Resource Name
    String slot = "slot_example"; // String | Slot Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start Time
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End Time
    String timeGrain = "timeGrain_example"; // String | Time Grain
    try {
      DetectorResponse result = apiInstance.diagnosticsGetSiteDetectorResponseSlot(resourceGroupName, siteName, detectorName, slot, subscriptionId, apiVersion, startTime, endTime, timeGrain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsGetSiteDetectorResponseSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **detectorName** | **String**| Detector Resource Name | |
| **slot** | **String**| Slot Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **OffsetDateTime**| Start Time | [optional] |
| **endTime** | **OffsetDateTime**| End Time | [optional] |
| **timeGrain** | **String**| Time Grain | [optional] |

### Return type

[**DetectorResponse**](DetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsGetSiteDetectorSlot"></a>
# **diagnosticsGetSiteDetectorSlot**
> DiagnosticDetectorCollection diagnosticsGetSiteDetectorSlot(resourceGroupName, siteName, diagnosticCategory, detectorName, slot, subscriptionId, apiVersion)

Get Detector

Get Detector

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String detectorName = "detectorName_example"; // String | Detector Name
    String slot = "slot_example"; // String | Slot Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticDetectorCollection result = apiInstance.diagnosticsGetSiteDetectorSlot(resourceGroupName, siteName, diagnosticCategory, detectorName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsGetSiteDetectorSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **detectorName** | **String**| Detector Name | |
| **slot** | **String**| Slot Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticDetectorCollection**](DiagnosticDetectorCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsGetSiteDiagnosticCategory"></a>
# **diagnosticsGetSiteDiagnosticCategory**
> DiagnosticCategory diagnosticsGetSiteDiagnosticCategory(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion)

Get Diagnostics Category

Get Diagnostics Category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticCategory result = apiInstance.diagnosticsGetSiteDiagnosticCategory(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsGetSiteDiagnosticCategory");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticCategory**](DiagnosticCategory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsGetSiteDiagnosticCategorySlot"></a>
# **diagnosticsGetSiteDiagnosticCategorySlot**
> DiagnosticCategory diagnosticsGetSiteDiagnosticCategorySlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion)

Get Diagnostics Category

Get Diagnostics Category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String slot = "slot_example"; // String | Slot Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticCategory result = apiInstance.diagnosticsGetSiteDiagnosticCategorySlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsGetSiteDiagnosticCategorySlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **slot** | **String**| Slot Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticCategory**](DiagnosticCategory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsListHostingEnvironmentDetectorResponses"></a>
# **diagnosticsListHostingEnvironmentDetectorResponses**
> DetectorResponseCollection diagnosticsListHostingEnvironmentDetectorResponses(resourceGroupName, name, subscriptionId, apiVersion)

List Hosting Environment Detector Responses

List Hosting Environment Detector Responses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Site Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DetectorResponseCollection result = apiInstance.diagnosticsListHostingEnvironmentDetectorResponses(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsListHostingEnvironmentDetectorResponses");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Site Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DetectorResponseCollection**](DetectorResponseCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsListSiteAnalyses"></a>
# **diagnosticsListSiteAnalyses**
> DiagnosticAnalysisCollection diagnosticsListSiteAnalyses(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion)

Get Site Analyses

Get Site Analyses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticAnalysisCollection result = apiInstance.diagnosticsListSiteAnalyses(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsListSiteAnalyses");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticAnalysisCollection**](DiagnosticAnalysisCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsListSiteAnalysesSlot"></a>
# **diagnosticsListSiteAnalysesSlot**
> DiagnosticAnalysisCollection diagnosticsListSiteAnalysesSlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion)

Get Site Analyses

Get Site Analyses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String slot = "slot_example"; // String | Slot Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticAnalysisCollection result = apiInstance.diagnosticsListSiteAnalysesSlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsListSiteAnalysesSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **slot** | **String**| Slot Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticAnalysisCollection**](DiagnosticAnalysisCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsListSiteDetectorResponses"></a>
# **diagnosticsListSiteDetectorResponses**
> DetectorResponseCollection diagnosticsListSiteDetectorResponses(resourceGroupName, siteName, subscriptionId, apiVersion)

List Site Detector Responses

List Site Detector Responses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DetectorResponseCollection result = apiInstance.diagnosticsListSiteDetectorResponses(resourceGroupName, siteName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsListSiteDetectorResponses");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DetectorResponseCollection**](DetectorResponseCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsListSiteDetectorResponsesSlot"></a>
# **diagnosticsListSiteDetectorResponsesSlot**
> DetectorResponseCollection diagnosticsListSiteDetectorResponsesSlot(resourceGroupName, siteName, slot, subscriptionId, apiVersion)

List Site Detector Responses

List Site Detector Responses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String slot = "slot_example"; // String | Slot Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DetectorResponseCollection result = apiInstance.diagnosticsListSiteDetectorResponsesSlot(resourceGroupName, siteName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsListSiteDetectorResponsesSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **slot** | **String**| Slot Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DetectorResponseCollection**](DetectorResponseCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsListSiteDetectors"></a>
# **diagnosticsListSiteDetectors**
> DiagnosticDetectorCollection diagnosticsListSiteDetectors(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion)

Get Detectors

Get Detectors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticDetectorCollection result = apiInstance.diagnosticsListSiteDetectors(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsListSiteDetectors");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticDetectorCollection**](DiagnosticDetectorCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsListSiteDetectorsSlot"></a>
# **diagnosticsListSiteDetectorsSlot**
> DiagnosticDetectorCollection diagnosticsListSiteDetectorsSlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion)

Get Detectors

Get Detectors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
    String slot = "slot_example"; // String | Slot Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticDetectorCollection result = apiInstance.diagnosticsListSiteDetectorsSlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsListSiteDetectorsSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **diagnosticCategory** | **String**| Diagnostic Category | |
| **slot** | **String**| Slot Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticDetectorCollection**](DiagnosticDetectorCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsListSiteDiagnosticCategories"></a>
# **diagnosticsListSiteDiagnosticCategories**
> DiagnosticCategoryCollection diagnosticsListSiteDiagnosticCategories(resourceGroupName, siteName, subscriptionId, apiVersion)

Get Diagnostics Categories

Get Diagnostics Categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticCategoryCollection result = apiInstance.diagnosticsListSiteDiagnosticCategories(resourceGroupName, siteName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsListSiteDiagnosticCategories");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticCategoryCollection**](DiagnosticCategoryCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="diagnosticsListSiteDiagnosticCategoriesSlot"></a>
# **diagnosticsListSiteDiagnosticCategoriesSlot**
> DiagnosticCategoryCollection diagnosticsListSiteDiagnosticCategoriesSlot(resourceGroupName, siteName, slot, subscriptionId, apiVersion)

Get Diagnostics Categories

Get Diagnostics Categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticsApi apiInstance = new DiagnosticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site Name
    String slot = "slot_example"; // String | Slot Name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DiagnosticCategoryCollection result = apiInstance.diagnosticsListSiteDiagnosticCategoriesSlot(resourceGroupName, siteName, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticsApi#diagnosticsListSiteDiagnosticCategoriesSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site Name | |
| **slot** | **String**| Slot Name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DiagnosticCategoryCollection**](DiagnosticCategoryCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

