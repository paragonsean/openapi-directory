# OmInvoiceApiSettingsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrderInvoiceDesignSettings**](OmInvoiceApiSettingsApi.md#getOrderInvoiceDesignSettings) | **GET** /v2/user/marketplaces/orders/invoices/settings/design | Get Order Invoice design settings |
| [**getOrderInvoiceDesignSettingsPreview**](OmInvoiceApiSettingsApi.md#getOrderInvoiceDesignSettingsPreview) | **POST** /v2/user/marketplaces/orders/invoices/settings/design/preview | View a preview an Order Invoice using custom design settings |
| [**getOrderInvoiceGeneralSettings**](OmInvoiceApiSettingsApi.md#getOrderInvoiceGeneralSettings) | **GET** /v2/user/marketplaces/orders/invoices/settings/general | Get Order Invoice general settings |
| [**saveOrderInvoiceDesignSettings**](OmInvoiceApiSettingsApi.md#saveOrderInvoiceDesignSettings) | **PUT** /v2/user/marketplaces/orders/invoices/settings/design | Save Order Invoice design settings |
| [**saveOrderInvoiceGeneralSettings**](OmInvoiceApiSettingsApi.md#saveOrderInvoiceGeneralSettings) | **PUT** /v2/user/marketplaces/orders/invoices/settings/general | Save Order Invoice general settings |


<a id="getOrderInvoiceDesignSettings"></a>
# **getOrderInvoiceDesignSettings**
> OrderInvoiceDesignSettings getOrderInvoiceDesignSettings()

Get Order Invoice design settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OmInvoiceApiSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    OmInvoiceApiSettingsApi apiInstance = new OmInvoiceApiSettingsApi(defaultClient);
    try {
      OrderInvoiceDesignSettings result = apiInstance.getOrderInvoiceDesignSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OmInvoiceApiSettingsApi#getOrderInvoiceDesignSettings");
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

[**OrderInvoiceDesignSettings**](OrderInvoiceDesignSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Design successfully retrieved |  -  |
| **403** | The ownerId is not found or not authorized |  -  |
| **404** | The order invoice design is not found  |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderInvoiceDesignSettingsPreview"></a>
# **getOrderInvoiceDesignSettingsPreview**
> GetOrderInvoiceDesignPreviewResponse getOrderInvoiceDesignSettingsPreview(acceptEncoding, orderInvoiceDesignSettings)

View a preview an Order Invoice using custom design settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OmInvoiceApiSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    OmInvoiceApiSettingsApi apiInstance = new OmInvoiceApiSettingsApi(defaultClient);
    List<String> acceptEncoding = Arrays.asList(); // List<String> | Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
    OrderInvoiceDesignSettings orderInvoiceDesignSettings = new OrderInvoiceDesignSettings(); // OrderInvoiceDesignSettings | 
    try {
      GetOrderInvoiceDesignPreviewResponse result = apiInstance.getOrderInvoiceDesignSettingsPreview(acceptEncoding, orderInvoiceDesignSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OmInvoiceApiSettingsApi#getOrderInvoiceDesignSettingsPreview");
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
| **acceptEncoding** | [**List&lt;String&gt;**](String.md)| Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size | |
| **orderInvoiceDesignSettings** | [**OrderInvoiceDesignSettings**](OrderInvoiceDesignSettings.md)|  | |

### Return type

[**GetOrderInvoiceDesignPreviewResponse**](GetOrderInvoiceDesignPreviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Design Preview successfully retrieved |  -  |
| **403** | The ownerId is not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderInvoiceGeneralSettings"></a>
# **getOrderInvoiceGeneralSettings**
> GetOrderInvoiceGeneralSettingsResponse getOrderInvoiceGeneralSettings()

Get Order Invoice general settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OmInvoiceApiSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    OmInvoiceApiSettingsApi apiInstance = new OmInvoiceApiSettingsApi(defaultClient);
    try {
      GetOrderInvoiceGeneralSettingsResponse result = apiInstance.getOrderInvoiceGeneralSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OmInvoiceApiSettingsApi#getOrderInvoiceGeneralSettings");
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

[**GetOrderInvoiceGeneralSettingsResponse**](GetOrderInvoiceGeneralSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings successfully retrieved |  -  |
| **403** | The ownerId is not found or not authorized |  -  |
| **404** | The order invoice general settings are not found  |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="saveOrderInvoiceDesignSettings"></a>
# **saveOrderInvoiceDesignSettings**
> saveOrderInvoiceDesignSettings(orderInvoiceDesignSettings)

Save Order Invoice design settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OmInvoiceApiSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    OmInvoiceApiSettingsApi apiInstance = new OmInvoiceApiSettingsApi(defaultClient);
    OrderInvoiceDesignSettings orderInvoiceDesignSettings = new OrderInvoiceDesignSettings(); // OrderInvoiceDesignSettings | 
    try {
      apiInstance.saveOrderInvoiceDesignSettings(orderInvoiceDesignSettings);
    } catch (ApiException e) {
      System.err.println("Exception when calling OmInvoiceApiSettingsApi#saveOrderInvoiceDesignSettings");
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
| **orderInvoiceDesignSettings** | [**OrderInvoiceDesignSettings**](OrderInvoiceDesignSettings.md)|  | |

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
| **204** | Design successfully saved |  -  |
| **400** | The design did not pass the validation  |  -  |
| **403** | The ownerId is not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="saveOrderInvoiceGeneralSettings"></a>
# **saveOrderInvoiceGeneralSettings**
> saveOrderInvoiceGeneralSettings(orderInvoiceGeneralSettings)

Save Order Invoice general settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OmInvoiceApiSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    OmInvoiceApiSettingsApi apiInstance = new OmInvoiceApiSettingsApi(defaultClient);
    OrderInvoiceGeneralSettings orderInvoiceGeneralSettings = new OrderInvoiceGeneralSettings(); // OrderInvoiceGeneralSettings | 
    try {
      apiInstance.saveOrderInvoiceGeneralSettings(orderInvoiceGeneralSettings);
    } catch (ApiException e) {
      System.err.println("Exception when calling OmInvoiceApiSettingsApi#saveOrderInvoiceGeneralSettings");
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
| **orderInvoiceGeneralSettings** | [**OrderInvoiceGeneralSettings**](OrderInvoiceGeneralSettings.md)|  | |

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
| **204** | General Settings successfully saved |  -  |
| **400** | The settingsgeneral did not pass the validation  |  -  |
| **403** | The ownerId is not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

