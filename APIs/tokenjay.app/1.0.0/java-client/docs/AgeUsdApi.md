# AgeUsdApi

All URIs are relative to *https://api.tokenjay.app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calcSigmaRsvExchange**](AgeUsdApi.md#calcSigmaRsvExchange) | **GET** /sigrsv/exchange/{amount}/info | Calculates SigRSV exchange |
| [**calcSigmaUsdExchange**](AgeUsdApi.md#calcSigmaUsdExchange) | **GET** /sigusd/exchange/{amount}/info | Calculates SigUSD exchange |
| [**doSigmaRsvExchange**](AgeUsdApi.md#doSigmaRsvExchange) | **GET** /sigrsv/exchange/ | Builds ErgoPayRequest for SigRSV exchange |
| [**doSigmaUsdExchange**](AgeUsdApi.md#doSigmaUsdExchange) | **GET** /sigusd/exchange/ | Builds ErgoPayRequest for SigUSD exchange |
| [**getAgeUsdInfo**](AgeUsdApi.md#getAgeUsdInfo) | **GET** /ageusd/info | Returns state of AgeUSD at this moment |
| [**getSigmaRsvPrice**](AgeUsdApi.md#getSigmaRsvPrice) | **GET** /sigrsv/price | Lists price and available volume for SigmaRSV |
| [**getSigmaUsdPrice**](AgeUsdApi.md#getSigmaUsdPrice) | **GET** /sigusd/price | Lists price and available volume for SigmaUSD |


<a id="calcSigmaRsvExchange"></a>
# **calcSigmaRsvExchange**
> AgeUsdExchangeInfo calcSigmaRsvExchange(amount)

Calculates SigRSV exchange

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgeUsdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    AgeUsdApi apiInstance = new AgeUsdApi(defaultClient);
    Long amount = 56L; // Long | 
    try {
      AgeUsdExchangeInfo result = apiInstance.calcSigmaRsvExchange(amount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgeUsdApi#calcSigmaRsvExchange");
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
| **amount** | **Long**|  | |

### Return type

[**AgeUsdExchangeInfo**](AgeUsdExchangeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="calcSigmaUsdExchange"></a>
# **calcSigmaUsdExchange**
> AgeUsdExchangeInfo calcSigmaUsdExchange(amount)

Calculates SigUSD exchange

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgeUsdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    AgeUsdApi apiInstance = new AgeUsdApi(defaultClient);
    Long amount = 56L; // Long | 
    try {
      AgeUsdExchangeInfo result = apiInstance.calcSigmaUsdExchange(amount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgeUsdApi#calcSigmaUsdExchange");
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
| **amount** | **Long**|  | |

### Return type

[**AgeUsdExchangeInfo**](AgeUsdExchangeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="doSigmaRsvExchange"></a>
# **doSigmaRsvExchange**
> ErgoPayResponse doSigmaRsvExchange(amount, address, checkRate, executionFee)

Builds ErgoPayRequest for SigRSV exchange

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgeUsdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    AgeUsdApi apiInstance = new AgeUsdApi(defaultClient);
    Long amount = 56L; // Long | 
    String address = "address_example"; // String | 
    Long checkRate = 0L; // Long | 
    Long executionFee = 0L; // Long | 
    try {
      ErgoPayResponse result = apiInstance.doSigmaRsvExchange(amount, address, checkRate, executionFee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgeUsdApi#doSigmaRsvExchange");
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
| **amount** | **Long**|  | |
| **address** | **String**|  | |
| **checkRate** | **Long**|  | [optional] [default to 0] |
| **executionFee** | **Long**|  | [optional] [default to 0] |

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="doSigmaUsdExchange"></a>
# **doSigmaUsdExchange**
> ErgoPayResponse doSigmaUsdExchange(amount, address, checkRate, executionFee)

Builds ErgoPayRequest for SigUSD exchange

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgeUsdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    AgeUsdApi apiInstance = new AgeUsdApi(defaultClient);
    Long amount = 56L; // Long | 
    String address = "address_example"; // String | 
    Long checkRate = 0L; // Long | 
    Long executionFee = 0L; // Long | 
    try {
      ErgoPayResponse result = apiInstance.doSigmaUsdExchange(amount, address, checkRate, executionFee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgeUsdApi#doSigmaUsdExchange");
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
| **amount** | **Long**|  | |
| **address** | **String**|  | |
| **checkRate** | **Long**|  | [optional] [default to 0] |
| **executionFee** | **Long**|  | [optional] [default to 0] |

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="getAgeUsdInfo"></a>
# **getAgeUsdInfo**
> AgeUsdInfo getAgeUsdInfo()

Returns state of AgeUSD at this moment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgeUsdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    AgeUsdApi apiInstance = new AgeUsdApi(defaultClient);
    try {
      AgeUsdInfo result = apiInstance.getAgeUsdInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgeUsdApi#getAgeUsdInfo");
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

[**AgeUsdInfo**](AgeUsdInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="getSigmaRsvPrice"></a>
# **getSigmaRsvPrice**
> TokenPrice getSigmaRsvPrice()

Lists price and available volume for SigmaRSV

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgeUsdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    AgeUsdApi apiInstance = new AgeUsdApi(defaultClient);
    try {
      TokenPrice result = apiInstance.getSigmaRsvPrice();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgeUsdApi#getSigmaRsvPrice");
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

[**TokenPrice**](TokenPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="getSigmaUsdPrice"></a>
# **getSigmaUsdPrice**
> TokenPrice getSigmaUsdPrice()

Lists price and available volume for SigmaUSD

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgeUsdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    AgeUsdApi apiInstance = new AgeUsdApi(defaultClient);
    try {
      TokenPrice result = apiInstance.getSigmaUsdPrice();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgeUsdApi#getSigmaUsdPrice");
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

[**TokenPrice**](TokenPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

