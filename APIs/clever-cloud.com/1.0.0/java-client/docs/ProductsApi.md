# ProductsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProductsAddonProvidersProviderId_0**](ProductsApi.md#getProductsAddonProvidersProviderId_0) | **GET** /products/addonproviders/{provider_id} |  |
| [**getProductsAddonProviders_0**](ProductsApi.md#getProductsAddonProviders_0) | **GET** /products/addonproviders |  |
| [**getProductsCountries_0**](ProductsApi.md#getProductsCountries_0) | **GET** /products/countries |  |
| [**getProductsCountrycodes_0**](ProductsApi.md#getProductsCountrycodes_0) | **GET** /products/countrycodes |  |
| [**getProductsInstancesTypeVersion_0**](ProductsApi.md#getProductsInstancesTypeVersion_0) | **GET** /products/instances/{type}-{version} |  |
| [**getProductsInstances_0**](ProductsApi.md#getProductsInstances_0) | **GET** /products/instances |  |
| [**getProductsPackages_0**](ProductsApi.md#getProductsPackages_0) | **GET** /products/packages |  |
| [**getProductsPrices_0**](ProductsApi.md#getProductsPrices_0) | **GET** /products/prices |  |
| [**getProductsZones_0**](ProductsApi.md#getProductsZones_0) | **GET** /products/zones |  |
| [**productsAddonprovidersProviderIdVersionsGet_0**](ProductsApi.md#productsAddonprovidersProviderIdVersionsGet_0) | **GET** /products/addonproviders/{provider_id}/versions |  |
| [**productsMfaKindsGet_0**](ProductsApi.md#productsMfaKindsGet_0) | **GET** /products/mfa_kinds |  |


<a id="getProductsAddonProvidersProviderId_0"></a>
# **getProductsAddonProvidersProviderId_0**
> Provider getProductsAddonProvidersProviderId_0(providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String providerId = "providerId_example"; // String | 
    try {
      Provider result = apiInstance.getProductsAddonProvidersProviderId_0(providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsAddonProvidersProviderId_0");
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
| **providerId** | **String**|  | |

### Return type

[**Provider**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonProvider |  -  |

<a id="getProductsAddonProviders_0"></a>
# **getProductsAddonProviders_0**
> List&lt;Provider&gt; getProductsAddonProviders_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      List<Provider> result = apiInstance.getProductsAddonProviders_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsAddonProviders_0");
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

[**List&lt;Provider&gt;**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonProviders |  -  |

<a id="getProductsCountries_0"></a>
# **getProductsCountries_0**
> Country getProductsCountries_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      Country result = apiInstance.getProductsCountries_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsCountries_0");
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

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getCountries |  -  |

<a id="getProductsCountrycodes_0"></a>
# **getProductsCountrycodes_0**
> Country getProductsCountrycodes_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      Country result = apiInstance.getProductsCountrycodes_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsCountrycodes_0");
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

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getCountryCodes |  -  |

<a id="getProductsInstancesTypeVersion_0"></a>
# **getProductsInstancesTypeVersion_0**
> Instance getProductsInstancesTypeVersion_0(type, version, _for, app)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String type = "type_example"; // String | 
    String version = "version_example"; // String | 
    String _for = "_for_example"; // String | 
    String app = "app_example"; // String | 
    try {
      Instance result = apiInstance.getProductsInstancesTypeVersion_0(type, version, _for, app);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsInstancesTypeVersion_0");
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
| **type** | **String**|  | |
| **version** | **String**|  | |
| **_for** | **String**|  | [optional] |
| **app** | **String**|  | [optional] |

### Return type

[**Instance**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAvailableInstance |  -  |

<a id="getProductsInstances_0"></a>
# **getProductsInstances_0**
> List&lt;Instance&gt; getProductsInstances_0(_for)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String _for = "_for_example"; // String | 
    try {
      List<Instance> result = apiInstance.getProductsInstances_0(_for);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsInstances_0");
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
| **_for** | **String**|  | [optional] |

### Return type

[**List&lt;Instance&gt;**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAvailableInstances |  -  |

<a id="getProductsPackages_0"></a>
# **getProductsPackages_0**
> getProductsPackages_0(coupon, orgaId, currency)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String coupon = "coupon_example"; // String | 
    String orgaId = "orgaId_example"; // String | 
    String currency = "currency_example"; // String | 
    try {
      apiInstance.getProductsPackages_0(coupon, orgaId, currency);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsPackages_0");
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
| **coupon** | **String**|  | [optional] |
| **orgaId** | **String**|  | [optional] |
| **currency** | **String**|  | [optional] |

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
| **200** | getAvailablePackages |  -  |

<a id="getProductsPrices_0"></a>
# **getProductsPrices_0**
> getProductsPrices_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      apiInstance.getProductsPrices_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsPrices_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getExchangeRates |  -  |

<a id="getProductsZones_0"></a>
# **getProductsZones_0**
> List&lt;Zone&gt; getProductsZones_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      List<Zone> result = apiInstance.getProductsZones_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsZones_0");
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

[**List&lt;Zone&gt;**](Zone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getZones |  -  |

<a id="productsAddonprovidersProviderIdVersionsGet_0"></a>
# **productsAddonprovidersProviderIdVersionsGet_0**
> productsAddonprovidersProviderIdVersionsGet_0(providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String providerId = "providerId_example"; // String | 
    try {
      apiInstance.productsAddonprovidersProviderIdVersionsGet_0(providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsAddonprovidersProviderIdVersionsGet_0");
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
| **providerId** | **String**|  | |

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
| **200** | Status 200 |  -  |

<a id="productsMfaKindsGet_0"></a>
# **productsMfaKindsGet_0**
> productsMfaKindsGet_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      apiInstance.productsMfaKindsGet_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsMfaKindsGet_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

