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

#include "OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data() {
    this->initializeModel();
}

OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::~OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data() {}

void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::initializeModel() {

    m_companies_vendor_id_isSet = false;
    m_companies_vendor_id_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_dir_isSet = false;
    m_dir_isValid = false;

    m_file_isSet = false;
    m_file_isValid = false;

    m_finished_isSet = false;
    m_finished_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_original_file_name_isSet = false;
    m_original_file_name_isValid = false;

    m_progress_isSet = false;
    m_progress_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_vendor_products_count_isSet = false;
    m_vendor_products_count_isValid = false;

    m_vendor_products_count_total_isSet = false;
    m_vendor_products_count_total_isValid = false;

    m_download_link_isSet = false;
    m_download_link_isValid = false;
}

void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::fromJsonObject(QJsonObject json) {

    m_companies_vendor_id_isValid = ::OpenAPI::fromJsonValue(m_companies_vendor_id, json[QString("companies_vendor_id")]);
    m_companies_vendor_id_isSet = !json[QString("companies_vendor_id")].isNull() && m_companies_vendor_id_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_dir_isValid = ::OpenAPI::fromJsonValue(m_dir, json[QString("dir")]);
    m_dir_isSet = !json[QString("dir")].isNull() && m_dir_isValid;

    m_file_isValid = ::OpenAPI::fromJsonValue(m_file, json[QString("file")]);
    m_file_isSet = !json[QString("file")].isNull() && m_file_isValid;

    m_finished_isValid = ::OpenAPI::fromJsonValue(m_finished, json[QString("finished")]);
    m_finished_isSet = !json[QString("finished")].isNull() && m_finished_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_original_file_name_isValid = ::OpenAPI::fromJsonValue(m_original_file_name, json[QString("original_file_name")]);
    m_original_file_name_isSet = !json[QString("original_file_name")].isNull() && m_original_file_name_isValid;

    m_progress_isValid = ::OpenAPI::fromJsonValue(m_progress, json[QString("progress")]);
    m_progress_isSet = !json[QString("progress")].isNull() && m_progress_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_vendor_products_count_isValid = ::OpenAPI::fromJsonValue(m_vendor_products_count, json[QString("vendor_products_count")]);
    m_vendor_products_count_isSet = !json[QString("vendor_products_count")].isNull() && m_vendor_products_count_isValid;

    m_vendor_products_count_total_isValid = ::OpenAPI::fromJsonValue(m_vendor_products_count_total, json[QString("vendor_products_count_total")]);
    m_vendor_products_count_total_isSet = !json[QString("vendor_products_count_total")].isNull() && m_vendor_products_count_total_isValid;

    m_download_link_isValid = ::OpenAPI::fromJsonValue(m_download_link, json[QString("download_link")]);
    m_download_link_isSet = !json[QString("download_link")].isNull() && m_download_link_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::asJsonObject() const {
    QJsonObject obj;
    if (m_companies_vendor_id_isSet) {
        obj.insert(QString("companies_vendor_id"), ::OpenAPI::toJsonValue(m_companies_vendor_id));
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
    if (m_dir_isSet) {
        obj.insert(QString("dir"), ::OpenAPI::toJsonValue(m_dir));
    }
    if (m_file_isSet) {
        obj.insert(QString("file"), ::OpenAPI::toJsonValue(m_file));
    }
    if (m_finished_isSet) {
        obj.insert(QString("finished"), ::OpenAPI::toJsonValue(m_finished));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_original_file_name_isSet) {
        obj.insert(QString("original_file_name"), ::OpenAPI::toJsonValue(m_original_file_name));
    }
    if (m_progress_isSet) {
        obj.insert(QString("progress"), ::OpenAPI::toJsonValue(m_progress));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_vendor_products_count_isSet) {
        obj.insert(QString("vendor_products_count"), ::OpenAPI::toJsonValue(m_vendor_products_count));
    }
    if (m_vendor_products_count_total_isSet) {
        obj.insert(QString("vendor_products_count_total"), ::OpenAPI::toJsonValue(m_vendor_products_count_total));
    }
    if (m_download_link_isSet) {
        obj.insert(QString("download_link"), ::OpenAPI::toJsonValue(m_download_link));
    }
    return obj;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getCompaniesVendorId() const {
    return m_companies_vendor_id;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setCompaniesVendorId(const QString &companies_vendor_id) {
    m_companies_vendor_id = companies_vendor_id;
    m_companies_vendor_id_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_companies_vendor_id_Set() const{
    return m_companies_vendor_id_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_companies_vendor_id_Valid() const{
    return m_companies_vendor_id_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getCreated() const {
    return m_created;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_created_Set() const{
    return m_created_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_created_Valid() const{
    return m_created_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getCreatedById() const {
    return m_created_by_id;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getDeleted() const {
    return m_deleted;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getDir() const {
    return m_dir;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setDir(const QString &dir) {
    m_dir = dir;
    m_dir_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_dir_Set() const{
    return m_dir_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_dir_Valid() const{
    return m_dir_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getFile() const {
    return m_file;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setFile(const QString &file) {
    m_file = file;
    m_file_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_file_Set() const{
    return m_file_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_file_Valid() const{
    return m_file_isValid;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::isFinished() const {
    return m_finished;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setFinished(const bool &finished) {
    m_finished = finished;
    m_finished_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_finished_Set() const{
    return m_finished_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_finished_Valid() const{
    return m_finished_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getId() const {
    return m_id;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_id_Set() const{
    return m_id_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_id_Valid() const{
    return m_id_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getModified() const {
    return m_modified;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getOriginalFileName() const {
    return m_original_file_name;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setOriginalFileName(const QString &original_file_name) {
    m_original_file_name = original_file_name;
    m_original_file_name_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_original_file_name_Set() const{
    return m_original_file_name_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_original_file_name_Valid() const{
    return m_original_file_name_isValid;
}

qint32 OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getProgress() const {
    return m_progress;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setProgress(const qint32 &progress) {
    m_progress = progress;
    m_progress_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_progress_Set() const{
    return m_progress_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_progress_Valid() const{
    return m_progress_isValid;
}

qint32 OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getSize() const {
    return m_size;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setSize(const qint32 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_size_Set() const{
    return m_size_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_size_Valid() const{
    return m_size_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getStatus() const {
    return m_status;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_status_Set() const{
    return m_status_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_status_Valid() const{
    return m_status_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getType() const {
    return m_type;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_type_Set() const{
    return m_type_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_type_Valid() const{
    return m_type_isValid;
}

qint32 OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getVendorProductsCount() const {
    return m_vendor_products_count;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setVendorProductsCount(const qint32 &vendor_products_count) {
    m_vendor_products_count = vendor_products_count;
    m_vendor_products_count_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_vendor_products_count_Set() const{
    return m_vendor_products_count_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_vendor_products_count_Valid() const{
    return m_vendor_products_count_isValid;
}

qint32 OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getVendorProductsCountTotal() const {
    return m_vendor_products_count_total;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setVendorProductsCountTotal(const qint32 &vendor_products_count_total) {
    m_vendor_products_count_total = vendor_products_count_total;
    m_vendor_products_count_total_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_vendor_products_count_total_Set() const{
    return m_vendor_products_count_total_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_vendor_products_count_total_Valid() const{
    return m_vendor_products_count_total_isValid;
}

QString OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::getDownloadLink() const {
    return m_download_link;
}
void OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::setDownloadLink(const QString &download_link) {
    m_download_link = download_link;
    m_download_link_isSet = true;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_download_link_Set() const{
    return m_download_link_isSet;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::is_download_link_Valid() const{
    return m_download_link_isValid;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_companies_vendor_id_isSet) {
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

        if (m_dir_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_finished_isSet) {
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

        if (m_original_file_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_progress_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_products_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_products_count_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_download_link_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
