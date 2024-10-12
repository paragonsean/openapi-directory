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

#include "OAIExpense.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExpense::OAIExpense(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExpense::OAIExpense() {
    this->initializeModel();
}

OAIExpense::~OAIExpense() {}

void OAIExpense::initializeModel() {

    m_activity_id_isSet = false;
    m_activity_id_isValid = false;

    m_comment_isSet = false;
    m_comment_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_contact_id_isSet = false;
    m_contact_id_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_currency_id_isSet = false;
    m_currency_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_delivery_date_isSet = false;
    m_delivery_date_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_due_date_isSet = false;
    m_due_date_isValid = false;

    m_file_reference_isSet = false;
    m_file_reference_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_imported_isSet = false;
    m_is_imported_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_order_number_isSet = false;
    m_order_number_isValid = false;

    m_project_id_isSet = false;
    m_project_id_isValid = false;

    m_readsoft_id_isSet = false;
    m_readsoft_id_isValid = false;

    m_reference_isSet = false;
    m_reference_isValid = false;

    m_roger_id_isSet = false;
    m_roger_id_isValid = false;

    m_sent_to_email_isSet = false;
    m_sent_to_email_isValid = false;

    m_short_text_isSet = false;
    m_short_text_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_supplier_invoice_number_isSet = false;
    m_supplier_invoice_number_isValid = false;

    m_total_buying_price_isSet = false;
    m_total_buying_price_isValid = false;

    m_total_selling_price_isSet = false;
    m_total_selling_price_isValid = false;
}

void OAIExpense::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExpense::fromJsonObject(QJsonObject json) {

    m_activity_id_isValid = ::OpenAPI::fromJsonValue(m_activity_id, json[QString("activity_id")]);
    m_activity_id_isSet = !json[QString("activity_id")].isNull() && m_activity_id_isValid;

    m_comment_isValid = ::OpenAPI::fromJsonValue(m_comment, json[QString("comment")]);
    m_comment_isSet = !json[QString("comment")].isNull() && m_comment_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_contact_id_isValid = ::OpenAPI::fromJsonValue(m_contact_id, json[QString("contact_id")]);
    m_contact_id_isSet = !json[QString("contact_id")].isNull() && m_contact_id_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_currency_id_isValid = ::OpenAPI::fromJsonValue(m_currency_id, json[QString("currency_id")]);
    m_currency_id_isSet = !json[QString("currency_id")].isNull() && m_currency_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_delivery_date_isValid = ::OpenAPI::fromJsonValue(m_delivery_date, json[QString("delivery_date")]);
    m_delivery_date_isSet = !json[QString("delivery_date")].isNull() && m_delivery_date_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_due_date_isValid = ::OpenAPI::fromJsonValue(m_due_date, json[QString("due_date")]);
    m_due_date_isSet = !json[QString("due_date")].isNull() && m_due_date_isValid;

    m_file_reference_isValid = ::OpenAPI::fromJsonValue(m_file_reference, json[QString("file_reference")]);
    m_file_reference_isSet = !json[QString("file_reference")].isNull() && m_file_reference_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_imported_isValid = ::OpenAPI::fromJsonValue(m_is_imported, json[QString("is_imported")]);
    m_is_imported_isSet = !json[QString("is_imported")].isNull() && m_is_imported_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_order_number_isValid = ::OpenAPI::fromJsonValue(m_order_number, json[QString("order_number")]);
    m_order_number_isSet = !json[QString("order_number")].isNull() && m_order_number_isValid;

    m_project_id_isValid = ::OpenAPI::fromJsonValue(m_project_id, json[QString("project_id")]);
    m_project_id_isSet = !json[QString("project_id")].isNull() && m_project_id_isValid;

    m_readsoft_id_isValid = ::OpenAPI::fromJsonValue(m_readsoft_id, json[QString("readsoft_id")]);
    m_readsoft_id_isSet = !json[QString("readsoft_id")].isNull() && m_readsoft_id_isValid;

    m_reference_isValid = ::OpenAPI::fromJsonValue(m_reference, json[QString("reference")]);
    m_reference_isSet = !json[QString("reference")].isNull() && m_reference_isValid;

    m_roger_id_isValid = ::OpenAPI::fromJsonValue(m_roger_id, json[QString("roger_id")]);
    m_roger_id_isSet = !json[QString("roger_id")].isNull() && m_roger_id_isValid;

    m_sent_to_email_isValid = ::OpenAPI::fromJsonValue(m_sent_to_email, json[QString("sent_to_email")]);
    m_sent_to_email_isSet = !json[QString("sent_to_email")].isNull() && m_sent_to_email_isValid;

    m_short_text_isValid = ::OpenAPI::fromJsonValue(m_short_text, json[QString("short_text")]);
    m_short_text_isSet = !json[QString("short_text")].isNull() && m_short_text_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_supplier_invoice_number_isValid = ::OpenAPI::fromJsonValue(m_supplier_invoice_number, json[QString("supplier_invoice_number")]);
    m_supplier_invoice_number_isSet = !json[QString("supplier_invoice_number")].isNull() && m_supplier_invoice_number_isValid;

    m_total_buying_price_isValid = ::OpenAPI::fromJsonValue(m_total_buying_price, json[QString("total_buying_price")]);
    m_total_buying_price_isSet = !json[QString("total_buying_price")].isNull() && m_total_buying_price_isValid;

    m_total_selling_price_isValid = ::OpenAPI::fromJsonValue(m_total_selling_price, json[QString("total_selling_price")]);
    m_total_selling_price_isSet = !json[QString("total_selling_price")].isNull() && m_total_selling_price_isValid;
}

QString OAIExpense::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExpense::asJsonObject() const {
    QJsonObject obj;
    if (m_activity_id_isSet) {
        obj.insert(QString("activity_id"), ::OpenAPI::toJsonValue(m_activity_id));
    }
    if (m_comment_isSet) {
        obj.insert(QString("comment"), ::OpenAPI::toJsonValue(m_comment));
    }
    if (m_company_id_isSet) {
        obj.insert(QString("company_id"), ::OpenAPI::toJsonValue(m_company_id));
    }
    if (m_contact_id_isSet) {
        obj.insert(QString("contact_id"), ::OpenAPI::toJsonValue(m_contact_id));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_created_by_id_isSet) {
        obj.insert(QString("created_by_id"), ::OpenAPI::toJsonValue(m_created_by_id));
    }
    if (m_currency_id_isSet) {
        obj.insert(QString("currency_id"), ::OpenAPI::toJsonValue(m_currency_id));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_delivery_date_isSet) {
        obj.insert(QString("delivery_date"), ::OpenAPI::toJsonValue(m_delivery_date));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_due_date_isSet) {
        obj.insert(QString("due_date"), ::OpenAPI::toJsonValue(m_due_date));
    }
    if (m_file_reference_isSet) {
        obj.insert(QString("file_reference"), ::OpenAPI::toJsonValue(m_file_reference));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_imported_isSet) {
        obj.insert(QString("is_imported"), ::OpenAPI::toJsonValue(m_is_imported));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_order_number_isSet) {
        obj.insert(QString("order_number"), ::OpenAPI::toJsonValue(m_order_number));
    }
    if (m_project_id_isSet) {
        obj.insert(QString("project_id"), ::OpenAPI::toJsonValue(m_project_id));
    }
    if (m_readsoft_id_isSet) {
        obj.insert(QString("readsoft_id"), ::OpenAPI::toJsonValue(m_readsoft_id));
    }
    if (m_reference_isSet) {
        obj.insert(QString("reference"), ::OpenAPI::toJsonValue(m_reference));
    }
    if (m_roger_id_isSet) {
        obj.insert(QString("roger_id"), ::OpenAPI::toJsonValue(m_roger_id));
    }
    if (m_sent_to_email_isSet) {
        obj.insert(QString("sent_to_email"), ::OpenAPI::toJsonValue(m_sent_to_email));
    }
    if (m_short_text_isSet) {
        obj.insert(QString("short_text"), ::OpenAPI::toJsonValue(m_short_text));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_supplier_invoice_number_isSet) {
        obj.insert(QString("supplier_invoice_number"), ::OpenAPI::toJsonValue(m_supplier_invoice_number));
    }
    if (m_total_buying_price_isSet) {
        obj.insert(QString("total_buying_price"), ::OpenAPI::toJsonValue(m_total_buying_price));
    }
    if (m_total_selling_price_isSet) {
        obj.insert(QString("total_selling_price"), ::OpenAPI::toJsonValue(m_total_selling_price));
    }
    return obj;
}

QString OAIExpense::getActivityId() const {
    return m_activity_id;
}
void OAIExpense::setActivityId(const QString &activity_id) {
    m_activity_id = activity_id;
    m_activity_id_isSet = true;
}

bool OAIExpense::is_activity_id_Set() const{
    return m_activity_id_isSet;
}

bool OAIExpense::is_activity_id_Valid() const{
    return m_activity_id_isValid;
}

QString OAIExpense::getComment() const {
    return m_comment;
}
void OAIExpense::setComment(const QString &comment) {
    m_comment = comment;
    m_comment_isSet = true;
}

bool OAIExpense::is_comment_Set() const{
    return m_comment_isSet;
}

bool OAIExpense::is_comment_Valid() const{
    return m_comment_isValid;
}

QString OAIExpense::getCompanyId() const {
    return m_company_id;
}
void OAIExpense::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIExpense::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIExpense::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIExpense::getContactId() const {
    return m_contact_id;
}
void OAIExpense::setContactId(const QString &contact_id) {
    m_contact_id = contact_id;
    m_contact_id_isSet = true;
}

bool OAIExpense::is_contact_id_Set() const{
    return m_contact_id_isSet;
}

bool OAIExpense::is_contact_id_Valid() const{
    return m_contact_id_isValid;
}

QString OAIExpense::getCreated() const {
    return m_created;
}
void OAIExpense::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIExpense::is_created_Set() const{
    return m_created_isSet;
}

bool OAIExpense::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIExpense::getCreatedById() const {
    return m_created_by_id;
}
void OAIExpense::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIExpense::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIExpense::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIExpense::getCurrencyId() const {
    return m_currency_id;
}
void OAIExpense::setCurrencyId(const QString &currency_id) {
    m_currency_id = currency_id;
    m_currency_id_isSet = true;
}

bool OAIExpense::is_currency_id_Set() const{
    return m_currency_id_isSet;
}

bool OAIExpense::is_currency_id_Valid() const{
    return m_currency_id_isValid;
}

QString OAIExpense::getDeleted() const {
    return m_deleted;
}
void OAIExpense::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIExpense::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIExpense::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QDate OAIExpense::getDeliveryDate() const {
    return m_delivery_date;
}
void OAIExpense::setDeliveryDate(const QDate &delivery_date) {
    m_delivery_date = delivery_date;
    m_delivery_date_isSet = true;
}

bool OAIExpense::is_delivery_date_Set() const{
    return m_delivery_date_isSet;
}

bool OAIExpense::is_delivery_date_Valid() const{
    return m_delivery_date_isValid;
}

QString OAIExpense::getDescription() const {
    return m_description;
}
void OAIExpense::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIExpense::is_description_Set() const{
    return m_description_isSet;
}

bool OAIExpense::is_description_Valid() const{
    return m_description_isValid;
}

QDate OAIExpense::getDueDate() const {
    return m_due_date;
}
void OAIExpense::setDueDate(const QDate &due_date) {
    m_due_date = due_date;
    m_due_date_isSet = true;
}

bool OAIExpense::is_due_date_Set() const{
    return m_due_date_isSet;
}

bool OAIExpense::is_due_date_Valid() const{
    return m_due_date_isValid;
}

QString OAIExpense::getFileReference() const {
    return m_file_reference;
}
void OAIExpense::setFileReference(const QString &file_reference) {
    m_file_reference = file_reference;
    m_file_reference_isSet = true;
}

bool OAIExpense::is_file_reference_Set() const{
    return m_file_reference_isSet;
}

bool OAIExpense::is_file_reference_Valid() const{
    return m_file_reference_isValid;
}

QString OAIExpense::getId() const {
    return m_id;
}
void OAIExpense::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIExpense::is_id_Set() const{
    return m_id_isSet;
}

bool OAIExpense::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIExpense::getIsImported() const {
    return m_is_imported;
}
void OAIExpense::setIsImported(const QString &is_imported) {
    m_is_imported = is_imported;
    m_is_imported_isSet = true;
}

bool OAIExpense::is_is_imported_Set() const{
    return m_is_imported_isSet;
}

bool OAIExpense::is_is_imported_Valid() const{
    return m_is_imported_isValid;
}

QString OAIExpense::getModified() const {
    return m_modified;
}
void OAIExpense::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIExpense::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIExpense::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIExpense::getOrderNumber() const {
    return m_order_number;
}
void OAIExpense::setOrderNumber(const QString &order_number) {
    m_order_number = order_number;
    m_order_number_isSet = true;
}

bool OAIExpense::is_order_number_Set() const{
    return m_order_number_isSet;
}

bool OAIExpense::is_order_number_Valid() const{
    return m_order_number_isValid;
}

QString OAIExpense::getProjectId() const {
    return m_project_id;
}
void OAIExpense::setProjectId(const QString &project_id) {
    m_project_id = project_id;
    m_project_id_isSet = true;
}

bool OAIExpense::is_project_id_Set() const{
    return m_project_id_isSet;
}

bool OAIExpense::is_project_id_Valid() const{
    return m_project_id_isValid;
}

QString OAIExpense::getReadsoftId() const {
    return m_readsoft_id;
}
void OAIExpense::setReadsoftId(const QString &readsoft_id) {
    m_readsoft_id = readsoft_id;
    m_readsoft_id_isSet = true;
}

bool OAIExpense::is_readsoft_id_Set() const{
    return m_readsoft_id_isSet;
}

bool OAIExpense::is_readsoft_id_Valid() const{
    return m_readsoft_id_isValid;
}

QString OAIExpense::getReference() const {
    return m_reference;
}
void OAIExpense::setReference(const QString &reference) {
    m_reference = reference;
    m_reference_isSet = true;
}

bool OAIExpense::is_reference_Set() const{
    return m_reference_isSet;
}

bool OAIExpense::is_reference_Valid() const{
    return m_reference_isValid;
}

QString OAIExpense::getRogerId() const {
    return m_roger_id;
}
void OAIExpense::setRogerId(const QString &roger_id) {
    m_roger_id = roger_id;
    m_roger_id_isSet = true;
}

bool OAIExpense::is_roger_id_Set() const{
    return m_roger_id_isSet;
}

bool OAIExpense::is_roger_id_Valid() const{
    return m_roger_id_isValid;
}

QString OAIExpense::getSentToEmail() const {
    return m_sent_to_email;
}
void OAIExpense::setSentToEmail(const QString &sent_to_email) {
    m_sent_to_email = sent_to_email;
    m_sent_to_email_isSet = true;
}

bool OAIExpense::is_sent_to_email_Set() const{
    return m_sent_to_email_isSet;
}

bool OAIExpense::is_sent_to_email_Valid() const{
    return m_sent_to_email_isValid;
}

QString OAIExpense::getShortText() const {
    return m_short_text;
}
void OAIExpense::setShortText(const QString &short_text) {
    m_short_text = short_text;
    m_short_text_isSet = true;
}

bool OAIExpense::is_short_text_Set() const{
    return m_short_text_isSet;
}

bool OAIExpense::is_short_text_Valid() const{
    return m_short_text_isValid;
}

QString OAIExpense::getStatus() const {
    return m_status;
}
void OAIExpense::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIExpense::is_status_Set() const{
    return m_status_isSet;
}

bool OAIExpense::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIExpense::getSupplierInvoiceNumber() const {
    return m_supplier_invoice_number;
}
void OAIExpense::setSupplierInvoiceNumber(const QString &supplier_invoice_number) {
    m_supplier_invoice_number = supplier_invoice_number;
    m_supplier_invoice_number_isSet = true;
}

bool OAIExpense::is_supplier_invoice_number_Set() const{
    return m_supplier_invoice_number_isSet;
}

bool OAIExpense::is_supplier_invoice_number_Valid() const{
    return m_supplier_invoice_number_isValid;
}

float OAIExpense::getTotalBuyingPrice() const {
    return m_total_buying_price;
}
void OAIExpense::setTotalBuyingPrice(const float &total_buying_price) {
    m_total_buying_price = total_buying_price;
    m_total_buying_price_isSet = true;
}

bool OAIExpense::is_total_buying_price_Set() const{
    return m_total_buying_price_isSet;
}

bool OAIExpense::is_total_buying_price_Valid() const{
    return m_total_buying_price_isValid;
}

float OAIExpense::getTotalSellingPrice() const {
    return m_total_selling_price;
}
void OAIExpense::setTotalSellingPrice(const float &total_selling_price) {
    m_total_selling_price = total_selling_price;
    m_total_selling_price_isSet = true;
}

bool OAIExpense::is_total_selling_price_Set() const{
    return m_total_selling_price_isSet;
}

bool OAIExpense::is_total_selling_price_Valid() const{
    return m_total_selling_price_isValid;
}

bool OAIExpense::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_activity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact_id_isSet) {
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

        if (m_currency_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_delivery_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_due_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_imported_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_readsoft_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_roger_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sent_to_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_supplier_invoice_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_buying_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_selling_price_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExpense::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
