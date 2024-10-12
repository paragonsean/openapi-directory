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

#include "OAIClockingRecord.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIClockingRecord::OAIClockingRecord(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIClockingRecord::OAIClockingRecord() {
    this->initializeModel();
}

OAIClockingRecord::~OAIClockingRecord() {}

void OAIClockingRecord::initializeModel() {

    m_checked_in_isSet = false;
    m_checked_in_isValid = false;

    m_checked_out_isSet = false;
    m_checked_out_isValid = false;

    m_checkin_latitude_isSet = false;
    m_checkin_latitude_isValid = false;

    m_checkin_longitude_isSet = false;
    m_checkin_longitude_isValid = false;

    m_checkout_latitude_isSet = false;
    m_checkout_latitude_isValid = false;

    m_checkout_longitude_isSet = false;
    m_checkout_longitude_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_modified_by_id_isSet = false;
    m_modified_by_id_isValid = false;

    m_project_id_isSet = false;
    m_project_id_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIClockingRecord::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIClockingRecord::fromJsonObject(QJsonObject json) {

    m_checked_in_isValid = ::OpenAPI::fromJsonValue(m_checked_in, json[QString("checked_in")]);
    m_checked_in_isSet = !json[QString("checked_in")].isNull() && m_checked_in_isValid;

    m_checked_out_isValid = ::OpenAPI::fromJsonValue(m_checked_out, json[QString("checked_out")]);
    m_checked_out_isSet = !json[QString("checked_out")].isNull() && m_checked_out_isValid;

    m_checkin_latitude_isValid = ::OpenAPI::fromJsonValue(m_checkin_latitude, json[QString("checkin_latitude")]);
    m_checkin_latitude_isSet = !json[QString("checkin_latitude")].isNull() && m_checkin_latitude_isValid;

    m_checkin_longitude_isValid = ::OpenAPI::fromJsonValue(m_checkin_longitude, json[QString("checkin_longitude")]);
    m_checkin_longitude_isSet = !json[QString("checkin_longitude")].isNull() && m_checkin_longitude_isValid;

    m_checkout_latitude_isValid = ::OpenAPI::fromJsonValue(m_checkout_latitude, json[QString("checkout_latitude")]);
    m_checkout_latitude_isSet = !json[QString("checkout_latitude")].isNull() && m_checkout_latitude_isValid;

    m_checkout_longitude_isValid = ::OpenAPI::fromJsonValue(m_checkout_longitude, json[QString("checkout_longitude")]);
    m_checkout_longitude_isSet = !json[QString("checkout_longitude")].isNull() && m_checkout_longitude_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_modified_by_id_isValid = ::OpenAPI::fromJsonValue(m_modified_by_id, json[QString("modified_by_id")]);
    m_modified_by_id_isSet = !json[QString("modified_by_id")].isNull() && m_modified_by_id_isValid;

    m_project_id_isValid = ::OpenAPI::fromJsonValue(m_project_id, json[QString("project_id")]);
    m_project_id_isSet = !json[QString("project_id")].isNull() && m_project_id_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;
}

QString OAIClockingRecord::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIClockingRecord::asJsonObject() const {
    QJsonObject obj;
    if (m_checked_in_isSet) {
        obj.insert(QString("checked_in"), ::OpenAPI::toJsonValue(m_checked_in));
    }
    if (m_checked_out_isSet) {
        obj.insert(QString("checked_out"), ::OpenAPI::toJsonValue(m_checked_out));
    }
    if (m_checkin_latitude_isSet) {
        obj.insert(QString("checkin_latitude"), ::OpenAPI::toJsonValue(m_checkin_latitude));
    }
    if (m_checkin_longitude_isSet) {
        obj.insert(QString("checkin_longitude"), ::OpenAPI::toJsonValue(m_checkin_longitude));
    }
    if (m_checkout_latitude_isSet) {
        obj.insert(QString("checkout_latitude"), ::OpenAPI::toJsonValue(m_checkout_latitude));
    }
    if (m_checkout_longitude_isSet) {
        obj.insert(QString("checkout_longitude"), ::OpenAPI::toJsonValue(m_checkout_longitude));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_created_by_id_isSet) {
        obj.insert(QString("created_by_id"), ::OpenAPI::toJsonValue(m_created_by_id));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_modified_by_id_isSet) {
        obj.insert(QString("modified_by_id"), ::OpenAPI::toJsonValue(m_modified_by_id));
    }
    if (m_project_id_isSet) {
        obj.insert(QString("project_id"), ::OpenAPI::toJsonValue(m_project_id));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIClockingRecord::getCheckedIn() const {
    return m_checked_in;
}
void OAIClockingRecord::setCheckedIn(const QString &checked_in) {
    m_checked_in = checked_in;
    m_checked_in_isSet = true;
}

bool OAIClockingRecord::is_checked_in_Set() const{
    return m_checked_in_isSet;
}

bool OAIClockingRecord::is_checked_in_Valid() const{
    return m_checked_in_isValid;
}

QString OAIClockingRecord::getCheckedOut() const {
    return m_checked_out;
}
void OAIClockingRecord::setCheckedOut(const QString &checked_out) {
    m_checked_out = checked_out;
    m_checked_out_isSet = true;
}

bool OAIClockingRecord::is_checked_out_Set() const{
    return m_checked_out_isSet;
}

bool OAIClockingRecord::is_checked_out_Valid() const{
    return m_checked_out_isValid;
}

QString OAIClockingRecord::getCheckinLatitude() const {
    return m_checkin_latitude;
}
void OAIClockingRecord::setCheckinLatitude(const QString &checkin_latitude) {
    m_checkin_latitude = checkin_latitude;
    m_checkin_latitude_isSet = true;
}

bool OAIClockingRecord::is_checkin_latitude_Set() const{
    return m_checkin_latitude_isSet;
}

bool OAIClockingRecord::is_checkin_latitude_Valid() const{
    return m_checkin_latitude_isValid;
}

QString OAIClockingRecord::getCheckinLongitude() const {
    return m_checkin_longitude;
}
void OAIClockingRecord::setCheckinLongitude(const QString &checkin_longitude) {
    m_checkin_longitude = checkin_longitude;
    m_checkin_longitude_isSet = true;
}

bool OAIClockingRecord::is_checkin_longitude_Set() const{
    return m_checkin_longitude_isSet;
}

bool OAIClockingRecord::is_checkin_longitude_Valid() const{
    return m_checkin_longitude_isValid;
}

QString OAIClockingRecord::getCheckoutLatitude() const {
    return m_checkout_latitude;
}
void OAIClockingRecord::setCheckoutLatitude(const QString &checkout_latitude) {
    m_checkout_latitude = checkout_latitude;
    m_checkout_latitude_isSet = true;
}

bool OAIClockingRecord::is_checkout_latitude_Set() const{
    return m_checkout_latitude_isSet;
}

bool OAIClockingRecord::is_checkout_latitude_Valid() const{
    return m_checkout_latitude_isValid;
}

QString OAIClockingRecord::getCheckoutLongitude() const {
    return m_checkout_longitude;
}
void OAIClockingRecord::setCheckoutLongitude(const QString &checkout_longitude) {
    m_checkout_longitude = checkout_longitude;
    m_checkout_longitude_isSet = true;
}

bool OAIClockingRecord::is_checkout_longitude_Set() const{
    return m_checkout_longitude_isSet;
}

bool OAIClockingRecord::is_checkout_longitude_Valid() const{
    return m_checkout_longitude_isValid;
}

QString OAIClockingRecord::getCreated() const {
    return m_created;
}
void OAIClockingRecord::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIClockingRecord::is_created_Set() const{
    return m_created_isSet;
}

bool OAIClockingRecord::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIClockingRecord::getCreatedById() const {
    return m_created_by_id;
}
void OAIClockingRecord::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIClockingRecord::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIClockingRecord::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIClockingRecord::getDeleted() const {
    return m_deleted;
}
void OAIClockingRecord::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIClockingRecord::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIClockingRecord::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIClockingRecord::getId() const {
    return m_id;
}
void OAIClockingRecord::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIClockingRecord::is_id_Set() const{
    return m_id_isSet;
}

bool OAIClockingRecord::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIClockingRecord::getModified() const {
    return m_modified;
}
void OAIClockingRecord::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIClockingRecord::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIClockingRecord::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIClockingRecord::getModifiedById() const {
    return m_modified_by_id;
}
void OAIClockingRecord::setModifiedById(const QString &modified_by_id) {
    m_modified_by_id = modified_by_id;
    m_modified_by_id_isSet = true;
}

bool OAIClockingRecord::is_modified_by_id_Set() const{
    return m_modified_by_id_isSet;
}

bool OAIClockingRecord::is_modified_by_id_Valid() const{
    return m_modified_by_id_isValid;
}

QString OAIClockingRecord::getProjectId() const {
    return m_project_id;
}
void OAIClockingRecord::setProjectId(const QString &project_id) {
    m_project_id = project_id;
    m_project_id_isSet = true;
}

bool OAIClockingRecord::is_project_id_Set() const{
    return m_project_id_isSet;
}

bool OAIClockingRecord::is_project_id_Valid() const{
    return m_project_id_isValid;
}

QString OAIClockingRecord::getUserId() const {
    return m_user_id;
}
void OAIClockingRecord::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIClockingRecord::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIClockingRecord::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIClockingRecord::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_checked_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_checked_out_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_checkin_latitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_checkin_longitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_checkout_latitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_checkout_longitude_isSet) {
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

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_by_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_id_isSet) {
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

bool OAIClockingRecord::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
