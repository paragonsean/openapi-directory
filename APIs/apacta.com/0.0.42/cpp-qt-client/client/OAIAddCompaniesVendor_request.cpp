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

#include "OAIAddCompaniesVendor_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddCompaniesVendor_request::OAIAddCompaniesVendor_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddCompaniesVendor_request::OAIAddCompaniesVendor_request() {
    this->initializeModel();
}

OAIAddCompaniesVendor_request::~OAIAddCompaniesVendor_request() {}

void OAIAddCompaniesVendor_request::initializeModel() {

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_delivery_price_isSet = false;
    m_delivery_price_isValid = false;

    m_free_delivery_price_isSet = false;
    m_free_delivery_price_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_receive_automatic_price_files_isSet = false;
    m_receive_automatic_price_files_isValid = false;

    m_receive_invoice_mails_isSet = false;
    m_receive_invoice_mails_isValid = false;

    m_reviewed_isSet = false;
    m_reviewed_isValid = false;

    m_use_price_files_isSet = false;
    m_use_price_files_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;

    m_vendor_account_reference_isSet = false;
    m_vendor_account_reference_isValid = false;

    m_vendor_department_id_isSet = false;
    m_vendor_department_id_isValid = false;

    m_vendor_email_isSet = false;
    m_vendor_email_isValid = false;

    m_vendor_id_isSet = false;
    m_vendor_id_isValid = false;

    m_vendor_name_isSet = false;
    m_vendor_name_isValid = false;
}

void OAIAddCompaniesVendor_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddCompaniesVendor_request::fromJsonObject(QJsonObject json) {

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_delivery_price_isValid = ::OpenAPI::fromJsonValue(m_delivery_price, json[QString("delivery_price")]);
    m_delivery_price_isSet = !json[QString("delivery_price")].isNull() && m_delivery_price_isValid;

    m_free_delivery_price_isValid = ::OpenAPI::fromJsonValue(m_free_delivery_price, json[QString("free_delivery_price")]);
    m_free_delivery_price_isSet = !json[QString("free_delivery_price")].isNull() && m_free_delivery_price_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("is_active")]);
    m_is_active_isSet = !json[QString("is_active")].isNull() && m_is_active_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_receive_automatic_price_files_isValid = ::OpenAPI::fromJsonValue(m_receive_automatic_price_files, json[QString("receive_automatic_price_files")]);
    m_receive_automatic_price_files_isSet = !json[QString("receive_automatic_price_files")].isNull() && m_receive_automatic_price_files_isValid;

    m_receive_invoice_mails_isValid = ::OpenAPI::fromJsonValue(m_receive_invoice_mails, json[QString("receive_invoice_mails")]);
    m_receive_invoice_mails_isSet = !json[QString("receive_invoice_mails")].isNull() && m_receive_invoice_mails_isValid;

    m_reviewed_isValid = ::OpenAPI::fromJsonValue(m_reviewed, json[QString("reviewed")]);
    m_reviewed_isSet = !json[QString("reviewed")].isNull() && m_reviewed_isValid;

    m_use_price_files_isValid = ::OpenAPI::fromJsonValue(m_use_price_files, json[QString("use_price_files")]);
    m_use_price_files_isSet = !json[QString("use_price_files")].isNull() && m_use_price_files_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;

    m_vendor_account_reference_isValid = ::OpenAPI::fromJsonValue(m_vendor_account_reference, json[QString("vendor_account_reference")]);
    m_vendor_account_reference_isSet = !json[QString("vendor_account_reference")].isNull() && m_vendor_account_reference_isValid;

    m_vendor_department_id_isValid = ::OpenAPI::fromJsonValue(m_vendor_department_id, json[QString("vendor_department_id")]);
    m_vendor_department_id_isSet = !json[QString("vendor_department_id")].isNull() && m_vendor_department_id_isValid;

    m_vendor_email_isValid = ::OpenAPI::fromJsonValue(m_vendor_email, json[QString("vendor_email")]);
    m_vendor_email_isSet = !json[QString("vendor_email")].isNull() && m_vendor_email_isValid;

    m_vendor_id_isValid = ::OpenAPI::fromJsonValue(m_vendor_id, json[QString("vendor_id")]);
    m_vendor_id_isSet = !json[QString("vendor_id")].isNull() && m_vendor_id_isValid;

    m_vendor_name_isValid = ::OpenAPI::fromJsonValue(m_vendor_name, json[QString("vendor_name")]);
    m_vendor_name_isSet = !json[QString("vendor_name")].isNull() && m_vendor_name_isValid;
}

QString OAIAddCompaniesVendor_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddCompaniesVendor_request::asJsonObject() const {
    QJsonObject obj;
    if (m_company_id_isSet) {
        obj.insert(QString("company_id"), ::OpenAPI::toJsonValue(m_company_id));
    }
    if (m_delivery_price_isSet) {
        obj.insert(QString("delivery_price"), ::OpenAPI::toJsonValue(m_delivery_price));
    }
    if (m_free_delivery_price_isSet) {
        obj.insert(QString("free_delivery_price"), ::OpenAPI::toJsonValue(m_free_delivery_price));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("is_active"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_receive_automatic_price_files_isSet) {
        obj.insert(QString("receive_automatic_price_files"), ::OpenAPI::toJsonValue(m_receive_automatic_price_files));
    }
    if (m_receive_invoice_mails_isSet) {
        obj.insert(QString("receive_invoice_mails"), ::OpenAPI::toJsonValue(m_receive_invoice_mails));
    }
    if (m_reviewed_isSet) {
        obj.insert(QString("reviewed"), ::OpenAPI::toJsonValue(m_reviewed));
    }
    if (m_use_price_files_isSet) {
        obj.insert(QString("use_price_files"), ::OpenAPI::toJsonValue(m_use_price_files));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    if (m_vendor_account_reference_isSet) {
        obj.insert(QString("vendor_account_reference"), ::OpenAPI::toJsonValue(m_vendor_account_reference));
    }
    if (m_vendor_department_id_isSet) {
        obj.insert(QString("vendor_department_id"), ::OpenAPI::toJsonValue(m_vendor_department_id));
    }
    if (m_vendor_email_isSet) {
        obj.insert(QString("vendor_email"), ::OpenAPI::toJsonValue(m_vendor_email));
    }
    if (m_vendor_id_isSet) {
        obj.insert(QString("vendor_id"), ::OpenAPI::toJsonValue(m_vendor_id));
    }
    if (m_vendor_name_isSet) {
        obj.insert(QString("vendor_name"), ::OpenAPI::toJsonValue(m_vendor_name));
    }
    return obj;
}

QString OAIAddCompaniesVendor_request::getCompanyId() const {
    return m_company_id;
}
void OAIAddCompaniesVendor_request::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIAddCompaniesVendor_request::is_company_id_Valid() const{
    return m_company_id_isValid;
}

float OAIAddCompaniesVendor_request::getDeliveryPrice() const {
    return m_delivery_price;
}
void OAIAddCompaniesVendor_request::setDeliveryPrice(const float &delivery_price) {
    m_delivery_price = delivery_price;
    m_delivery_price_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_delivery_price_Set() const{
    return m_delivery_price_isSet;
}

bool OAIAddCompaniesVendor_request::is_delivery_price_Valid() const{
    return m_delivery_price_isValid;
}

float OAIAddCompaniesVendor_request::getFreeDeliveryPrice() const {
    return m_free_delivery_price;
}
void OAIAddCompaniesVendor_request::setFreeDeliveryPrice(const float &free_delivery_price) {
    m_free_delivery_price = free_delivery_price;
    m_free_delivery_price_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_free_delivery_price_Set() const{
    return m_free_delivery_price_isSet;
}

bool OAIAddCompaniesVendor_request::is_free_delivery_price_Valid() const{
    return m_free_delivery_price_isValid;
}

bool OAIAddCompaniesVendor_request::isIsActive() const {
    return m_is_active;
}
void OAIAddCompaniesVendor_request::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAIAddCompaniesVendor_request::is_is_active_Valid() const{
    return m_is_active_isValid;
}

QString OAIAddCompaniesVendor_request::getPassword() const {
    return m_password;
}
void OAIAddCompaniesVendor_request::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_password_Set() const{
    return m_password_isSet;
}

bool OAIAddCompaniesVendor_request::is_password_Valid() const{
    return m_password_isValid;
}

bool OAIAddCompaniesVendor_request::isReceiveAutomaticPriceFiles() const {
    return m_receive_automatic_price_files;
}
void OAIAddCompaniesVendor_request::setReceiveAutomaticPriceFiles(const bool &receive_automatic_price_files) {
    m_receive_automatic_price_files = receive_automatic_price_files;
    m_receive_automatic_price_files_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_receive_automatic_price_files_Set() const{
    return m_receive_automatic_price_files_isSet;
}

bool OAIAddCompaniesVendor_request::is_receive_automatic_price_files_Valid() const{
    return m_receive_automatic_price_files_isValid;
}

bool OAIAddCompaniesVendor_request::isReceiveInvoiceMails() const {
    return m_receive_invoice_mails;
}
void OAIAddCompaniesVendor_request::setReceiveInvoiceMails(const bool &receive_invoice_mails) {
    m_receive_invoice_mails = receive_invoice_mails;
    m_receive_invoice_mails_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_receive_invoice_mails_Set() const{
    return m_receive_invoice_mails_isSet;
}

bool OAIAddCompaniesVendor_request::is_receive_invoice_mails_Valid() const{
    return m_receive_invoice_mails_isValid;
}

bool OAIAddCompaniesVendor_request::isReviewed() const {
    return m_reviewed;
}
void OAIAddCompaniesVendor_request::setReviewed(const bool &reviewed) {
    m_reviewed = reviewed;
    m_reviewed_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_reviewed_Set() const{
    return m_reviewed_isSet;
}

bool OAIAddCompaniesVendor_request::is_reviewed_Valid() const{
    return m_reviewed_isValid;
}

bool OAIAddCompaniesVendor_request::isUsePriceFiles() const {
    return m_use_price_files;
}
void OAIAddCompaniesVendor_request::setUsePriceFiles(const bool &use_price_files) {
    m_use_price_files = use_price_files;
    m_use_price_files_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_use_price_files_Set() const{
    return m_use_price_files_isSet;
}

bool OAIAddCompaniesVendor_request::is_use_price_files_Valid() const{
    return m_use_price_files_isValid;
}

QString OAIAddCompaniesVendor_request::getUsername() const {
    return m_username;
}
void OAIAddCompaniesVendor_request::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_username_Set() const{
    return m_username_isSet;
}

bool OAIAddCompaniesVendor_request::is_username_Valid() const{
    return m_username_isValid;
}

QString OAIAddCompaniesVendor_request::getVendorAccountReference() const {
    return m_vendor_account_reference;
}
void OAIAddCompaniesVendor_request::setVendorAccountReference(const QString &vendor_account_reference) {
    m_vendor_account_reference = vendor_account_reference;
    m_vendor_account_reference_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_vendor_account_reference_Set() const{
    return m_vendor_account_reference_isSet;
}

bool OAIAddCompaniesVendor_request::is_vendor_account_reference_Valid() const{
    return m_vendor_account_reference_isValid;
}

QString OAIAddCompaniesVendor_request::getVendorDepartmentId() const {
    return m_vendor_department_id;
}
void OAIAddCompaniesVendor_request::setVendorDepartmentId(const QString &vendor_department_id) {
    m_vendor_department_id = vendor_department_id;
    m_vendor_department_id_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_vendor_department_id_Set() const{
    return m_vendor_department_id_isSet;
}

bool OAIAddCompaniesVendor_request::is_vendor_department_id_Valid() const{
    return m_vendor_department_id_isValid;
}

QString OAIAddCompaniesVendor_request::getVendorEmail() const {
    return m_vendor_email;
}
void OAIAddCompaniesVendor_request::setVendorEmail(const QString &vendor_email) {
    m_vendor_email = vendor_email;
    m_vendor_email_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_vendor_email_Set() const{
    return m_vendor_email_isSet;
}

bool OAIAddCompaniesVendor_request::is_vendor_email_Valid() const{
    return m_vendor_email_isValid;
}

QString OAIAddCompaniesVendor_request::getVendorId() const {
    return m_vendor_id;
}
void OAIAddCompaniesVendor_request::setVendorId(const QString &vendor_id) {
    m_vendor_id = vendor_id;
    m_vendor_id_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_vendor_id_Set() const{
    return m_vendor_id_isSet;
}

bool OAIAddCompaniesVendor_request::is_vendor_id_Valid() const{
    return m_vendor_id_isValid;
}

QString OAIAddCompaniesVendor_request::getVendorName() const {
    return m_vendor_name;
}
void OAIAddCompaniesVendor_request::setVendorName(const QString &vendor_name) {
    m_vendor_name = vendor_name;
    m_vendor_name_isSet = true;
}

bool OAIAddCompaniesVendor_request::is_vendor_name_Set() const{
    return m_vendor_name_isSet;
}

bool OAIAddCompaniesVendor_request::is_vendor_name_Valid() const{
    return m_vendor_name_isValid;
}

bool OAIAddCompaniesVendor_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_company_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_delivery_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_free_delivery_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_receive_automatic_price_files_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_receive_invoice_mails_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reviewed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_price_files_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_account_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_department_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddCompaniesVendor_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
