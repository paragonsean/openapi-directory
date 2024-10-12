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

#include "OAIInvoice.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInvoice::OAIInvoice(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInvoice::OAIInvoice() {
    this->initializeModel();
}

OAIInvoice::~OAIInvoice() {}

void OAIInvoice::initializeModel() {

    m_all_products_one_line_isSet = false;
    m_all_products_one_line_isValid = false;

    m_all_working_hours_one_line_isSet = false;
    m_all_working_hours_one_line_isValid = false;

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

    m_date_from_isSet = false;
    m_date_from_isValid = false;

    m_date_to_isSet = false;
    m_date_to_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_downloaded_isSet = false;
    m_downloaded_isValid = false;

    m_erp_id_isSet = false;
    m_erp_id_isValid = false;

    m_erp_payment_term_id_isSet = false;
    m_erp_payment_term_id_isValid = false;

    m_eu_customer_isSet = false;
    m_eu_customer_isValid = false;

    m_gross_payment_isSet = false;
    m_gross_payment_isValid = false;

    m_group_by_forms_isSet = false;
    m_group_by_forms_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_include_invoiced_lines_isSet = false;
    m_include_invoiced_lines_isValid = false;

    m_integration_id_isSet = false;
    m_integration_id_isValid = false;

    m_invoice_number_isSet = false;
    m_invoice_number_isValid = false;

    m_is_draft_isSet = false;
    m_is_draft_isValid = false;

    m_is_final_invoice_isSet = false;
    m_is_final_invoice_isValid = false;

    m_is_locked_isSet = false;
    m_is_locked_isValid = false;

    m_is_offer_isSet = false;
    m_is_offer_isValid = false;

    m_issued_date_isSet = false;
    m_issued_date_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_net_payment_isSet = false;
    m_net_payment_isValid = false;

    m_offer_number_isSet = false;
    m_offer_number_isValid = false;

    m_order_line_group_id_isSet = false;
    m_order_line_group_id_isValid = false;

    m_payment_due_date_isSet = false;
    m_payment_due_date_isValid = false;

    m_payment_term_id_isSet = false;
    m_payment_term_id_isValid = false;

    m_project_id_isSet = false;
    m_project_id_isValid = false;

    m_project_overview_attached_isSet = false;
    m_project_overview_attached_isValid = false;

    m_reference_isSet = false;
    m_reference_isValid = false;

    m_show_employee_name_isSet = false;
    m_show_employee_name_isValid = false;

    m_show_price_product_bundle_isSet = false;
    m_show_price_product_bundle_isValid = false;

    m_show_prices_products_and_hours_isSet = false;
    m_show_prices_products_and_hours_isValid = false;

    m_show_product_images_isSet = false;
    m_show_product_images_isValid = false;

    m_show_products_product_bundle_isSet = false;
    m_show_products_product_bundle_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_total_cost_price_isSet = false;
    m_total_cost_price_isValid = false;

    m_total_discount_percent_isSet = false;
    m_total_discount_percent_isValid = false;

    m_vat_percent_isSet = false;
    m_vat_percent_isValid = false;

    m_vendor_id_isSet = false;
    m_vendor_id_isValid = false;
}

void OAIInvoice::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInvoice::fromJsonObject(QJsonObject json) {

    m_all_products_one_line_isValid = ::OpenAPI::fromJsonValue(m_all_products_one_line, json[QString("all_products_one_line")]);
    m_all_products_one_line_isSet = !json[QString("all_products_one_line")].isNull() && m_all_products_one_line_isValid;

    m_all_working_hours_one_line_isValid = ::OpenAPI::fromJsonValue(m_all_working_hours_one_line, json[QString("all_working_hours_one_line")]);
    m_all_working_hours_one_line_isSet = !json[QString("all_working_hours_one_line")].isNull() && m_all_working_hours_one_line_isValid;

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

    m_date_from_isValid = ::OpenAPI::fromJsonValue(m_date_from, json[QString("date_from")]);
    m_date_from_isSet = !json[QString("date_from")].isNull() && m_date_from_isValid;

    m_date_to_isValid = ::OpenAPI::fromJsonValue(m_date_to, json[QString("date_to")]);
    m_date_to_isSet = !json[QString("date_to")].isNull() && m_date_to_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_downloaded_isValid = ::OpenAPI::fromJsonValue(m_downloaded, json[QString("downloaded")]);
    m_downloaded_isSet = !json[QString("downloaded")].isNull() && m_downloaded_isValid;

    m_erp_id_isValid = ::OpenAPI::fromJsonValue(m_erp_id, json[QString("erp_id")]);
    m_erp_id_isSet = !json[QString("erp_id")].isNull() && m_erp_id_isValid;

    m_erp_payment_term_id_isValid = ::OpenAPI::fromJsonValue(m_erp_payment_term_id, json[QString("erp_payment_term_id")]);
    m_erp_payment_term_id_isSet = !json[QString("erp_payment_term_id")].isNull() && m_erp_payment_term_id_isValid;

    m_eu_customer_isValid = ::OpenAPI::fromJsonValue(m_eu_customer, json[QString("eu_customer")]);
    m_eu_customer_isSet = !json[QString("eu_customer")].isNull() && m_eu_customer_isValid;

    m_gross_payment_isValid = ::OpenAPI::fromJsonValue(m_gross_payment, json[QString("gross_payment")]);
    m_gross_payment_isSet = !json[QString("gross_payment")].isNull() && m_gross_payment_isValid;

    m_group_by_forms_isValid = ::OpenAPI::fromJsonValue(m_group_by_forms, json[QString("group_by_forms")]);
    m_group_by_forms_isSet = !json[QString("group_by_forms")].isNull() && m_group_by_forms_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_include_invoiced_lines_isValid = ::OpenAPI::fromJsonValue(m_include_invoiced_lines, json[QString("include_invoiced_lines")]);
    m_include_invoiced_lines_isSet = !json[QString("include_invoiced_lines")].isNull() && m_include_invoiced_lines_isValid;

    m_integration_id_isValid = ::OpenAPI::fromJsonValue(m_integration_id, json[QString("integration_id")]);
    m_integration_id_isSet = !json[QString("integration_id")].isNull() && m_integration_id_isValid;

    m_invoice_number_isValid = ::OpenAPI::fromJsonValue(m_invoice_number, json[QString("invoice_number")]);
    m_invoice_number_isSet = !json[QString("invoice_number")].isNull() && m_invoice_number_isValid;

    m_is_draft_isValid = ::OpenAPI::fromJsonValue(m_is_draft, json[QString("is_draft")]);
    m_is_draft_isSet = !json[QString("is_draft")].isNull() && m_is_draft_isValid;

    m_is_final_invoice_isValid = ::OpenAPI::fromJsonValue(m_is_final_invoice, json[QString("is_final_invoice")]);
    m_is_final_invoice_isSet = !json[QString("is_final_invoice")].isNull() && m_is_final_invoice_isValid;

    m_is_locked_isValid = ::OpenAPI::fromJsonValue(m_is_locked, json[QString("is_locked")]);
    m_is_locked_isSet = !json[QString("is_locked")].isNull() && m_is_locked_isValid;

    m_is_offer_isValid = ::OpenAPI::fromJsonValue(m_is_offer, json[QString("is_offer")]);
    m_is_offer_isSet = !json[QString("is_offer")].isNull() && m_is_offer_isValid;

    m_issued_date_isValid = ::OpenAPI::fromJsonValue(m_issued_date, json[QString("issued_date")]);
    m_issued_date_isSet = !json[QString("issued_date")].isNull() && m_issued_date_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_net_payment_isValid = ::OpenAPI::fromJsonValue(m_net_payment, json[QString("net_payment")]);
    m_net_payment_isSet = !json[QString("net_payment")].isNull() && m_net_payment_isValid;

    m_offer_number_isValid = ::OpenAPI::fromJsonValue(m_offer_number, json[QString("offer_number")]);
    m_offer_number_isSet = !json[QString("offer_number")].isNull() && m_offer_number_isValid;

    m_order_line_group_id_isValid = ::OpenAPI::fromJsonValue(m_order_line_group_id, json[QString("order_line_group_id")]);
    m_order_line_group_id_isSet = !json[QString("order_line_group_id")].isNull() && m_order_line_group_id_isValid;

    m_payment_due_date_isValid = ::OpenAPI::fromJsonValue(m_payment_due_date, json[QString("payment_due_date")]);
    m_payment_due_date_isSet = !json[QString("payment_due_date")].isNull() && m_payment_due_date_isValid;

    m_payment_term_id_isValid = ::OpenAPI::fromJsonValue(m_payment_term_id, json[QString("payment_term_id")]);
    m_payment_term_id_isSet = !json[QString("payment_term_id")].isNull() && m_payment_term_id_isValid;

    m_project_id_isValid = ::OpenAPI::fromJsonValue(m_project_id, json[QString("project_id")]);
    m_project_id_isSet = !json[QString("project_id")].isNull() && m_project_id_isValid;

    m_project_overview_attached_isValid = ::OpenAPI::fromJsonValue(m_project_overview_attached, json[QString("project_overview_attached")]);
    m_project_overview_attached_isSet = !json[QString("project_overview_attached")].isNull() && m_project_overview_attached_isValid;

    m_reference_isValid = ::OpenAPI::fromJsonValue(m_reference, json[QString("reference")]);
    m_reference_isSet = !json[QString("reference")].isNull() && m_reference_isValid;

    m_show_employee_name_isValid = ::OpenAPI::fromJsonValue(m_show_employee_name, json[QString("show_employee_name")]);
    m_show_employee_name_isSet = !json[QString("show_employee_name")].isNull() && m_show_employee_name_isValid;

    m_show_price_product_bundle_isValid = ::OpenAPI::fromJsonValue(m_show_price_product_bundle, json[QString("show_price_product_bundle")]);
    m_show_price_product_bundle_isSet = !json[QString("show_price_product_bundle")].isNull() && m_show_price_product_bundle_isValid;

    m_show_prices_products_and_hours_isValid = ::OpenAPI::fromJsonValue(m_show_prices_products_and_hours, json[QString("show_prices_products_and_hours")]);
    m_show_prices_products_and_hours_isSet = !json[QString("show_prices_products_and_hours")].isNull() && m_show_prices_products_and_hours_isValid;

    m_show_product_images_isValid = ::OpenAPI::fromJsonValue(m_show_product_images, json[QString("show_product_images")]);
    m_show_product_images_isSet = !json[QString("show_product_images")].isNull() && m_show_product_images_isValid;

    m_show_products_product_bundle_isValid = ::OpenAPI::fromJsonValue(m_show_products_product_bundle, json[QString("show_products_product_bundle")]);
    m_show_products_product_bundle_isSet = !json[QString("show_products_product_bundle")].isNull() && m_show_products_product_bundle_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_total_cost_price_isValid = ::OpenAPI::fromJsonValue(m_total_cost_price, json[QString("total_cost_price")]);
    m_total_cost_price_isSet = !json[QString("total_cost_price")].isNull() && m_total_cost_price_isValid;

    m_total_discount_percent_isValid = ::OpenAPI::fromJsonValue(m_total_discount_percent, json[QString("total_discount_percent")]);
    m_total_discount_percent_isSet = !json[QString("total_discount_percent")].isNull() && m_total_discount_percent_isValid;

    m_vat_percent_isValid = ::OpenAPI::fromJsonValue(m_vat_percent, json[QString("vat_percent")]);
    m_vat_percent_isSet = !json[QString("vat_percent")].isNull() && m_vat_percent_isValid;

    m_vendor_id_isValid = ::OpenAPI::fromJsonValue(m_vendor_id, json[QString("vendor_id")]);
    m_vendor_id_isSet = !json[QString("vendor_id")].isNull() && m_vendor_id_isValid;
}

QString OAIInvoice::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInvoice::asJsonObject() const {
    QJsonObject obj;
    if (m_all_products_one_line_isSet) {
        obj.insert(QString("all_products_one_line"), ::OpenAPI::toJsonValue(m_all_products_one_line));
    }
    if (m_all_working_hours_one_line_isSet) {
        obj.insert(QString("all_working_hours_one_line"), ::OpenAPI::toJsonValue(m_all_working_hours_one_line));
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
    if (m_date_from_isSet) {
        obj.insert(QString("date_from"), ::OpenAPI::toJsonValue(m_date_from));
    }
    if (m_date_to_isSet) {
        obj.insert(QString("date_to"), ::OpenAPI::toJsonValue(m_date_to));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_downloaded_isSet) {
        obj.insert(QString("downloaded"), ::OpenAPI::toJsonValue(m_downloaded));
    }
    if (m_erp_id_isSet) {
        obj.insert(QString("erp_id"), ::OpenAPI::toJsonValue(m_erp_id));
    }
    if (m_erp_payment_term_id_isSet) {
        obj.insert(QString("erp_payment_term_id"), ::OpenAPI::toJsonValue(m_erp_payment_term_id));
    }
    if (m_eu_customer_isSet) {
        obj.insert(QString("eu_customer"), ::OpenAPI::toJsonValue(m_eu_customer));
    }
    if (m_gross_payment_isSet) {
        obj.insert(QString("gross_payment"), ::OpenAPI::toJsonValue(m_gross_payment));
    }
    if (m_group_by_forms_isSet) {
        obj.insert(QString("group_by_forms"), ::OpenAPI::toJsonValue(m_group_by_forms));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_include_invoiced_lines_isSet) {
        obj.insert(QString("include_invoiced_lines"), ::OpenAPI::toJsonValue(m_include_invoiced_lines));
    }
    if (m_integration_id_isSet) {
        obj.insert(QString("integration_id"), ::OpenAPI::toJsonValue(m_integration_id));
    }
    if (m_invoice_number_isSet) {
        obj.insert(QString("invoice_number"), ::OpenAPI::toJsonValue(m_invoice_number));
    }
    if (m_is_draft_isSet) {
        obj.insert(QString("is_draft"), ::OpenAPI::toJsonValue(m_is_draft));
    }
    if (m_is_final_invoice_isSet) {
        obj.insert(QString("is_final_invoice"), ::OpenAPI::toJsonValue(m_is_final_invoice));
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
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_net_payment_isSet) {
        obj.insert(QString("net_payment"), ::OpenAPI::toJsonValue(m_net_payment));
    }
    if (m_offer_number_isSet) {
        obj.insert(QString("offer_number"), ::OpenAPI::toJsonValue(m_offer_number));
    }
    if (m_order_line_group_id_isSet) {
        obj.insert(QString("order_line_group_id"), ::OpenAPI::toJsonValue(m_order_line_group_id));
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
    if (m_project_overview_attached_isSet) {
        obj.insert(QString("project_overview_attached"), ::OpenAPI::toJsonValue(m_project_overview_attached));
    }
    if (m_reference_isSet) {
        obj.insert(QString("reference"), ::OpenAPI::toJsonValue(m_reference));
    }
    if (m_show_employee_name_isSet) {
        obj.insert(QString("show_employee_name"), ::OpenAPI::toJsonValue(m_show_employee_name));
    }
    if (m_show_price_product_bundle_isSet) {
        obj.insert(QString("show_price_product_bundle"), ::OpenAPI::toJsonValue(m_show_price_product_bundle));
    }
    if (m_show_prices_products_and_hours_isSet) {
        obj.insert(QString("show_prices_products_and_hours"), ::OpenAPI::toJsonValue(m_show_prices_products_and_hours));
    }
    if (m_show_product_images_isSet) {
        obj.insert(QString("show_product_images"), ::OpenAPI::toJsonValue(m_show_product_images));
    }
    if (m_show_products_product_bundle_isSet) {
        obj.insert(QString("show_products_product_bundle"), ::OpenAPI::toJsonValue(m_show_products_product_bundle));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_total_cost_price_isSet) {
        obj.insert(QString("total_cost_price"), ::OpenAPI::toJsonValue(m_total_cost_price));
    }
    if (m_total_discount_percent_isSet) {
        obj.insert(QString("total_discount_percent"), ::OpenAPI::toJsonValue(m_total_discount_percent));
    }
    if (m_vat_percent_isSet) {
        obj.insert(QString("vat_percent"), ::OpenAPI::toJsonValue(m_vat_percent));
    }
    if (m_vendor_id_isSet) {
        obj.insert(QString("vendor_id"), ::OpenAPI::toJsonValue(m_vendor_id));
    }
    return obj;
}

bool OAIInvoice::isAllProductsOneLine() const {
    return m_all_products_one_line;
}
void OAIInvoice::setAllProductsOneLine(const bool &all_products_one_line) {
    m_all_products_one_line = all_products_one_line;
    m_all_products_one_line_isSet = true;
}

bool OAIInvoice::is_all_products_one_line_Set() const{
    return m_all_products_one_line_isSet;
}

bool OAIInvoice::is_all_products_one_line_Valid() const{
    return m_all_products_one_line_isValid;
}

bool OAIInvoice::isAllWorkingHoursOneLine() const {
    return m_all_working_hours_one_line;
}
void OAIInvoice::setAllWorkingHoursOneLine(const bool &all_working_hours_one_line) {
    m_all_working_hours_one_line = all_working_hours_one_line;
    m_all_working_hours_one_line_isSet = true;
}

bool OAIInvoice::is_all_working_hours_one_line_Set() const{
    return m_all_working_hours_one_line_isSet;
}

bool OAIInvoice::is_all_working_hours_one_line_Valid() const{
    return m_all_working_hours_one_line_isValid;
}

QString OAIInvoice::getCompanyId() const {
    return m_company_id;
}
void OAIInvoice::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIInvoice::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIInvoice::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIInvoice::getContactId() const {
    return m_contact_id;
}
void OAIInvoice::setContactId(const QString &contact_id) {
    m_contact_id = contact_id;
    m_contact_id_isSet = true;
}

bool OAIInvoice::is_contact_id_Set() const{
    return m_contact_id_isSet;
}

bool OAIInvoice::is_contact_id_Valid() const{
    return m_contact_id_isValid;
}

QString OAIInvoice::getCreated() const {
    return m_created;
}
void OAIInvoice::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIInvoice::is_created_Set() const{
    return m_created_isSet;
}

bool OAIInvoice::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIInvoice::getCreatedById() const {
    return m_created_by_id;
}
void OAIInvoice::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIInvoice::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIInvoice::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIInvoice::getCurrencyId() const {
    return m_currency_id;
}
void OAIInvoice::setCurrencyId(const QString &currency_id) {
    m_currency_id = currency_id;
    m_currency_id_isSet = true;
}

bool OAIInvoice::is_currency_id_Set() const{
    return m_currency_id_isSet;
}

bool OAIInvoice::is_currency_id_Valid() const{
    return m_currency_id_isValid;
}

QDate OAIInvoice::getDateFrom() const {
    return m_date_from;
}
void OAIInvoice::setDateFrom(const QDate &date_from) {
    m_date_from = date_from;
    m_date_from_isSet = true;
}

bool OAIInvoice::is_date_from_Set() const{
    return m_date_from_isSet;
}

bool OAIInvoice::is_date_from_Valid() const{
    return m_date_from_isValid;
}

QDate OAIInvoice::getDateTo() const {
    return m_date_to;
}
void OAIInvoice::setDateTo(const QDate &date_to) {
    m_date_to = date_to;
    m_date_to_isSet = true;
}

bool OAIInvoice::is_date_to_Set() const{
    return m_date_to_isSet;
}

bool OAIInvoice::is_date_to_Valid() const{
    return m_date_to_isValid;
}

QString OAIInvoice::getDeleted() const {
    return m_deleted;
}
void OAIInvoice::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIInvoice::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIInvoice::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIInvoice::getDownloaded() const {
    return m_downloaded;
}
void OAIInvoice::setDownloaded(const QString &downloaded) {
    m_downloaded = downloaded;
    m_downloaded_isSet = true;
}

bool OAIInvoice::is_downloaded_Set() const{
    return m_downloaded_isSet;
}

bool OAIInvoice::is_downloaded_Valid() const{
    return m_downloaded_isValid;
}

QString OAIInvoice::getErpId() const {
    return m_erp_id;
}
void OAIInvoice::setErpId(const QString &erp_id) {
    m_erp_id = erp_id;
    m_erp_id_isSet = true;
}

bool OAIInvoice::is_erp_id_Set() const{
    return m_erp_id_isSet;
}

bool OAIInvoice::is_erp_id_Valid() const{
    return m_erp_id_isValid;
}

QString OAIInvoice::getErpPaymentTermId() const {
    return m_erp_payment_term_id;
}
void OAIInvoice::setErpPaymentTermId(const QString &erp_payment_term_id) {
    m_erp_payment_term_id = erp_payment_term_id;
    m_erp_payment_term_id_isSet = true;
}

bool OAIInvoice::is_erp_payment_term_id_Set() const{
    return m_erp_payment_term_id_isSet;
}

bool OAIInvoice::is_erp_payment_term_id_Valid() const{
    return m_erp_payment_term_id_isValid;
}

bool OAIInvoice::isEuCustomer() const {
    return m_eu_customer;
}
void OAIInvoice::setEuCustomer(const bool &eu_customer) {
    m_eu_customer = eu_customer;
    m_eu_customer_isSet = true;
}

bool OAIInvoice::is_eu_customer_Set() const{
    return m_eu_customer_isSet;
}

bool OAIInvoice::is_eu_customer_Valid() const{
    return m_eu_customer_isValid;
}

float OAIInvoice::getGrossPayment() const {
    return m_gross_payment;
}
void OAIInvoice::setGrossPayment(const float &gross_payment) {
    m_gross_payment = gross_payment;
    m_gross_payment_isSet = true;
}

bool OAIInvoice::is_gross_payment_Set() const{
    return m_gross_payment_isSet;
}

bool OAIInvoice::is_gross_payment_Valid() const{
    return m_gross_payment_isValid;
}

bool OAIInvoice::isGroupByForms() const {
    return m_group_by_forms;
}
void OAIInvoice::setGroupByForms(const bool &group_by_forms) {
    m_group_by_forms = group_by_forms;
    m_group_by_forms_isSet = true;
}

bool OAIInvoice::is_group_by_forms_Set() const{
    return m_group_by_forms_isSet;
}

bool OAIInvoice::is_group_by_forms_Valid() const{
    return m_group_by_forms_isValid;
}

QString OAIInvoice::getId() const {
    return m_id;
}
void OAIInvoice::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIInvoice::is_id_Set() const{
    return m_id_isSet;
}

bool OAIInvoice::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIInvoice::isIncludeInvoicedLines() const {
    return m_include_invoiced_lines;
}
void OAIInvoice::setIncludeInvoicedLines(const bool &include_invoiced_lines) {
    m_include_invoiced_lines = include_invoiced_lines;
    m_include_invoiced_lines_isSet = true;
}

bool OAIInvoice::is_include_invoiced_lines_Set() const{
    return m_include_invoiced_lines_isSet;
}

bool OAIInvoice::is_include_invoiced_lines_Valid() const{
    return m_include_invoiced_lines_isValid;
}

QString OAIInvoice::getIntegrationId() const {
    return m_integration_id;
}
void OAIInvoice::setIntegrationId(const QString &integration_id) {
    m_integration_id = integration_id;
    m_integration_id_isSet = true;
}

bool OAIInvoice::is_integration_id_Set() const{
    return m_integration_id_isSet;
}

bool OAIInvoice::is_integration_id_Valid() const{
    return m_integration_id_isValid;
}

qint32 OAIInvoice::getInvoiceNumber() const {
    return m_invoice_number;
}
void OAIInvoice::setInvoiceNumber(const qint32 &invoice_number) {
    m_invoice_number = invoice_number;
    m_invoice_number_isSet = true;
}

bool OAIInvoice::is_invoice_number_Set() const{
    return m_invoice_number_isSet;
}

bool OAIInvoice::is_invoice_number_Valid() const{
    return m_invoice_number_isValid;
}

bool OAIInvoice::isIsDraft() const {
    return m_is_draft;
}
void OAIInvoice::setIsDraft(const bool &is_draft) {
    m_is_draft = is_draft;
    m_is_draft_isSet = true;
}

bool OAIInvoice::is_is_draft_Set() const{
    return m_is_draft_isSet;
}

bool OAIInvoice::is_is_draft_Valid() const{
    return m_is_draft_isValid;
}

bool OAIInvoice::isIsFinalInvoice() const {
    return m_is_final_invoice;
}
void OAIInvoice::setIsFinalInvoice(const bool &is_final_invoice) {
    m_is_final_invoice = is_final_invoice;
    m_is_final_invoice_isSet = true;
}

bool OAIInvoice::is_is_final_invoice_Set() const{
    return m_is_final_invoice_isSet;
}

bool OAIInvoice::is_is_final_invoice_Valid() const{
    return m_is_final_invoice_isValid;
}

bool OAIInvoice::isIsLocked() const {
    return m_is_locked;
}
void OAIInvoice::setIsLocked(const bool &is_locked) {
    m_is_locked = is_locked;
    m_is_locked_isSet = true;
}

bool OAIInvoice::is_is_locked_Set() const{
    return m_is_locked_isSet;
}

bool OAIInvoice::is_is_locked_Valid() const{
    return m_is_locked_isValid;
}

bool OAIInvoice::isIsOffer() const {
    return m_is_offer;
}
void OAIInvoice::setIsOffer(const bool &is_offer) {
    m_is_offer = is_offer;
    m_is_offer_isSet = true;
}

bool OAIInvoice::is_is_offer_Set() const{
    return m_is_offer_isSet;
}

bool OAIInvoice::is_is_offer_Valid() const{
    return m_is_offer_isValid;
}

QDate OAIInvoice::getIssuedDate() const {
    return m_issued_date;
}
void OAIInvoice::setIssuedDate(const QDate &issued_date) {
    m_issued_date = issued_date;
    m_issued_date_isSet = true;
}

bool OAIInvoice::is_issued_date_Set() const{
    return m_issued_date_isSet;
}

bool OAIInvoice::is_issued_date_Valid() const{
    return m_issued_date_isValid;
}

QString OAIInvoice::getMessage() const {
    return m_message;
}
void OAIInvoice::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIInvoice::is_message_Set() const{
    return m_message_isSet;
}

bool OAIInvoice::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIInvoice::getModified() const {
    return m_modified;
}
void OAIInvoice::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIInvoice::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIInvoice::is_modified_Valid() const{
    return m_modified_isValid;
}

float OAIInvoice::getNetPayment() const {
    return m_net_payment;
}
void OAIInvoice::setNetPayment(const float &net_payment) {
    m_net_payment = net_payment;
    m_net_payment_isSet = true;
}

bool OAIInvoice::is_net_payment_Set() const{
    return m_net_payment_isSet;
}

bool OAIInvoice::is_net_payment_Valid() const{
    return m_net_payment_isValid;
}

qint32 OAIInvoice::getOfferNumber() const {
    return m_offer_number;
}
void OAIInvoice::setOfferNumber(const qint32 &offer_number) {
    m_offer_number = offer_number;
    m_offer_number_isSet = true;
}

bool OAIInvoice::is_offer_number_Set() const{
    return m_offer_number_isSet;
}

bool OAIInvoice::is_offer_number_Valid() const{
    return m_offer_number_isValid;
}

QString OAIInvoice::getOrderLineGroupId() const {
    return m_order_line_group_id;
}
void OAIInvoice::setOrderLineGroupId(const QString &order_line_group_id) {
    m_order_line_group_id = order_line_group_id;
    m_order_line_group_id_isSet = true;
}

bool OAIInvoice::is_order_line_group_id_Set() const{
    return m_order_line_group_id_isSet;
}

bool OAIInvoice::is_order_line_group_id_Valid() const{
    return m_order_line_group_id_isValid;
}

QDate OAIInvoice::getPaymentDueDate() const {
    return m_payment_due_date;
}
void OAIInvoice::setPaymentDueDate(const QDate &payment_due_date) {
    m_payment_due_date = payment_due_date;
    m_payment_due_date_isSet = true;
}

bool OAIInvoice::is_payment_due_date_Set() const{
    return m_payment_due_date_isSet;
}

bool OAIInvoice::is_payment_due_date_Valid() const{
    return m_payment_due_date_isValid;
}

QString OAIInvoice::getPaymentTermId() const {
    return m_payment_term_id;
}
void OAIInvoice::setPaymentTermId(const QString &payment_term_id) {
    m_payment_term_id = payment_term_id;
    m_payment_term_id_isSet = true;
}

bool OAIInvoice::is_payment_term_id_Set() const{
    return m_payment_term_id_isSet;
}

bool OAIInvoice::is_payment_term_id_Valid() const{
    return m_payment_term_id_isValid;
}

QString OAIInvoice::getProjectId() const {
    return m_project_id;
}
void OAIInvoice::setProjectId(const QString &project_id) {
    m_project_id = project_id;
    m_project_id_isSet = true;
}

bool OAIInvoice::is_project_id_Set() const{
    return m_project_id_isSet;
}

bool OAIInvoice::is_project_id_Valid() const{
    return m_project_id_isValid;
}

bool OAIInvoice::isProjectOverviewAttached() const {
    return m_project_overview_attached;
}
void OAIInvoice::setProjectOverviewAttached(const bool &project_overview_attached) {
    m_project_overview_attached = project_overview_attached;
    m_project_overview_attached_isSet = true;
}

bool OAIInvoice::is_project_overview_attached_Set() const{
    return m_project_overview_attached_isSet;
}

bool OAIInvoice::is_project_overview_attached_Valid() const{
    return m_project_overview_attached_isValid;
}

QString OAIInvoice::getReference() const {
    return m_reference;
}
void OAIInvoice::setReference(const QString &reference) {
    m_reference = reference;
    m_reference_isSet = true;
}

bool OAIInvoice::is_reference_Set() const{
    return m_reference_isSet;
}

bool OAIInvoice::is_reference_Valid() const{
    return m_reference_isValid;
}

bool OAIInvoice::isShowEmployeeName() const {
    return m_show_employee_name;
}
void OAIInvoice::setShowEmployeeName(const bool &show_employee_name) {
    m_show_employee_name = show_employee_name;
    m_show_employee_name_isSet = true;
}

bool OAIInvoice::is_show_employee_name_Set() const{
    return m_show_employee_name_isSet;
}

bool OAIInvoice::is_show_employee_name_Valid() const{
    return m_show_employee_name_isValid;
}

bool OAIInvoice::isShowPriceProductBundle() const {
    return m_show_price_product_bundle;
}
void OAIInvoice::setShowPriceProductBundle(const bool &show_price_product_bundle) {
    m_show_price_product_bundle = show_price_product_bundle;
    m_show_price_product_bundle_isSet = true;
}

bool OAIInvoice::is_show_price_product_bundle_Set() const{
    return m_show_price_product_bundle_isSet;
}

bool OAIInvoice::is_show_price_product_bundle_Valid() const{
    return m_show_price_product_bundle_isValid;
}

bool OAIInvoice::isShowPricesProductsAndHours() const {
    return m_show_prices_products_and_hours;
}
void OAIInvoice::setShowPricesProductsAndHours(const bool &show_prices_products_and_hours) {
    m_show_prices_products_and_hours = show_prices_products_and_hours;
    m_show_prices_products_and_hours_isSet = true;
}

bool OAIInvoice::is_show_prices_products_and_hours_Set() const{
    return m_show_prices_products_and_hours_isSet;
}

bool OAIInvoice::is_show_prices_products_and_hours_Valid() const{
    return m_show_prices_products_and_hours_isValid;
}

bool OAIInvoice::isShowProductImages() const {
    return m_show_product_images;
}
void OAIInvoice::setShowProductImages(const bool &show_product_images) {
    m_show_product_images = show_product_images;
    m_show_product_images_isSet = true;
}

bool OAIInvoice::is_show_product_images_Set() const{
    return m_show_product_images_isSet;
}

bool OAIInvoice::is_show_product_images_Valid() const{
    return m_show_product_images_isValid;
}

bool OAIInvoice::isShowProductsProductBundle() const {
    return m_show_products_product_bundle;
}
void OAIInvoice::setShowProductsProductBundle(const bool &show_products_product_bundle) {
    m_show_products_product_bundle = show_products_product_bundle;
    m_show_products_product_bundle_isSet = true;
}

bool OAIInvoice::is_show_products_product_bundle_Set() const{
    return m_show_products_product_bundle_isSet;
}

bool OAIInvoice::is_show_products_product_bundle_Valid() const{
    return m_show_products_product_bundle_isValid;
}

QString OAIInvoice::getTitle() const {
    return m_title;
}
void OAIInvoice::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIInvoice::is_title_Set() const{
    return m_title_isSet;
}

bool OAIInvoice::is_title_Valid() const{
    return m_title_isValid;
}

float OAIInvoice::getTotalCostPrice() const {
    return m_total_cost_price;
}
void OAIInvoice::setTotalCostPrice(const float &total_cost_price) {
    m_total_cost_price = total_cost_price;
    m_total_cost_price_isSet = true;
}

bool OAIInvoice::is_total_cost_price_Set() const{
    return m_total_cost_price_isSet;
}

bool OAIInvoice::is_total_cost_price_Valid() const{
    return m_total_cost_price_isValid;
}

float OAIInvoice::getTotalDiscountPercent() const {
    return m_total_discount_percent;
}
void OAIInvoice::setTotalDiscountPercent(const float &total_discount_percent) {
    m_total_discount_percent = total_discount_percent;
    m_total_discount_percent_isSet = true;
}

bool OAIInvoice::is_total_discount_percent_Set() const{
    return m_total_discount_percent_isSet;
}

bool OAIInvoice::is_total_discount_percent_Valid() const{
    return m_total_discount_percent_isValid;
}

qint32 OAIInvoice::getVatPercent() const {
    return m_vat_percent;
}
void OAIInvoice::setVatPercent(const qint32 &vat_percent) {
    m_vat_percent = vat_percent;
    m_vat_percent_isSet = true;
}

bool OAIInvoice::is_vat_percent_Set() const{
    return m_vat_percent_isSet;
}

bool OAIInvoice::is_vat_percent_Valid() const{
    return m_vat_percent_isValid;
}

QString OAIInvoice::getVendorId() const {
    return m_vendor_id;
}
void OAIInvoice::setVendorId(const QString &vendor_id) {
    m_vendor_id = vendor_id;
    m_vendor_id_isSet = true;
}

bool OAIInvoice::is_vendor_id_Set() const{
    return m_vendor_id_isSet;
}

bool OAIInvoice::is_vendor_id_Valid() const{
    return m_vendor_id_isValid;
}

bool OAIInvoice::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_all_products_one_line_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_all_working_hours_one_line_isSet) {
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

        if (m_date_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_downloaded_isSet) {
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

        if (m_eu_customer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gross_payment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_by_forms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_invoiced_lines_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_integration_id_isSet) {
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

        if (m_is_final_invoice_isSet) {
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

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_net_payment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offer_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_line_group_id_isSet) {
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

        if (m_project_overview_attached_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_employee_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_price_product_bundle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_prices_products_and_hours_isSet) {
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

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_cost_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_discount_percent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_percent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInvoice::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
