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

#include "OAISender.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISender::OAISender(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISender::OAISender() {
    this->initializeModel();
}

OAISender::~OAISender() {}

void OAISender::initializeModel() {

    m_city_id_isSet = false;
    m_city_id_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_cvr_isSet = false;
    m_cvr_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_language_id_isSet = false;
    m_language_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_phone_countrycode_isSet = false;
    m_phone_countrycode_isValid = false;

    m_street_name_isSet = false;
    m_street_name_isValid = false;

    m_website_isSet = false;
    m_website_isValid = false;
}

void OAISender::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISender::fromJsonObject(QJsonObject json) {

    m_city_id_isValid = ::OpenAPI::fromJsonValue(m_city_id, json[QString("city_id")]);
    m_city_id_isSet = !json[QString("city_id")].isNull() && m_city_id_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_cvr_isValid = ::OpenAPI::fromJsonValue(m_cvr, json[QString("cvr")]);
    m_cvr_isSet = !json[QString("cvr")].isNull() && m_cvr_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_language_id_isValid = ::OpenAPI::fromJsonValue(m_language_id, json[QString("language_id")]);
    m_language_id_isSet = !json[QString("language_id")].isNull() && m_language_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;

    m_phone_countrycode_isValid = ::OpenAPI::fromJsonValue(m_phone_countrycode, json[QString("phone_countrycode")]);
    m_phone_countrycode_isSet = !json[QString("phone_countrycode")].isNull() && m_phone_countrycode_isValid;

    m_street_name_isValid = ::OpenAPI::fromJsonValue(m_street_name, json[QString("street_name")]);
    m_street_name_isSet = !json[QString("street_name")].isNull() && m_street_name_isValid;

    m_website_isValid = ::OpenAPI::fromJsonValue(m_website, json[QString("website")]);
    m_website_isSet = !json[QString("website")].isNull() && m_website_isValid;
}

QString OAISender::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISender::asJsonObject() const {
    QJsonObject obj;
    if (m_city_id_isSet) {
        obj.insert(QString("city_id"), ::OpenAPI::toJsonValue(m_city_id));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_created_by_id_isSet) {
        obj.insert(QString("created_by_id"), ::OpenAPI::toJsonValue(m_created_by_id));
    }
    if (m_cvr_isSet) {
        obj.insert(QString("cvr"), ::OpenAPI::toJsonValue(m_cvr));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
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
    if (m_phone_isSet) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_phone_countrycode_isSet) {
        obj.insert(QString("phone_countrycode"), ::OpenAPI::toJsonValue(m_phone_countrycode));
    }
    if (m_street_name_isSet) {
        obj.insert(QString("street_name"), ::OpenAPI::toJsonValue(m_street_name));
    }
    if (m_website_isSet) {
        obj.insert(QString("website"), ::OpenAPI::toJsonValue(m_website));
    }
    return obj;
}

QString OAISender::getCityId() const {
    return m_city_id;
}
void OAISender::setCityId(const QString &city_id) {
    m_city_id = city_id;
    m_city_id_isSet = true;
}

bool OAISender::is_city_id_Set() const{
    return m_city_id_isSet;
}

bool OAISender::is_city_id_Valid() const{
    return m_city_id_isValid;
}

QString OAISender::getCreated() const {
    return m_created;
}
void OAISender::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAISender::is_created_Set() const{
    return m_created_isSet;
}

bool OAISender::is_created_Valid() const{
    return m_created_isValid;
}

QString OAISender::getCreatedById() const {
    return m_created_by_id;
}
void OAISender::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAISender::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAISender::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAISender::getCvr() const {
    return m_cvr;
}
void OAISender::setCvr(const QString &cvr) {
    m_cvr = cvr;
    m_cvr_isSet = true;
}

bool OAISender::is_cvr_Set() const{
    return m_cvr_isSet;
}

bool OAISender::is_cvr_Valid() const{
    return m_cvr_isValid;
}

QString OAISender::getDeleted() const {
    return m_deleted;
}
void OAISender::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAISender::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAISender::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAISender::getEmail() const {
    return m_email;
}
void OAISender::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAISender::is_email_Set() const{
    return m_email_isSet;
}

bool OAISender::is_email_Valid() const{
    return m_email_isValid;
}

QString OAISender::getId() const {
    return m_id;
}
void OAISender::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISender::is_id_Set() const{
    return m_id_isSet;
}

bool OAISender::is_id_Valid() const{
    return m_id_isValid;
}

QString OAISender::getLanguageId() const {
    return m_language_id;
}
void OAISender::setLanguageId(const QString &language_id) {
    m_language_id = language_id;
    m_language_id_isSet = true;
}

bool OAISender::is_language_id_Set() const{
    return m_language_id_isSet;
}

bool OAISender::is_language_id_Valid() const{
    return m_language_id_isValid;
}

QString OAISender::getModified() const {
    return m_modified;
}
void OAISender::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAISender::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAISender::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAISender::getName() const {
    return m_name;
}
void OAISender::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISender::is_name_Set() const{
    return m_name_isSet;
}

bool OAISender::is_name_Valid() const{
    return m_name_isValid;
}

QString OAISender::getPhone() const {
    return m_phone;
}
void OAISender::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAISender::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAISender::is_phone_Valid() const{
    return m_phone_isValid;
}

QString OAISender::getPhoneCountrycode() const {
    return m_phone_countrycode;
}
void OAISender::setPhoneCountrycode(const QString &phone_countrycode) {
    m_phone_countrycode = phone_countrycode;
    m_phone_countrycode_isSet = true;
}

bool OAISender::is_phone_countrycode_Set() const{
    return m_phone_countrycode_isSet;
}

bool OAISender::is_phone_countrycode_Valid() const{
    return m_phone_countrycode_isValid;
}

QString OAISender::getStreetName() const {
    return m_street_name;
}
void OAISender::setStreetName(const QString &street_name) {
    m_street_name = street_name;
    m_street_name_isSet = true;
}

bool OAISender::is_street_name_Set() const{
    return m_street_name_isSet;
}

bool OAISender::is_street_name_Valid() const{
    return m_street_name_isValid;
}

QString OAISender::getWebsite() const {
    return m_website;
}
void OAISender::setWebsite(const QString &website) {
    m_website = website;
    m_website_isSet = true;
}

bool OAISender::is_website_Set() const{
    return m_website_isSet;
}

bool OAISender::is_website_Valid() const{
    return m_website_isValid;
}

bool OAISender::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_by_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cvr_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
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

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_countrycode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISender::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
