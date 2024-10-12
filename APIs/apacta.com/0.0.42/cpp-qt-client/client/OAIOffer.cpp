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

#include "OAIOffer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOffer::OAIOffer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOffer::OAIOffer() {
    this->initializeModel();
}

OAIOffer::~OAIOffer() {}

void OAIOffer::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_all_lines_one_line_isSet = false;
    m_all_lines_one_line_isValid = false;

    m_all_products_one_line_isSet = false;
    m_all_products_one_line_isValid = false;

    m_all_working_hours_one_line_isSet = false;
    m_all_working_hours_one_line_isValid = false;

    m_city_id_isSet = false;
    m_city_id_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_contact_id_isSet = false;
    m_contact_id_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_discount_percent_isSet = false;
    m_discount_percent_isValid = false;

    m_erp_payment_term_id_isSet = false;
    m_erp_payment_term_id_isValid = false;

    m_expiraton_date_isSet = false;
    m_expiraton_date_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_issue_date_isSet = false;
    m_issue_date_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_modified_by_id_isSet = false;
    m_modified_by_id_isValid = false;

    m_offer_number_isSet = false;
    m_offer_number_isValid = false;

    m_offer_status_id_isSet = false;
    m_offer_status_id_isValid = false;

    m_payment_term_id_isSet = false;
    m_payment_term_id_isValid = false;

    m_rejection_reason_isSet = false;
    m_rejection_reason_isValid = false;

    m_sender_id_isSet = false;
    m_sender_id_isValid = false;

    m_show_employee_name_isSet = false;
    m_show_employee_name_isValid = false;

    m_show_offer_lines_isSet = false;
    m_show_offer_lines_isValid = false;

    m_show_payment_term_isSet = false;
    m_show_payment_term_isValid = false;

    m_show_prices_isSet = false;
    m_show_prices_isValid = false;

    m_show_product_images_isSet = false;
    m_show_product_images_isValid = false;

    m_show_products_product_bundle_isSet = false;
    m_show_products_product_bundle_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_vat_percent_isSet = false;
    m_vat_percent_isValid = false;
}

void OAIOffer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOffer::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_all_lines_one_line_isValid = ::OpenAPI::fromJsonValue(m_all_lines_one_line, json[QString("all_lines_one_line")]);
    m_all_lines_one_line_isSet = !json[QString("all_lines_one_line")].isNull() && m_all_lines_one_line_isValid;

    m_all_products_one_line_isValid = ::OpenAPI::fromJsonValue(m_all_products_one_line, json[QString("all_products_one_line")]);
    m_all_products_one_line_isSet = !json[QString("all_products_one_line")].isNull() && m_all_products_one_line_isValid;

    m_all_working_hours_one_line_isValid = ::OpenAPI::fromJsonValue(m_all_working_hours_one_line, json[QString("all_working_hours_one_line")]);
    m_all_working_hours_one_line_isSet = !json[QString("all_working_hours_one_line")].isNull() && m_all_working_hours_one_line_isValid;

    m_city_id_isValid = ::OpenAPI::fromJsonValue(m_city_id, json[QString("city_id")]);
    m_city_id_isSet = !json[QString("city_id")].isNull() && m_city_id_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_contact_id_isValid = ::OpenAPI::fromJsonValue(m_contact_id, json[QString("contact_id")]);
    m_contact_id_isSet = !json[QString("contact_id")].isNull() && m_contact_id_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_discount_percent_isValid = ::OpenAPI::fromJsonValue(m_discount_percent, json[QString("discount_percent")]);
    m_discount_percent_isSet = !json[QString("discount_percent")].isNull() && m_discount_percent_isValid;

    m_erp_payment_term_id_isValid = ::OpenAPI::fromJsonValue(m_erp_payment_term_id, json[QString("erp_payment_term_id")]);
    m_erp_payment_term_id_isSet = !json[QString("erp_payment_term_id")].isNull() && m_erp_payment_term_id_isValid;

    m_expiraton_date_isValid = ::OpenAPI::fromJsonValue(m_expiraton_date, json[QString("expiraton_date")]);
    m_expiraton_date_isSet = !json[QString("expiraton_date")].isNull() && m_expiraton_date_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_issue_date_isValid = ::OpenAPI::fromJsonValue(m_issue_date, json[QString("issue_date")]);
    m_issue_date_isSet = !json[QString("issue_date")].isNull() && m_issue_date_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_modified_by_id_isValid = ::OpenAPI::fromJsonValue(m_modified_by_id, json[QString("modified_by_id")]);
    m_modified_by_id_isSet = !json[QString("modified_by_id")].isNull() && m_modified_by_id_isValid;

    m_offer_number_isValid = ::OpenAPI::fromJsonValue(m_offer_number, json[QString("offer_number")]);
    m_offer_number_isSet = !json[QString("offer_number")].isNull() && m_offer_number_isValid;

    m_offer_status_id_isValid = ::OpenAPI::fromJsonValue(m_offer_status_id, json[QString("offer_status_id")]);
    m_offer_status_id_isSet = !json[QString("offer_status_id")].isNull() && m_offer_status_id_isValid;

    m_payment_term_id_isValid = ::OpenAPI::fromJsonValue(m_payment_term_id, json[QString("payment_term_id")]);
    m_payment_term_id_isSet = !json[QString("payment_term_id")].isNull() && m_payment_term_id_isValid;

    m_rejection_reason_isValid = ::OpenAPI::fromJsonValue(m_rejection_reason, json[QString("rejection_reason")]);
    m_rejection_reason_isSet = !json[QString("rejection_reason")].isNull() && m_rejection_reason_isValid;

    m_sender_id_isValid = ::OpenAPI::fromJsonValue(m_sender_id, json[QString("sender_id")]);
    m_sender_id_isSet = !json[QString("sender_id")].isNull() && m_sender_id_isValid;

    m_show_employee_name_isValid = ::OpenAPI::fromJsonValue(m_show_employee_name, json[QString("show_employee_name")]);
    m_show_employee_name_isSet = !json[QString("show_employee_name")].isNull() && m_show_employee_name_isValid;

    m_show_offer_lines_isValid = ::OpenAPI::fromJsonValue(m_show_offer_lines, json[QString("show_offer_lines")]);
    m_show_offer_lines_isSet = !json[QString("show_offer_lines")].isNull() && m_show_offer_lines_isValid;

    m_show_payment_term_isValid = ::OpenAPI::fromJsonValue(m_show_payment_term, json[QString("show_payment_term")]);
    m_show_payment_term_isSet = !json[QString("show_payment_term")].isNull() && m_show_payment_term_isValid;

    m_show_prices_isValid = ::OpenAPI::fromJsonValue(m_show_prices, json[QString("show_prices")]);
    m_show_prices_isSet = !json[QString("show_prices")].isNull() && m_show_prices_isValid;

    m_show_product_images_isValid = ::OpenAPI::fromJsonValue(m_show_product_images, json[QString("show_product_images")]);
    m_show_product_images_isSet = !json[QString("show_product_images")].isNull() && m_show_product_images_isValid;

    m_show_products_product_bundle_isValid = ::OpenAPI::fromJsonValue(m_show_products_product_bundle, json[QString("show_products_product_bundle")]);
    m_show_products_product_bundle_isSet = !json[QString("show_products_product_bundle")].isNull() && m_show_products_product_bundle_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_vat_percent_isValid = ::OpenAPI::fromJsonValue(m_vat_percent, json[QString("vat_percent")]);
    m_vat_percent_isSet = !json[QString("vat_percent")].isNull() && m_vat_percent_isValid;
}

QString OAIOffer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOffer::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_all_lines_one_line_isSet) {
        obj.insert(QString("all_lines_one_line"), ::OpenAPI::toJsonValue(m_all_lines_one_line));
    }
    if (m_all_products_one_line_isSet) {
        obj.insert(QString("all_products_one_line"), ::OpenAPI::toJsonValue(m_all_products_one_line));
    }
    if (m_all_working_hours_one_line_isSet) {
        obj.insert(QString("all_working_hours_one_line"), ::OpenAPI::toJsonValue(m_all_working_hours_one_line));
    }
    if (m_city_id_isSet) {
        obj.insert(QString("city_id"), ::OpenAPI::toJsonValue(m_city_id));
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
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_discount_percent_isSet) {
        obj.insert(QString("discount_percent"), ::OpenAPI::toJsonValue(m_discount_percent));
    }
    if (m_erp_payment_term_id_isSet) {
        obj.insert(QString("erp_payment_term_id"), ::OpenAPI::toJsonValue(m_erp_payment_term_id));
    }
    if (m_expiraton_date_isSet) {
        obj.insert(QString("expiraton_date"), ::OpenAPI::toJsonValue(m_expiraton_date));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_issue_date_isSet) {
        obj.insert(QString("issue_date"), ::OpenAPI::toJsonValue(m_issue_date));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_modified_by_id_isSet) {
        obj.insert(QString("modified_by_id"), ::OpenAPI::toJsonValue(m_modified_by_id));
    }
    if (m_offer_number_isSet) {
        obj.insert(QString("offer_number"), ::OpenAPI::toJsonValue(m_offer_number));
    }
    if (m_offer_status_id_isSet) {
        obj.insert(QString("offer_status_id"), ::OpenAPI::toJsonValue(m_offer_status_id));
    }
    if (m_payment_term_id_isSet) {
        obj.insert(QString("payment_term_id"), ::OpenAPI::toJsonValue(m_payment_term_id));
    }
    if (m_rejection_reason_isSet) {
        obj.insert(QString("rejection_reason"), ::OpenAPI::toJsonValue(m_rejection_reason));
    }
    if (m_sender_id_isSet) {
        obj.insert(QString("sender_id"), ::OpenAPI::toJsonValue(m_sender_id));
    }
    if (m_show_employee_name_isSet) {
        obj.insert(QString("show_employee_name"), ::OpenAPI::toJsonValue(m_show_employee_name));
    }
    if (m_show_offer_lines_isSet) {
        obj.insert(QString("show_offer_lines"), ::OpenAPI::toJsonValue(m_show_offer_lines));
    }
    if (m_show_payment_term_isSet) {
        obj.insert(QString("show_payment_term"), ::OpenAPI::toJsonValue(m_show_payment_term));
    }
    if (m_show_prices_isSet) {
        obj.insert(QString("show_prices"), ::OpenAPI::toJsonValue(m_show_prices));
    }
    if (m_show_product_images_isSet) {
        obj.insert(QString("show_product_images"), ::OpenAPI::toJsonValue(m_show_product_images));
    }
    if (m_show_products_product_bundle_isSet) {
        obj.insert(QString("show_products_product_bundle"), ::OpenAPI::toJsonValue(m_show_products_product_bundle));
    }
    if (m_slug_isSet) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_vat_percent_isSet) {
        obj.insert(QString("vat_percent"), ::OpenAPI::toJsonValue(m_vat_percent));
    }
    return obj;
}

QString OAIOffer::getAddress() const {
    return m_address;
}
void OAIOffer::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIOffer::is_address_Set() const{
    return m_address_isSet;
}

bool OAIOffer::is_address_Valid() const{
    return m_address_isValid;
}

bool OAIOffer::isAllLinesOneLine() const {
    return m_all_lines_one_line;
}
void OAIOffer::setAllLinesOneLine(const bool &all_lines_one_line) {
    m_all_lines_one_line = all_lines_one_line;
    m_all_lines_one_line_isSet = true;
}

bool OAIOffer::is_all_lines_one_line_Set() const{
    return m_all_lines_one_line_isSet;
}

bool OAIOffer::is_all_lines_one_line_Valid() const{
    return m_all_lines_one_line_isValid;
}

bool OAIOffer::isAllProductsOneLine() const {
    return m_all_products_one_line;
}
void OAIOffer::setAllProductsOneLine(const bool &all_products_one_line) {
    m_all_products_one_line = all_products_one_line;
    m_all_products_one_line_isSet = true;
}

bool OAIOffer::is_all_products_one_line_Set() const{
    return m_all_products_one_line_isSet;
}

bool OAIOffer::is_all_products_one_line_Valid() const{
    return m_all_products_one_line_isValid;
}

bool OAIOffer::isAllWorkingHoursOneLine() const {
    return m_all_working_hours_one_line;
}
void OAIOffer::setAllWorkingHoursOneLine(const bool &all_working_hours_one_line) {
    m_all_working_hours_one_line = all_working_hours_one_line;
    m_all_working_hours_one_line_isSet = true;
}

bool OAIOffer::is_all_working_hours_one_line_Set() const{
    return m_all_working_hours_one_line_isSet;
}

bool OAIOffer::is_all_working_hours_one_line_Valid() const{
    return m_all_working_hours_one_line_isValid;
}

QString OAIOffer::getCityId() const {
    return m_city_id;
}
void OAIOffer::setCityId(const QString &city_id) {
    m_city_id = city_id;
    m_city_id_isSet = true;
}

bool OAIOffer::is_city_id_Set() const{
    return m_city_id_isSet;
}

bool OAIOffer::is_city_id_Valid() const{
    return m_city_id_isValid;
}

QString OAIOffer::getCompanyId() const {
    return m_company_id;
}
void OAIOffer::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIOffer::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIOffer::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIOffer::getContactId() const {
    return m_contact_id;
}
void OAIOffer::setContactId(const QString &contact_id) {
    m_contact_id = contact_id;
    m_contact_id_isSet = true;
}

bool OAIOffer::is_contact_id_Set() const{
    return m_contact_id_isSet;
}

bool OAIOffer::is_contact_id_Valid() const{
    return m_contact_id_isValid;
}

QString OAIOffer::getCreated() const {
    return m_created;
}
void OAIOffer::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIOffer::is_created_Set() const{
    return m_created_isSet;
}

bool OAIOffer::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIOffer::getCreatedById() const {
    return m_created_by_id;
}
void OAIOffer::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIOffer::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIOffer::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIOffer::getDeleted() const {
    return m_deleted;
}
void OAIOffer::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIOffer::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIOffer::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIOffer::getDescription() const {
    return m_description;
}
void OAIOffer::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIOffer::is_description_Set() const{
    return m_description_isSet;
}

bool OAIOffer::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIOffer::getDiscountPercent() const {
    return m_discount_percent;
}
void OAIOffer::setDiscountPercent(const qint32 &discount_percent) {
    m_discount_percent = discount_percent;
    m_discount_percent_isSet = true;
}

bool OAIOffer::is_discount_percent_Set() const{
    return m_discount_percent_isSet;
}

bool OAIOffer::is_discount_percent_Valid() const{
    return m_discount_percent_isValid;
}

QString OAIOffer::getErpPaymentTermId() const {
    return m_erp_payment_term_id;
}
void OAIOffer::setErpPaymentTermId(const QString &erp_payment_term_id) {
    m_erp_payment_term_id = erp_payment_term_id;
    m_erp_payment_term_id_isSet = true;
}

bool OAIOffer::is_erp_payment_term_id_Set() const{
    return m_erp_payment_term_id_isSet;
}

bool OAIOffer::is_erp_payment_term_id_Valid() const{
    return m_erp_payment_term_id_isValid;
}

QString OAIOffer::getExpiratonDate() const {
    return m_expiraton_date;
}
void OAIOffer::setExpiratonDate(const QString &expiraton_date) {
    m_expiraton_date = expiraton_date;
    m_expiraton_date_isSet = true;
}

bool OAIOffer::is_expiraton_date_Set() const{
    return m_expiraton_date_isSet;
}

bool OAIOffer::is_expiraton_date_Valid() const{
    return m_expiraton_date_isValid;
}

QString OAIOffer::getId() const {
    return m_id;
}
void OAIOffer::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOffer::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOffer::is_id_Valid() const{
    return m_id_isValid;
}

QDate OAIOffer::getIssueDate() const {
    return m_issue_date;
}
void OAIOffer::setIssueDate(const QDate &issue_date) {
    m_issue_date = issue_date;
    m_issue_date_isSet = true;
}

bool OAIOffer::is_issue_date_Set() const{
    return m_issue_date_isSet;
}

bool OAIOffer::is_issue_date_Valid() const{
    return m_issue_date_isValid;
}

QString OAIOffer::getModified() const {
    return m_modified;
}
void OAIOffer::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIOffer::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIOffer::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIOffer::getModifiedById() const {
    return m_modified_by_id;
}
void OAIOffer::setModifiedById(const QString &modified_by_id) {
    m_modified_by_id = modified_by_id;
    m_modified_by_id_isSet = true;
}

bool OAIOffer::is_modified_by_id_Set() const{
    return m_modified_by_id_isSet;
}

bool OAIOffer::is_modified_by_id_Valid() const{
    return m_modified_by_id_isValid;
}

qint32 OAIOffer::getOfferNumber() const {
    return m_offer_number;
}
void OAIOffer::setOfferNumber(const qint32 &offer_number) {
    m_offer_number = offer_number;
    m_offer_number_isSet = true;
}

bool OAIOffer::is_offer_number_Set() const{
    return m_offer_number_isSet;
}

bool OAIOffer::is_offer_number_Valid() const{
    return m_offer_number_isValid;
}

QString OAIOffer::getOfferStatusId() const {
    return m_offer_status_id;
}
void OAIOffer::setOfferStatusId(const QString &offer_status_id) {
    m_offer_status_id = offer_status_id;
    m_offer_status_id_isSet = true;
}

bool OAIOffer::is_offer_status_id_Set() const{
    return m_offer_status_id_isSet;
}

bool OAIOffer::is_offer_status_id_Valid() const{
    return m_offer_status_id_isValid;
}

QString OAIOffer::getPaymentTermId() const {
    return m_payment_term_id;
}
void OAIOffer::setPaymentTermId(const QString &payment_term_id) {
    m_payment_term_id = payment_term_id;
    m_payment_term_id_isSet = true;
}

bool OAIOffer::is_payment_term_id_Set() const{
    return m_payment_term_id_isSet;
}

bool OAIOffer::is_payment_term_id_Valid() const{
    return m_payment_term_id_isValid;
}

QString OAIOffer::getRejectionReason() const {
    return m_rejection_reason;
}
void OAIOffer::setRejectionReason(const QString &rejection_reason) {
    m_rejection_reason = rejection_reason;
    m_rejection_reason_isSet = true;
}

bool OAIOffer::is_rejection_reason_Set() const{
    return m_rejection_reason_isSet;
}

bool OAIOffer::is_rejection_reason_Valid() const{
    return m_rejection_reason_isValid;
}

QString OAIOffer::getSenderId() const {
    return m_sender_id;
}
void OAIOffer::setSenderId(const QString &sender_id) {
    m_sender_id = sender_id;
    m_sender_id_isSet = true;
}

bool OAIOffer::is_sender_id_Set() const{
    return m_sender_id_isSet;
}

bool OAIOffer::is_sender_id_Valid() const{
    return m_sender_id_isValid;
}

bool OAIOffer::isShowEmployeeName() const {
    return m_show_employee_name;
}
void OAIOffer::setShowEmployeeName(const bool &show_employee_name) {
    m_show_employee_name = show_employee_name;
    m_show_employee_name_isSet = true;
}

bool OAIOffer::is_show_employee_name_Set() const{
    return m_show_employee_name_isSet;
}

bool OAIOffer::is_show_employee_name_Valid() const{
    return m_show_employee_name_isValid;
}

bool OAIOffer::isShowOfferLines() const {
    return m_show_offer_lines;
}
void OAIOffer::setShowOfferLines(const bool &show_offer_lines) {
    m_show_offer_lines = show_offer_lines;
    m_show_offer_lines_isSet = true;
}

bool OAIOffer::is_show_offer_lines_Set() const{
    return m_show_offer_lines_isSet;
}

bool OAIOffer::is_show_offer_lines_Valid() const{
    return m_show_offer_lines_isValid;
}

bool OAIOffer::isShowPaymentTerm() const {
    return m_show_payment_term;
}
void OAIOffer::setShowPaymentTerm(const bool &show_payment_term) {
    m_show_payment_term = show_payment_term;
    m_show_payment_term_isSet = true;
}

bool OAIOffer::is_show_payment_term_Set() const{
    return m_show_payment_term_isSet;
}

bool OAIOffer::is_show_payment_term_Valid() const{
    return m_show_payment_term_isValid;
}

bool OAIOffer::isShowPrices() const {
    return m_show_prices;
}
void OAIOffer::setShowPrices(const bool &show_prices) {
    m_show_prices = show_prices;
    m_show_prices_isSet = true;
}

bool OAIOffer::is_show_prices_Set() const{
    return m_show_prices_isSet;
}

bool OAIOffer::is_show_prices_Valid() const{
    return m_show_prices_isValid;
}

bool OAIOffer::isShowProductImages() const {
    return m_show_product_images;
}
void OAIOffer::setShowProductImages(const bool &show_product_images) {
    m_show_product_images = show_product_images;
    m_show_product_images_isSet = true;
}

bool OAIOffer::is_show_product_images_Set() const{
    return m_show_product_images_isSet;
}

bool OAIOffer::is_show_product_images_Valid() const{
    return m_show_product_images_isValid;
}

bool OAIOffer::isShowProductsProductBundle() const {
    return m_show_products_product_bundle;
}
void OAIOffer::setShowProductsProductBundle(const bool &show_products_product_bundle) {
    m_show_products_product_bundle = show_products_product_bundle;
    m_show_products_product_bundle_isSet = true;
}

bool OAIOffer::is_show_products_product_bundle_Set() const{
    return m_show_products_product_bundle_isSet;
}

bool OAIOffer::is_show_products_product_bundle_Valid() const{
    return m_show_products_product_bundle_isValid;
}

QString OAIOffer::getSlug() const {
    return m_slug;
}
void OAIOffer::setSlug(const QString &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAIOffer::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAIOffer::is_slug_Valid() const{
    return m_slug_isValid;
}

QString OAIOffer::getStatus() const {
    return m_status;
}
void OAIOffer::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIOffer::is_status_Set() const{
    return m_status_isSet;
}

bool OAIOffer::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIOffer::getTitle() const {
    return m_title;
}
void OAIOffer::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIOffer::is_title_Set() const{
    return m_title_isSet;
}

bool OAIOffer::is_title_Valid() const{
    return m_title_isValid;
}

qint32 OAIOffer::getVatPercent() const {
    return m_vat_percent;
}
void OAIOffer::setVatPercent(const qint32 &vat_percent) {
    m_vat_percent = vat_percent;
    m_vat_percent_isSet = true;
}

bool OAIOffer::is_vat_percent_Set() const{
    return m_vat_percent_isSet;
}

bool OAIOffer::is_vat_percent_Valid() const{
    return m_vat_percent_isValid;
}

bool OAIOffer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_all_lines_one_line_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_all_products_one_line_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_all_working_hours_one_line_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_id_isSet) {
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

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_percent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_erp_payment_term_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiraton_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_issue_date_isSet) {
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

        if (m_offer_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offer_status_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_term_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rejection_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sender_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_employee_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_offer_lines_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_payment_term_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_prices_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_product_images_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_products_product_bundle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
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

bool OAIOffer::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
