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
import java.time.LocalDate;
import java.util.Arrays;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for Invoice
 */
public class InvoiceTest {
    private final Invoice model = new Invoice();

    /**
     * Model tests for Invoice
     */
    @Test
    public void testInvoice() {
        // TODO: test Invoice
    }

    /**
     * Test the property 'allProductsOneLine'
     */
    @Test
    public void allProductsOneLineTest() {
        // TODO: test allProductsOneLine
    }

    /**
     * Test the property 'allWorkingHoursOneLine'
     */
    @Test
    public void allWorkingHoursOneLineTest() {
        // TODO: test allWorkingHoursOneLine
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
     * Test the property 'currencyId'
     */
    @Test
    public void currencyIdTest() {
        // TODO: test currencyId
    }

    /**
     * Test the property 'dateFrom'
     */
    @Test
    public void dateFromTest() {
        // TODO: test dateFrom
    }

    /**
     * Test the property 'dateTo'
     */
    @Test
    public void dateToTest() {
        // TODO: test dateTo
    }

    /**
     * Test the property 'deleted'
     */
    @Test
    public void deletedTest() {
        // TODO: test deleted
    }

    /**
     * Test the property 'downloaded'
     */
    @Test
    public void downloadedTest() {
        // TODO: test downloaded
    }

    /**
     * Test the property 'erpId'
     */
    @Test
    public void erpIdTest() {
        // TODO: test erpId
    }

    /**
     * Test the property 'erpPaymentTermId'
     */
    @Test
    public void erpPaymentTermIdTest() {
        // TODO: test erpPaymentTermId
    }

    /**
     * Test the property 'euCustomer'
     */
    @Test
    public void euCustomerTest() {
        // TODO: test euCustomer
    }

    /**
     * Test the property 'grossPayment'
     */
    @Test
    public void grossPaymentTest() {
        // TODO: test grossPayment
    }

    /**
     * Test the property 'groupByForms'
     */
    @Test
    public void groupByFormsTest() {
        // TODO: test groupByForms
    }

    /**
     * Test the property 'id'
     */
    @Test
    public void idTest() {
        // TODO: test id
    }

    /**
     * Test the property 'includeInvoicedLines'
     */
    @Test
    public void includeInvoicedLinesTest() {
        // TODO: test includeInvoicedLines
    }

    /**
     * Test the property 'integrationId'
     */
    @Test
    public void integrationIdTest() {
        // TODO: test integrationId
    }

    /**
     * Test the property 'invoiceNumber'
     */
    @Test
    public void invoiceNumberTest() {
        // TODO: test invoiceNumber
    }

    /**
     * Test the property 'isDraft'
     */
    @Test
    public void isDraftTest() {
        // TODO: test isDraft
    }

    /**
     * Test the property 'isFinalInvoice'
     */
    @Test
    public void isFinalInvoiceTest() {
        // TODO: test isFinalInvoice
    }

    /**
     * Test the property 'isLocked'
     */
    @Test
    public void isLockedTest() {
        // TODO: test isLocked
    }

    /**
     * Test the property 'isOffer'
     */
    @Test
    public void isOfferTest() {
        // TODO: test isOffer
    }

    /**
     * Test the property 'issuedDate'
     */
    @Test
    public void issuedDateTest() {
        // TODO: test issuedDate
    }

    /**
     * Test the property 'message'
     */
    @Test
    public void messageTest() {
        // TODO: test message
    }

    /**
     * Test the property 'modified'
     */
    @Test
    public void modifiedTest() {
        // TODO: test modified
    }

    /**
     * Test the property 'netPayment'
     */
    @Test
    public void netPaymentTest() {
        // TODO: test netPayment
    }

    /**
     * Test the property 'offerNumber'
     */
    @Test
    public void offerNumberTest() {
        // TODO: test offerNumber
    }

    /**
     * Test the property 'orderLineGroupId'
     */
    @Test
    public void orderLineGroupIdTest() {
        // TODO: test orderLineGroupId
    }

    /**
     * Test the property 'paymentDueDate'
     */
    @Test
    public void paymentDueDateTest() {
        // TODO: test paymentDueDate
    }

    /**
     * Test the property 'paymentTermId'
     */
    @Test
    public void paymentTermIdTest() {
        // TODO: test paymentTermId
    }

    /**
     * Test the property 'projectId'
     */
    @Test
    public void projectIdTest() {
        // TODO: test projectId
    }

    /**
     * Test the property 'projectOverviewAttached'
     */
    @Test
    public void projectOverviewAttachedTest() {
        // TODO: test projectOverviewAttached
    }

    /**
     * Test the property 'reference'
     */
    @Test
    public void referenceTest() {
        // TODO: test reference
    }

    /**
     * Test the property 'showEmployeeName'
     */
    @Test
    public void showEmployeeNameTest() {
        // TODO: test showEmployeeName
    }

    /**
     * Test the property 'showPriceProductBundle'
     */
    @Test
    public void showPriceProductBundleTest() {
        // TODO: test showPriceProductBundle
    }

    /**
     * Test the property 'showPricesProductsAndHours'
     */
    @Test
    public void showPricesProductsAndHoursTest() {
        // TODO: test showPricesProductsAndHours
    }

    /**
     * Test the property 'showProductImages'
     */
    @Test
    public void showProductImagesTest() {
        // TODO: test showProductImages
    }

    /**
     * Test the property 'showProductsProductBundle'
     */
    @Test
    public void showProductsProductBundleTest() {
        // TODO: test showProductsProductBundle
    }

    /**
     * Test the property 'title'
     */
    @Test
    public void titleTest() {
        // TODO: test title
    }

    /**
     * Test the property 'totalCostPrice'
     */
    @Test
    public void totalCostPriceTest() {
        // TODO: test totalCostPrice
    }

    /**
     * Test the property 'totalDiscountPercent'
     */
    @Test
    public void totalDiscountPercentTest() {
        // TODO: test totalDiscountPercent
    }

    /**
     * Test the property 'vatPercent'
     */
    @Test
    public void vatPercentTest() {
        // TODO: test vatPercent
    }

    /**
     * Test the property 'vendorId'
     */
    @Test
    public void vendorIdTest() {
        // TODO: test vendorId
    }

}
