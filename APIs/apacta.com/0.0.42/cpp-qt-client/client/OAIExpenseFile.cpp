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

#include "OAIExpenseFile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExpenseFile::OAIExpenseFile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExpenseFile::OAIExpenseFile() {
    this->initializeModel();
}

OAIExpenseFile::~OAIExpenseFile() {}

void OAIExpenseFile::initializeModel() {

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_expense_id_isSet = false;
    m_expense_id_isValid = false;

    m_file_isSet = false;
    m_file_isValid = false;

    m_file_extension_isSet = false;
    m_file_extension_isValid = false;

    m_file_original_name_isSet = false;
    m_file_original_name_isValid = false;

    m_file_size_isSet = false;
    m_file_size_isValid = false;

    m_file_type_isSet = false;
    m_file_type_isValid = false;

    m_file_url_isSet = false;
    m_file_url_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;
}

void OAIExpenseFile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExpenseFile::fromJsonObject(QJsonObject json) {

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_expense_id_isValid = ::OpenAPI::fromJsonValue(m_expense_id, json[QString("expense_id")]);
    m_expense_id_isSet = !json[QString("expense_id")].isNull() && m_expense_id_isValid;

    m_file_isValid = ::OpenAPI::fromJsonValue(m_file, json[QString("file")]);
    m_file_isSet = !json[QString("file")].isNull() && m_file_isValid;

    m_file_extension_isValid = ::OpenAPI::fromJsonValue(m_file_extension, json[QString("file_extension")]);
    m_file_extension_isSet = !json[QString("file_extension")].isNull() && m_file_extension_isValid;

    m_file_original_name_isValid = ::OpenAPI::fromJsonValue(m_file_original_name, json[QString("file_original_name")]);
    m_file_original_name_isSet = !json[QString("file_original_name")].isNull() && m_file_original_name_isValid;

    m_file_size_isValid = ::OpenAPI::fromJsonValue(m_file_size, json[QString("file_size")]);
    m_file_size_isSet = !json[QString("file_size")].isNull() && m_file_size_isValid;

    m_file_type_isValid = ::OpenAPI::fromJsonValue(m_file_type, json[QString("file_type")]);
    m_file_type_isSet = !json[QString("file_type")].isNull() && m_file_type_isValid;

    m_file_url_isValid = ::OpenAPI::fromJsonValue(m_file_url, json[QString("file_url")]);
    m_file_url_isSet = !json[QString("file_url")].isNull() && m_file_url_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;
}

QString OAIExpenseFile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExpenseFile::asJsonObject() const {
    QJsonObject obj;
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_created_by_id_isSet) {
        obj.insert(QString("created_by_id"), ::OpenAPI::toJsonValue(m_created_by_id));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_expense_id_isSet) {
        obj.insert(QString("expense_id"), ::OpenAPI::toJsonValue(m_expense_id));
    }
    if (m_file_isSet) {
        obj.insert(QString("file"), ::OpenAPI::toJsonValue(m_file));
    }
    if (m_file_extension_isSet) {
        obj.insert(QString("file_extension"), ::OpenAPI::toJsonValue(m_file_extension));
    }
    if (m_file_original_name_isSet) {
        obj.insert(QString("file_original_name"), ::OpenAPI::toJsonValue(m_file_original_name));
    }
    if (m_file_size_isSet) {
        obj.insert(QString("file_size"), ::OpenAPI::toJsonValue(m_file_size));
    }
    if (m_file_type_isSet) {
        obj.insert(QString("file_type"), ::OpenAPI::toJsonValue(m_file_type));
    }
    if (m_file_url_isSet) {
        obj.insert(QString("file_url"), ::OpenAPI::toJsonValue(m_file_url));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    return obj;
}

QString OAIExpenseFile::getCreated() const {
    return m_created;
}
void OAIExpenseFile::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIExpenseFile::is_created_Set() const{
    return m_created_isSet;
}

bool OAIExpenseFile::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIExpenseFile::getCreatedById() const {
    return m_created_by_id;
}
void OAIExpenseFile::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIExpenseFile::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIExpenseFile::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIExpenseFile::getDeleted() const {
    return m_deleted;
}
void OAIExpenseFile::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIExpenseFile::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIExpenseFile::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIExpenseFile::getDescription() const {
    return m_description;
}
void OAIExpenseFile::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIExpenseFile::is_description_Set() const{
    return m_description_isSet;
}

bool OAIExpenseFile::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIExpenseFile::getExpenseId() const {
    return m_expense_id;
}
void OAIExpenseFile::setExpenseId(const QString &expense_id) {
    m_expense_id = expense_id;
    m_expense_id_isSet = true;
}

bool OAIExpenseFile::is_expense_id_Set() const{
    return m_expense_id_isSet;
}

bool OAIExpenseFile::is_expense_id_Valid() const{
    return m_expense_id_isValid;
}

QString OAIExpenseFile::getFile() const {
    return m_file;
}
void OAIExpenseFile::setFile(const QString &file) {
    m_file = file;
    m_file_isSet = true;
}

bool OAIExpenseFile::is_file_Set() const{
    return m_file_isSet;
}

bool OAIExpenseFile::is_file_Valid() const{
    return m_file_isValid;
}

QString OAIExpenseFile::getFileExtension() const {
    return m_file_extension;
}
void OAIExpenseFile::setFileExtension(const QString &file_extension) {
    m_file_extension = file_extension;
    m_file_extension_isSet = true;
}

bool OAIExpenseFile::is_file_extension_Set() const{
    return m_file_extension_isSet;
}

bool OAIExpenseFile::is_file_extension_Valid() const{
    return m_file_extension_isValid;
}

QString OAIExpenseFile::getFileOriginalName() const {
    return m_file_original_name;
}
void OAIExpenseFile::setFileOriginalName(const QString &file_original_name) {
    m_file_original_name = file_original_name;
    m_file_original_name_isSet = true;
}

bool OAIExpenseFile::is_file_original_name_Set() const{
    return m_file_original_name_isSet;
}

bool OAIExpenseFile::is_file_original_name_Valid() const{
    return m_file_original_name_isValid;
}

QString OAIExpenseFile::getFileSize() const {
    return m_file_size;
}
void OAIExpenseFile::setFileSize(const QString &file_size) {
    m_file_size = file_size;
    m_file_size_isSet = true;
}

bool OAIExpenseFile::is_file_size_Set() const{
    return m_file_size_isSet;
}

bool OAIExpenseFile::is_file_size_Valid() const{
    return m_file_size_isValid;
}

QString OAIExpenseFile::getFileType() const {
    return m_file_type;
}
void OAIExpenseFile::setFileType(const QString &file_type) {
    m_file_type = file_type;
    m_file_type_isSet = true;
}

bool OAIExpenseFile::is_file_type_Set() const{
    return m_file_type_isSet;
}

bool OAIExpenseFile::is_file_type_Valid() const{
    return m_file_type_isValid;
}

QString OAIExpenseFile::getFileUrl() const {
    return m_file_url;
}
void OAIExpenseFile::setFileUrl(const QString &file_url) {
    m_file_url = file_url;
    m_file_url_isSet = true;
}

bool OAIExpenseFile::is_file_url_Set() const{
    return m_file_url_isSet;
}

bool OAIExpenseFile::is_file_url_Valid() const{
    return m_file_url_isValid;
}

QString OAIExpenseFile::getId() const {
    return m_id;
}
void OAIExpenseFile::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIExpenseFile::is_id_Set() const{
    return m_id_isSet;
}

bool OAIExpenseFile::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIExpenseFile::getModified() const {
    return m_modified;
}
void OAIExpenseFile::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIExpenseFile::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIExpenseFile::is_modified_Valid() const{
    return m_modified_isValid;
}

bool OAIExpenseFile::isSet() const {
    bool isObjectUpdated = false;
    do {
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

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expense_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_extension_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_original_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_url_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIExpenseFile::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
