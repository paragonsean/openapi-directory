# TaxesApi

All URIs are relative to *https://products.izettle.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTaxRates**](TaxesApi.md#createTaxRates) | **POST** /v1/taxes | Create new tax rates |
| [**deleteTaxRate**](TaxesApi.md#deleteTaxRate) | **DELETE** /v1/taxes/{taxRateUuid} | Delete a single tax rate |
| [**getProductCountForAllTaxes**](TaxesApi.md#getProductCountForAllTaxes) | **GET** /v1/taxes/count | Get all tax rates and a count of products associated with each |
| [**getTaxRate**](TaxesApi.md#getTaxRate) | **GET** /v1/taxes/{taxRateUuid} | Get a single tax rate |
| [**getTaxRates**](TaxesApi.md#getTaxRates) | **GET** /v1/taxes | Get all available tax rates |
| [**getTaxSettings**](TaxesApi.md#getTaxSettings) | **GET** /v1/taxes/settings | Get the organization tax settings  |
| [**setTaxationMode**](TaxesApi.md#setTaxationMode) | **PUT** /v1/taxes/settings | Update the organization tax settings |
| [**updateTaxRate**](TaxesApi.md#updateTaxRate) | **PUT** /v1/taxes/{taxRateUuid} | Update a single tax rate |


<a id="createTaxRates"></a>
# **createTaxRates**
> TaxRatesResponse createTaxRates(taxRatesCreateRequest)

Create new tax rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    TaxesApi apiInstance = new TaxesApi(defaultClient);
    TaxRatesCreateRequest taxRatesCreateRequest = new TaxRatesCreateRequest(); // TaxRatesCreateRequest | 
    try {
      TaxRatesResponse result = apiInstance.createTaxRates(taxRatesCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxesApi#createTaxRates");
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
| **taxRatesCreateRequest** | [**TaxRatesCreateRequest**](TaxRatesCreateRequest.md)|  | |

### Return type

[**TaxRatesResponse**](TaxRatesResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tax rates created |  -  |
| **400** | Invalid request body |  -  |
| **403** | Not a sales tax user |  -  |

<a id="deleteTaxRate"></a>
# **deleteTaxRate**
> deleteTaxRate(taxRateUuid)

Delete a single tax rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    TaxesApi apiInstance = new TaxesApi(defaultClient);
    UUID taxRateUuid = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.deleteTaxRate(taxRateUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxesApi#deleteTaxRate");
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
| **taxRateUuid** | **UUID**|  | |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Tax rate deleted |  -  |
| **403** | Not a sales tax user |  -  |
| **404** | Tax rate not found |  -  |

<a id="getProductCountForAllTaxes"></a>
# **getProductCountForAllTaxes**
> TaxRateProductCountResponse getProductCountForAllTaxes()

Get all tax rates and a count of products associated with each

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    TaxesApi apiInstance = new TaxesApi(defaultClient);
    try {
      TaxRateProductCountResponse result = apiInstance.getProductCountForAllTaxes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxesApi#getProductCountForAllTaxes");
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

[**TaxRateProductCountResponse**](TaxRateProductCountResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of products for each tax rate |  -  |
| **403** | Not a sales tax user |  -  |

<a id="getTaxRate"></a>
# **getTaxRate**
> TaxRate getTaxRate(taxRateUuid)

Get a single tax rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    TaxesApi apiInstance = new TaxesApi(defaultClient);
    UUID taxRateUuid = UUID.randomUUID(); // UUID | 
    try {
      TaxRate result = apiInstance.getTaxRate(taxRateUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxesApi#getTaxRate");
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
| **taxRateUuid** | **UUID**|  | |

### Return type

[**TaxRate**](TaxRate.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single tax rate |  -  |
| **403** | Not a sales tax user |  -  |
| **404** | Tax rate not found |  -  |

<a id="getTaxRates"></a>
# **getTaxRates**
> List&lt;TaxRatesResponse&gt; getTaxRates()

Get all available tax rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    TaxesApi apiInstance = new TaxesApi(defaultClient);
    try {
      List<TaxRatesResponse> result = apiInstance.getTaxRates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxesApi#getTaxRates");
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

[**List&lt;TaxRatesResponse&gt;**](TaxRatesResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of tax rates |  -  |
| **403** | Not a sales tax user |  -  |

<a id="getTaxSettings"></a>
# **getTaxSettings**
> TaxSettingsResponse getTaxSettings()

Get the organization tax settings 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    TaxesApi apiInstance = new TaxesApi(defaultClient);
    try {
      TaxSettingsResponse result = apiInstance.getTaxSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxesApi#getTaxSettings");
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

[**TaxSettingsResponse**](TaxSettingsResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tax settings |  -  |
| **403** | Not a sales tax user |  -  |

<a id="setTaxationMode"></a>
# **setTaxationMode**
> TaxSettingsResponse setTaxationMode(taxSettingsUpdateRequest)

Update the organization tax settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    TaxesApi apiInstance = new TaxesApi(defaultClient);
    TaxSettingsUpdateRequest taxSettingsUpdateRequest = new TaxSettingsUpdateRequest(); // TaxSettingsUpdateRequest | 
    try {
      TaxSettingsResponse result = apiInstance.setTaxationMode(taxSettingsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxesApi#setTaxationMode");
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
| **taxSettingsUpdateRequest** | [**TaxSettingsUpdateRequest**](TaxSettingsUpdateRequest.md)|  | |

### Return type

[**TaxSettingsResponse**](TaxSettingsResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated tax settings |  -  |
| **400** | Invalid request body |  -  |
| **403** | Not a sales tax user |  -  |

<a id="updateTaxRate"></a>
# **updateTaxRate**
> TaxRate updateTaxRate(taxRateUuid, taxRateUpdateRequest)

Update a single tax rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    TaxesApi apiInstance = new TaxesApi(defaultClient);
    UUID taxRateUuid = UUID.randomUUID(); // UUID | 
    TaxRateUpdateRequest taxRateUpdateRequest = new TaxRateUpdateRequest(); // TaxRateUpdateRequest | 
    try {
      TaxRate result = apiInstance.updateTaxRate(taxRateUuid, taxRateUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxesApi#updateTaxRate");
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
| **taxRateUuid** | **UUID**|  | |
| **taxRateUpdateRequest** | [**TaxRateUpdateRequest**](TaxRateUpdateRequest.md)|  | |

### Return type

[**TaxRate**](TaxRate.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated tax rate |  -  |
| **400** | Invalid request body |  -  |
| **403** | Not a sales tax user |  -  |
| **404** | Tax rate not found |  -  |

