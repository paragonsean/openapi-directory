# TaxratesIoApi.V3TaxApi

All URIs are relative to *https://api.taxrates.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allTaxRates**](V3TaxApi.md#allTaxRates) | **GET** /v3/tax/rates | All tax rates



## allTaxRates

> [AllTaxRates200ResponseInner] allTaxRates(opts)

All tax rates

&lt;p&gt;Get request. This method returns all tax rates configured on your account. Based on your country selection the endpoint will return all taxes for all countries. You can use the &#39;filter&#39; parameter to narrow results to selected type of tax. Use &#39;zip&#39; parameter when you have selected the United States.&lt;/p&gt; &lt;p&gt;We have development an easy to use scheduler so you can call the API to get the rates every hour or day. Please click on the following link to see the &lt;a href&#x3D;\&quot;https://gist.github.com/gregbird/cd904ff230cdf86253716aa351154edb\&quot;&gt;code on Github&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;&lt;b&gt;Please note&lt;/b&gt; in cases when a US state doesn&#39;t have sales tax and when a product is tax exempt for a zip code or for a state the API response will be \&quot;null\&quot;&lt;/p&gt; &lt;p&gt;To get a response you need to have selected a product code in your Taxrates.io dashboard, please see the Introduction section above for description of the different types of product codes.&lt;/p&gt; &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;   var taxrates_endpoint &#x3D; &#39;tax/rates&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;};   var taxrates_url &#x3D; &#39;/api/v3/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data, textStatus, jqXHR) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             var taxrates_range &#x3D; &#39;&#39;;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;rates\&quot;)){                     jQuery.each(v.rates, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Type;                             rates[i][1] &#x3D; w.data_value;                             rates[i][2] &#x3D; w.product_code;                             i++;                         }                     });                 }             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             var cursor &#x3D; jqXHR.getResponseHeader(&#39;X-Cursor-Next&#39;);             if (cursor) {               // get next page...             }             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 

### Example

```javascript
import TaxratesIoApi from 'taxrates_io_api';

let apiInstance = new TaxratesIoApi.V3TaxApi();
let opts = {
  'domain': "<string>", // String | Domain name: api.taxrates.io
  'filter': "", // String | You can filter your taxes by one of following types: 'standard', 'CombinedRate', 'CountyRate', 'CityRate', 'SPDRate' and 'MTARate'.
  'cursor': "", // String | Cursor shows from which record you want to get information. Default value is 0, next value can be retrieved from X-Cursor-Next header.
  'productCode': "C012" // String | 
};
apiInstance.allTaxRates(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **String**| Domain name: api.taxrates.io | [optional] 
 **filter** | **String**| You can filter your taxes by one of following types: &#39;standard&#39;, &#39;CombinedRate&#39;, &#39;CountyRate&#39;, &#39;CityRate&#39;, &#39;SPDRate&#39; and &#39;MTARate&#39;. | [optional] 
 **cursor** | **String**| Cursor shows from which record you want to get information. Default value is 0, next value can be retrieved from X-Cursor-Next header. | [optional] 
 **productCode** | **String**|  | [optional] 

### Return type

[**[AllTaxRates200ResponseInner]**](AllTaxRates200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

