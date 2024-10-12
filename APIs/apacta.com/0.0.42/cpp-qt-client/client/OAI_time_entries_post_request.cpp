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

#include "OAI_time_entries_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_time_entries_post_request::OAI_time_entries_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_time_entries_post_request::OAI_time_entries_post_request() {
    this->initializeModel();
}

OAI_time_entries_post_request::~OAI_time_entries_post_request() {}

void OAI_time_entries_post_request::initializeModel() {

    m_form_id_isSet = false;
    m_form_id_isValid = false;

    m_from_time_isSet = false;
    m_from_time_isValid = false;

    m_is_all_day_isSet = false;
    m_is_all_day_isValid = false;

    m_project_id_isSet = false;
    m_project_id_isValid = false;

    m_sum_isSet = false;
    m_sum_isValid = false;

    m_time_entry_type_id_isSet = false;
    m_time_entry_type_id_isValid = false;

    m_to_time_isSet = false;
    m_to_time_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAI_time_entries_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_time_entries_post_request::fromJsonObject(QJsonObject json) {

    m_form_id_isValid = ::OpenAPI::fromJsonValue(m_form_id, json[QString("form_id")]);
    m_form_id_isSet = !json[QString("form_id")].isNull() && m_form_id_isValid;

    m_from_time_isValid = ::OpenAPI::fromJsonValue(m_from_time, json[QString("from_time")]);
    m_from_time_isSet = !json[QString("from_time")].isNull() && m_from_time_isValid;

    m_is_all_day_isValid = ::OpenAPI::fromJsonValue(m_is_all_day, json[QString("is_all_day")]);
    m_is_all_day_isSet = !json[QString("is_all_day")].isNull() && m_is_all_day_isValid;

    m_project_id_isValid = ::OpenAPI::fromJsonValue(m_project_id, json[QString("project_id")]);
    m_project_id_isSet = !json[QString("project_id")].isNull() && m_project_id_isValid;

    m_sum_isValid = ::OpenAPI::fromJsonValue(m_sum, json[QString("sum")]);
    m_sum_isSet = !json[QString("sum")].isNull() && m_sum_isValid;

    m_time_entry_type_id_isValid = ::OpenAPI::fromJsonValue(m_time_entry_type_id, json[QString("time_entry_type_id")]);
    m_time_entry_type_id_isSet = !json[QString("time_entry_type_id")].isNull() && m_time_entry_type_id_isValid;

    m_to_time_isValid = ::OpenAPI::fromJsonValue(m_to_time, json[QString("to_time")]);
    m_to_time_isSet = !json[QString("to_time")].isNull() && m_to_time_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;
}

QString OAI_time_entries_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_time_entries_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_form_id_isSet) {
        obj.insert(QString("form_id"), ::OpenAPI::toJsonValue(m_form_id));
    }
    if (m_from_time_isSet) {
        obj.insert(QString("from_time"), ::OpenAPI::toJsonValue(m_from_time));
    }
    if (m_is_all_day_isSet) {
        obj.insert(QString("is_all_day"), ::OpenAPI::toJsonValue(m_is_all_day));
    }
    if (m_project_id_isSet) {
        obj.insert(QString("project_id"), ::OpenAPI::toJsonValue(m_project_id));
    }
    if (m_sum_isSet) {
        obj.insert(QString("sum"), ::OpenAPI::toJsonValue(m_sum));
    }
    if (m_time_entry_type_id_isSet) {
        obj.insert(QString("time_entry_type_id"), ::OpenAPI::toJsonValue(m_time_entry_type_id));
    }
    if (m_to_time_isSet) {
        obj.insert(QString("to_time"), ::OpenAPI::toJsonValue(m_to_time));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAI_time_entries_post_request::getFormId() const {
    return m_form_id;
}
void OAI_time_entries_post_request::setFormId(const QString &form_id) {
    m_form_id = form_id;
    m_form_id_isSet = true;
}

bool OAI_time_entries_post_request::is_form_id_Set() const{
    return m_form_id_isSet;
}

bool OAI_time_entries_post_request::is_form_id_Valid() const{
    return m_form_id_isValid;
}

QString OAI_time_entries_post_request::getFromTime() const {
    return m_from_time;
}
void OAI_time_entries_post_request::setFromTime(const QString &from_time) {
    m_from_time = from_time;
    m_from_time_isSet = true;
}

bool OAI_time_entries_post_request::is_from_time_Set() const{
    return m_from_time_isSet;
}

bool OAI_time_entries_post_request::is_from_time_Valid() const{
    return m_from_time_isValid;
}

bool OAI_time_entries_post_request::isIsAllDay() const {
    return m_is_all_day;
}
void OAI_time_entries_post_request::setIsAllDay(const bool &is_all_day) {
    m_is_all_day = is_all_day;
    m_is_all_day_isSet = true;
}

bool OAI_time_entries_post_request::is_is_all_day_Set() const{
    return m_is_all_day_isSet;
}

bool OAI_time_entries_post_request::is_is_all_day_Valid() const{
    return m_is_all_day_isValid;
}

QString OAI_time_entries_post_request::getProjectId() const {
    return m_project_id;
}
void OAI_time_entries_post_request::setProjectId(const QString &project_id) {
    m_project_id = project_id;
    m_project_id_isSet = true;
}

bool OAI_time_entries_post_request::is_project_id_Set() const{
    return m_project_id_isSet;
}

bool OAI_time_entries_post_request::is_project_id_Valid() const{
    return m_project_id_isValid;
}

qint32 OAI_time_entries_post_request::getSum() const {
    return m_sum;
}
void OAI_time_entries_post_request::setSum(const qint32 &sum) {
    m_sum = sum;
    m_sum_isSet = true;
}

bool OAI_time_entries_post_request::is_sum_Set() const{
    return m_sum_isSet;
}

bool OAI_time_entries_post_request::is_sum_Valid() const{
    return m_sum_isValid;
}

QString OAI_time_entries_post_request::getTimeEntryTypeId() const {
    return m_time_entry_type_id;
}
void OAI_time_entries_post_request::setTimeEntryTypeId(const QString &time_entry_type_id) {
    m_time_entry_type_id = time_entry_type_id;
    m_time_entry_type_id_isSet = true;
}

bool OAI_time_entries_post_request::is_time_entry_type_id_Set() const{
    return m_time_entry_type_id_isSet;
}

bool OAI_time_entries_post_request::is_time_entry_type_id_Valid() const{
    return m_time_entry_type_id_isValid;
}

QString OAI_time_entries_post_request::getToTime() const {
    return m_to_time;
}
void OAI_time_entries_post_request::setToTime(const QString &to_time) {
    m_to_time = to_time;
    m_to_time_isSet = true;
}

bool OAI_time_entries_post_request::is_to_time_Set() const{
    return m_to_time_isSet;
}

bool OAI_time_entries_post_request::is_to_time_Valid() const{
    return m_to_time_isValid;
}

QString OAI_time_entries_post_request::getUserId() const {
    return m_user_id;
}
void OAI_time_entries_post_request::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAI_time_entries_post_request::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAI_time_entries_post_request::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAI_time_entries_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_form_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_from_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_all_day_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_entry_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_to_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_time_entries_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_time_entry_type_id_isValid && m_user_id_isValid && true;
}

} // namespace OpenAPI
