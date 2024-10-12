# CatalogsImportationProcessApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**importationCancel**](CatalogsImportationProcessApi.md#importationCancel) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/cancel | Cancel importation |
| [**importationCommit**](CatalogsImportationProcessApi.md#importationCommit) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/commit | Commit Importation |
| [**importationCommitColumns**](CatalogsImportationProcessApi.md#importationCommitColumns) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/commitColumns | Commit columns |
| [**importationConfigureRemainingCatalogColumns**](CatalogsImportationProcessApi.md#importationConfigureRemainingCatalogColumns) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/configureRemainingCatalogColumns | Configure remaining catalog columns |
| [**importationGetImportationMonitoring**](CatalogsImportationProcessApi.md#importationGetImportationMonitoring) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId} | Get the importation status |
| [**importationGetProductsReport**](CatalogsImportationProcessApi.md#importationGetProductsReport) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/products/list | Importation Get Products Report |
| [**importationGetReport**](CatalogsImportationProcessApi.md#importationGetReport) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/report | Importation Get Report |
| [**importationGetReportings**](CatalogsImportationProcessApi.md#importationGetReportings) | **GET** /v2/user/catalogs/{storeId}/importations | Get the latest catalog importation reporting |
| [**importationGetReportingsAllStores**](CatalogsImportationProcessApi.md#importationGetReportingsAllStores) | **GET** /v2/user/catalogs/importations | Get the latest catalog importation reporting for all your stores |
| [**importationStartManualUpdate**](CatalogsImportationProcessApi.md#importationStartManualUpdate) | **POST** /v2/user/catalogs/{storeId}/importations/start | Start Manual Import |
| [**importationTechnicalProgression**](CatalogsImportationProcessApi.md#importationTechnicalProgression) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/technicalProgression | Get technical progression |


<a id="importationCancel"></a>
# **importationCancel**
> importationCancel(storeId, executionId)

Cancel importation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    try {
      apiInstance.importationCancel(storeId, executionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationCancel");
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
| **storeId** | **String**| Your store identifier | |
| **executionId** | **String**| The execution identifier of you catalog importation | |

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
| **204** | Catalog importation canceled |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationCommit"></a>
# **importationCommit**
> importationCommit(storeId, executionId)

Commit Importation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    try {
      apiInstance.importationCommit(storeId, executionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationCommit");
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
| **storeId** | **String**| Your store identifier | |
| **executionId** | **String**| The execution identifier of you catalog importation | |

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
| **204** | Catalog importation committed |  -  |
| **400** |  |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationCommitColumns"></a>
# **importationCommitColumns**
> importationCommitColumns(storeId, executionId)

Commit columns

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    try {
      apiInstance.importationCommitColumns(storeId, executionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationCommitColumns");
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
| **storeId** | **String**| Your store identifier | |
| **executionId** | **String**| The execution identifier of you catalog importation | |

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
| **204** | Columns configuration have been committed. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **400** | When a user column name is duplicate. When the catalog column name are duplicate. When the BeezUP column have duplicate mapping. Occurs when the required beezup column is not mapped to any column. Occurs when the category hierarchy is not correctly mapped. When the catalog column count limit has been reached. When the catalog custom column count limit has been reached. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. Occurs when a catalog column is not found. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationConfigureRemainingCatalogColumns"></a>
# **importationConfigureRemainingCatalogColumns**
> importationConfigureRemainingCatalogColumns(storeId, executionId)

Configure remaining catalog columns

This operation should be used after you have mapped the required BeezUP Columns

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    try {
      apiInstance.importationConfigureRemainingCatalogColumns(storeId, executionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationConfigureRemainingCatalogColumns");
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
| **storeId** | **String**| Your store identifier | |
| **executionId** | **String**| The execution identifier of you catalog importation | |

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
| **204** | Remaining catalog columns have been configured. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **400** | When a user column name is duplicate. When the catalog column name are duplicate. When the BeezUP column have duplicate mapping. Occurs when the required beezup column is not mapped to any column. Occurs when the category hierarchy is not correctly mapped. Occurs when the duplicate strategy on {catalogColumnName} is not found. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. Occurs when a catalog column is not found. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationGetImportationMonitoring"></a>
# **importationGetImportationMonitoring**
> ImportationMonitoring importationGetImportationMonitoring(storeId, executionId)

Get the importation status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    try {
      ImportationMonitoring result = apiInstance.importationGetImportationMonitoring(storeId, executionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationGetImportationMonitoring");
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
| **storeId** | **String**| Your store identifier | |
| **executionId** | **String**| The execution identifier of you catalog importation | |

### Return type

[**ImportationMonitoring**](ImportationMonitoring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | ExecutionId not found or not yet synchronized. If not synchronized within 30 sec after the import has been started, please contact our support |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationGetProductsReport"></a>
# **importationGetProductsReport**
> GetImportationProductsReportResponse importationGetProductsReport(storeId, executionId, getImportationProductsReportRequest)

Importation Get Products Report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    GetImportationProductsReportRequest getImportationProductsReportRequest = new GetImportationProductsReportRequest(); // GetImportationProductsReportRequest | 
    try {
      GetImportationProductsReportResponse result = apiInstance.importationGetProductsReport(storeId, executionId, getImportationProductsReportRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationGetProductsReport");
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
| **storeId** | **String**| Your store identifier | |
| **executionId** | **String**| The execution identifier of you catalog importation | |
| **getImportationProductsReportRequest** | [**GetImportationProductsReportRequest**](GetImportationProductsReportRequest.md)|  | |

### Return type

[**GetImportationProductsReportResponse**](GetImportationProductsReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Products Report Response |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. |  -  |
| **409** | Report Not ready Yet. Please retry in a few minutes. |  -  |

<a id="importationGetReport"></a>
# **importationGetReport**
> GetImportationReportResponse importationGetReport(storeId, executionId)

Importation Get Report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    try {
      GetImportationReportResponse result = apiInstance.importationGetReport(storeId, executionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationGetReport");
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
| **storeId** | **String**| Your store identifier | |
| **executionId** | **String**| The execution identifier of you catalog importation | |

### Return type

[**GetImportationReportResponse**](GetImportationReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Report Response |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. |  -  |
| **409** | Report Not ready Yet. Please retry in a few minutes. |  -  |

<a id="importationGetReportings"></a>
# **importationGetReportings**
> ImportationsResponse importationGetReportings(storeId)

Get the latest catalog importation reporting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      ImportationsResponse result = apiInstance.importationGetReportings(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationGetReportings");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**ImportationsResponse**](ImportationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The last importation reportings |  -  |
| **404** | StoreId not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationGetReportingsAllStores"></a>
# **importationGetReportingsAllStores**
> Map&lt;String, ImportationsResponse&gt; importationGetReportingsAllStores()

Get the latest catalog importation reporting for all your stores

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    try {
      Map<String, ImportationsResponse> result = apiInstance.importationGetReportingsAllStores();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationGetReportingsAllStores");
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

[**Map&lt;String, ImportationsResponse&gt;**](ImportationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The last importation reportings |  -  |
| **404** | UserId not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationStartManualUpdate"></a>
# **importationStartManualUpdate**
> LinksImportationGetImportationMonitoringLink importationStartManualUpdate(storeId, startManualImportRequest)

Start Manual Import

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    StartManualImportRequest startManualImportRequest = new StartManualImportRequest(); // StartManualImportRequest | 
    try {
      LinksImportationGetImportationMonitoringLink result = apiInstance.importationStartManualUpdate(storeId, startManualImportRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationStartManualUpdate");
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
| **storeId** | **String**| Your store identifier | |
| **startManualImportRequest** | [**StartManualImportRequest**](StartManualImportRequest.md)|  | |

### Return type

[**LinksImportationGetImportationMonitoringLink**](LinksImportationGetImportationMonitoringLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Catalog importation started |  * Location - The location of the generated invoice. Might take a few seconds to be available <br>  * Retry-After - The duration in second to wait before polling this resource <br>  |
| **400** | Missing Input configuration in the request Occurs when there is a duplicate file number in the input configuration Occurs when there is a duplicate file Uri in the input configuration |  -  |
| **404** | StoreId not found |  -  |
| **409** | A catalog importation is already in progress! |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationTechnicalProgression"></a>
# **importationTechnicalProgression**
> ImportationTechnicalProgression importationTechnicalProgression(storeId, executionId)

Get technical progression

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationProcessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationProcessApi apiInstance = new CatalogsImportationProcessApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    try {
      ImportationTechnicalProgression result = apiInstance.importationTechnicalProgression(storeId, executionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationProcessApi#importationTechnicalProgression");
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
| **storeId** | **String**| Your store identifier | |
| **executionId** | **String**| The execution identifier of you catalog importation | |

### Return type

[**ImportationTechnicalProgression**](ImportationTechnicalProgression.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | When the technical progression is correctly retrived |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

