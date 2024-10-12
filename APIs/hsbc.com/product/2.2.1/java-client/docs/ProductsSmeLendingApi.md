# ProductsSmeLendingApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**openBankingV22UnsecuredSmeLoansGet**](ProductsSmeLendingApi.md#openBankingV22UnsecuredSmeLoansGet) | **GET** /open-banking/v2.2/unsecured-sme-loans |  |
| [**xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet**](ProductsSmeLendingApi.md#xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet) | **GET** /x-open-banking/v2.2/unsecured-sme-loans/segment/{segment} |  |


<a id="openBankingV22UnsecuredSmeLoansGet"></a>
# **openBankingV22UnsecuredSmeLoansGet**
> SMELendingDefinitionMeta openBankingV22UnsecuredSmeLoansGet()



This API will return data about all SME lending products and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSmeLendingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    ProductsSmeLendingApi apiInstance = new ProductsSmeLendingApi(defaultClient);
    try {
      SMELendingDefinitionMeta result = apiInstance.openBankingV22UnsecuredSmeLoansGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSmeLendingApi#openBankingV22UnsecuredSmeLoansGet");
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

[**SMELendingDefinitionMeta**](SMELendingDefinitionMeta.md)

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

<a id="xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet"></a>
# **xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet**
> SMELendingDefinitionMeta xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet(segment)



This extended API will return data about all SME lending products for the specified segment. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSmeLendingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    ProductsSmeLendingApi apiInstance = new ProductsSmeLendingApi(defaultClient);
    String segment = "segment_example"; // String | Segment name from this list&#58; &quot;AgricultureSector&quot;, &quot;Business&quot;, &quot;FixedGroup&quot;, &quot;FlexibleBusinessLoan&quot;, &quot;GovernmentScheme&quot;, &quot;Other&quot;, &quot;SectorSpecific&quot;.
    try {
      SMELendingDefinitionMeta result = apiInstance.xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet(segment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSmeLendingApi#xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet");
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
| **segment** | **String**| Segment name from this list&amp;#58; &amp;quot;AgricultureSector&amp;quot;, &amp;quot;Business&amp;quot;, &amp;quot;FixedGroup&amp;quot;, &amp;quot;FlexibleBusinessLoan&amp;quot;, &amp;quot;GovernmentScheme&amp;quot;, &amp;quot;Other&amp;quot;, &amp;quot;SectorSpecific&amp;quot;. | |

### Return type

[**SMELendingDefinitionMeta**](SMELendingDefinitionMeta.md)

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

