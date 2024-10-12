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

#include "OAI_employee_hours_get_200_response_data_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_employee_hours_get_200_response_data_inner::OAI_employee_hours_get_200_response_data_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_employee_hours_get_200_response_data_inner::OAI_employee_hours_get_200_response_data_inner() {
    this->initializeModel();
}

OAI_employee_hours_get_200_response_data_inner::~OAI_employee_hours_get_200_response_data_inner() {}

void OAI_employee_hours_get_200_response_data_inner::initializeModel() {

    m_form_date_isSet = false;
    m_form_date_isValid = false;

    m_form_id_isSet = false;
    m_form_id_isValid = false;

    m_project_name_isSet = false;
    m_project_name_isValid = false;

    m_total_hours_isSet = false;
    m_total_hours_isValid = false;

    m_working_description_isSet = false;
    m_working_description_isValid = false;

    m_working_description_full_isSet = false;
    m_working_description_full_isValid = false;
}

void OAI_employee_hours_get_200_response_data_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_employee_hours_get_200_response_data_inner::fromJsonObject(QJsonObject json) {

    m_form_date_isValid = ::OpenAPI::fromJsonValue(m_form_date, json[QString("form_date")]);
    m_form_date_isSet = !json[QString("form_date")].isNull() && m_form_date_isValid;

    m_form_id_isValid = ::OpenAPI::fromJsonValue(m_form_id, json[QString("form_id")]);
    m_form_id_isSet = !json[QString("form_id")].isNull() && m_form_id_isValid;

    m_project_name_isValid = ::OpenAPI::fromJsonValue(m_project_name, json[QString("project_name")]);
    m_project_name_isSet = !json[QString("project_name")].isNull() && m_project_name_isValid;

    m_total_hours_isValid = ::OpenAPI::fromJsonValue(m_total_hours, json[QString("total_hours")]);
    m_total_hours_isSet = !json[QString("total_hours")].isNull() && m_total_hours_isValid;

    m_working_description_isValid = ::OpenAPI::fromJsonValue(m_working_description, json[QString("working_description")]);
    m_working_description_isSet = !json[QString("working_description")].isNull() && m_working_description_isValid;

    m_working_description_full_isValid = ::OpenAPI::fromJsonValue(m_working_description_full, json[QString("working_description_full")]);
    m_working_description_full_isSet = !json[QString("working_description_full")].isNull() && m_working_description_full_isValid;
}

QString OAI_employee_hours_get_200_response_data_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_employee_hours_get_200_response_data_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_form_date_isSet) {
        obj.insert(QString("form_date"), ::OpenAPI::toJsonValue(m_form_date));
    }
    if (m_form_id_isSet) {
        obj.insert(QString("form_id"), ::OpenAPI::toJsonValue(m_form_id));
    }
    if (m_project_name_isSet) {
        obj.insert(QString("project_name"), ::OpenAPI::toJsonValue(m_project_name));
    }
    if (m_total_hours_isSet) {
        obj.insert(QString("total_hours"), ::OpenAPI::toJsonValue(m_total_hours));
    }
    if (m_working_description_isSet) {
        obj.insert(QString("working_description"), ::OpenAPI::toJsonValue(m_working_description));
    }
    if (m_working_description_full_isSet) {
        obj.insert(QString("working_description_full"), ::OpenAPI::toJsonValue(m_working_description_full));
    }
    return obj;
}

QDate OAI_employee_hours_get_200_response_data_inner::getFormDate() const {
    return m_form_date;
}
void OAI_employee_hours_get_200_response_data_inner::setFormDate(const QDate &form_date) {
    m_form_date = form_date;
    m_form_date_isSet = true;
}

bool OAI_employee_hours_get_200_response_data_inner::is_form_date_Set() const{
    return m_form_date_isSet;
}

bool OAI_employee_hours_get_200_response_data_inner::is_form_date_Valid() const{
    return m_form_date_isValid;
}

QString OAI_employee_hours_get_200_response_data_inner::getFormId() const {
    return m_form_id;
}
void OAI_employee_hours_get_200_response_data_inner::setFormId(const QString &form_id) {
    m_form_id = form_id;
    m_form_id_isSet = true;
}

bool OAI_employee_hours_get_200_response_data_inner::is_form_id_Set() const{
    return m_form_id_isSet;
}

bool OAI_employee_hours_get_200_response_data_inner::is_form_id_Valid() const{
    return m_form_id_isValid;
}

QString OAI_employee_hours_get_200_response_data_inner::getProjectName() const {
    return m_project_name;
}
void OAI_employee_hours_get_200_response_data_inner::setProjectName(const QString &project_name) {
    m_project_name = project_name;
    m_project_name_isSet = true;
}

bool OAI_employee_hours_get_200_response_data_inner::is_project_name_Set() const{
    return m_project_name_isSet;
}

bool OAI_employee_hours_get_200_response_data_inner::is_project_name_Valid() const{
    return m_project_name_isValid;
}

qint32 OAI_employee_hours_get_200_response_data_inner::getTotalHours() const {
    return m_total_hours;
}
void OAI_employee_hours_get_200_response_data_inner::setTotalHours(const qint32 &total_hours) {
    m_total_hours = total_hours;
    m_total_hours_isSet = true;
}

bool OAI_employee_hours_get_200_response_data_inner::is_total_hours_Set() const{
    return m_total_hours_isSet;
}

bool OAI_employee_hours_get_200_response_data_inner::is_total_hours_Valid() const{
    return m_total_hours_isValid;
}

QString OAI_employee_hours_get_200_response_data_inner::getWorkingDescription() const {
    return m_working_description;
}
void OAI_employee_hours_get_200_response_data_inner::setWorkingDescription(const QString &working_description) {
    m_working_description = working_description;
    m_working_description_isSet = true;
}

bool OAI_employee_hours_get_200_response_data_inner::is_working_description_Set() const{
    return m_working_description_isSet;
}

bool OAI_employee_hours_get_200_response_data_inner::is_working_description_Valid() const{
    return m_working_description_isValid;
}

QString OAI_employee_hours_get_200_response_data_inner::getWorkingDescriptionFull() const {
    return m_working_description_full;
}
void OAI_employee_hours_get_200_response_data_inner::setWorkingDescriptionFull(const QString &working_description_full) {
    m_working_description_full = working_description_full;
    m_working_description_full_isSet = true;
}

bool OAI_employee_hours_get_200_response_data_inner::is_working_description_full_Set() const{
    return m_working_description_full_isSet;
}

bool OAI_employee_hours_get_200_response_data_inner::is_working_description_full_Valid() const{
    return m_working_description_full_isValid;
}

bool OAI_employee_hours_get_200_response_data_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_form_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_working_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_working_description_full_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_employee_hours_get_200_response_data_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
