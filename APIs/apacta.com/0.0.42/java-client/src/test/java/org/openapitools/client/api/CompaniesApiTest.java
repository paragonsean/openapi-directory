/*
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest;
import org.openapitools.client.model.CompaniesCompanyIdFormTemplatesGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationFeatureSettingsGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationSettingsGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationSettingsPostRequest;
import org.openapitools.client.model.CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest;
import org.openapitools.client.model.CompaniesGet200Response;
import org.openapitools.client.model.CompaniesSubscriptionSelfServiceGet200Response;
import org.openapitools.client.model.CreateSuccessResponse;
import org.openapitools.client.model.EmptySuccessResponse;
import org.openapitools.client.model.ErrorNotFound;
import org.openapitools.client.model.ErrorValidation;
import org.openapitools.client.model.ForbiddenError;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CompaniesApi
 */
@Disabled
public class CompaniesApiTest {

    private final CompaniesApi api = new CompaniesApi();

    /**
     * View a company integration feature setting
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetTest() throws ApiException {
        String companyId = null;
        String cIntegrationFeatureSettingId = null;
        CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response response = api.companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(companyId, cIntegrationFeatureSettingId);
        // TODO: test validations
    }

    /**
     * Edit a company integration feature setting
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutTest() throws ApiException {
        String companyId = null;
        String cIntegrationFeatureSettingId = null;
        CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response response = api.companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(companyId, cIntegrationFeatureSettingId);
        // TODO: test validations
    }

    /**
     * List a company integration feature settings
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdCompaniesIntegrationFeatureSettingsGetTest() throws ApiException {
        String companyId = null;
        CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response response = api.companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(companyId);
        // TODO: test validations
    }

    /**
     * Add a company integration feature setting
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdCompaniesIntegrationFeatureSettingsPostTest() throws ApiException {
        String companyId = null;
        CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest = null;
        CreateSuccessResponse response = api.companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(companyId, companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest);
        // TODO: test validations
    }

    /**
     * Delete a form template company
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdFormTemplatesFormTemplateIdDeleteTest() throws ApiException {
        String companyId = null;
        String formTemplateId = null;
        EmptySuccessResponse response = api.companiesCompanyIdFormTemplatesFormTemplateIdDelete(companyId, formTemplateId);
        // TODO: test validations
    }

    /**
     * Get a company form template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdFormTemplatesFormTemplateIdGetTest() throws ApiException {
        String companyId = null;
        String id = null;
        String formTemplateId = null;
        CompaniesCompanyIdFormTemplatesGet200Response response = api.companiesCompanyIdFormTemplatesFormTemplateIdGet(companyId, id, formTemplateId);
        // TODO: test validations
    }

    /**
     * Get a list of company form templates
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdFormTemplatesGetTest() throws ApiException {
        String companyId = null;
        String formTemplateId = null;
        CompaniesCompanyIdFormTemplatesGet200Response response = api.companiesCompanyIdFormTemplatesGet(companyId, formTemplateId);
        // TODO: test validations
    }

    /**
     * Details of 1 company
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdGetTest() throws ApiException {
        String companyId = null;
        CompaniesCompanyIdGet200Response response = api.companiesCompanyIdGet(companyId);
        // TODO: test validations
    }

    /**
     * Get a list of integration feature settings
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdIntegrationFeatureSettingsGetTest() throws ApiException {
        String companyId = null;
        CompaniesCompanyIdIntegrationFeatureSettingsGet200Response response = api.companiesCompanyIdIntegrationFeatureSettingsGet(companyId);
        // TODO: test validations
    }

    /**
     * Show details of 1 integration feature setting
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetTest() throws ApiException {
        String companyId = null;
        String integrationFeatureSettingId = null;
        CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response response = api.companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(companyId, integrationFeatureSettingId);
        // TODO: test validations
    }

    /**
     * Delete a company integration setting
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteTest() throws ApiException {
        String companyId = null;
        String companiesIntegrationSettingId = null;
        EmptySuccessResponse response = api.companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(companyId, companiesIntegrationSettingId);
        // TODO: test validations
    }

    /**
     * Get a company integration setting
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetTest() throws ApiException {
        String companyId = null;
        String companiesIntegrationSettingId = null;
        CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response response = api.companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(companyId, companiesIntegrationSettingId);
        // TODO: test validations
    }

    /**
     * Edit a company integration setting
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutTest() throws ApiException {
        String companyId = null;
        String companiesIntegrationSettingId = null;
        EmptySuccessResponse response = api.companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(companyId, companiesIntegrationSettingId);
        // TODO: test validations
    }

    /**
     * Get a list of company integration settings
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdIntegrationSettingsGetTest() throws ApiException {
        String companyId = null;
        String identifier = null;
        CompaniesCompanyIdIntegrationSettingsGet200Response response = api.companiesCompanyIdIntegrationSettingsGet(companyId, identifier);
        // TODO: test validations
    }

    /**
     * Add a company integration setting
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdIntegrationSettingsPostTest() throws ApiException {
        String companyId = null;
        CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest = null;
        CreateSuccessResponse response = api.companiesCompanyIdIntegrationSettingsPost(companyId, companiesCompanyIdIntegrationSettingsPostRequest);
        // TODO: test validations
    }

    /**
     * Delete a company price margin
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdPriceMarginsPriceMarginsIdDeleteTest() throws ApiException {
        String companyId = null;
        String priceMarginId = null;
        String priceMarginsId = null;
        EmptySuccessResponse response = api.companiesCompanyIdPriceMarginsPriceMarginsIdDelete(companyId, priceMarginId, priceMarginsId);
        // TODO: test validations
    }

    /**
     * Get a list of company price margins
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdPriceMarginsPriceMarginsIdGetTest() throws ApiException {
        String companyId = null;
        String priceMarginsId = null;
        CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response response = api.companiesCompanyIdPriceMarginsPriceMarginsIdGet(companyId, priceMarginsId);
        // TODO: test validations
    }

    /**
     * Add a company price margin
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesCompanyIdPriceMarginsPriceMarginsIdPostTest() throws ApiException {
        String companyId = null;
        String priceMarginsId = null;
        CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest = null;
        CreateSuccessResponse response = api.companiesCompanyIdPriceMarginsPriceMarginsIdPost(companyId, priceMarginsId, companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest);
        // TODO: test validations
    }

    /**
     * Get a list of companies
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesGetTest() throws ApiException {
        CompaniesGet200Response response = api.companiesGet();
        // TODO: test validations
    }

    /**
     * URL for subscription selfservice
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void companiesSubscriptionSelfServiceGetTest() throws ApiException {
        CompaniesSubscriptionSelfServiceGet200Response response = api.companiesSubscriptionSelfServiceGet();
        // TODO: test validations
    }

}
