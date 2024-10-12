/**
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetFinancialStatistics_200_response_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetFinancialStatistics_200_response_data::OAIGetFinancialStatistics_200_response_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetFinancialStatistics_200_response_data::OAIGetFinancialStatistics_200_response_data() {
    this->initializeModel();
}

OAIGetFinancialStatistics_200_response_data::~OAIGetFinancialStatistics_200_response_data() {}

void OAIGetFinancialStatistics_200_response_data::initializeModel() {

    m_invoiced_amount_isSet = false;
    m_invoiced_amount_isValid = false;

    m_invoiced_working_hours_isSet = false;
    m_invoiced_working_hours_isValid = false;

    m_not_invoiced_amount_isSet = false;
    m_not_invoiced_amount_isValid = false;

    m_not_invoiced_working_hours_isSet = false;
    m_not_invoiced_working_hours_isValid = false;

    m_products_costs_isSet = false;
    m_products_costs_isValid = false;

    m_products_sales_isSet = false;
    m_products_sales_isValid = false;

    m_rentals_costs_isSet = false;
    m_rentals_costs_isValid = false;

    m_rentals_sales_isSet = false;
    m_rentals_sales_isValid = false;

    m_total_costs_isSet = false;
    m_total_costs_isValid = false;

    m_total_sales_isSet = false;
    m_total_sales_isValid = false;

    m_work_time_costs_isSet = false;
    m_work_time_costs_isValid = false;

    m_work_time_sales_isSet = false;
    m_work_time_sales_isValid = false;
}

void OAIGetFinancialStatistics_200_response_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetFinancialStatistics_200_response_data::fromJsonObject(QJsonObject json) {

    m_invoiced_amount_isValid = ::OpenAPI::fromJsonValue(m_invoiced_amount, json[QString("invoicedAmount")]);
    m_invoiced_amount_isSet = !json[QString("invoicedAmount")].isNull() && m_invoiced_amount_isValid;

    m_invoiced_working_hours_isValid = ::OpenAPI::fromJsonValue(m_invoiced_working_hours, json[QString("invoicedWorkingHours")]);
    m_invoiced_working_hours_isSet = !json[QString("invoicedWorkingHours")].isNull() && m_invoiced_working_hours_isValid;

    m_not_invoiced_amount_isValid = ::OpenAPI::fromJsonValue(m_not_invoiced_amount, json[QString("notInvoicedAmount")]);
    m_not_invoiced_amount_isSet = !json[QString("notInvoicedAmount")].isNull() && m_not_invoiced_amount_isValid;

    m_not_invoiced_working_hours_isValid = ::OpenAPI::fromJsonValue(m_not_invoiced_working_hours, json[QString("notInvoicedWorkingHours")]);
    m_not_invoiced_working_hours_isSet = !json[QString("notInvoicedWorkingHours")].isNull() && m_not_invoiced_working_hours_isValid;

    m_products_costs_isValid = ::OpenAPI::fromJsonValue(m_products_costs, json[QString("productsCosts")]);
    m_products_costs_isSet = !json[QString("productsCosts")].isNull() && m_products_costs_isValid;

    m_products_sales_isValid = ::OpenAPI::fromJsonValue(m_products_sales, json[QString("productsSales")]);
    m_products_sales_isSet = !json[QString("productsSales")].isNull() && m_products_sales_isValid;

    m_rentals_costs_isValid = ::OpenAPI::fromJsonValue(m_rentals_costs, json[QString("rentalsCosts")]);
    m_rentals_costs_isSet = !json[QString("rentalsCosts")].isNull() && m_rentals_costs_isValid;

    m_rentals_sales_isValid = ::OpenAPI::fromJsonValue(m_rentals_sales, json[QString("rentalsSales")]);
    m_rentals_sales_isSet = !json[QString("rentalsSales")].isNull() && m_rentals_sales_isValid;

    m_total_costs_isValid = ::OpenAPI::fromJsonValue(m_total_costs, json[QString("totalCosts")]);
    m_total_costs_isSet = !json[QString("totalCosts")].isNull() && m_total_costs_isValid;

    m_total_sales_isValid = ::OpenAPI::fromJsonValue(m_total_sales, json[QString("totalSales")]);
    m_total_sales_isSet = !json[QString("totalSales")].isNull() && m_total_sales_isValid;

    m_work_time_costs_isValid = ::OpenAPI::fromJsonValue(m_work_time_costs, json[QString("workTimeCosts")]);
    m_work_time_costs_isSet = !json[QString("workTimeCosts")].isNull() && m_work_time_costs_isValid;

    m_work_time_sales_isValid = ::OpenAPI::fromJsonValue(m_work_time_sales, json[QString("workTimeSales")]);
    m_work_time_sales_isSet = !json[QString("workTimeSales")].isNull() && m_work_time_sales_isValid;
}

QString OAIGetFinancialStatistics_200_response_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetFinancialStatistics_200_response_data::asJsonObject() const {
    QJsonObject obj;
    if (m_invoiced_amount_isSet) {
        obj.insert(QString("invoicedAmount"), ::OpenAPI::toJsonValue(m_invoiced_amount));
    }
    if (m_invoiced_working_hours_isSet) {
        obj.insert(QString("invoicedWorkingHours"), ::OpenAPI::toJsonValue(m_invoiced_working_hours));
    }
    if (m_not_invoiced_amount_isSet) {
        obj.insert(QString("notInvoicedAmount"), ::OpenAPI::toJsonValue(m_not_invoiced_amount));
    }
    if (m_not_invoiced_working_hours_isSet) {
        obj.insert(QString("notInvoicedWorkingHours"), ::OpenAPI::toJsonValue(m_not_invoiced_working_hours));
    }
    if (m_products_costs_isSet) {
        obj.insert(QString("productsCosts"), ::OpenAPI::toJsonValue(m_products_costs));
    }
    if (m_products_sales_isSet) {
        obj.insert(QString("productsSales"), ::OpenAPI::toJsonValue(m_products_sales));
    }
    if (m_rentals_costs_isSet) {
        obj.insert(QString("rentalsCosts"), ::OpenAPI::toJsonValue(m_rentals_costs));
    }
    if (m_rentals_sales_isSet) {
        obj.insert(QString("rentalsSales"), ::OpenAPI::toJsonValue(m_rentals_sales));
    }
    if (m_total_costs_isSet) {
        obj.insert(QString("totalCosts"), ::OpenAPI::toJsonValue(m_total_costs));
    }
    if (m_total_sales_isSet) {
        obj.insert(QString("totalSales"), ::OpenAPI::toJsonValue(m_total_sales));
    }
    if (m_work_time_costs_isSet) {
        obj.insert(QString("workTimeCosts"), ::OpenAPI::toJsonValue(m_work_time_costs));
    }
    if (m_work_time_sales_isSet) {
        obj.insert(QString("workTimeSales"), ::OpenAPI::toJsonValue(m_work_time_sales));
    }
    return obj;
}

float OAIGetFinancialStatistics_200_response_data::getInvoicedAmount() const {
    return m_invoiced_amount;
}
void OAIGetFinancialStatistics_200_response_data::setInvoicedAmount(const float &invoiced_amount) {
    m_invoiced_amount = invoiced_amount;
    m_invoiced_amount_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_invoiced_amount_Set() const{
    return m_invoiced_amount_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_invoiced_amount_Valid() const{
    return m_invoiced_amount_isValid;
}

QString OAIGetFinancialStatistics_200_response_data::getInvoicedWorkingHours() const {
    return m_invoiced_working_hours;
}
void OAIGetFinancialStatistics_200_response_data::setInvoicedWorkingHours(const QString &invoiced_working_hours) {
    m_invoiced_working_hours = invoiced_working_hours;
    m_invoiced_working_hours_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_invoiced_working_hours_Set() const{
    return m_invoiced_working_hours_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_invoiced_working_hours_Valid() const{
    return m_invoiced_working_hours_isValid;
}

float OAIGetFinancialStatistics_200_response_data::getNotInvoicedAmount() const {
    return m_not_invoiced_amount;
}
void OAIGetFinancialStatistics_200_response_data::setNotInvoicedAmount(const float &not_invoiced_amount) {
    m_not_invoiced_amount = not_invoiced_amount;
    m_not_invoiced_amount_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_not_invoiced_amount_Set() const{
    return m_not_invoiced_amount_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_not_invoiced_amount_Valid() const{
    return m_not_invoiced_amount_isValid;
}

QString OAIGetFinancialStatistics_200_response_data::getNotInvoicedWorkingHours() const {
    return m_not_invoiced_working_hours;
}
void OAIGetFinancialStatistics_200_response_data::setNotInvoicedWorkingHours(const QString &not_invoiced_working_hours) {
    m_not_invoiced_working_hours = not_invoiced_working_hours;
    m_not_invoiced_working_hours_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_not_invoiced_working_hours_Set() const{
    return m_not_invoiced_working_hours_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_not_invoiced_working_hours_Valid() const{
    return m_not_invoiced_working_hours_isValid;
}

float OAIGetFinancialStatistics_200_response_data::getProductsCosts() const {
    return m_products_costs;
}
void OAIGetFinancialStatistics_200_response_data::setProductsCosts(const float &products_costs) {
    m_products_costs = products_costs;
    m_products_costs_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_products_costs_Set() const{
    return m_products_costs_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_products_costs_Valid() const{
    return m_products_costs_isValid;
}

float OAIGetFinancialStatistics_200_response_data::getProductsSales() const {
    return m_products_sales;
}
void OAIGetFinancialStatistics_200_response_data::setProductsSales(const float &products_sales) {
    m_products_sales = products_sales;
    m_products_sales_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_products_sales_Set() const{
    return m_products_sales_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_products_sales_Valid() const{
    return m_products_sales_isValid;
}

float OAIGetFinancialStatistics_200_response_data::getRentalsCosts() const {
    return m_rentals_costs;
}
void OAIGetFinancialStatistics_200_response_data::setRentalsCosts(const float &rentals_costs) {
    m_rentals_costs = rentals_costs;
    m_rentals_costs_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_rentals_costs_Set() const{
    return m_rentals_costs_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_rentals_costs_Valid() const{
    return m_rentals_costs_isValid;
}

float OAIGetFinancialStatistics_200_response_data::getRentalsSales() const {
    return m_rentals_sales;
}
void OAIGetFinancialStatistics_200_response_data::setRentalsSales(const float &rentals_sales) {
    m_rentals_sales = rentals_sales;
    m_rentals_sales_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_rentals_sales_Set() const{
    return m_rentals_sales_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_rentals_sales_Valid() const{
    return m_rentals_sales_isValid;
}

float OAIGetFinancialStatistics_200_response_data::getTotalCosts() const {
    return m_total_costs;
}
void OAIGetFinancialStatistics_200_response_data::setTotalCosts(const float &total_costs) {
    m_total_costs = total_costs;
    m_total_costs_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_total_costs_Set() const{
    return m_total_costs_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_total_costs_Valid() const{
    return m_total_costs_isValid;
}

float OAIGetFinancialStatistics_200_response_data::getTotalSales() const {
    return m_total_sales;
}
void OAIGetFinancialStatistics_200_response_data::setTotalSales(const float &total_sales) {
    m_total_sales = total_sales;
    m_total_sales_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_total_sales_Set() const{
    return m_total_sales_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_total_sales_Valid() const{
    return m_total_sales_isValid;
}

float OAIGetFinancialStatistics_200_response_data::getWorkTimeCosts() const {
    return m_work_time_costs;
}
void OAIGetFinancialStatistics_200_response_data::setWorkTimeCosts(const float &work_time_costs) {
    m_work_time_costs = work_time_costs;
    m_work_time_costs_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_work_time_costs_Set() const{
    return m_work_time_costs_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_work_time_costs_Valid() const{
    return m_work_time_costs_isValid;
}

float OAIGetFinancialStatistics_200_response_data::getWorkTimeSales() const {
    return m_work_time_sales;
}
void OAIGetFinancialStatistics_200_response_data::setWorkTimeSales(const float &work_time_sales) {
    m_work_time_sales = work_time_sales;
    m_work_time_sales_isSet = true;
}

bool OAIGetFinancialStatistics_200_response_data::is_work_time_sales_Set() const{
    return m_work_time_sales_isSet;
}

bool OAIGetFinancialStatistics_200_response_data::is_work_time_sales_Valid() const{
    return m_work_time_sales_isValid;
}

bool OAIGetFinancialStatistics_200_response_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_invoiced_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoiced_working_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_not_invoiced_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_not_invoiced_working_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_products_costs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_products_sales_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rentals_costs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rentals_sales_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_costs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_sales_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_time_costs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_time_sales_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetFinancialStatistics_200_response_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
