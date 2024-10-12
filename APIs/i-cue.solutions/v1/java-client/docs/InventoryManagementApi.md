# InventoryManagementApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**inventoryAmazonIpiPost**](InventoryManagementApi.md#inventoryAmazonIpiPost) | **POST** /inventory/amazon-ipi | Calculate Amazon Inventory Performance Index (IPI) |
| [**inventoryCaryyingCostPost**](InventoryManagementApi.md#inventoryCaryyingCostPost) | **POST** /inventory/caryying-cost | Carrying Cost |
| [**inventoryEoqPost**](InventoryManagementApi.md#inventoryEoqPost) | **POST** /inventory/eoq | Calculate economic order quantity |
| [**inventoryFillRatePost**](InventoryManagementApi.md#inventoryFillRatePost) | **POST** /inventory/fill-rate | Calculate fill rate |
| [**inventoryFinancialImapctForecastAccuracyPost**](InventoryManagementApi.md#inventoryFinancialImapctForecastAccuracyPost) | **POST** /inventory/financial-imapct-forecast-accuracy | Calculate financial impact of forecast accuracy |
| [**inventoryInventoryTurnoverPost**](InventoryManagementApi.md#inventoryInventoryTurnoverPost) | **POST** /inventory/inventory-turnover | Inventroy Turn-over |
| [**inventoryLtdPost**](InventoryManagementApi.md#inventoryLtdPost) | **POST** /inventory/ltd | Calculate lead time demand |
| [**inventoryMoqPost**](InventoryManagementApi.md#inventoryMoqPost) | **POST** /inventory/moq | Calculate minimum order quantity |
| [**inventoryOptimalServiceLevelPost**](InventoryManagementApi.md#inventoryOptimalServiceLevelPost) | **POST** /inventory/optimal-service-level | Calculate optimal service level |
| [**inventoryReorderPointPost**](InventoryManagementApi.md#inventoryReorderPointPost) | **POST** /inventory/reorder-point | Re-order Point |
| [**inventorySafetyStockPost**](InventoryManagementApi.md#inventorySafetyStockPost) | **POST** /inventory/safety-stock | Safety Stock |
| [**inventoryServiceLevelPost**](InventoryManagementApi.md#inventoryServiceLevelPost) | **POST** /inventory/service-level | Calculate service level |
| [**inventoryTurnsPost**](InventoryManagementApi.md#inventoryTurnsPost) | **POST** /inventory/turns | Calculate inventory turns |


<a id="inventoryAmazonIpiPost"></a>
# **inventoryAmazonIpiPost**
> inventoryAmazonIpiPost(token)

Calculate Amazon Inventory Performance Index (IPI)

Calculate Amazon Inventory Performance Index (IPI)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryAmazonIpiPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryAmazonIpiPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryCaryyingCostPost"></a>
# **inventoryCaryyingCostPost**
> inventoryCaryyingCostPost(token)

Carrying Cost

Carrying Cost

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryCaryyingCostPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryCaryyingCostPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryEoqPost"></a>
# **inventoryEoqPost**
> inventoryEoqPost(token)

Calculate economic order quantity

Calculate economic order quantity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryEoqPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryEoqPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryFillRatePost"></a>
# **inventoryFillRatePost**
> inventoryFillRatePost(token)

Calculate fill rate

Calculate fill rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryFillRatePost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryFillRatePost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryFinancialImapctForecastAccuracyPost"></a>
# **inventoryFinancialImapctForecastAccuracyPost**
> inventoryFinancialImapctForecastAccuracyPost(token)

Calculate financial impact of forecast accuracy

Calculate financial impact of forecast accuracy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryFinancialImapctForecastAccuracyPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryFinancialImapctForecastAccuracyPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryInventoryTurnoverPost"></a>
# **inventoryInventoryTurnoverPost**
> inventoryInventoryTurnoverPost(token)

Inventroy Turn-over

Inventroy Turn-over

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryInventoryTurnoverPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryInventoryTurnoverPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryLtdPost"></a>
# **inventoryLtdPost**
> inventoryLtdPost(token)

Calculate lead time demand

Calculate lead time demand

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryLtdPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryLtdPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryMoqPost"></a>
# **inventoryMoqPost**
> inventoryMoqPost(token)

Calculate minimum order quantity

Calculate minimum order quantity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryMoqPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryMoqPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryOptimalServiceLevelPost"></a>
# **inventoryOptimalServiceLevelPost**
> inventoryOptimalServiceLevelPost(token)

Calculate optimal service level

Calculate optimal service level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryOptimalServiceLevelPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryOptimalServiceLevelPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryReorderPointPost"></a>
# **inventoryReorderPointPost**
> inventoryReorderPointPost(token)

Re-order Point

Re-order Point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryReorderPointPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryReorderPointPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventorySafetyStockPost"></a>
# **inventorySafetyStockPost**
> inventorySafetyStockPost(token)

Safety Stock

Safety Stock

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventorySafetyStockPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventorySafetyStockPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryServiceLevelPost"></a>
# **inventoryServiceLevelPost**
> inventoryServiceLevelPost(token)

Calculate service level

Calculate service level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryServiceLevelPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryServiceLevelPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

<a id="inventoryTurnsPost"></a>
# **inventoryTurnsPost**
> inventoryTurnsPost(token)

Calculate inventory turns

Calculate inventory turns

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InventoryManagementApi apiInstance = new InventoryManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.inventoryTurnsPost(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryManagementApi#inventoryTurnsPost");
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
| **token** | **String**| User Authentication Token | [optional] |

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
| **200** | Success |  -  |

