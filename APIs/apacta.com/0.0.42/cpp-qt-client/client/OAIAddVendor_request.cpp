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

#include "OAIAddVendor_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddVendor_request::OAIAddVendor_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddVendor_request::OAIAddVendor_request() {
    this->initializeModel();
}

OAIAddVendor_request::~OAIAddVendor_request() {}

void OAIAddVendor_request::initializeModel() {

    m_country_id_isSet = false;
    m_country_id_isValid = false;

    m_cvr_isSet = false;
    m_cvr_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_identifier_isSet = false;
    m_identifier_isValid = false;

    m_is_custom_isSet = false;
    m_is_custom_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIAddVendor_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddVendor_request::fromJsonObject(QJsonObject json) {

    m_country_id_isValid = ::OpenAPI::fromJsonValue(m_country_id, json[QString("country_id")]);
    m_country_id_isSet = !json[QString("country_id")].isNull() && m_country_id_isValid;

    m_cvr_isValid = ::OpenAPI::fromJsonValue(m_cvr, json[QString("cvr")]);
    m_cvr_isSet = !json[QString("cvr")].isNull() && m_cvr_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_identifier_isValid = ::OpenAPI::fromJsonValue(m_identifier, json[QString("identifier")]);
    m_identifier_isSet = !json[QString("identifier")].isNull() && m_identifier_isValid;

    m_is_custom_isValid = ::OpenAPI::fromJsonValue(m_is_custom, json[QString("is_custom")]);
    m_is_custom_isSet = !json[QString("is_custom")].isNull() && m_is_custom_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIAddVendor_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddVendor_request::asJsonObject() const {
    QJsonObject obj;
    if (m_country_id_isSet) {
        obj.insert(QString("country_id"), ::OpenAPI::toJsonValue(m_country_id));
    }
    if (m_cvr_isSet) {
        obj.insert(QString("cvr"), ::OpenAPI::toJsonValue(m_cvr));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_identifier_isSet) {
        obj.insert(QString("identifier"), ::OpenAPI::toJsonValue(m_identifier));
    }
    if (m_is_custom_isSet) {
        obj.insert(QString("is_custom"), ::OpenAPI::toJsonValue(m_is_custom));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIAddVendor_request::getCountryId() const {
    return m_country_id;
}
void OAIAddVendor_request::setCountryId(const QString &country_id) {
    m_country_id = country_id;
    m_country_id_isSet = true;
}

bool OAIAddVendor_request::is_country_id_Set() const{
    return m_country_id_isSet;
}

bool OAIAddVendor_request::is_country_id_Valid() const{
    return m_country_id_isValid;
}

QString OAIAddVendor_request::getCvr() const {
    return m_cvr;
}
void OAIAddVendor_request::setCvr(const QString &cvr) {
    m_cvr = cvr;
    m_cvr_isSet = true;
}

bool OAIAddVendor_request::is_cvr_Set() const{
    return m_cvr_isSet;
}

bool OAIAddVendor_request::is_cvr_Valid() const{
    return m_cvr_isValid;
}

QString OAIAddVendor_request::getEmail() const {
    return m_email;
}
void OAIAddVendor_request::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIAddVendor_request::is_email_Set() const{
    return m_email_isSet;
}

bool OAIAddVendor_request::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIAddVendor_request::getIdentifier() const {
    return m_identifier;
}
void OAIAddVendor_request::setIdentifier(const QString &identifier) {
    m_identifier = identifier;
    m_identifier_isSet = true;
}

bool OAIAddVendor_request::is_identifier_Set() const{
    return m_identifier_isSet;
}

bool OAIAddVendor_request::is_identifier_Valid() const{
    return m_identifier_isValid;
}

bool OAIAddVendor_request::isIsCustom() const {
    return m_is_custom;
}
void OAIAddVendor_request::setIsCustom(const bool &is_custom) {
    m_is_custom = is_custom;
    m_is_custom_isSet = true;
}

bool OAIAddVendor_request::is_is_custom_Set() const{
    return m_is_custom_isSet;
}

bool OAIAddVendor_request::is_is_custom_Valid() const{
    return m_is_custom_isValid;
}

QString OAIAddVendor_request::getName() const {
    return m_name;
}
void OAIAddVendor_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAddVendor_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAddVendor_request::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIAddVendor_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_country_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cvr_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_custom_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddVendor_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
