# CountryApi

All URIs are relative to *https://api.ebay.com/sell/metadata/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSalesTaxJurisdictions**](CountryApi.md#getSalesTaxJurisdictions) | **GET** /country/{countryCode}/sales_tax_jurisdiction |  |


<a id="getSalesTaxJurisdictions"></a>
# **getSalesTaxJurisdictions**
> SalesTaxJurisdictions getSalesTaxJurisdictions(countryCode)



This method retrieves all the sales tax jurisdictions for the country that you specify in the &lt;b&gt;countryCode&lt;/b&gt; path parameter. Countries with valid sales tax jurisdictions are Canada and the US.  &lt;br/&gt;&lt;br/&gt;The response from this call tells you the jurisdictions for which a seller can configure tax tables. Although setting up tax tables is optional, you can use the &lt;b&gt;createOrReplaceSalesTax&lt;/b&gt; in the &lt;b&gt;Account API&lt;/b&gt; call to configure the tax tables for the jurisdictions you sell to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/metadata/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    CountryApi apiInstance = new CountryApi(defaultClient);
    String countryCode = "countryCode_example"; // String | This path parameter specifies the two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 3166</a> country code for the country whose jurisdictions you want to retrieve. eBay provides sales tax jurisdiction information for Canada and the United States.Valid values for this path parameter are <code>CA</code> and <code>US</code>.
    try {
      SalesTaxJurisdictions result = apiInstance.getSalesTaxJurisdictions(countryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryApi#getSalesTaxJurisdictions");
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
| **countryCode** | **String**| This path parameter specifies the two-letter &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 3166&lt;/a&gt; country code for the country whose jurisdictions you want to retrieve. eBay provides sales tax jurisdiction information for Canada and the United States.Valid values for this path parameter are &lt;code&gt;CA&lt;/code&gt; and &lt;code&gt;US&lt;/code&gt;. | |

### Return type

[**SalesTaxJurisdictions**](SalesTaxJurisdictions.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

