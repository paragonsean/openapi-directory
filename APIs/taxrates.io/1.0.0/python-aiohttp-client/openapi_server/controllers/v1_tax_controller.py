from typing import List, Dict
from aiohttp import web

from openapi_server.models.tax_rates_by_country_code200_response import TaxRatesByCountryCode200Response
from openapi_server.models.tax_rates_by_country_code500_response import TaxRatesByCountryCode500Response
from openapi_server import util


async def tax_rates_by_country_code(request: web.Request, domain=None, country_code=None, filter=None, zip=None, product_codes=None, province_=None, _date=None) -> web.Response:
    """Tax rates by Country Code

    Get request. This method returns all tax rates for country discovered based on country code. The country code must be 2 letters ISO 3166-1 alfa-2 country code (see &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes\&quot;&gt;here&lt;/a&gt; for more information). You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/countrycode&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;country_code&#39;:&#39;IE&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 

    :param domain: Domain name: api.taxrates.io
    :type domain: str
    :param country_code: Country code alpha 2
    :type country_code: str
    :param filter: You can filter your taxes by one of following types: &#39;standard&#39;, &#39;reduced&#39;, &#39;second reduced&#39;, &#39;third reduced&#39; and &#39;super reduced&#39;.
    :type filter: str
    :param zip: You must provide a zip code if one of your selected countries is United States and you&#39;ve had selected a state on your Taxrates.io member&#39;s dashboard.
    :type zip: str
    :param product_codes: Use one or many product code/s.
    :type product_codes: str
    :param province_: Use for Canada
    :type province_: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def tax_rates_by_ip_address(request: web.Request, domain=None, ip=None, filter=None, zip=None, product_code=None) -> web.Response:
    """Tax rates by IP address

    Get request. This method returns all tax rates for country discovered on either your IP address or IP address param. The IP param is not required. When empty, the taxrates.io will try to discover your IP address and based on this will retrieve the tax rates. You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/ip&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;ip&#39;:&#39;208.80.152.201&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 

    :param domain: Domain name: api.taxrates.io
    :type domain: str
    :param ip: Customer&#39;s IP address
    :type ip: str
    :param filter: For US sales tax you can filter the tax type
    :type filter: str
    :param zip: For US sales tax a Zipcode must be proivded
    :type zip: str
    :param product_code: Your can filter your taxes by product code
    :type product_code: str

    """
    return web.Response(status=200)
