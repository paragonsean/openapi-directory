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

#include "OAI_financial_statistics_workingHours_get_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_financial_statistics_workingHours_get_200_response::OAI_financial_statistics_workingHours_get_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_financial_statistics_workingHours_get_200_response::OAI_financial_statistics_workingHours_get_200_response() {
    this->initializeModel();
}

OAI_financial_statistics_workingHours_get_200_response::~OAI_financial_statistics_workingHours_get_200_response() {}

void OAI_financial_statistics_workingHours_get_200_response::initializeModel() {

    m_normal_working_hours_isSet = false;
    m_normal_working_hours_isValid = false;

    m_time_entries_isSet = false;
    m_time_entries_isValid = false;

    m_total_working_hours_isSet = false;
    m_total_working_hours_isValid = false;
}

void OAI_financial_statistics_workingHours_get_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_financial_statistics_workingHours_get_200_response::fromJsonObject(QJsonObject json) {

    m_normal_working_hours_isValid = ::OpenAPI::fromJsonValue(m_normal_working_hours, json[QString("normalWorkingHours")]);
    m_normal_working_hours_isSet = !json[QString("normalWorkingHours")].isNull() && m_normal_working_hours_isValid;

    m_time_entries_isValid = ::OpenAPI::fromJsonValue(m_time_entries, json[QString("timeEntries")]);
    m_time_entries_isSet = !json[QString("timeEntries")].isNull() && m_time_entries_isValid;

    m_total_working_hours_isValid = ::OpenAPI::fromJsonValue(m_total_working_hours, json[QString("totalWorkingHours")]);
    m_total_working_hours_isSet = !json[QString("totalWorkingHours")].isNull() && m_total_working_hours_isValid;
}

QString OAI_financial_statistics_workingHours_get_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_financial_statistics_workingHours_get_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_normal_working_hours_isSet) {
        obj.insert(QString("normalWorkingHours"), ::OpenAPI::toJsonValue(m_normal_working_hours));
    }
    if (m_time_entries.size() > 0) {
        obj.insert(QString("timeEntries"), ::OpenAPI::toJsonValue(m_time_entries));
    }
    if (m_total_working_hours_isSet) {
        obj.insert(QString("totalWorkingHours"), ::OpenAPI::toJsonValue(m_total_working_hours));
    }
    return obj;
}

QString OAI_financial_statistics_workingHours_get_200_response::getNormalWorkingHours() const {
    return m_normal_working_hours;
}
void OAI_financial_statistics_workingHours_get_200_response::setNormalWorkingHours(const QString &normal_working_hours) {
    m_normal_working_hours = normal_working_hours;
    m_normal_working_hours_isSet = true;
}

bool OAI_financial_statistics_workingHours_get_200_response::is_normal_working_hours_Set() const{
    return m_normal_working_hours_isSet;
}

bool OAI_financial_statistics_workingHours_get_200_response::is_normal_working_hours_Valid() const{
    return m_normal_working_hours_isValid;
}

QList<OAI_financial_statistics_workingHours_get_200_response_timeEntries_inner> OAI_financial_statistics_workingHours_get_200_response::getTimeEntries() const {
    return m_time_entries;
}
void OAI_financial_statistics_workingHours_get_200_response::setTimeEntries(const QList<OAI_financial_statistics_workingHours_get_200_response_timeEntries_inner> &time_entries) {
    m_time_entries = time_entries;
    m_time_entries_isSet = true;
}

bool OAI_financial_statistics_workingHours_get_200_response::is_time_entries_Set() const{
    return m_time_entries_isSet;
}

bool OAI_financial_statistics_workingHours_get_200_response::is_time_entries_Valid() const{
    return m_time_entries_isValid;
}

QString OAI_financial_statistics_workingHours_get_200_response::getTotalWorkingHours() const {
    return m_total_working_hours;
}
void OAI_financial_statistics_workingHours_get_200_response::setTotalWorkingHours(const QString &total_working_hours) {
    m_total_working_hours = total_working_hours;
    m_total_working_hours_isSet = true;
}

bool OAI_financial_statistics_workingHours_get_200_response::is_total_working_hours_Set() const{
    return m_total_working_hours_isSet;
}

bool OAI_financial_statistics_workingHours_get_200_response::is_total_working_hours_Valid() const{
    return m_total_working_hours_isValid;
}

bool OAI_financial_statistics_workingHours_get_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_normal_working_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_entries.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_working_hours_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_financial_statistics_workingHours_get_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
