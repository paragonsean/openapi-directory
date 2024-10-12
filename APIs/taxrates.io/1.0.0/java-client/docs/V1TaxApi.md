# V1TaxApi

All URIs are relative to *https://api.taxrates.io/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxRatesByCountryCode**](V1TaxApi.md#taxRatesByCountryCode) | **GET** /v1/tax/countrycode | Tax rates by Country Code |
| [**taxRatesByIpAddress**](V1TaxApi.md#taxRatesByIpAddress) | **GET** /v1/tax/ip | Tax rates by IP address |


<a id="taxRatesByCountryCode"></a>
# **taxRatesByCountryCode**
> TaxRatesByCountryCode200Response taxRatesByCountryCode(domain, countryCode, filter, zip, productCodes, province, date)

Tax rates by Country Code

Get request. This method returns all tax rates for country discovered based on country code. The country code must be 2 letters ISO 3166-1 alfa-2 country code (see &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes\&quot;&gt;here&lt;/a&gt; for more information). You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/countrycode&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;country_code&#39;:&#39;IE&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxrates.io/api");

    V1TaxApi apiInstance = new V1TaxApi(defaultClient);
    String domain = "api.taxrates.io"; // String | Domain name: api.taxrates.io
    String countryCode = "US"; // String | Country code alpha 2
    String filter = ""; // String | You can filter your taxes by one of following types: 'standard', 'reduced', 'second reduced', 'third reduced' and 'super reduced'.
    String zip = "71642"; // String | You must provide a zip code if one of your selected countries is United States and you've had selected a state on your Taxrates.io member's dashboard.
    String productCodes = "C010"; // String | Use one or many product code/s.
    String province = ""; // String | Use for Canada
    String date = "2020-09-02"; // String | 
    try {
      TaxRatesByCountryCode200Response result = apiInstance.taxRatesByCountryCode(domain, countryCode, filter, zip, productCodes, province, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1TaxApi#taxRatesByCountryCode");
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
| **domain** | **String**| Domain name: api.taxrates.io | [optional] |
| **countryCode** | **String**| Country code alpha 2 | [optional] |
| **filter** | **String**| You can filter your taxes by one of following types: &#39;standard&#39;, &#39;reduced&#39;, &#39;second reduced&#39;, &#39;third reduced&#39; and &#39;super reduced&#39;. | [optional] |
| **zip** | **String**| You must provide a zip code if one of your selected countries is United States and you&#39;ve had selected a state on your Taxrates.io member&#39;s dashboard. | [optional] |
| **productCodes** | **String**| Use one or many product code/s. | [optional] |
| **province** | **String**| Use for Canada | [optional] |
| **date** | **String**|  | [optional] |

### Return type

[**TaxRatesByCountryCode200Response**](TaxRatesByCountryCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Country not found. Have you provided correct alpha-2 country code? |  -  |
| **500** | Unexpected error |  -  |

<a id="taxRatesByIpAddress"></a>
# **taxRatesByIpAddress**
> List&lt;TaxRatesByCountryCode200Response&gt; taxRatesByIpAddress(domain, ip, filter, zip, productCode)

Tax rates by IP address

Get request. This method returns all tax rates for country discovered on either your IP address or IP address param. The IP param is not required. When empty, the taxrates.io will try to discover your IP address and based on this will retrieve the tax rates. You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/ip&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;ip&#39;:&#39;208.80.152.201&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxrates.io/api");

    V1TaxApi apiInstance = new V1TaxApi(defaultClient);
    String domain = "api.taxrates.io"; // String | Domain name: api.taxrates.io
    String ip = "86.139.70.49"; // String | Customer's IP address
    String filter = ""; // String | For US sales tax you can filter the tax type
    String zip = ""; // String | For US sales tax a Zipcode must be proivded
    String productCode = "C010"; // String | Your can filter your taxes by product code
    try {
      List<TaxRatesByCountryCode200Response> result = apiInstance.taxRatesByIpAddress(domain, ip, filter, zip, productCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1TaxApi#taxRatesByIpAddress");
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
| **domain** | **String**| Domain name: api.taxrates.io | [optional] |
| **ip** | **String**| Customer&#39;s IP address | [optional] |
| **filter** | **String**| For US sales tax you can filter the tax type | [optional] |
| **zip** | **String**| For US sales tax a Zipcode must be proivded | [optional] |
| **productCode** | **String**| Your can filter your taxes by product code | [optional] |

### Return type

[**List&lt;TaxRatesByCountryCode200Response&gt;**](TaxRatesByCountryCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of tax rates for VAT, GST &amp; TAX |  -  |
| **404** | Geolocation can not be processed/No matching country found |  -  |
| **500** | Unexpected error |  -  |

