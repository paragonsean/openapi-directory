# PortfoliosEssentialsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPortfolio**](PortfoliosEssentialsApi.md#getPortfolio) | **GET** /users/{user_id}/portfolios/{portfolio_id} | Get a specific portfolio |
| [**getPortfolioAlt1**](PortfoliosEssentialsApi.md#getPortfolioAlt1) | **GET** /me/portfolios/{portfolio_id} | Get a specific portfolio |
| [**getPortfolios**](PortfoliosEssentialsApi.md#getPortfolios) | **GET** /users/{user_id}/portfolios | Get all the portfolios that belong to a user |
| [**getPortfoliosAlt1**](PortfoliosEssentialsApi.md#getPortfoliosAlt1) | **GET** /me/portfolios | Get all the portfolios that belong to a user |


<a id="getPortfolio"></a>
# **getPortfolio**
> Portfolio getPortfolio(portfolioId, userId)

Get a specific portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PortfoliosEssentialsApi apiInstance = new PortfoliosEssentialsApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Portfolio result = apiInstance.getPortfolio(portfolioId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosEssentialsApi#getPortfolio");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.portfolio+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The portfolio was returned. |  -  |

<a id="getPortfolioAlt1"></a>
# **getPortfolioAlt1**
> Portfolio getPortfolioAlt1(portfolioId)

Get a specific portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PortfoliosEssentialsApi apiInstance = new PortfoliosEssentialsApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    try {
      Portfolio result = apiInstance.getPortfolioAlt1(portfolioId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosEssentialsApi#getPortfolioAlt1");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.portfolio+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The portfolio was returned. |  -  |

<a id="getPortfolios"></a>
# **getPortfolios**
> List&lt;Portfolio&gt; getPortfolios(userId, direction, page, perPage, query, sort)

Get all the portfolios that belong to a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PortfoliosEssentialsApi apiInstance = new PortfoliosEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Portfolio> result = apiInstance.getPortfolios(userId, direction, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosEssentialsApi#getPortfolios");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date] |

### Return type

[**List&lt;Portfolio&gt;**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.portfolio+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The portfolios were returned. |  -  |

<a id="getPortfoliosAlt1"></a>
# **getPortfoliosAlt1**
> List&lt;Portfolio&gt; getPortfoliosAlt1(direction, page, perPage, query, sort)

Get all the portfolios that belong to a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PortfoliosEssentialsApi apiInstance = new PortfoliosEssentialsApi(defaultClient);
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Portfolio> result = apiInstance.getPortfoliosAlt1(direction, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosEssentialsApi#getPortfoliosAlt1");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date] |

### Return type

[**List&lt;Portfolio&gt;**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.portfolio+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The portfolios were returned. |  -  |

