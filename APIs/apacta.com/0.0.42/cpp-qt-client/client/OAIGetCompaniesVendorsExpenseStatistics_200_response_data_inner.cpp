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

#include "OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner() {
    this->initializeModel();
}

OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::~OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner() {}

void OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::initializeModel() {

    m_last_month_isSet = false;
    m_last_month_isValid = false;

    m_thirty_days_isSet = false;
    m_thirty_days_isValid = false;

    m_vendor_id_isSet = false;
    m_vendor_id_isValid = false;
}

void OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::fromJsonObject(QJsonObject json) {

    m_last_month_isValid = ::OpenAPI::fromJsonValue(m_last_month, json[QString("last_month")]);
    m_last_month_isSet = !json[QString("last_month")].isNull() && m_last_month_isValid;

    m_thirty_days_isValid = ::OpenAPI::fromJsonValue(m_thirty_days, json[QString("thirty_days")]);
    m_thirty_days_isSet = !json[QString("thirty_days")].isNull() && m_thirty_days_isValid;

    m_vendor_id_isValid = ::OpenAPI::fromJsonValue(m_vendor_id, json[QString("vendor_id")]);
    m_vendor_id_isSet = !json[QString("vendor_id")].isNull() && m_vendor_id_isValid;
}

QString OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_last_month.size() > 0) {
        obj.insert(QString("last_month"), ::OpenAPI::toJsonValue(m_last_month));
    }
    if (m_thirty_days.size() > 0) {
        obj.insert(QString("thirty_days"), ::OpenAPI::toJsonValue(m_thirty_days));
    }
    if (m_vendor_id_isSet) {
        obj.insert(QString("vendor_id"), ::OpenAPI::toJsonValue(m_vendor_id));
    }
    return obj;
}

QList<OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner_last_month_inner> OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::getLastMonth() const {
    return m_last_month;
}
void OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::setLastMonth(const QList<OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner_last_month_inner> &last_month) {
    m_last_month = last_month;
    m_last_month_isSet = true;
}

bool OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::is_last_month_Set() const{
    return m_last_month_isSet;
}

bool OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::is_last_month_Valid() const{
    return m_last_month_isValid;
}

QList<OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner_last_month_inner> OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::getThirtyDays() const {
    return m_thirty_days;
}
void OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::setThirtyDays(const QList<OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner_last_month_inner> &thirty_days) {
    m_thirty_days = thirty_days;
    m_thirty_days_isSet = true;
}

bool OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::is_thirty_days_Set() const{
    return m_thirty_days_isSet;
}

bool OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::is_thirty_days_Valid() const{
    return m_thirty_days_isValid;
}

QString OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::getVendorId() const {
    return m_vendor_id;
}
void OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::setVendorId(const QString &vendor_id) {
    m_vendor_id = vendor_id;
    m_vendor_id_isSet = true;
}

bool OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::is_vendor_id_Set() const{
    return m_vendor_id_isSet;
}

bool OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::is_vendor_id_Valid() const{
    return m_vendor_id_isValid;
}

bool OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_last_month.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_thirty_days.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetCompaniesVendorsExpenseStatistics_200_response_data_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
