/**
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.Apacta);
  }
}(this, function(expect, Apacta) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Apacta.Project();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('Project', function() {
    it('should create an instance of Project', function() {
      // uncomment below and update the code to test Project
      //var instance = new Apacta.Project();
      //expect(instance).to.be.a(Apacta.Project);
    });

    it('should have the property cityId (base name: "city_id")', function() {
      // uncomment below and update the code to test the property cityId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property companyId (base name: "company_id")', function() {
      // uncomment below and update the code to test the property companyId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property contactId (base name: "contact_id")', function() {
      // uncomment below and update the code to test the property contactId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property created (base name: "created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property createdById (base name: "created_by_id")', function() {
      // uncomment below and update the code to test the property createdById
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property deleted (base name: "deleted")', function() {
      // uncomment below and update the code to test the property deleted
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property endTime (base name: "end_time")', function() {
      // uncomment below and update the code to test the property endTime
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property erpProjectId (base name: "erp_project_id")', function() {
      // uncomment below and update the code to test the property erpProjectId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property erpTaskId (base name: "erp_task_id")', function() {
      // uncomment below and update the code to test the property erpTaskId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property fullName (base name: "full_name")', function() {
      // uncomment below and update the code to test the property fullName
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property hasFinalInvoice (base name: "has_final_invoice")', function() {
      // uncomment below and update the code to test the property hasFinalInvoice
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property isFixedPrice (base name: "is_fixed_price")', function() {
      // uncomment below and update the code to test the property isFixedPrice
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property isOffer (base name: "is_offer")', function() {
      // uncomment below and update the code to test the property isOffer
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property isRotten (base name: "is_rotten")', function() {
      // uncomment below and update the code to test the property isRotten
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property latitude (base name: "latitude")', function() {
      // uncomment below and update the code to test the property latitude
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property longitude (base name: "longitude")', function() {
      // uncomment below and update the code to test the property longitude
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property modified (base name: "modified")', function() {
      // uncomment below and update the code to test the property modified
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property notInvoicedAmount (base name: "not_invoiced_amount")', function() {
      // uncomment below and update the code to test the property notInvoicedAmount
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property offerId (base name: "offer_id")', function() {
      // uncomment below and update the code to test the property offerId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property parentId (base name: "parent_id")', function() {
      // uncomment below and update the code to test the property parentId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property preCalculationId (base name: "pre_calculation_id")', function() {
      // uncomment below and update the code to test the property preCalculationId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property productsTotalCostPrice (base name: "products_total_cost_price")', function() {
      // uncomment below and update the code to test the property productsTotalCostPrice
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property projectImageUrl (base name: "project_image_url")', function() {
      // uncomment below and update the code to test the property projectImageUrl
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property projectNumber (base name: "project_number")', function() {
      // uncomment below and update the code to test the property projectNumber
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property projectStatusId (base name: "project_status_id")', function() {
      // uncomment below and update the code to test the property projectStatusId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property sharedProjectId (base name: "shared_project_id")', function() {
      // uncomment below and update the code to test the property sharedProjectId
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property startTime (base name: "start_time")', function() {
      // uncomment below and update the code to test the property startTime
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property streetName (base name: "street_name")', function() {
      // uncomment below and update the code to test the property streetName
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property thumbnail (base name: "thumbnail")', function() {
      // uncomment below and update the code to test the property thumbnail
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property totalSalesPrice (base name: "total_sales_price")', function() {
      // uncomment below and update the code to test the property totalSalesPrice
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

    it('should have the property workingHoursTotalCostPrice (base name: "working_hours_total_cost_price")', function() {
      // uncomment below and update the code to test the property workingHoursTotalCostPrice
      //var instance = new Apacta.Project();
      //expect(instance).to.be();
    });

  });

}));
