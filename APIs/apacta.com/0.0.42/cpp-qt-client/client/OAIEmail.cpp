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

#include "OAIEmail.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEmail::OAIEmail(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEmail::OAIEmail() {
    this->initializeModel();
}

OAIEmail::~OAIEmail() {}

void OAIEmail::initializeModel() {

    m_api_response_isSet = false;
    m_api_response_isValid = false;

    m_body_isSet = false;
    m_body_isValid = false;

    m_carbon_copy_isSet = false;
    m_carbon_copy_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_sent_isSet = false;
    m_is_sent_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_recipients_isSet = false;
    m_recipients_isValid = false;

    m_reply_to_isSet = false;
    m_reply_to_isValid = false;

    m_subject_isSet = false;
    m_subject_isValid = false;
}

void OAIEmail::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEmail::fromJsonObject(QJsonObject json) {

    m_api_response_isValid = ::OpenAPI::fromJsonValue(m_api_response, json[QString("api_response")]);
    m_api_response_isSet = !json[QString("api_response")].isNull() && m_api_response_isValid;

    m_body_isValid = ::OpenAPI::fromJsonValue(m_body, json[QString("body")]);
    m_body_isSet = !json[QString("body")].isNull() && m_body_isValid;

    m_carbon_copy_isValid = ::OpenAPI::fromJsonValue(m_carbon_copy, json[QString("carbon_copy")]);
    m_carbon_copy_isSet = !json[QString("carbon_copy")].isNull() && m_carbon_copy_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_sent_isValid = ::OpenAPI::fromJsonValue(m_is_sent, json[QString("is_sent")]);
    m_is_sent_isSet = !json[QString("is_sent")].isNull() && m_is_sent_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_recipients_isValid = ::OpenAPI::fromJsonValue(m_recipients, json[QString("recipients")]);
    m_recipients_isSet = !json[QString("recipients")].isNull() && m_recipients_isValid;

    m_reply_to_isValid = ::OpenAPI::fromJsonValue(m_reply_to, json[QString("reply_to")]);
    m_reply_to_isSet = !json[QString("reply_to")].isNull() && m_reply_to_isValid;

    m_subject_isValid = ::OpenAPI::fromJsonValue(m_subject, json[QString("subject")]);
    m_subject_isSet = !json[QString("subject")].isNull() && m_subject_isValid;
}

QString OAIEmail::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEmail::asJsonObject() const {
    QJsonObject obj;
    if (m_api_response_isSet) {
        obj.insert(QString("api_response"), ::OpenAPI::toJsonValue(m_api_response));
    }
    if (m_body_isSet) {
        obj.insert(QString("body"), ::OpenAPI::toJsonValue(m_body));
    }
    if (m_carbon_copy_isSet) {
        obj.insert(QString("carbon_copy"), ::OpenAPI::toJsonValue(m_carbon_copy));
    }
    if (m_company_id_isSet) {
        obj.insert(QString("company_id"), ::OpenAPI::toJsonValue(m_company_id));
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
    if (m_is_sent_isSet) {
        obj.insert(QString("is_sent"), ::OpenAPI::toJsonValue(m_is_sent));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_recipients_isSet) {
        obj.insert(QString("recipients"), ::OpenAPI::toJsonValue(m_recipients));
    }
    if (m_reply_to_isSet) {
        obj.insert(QString("reply_to"), ::OpenAPI::toJsonValue(m_reply_to));
    }
    if (m_subject_isSet) {
        obj.insert(QString("subject"), ::OpenAPI::toJsonValue(m_subject));
    }
    return obj;
}

QString OAIEmail::getApiResponse() const {
    return m_api_response;
}
void OAIEmail::setApiResponse(const QString &api_response) {
    m_api_response = api_response;
    m_api_response_isSet = true;
}

bool OAIEmail::is_api_response_Set() const{
    return m_api_response_isSet;
}

bool OAIEmail::is_api_response_Valid() const{
    return m_api_response_isValid;
}

QString OAIEmail::getBody() const {
    return m_body;
}
void OAIEmail::setBody(const QString &body) {
    m_body = body;
    m_body_isSet = true;
}

bool OAIEmail::is_body_Set() const{
    return m_body_isSet;
}

bool OAIEmail::is_body_Valid() const{
    return m_body_isValid;
}

QString OAIEmail::getCarbonCopy() const {
    return m_carbon_copy;
}
void OAIEmail::setCarbonCopy(const QString &carbon_copy) {
    m_carbon_copy = carbon_copy;
    m_carbon_copy_isSet = true;
}

bool OAIEmail::is_carbon_copy_Set() const{
    return m_carbon_copy_isSet;
}

bool OAIEmail::is_carbon_copy_Valid() const{
    return m_carbon_copy_isValid;
}

QString OAIEmail::getCompanyId() const {
    return m_company_id;
}
void OAIEmail::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIEmail::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIEmail::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIEmail::getCreated() const {
    return m_created;
}
void OAIEmail::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIEmail::is_created_Set() const{
    return m_created_isSet;
}

bool OAIEmail::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIEmail::getCreatedById() const {
    return m_created_by_id;
}
void OAIEmail::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIEmail::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIEmail::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIEmail::getDeleted() const {
    return m_deleted;
}
void OAIEmail::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIEmail::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIEmail::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIEmail::getId() const {
    return m_id;
}
void OAIEmail::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIEmail::is_id_Set() const{
    return m_id_isSet;
}

bool OAIEmail::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIEmail::isIsSent() const {
    return m_is_sent;
}
void OAIEmail::setIsSent(const bool &is_sent) {
    m_is_sent = is_sent;
    m_is_sent_isSet = true;
}

bool OAIEmail::is_is_sent_Set() const{
    return m_is_sent_isSet;
}

bool OAIEmail::is_is_sent_Valid() const{
    return m_is_sent_isValid;
}

QString OAIEmail::getModified() const {
    return m_modified;
}
void OAIEmail::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIEmail::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIEmail::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIEmail::getRecipients() const {
    return m_recipients;
}
void OAIEmail::setRecipients(const QString &recipients) {
    m_recipients = recipients;
    m_recipients_isSet = true;
}

bool OAIEmail::is_recipients_Set() const{
    return m_recipients_isSet;
}

bool OAIEmail::is_recipients_Valid() const{
    return m_recipients_isValid;
}

QString OAIEmail::getReplyTo() const {
    return m_reply_to;
}
void OAIEmail::setReplyTo(const QString &reply_to) {
    m_reply_to = reply_to;
    m_reply_to_isSet = true;
}

bool OAIEmail::is_reply_to_Set() const{
    return m_reply_to_isSet;
}

bool OAIEmail::is_reply_to_Valid() const{
    return m_reply_to_isValid;
}

QString OAIEmail::getSubject() const {
    return m_subject;
}
void OAIEmail::setSubject(const QString &subject) {
    m_subject = subject;
    m_subject_isSet = true;
}

bool OAIEmail::is_subject_Set() const{
    return m_subject_isSet;
}

bool OAIEmail::is_subject_Valid() const{
    return m_subject_isValid;
}

bool OAIEmail::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_api_response_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_body_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_carbon_copy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_id_isSet) {
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

        if (m_is_sent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recipients_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reply_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subject_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEmail::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
