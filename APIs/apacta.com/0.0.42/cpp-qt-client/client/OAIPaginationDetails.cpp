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

#include "OAIPaginationDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaginationDetails::OAIPaginationDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaginationDetails::OAIPaginationDetails() {
    this->initializeModel();
}

OAIPaginationDetails::~OAIPaginationDetails() {}

void OAIPaginationDetails::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_current_page_isSet = false;
    m_current_page_isValid = false;

    m_has_next_page_isSet = false;
    m_has_next_page_isValid = false;

    m_has_prev_page_isSet = false;
    m_has_prev_page_isValid = false;

    m_limit_isSet = false;
    m_limit_isValid = false;

    m_page_count_isSet = false;
    m_page_count_isValid = false;
}

void OAIPaginationDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPaginationDetails::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_current_page_isValid = ::OpenAPI::fromJsonValue(m_current_page, json[QString("current_page")]);
    m_current_page_isSet = !json[QString("current_page")].isNull() && m_current_page_isValid;

    m_has_next_page_isValid = ::OpenAPI::fromJsonValue(m_has_next_page, json[QString("has_next_page")]);
    m_has_next_page_isSet = !json[QString("has_next_page")].isNull() && m_has_next_page_isValid;

    m_has_prev_page_isValid = ::OpenAPI::fromJsonValue(m_has_prev_page, json[QString("has_prev_page")]);
    m_has_prev_page_isSet = !json[QString("has_prev_page")].isNull() && m_has_prev_page_isValid;

    m_limit_isValid = ::OpenAPI::fromJsonValue(m_limit, json[QString("limit")]);
    m_limit_isSet = !json[QString("limit")].isNull() && m_limit_isValid;

    m_page_count_isValid = ::OpenAPI::fromJsonValue(m_page_count, json[QString("page_count")]);
    m_page_count_isSet = !json[QString("page_count")].isNull() && m_page_count_isValid;
}

QString OAIPaginationDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPaginationDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_current_page_isSet) {
        obj.insert(QString("current_page"), ::OpenAPI::toJsonValue(m_current_page));
    }
    if (m_has_next_page_isSet) {
        obj.insert(QString("has_next_page"), ::OpenAPI::toJsonValue(m_has_next_page));
    }
    if (m_has_prev_page_isSet) {
        obj.insert(QString("has_prev_page"), ::OpenAPI::toJsonValue(m_has_prev_page));
    }
    if (m_limit_isSet) {
        obj.insert(QString("limit"), ::OpenAPI::toJsonValue(m_limit));
    }
    if (m_page_count_isSet) {
        obj.insert(QString("page_count"), ::OpenAPI::toJsonValue(m_page_count));
    }
    return obj;
}

qint32 OAIPaginationDetails::getCount() const {
    return m_count;
}
void OAIPaginationDetails::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIPaginationDetails::is_count_Set() const{
    return m_count_isSet;
}

bool OAIPaginationDetails::is_count_Valid() const{
    return m_count_isValid;
}

QString OAIPaginationDetails::getCurrentPage() const {
    return m_current_page;
}
void OAIPaginationDetails::setCurrentPage(const QString &current_page) {
    m_current_page = current_page;
    m_current_page_isSet = true;
}

bool OAIPaginationDetails::is_current_page_Set() const{
    return m_current_page_isSet;
}

bool OAIPaginationDetails::is_current_page_Valid() const{
    return m_current_page_isValid;
}

bool OAIPaginationDetails::isHasNextPage() const {
    return m_has_next_page;
}
void OAIPaginationDetails::setHasNextPage(const bool &has_next_page) {
    m_has_next_page = has_next_page;
    m_has_next_page_isSet = true;
}

bool OAIPaginationDetails::is_has_next_page_Set() const{
    return m_has_next_page_isSet;
}

bool OAIPaginationDetails::is_has_next_page_Valid() const{
    return m_has_next_page_isValid;
}

bool OAIPaginationDetails::isHasPrevPage() const {
    return m_has_prev_page;
}
void OAIPaginationDetails::setHasPrevPage(const bool &has_prev_page) {
    m_has_prev_page = has_prev_page;
    m_has_prev_page_isSet = true;
}

bool OAIPaginationDetails::is_has_prev_page_Set() const{
    return m_has_prev_page_isSet;
}

bool OAIPaginationDetails::is_has_prev_page_Valid() const{
    return m_has_prev_page_isValid;
}

qint32 OAIPaginationDetails::getLimit() const {
    return m_limit;
}
void OAIPaginationDetails::setLimit(const qint32 &limit) {
    m_limit = limit;
    m_limit_isSet = true;
}

bool OAIPaginationDetails::is_limit_Set() const{
    return m_limit_isSet;
}

bool OAIPaginationDetails::is_limit_Valid() const{
    return m_limit_isValid;
}

QString OAIPaginationDetails::getPageCount() const {
    return m_page_count;
}
void OAIPaginationDetails::setPageCount(const QString &page_count) {
    m_page_count = page_count;
    m_page_count_isSet = true;
}

bool OAIPaginationDetails::is_page_count_Set() const{
    return m_page_count_isSet;
}

bool OAIPaginationDetails::is_page_count_Valid() const{
    return m_page_count_isValid;
}

bool OAIPaginationDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_current_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_next_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_prev_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPaginationDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
