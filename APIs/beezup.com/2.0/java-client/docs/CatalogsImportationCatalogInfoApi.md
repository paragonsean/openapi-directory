# CatalogsImportationCatalogInfoApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**importationConfigureCatalogColumn**](CatalogsImportationCatalogInfoApi.md#importationConfigureCatalogColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId} | Configure catalog column |
| [**importationDeleteCustomColumn**](CatalogsImportationCatalogInfoApi.md#importationDeleteCustomColumn) | **DELETE** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId} | Delete Custom Column |
| [**importationGetCustomColumnExpression**](CatalogsImportationCatalogInfoApi.md#importationGetCustomColumnExpression) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId}/expression | Get the encrypted custom column expression in this importation |
| [**importationGetCustomColumns**](CatalogsImportationCatalogInfoApi.md#importationGetCustomColumns) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns | Get custom columns currently place in this importation |
| [**importationGetDetectedCatalogColumns**](CatalogsImportationCatalogInfoApi.md#importationGetDetectedCatalogColumns) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns | Get detected catalog columns during this importation. |
| [**importationGetProductSample**](CatalogsImportationCatalogInfoApi.md#importationGetProductSample) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/productSamples/{productSampleIndex} | Get the product sample related to this importation with all columns (catalog and custom) |
| [**importationGetProductSampleCustomColumnValue**](CatalogsImportationCatalogInfoApi.md#importationGetProductSampleCustomColumnValue) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/productSamples/{productSampleIndex}/customColumns/{columnId} | Get product sample custom column value related to this importation. |
| [**importationIgnoreColumn**](CatalogsImportationCatalogInfoApi.md#importationIgnoreColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId}/ignore | Ignore Column |
| [**importationMapCatalogColumn**](CatalogsImportationCatalogInfoApi.md#importationMapCatalogColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId}/map | Map catalog column to a BeezUP column |
| [**importationMapCustomColumn**](CatalogsImportationCatalogInfoApi.md#importationMapCustomColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId}/map | Map custom column to a BeezUP column |
| [**importationReattendColumn**](CatalogsImportationCatalogInfoApi.md#importationReattendColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId}/reattend | Reattend Column |
| [**importationSaveCustomColumn**](CatalogsImportationCatalogInfoApi.md#importationSaveCustomColumn) | **PUT** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId} | Create or replace a custom column |
| [**importationUnmapCatalogColumn**](CatalogsImportationCatalogInfoApi.md#importationUnmapCatalogColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId}/unmap | Unmap catalog column |
| [**importationUnmapCustomColumn**](CatalogsImportationCatalogInfoApi.md#importationUnmapCustomColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId}/unmap | Unmap custom column |


<a id="importationConfigureCatalogColumn"></a>
# **importationConfigureCatalogColumn**
> importationConfigureCatalogColumn(storeId, executionId, columnId, configureCatalogColumnCatalogRequest)

Configure catalog column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The custom column identifier
    ConfigureCatalogColumnCatalogRequest configureCatalogColumnCatalogRequest = new ConfigureCatalogColumnCatalogRequest(); // ConfigureCatalogColumnCatalogRequest | 
    try {
      apiInstance.importationConfigureCatalogColumn(storeId, executionId, columnId, configureCatalogColumnCatalogRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationConfigureCatalogColumn");
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
| **columnId** | **String**| The custom column identifier | |
| **configureCatalogColumnCatalogRequest** | [**ConfigureCatalogColumnCatalogRequest**](ConfigureCatalogColumnCatalogRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Catalog column configured. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **400** |  When the catalog column name is not found |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. Occurs when a catalog column is not found. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationDeleteCustomColumn"></a>
# **importationDeleteCustomColumn**
> importationDeleteCustomColumn(storeId, executionId, columnId)

Delete Custom Column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The custom column identifier
    try {
      apiInstance.importationDeleteCustomColumn(storeId, executionId, columnId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationDeleteCustomColumn");
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
| **columnId** | **String**| The custom column identifier | |

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
| **204** | When the custom column for this importation is correctly deleted |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationGetCustomColumnExpression"></a>
# **importationGetCustomColumnExpression**
> String importationGetCustomColumnExpression(storeId, executionId, columnId)

Get the encrypted custom column expression in this importation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The custom column identifier
    try {
      String result = apiInstance.importationGetCustomColumnExpression(storeId, executionId, columnId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationGetCustomColumnExpression");
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
| **columnId** | **String**| The custom column identifier | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Encrypted expression |  -  |
| **404** | ExecutionId not found or not yet synchronized. If not synchronized within 30 sec, please contact our support |  -  |
| **409** | Catalog preparation read step is not completed. Please refer to the reporting of this execution for more details. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationGetCustomColumns"></a>
# **importationGetCustomColumns**
> ImportationCustomColumnList importationGetCustomColumns(storeId, executionId)

Get custom columns currently place in this importation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    try {
      ImportationCustomColumnList result = apiInstance.importationGetCustomColumns(storeId, executionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationGetCustomColumns");
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

[**ImportationCustomColumnList**](ImportationCustomColumnList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom columns of current Importation successfully retrieved |  -  |
| **404** | ExecutionId not found or not yet synchronized. If not synchronized within 30 sec, please contact our support |  -  |
| **409** | Catalog preparation read step is not completed. Please refer to the reporting of this execution for more details. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationGetDetectedCatalogColumns"></a>
# **importationGetDetectedCatalogColumns**
> DetectedCatalogColumnList importationGetDetectedCatalogColumns(storeId, executionId)

Get detected catalog columns during this importation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    try {
      DetectedCatalogColumnList result = apiInstance.importationGetDetectedCatalogColumns(storeId, executionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationGetDetectedCatalogColumns");
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

[**DetectedCatalogColumnList**](DetectedCatalogColumnList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | ExecutionId not found or not yet synchronized. If not synchronized within 30 sec, please contact our support |  -  |
| **409** | Catalog preparation read step is not completed. Please refer to the reporting of this execution for more details. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationGetProductSample"></a>
# **importationGetProductSample**
> ProductSample importationGetProductSample(storeId, executionId, productSampleIndex)

Get the product sample related to this importation with all columns (catalog and custom)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    Integer productSampleIndex = 56; // Integer | Index of the product sample. Starting from 0 to 99.
    try {
      ProductSample result = apiInstance.importationGetProductSample(storeId, executionId, productSampleIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationGetProductSample");
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
| **productSampleIndex** | **Integer**| Index of the product sample. Starting from 0 to 99. | |

### Return type

[**ProductSample**](ProductSample.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | ExecutionId not found or not yet synchronized. If not synchronized within 30 sec, please contact our support       schema: $ref: &#39;https://api.beezup.com/swaggerhub/domains/BeezUP/api.beezup.com/v2#/definitions/BeezUP.Common.ErrorResponseMessage&#39; |  -  |
| **409** | Catalog preparation read step is not completed. Please refer to the reporting of this execution for more details. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationGetProductSampleCustomColumnValue"></a>
# **importationGetProductSampleCustomColumnValue**
> String importationGetProductSampleCustomColumnValue(storeId, executionId, productSampleIndex, columnId)

Get product sample custom column value related to this importation.

/!\\ Use this operation only when you just changed the custom column expression and you want to get a precise the property value. Otherwise use the operation Importation_GetProductSample which will give you all property values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    Integer productSampleIndex = 56; // Integer | Index of the product sample. Starting from 0 to 99.
    String columnId = "columnId_example"; // String | The custom column identifier
    try {
      String result = apiInstance.importationGetProductSampleCustomColumnValue(storeId, executionId, productSampleIndex, columnId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationGetProductSampleCustomColumnValue");
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
| **productSampleIndex** | **Integer**| Index of the product sample. Starting from 0 to 99. | |
| **columnId** | **String**| The custom column identifier | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product sample custom column value |  -  |
| **404** | ExecutionId not found or not yet synchronized. If not synchronized within 30 sec, please contact our support |  * Retry-After - The duration in second to wait before polling this resource <br>  |
| **409** | Catalog preparation read step is not completed. Please refer to the reporting of this execution for more details. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationIgnoreColumn"></a>
# **importationIgnoreColumn**
> importationIgnoreColumn(storeId, executionId, columnId)

Ignore Column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The custom column identifier
    try {
      apiInstance.importationIgnoreColumn(storeId, executionId, columnId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationIgnoreColumn");
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
| **columnId** | **String**| The custom column identifier | |

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
| **204** | Catalog column ignored. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. Occurs when a catalog column is not found. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationMapCatalogColumn"></a>
# **importationMapCatalogColumn**
> importationMapCatalogColumn(storeId, executionId, columnId, mapBeezUPColumnRequest)

Map catalog column to a BeezUP column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The catalog column identifier
    MapBeezUPColumnRequest mapBeezUPColumnRequest = new MapBeezUPColumnRequest(); // MapBeezUPColumnRequest | 
    try {
      apiInstance.importationMapCatalogColumn(storeId, executionId, columnId, mapBeezUPColumnRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationMapCatalogColumn");
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
| **columnId** | **String**| The catalog column identifier | |
| **mapBeezUPColumnRequest** | [**MapBeezUPColumnRequest**](MapBeezUPColumnRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Catalog column mapped. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. Occurs when a catalog column is not found. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationMapCustomColumn"></a>
# **importationMapCustomColumn**
> importationMapCustomColumn(storeId, executionId, columnId, mapBeezUPColumnRequest)

Map custom column to a BeezUP column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The custom column identifier
    MapBeezUPColumnRequest mapBeezUPColumnRequest = new MapBeezUPColumnRequest(); // MapBeezUPColumnRequest | 
    try {
      apiInstance.importationMapCustomColumn(storeId, executionId, columnId, mapBeezUPColumnRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationMapCustomColumn");
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
| **columnId** | **String**| The custom column identifier | |
| **mapBeezUPColumnRequest** | [**MapBeezUPColumnRequest**](MapBeezUPColumnRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Custom column mapped. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. Occurs when a catalog column is not found. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationReattendColumn"></a>
# **importationReattendColumn**
> importationReattendColumn(storeId, executionId, columnId)

Reattend Column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The custom column identifier
    try {
      apiInstance.importationReattendColumn(storeId, executionId, columnId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationReattendColumn");
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
| **columnId** | **String**| The custom column identifier | |

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
| **204** | Catalog column reattended. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. Occurs when a catalog column is not found. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationSaveCustomColumn"></a>
# **importationSaveCustomColumn**
> importationSaveCustomColumn(storeId, executionId, columnId, changeCustomColumnRequest)

Create or replace a custom column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The custom column identifier
    ChangeCustomColumnRequest changeCustomColumnRequest = new ChangeCustomColumnRequest(); // ChangeCustomColumnRequest | 
    try {
      apiInstance.importationSaveCustomColumn(storeId, executionId, columnId, changeCustomColumnRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationSaveCustomColumn");
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
| **columnId** | **String**| The custom column identifier | |
| **changeCustomColumnRequest** | [**ChangeCustomColumnRequest**](ChangeCustomColumnRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Custom column configured. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationUnmapCatalogColumn"></a>
# **importationUnmapCatalogColumn**
> importationUnmapCatalogColumn(storeId, executionId, columnId)

Unmap catalog column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The catalog column identifier
    try {
      apiInstance.importationUnmapCatalogColumn(storeId, executionId, columnId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationUnmapCatalogColumn");
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
| **columnId** | **String**| The catalog column identifier | |

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
| **204** | Catalog Column unmapped. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. Occurs when a catalog column is not found. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationUnmapCustomColumn"></a>
# **importationUnmapCustomColumn**
> importationUnmapCustomColumn(storeId, executionId, columnId)

Unmap custom column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsImportationCatalogInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsImportationCatalogInfoApi apiInstance = new CatalogsImportationCatalogInfoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String executionId = "executionId_example"; // String | The execution identifier of you catalog importation
    String columnId = "columnId_example"; // String | The custom column identifier
    try {
      apiInstance.importationUnmapCustomColumn(storeId, executionId, columnId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsImportationCatalogInfoApi#importationUnmapCustomColumn");
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
| **columnId** | **String**| The custom column identifier | |

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
| **204** | Custom column unmapped. This operation has no impact on the current catalog until you commit the catalog importation. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when the message concerns the wrong execution. Occurs when a catalog column is not found. |  -  |
| **409** | Occurs when this importation is already finished. |  -  |
| **0** | Occurs when something goes wrong |  -  |

