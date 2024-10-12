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

#include "OAICountries.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICountries::OAICountries(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICountries::OAICountries() {
    this->initializeModel();
}

OAICountries::~OAICountries() {}

void OAICountries::initializeModel() {

    m_created_isSet = false;
    m_created_isValid = false;

    m_currency_id_isSet = false;
    m_currency_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_identifier_isSet = false;
    m_identifier_isValid = false;

    m_language_id_isSet = false;
    m_language_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_phone_code_isSet = false;
    m_phone_code_isValid = false;

    m_time_zone_isSet = false;
    m_time_zone_isValid = false;
}

void OAICountries::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICountries::fromJsonObject(QJsonObject json) {

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_currency_id_isValid = ::OpenAPI::fromJsonValue(m_currency_id, json[QString("currency_id")]);
    m_currency_id_isSet = !json[QString("currency_id")].isNull() && m_currency_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_identifier_isValid = ::OpenAPI::fromJsonValue(m_identifier, json[QString("identifier")]);
    m_identifier_isSet = !json[QString("identifier")].isNull() && m_identifier_isValid;

    m_language_id_isValid = ::OpenAPI::fromJsonValue(m_language_id, json[QString("language_id")]);
    m_language_id_isSet = !json[QString("language_id")].isNull() && m_language_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_phone_code_isValid = ::OpenAPI::fromJsonValue(m_phone_code, json[QString("phone_code")]);
    m_phone_code_isSet = !json[QString("phone_code")].isNull() && m_phone_code_isValid;

    m_time_zone_isValid = ::OpenAPI::fromJsonValue(m_time_zone, json[QString("time_zone")]);
    m_time_zone_isSet = !json[QString("time_zone")].isNull() && m_time_zone_isValid;
}

QString OAICountries::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICountries::asJsonObject() const {
    QJsonObject obj;
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_currency_id_isSet) {
        obj.insert(QString("currency_id"), ::OpenAPI::toJsonValue(m_currency_id));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_identifier_isSet) {
        obj.insert(QString("identifier"), ::OpenAPI::toJsonValue(m_identifier));
    }
    if (m_language_id_isSet) {
        obj.insert(QString("language_id"), ::OpenAPI::toJsonValue(m_language_id));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_phone_code_isSet) {
        obj.insert(QString("phone_code"), ::OpenAPI::toJsonValue(m_phone_code));
    }
    if (m_time_zone_isSet) {
        obj.insert(QString("time_zone"), ::OpenAPI::toJsonValue(m_time_zone));
    }
    return obj;
}

QString OAICountries::getCreated() const {
    return m_created;
}
void OAICountries::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAICountries::is_created_Set() const{
    return m_created_isSet;
}

bool OAICountries::is_created_Valid() const{
    return m_created_isValid;
}

QString OAICountries::getCurrencyId() const {
    return m_currency_id;
}
void OAICountries::setCurrencyId(const QString &currency_id) {
    m_currency_id = currency_id;
    m_currency_id_isSet = true;
}

bool OAICountries::is_currency_id_Set() const{
    return m_currency_id_isSet;
}

bool OAICountries::is_currency_id_Valid() const{
    return m_currency_id_isValid;
}

QString OAICountries::getDeleted() const {
    return m_deleted;
}
void OAICountries::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAICountries::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAICountries::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAICountries::getId() const {
    return m_id;
}
void OAICountries::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICountries::is_id_Set() const{
    return m_id_isSet;
}

bool OAICountries::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICountries::getIdentifier() const {
    return m_identifier;
}
void OAICountries::setIdentifier(const QString &identifier) {
    m_identifier = identifier;
    m_identifier_isSet = true;
}

bool OAICountries::is_identifier_Set() const{
    return m_identifier_isSet;
}

bool OAICountries::is_identifier_Valid() const{
    return m_identifier_isValid;
}

QString OAICountries::getLanguageId() const {
    return m_language_id;
}
void OAICountries::setLanguageId(const QString &language_id) {
    m_language_id = language_id;
    m_language_id_isSet = true;
}

bool OAICountries::is_language_id_Set() const{
    return m_language_id_isSet;
}

bool OAICountries::is_language_id_Valid() const{
    return m_language_id_isValid;
}

QString OAICountries::getModified() const {
    return m_modified;
}
void OAICountries::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAICountries::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAICountries::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAICountries::getName() const {
    return m_name;
}
void OAICountries::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICountries::is_name_Set() const{
    return m_name_isSet;
}

bool OAICountries::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICountries::getPhoneCode() const {
    return m_phone_code;
}
void OAICountries::setPhoneCode(const QString &phone_code) {
    m_phone_code = phone_code;
    m_phone_code_isSet = true;
}

bool OAICountries::is_phone_code_Set() const{
    return m_phone_code_isSet;
}

bool OAICountries::is_phone_code_Valid() const{
    return m_phone_code_isValid;
}

QString OAICountries::getTimeZone() const {
    return m_time_zone;
}
void OAICountries::setTimeZone(const QString &time_zone) {
    m_time_zone = time_zone;
    m_time_zone_isSet = true;
}

bool OAICountries::is_time_zone_Set() const{
    return m_time_zone_isSet;
}

bool OAICountries::is_time_zone_Valid() const{
    return m_time_zone_isValid;
}

bool OAICountries::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_zone_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICountries::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
