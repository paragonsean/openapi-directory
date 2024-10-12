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

#include "OAIProject.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProject::OAIProject(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProject::OAIProject() {
    this->initializeModel();
}

OAIProject::~OAIProject() {}

void OAIProject::initializeModel() {

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

    m_end_time_isSet = false;
    m_end_time_isValid = false;

    m_erp_project_id_isSet = false;
    m_erp_project_id_isValid = false;

    m_erp_task_id_isSet = false;
    m_erp_task_id_isValid = false;

    m_full_name_isSet = false;
    m_full_name_isValid = false;

    m_has_final_invoice_isSet = false;
    m_has_final_invoice_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_fixed_price_isSet = false;
    m_is_fixed_price_isValid = false;

    m_is_offer_isSet = false;
    m_is_offer_isValid = false;

    m_is_rotten_isSet = false;
    m_is_rotten_isValid = false;

    m_latitude_isSet = false;
    m_latitude_isValid = false;

    m_longitude_isSet = false;
    m_longitude_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_not_invoiced_amount_isSet = false;
    m_not_invoiced_amount_isValid = false;

    m_offer_id_isSet = false;
    m_offer_id_isValid = false;

    m_parent_id_isSet = false;
    m_parent_id_isValid = false;

    m_pre_calculation_id_isSet = false;
    m_pre_calculation_id_isValid = false;

    m_products_total_cost_price_isSet = false;
    m_products_total_cost_price_isValid = false;

    m_project_image_url_isSet = false;
    m_project_image_url_isValid = false;

    m_project_number_isSet = false;
    m_project_number_isValid = false;

    m_project_status_id_isSet = false;
    m_project_status_id_isValid = false;

    m_shared_project_id_isSet = false;
    m_shared_project_id_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_street_name_isSet = false;
    m_street_name_isValid = false;

    m_thumbnail_isSet = false;
    m_thumbnail_isValid = false;

    m_total_sales_price_isSet = false;
    m_total_sales_price_isValid = false;

    m_working_hours_total_cost_price_isSet = false;
    m_working_hours_total_cost_price_isValid = false;
}

void OAIProject::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProject::fromJsonObject(QJsonObject json) {

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

    m_end_time_isValid = ::OpenAPI::fromJsonValue(m_end_time, json[QString("end_time")]);
    m_end_time_isSet = !json[QString("end_time")].isNull() && m_end_time_isValid;

    m_erp_project_id_isValid = ::OpenAPI::fromJsonValue(m_erp_project_id, json[QString("erp_project_id")]);
    m_erp_project_id_isSet = !json[QString("erp_project_id")].isNull() && m_erp_project_id_isValid;

    m_erp_task_id_isValid = ::OpenAPI::fromJsonValue(m_erp_task_id, json[QString("erp_task_id")]);
    m_erp_task_id_isSet = !json[QString("erp_task_id")].isNull() && m_erp_task_id_isValid;

    m_full_name_isValid = ::OpenAPI::fromJsonValue(m_full_name, json[QString("full_name")]);
    m_full_name_isSet = !json[QString("full_name")].isNull() && m_full_name_isValid;

    m_has_final_invoice_isValid = ::OpenAPI::fromJsonValue(m_has_final_invoice, json[QString("has_final_invoice")]);
    m_has_final_invoice_isSet = !json[QString("has_final_invoice")].isNull() && m_has_final_invoice_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_fixed_price_isValid = ::OpenAPI::fromJsonValue(m_is_fixed_price, json[QString("is_fixed_price")]);
    m_is_fixed_price_isSet = !json[QString("is_fixed_price")].isNull() && m_is_fixed_price_isValid;

    m_is_offer_isValid = ::OpenAPI::fromJsonValue(m_is_offer, json[QString("is_offer")]);
    m_is_offer_isSet = !json[QString("is_offer")].isNull() && m_is_offer_isValid;

    m_is_rotten_isValid = ::OpenAPI::fromJsonValue(m_is_rotten, json[QString("is_rotten")]);
    m_is_rotten_isSet = !json[QString("is_rotten")].isNull() && m_is_rotten_isValid;

    m_latitude_isValid = ::OpenAPI::fromJsonValue(m_latitude, json[QString("latitude")]);
    m_latitude_isSet = !json[QString("latitude")].isNull() && m_latitude_isValid;

    m_longitude_isValid = ::OpenAPI::fromJsonValue(m_longitude, json[QString("longitude")]);
    m_longitude_isSet = !json[QString("longitude")].isNull() && m_longitude_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_not_invoiced_amount_isValid = ::OpenAPI::fromJsonValue(m_not_invoiced_amount, json[QString("not_invoiced_amount")]);
    m_not_invoiced_amount_isSet = !json[QString("not_invoiced_amount")].isNull() && m_not_invoiced_amount_isValid;

    m_offer_id_isValid = ::OpenAPI::fromJsonValue(m_offer_id, json[QString("offer_id")]);
    m_offer_id_isSet = !json[QString("offer_id")].isNull() && m_offer_id_isValid;

    m_parent_id_isValid = ::OpenAPI::fromJsonValue(m_parent_id, json[QString("parent_id")]);
    m_parent_id_isSet = !json[QString("parent_id")].isNull() && m_parent_id_isValid;

    m_pre_calculation_id_isValid = ::OpenAPI::fromJsonValue(m_pre_calculation_id, json[QString("pre_calculation_id")]);
    m_pre_calculation_id_isSet = !json[QString("pre_calculation_id")].isNull() && m_pre_calculation_id_isValid;

    m_products_total_cost_price_isValid = ::OpenAPI::fromJsonValue(m_products_total_cost_price, json[QString("products_total_cost_price")]);
    m_products_total_cost_price_isSet = !json[QString("products_total_cost_price")].isNull() && m_products_total_cost_price_isValid;

    m_project_image_url_isValid = ::OpenAPI::fromJsonValue(m_project_image_url, json[QString("project_image_url")]);
    m_project_image_url_isSet = !json[QString("project_image_url")].isNull() && m_project_image_url_isValid;

    m_project_number_isValid = ::OpenAPI::fromJsonValue(m_project_number, json[QString("project_number")]);
    m_project_number_isSet = !json[QString("project_number")].isNull() && m_project_number_isValid;

    m_project_status_id_isValid = ::OpenAPI::fromJsonValue(m_project_status_id, json[QString("project_status_id")]);
    m_project_status_id_isSet = !json[QString("project_status_id")].isNull() && m_project_status_id_isValid;

    m_shared_project_id_isValid = ::OpenAPI::fromJsonValue(m_shared_project_id, json[QString("shared_project_id")]);
    m_shared_project_id_isSet = !json[QString("shared_project_id")].isNull() && m_shared_project_id_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("start_time")]);
    m_start_time_isSet = !json[QString("start_time")].isNull() && m_start_time_isValid;

    m_street_name_isValid = ::OpenAPI::fromJsonValue(m_street_name, json[QString("street_name")]);
    m_street_name_isSet = !json[QString("street_name")].isNull() && m_street_name_isValid;

    m_thumbnail_isValid = ::OpenAPI::fromJsonValue(m_thumbnail, json[QString("thumbnail")]);
    m_thumbnail_isSet = !json[QString("thumbnail")].isNull() && m_thumbnail_isValid;

    m_total_sales_price_isValid = ::OpenAPI::fromJsonValue(m_total_sales_price, json[QString("total_sales_price")]);
    m_total_sales_price_isSet = !json[QString("total_sales_price")].isNull() && m_total_sales_price_isValid;

    m_working_hours_total_cost_price_isValid = ::OpenAPI::fromJsonValue(m_working_hours_total_cost_price, json[QString("working_hours_total_cost_price")]);
    m_working_hours_total_cost_price_isSet = !json[QString("working_hours_total_cost_price")].isNull() && m_working_hours_total_cost_price_isValid;
}

QString OAIProject::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProject::asJsonObject() const {
    QJsonObject obj;
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
    if (m_end_time_isSet) {
        obj.insert(QString("end_time"), ::OpenAPI::toJsonValue(m_end_time));
    }
    if (m_erp_project_id_isSet) {
        obj.insert(QString("erp_project_id"), ::OpenAPI::toJsonValue(m_erp_project_id));
    }
    if (m_erp_task_id_isSet) {
        obj.insert(QString("erp_task_id"), ::OpenAPI::toJsonValue(m_erp_task_id));
    }
    if (m_full_name_isSet) {
        obj.insert(QString("full_name"), ::OpenAPI::toJsonValue(m_full_name));
    }
    if (m_has_final_invoice_isSet) {
        obj.insert(QString("has_final_invoice"), ::OpenAPI::toJsonValue(m_has_final_invoice));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_fixed_price_isSet) {
        obj.insert(QString("is_fixed_price"), ::OpenAPI::toJsonValue(m_is_fixed_price));
    }
    if (m_is_offer_isSet) {
        obj.insert(QString("is_offer"), ::OpenAPI::toJsonValue(m_is_offer));
    }
    if (m_is_rotten_isSet) {
        obj.insert(QString("is_rotten"), ::OpenAPI::toJsonValue(m_is_rotten));
    }
    if (m_latitude_isSet) {
        obj.insert(QString("latitude"), ::OpenAPI::toJsonValue(m_latitude));
    }
    if (m_longitude_isSet) {
        obj.insert(QString("longitude"), ::OpenAPI::toJsonValue(m_longitude));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_not_invoiced_amount_isSet) {
        obj.insert(QString("not_invoiced_amount"), ::OpenAPI::toJsonValue(m_not_invoiced_amount));
    }
    if (m_offer_id_isSet) {
        obj.insert(QString("offer_id"), ::OpenAPI::toJsonValue(m_offer_id));
    }
    if (m_parent_id_isSet) {
        obj.insert(QString("parent_id"), ::OpenAPI::toJsonValue(m_parent_id));
    }
    if (m_pre_calculation_id_isSet) {
        obj.insert(QString("pre_calculation_id"), ::OpenAPI::toJsonValue(m_pre_calculation_id));
    }
    if (m_products_total_cost_price_isSet) {
        obj.insert(QString("products_total_cost_price"), ::OpenAPI::toJsonValue(m_products_total_cost_price));
    }
    if (m_project_image_url_isSet) {
        obj.insert(QString("project_image_url"), ::OpenAPI::toJsonValue(m_project_image_url));
    }
    if (m_project_number_isSet) {
        obj.insert(QString("project_number"), ::OpenAPI::toJsonValue(m_project_number));
    }
    if (m_project_status_id_isSet) {
        obj.insert(QString("project_status_id"), ::OpenAPI::toJsonValue(m_project_status_id));
    }
    if (m_shared_project_id_isSet) {
        obj.insert(QString("shared_project_id"), ::OpenAPI::toJsonValue(m_shared_project_id));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("start_time"), ::OpenAPI::toJsonValue(m_start_time));
    }
    if (m_street_name_isSet) {
        obj.insert(QString("street_name"), ::OpenAPI::toJsonValue(m_street_name));
    }
    if (m_thumbnail_isSet) {
        obj.insert(QString("thumbnail"), ::OpenAPI::toJsonValue(m_thumbnail));
    }
    if (m_total_sales_price_isSet) {
        obj.insert(QString("total_sales_price"), ::OpenAPI::toJsonValue(m_total_sales_price));
    }
    if (m_working_hours_total_cost_price_isSet) {
        obj.insert(QString("working_hours_total_cost_price"), ::OpenAPI::toJsonValue(m_working_hours_total_cost_price));
    }
    return obj;
}

QString OAIProject::getCityId() const {
    return m_city_id;
}
void OAIProject::setCityId(const QString &city_id) {
    m_city_id = city_id;
    m_city_id_isSet = true;
}

bool OAIProject::is_city_id_Set() const{
    return m_city_id_isSet;
}

bool OAIProject::is_city_id_Valid() const{
    return m_city_id_isValid;
}

QString OAIProject::getCompanyId() const {
    return m_company_id;
}
void OAIProject::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIProject::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIProject::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIProject::getContactId() const {
    return m_contact_id;
}
void OAIProject::setContactId(const QString &contact_id) {
    m_contact_id = contact_id;
    m_contact_id_isSet = true;
}

bool OAIProject::is_contact_id_Set() const{
    return m_contact_id_isSet;
}

bool OAIProject::is_contact_id_Valid() const{
    return m_contact_id_isValid;
}

QString OAIProject::getCreated() const {
    return m_created;
}
void OAIProject::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIProject::is_created_Set() const{
    return m_created_isSet;
}

bool OAIProject::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIProject::getCreatedById() const {
    return m_created_by_id;
}
void OAIProject::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIProject::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIProject::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIProject::getDeleted() const {
    return m_deleted;
}
void OAIProject::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIProject::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIProject::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIProject::getDescription() const {
    return m_description;
}
void OAIProject::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIProject::is_description_Set() const{
    return m_description_isSet;
}

bool OAIProject::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIProject::getEndTime() const {
    return m_end_time;
}
void OAIProject::setEndTime(const QString &end_time) {
    m_end_time = end_time;
    m_end_time_isSet = true;
}

bool OAIProject::is_end_time_Set() const{
    return m_end_time_isSet;
}

bool OAIProject::is_end_time_Valid() const{
    return m_end_time_isValid;
}

QString OAIProject::getErpProjectId() const {
    return m_erp_project_id;
}
void OAIProject::setErpProjectId(const QString &erp_project_id) {
    m_erp_project_id = erp_project_id;
    m_erp_project_id_isSet = true;
}

bool OAIProject::is_erp_project_id_Set() const{
    return m_erp_project_id_isSet;
}

bool OAIProject::is_erp_project_id_Valid() const{
    return m_erp_project_id_isValid;
}

QString OAIProject::getErpTaskId() const {
    return m_erp_task_id;
}
void OAIProject::setErpTaskId(const QString &erp_task_id) {
    m_erp_task_id = erp_task_id;
    m_erp_task_id_isSet = true;
}

bool OAIProject::is_erp_task_id_Set() const{
    return m_erp_task_id_isSet;
}

bool OAIProject::is_erp_task_id_Valid() const{
    return m_erp_task_id_isValid;
}

QString OAIProject::getFullName() const {
    return m_full_name;
}
void OAIProject::setFullName(const QString &full_name) {
    m_full_name = full_name;
    m_full_name_isSet = true;
}

bool OAIProject::is_full_name_Set() const{
    return m_full_name_isSet;
}

bool OAIProject::is_full_name_Valid() const{
    return m_full_name_isValid;
}

bool OAIProject::isHasFinalInvoice() const {
    return m_has_final_invoice;
}
void OAIProject::setHasFinalInvoice(const bool &has_final_invoice) {
    m_has_final_invoice = has_final_invoice;
    m_has_final_invoice_isSet = true;
}

bool OAIProject::is_has_final_invoice_Set() const{
    return m_has_final_invoice_isSet;
}

bool OAIProject::is_has_final_invoice_Valid() const{
    return m_has_final_invoice_isValid;
}

QString OAIProject::getId() const {
    return m_id;
}
void OAIProject::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProject::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProject::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIProject::isIsFixedPrice() const {
    return m_is_fixed_price;
}
void OAIProject::setIsFixedPrice(const bool &is_fixed_price) {
    m_is_fixed_price = is_fixed_price;
    m_is_fixed_price_isSet = true;
}

bool OAIProject::is_is_fixed_price_Set() const{
    return m_is_fixed_price_isSet;
}

bool OAIProject::is_is_fixed_price_Valid() const{
    return m_is_fixed_price_isValid;
}

bool OAIProject::getIsOffer() const {
    return m_is_offer;
}
void OAIProject::setIsOffer(const bool &is_offer) {
    m_is_offer = is_offer;
    m_is_offer_isSet = true;
}

bool OAIProject::is_is_offer_Set() const{
    return m_is_offer_isSet;
}

bool OAIProject::is_is_offer_Valid() const{
    return m_is_offer_isValid;
}

QString OAIProject::getIsRotten() const {
    return m_is_rotten;
}
void OAIProject::setIsRotten(const QString &is_rotten) {
    m_is_rotten = is_rotten;
    m_is_rotten_isSet = true;
}

bool OAIProject::is_is_rotten_Set() const{
    return m_is_rotten_isSet;
}

bool OAIProject::is_is_rotten_Valid() const{
    return m_is_rotten_isValid;
}

QString OAIProject::getLatitude() const {
    return m_latitude;
}
void OAIProject::setLatitude(const QString &latitude) {
    m_latitude = latitude;
    m_latitude_isSet = true;
}

bool OAIProject::is_latitude_Set() const{
    return m_latitude_isSet;
}

bool OAIProject::is_latitude_Valid() const{
    return m_latitude_isValid;
}

QString OAIProject::getLongitude() const {
    return m_longitude;
}
void OAIProject::setLongitude(const QString &longitude) {
    m_longitude = longitude;
    m_longitude_isSet = true;
}

bool OAIProject::is_longitude_Set() const{
    return m_longitude_isSet;
}

bool OAIProject::is_longitude_Valid() const{
    return m_longitude_isValid;
}

QString OAIProject::getModified() const {
    return m_modified;
}
void OAIProject::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIProject::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIProject::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIProject::getName() const {
    return m_name;
}
void OAIProject::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProject::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProject::is_name_Valid() const{
    return m_name_isValid;
}

float OAIProject::getNotInvoicedAmount() const {
    return m_not_invoiced_amount;
}
void OAIProject::setNotInvoicedAmount(const float &not_invoiced_amount) {
    m_not_invoiced_amount = not_invoiced_amount;
    m_not_invoiced_amount_isSet = true;
}

bool OAIProject::is_not_invoiced_amount_Set() const{
    return m_not_invoiced_amount_isSet;
}

bool OAIProject::is_not_invoiced_amount_Valid() const{
    return m_not_invoiced_amount_isValid;
}

QString OAIProject::getOfferId() const {
    return m_offer_id;
}
void OAIProject::setOfferId(const QString &offer_id) {
    m_offer_id = offer_id;
    m_offer_id_isSet = true;
}

bool OAIProject::is_offer_id_Set() const{
    return m_offer_id_isSet;
}

bool OAIProject::is_offer_id_Valid() const{
    return m_offer_id_isValid;
}

QString OAIProject::getParentId() const {
    return m_parent_id;
}
void OAIProject::setParentId(const QString &parent_id) {
    m_parent_id = parent_id;
    m_parent_id_isSet = true;
}

bool OAIProject::is_parent_id_Set() const{
    return m_parent_id_isSet;
}

bool OAIProject::is_parent_id_Valid() const{
    return m_parent_id_isValid;
}

QString OAIProject::getPreCalculationId() const {
    return m_pre_calculation_id;
}
void OAIProject::setPreCalculationId(const QString &pre_calculation_id) {
    m_pre_calculation_id = pre_calculation_id;
    m_pre_calculation_id_isSet = true;
}

bool OAIProject::is_pre_calculation_id_Set() const{
    return m_pre_calculation_id_isSet;
}

bool OAIProject::is_pre_calculation_id_Valid() const{
    return m_pre_calculation_id_isValid;
}

float OAIProject::getProductsTotalCostPrice() const {
    return m_products_total_cost_price;
}
void OAIProject::setProductsTotalCostPrice(const float &products_total_cost_price) {
    m_products_total_cost_price = products_total_cost_price;
    m_products_total_cost_price_isSet = true;
}

bool OAIProject::is_products_total_cost_price_Set() const{
    return m_products_total_cost_price_isSet;
}

bool OAIProject::is_products_total_cost_price_Valid() const{
    return m_products_total_cost_price_isValid;
}

QString OAIProject::getProjectImageUrl() const {
    return m_project_image_url;
}
void OAIProject::setProjectImageUrl(const QString &project_image_url) {
    m_project_image_url = project_image_url;
    m_project_image_url_isSet = true;
}

bool OAIProject::is_project_image_url_Set() const{
    return m_project_image_url_isSet;
}

bool OAIProject::is_project_image_url_Valid() const{
    return m_project_image_url_isValid;
}

double OAIProject::getProjectNumber() const {
    return m_project_number;
}
void OAIProject::setProjectNumber(const double &project_number) {
    m_project_number = project_number;
    m_project_number_isSet = true;
}

bool OAIProject::is_project_number_Set() const{
    return m_project_number_isSet;
}

bool OAIProject::is_project_number_Valid() const{
    return m_project_number_isValid;
}

QString OAIProject::getProjectStatusId() const {
    return m_project_status_id;
}
void OAIProject::setProjectStatusId(const QString &project_status_id) {
    m_project_status_id = project_status_id;
    m_project_status_id_isSet = true;
}

bool OAIProject::is_project_status_id_Set() const{
    return m_project_status_id_isSet;
}

bool OAIProject::is_project_status_id_Valid() const{
    return m_project_status_id_isValid;
}

QString OAIProject::getSharedProjectId() const {
    return m_shared_project_id;
}
void OAIProject::setSharedProjectId(const QString &shared_project_id) {
    m_shared_project_id = shared_project_id;
    m_shared_project_id_isSet = true;
}

bool OAIProject::is_shared_project_id_Set() const{
    return m_shared_project_id_isSet;
}

bool OAIProject::is_shared_project_id_Valid() const{
    return m_shared_project_id_isValid;
}

QString OAIProject::getStartTime() const {
    return m_start_time;
}
void OAIProject::setStartTime(const QString &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAIProject::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAIProject::is_start_time_Valid() const{
    return m_start_time_isValid;
}

QString OAIProject::getStreetName() const {
    return m_street_name;
}
void OAIProject::setStreetName(const QString &street_name) {
    m_street_name = street_name;
    m_street_name_isSet = true;
}

bool OAIProject::is_street_name_Set() const{
    return m_street_name_isSet;
}

bool OAIProject::is_street_name_Valid() const{
    return m_street_name_isValid;
}

QString OAIProject::getThumbnail() const {
    return m_thumbnail;
}
void OAIProject::setThumbnail(const QString &thumbnail) {
    m_thumbnail = thumbnail;
    m_thumbnail_isSet = true;
}

bool OAIProject::is_thumbnail_Set() const{
    return m_thumbnail_isSet;
}

bool OAIProject::is_thumbnail_Valid() const{
    return m_thumbnail_isValid;
}

float OAIProject::getTotalSalesPrice() const {
    return m_total_sales_price;
}
void OAIProject::setTotalSalesPrice(const float &total_sales_price) {
    m_total_sales_price = total_sales_price;
    m_total_sales_price_isSet = true;
}

bool OAIProject::is_total_sales_price_Set() const{
    return m_total_sales_price_isSet;
}

bool OAIProject::is_total_sales_price_Valid() const{
    return m_total_sales_price_isValid;
}

float OAIProject::getWorkingHoursTotalCostPrice() const {
    return m_working_hours_total_cost_price;
}
void OAIProject::setWorkingHoursTotalCostPrice(const float &working_hours_total_cost_price) {
    m_working_hours_total_cost_price = working_hours_total_cost_price;
    m_working_hours_total_cost_price_isSet = true;
}

bool OAIProject::is_working_hours_total_cost_price_Set() const{
    return m_working_hours_total_cost_price_isSet;
}

bool OAIProject::is_working_hours_total_cost_price_Valid() const{
    return m_working_hours_total_cost_price_isValid;
}

bool OAIProject::isSet() const {
    bool isObjectUpdated = false;
    do {
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

        if (m_end_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_erp_project_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_erp_task_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_full_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_final_invoice_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_fixed_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_offer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_rotten_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_longitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_not_invoiced_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pre_calculation_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_products_total_cost_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_image_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_status_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shared_project_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_sales_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_working_hours_total_cost_price_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProject::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
