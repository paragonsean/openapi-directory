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

#include "OAI_invoices_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_invoices_post_request::OAI_invoices_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_invoices_post_request::OAI_invoices_post_request() {
    this->initializeModel();
}

OAI_invoices_post_request::~OAI_invoices_post_request() {}

void OAI_invoices_post_request::initializeModel() {

    m_contact_id_isSet = false;
    m_contact_id_isValid = false;

    m_created_or_modified_gte_isSet = false;
    m_created_or_modified_gte_isValid = false;

    m_date_from_isSet = false;
    m_date_from_isValid = false;

    m_date_to_isSet = false;
    m_date_to_isValid = false;

    m_erp_id_isSet = false;
    m_erp_id_isValid = false;

    m_erp_payment_term_id_isSet = false;
    m_erp_payment_term_id_isValid = false;

    m_invoice_number_isSet = false;
    m_invoice_number_isValid = false;

    m_is_draft_isSet = false;
    m_is_draft_isValid = false;

    m_is_locked_isSet = false;
    m_is_locked_isValid = false;

    m_is_offer_isSet = false;
    m_is_offer_isValid = false;

    m_issued_date_isSet = false;
    m_issued_date_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_offer_number_isSet = false;
    m_offer_number_isValid = false;

    m_payment_due_date_isSet = false;
    m_payment_due_date_isValid = false;

    m_payment_term_id_isSet = false;
    m_payment_term_id_isValid = false;

    m_project_id_isSet = false;
    m_project_id_isValid = false;

    m_reference_isSet = false;
    m_reference_isValid = false;

    m_vat_percent_isSet = false;
    m_vat_percent_isValid = false;
}

void OAI_invoices_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_invoices_post_request::fromJsonObject(QJsonObject json) {

    m_contact_id_isValid = ::OpenAPI::fromJsonValue(m_contact_id, json[QString("contact_id")]);
    m_contact_id_isSet = !json[QString("contact_id")].isNull() && m_contact_id_isValid;

    m_created_or_modified_gte_isValid = ::OpenAPI::fromJsonValue(m_created_or_modified_gte, json[QString("created_or_modified_gte")]);
    m_created_or_modified_gte_isSet = !json[QString("created_or_modified_gte")].isNull() && m_created_or_modified_gte_isValid;

    m_date_from_isValid = ::OpenAPI::fromJsonValue(m_date_from, json[QString("date_from")]);
    m_date_from_isSet = !json[QString("date_from")].isNull() && m_date_from_isValid;

    m_date_to_isValid = ::OpenAPI::fromJsonValue(m_date_to, json[QString("date_to")]);
    m_date_to_isSet = !json[QString("date_to")].isNull() && m_date_to_isValid;

    m_erp_id_isValid = ::OpenAPI::fromJsonValue(m_erp_id, json[QString("erp_id")]);
    m_erp_id_isSet = !json[QString("erp_id")].isNull() && m_erp_id_isValid;

    m_erp_payment_term_id_isValid = ::OpenAPI::fromJsonValue(m_erp_payment_term_id, json[QString("erp_payment_term_id")]);
    m_erp_payment_term_id_isSet = !json[QString("erp_payment_term_id")].isNull() && m_erp_payment_term_id_isValid;

    m_invoice_number_isValid = ::OpenAPI::fromJsonValue(m_invoice_number, json[QString("invoice_number")]);
    m_invoice_number_isSet = !json[QString("invoice_number")].isNull() && m_invoice_number_isValid;

    m_is_draft_isValid = ::OpenAPI::fromJsonValue(m_is_draft, json[QString("is_draft")]);
    m_is_draft_isSet = !json[QString("is_draft")].isNull() && m_is_draft_isValid;

    m_is_locked_isValid = ::OpenAPI::fromJsonValue(m_is_locked, json[QString("is_locked")]);
    m_is_locked_isSet = !json[QString("is_locked")].isNull() && m_is_locked_isValid;

    m_is_offer_isValid = ::OpenAPI::fromJsonValue(m_is_offer, json[QString("is_offer")]);
    m_is_offer_isSet = !json[QString("is_offer")].isNull() && m_is_offer_isValid;

    m_issued_date_isValid = ::OpenAPI::fromJsonValue(m_issued_date, json[QString("issued_date")]);
    m_issued_date_isSet = !json[QString("issued_date")].isNull() && m_issued_date_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_offer_number_isValid = ::OpenAPI::fromJsonValue(m_offer_number, json[QString("offer_number")]);
    m_offer_number_isSet = !json[QString("offer_number")].isNull() && m_offer_number_isValid;

    m_payment_due_date_isValid = ::OpenAPI::fromJsonValue(m_payment_due_date, json[QString("payment_due_date")]);
    m_payment_due_date_isSet = !json[QString("payment_due_date")].isNull() && m_payment_due_date_isValid;

    m_payment_term_id_isValid = ::OpenAPI::fromJsonValue(m_payment_term_id, json[QString("payment_term_id")]);
    m_payment_term_id_isSet = !json[QString("payment_term_id")].isNull() && m_payment_term_id_isValid;

    m_project_id_isValid = ::OpenAPI::fromJsonValue(m_project_id, json[QString("project_id")]);
    m_project_id_isSet = !json[QString("project_id")].isNull() && m_project_id_isValid;

    m_reference_isValid = ::OpenAPI::fromJsonValue(m_reference, json[QString("reference")]);
    m_reference_isSet = !json[QString("reference")].isNull() && m_reference_isValid;

    m_vat_percent_isValid = ::OpenAPI::fromJsonValue(m_vat_percent, json[QString("vat_percent")]);
    m_vat_percent_isSet = !json[QString("vat_percent")].isNull() && m_vat_percent_isValid;
}

QString OAI_invoices_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_invoices_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_contact_id_isSet) {
        obj.insert(QString("contact_id"), ::OpenAPI::toJsonValue(m_contact_id));
    }
    if (m_created_or_modified_gte_isSet) {
        obj.insert(QString("created_or_modified_gte"), ::OpenAPI::toJsonValue(m_created_or_modified_gte));
    }
    if (m_date_from_isSet) {
        obj.insert(QString("date_from"), ::OpenAPI::toJsonValue(m_date_from));
    }
    if (m_date_to_isSet) {
        obj.insert(QString("date_to"), ::OpenAPI::toJsonValue(m_date_to));
    }
    if (m_erp_id_isSet) {
        obj.insert(QString("erp_id"), ::OpenAPI::toJsonValue(m_erp_id));
    }
    if (m_erp_payment_term_id_isSet) {
        obj.insert(QString("erp_payment_term_id"), ::OpenAPI::toJsonValue(m_erp_payment_term_id));
    }
    if (m_invoice_number_isSet) {
        obj.insert(QString("invoice_number"), ::OpenAPI::toJsonValue(m_invoice_number));
    }
    if (m_is_draft_isSet) {
        obj.insert(QString("is_draft"), ::OpenAPI::toJsonValue(m_is_draft));
    }
    if (m_is_locked_isSet) {
        obj.insert(QString("is_locked"), ::OpenAPI::toJsonValue(m_is_locked));
    }
    if (m_is_offer_isSet) {
        obj.insert(QString("is_offer"), ::OpenAPI::toJsonValue(m_is_offer));
    }
    if (m_issued_date_isSet) {
        obj.insert(QString("issued_date"), ::OpenAPI::toJsonValue(m_issued_date));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_offer_number_isSet) {
        obj.insert(QString("offer_number"), ::OpenAPI::toJsonValue(m_offer_number));
    }
    if (m_payment_due_date_isSet) {
        obj.insert(QString("payment_due_date"), ::OpenAPI::toJsonValue(m_payment_due_date));
    }
    if (m_payment_term_id_isSet) {
        obj.insert(QString("payment_term_id"), ::OpenAPI::toJsonValue(m_payment_term_id));
    }
    if (m_project_id_isSet) {
        obj.insert(QString("project_id"), ::OpenAPI::toJsonValue(m_project_id));
    }
    if (m_reference_isSet) {
        obj.insert(QString("reference"), ::OpenAPI::toJsonValue(m_reference));
    }
    if (m_vat_percent_isSet) {
        obj.insert(QString("vat_percent"), ::OpenAPI::toJsonValue(m_vat_percent));
    }
    return obj;
}

QString OAI_invoices_post_request::getContactId() const {
    return m_contact_id;
}
void OAI_invoices_post_request::setContactId(const QString &contact_id) {
    m_contact_id = contact_id;
    m_contact_id_isSet = true;
}

bool OAI_invoices_post_request::is_contact_id_Set() const{
    return m_contact_id_isSet;
}

bool OAI_invoices_post_request::is_contact_id_Valid() const{
    return m_contact_id_isValid;
}

QDate OAI_invoices_post_request::getCreatedOrModifiedGte() const {
    return m_created_or_modified_gte;
}
void OAI_invoices_post_request::setCreatedOrModifiedGte(const QDate &created_or_modified_gte) {
    m_created_or_modified_gte = created_or_modified_gte;
    m_created_or_modified_gte_isSet = true;
}

bool OAI_invoices_post_request::is_created_or_modified_gte_Set() const{
    return m_created_or_modified_gte_isSet;
}

bool OAI_invoices_post_request::is_created_or_modified_gte_Valid() const{
    return m_created_or_modified_gte_isValid;
}

QDate OAI_invoices_post_request::getDateFrom() const {
    return m_date_from;
}
void OAI_invoices_post_request::setDateFrom(const QDate &date_from) {
    m_date_from = date_from;
    m_date_from_isSet = true;
}

bool OAI_invoices_post_request::is_date_from_Set() const{
    return m_date_from_isSet;
}

bool OAI_invoices_post_request::is_date_from_Valid() const{
    return m_date_from_isValid;
}

QDate OAI_invoices_post_request::getDateTo() const {
    return m_date_to;
}
void OAI_invoices_post_request::setDateTo(const QDate &date_to) {
    m_date_to = date_to;
    m_date_to_isSet = true;
}

bool OAI_invoices_post_request::is_date_to_Set() const{
    return m_date_to_isSet;
}

bool OAI_invoices_post_request::is_date_to_Valid() const{
    return m_date_to_isValid;
}

QString OAI_invoices_post_request::getErpId() const {
    return m_erp_id;
}
void OAI_invoices_post_request::setErpId(const QString &erp_id) {
    m_erp_id = erp_id;
    m_erp_id_isSet = true;
}

bool OAI_invoices_post_request::is_erp_id_Set() const{
    return m_erp_id_isSet;
}

bool OAI_invoices_post_request::is_erp_id_Valid() const{
    return m_erp_id_isValid;
}

QString OAI_invoices_post_request::getErpPaymentTermId() const {
    return m_erp_payment_term_id;
}
void OAI_invoices_post_request::setErpPaymentTermId(const QString &erp_payment_term_id) {
    m_erp_payment_term_id = erp_payment_term_id;
    m_erp_payment_term_id_isSet = true;
}

bool OAI_invoices_post_request::is_erp_payment_term_id_Set() const{
    return m_erp_payment_term_id_isSet;
}

bool OAI_invoices_post_request::is_erp_payment_term_id_Valid() const{
    return m_erp_payment_term_id_isValid;
}

qint32 OAI_invoices_post_request::getInvoiceNumber() const {
    return m_invoice_number;
}
void OAI_invoices_post_request::setInvoiceNumber(const qint32 &invoice_number) {
    m_invoice_number = invoice_number;
    m_invoice_number_isSet = true;
}

bool OAI_invoices_post_request::is_invoice_number_Set() const{
    return m_invoice_number_isSet;
}

bool OAI_invoices_post_request::is_invoice_number_Valid() const{
    return m_invoice_number_isValid;
}

bool OAI_invoices_post_request::isIsDraft() const {
    return m_is_draft;
}
void OAI_invoices_post_request::setIsDraft(const bool &is_draft) {
    m_is_draft = is_draft;
    m_is_draft_isSet = true;
}

bool OAI_invoices_post_request::is_is_draft_Set() const{
    return m_is_draft_isSet;
}

bool OAI_invoices_post_request::is_is_draft_Valid() const{
    return m_is_draft_isValid;
}

bool OAI_invoices_post_request::isIsLocked() const {
    return m_is_locked;
}
void OAI_invoices_post_request::setIsLocked(const bool &is_locked) {
    m_is_locked = is_locked;
    m_is_locked_isSet = true;
}

bool OAI_invoices_post_request::is_is_locked_Set() const{
    return m_is_locked_isSet;
}

bool OAI_invoices_post_request::is_is_locked_Valid() const{
    return m_is_locked_isValid;
}

bool OAI_invoices_post_request::isIsOffer() const {
    return m_is_offer;
}
void OAI_invoices_post_request::setIsOffer(const bool &is_offer) {
    m_is_offer = is_offer;
    m_is_offer_isSet = true;
}

bool OAI_invoices_post_request::is_is_offer_Set() const{
    return m_is_offer_isSet;
}

bool OAI_invoices_post_request::is_is_offer_Valid() const{
    return m_is_offer_isValid;
}

QDate OAI_invoices_post_request::getIssuedDate() const {
    return m_issued_date;
}
void OAI_invoices_post_request::setIssuedDate(const QDate &issued_date) {
    m_issued_date = issued_date;
    m_issued_date_isSet = true;
}

bool OAI_invoices_post_request::is_issued_date_Set() const{
    return m_issued_date_isSet;
}

bool OAI_invoices_post_request::is_issued_date_Valid() const{
    return m_issued_date_isValid;
}

QString OAI_invoices_post_request::getMessage() const {
    return m_message;
}
void OAI_invoices_post_request::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAI_invoices_post_request::is_message_Set() const{
    return m_message_isSet;
}

bool OAI_invoices_post_request::is_message_Valid() const{
    return m_message_isValid;
}

qint32 OAI_invoices_post_request::getOfferNumber() const {
    return m_offer_number;
}
void OAI_invoices_post_request::setOfferNumber(const qint32 &offer_number) {
    m_offer_number = offer_number;
    m_offer_number_isSet = true;
}

bool OAI_invoices_post_request::is_offer_number_Set() const{
    return m_offer_number_isSet;
}

bool OAI_invoices_post_request::is_offer_number_Valid() const{
    return m_offer_number_isValid;
}

QDate OAI_invoices_post_request::getPaymentDueDate() const {
    return m_payment_due_date;
}
void OAI_invoices_post_request::setPaymentDueDate(const QDate &payment_due_date) {
    m_payment_due_date = payment_due_date;
    m_payment_due_date_isSet = true;
}

bool OAI_invoices_post_request::is_payment_due_date_Set() const{
    return m_payment_due_date_isSet;
}

bool OAI_invoices_post_request::is_payment_due_date_Valid() const{
    return m_payment_due_date_isValid;
}

QString OAI_invoices_post_request::getPaymentTermId() const {
    return m_payment_term_id;
}
void OAI_invoices_post_request::setPaymentTermId(const QString &payment_term_id) {
    m_payment_term_id = payment_term_id;
    m_payment_term_id_isSet = true;
}

bool OAI_invoices_post_request::is_payment_term_id_Set() const{
    return m_payment_term_id_isSet;
}

bool OAI_invoices_post_request::is_payment_term_id_Valid() const{
    return m_payment_term_id_isValid;
}

QString OAI_invoices_post_request::getProjectId() const {
    return m_project_id;
}
void OAI_invoices_post_request::setProjectId(const QString &project_id) {
    m_project_id = project_id;
    m_project_id_isSet = true;
}

bool OAI_invoices_post_request::is_project_id_Set() const{
    return m_project_id_isSet;
}

bool OAI_invoices_post_request::is_project_id_Valid() const{
    return m_project_id_isValid;
}

QString OAI_invoices_post_request::getReference() const {
    return m_reference;
}
void OAI_invoices_post_request::setReference(const QString &reference) {
    m_reference = reference;
    m_reference_isSet = true;
}

bool OAI_invoices_post_request::is_reference_Set() const{
    return m_reference_isSet;
}

bool OAI_invoices_post_request::is_reference_Valid() const{
    return m_reference_isValid;
}

qint32 OAI_invoices_post_request::getVatPercent() const {
    return m_vat_percent;
}
void OAI_invoices_post_request::setVatPercent(const qint32 &vat_percent) {
    m_vat_percent = vat_percent;
    m_vat_percent_isSet = true;
}

bool OAI_invoices_post_request::is_vat_percent_Set() const{
    return m_vat_percent_isSet;
}

bool OAI_invoices_post_request::is_vat_percent_Valid() const{
    return m_vat_percent_isValid;
}

bool OAI_invoices_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contact_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_or_modified_gte_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_erp_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_erp_payment_term_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_draft_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_locked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_offer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_issued_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offer_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_due_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_term_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_percent_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_invoices_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
