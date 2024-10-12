# ProductsCommercialCreditCardsApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**openBankingV22CommercialCreditCardsGet**](ProductsCommercialCreditCardsApi.md#openBankingV22CommercialCreditCardsGet) | **GET** /open-banking/v2.2/commercial-credit-cards |  |
| [**xOpenBankingV22CommercialCreditCardsSegmentSegmentGet**](ProductsCommercialCreditCardsApi.md#xOpenBankingV22CommercialCreditCardsSegmentSegmentGet) | **GET** /x-open-banking/v2.2/commercial-credit-cards/segment/{segment} |  |


<a id="openBankingV22CommercialCreditCardsGet"></a>
# **openBankingV22CommercialCreditCardsGet**
> CCCDefinitionMeta openBankingV22CommercialCreditCardsGet()



This API will return data about all commercial credit cards products and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsCommercialCreditCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    ProductsCommercialCreditCardsApi apiInstance = new ProductsCommercialCreditCardsApi(defaultClient);
    try {
      CCCDefinitionMeta result = apiInstance.openBankingV22CommercialCreditCardsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsCommercialCreditCardsApi#openBankingV22CommercialCreditCardsGet");
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

[**CCCDefinitionMeta**](CCCDefinitionMeta.md)

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

<a id="xOpenBankingV22CommercialCreditCardsSegmentSegmentGet"></a>
# **xOpenBankingV22CommercialCreditCardsSegmentSegmentGet**
> CCCDefinitionMeta xOpenBankingV22CommercialCreditCardsSegmentSegmentGet(segment)



This extended API will return data about all commercial credit cards products for the specified segment. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsCommercialCreditCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    ProductsCommercialCreditCardsApi apiInstance = new ProductsCommercialCreditCardsApi(defaultClient);
    String segment = "segment_example"; // String | Segment name from this list&#58; &quot;General&quot;.
    try {
      CCCDefinitionMeta result = apiInstance.xOpenBankingV22CommercialCreditCardsSegmentSegmentGet(segment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsCommercialCreditCardsApi#xOpenBankingV22CommercialCreditCardsSegmentSegmentGet");
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
| **segment** | **String**| Segment name from this list&amp;#58; &amp;quot;General&amp;quot;. | |

### Return type

[**CCCDefinitionMeta**](CCCDefinitionMeta.md)

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

