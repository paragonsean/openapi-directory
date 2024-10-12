# CompanyCreditsApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCreditsSearchRead**](CompanyCreditsApi.md#companyCreditsSearchRead) | **GET** /api/v1/company-credits/search/{movie_title} | Return company credits search result |
| [**companyCreditsSearchallRead**](CompanyCreditsApi.md#companyCreditsSearchallRead) | **GET** /api/v1/company-credits/searchall/{param} | Return company credits search result |


<a id="companyCreditsSearchRead"></a>
# **companyCreditsSearchRead**
> companyCreditsSearchRead(movieTitle)

Return company credits search result

Return company credits search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search company credits for the movie * You can use both Amharic or English charset/font to search  For more details on how company credits are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCreditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    CompanyCreditsApi apiInstance = new CompanyCreditsApi(defaultClient);
    String movieTitle = "movieTitle_example"; // String | 
    try {
      apiInstance.companyCreditsSearchRead(movieTitle);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCreditsApi#companyCreditsSearchRead");
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
| **movieTitle** | **String**|  | |

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

<a id="companyCreditsSearchallRead"></a>
# **companyCreditsSearchallRead**
> companyCreditsSearchallRead(param)

Return company credits search result

Return company credits search result  ### Response Class (Status 200) __{param}__ argument can be * company name * movie title or * company credit description (such as production, cinematography, etc)  For more details on how company credits are listed [see here][ref]. [ref]: https://etmdb.com/en/company-list/company_name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCreditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    CompanyCreditsApi apiInstance = new CompanyCreditsApi(defaultClient);
    String param = "param_example"; // String | 
    try {
      apiInstance.companyCreditsSearchallRead(param);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCreditsApi#companyCreditsSearchallRead");
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
| **param** | **String**|  | |

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

