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


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.Arrays;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for Project
 */
public class ProjectTest {
    private final Project model = new Project();

    /**
     * Model tests for Project
     */
    @Test
    public void testProject() {
        // TODO: test Project
    }

    /**
     * Test the property 'cityId'
     */
    @Test
    public void cityIdTest() {
        // TODO: test cityId
    }

    /**
     * Test the property 'companyId'
     */
    @Test
    public void companyIdTest() {
        // TODO: test companyId
    }

    /**
     * Test the property 'contactId'
     */
    @Test
    public void contactIdTest() {
        // TODO: test contactId
    }

    /**
     * Test the property 'created'
     */
    @Test
    public void createdTest() {
        // TODO: test created
    }

    /**
     * Test the property 'createdById'
     */
    @Test
    public void createdByIdTest() {
        // TODO: test createdById
    }

    /**
     * Test the property 'deleted'
     */
    @Test
    public void deletedTest() {
        // TODO: test deleted
    }

    /**
     * Test the property 'description'
     */
    @Test
    public void descriptionTest() {
        // TODO: test description
    }

    /**
     * Test the property 'endTime'
     */
    @Test
    public void endTimeTest() {
        // TODO: test endTime
    }

    /**
     * Test the property 'erpProjectId'
     */
    @Test
    public void erpProjectIdTest() {
        // TODO: test erpProjectId
    }

    /**
     * Test the property 'erpTaskId'
     */
    @Test
    public void erpTaskIdTest() {
        // TODO: test erpTaskId
    }

    /**
     * Test the property 'fullName'
     */
    @Test
    public void fullNameTest() {
        // TODO: test fullName
    }

    /**
     * Test the property 'hasFinalInvoice'
     */
    @Test
    public void hasFinalInvoiceTest() {
        // TODO: test hasFinalInvoice
    }

    /**
     * Test the property 'id'
     */
    @Test
    public void idTest() {
        // TODO: test id
    }

    /**
     * Test the property 'isFixedPrice'
     */
    @Test
    public void isFixedPriceTest() {
        // TODO: test isFixedPrice
    }

    /**
     * Test the property 'isOffer'
     */
    @Test
    public void isOfferTest() {
        // TODO: test isOffer
    }

    /**
     * Test the property 'isRotten'
     */
    @Test
    public void isRottenTest() {
        // TODO: test isRotten
    }

    /**
     * Test the property 'latitude'
     */
    @Test
    public void latitudeTest() {
        // TODO: test latitude
    }

    /**
     * Test the property 'longitude'
     */
    @Test
    public void longitudeTest() {
        // TODO: test longitude
    }

    /**
     * Test the property 'modified'
     */
    @Test
    public void modifiedTest() {
        // TODO: test modified
    }

    /**
     * Test the property 'name'
     */
    @Test
    public void nameTest() {
        // TODO: test name
    }

    /**
     * Test the property 'notInvoicedAmount'
     */
    @Test
    public void notInvoicedAmountTest() {
        // TODO: test notInvoicedAmount
    }

    /**
     * Test the property 'offerId'
     */
    @Test
    public void offerIdTest() {
        // TODO: test offerId
    }

    /**
     * Test the property 'parentId'
     */
    @Test
    public void parentIdTest() {
        // TODO: test parentId
    }

    /**
     * Test the property 'preCalculationId'
     */
    @Test
    public void preCalculationIdTest() {
        // TODO: test preCalculationId
    }

    /**
     * Test the property 'productsTotalCostPrice'
     */
    @Test
    public void productsTotalCostPriceTest() {
        // TODO: test productsTotalCostPrice
    }

    /**
     * Test the property 'projectImageUrl'
     */
    @Test
    public void projectImageUrlTest() {
        // TODO: test projectImageUrl
    }

    /**
     * Test the property 'projectNumber'
     */
    @Test
    public void projectNumberTest() {
        // TODO: test projectNumber
    }

    /**
     * Test the property 'projectStatusId'
     */
    @Test
    public void projectStatusIdTest() {
        // TODO: test projectStatusId
    }

    /**
     * Test the property 'sharedProjectId'
     */
    @Test
    public void sharedProjectIdTest() {
        // TODO: test sharedProjectId
    }

    /**
     * Test the property 'startTime'
     */
    @Test
    public void startTimeTest() {
        // TODO: test startTime
    }

    /**
     * Test the property 'streetName'
     */
    @Test
    public void streetNameTest() {
        // TODO: test streetName
    }

    /**
     * Test the property 'thumbnail'
     */
    @Test
    public void thumbnailTest() {
        // TODO: test thumbnail
    }

    /**
     * Test the property 'totalSalesPrice'
     */
    @Test
    public void totalSalesPriceTest() {
        // TODO: test totalSalesPrice
    }

    /**
     * Test the property 'workingHoursTotalCostPrice'
     */
    @Test
    public void workingHoursTotalCostPriceTest() {
        // TODO: test workingHoursTotalCostPrice
    }

}
