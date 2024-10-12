/*
 * Taxrates.io API
 * <h3>Introduction</h3> <p>Taxrates.io is a global tax rate service that automates the management of monitoring tax rates changes in 181 countries. We monitor over 14,000 US sales tax, VAT, GST rates for you and make updates via our API so you always have the most update tax rates.</p> <p>You can use Taxrates.io as a virtual sandbox where we provide you with 30 days free trial.</p> <h3>Countries</h3> <p>We currently support the following countries around the world. If you would like to request the addition of a new country, please email us at <a href=\"mailto:support@taxrates.io\">support@taxrates.io</a></p> <table>   <tr><td>Afghanistan</td><td>Gambia</td><td>Nicaragua</td></tr>   <tr><td>Albania</td><td>Georgia</td><td>Niger</td></tr>   <tr><td>Andorra</td><td>Germany</td><td>Nigeria</td></tr>   <tr><td>Angola</td><td>Ghana</td><td>North Korea</td></tr>   <tr><td>Antigua and Barbuda</td><td>Greece</td><td>Norway</td></tr>   <tr><td>Argentina</td><td>Grenada</td><td>Pakistan</td></tr>   <tr><td>Armenia</td><td>Guam</td><td>Palestine</td></tr>   <tr><td>Aruba</td><td>Guatemala</td><td>Panama</td></tr>   <tr><td>Australia</td><td>Guinea</td><td>Papua New Guinea</td></tr>   <tr><td>Austria</td><td>Guyana</td><td>Paraguay</td></tr>   <tr><td>Azerbaijan</td><td>Haiti</td><td>Peru</td></tr>   <tr><td>Bahamas</td><td>Honduras</td><td>Philippines</td></tr>   <tr><td>Bangladesh</td><td>Hungary</td><td>Poland</td></tr>   <tr><td>Barbados</td><td>Iceland</td><td>Portugal</td></tr>   <tr><td>Belarus</td><td>India</td><td>Puerto Rico</td></tr>   <tr><td>Belgium</td><td>Indonesia</td><td>Republic of the Congo</td></tr>   <tr><td>Belize</td><td>Iran</td><td>Romania</td></tr>   <tr><td>Benin</td><td>Ireland</td><td>Russian Federation</td></tr>   <tr><td>Bhutan</td><td>Isle of Man</td><td>Rwanda</td></tr>   <tr><td>Bolivia</td><td>Israel</td><td>Samoa</td></tr>   <tr><td>Bonaire</td><td>Italy</td><td>Senegal</td></tr>   <tr><td>Bosnia and Herzegovina</td><td>Japan</td><td>Serbia</td></tr>   <tr><td>Botswana</td><td>Jersey</td><td>Seychelles</td></tr>   <tr><td>Brazil</td><td>Jordan</td><td>Sierra Leone</td></tr>   <tr><td>Bulgaria</td><td>Jordan</td><td>Singapore</td></tr>   <tr><td>Burkina Faso</td><td>Kazakhstan</td><td>Slovakia</td></tr>   <tr><td>Burundi</td><td>Kenya</td><td>Slovenia</td></tr>   <tr><td>Cambodia</td><td>Kiribati</td><td>Solomon Islands</td></tr>   <tr><td>Cameroon</td><td>Kosovo</td><td>Somalia</td></tr>   <tr><td>Cape Verde</td><td>Kyrgyzstan</td><td>South Africa</td></tr>   <tr><td>Central African Republic</td><td>Laos</td><td>South Korea</td></tr>   <tr><td>Chad</td><td>Latvia</td><td>South Sudan</td></tr>   <tr><td>Chile</td><td>Lebanon</td><td>Spain</td></tr>   <tr><td>China</td><td>Lesotho</td><td>Sri Lanka</td></tr>   <tr><td>Columbia</td><td>Liberia</td><td>St Lucia</td></tr>   <tr><td>Comoros</td><td>Liechtenstein</td><td>Sudan</td></tr>   <tr><td>Cook Islands</td><td>Lithuania</td><td>Suriname</td></tr>   <tr><td>Costa Rica</td><td>Luxembourg</td><td>Swaziland</td></tr>   <tr><td>Cote d'Ivoire</td><td>Macedonia</td><td>Sweden</td></tr>   <tr><td>Croatia</td><td>Madagascar</td><td>Switzerland</td></tr>   <tr><td>Cuba</td><td>Malawi</td><td>Tahiti</td></tr>   <tr><td>Curacao</td><td>Malaysia</td><td>Taiwan</td></tr>   <tr><td>Cyprus</td><td>Maldives</td><td>Tajikistan</td></tr>   <tr><td>Czech Republic</td><td>Mali</td><td>Tanzania</td></tr>   <tr><td>Democratic Republic of the Congo</td><td>Malta</td><td>Thailand</td></tr>   <tr><td>Denmark</td><td>Mauritania</td><td>Togo</td></tr>   <tr><td>Djbouti</td><td>Mauritius</td><td>Tonga</td></tr>   <tr><td>Dominica</td><td>Mexico</td><td>Trinidad and Tobago</td></tr>   <tr><td>Dominican Republic</td><td>Micronesia</td><td>Tunisia</td></tr>   <tr><td>Ecuador</td><td>Moldova</td><td>Turkmenistan</td></tr>   <tr><td>Egypt</td><td>Monaco</td><td>Tuvalu</td></tr>   <tr><td>El Salvador</td><td>Mongolia</td><td>Uganda</td></tr>   <tr><td>Equatorial Guinea</td><td>Montenegro</td><td>Ukraine</td></tr>   <tr><td>Eritrea</td><td>Morocco</td><td>United Kingdom</td></tr>   <tr><td>Estonia</td><td>Mozambique</td><td>United States</td></tr>   <tr><td>Ethiopia</td><td>Myanmar</td><td>Uruguay</td></tr>   <tr><td>Fiji</td><td>Namibia</td><td>Vanuatu</td></tr>   <tr><td>Finland</td><td>Nepal</td><td>Venezuela</td></tr>   <tr><td>France</td><td>Netherlands</td><td>Vietnam</td></tr>   <tr><td>Gabon</td><td>New Zealand</td><td>Yemen</td></tr> </table> <h3>Products codes</h3> <p>The Taxrates.io API’s provides product-level tax rates for a subset of product codes. These codes are to be used for products that are either exempt from tax in some jurisdictions or are taxed at reduced rates.</p> <p>We will be expanding support for additional, less common categories over time. If you would like to request the addition of a new product category, please email us at <a href=\"mailto:support@taxrates.io\">support@taxrates.io</a></p> <p>Please select a product code/s when making a request to the Taxrates.io API</p> <table>   <tr><th>Product code</th><th>Product Description</th></tr>   <tr><td>C010</td><td>Services which are not subject to a service-specific tax</td></tr>   <tr><td>C011</td><td>Software - Downloaded</td></tr>   <tr><td>C012</td><td>Books - Downloaded</td></tr>   <tr><td>C011</td><td>Music - Downloaded</td></tr>   <tr><td>C011</td><td>Movies/Digital Video - Downloaded</td></tr>   <tr><td>C011</td><td>Other Electronic Goods - Downloaded</td></tr>   <tr><td>C011</td><td>Streaming Music/Audio Services new</td></tr>   <tr><td>C011</td><td>Streaming Video Services new</td></tr>   <tr><td>C018</td><td>Software as a Services, Generally (Remote Access to Hosted Software)</td></tr>   <tr><td>C018</td><td>Remote Access to Hosted Software - Personal Use</td></tr>   <tr><td>C018</td><td>Remote Access to Hosted Software - Business Use</td></tr>   <tr><td>C021</td><td>Remote Access to Hosted Business Custom Applications</td></tr>   <tr><td>C021</td><td>Personal Cloud Storage/Backup</td></tr>   <tr><td>C021</td><td>Business Cloud Storage/Backup</td></tr>   <tr><td>C021</td><td>Business Data Warehouses</td></tr>   <tr><td>C022</td><td>Infrastructure as Service, Generally</td></tr>   <tr><td>C022</td><td>Ecommerce Site/Webserver Hosting</td></tr>   <tr><td>C022</td><td>Provision of Virtual Computing Capacity</td></tr>   <tr><td>C022</td><td>Software - package or canned program</td></tr>   <tr><td>C022</td><td>Software - modifications to canned program</td></tr>   <tr><td>C022</td><td>Software - custom programs - material</td></tr>   <tr><td>C022</td><td>Software - custom programs - professional serv.</td></tr>   <tr><td>C022</td><td>Information services</td></tr>   <tr><td>C022</td><td>Data processing services</td></tr>   <tr><td>C022</td><td>Mainframe computer access and processing serv.</td></tr>   <tr><td>C022</td><td>Online Data processing services</td></tr> </table> <h3>Filtering</h3> <p>When calling the API endpoints you can use 'filter' parameters to get tax rate for the selected type. You can get the following tax types (Each tax rate will always have one of following types)</p> <h3>US Sales tax Rates</h3> <ol>   <li>CombinedRate</li>   <li>StateRate</li>   <li>CountyRate</li>   <li>CityRate</li>   <li>SpecialRate</li> </ol> <p>We recommend using <a href=\"https://www.getpostman.com/\">Postman</a> when discovering our API. Happy using!</p> <h3>Rate Limiting</h3> <p>We limit API requests.</p> <p>If you’re exceeding this rate and encountering 429 errors, review the following:</p> <ul>   <li>Only make requests in states / regions where you have enabled.</li>   <li>Cache responses if the order details haven’t changed since the last calculation at checkout.</li> </ul> <h3>Errors</h3> <p>The Taxrates.io API uses the following error codes:<p/> <table>   <tr><th>Code</th><th>Error Message</th></tr>   <tr><td>400</td><td>Bad Request – Your request format is bad.</td></tr>   <tr><td>401</td><td>Unauthorized – Your API key is wrong.</td></tr>   <tr><td>404</td><td>Not Found – The specified resource could not be found.</td></tr>   <tr><td>405</td><td>Method Not Allowed – You tried to access a resource with an invalid method.</td></tr>   <tr><td>429</td><td>Too Many Requests – You’re requesting too many resources! Slow down!</td></tr>   <tr><td>500</td><td>Internal Server Error – We had a problem with our server. Try again later.</td></tr>   <tr><td>503</td><td>Service Unavailable – We’re temporarily offline for maintenance. Try again later.</td></tr> </table> <p>Verify your API token is correct and make sure you’re correctly setting the <a href=\"#authentication\">Authorization header</a>.</p> <p>If you’re still not sure what’s wrong, <a href=\"mailto:support@taxrates.io\">contact us</a> and we’ll investigate.</p> <h3>Changelog</h3> <p>Stay on top of new developer-facing features, accuracy improvements, and bug fixes for our API. Have a request? Encounter an issue? <a href=\"mailto:support@taxrates.io\">We’d love to hear your feedback.</a></p>   Contact Support:  Name: apiteam@taxrates.io
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.TaxRatesByCountryCode200Response;
import org.openapitools.client.model.TaxRatesByCountryCode500Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class V1TaxApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public V1TaxApi() {
        this(Configuration.getDefaultApiClient());
    }

    public V1TaxApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for taxRatesByCountryCode
     * @param domain Domain name: api.taxrates.io (optional)
     * @param countryCode Country code alpha 2 (optional)
     * @param filter You can filter your taxes by one of following types: &#39;standard&#39;, &#39;reduced&#39;, &#39;second reduced&#39;, &#39;third reduced&#39; and &#39;super reduced&#39;. (optional)
     * @param zip You must provide a zip code if one of your selected countries is United States and you&#39;ve had selected a state on your Taxrates.io member&#39;s dashboard. (optional)
     * @param productCodes Use one or many product code/s. (optional)
     * @param province Use for Canada (optional)
     * @param date  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Country not found. Have you provided correct alpha-2 country code? </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxRatesByCountryCodeCall(String domain, String countryCode, String filter, String zip, String productCodes, String province, String date, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/tax/countrycode";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (countryCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("country_code", countryCode));
        }

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (zip != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("zip", zip));
        }

        if (productCodes != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("product_codes[]", productCodes));
        }

        if (province != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("province ", province));
        }

        if (date != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date", date));
        }

        final String[] localVarAccepts = {
            "application/json",
            "text/plain"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call taxRatesByCountryCodeValidateBeforeCall(String domain, String countryCode, String filter, String zip, String productCodes, String province, String date, final ApiCallback _callback) throws ApiException {
        return taxRatesByCountryCodeCall(domain, countryCode, filter, zip, productCodes, province, date, _callback);

    }

    /**
     * Tax rates by Country Code
     * Get request. This method returns all tax rates for country discovered based on country code. The country code must be 2 letters ISO 3166-1 alfa-2 country code (see &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes\&quot;&gt;here&lt;/a&gt; for more information). You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/countrycode&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;country_code&#39;:&#39;IE&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 
     * @param domain Domain name: api.taxrates.io (optional)
     * @param countryCode Country code alpha 2 (optional)
     * @param filter You can filter your taxes by one of following types: &#39;standard&#39;, &#39;reduced&#39;, &#39;second reduced&#39;, &#39;third reduced&#39; and &#39;super reduced&#39;. (optional)
     * @param zip You must provide a zip code if one of your selected countries is United States and you&#39;ve had selected a state on your Taxrates.io member&#39;s dashboard. (optional)
     * @param productCodes Use one or many product code/s. (optional)
     * @param province Use for Canada (optional)
     * @param date  (optional)
     * @return TaxRatesByCountryCode200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Country not found. Have you provided correct alpha-2 country code? </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public TaxRatesByCountryCode200Response taxRatesByCountryCode(String domain, String countryCode, String filter, String zip, String productCodes, String province, String date) throws ApiException {
        ApiResponse<TaxRatesByCountryCode200Response> localVarResp = taxRatesByCountryCodeWithHttpInfo(domain, countryCode, filter, zip, productCodes, province, date);
        return localVarResp.getData();
    }

    /**
     * Tax rates by Country Code
     * Get request. This method returns all tax rates for country discovered based on country code. The country code must be 2 letters ISO 3166-1 alfa-2 country code (see &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes\&quot;&gt;here&lt;/a&gt; for more information). You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/countrycode&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;country_code&#39;:&#39;IE&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 
     * @param domain Domain name: api.taxrates.io (optional)
     * @param countryCode Country code alpha 2 (optional)
     * @param filter You can filter your taxes by one of following types: &#39;standard&#39;, &#39;reduced&#39;, &#39;second reduced&#39;, &#39;third reduced&#39; and &#39;super reduced&#39;. (optional)
     * @param zip You must provide a zip code if one of your selected countries is United States and you&#39;ve had selected a state on your Taxrates.io member&#39;s dashboard. (optional)
     * @param productCodes Use one or many product code/s. (optional)
     * @param province Use for Canada (optional)
     * @param date  (optional)
     * @return ApiResponse&lt;TaxRatesByCountryCode200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Country not found. Have you provided correct alpha-2 country code? </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<TaxRatesByCountryCode200Response> taxRatesByCountryCodeWithHttpInfo(String domain, String countryCode, String filter, String zip, String productCodes, String province, String date) throws ApiException {
        okhttp3.Call localVarCall = taxRatesByCountryCodeValidateBeforeCall(domain, countryCode, filter, zip, productCodes, province, date, null);
        Type localVarReturnType = new TypeToken<TaxRatesByCountryCode200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Tax rates by Country Code (asynchronously)
     * Get request. This method returns all tax rates for country discovered based on country code. The country code must be 2 letters ISO 3166-1 alfa-2 country code (see &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes\&quot;&gt;here&lt;/a&gt; for more information). You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/countrycode&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;country_code&#39;:&#39;IE&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 
     * @param domain Domain name: api.taxrates.io (optional)
     * @param countryCode Country code alpha 2 (optional)
     * @param filter You can filter your taxes by one of following types: &#39;standard&#39;, &#39;reduced&#39;, &#39;second reduced&#39;, &#39;third reduced&#39; and &#39;super reduced&#39;. (optional)
     * @param zip You must provide a zip code if one of your selected countries is United States and you&#39;ve had selected a state on your Taxrates.io member&#39;s dashboard. (optional)
     * @param productCodes Use one or many product code/s. (optional)
     * @param province Use for Canada (optional)
     * @param date  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Country not found. Have you provided correct alpha-2 country code? </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxRatesByCountryCodeAsync(String domain, String countryCode, String filter, String zip, String productCodes, String province, String date, final ApiCallback<TaxRatesByCountryCode200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = taxRatesByCountryCodeValidateBeforeCall(domain, countryCode, filter, zip, productCodes, province, date, _callback);
        Type localVarReturnType = new TypeToken<TaxRatesByCountryCode200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for taxRatesByIpAddress
     * @param domain Domain name: api.taxrates.io (optional)
     * @param ip Customer&#39;s IP address (optional)
     * @param filter For US sales tax you can filter the tax type (optional)
     * @param zip For US sales tax a Zipcode must be proivded (optional)
     * @param productCode Your can filter your taxes by product code (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of tax rates for VAT, GST &amp; TAX </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Geolocation can not be processed/No matching country found </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxRatesByIpAddressCall(String domain, String ip, String filter, String zip, String productCode, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/v1/tax/ip";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain", domain));
        }

        if (ip != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("ip", ip));
        }

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (zip != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("zip", zip));
        }

        if (productCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("product_code", productCode));
        }

        final String[] localVarAccepts = {
            "application/json",
            "text/plain"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call taxRatesByIpAddressValidateBeforeCall(String domain, String ip, String filter, String zip, String productCode, final ApiCallback _callback) throws ApiException {
        return taxRatesByIpAddressCall(domain, ip, filter, zip, productCode, _callback);

    }

    /**
     * Tax rates by IP address
     * Get request. This method returns all tax rates for country discovered on either your IP address or IP address param. The IP param is not required. When empty, the taxrates.io will try to discover your IP address and based on this will retrieve the tax rates. You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/ip&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;ip&#39;:&#39;208.80.152.201&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 
     * @param domain Domain name: api.taxrates.io (optional)
     * @param ip Customer&#39;s IP address (optional)
     * @param filter For US sales tax you can filter the tax type (optional)
     * @param zip For US sales tax a Zipcode must be proivded (optional)
     * @param productCode Your can filter your taxes by product code (optional)
     * @return List&lt;TaxRatesByCountryCode200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of tax rates for VAT, GST &amp; TAX </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Geolocation can not be processed/No matching country found </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public List<TaxRatesByCountryCode200Response> taxRatesByIpAddress(String domain, String ip, String filter, String zip, String productCode) throws ApiException {
        ApiResponse<List<TaxRatesByCountryCode200Response>> localVarResp = taxRatesByIpAddressWithHttpInfo(domain, ip, filter, zip, productCode);
        return localVarResp.getData();
    }

    /**
     * Tax rates by IP address
     * Get request. This method returns all tax rates for country discovered on either your IP address or IP address param. The IP param is not required. When empty, the taxrates.io will try to discover your IP address and based on this will retrieve the tax rates. You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/ip&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;ip&#39;:&#39;208.80.152.201&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 
     * @param domain Domain name: api.taxrates.io (optional)
     * @param ip Customer&#39;s IP address (optional)
     * @param filter For US sales tax you can filter the tax type (optional)
     * @param zip For US sales tax a Zipcode must be proivded (optional)
     * @param productCode Your can filter your taxes by product code (optional)
     * @return ApiResponse&lt;List&lt;TaxRatesByCountryCode200Response&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of tax rates for VAT, GST &amp; TAX </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Geolocation can not be processed/No matching country found </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<TaxRatesByCountryCode200Response>> taxRatesByIpAddressWithHttpInfo(String domain, String ip, String filter, String zip, String productCode) throws ApiException {
        okhttp3.Call localVarCall = taxRatesByIpAddressValidateBeforeCall(domain, ip, filter, zip, productCode, null);
        Type localVarReturnType = new TypeToken<List<TaxRatesByCountryCode200Response>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Tax rates by IP address (asynchronously)
     * Get request. This method returns all tax rates for country discovered on either your IP address or IP address param. The IP param is not required. When empty, the taxrates.io will try to discover your IP address and based on this will retrieve the tax rates. You can use &#39;filter&#39; parameter to narrow results to selected type of tax &lt;p&gt;For US sales tax you can filter the tax rate you want for each state or zip code with one of the following: (they are case sensitive)&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;CombinedRate&lt;/li&gt;   &lt;li&gt;StateRate&lt;/li&gt;   &lt;li&gt;CountyRate&lt;/li&gt;   &lt;li&gt;CityRate&lt;/li&gt;   &lt;li&gt;SpecialRate&lt;/li&gt; &lt;/ul&gt; &lt;pre&gt;&lt;code class&#x3D;\&quot;js\&quot;&gt;var taxrates_endpoint &#x3D; &#39;tax/ip&#39;;   var taxrates_params &#x3D; {&#39;domain&#39;:&#39;api.taxrates.io&#39;, &#39;ip&#39;:&#39;208.80.152.201&#39;, &#39;product_code&#39;:&#39;C010&#39;};   var taxrates_url &#x3D; &#39;/api/v1/&#39;;   if ( localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;) ){   jQuery.support.cors &#x3D; true;   jQuery.ajax({       url: taxrates_url+taxrates_endpoint,       type: &#39;get&#39;,       method: &#39;get&#39;,       dataType: \&quot;json\&quot;,       data: taxrates_params,       beforeSend: function (request) {               request.withCredentials &#x3D; true;               request.setRequestHeader(\&quot;Authorization\&quot;, \&quot;Apikey \&quot; + localStorage.getItem(\&quot;Taxrates_API_Client_Secret\&quot;));       },       headers: {         \&quot;accept\&quot;: \&quot;application/json\&quot;       },       contentType: &#39;application/json; charset&#x3D;utf-8&#39;,       success: function (data) {         //Maintain errors inside success because the API may return 200 in general, but different code inside           if(data.ErrorCode&#x3D;&#x3D;&#39;404&#39; || data.ErrorCode&#x3D;&#x3D;&#39;500&#39;){             //Maintain errors here             console.log(data.ErrorMessage);             return false;           }else{             var rates &#x3D; [];             var i&#x3D;0;             jQuery.each(data, function(k, v) {                 if(v.hasOwnProperty(\&quot;taxes\&quot;)){                     jQuery.each(v.taxes, function(m, w) {                         rates[i] &#x3D; [];                         //Only showing standard rate type                         if( w.Type &#x3D;&#x3D; \&quot;standard\&quot; ){                             rates[i][0] &#x3D; w.Country;                             rates[i][1] &#x3D; w.Type;                             rates[i][2] &#x3D; w.data_value;                             i++;                         }                     });                 }             //Now you have all your rates inside rates variable.             }).fail(function(xhr) {                     //Maintain your errors here                     return false;             });             return true;   }else{     //Not logged into taxrates.io     //Maintain your errors here     return false;   }&lt;/code&gt;&lt;/pre&gt; 
     * @param domain Domain name: api.taxrates.io (optional)
     * @param ip Customer&#39;s IP address (optional)
     * @param filter For US sales tax you can filter the tax type (optional)
     * @param zip For US sales tax a Zipcode must be proivded (optional)
     * @param productCode Your can filter your taxes by product code (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of tax rates for VAT, GST &amp; TAX </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Geolocation can not be processed/No matching country found </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxRatesByIpAddressAsync(String domain, String ip, String filter, String zip, String productCode, final ApiCallback<List<TaxRatesByCountryCode200Response>> _callback) throws ApiException {

        okhttp3.Call localVarCall = taxRatesByIpAddressValidateBeforeCall(domain, ip, filter, zip, productCode, _callback);
        Type localVarReturnType = new TypeToken<List<TaxRatesByCountryCode200Response>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
