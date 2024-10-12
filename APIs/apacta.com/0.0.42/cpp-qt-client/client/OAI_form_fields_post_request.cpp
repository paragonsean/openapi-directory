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

#include "OAI_form_fields_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_form_fields_post_request::OAI_form_fields_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_form_fields_post_request::OAI_form_fields_post_request() {
    this->initializeModel();
}

OAI_form_fields_post_request::~OAI_form_fields_post_request() {}

void OAI_form_fields_post_request::initializeModel() {

    m_comment_isSet = false;
    m_comment_isValid = false;

    m_content_value_isSet = false;
    m_content_value_isValid = false;

    m_file_id_isSet = false;
    m_file_id_isValid = false;

    m_form_field_type_id_isSet = false;
    m_form_field_type_id_isValid = false;

    m_form_id_isSet = false;
    m_form_id_isValid = false;

    m_form_template_field_id_isSet = false;
    m_form_template_field_id_isValid = false;

    m_placement_isSet = false;
    m_placement_isValid = false;
}

void OAI_form_fields_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_form_fields_post_request::fromJsonObject(QJsonObject json) {

    m_comment_isValid = ::OpenAPI::fromJsonValue(m_comment, json[QString("comment")]);
    m_comment_isSet = !json[QString("comment")].isNull() && m_comment_isValid;

    m_content_value_isValid = ::OpenAPI::fromJsonValue(m_content_value, json[QString("content_value")]);
    m_content_value_isSet = !json[QString("content_value")].isNull() && m_content_value_isValid;

    m_file_id_isValid = ::OpenAPI::fromJsonValue(m_file_id, json[QString("file_id")]);
    m_file_id_isSet = !json[QString("file_id")].isNull() && m_file_id_isValid;

    m_form_field_type_id_isValid = ::OpenAPI::fromJsonValue(m_form_field_type_id, json[QString("form_field_type_id")]);
    m_form_field_type_id_isSet = !json[QString("form_field_type_id")].isNull() && m_form_field_type_id_isValid;

    m_form_id_isValid = ::OpenAPI::fromJsonValue(m_form_id, json[QString("form_id")]);
    m_form_id_isSet = !json[QString("form_id")].isNull() && m_form_id_isValid;

    m_form_template_field_id_isValid = ::OpenAPI::fromJsonValue(m_form_template_field_id, json[QString("form_template_field_id")]);
    m_form_template_field_id_isSet = !json[QString("form_template_field_id")].isNull() && m_form_template_field_id_isValid;

    m_placement_isValid = ::OpenAPI::fromJsonValue(m_placement, json[QString("placement")]);
    m_placement_isSet = !json[QString("placement")].isNull() && m_placement_isValid;
}

QString OAI_form_fields_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_form_fields_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_comment_isSet) {
        obj.insert(QString("comment"), ::OpenAPI::toJsonValue(m_comment));
    }
    if (m_content_value_isSet) {
        obj.insert(QString("content_value"), ::OpenAPI::toJsonValue(m_content_value));
    }
    if (m_file_id_isSet) {
        obj.insert(QString("file_id"), ::OpenAPI::toJsonValue(m_file_id));
    }
    if (m_form_field_type_id_isSet) {
        obj.insert(QString("form_field_type_id"), ::OpenAPI::toJsonValue(m_form_field_type_id));
    }
    if (m_form_id_isSet) {
        obj.insert(QString("form_id"), ::OpenAPI::toJsonValue(m_form_id));
    }
    if (m_form_template_field_id_isSet) {
        obj.insert(QString("form_template_field_id"), ::OpenAPI::toJsonValue(m_form_template_field_id));
    }
    if (m_placement_isSet) {
        obj.insert(QString("placement"), ::OpenAPI::toJsonValue(m_placement));
    }
    return obj;
}

QString OAI_form_fields_post_request::getComment() const {
    return m_comment;
}
void OAI_form_fields_post_request::setComment(const QString &comment) {
    m_comment = comment;
    m_comment_isSet = true;
}

bool OAI_form_fields_post_request::is_comment_Set() const{
    return m_comment_isSet;
}

bool OAI_form_fields_post_request::is_comment_Valid() const{
    return m_comment_isValid;
}

QString OAI_form_fields_post_request::getContentValue() const {
    return m_content_value;
}
void OAI_form_fields_post_request::setContentValue(const QString &content_value) {
    m_content_value = content_value;
    m_content_value_isSet = true;
}

bool OAI_form_fields_post_request::is_content_value_Set() const{
    return m_content_value_isSet;
}

bool OAI_form_fields_post_request::is_content_value_Valid() const{
    return m_content_value_isValid;
}

QString OAI_form_fields_post_request::getFileId() const {
    return m_file_id;
}
void OAI_form_fields_post_request::setFileId(const QString &file_id) {
    m_file_id = file_id;
    m_file_id_isSet = true;
}

bool OAI_form_fields_post_request::is_file_id_Set() const{
    return m_file_id_isSet;
}

bool OAI_form_fields_post_request::is_file_id_Valid() const{
    return m_file_id_isValid;
}

QString OAI_form_fields_post_request::getFormFieldTypeId() const {
    return m_form_field_type_id;
}
void OAI_form_fields_post_request::setFormFieldTypeId(const QString &form_field_type_id) {
    m_form_field_type_id = form_field_type_id;
    m_form_field_type_id_isSet = true;
}

bool OAI_form_fields_post_request::is_form_field_type_id_Set() const{
    return m_form_field_type_id_isSet;
}

bool OAI_form_fields_post_request::is_form_field_type_id_Valid() const{
    return m_form_field_type_id_isValid;
}

QString OAI_form_fields_post_request::getFormId() const {
    return m_form_id;
}
void OAI_form_fields_post_request::setFormId(const QString &form_id) {
    m_form_id = form_id;
    m_form_id_isSet = true;
}

bool OAI_form_fields_post_request::is_form_id_Set() const{
    return m_form_id_isSet;
}

bool OAI_form_fields_post_request::is_form_id_Valid() const{
    return m_form_id_isValid;
}

QString OAI_form_fields_post_request::getFormTemplateFieldId() const {
    return m_form_template_field_id;
}
void OAI_form_fields_post_request::setFormTemplateFieldId(const QString &form_template_field_id) {
    m_form_template_field_id = form_template_field_id;
    m_form_template_field_id_isSet = true;
}

bool OAI_form_fields_post_request::is_form_template_field_id_Set() const{
    return m_form_template_field_id_isSet;
}

bool OAI_form_fields_post_request::is_form_template_field_id_Valid() const{
    return m_form_template_field_id_isValid;
}

qint32 OAI_form_fields_post_request::getPlacement() const {
    return m_placement;
}
void OAI_form_fields_post_request::setPlacement(const qint32 &placement) {
    m_placement = placement;
    m_placement_isSet = true;
}

bool OAI_form_fields_post_request::is_placement_Set() const{
    return m_placement_isSet;
}

bool OAI_form_fields_post_request::is_placement_Valid() const{
    return m_placement_isValid;
}

bool OAI_form_fields_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_comment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_content_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_field_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_template_field_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_placement_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_form_fields_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
