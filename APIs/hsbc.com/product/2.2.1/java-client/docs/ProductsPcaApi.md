# ProductsPcaApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**openBankingV22PersonalCurrentAccountsGet**](ProductsPcaApi.md#openBankingV22PersonalCurrentAccountsGet) | **GET** /open-banking/v2.2/personal-current-accounts |  |
| [**xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet**](ProductsPcaApi.md#xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet) | **GET** /x-open-banking/v2.2/personal-current-accounts/segment/{segment} |  |


<a id="openBankingV22PersonalCurrentAccountsGet"></a>
# **openBankingV22PersonalCurrentAccountsGet**
> PCADefinitionMeta openBankingV22PersonalCurrentAccountsGet()



This API will return data about all PCA products and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsPcaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    ProductsPcaApi apiInstance = new ProductsPcaApi(defaultClient);
    try {
      PCADefinitionMeta result = apiInstance.openBankingV22PersonalCurrentAccountsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsPcaApi#openBankingV22PersonalCurrentAccountsGet");
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

[**PCADefinitionMeta**](PCADefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/prs.openbanking.opendata.v2.2+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **408** | Bad request |  -  |
| **429** | Bad request |  -  |
| **500** | System error |  -  |
| **503** | System error |  -  |

<a id="xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet"></a>
# **xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet**
> PCADefinitionMeta xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet(segment)



This extended API will return data about all PCA products for the specified segment. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsPcaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    ProductsPcaApi apiInstance = new ProductsPcaApi(defaultClient);
    String segment = "segment_example"; // String | Segment name from this list&#58; &quot;Basic&quot;, &quot;General&quot;, &quot;Graduate&quot;, &quot;Packaged&quot;, &quot;Premium&quot;, &quot;Reward&quot;, &quot;Student&quot;, &quot;YoungAdult&quot;, &quot;Youth&quot;.
    try {
      PCADefinitionMeta result = apiInstance.xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet(segment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsPcaApi#xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet");
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
| **segment** | **String**| Segment name from this list&amp;#58; &amp;quot;Basic&amp;quot;, &amp;quot;General&amp;quot;, &amp;quot;Graduate&amp;quot;, &amp;quot;Packaged&amp;quot;, &amp;quot;Premium&amp;quot;, &amp;quot;Reward&amp;quot;, &amp;quot;Student&amp;quot;, &amp;quot;YoungAdult&amp;quot;, &amp;quot;Youth&amp;quot;. | |

### Return type

[**PCADefinitionMeta**](PCADefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/prs.openbanking.opendata.v2.2+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **408** | Bad request |  -  |
| **429** | Bad request |  -  |
| **500** | System error |  -  |
| **503** | System error |  -  |

