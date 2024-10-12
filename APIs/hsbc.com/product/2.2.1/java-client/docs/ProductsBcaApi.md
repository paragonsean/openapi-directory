# ProductsBcaApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**openBankingV22BusinessCurrentAccountsGet**](ProductsBcaApi.md#openBankingV22BusinessCurrentAccountsGet) | **GET** /open-banking/v2.2/business-current-accounts |  |
| [**xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet**](ProductsBcaApi.md#xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet) | **GET** /x-open-banking/v2.2/business-current-accounts/segment/{segment} |  |


<a id="openBankingV22BusinessCurrentAccountsGet"></a>
# **openBankingV22BusinessCurrentAccountsGet**
> BCADefinitionMeta openBankingV22BusinessCurrentAccountsGet()



This API will return data about all BCA products and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsBcaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    ProductsBcaApi apiInstance = new ProductsBcaApi(defaultClient);
    try {
      BCADefinitionMeta result = apiInstance.openBankingV22BusinessCurrentAccountsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsBcaApi#openBankingV22BusinessCurrentAccountsGet");
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

[**BCADefinitionMeta**](BCADefinitionMeta.md)

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

<a id="xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet"></a>
# **xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet**
> BCADefinitionMeta xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet(segment)



This extended API will return data about all BCA products for the specified segment. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsBcaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dikpeqbnwi3kx.cloudfront.net");

    ProductsBcaApi apiInstance = new ProductsBcaApi(defaultClient);
    String segment = "segment_example"; // String | Segment name from this list&#58; &quot;ClientAccount&quot;, &quot;Standard&quot;, &quot;NonCommercial&quot;, &quot;Religious&quot;, &quot;SectorSpecific&quot;, &quot;Startup&quot;, &quot;Switcher&quot;.
    try {
      BCADefinitionMeta result = apiInstance.xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet(segment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsBcaApi#xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet");
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
| **segment** | **String**| Segment name from this list&amp;#58; &amp;quot;ClientAccount&amp;quot;, &amp;quot;Standard&amp;quot;, &amp;quot;NonCommercial&amp;quot;, &amp;quot;Religious&amp;quot;, &amp;quot;SectorSpecific&amp;quot;, &amp;quot;Startup&amp;quot;, &amp;quot;Switcher&amp;quot;. | |

### Return type

[**BCADefinitionMeta**](BCADefinitionMeta.md)

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

