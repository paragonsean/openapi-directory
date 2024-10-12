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

#include "OAI_expenses_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_expenses_post_request::OAI_expenses_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_expenses_post_request::OAI_expenses_post_request() {
    this->initializeModel();
}

OAI_expenses_post_request::~OAI_expenses_post_request() {}

void OAI_expenses_post_request::initializeModel() {

    m_contact_id_isSet = false;
    m_contact_id_isValid = false;

    m_currency_id_isSet = false;
    m_currency_id_isValid = false;

    m_delivery_date_isSet = false;
    m_delivery_date_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_project_id_isSet = false;
    m_project_id_isValid = false;

    m_reference_isSet = false;
    m_reference_isValid = false;

    m_short_text_isSet = false;
    m_short_text_isValid = false;

    m_supplier_invoice_number_isSet = false;
    m_supplier_invoice_number_isValid = false;
}

void OAI_expenses_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_expenses_post_request::fromJsonObject(QJsonObject json) {

    m_contact_id_isValid = ::OpenAPI::fromJsonValue(m_contact_id, json[QString("contact_id")]);
    m_contact_id_isSet = !json[QString("contact_id")].isNull() && m_contact_id_isValid;

    m_currency_id_isValid = ::OpenAPI::fromJsonValue(m_currency_id, json[QString("currency_id")]);
    m_currency_id_isSet = !json[QString("currency_id")].isNull() && m_currency_id_isValid;

    m_delivery_date_isValid = ::OpenAPI::fromJsonValue(m_delivery_date, json[QString("delivery_date")]);
    m_delivery_date_isSet = !json[QString("delivery_date")].isNull() && m_delivery_date_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_project_id_isValid = ::OpenAPI::fromJsonValue(m_project_id, json[QString("project_id")]);
    m_project_id_isSet = !json[QString("project_id")].isNull() && m_project_id_isValid;

    m_reference_isValid = ::OpenAPI::fromJsonValue(m_reference, json[QString("reference")]);
    m_reference_isSet = !json[QString("reference")].isNull() && m_reference_isValid;

    m_short_text_isValid = ::OpenAPI::fromJsonValue(m_short_text, json[QString("short_text")]);
    m_short_text_isSet = !json[QString("short_text")].isNull() && m_short_text_isValid;

    m_supplier_invoice_number_isValid = ::OpenAPI::fromJsonValue(m_supplier_invoice_number, json[QString("supplier_invoice_number")]);
    m_supplier_invoice_number_isSet = !json[QString("supplier_invoice_number")].isNull() && m_supplier_invoice_number_isValid;
}

QString OAI_expenses_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_expenses_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_contact_id_isSet) {
        obj.insert(QString("contact_id"), ::OpenAPI::toJsonValue(m_contact_id));
    }
    if (m_currency_id_isSet) {
        obj.insert(QString("currency_id"), ::OpenAPI::toJsonValue(m_currency_id));
    }
    if (m_delivery_date_isSet) {
        obj.insert(QString("delivery_date"), ::OpenAPI::toJsonValue(m_delivery_date));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_project_id_isSet) {
        obj.insert(QString("project_id"), ::OpenAPI::toJsonValue(m_project_id));
    }
    if (m_reference_isSet) {
        obj.insert(QString("reference"), ::OpenAPI::toJsonValue(m_reference));
    }
    if (m_short_text_isSet) {
        obj.insert(QString("short_text"), ::OpenAPI::toJsonValue(m_short_text));
    }
    if (m_supplier_invoice_number_isSet) {
        obj.insert(QString("supplier_invoice_number"), ::OpenAPI::toJsonValue(m_supplier_invoice_number));
    }
    return obj;
}

QString OAI_expenses_post_request::getContactId() const {
    return m_contact_id;
}
void OAI_expenses_post_request::setContactId(const QString &contact_id) {
    m_contact_id = contact_id;
    m_contact_id_isSet = true;
}

bool OAI_expenses_post_request::is_contact_id_Set() const{
    return m_contact_id_isSet;
}

bool OAI_expenses_post_request::is_contact_id_Valid() const{
    return m_contact_id_isValid;
}

QString OAI_expenses_post_request::getCurrencyId() const {
    return m_currency_id;
}
void OAI_expenses_post_request::setCurrencyId(const QString &currency_id) {
    m_currency_id = currency_id;
    m_currency_id_isSet = true;
}

bool OAI_expenses_post_request::is_currency_id_Set() const{
    return m_currency_id_isSet;
}

bool OAI_expenses_post_request::is_currency_id_Valid() const{
    return m_currency_id_isValid;
}

QDate OAI_expenses_post_request::getDeliveryDate() const {
    return m_delivery_date;
}
void OAI_expenses_post_request::setDeliveryDate(const QDate &delivery_date) {
    m_delivery_date = delivery_date;
    m_delivery_date_isSet = true;
}

bool OAI_expenses_post_request::is_delivery_date_Set() const{
    return m_delivery_date_isSet;
}

bool OAI_expenses_post_request::is_delivery_date_Valid() const{
    return m_delivery_date_isValid;
}

QString OAI_expenses_post_request::getDescription() const {
    return m_description;
}
void OAI_expenses_post_request::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAI_expenses_post_request::is_description_Set() const{
    return m_description_isSet;
}

bool OAI_expenses_post_request::is_description_Valid() const{
    return m_description_isValid;
}

QString OAI_expenses_post_request::getProjectId() const {
    return m_project_id;
}
void OAI_expenses_post_request::setProjectId(const QString &project_id) {
    m_project_id = project_id;
    m_project_id_isSet = true;
}

bool OAI_expenses_post_request::is_project_id_Set() const{
    return m_project_id_isSet;
}

bool OAI_expenses_post_request::is_project_id_Valid() const{
    return m_project_id_isValid;
}

QString OAI_expenses_post_request::getReference() const {
    return m_reference;
}
void OAI_expenses_post_request::setReference(const QString &reference) {
    m_reference = reference;
    m_reference_isSet = true;
}

bool OAI_expenses_post_request::is_reference_Set() const{
    return m_reference_isSet;
}

bool OAI_expenses_post_request::is_reference_Valid() const{
    return m_reference_isValid;
}

QString OAI_expenses_post_request::getShortText() const {
    return m_short_text;
}
void OAI_expenses_post_request::setShortText(const QString &short_text) {
    m_short_text = short_text;
    m_short_text_isSet = true;
}

bool OAI_expenses_post_request::is_short_text_Set() const{
    return m_short_text_isSet;
}

bool OAI_expenses_post_request::is_short_text_Valid() const{
    return m_short_text_isValid;
}

QString OAI_expenses_post_request::getSupplierInvoiceNumber() const {
    return m_supplier_invoice_number;
}
void OAI_expenses_post_request::setSupplierInvoiceNumber(const QString &supplier_invoice_number) {
    m_supplier_invoice_number = supplier_invoice_number;
    m_supplier_invoice_number_isSet = true;
}

bool OAI_expenses_post_request::is_supplier_invoice_number_Set() const{
    return m_supplier_invoice_number_isSet;
}

bool OAI_expenses_post_request::is_supplier_invoice_number_Valid() const{
    return m_supplier_invoice_number_isValid;
}

bool OAI_expenses_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contact_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_id_isSet) {
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

        if (m_project_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_supplier_invoice_number_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_expenses_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
