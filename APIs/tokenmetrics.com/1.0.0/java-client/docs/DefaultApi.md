# DefaultApi

All URIs are relative to *https://api.tokenmetrics.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**correlation**](DefaultApi.md#correlation) | **GET** /v1/correlation | Correlation |
| [**indices**](DefaultApi.md#indices) | **GET** /v1/indices | Indices |
| [**investorGrades**](DefaultApi.md#investorGrades) | **GET** /v1/investor-grades | Investor Grades |
| [**marketIndicator**](DefaultApi.md#marketIndicator) | **GET** /v1/market-indicator | Market Indicator |
| [**price**](DefaultApi.md#price) | **GET** /v1/price | Price |
| [**pricePrediction**](DefaultApi.md#pricePrediction) | **GET** /v1/price-prediction | Price Prediction |
| [**quantmetricsTier1**](DefaultApi.md#quantmetricsTier1) | **GET** /v1/quantmetrics-tier-1 | Quantmetrics Tier 1 |
| [**quantmetricsTier2**](DefaultApi.md#quantmetricsTier2) | **GET** /v1/quantmetrics-tier-2 | Quantmetrics Tier 2 |
| [**resistanceSupport**](DefaultApi.md#resistanceSupport) | **GET** /v1/resistance-support | Resistance &amp; Support |
| [**scenarioAnalysis**](DefaultApi.md#scenarioAnalysis) | **GET** /v1/scenario-analysis | Scenario Analysis |
| [**sentiments**](DefaultApi.md#sentiments) | **GET** /v1/sentiments | Sentiments |
| [**tokens**](DefaultApi.md#tokens) | **GET** /v1/tokens | Tokens |
| [**traderGrades**](DefaultApi.md#traderGrades) | **GET** /v1/trader-grades | Trader Grades |
| [**tradingIndicator**](DefaultApi.md#tradingIndicator) | **GET** /v1/trading-indicator | Trading Indicator |


<a id="correlation"></a>
# **correlation**
> correlation(tokens, limit)

Correlation

Correlation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.correlation(tokens, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#correlation");
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
| **tokens** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="indices"></a>
# **indices**
> indices(exchanges, timeHorizon, lowCap, startDate, endDate, limit)

Indices

Indices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exchanges = "binance"; // String | 
    String timeHorizon = "daily"; // String | 
    String lowCap = "true"; // String | 
    String startDate = "2023-01-10"; // String | 
    String endDate = "2023-01-11"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.indices(exchanges, timeHorizon, lowCap, startDate, endDate, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#indices");
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
| **exchanges** | **String**|  | [optional] |
| **timeHorizon** | **String**|  | [optional] |
| **lowCap** | **String**|  | [optional] |
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="investorGrades"></a>
# **investorGrades**
> investorGrades(tokens, startDate, endDate, limit)

Investor Grades

Investor Grades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String startDate = "2023-01-10"; // String | 
    String endDate = "2023-01-11"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.investorGrades(tokens, startDate, endDate, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#investorGrades");
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
| **tokens** | **String**|  | [optional] |
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="marketIndicator"></a>
# **marketIndicator**
> marketIndicator(startDate, endDate, limit)

Market Indicator

Market Indicator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String startDate = "2023-01-10"; // String | 
    String endDate = "2023-01-11"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.marketIndicator(startDate, endDate, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#marketIndicator");
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
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="price"></a>
# **price**
> price(tokens, startDate, endDate, limit, page)

Price

Price

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String startDate = "2023-01-10"; // String | 
    String endDate = "2023-01-11"; // String | 
    String limit = "1000"; // String | 
    String page = "1"; // String | 
    try {
      apiInstance.price(tokens, startDate, endDate, limit, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#price");
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
| **tokens** | **String**|  | [optional] |
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="pricePrediction"></a>
# **pricePrediction**
> pricePrediction(tokens, date, limit)

Price Prediction

Price Prediction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String date = "2023-02-01"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.pricePrediction(tokens, date, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pricePrediction");
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
| **tokens** | **String**|  | [optional] |
| **date** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="quantmetricsTier1"></a>
# **quantmetricsTier1**
> quantmetricsTier1(tokens, date, limit)

Quantmetrics Tier 1

Quantmetrics Tier 1

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String date = "2023-02-01"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.quantmetricsTier1(tokens, date, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#quantmetricsTier1");
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
| **tokens** | **String**|  | [optional] |
| **date** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="quantmetricsTier2"></a>
# **quantmetricsTier2**
> quantmetricsTier2(tokens, date, limit)

Quantmetrics Tier 2

Quantmetrics Tier 2

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String date = "2023-02-01"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.quantmetricsTier2(tokens, date, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#quantmetricsTier2");
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
| **tokens** | **String**|  | [optional] |
| **date** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="resistanceSupport"></a>
# **resistanceSupport**
> resistanceSupport(tokens, startDate, endDate, limit)

Resistance &amp; Support

Resistance &amp; Support

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String startDate = "2023-01-10"; // String | 
    String endDate = "2023-01-11"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.resistanceSupport(tokens, startDate, endDate, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#resistanceSupport");
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
| **tokens** | **String**|  | [optional] |
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="scenarioAnalysis"></a>
# **scenarioAnalysis**
> scenarioAnalysis(tokens, limit)

Scenario Analysis

Scenario Analysis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.scenarioAnalysis(tokens, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#scenarioAnalysis");
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
| **tokens** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="sentiments"></a>
# **sentiments**
> sentiments(tokens, startDate, endDate, limit)

Sentiments

Sentiments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String startDate = "2023-01-10"; // String | 
    String endDate = "2023-01-11"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.sentiments(tokens, startDate, endDate, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sentiments");
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
| **tokens** | **String**|  | [optional] |
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="tokens"></a>
# **tokens**
> tokens(tokenIds, tokenNames, tokenSymbols)

Tokens

Tokens

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokenIds = "3375, 3306"; // String | 
    String tokenNames = "Hivemapper, Sei_Network, Layer_Zero, Lyra Huobi"; // String | 
    String tokenSymbols = "bds, bds, btc"; // String | 
    try {
      apiInstance.tokens(tokenIds, tokenNames, tokenSymbols);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tokens");
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
| **tokenIds** | **String**|  | [optional] |
| **tokenNames** | **String**|  | [optional] |
| **tokenSymbols** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="traderGrades"></a>
# **traderGrades**
> traderGrades(tokens, startDate, endDate, limit)

Trader Grades

Trader Grades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String startDate = "2023-01-10"; // String | 
    String endDate = "2023-01-11"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.traderGrades(tokens, startDate, endDate, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#traderGrades");
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
| **tokens** | **String**|  | [optional] |
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="tradingIndicator"></a>
# **tradingIndicator**
> tradingIndicator(tokens, limit)

Trading Indicator

Trading Indicator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenmetrics.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tokens = "3375, 3306"; // String | 
    String limit = "1000"; // String | 
    try {
      apiInstance.tradingIndicator(tokens, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tradingIndicator");
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
| **tokens** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

