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

#include "OAI_users_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_users_post_request::OAI_users_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_users_post_request::OAI_users_post_request() {
    this->initializeModel();
}

OAI_users_post_request::~OAI_users_post_request() {}

void OAI_users_post_request::initializeModel() {

    m_city_id_isSet = false;
    m_city_id_isValid = false;

    m_cost_price_isSet = false;
    m_cost_price_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_expected_billable_hours_isSet = false;
    m_expected_billable_hours_isValid = false;

    m_extra_price_isSet = false;
    m_extra_price_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_hide_address_isSet = false;
    m_hide_address_isValid = false;

    m_hide_phone_isSet = false;
    m_hide_phone_isValid = false;

    m_initials_isSet = false;
    m_initials_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_language_id_isSet = false;
    m_language_id_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_mobile_isSet = false;
    m_mobile_isValid = false;

    m_mobile_countrycode_isSet = false;
    m_mobile_countrycode_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_phone_countrycode_isSet = false;
    m_phone_countrycode_isValid = false;

    m_receive_form_mails_isSet = false;
    m_receive_form_mails_isValid = false;

    m_roles_isSet = false;
    m_roles_isValid = false;

    m_sale_price_isSet = false;
    m_sale_price_isValid = false;

    m_street_name_isSet = false;
    m_street_name_isValid = false;
}

void OAI_users_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_users_post_request::fromJsonObject(QJsonObject json) {

    m_city_id_isValid = ::OpenAPI::fromJsonValue(m_city_id, json[QString("city_id")]);
    m_city_id_isSet = !json[QString("city_id")].isNull() && m_city_id_isValid;

    m_cost_price_isValid = ::OpenAPI::fromJsonValue(m_cost_price, json[QString("cost_price")]);
    m_cost_price_isSet = !json[QString("cost_price")].isNull() && m_cost_price_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_expected_billable_hours_isValid = ::OpenAPI::fromJsonValue(m_expected_billable_hours, json[QString("expected_billable_hours")]);
    m_expected_billable_hours_isSet = !json[QString("expected_billable_hours")].isNull() && m_expected_billable_hours_isValid;

    m_extra_price_isValid = ::OpenAPI::fromJsonValue(m_extra_price, json[QString("extra_price")]);
    m_extra_price_isSet = !json[QString("extra_price")].isNull() && m_extra_price_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_hide_address_isValid = ::OpenAPI::fromJsonValue(m_hide_address, json[QString("hide_address")]);
    m_hide_address_isSet = !json[QString("hide_address")].isNull() && m_hide_address_isValid;

    m_hide_phone_isValid = ::OpenAPI::fromJsonValue(m_hide_phone, json[QString("hide_phone")]);
    m_hide_phone_isSet = !json[QString("hide_phone")].isNull() && m_hide_phone_isValid;

    m_initials_isValid = ::OpenAPI::fromJsonValue(m_initials, json[QString("initials")]);
    m_initials_isSet = !json[QString("initials")].isNull() && m_initials_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("is_active")]);
    m_is_active_isSet = !json[QString("is_active")].isNull() && m_is_active_isValid;

    m_language_id_isValid = ::OpenAPI::fromJsonValue(m_language_id, json[QString("language_id")]);
    m_language_id_isSet = !json[QString("language_id")].isNull() && m_language_id_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_mobile_isValid = ::OpenAPI::fromJsonValue(m_mobile, json[QString("mobile")]);
    m_mobile_isSet = !json[QString("mobile")].isNull() && m_mobile_isValid;

    m_mobile_countrycode_isValid = ::OpenAPI::fromJsonValue(m_mobile_countrycode, json[QString("mobile_countrycode")]);
    m_mobile_countrycode_isSet = !json[QString("mobile_countrycode")].isNull() && m_mobile_countrycode_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;

    m_phone_countrycode_isValid = ::OpenAPI::fromJsonValue(m_phone_countrycode, json[QString("phone_countrycode")]);
    m_phone_countrycode_isSet = !json[QString("phone_countrycode")].isNull() && m_phone_countrycode_isValid;

    m_receive_form_mails_isValid = ::OpenAPI::fromJsonValue(m_receive_form_mails, json[QString("receive_form_mails")]);
    m_receive_form_mails_isSet = !json[QString("receive_form_mails")].isNull() && m_receive_form_mails_isValid;

    m_roles_isValid = ::OpenAPI::fromJsonValue(m_roles, json[QString("roles")]);
    m_roles_isSet = !json[QString("roles")].isNull() && m_roles_isValid;

    m_sale_price_isValid = ::OpenAPI::fromJsonValue(m_sale_price, json[QString("sale_price")]);
    m_sale_price_isSet = !json[QString("sale_price")].isNull() && m_sale_price_isValid;

    m_street_name_isValid = ::OpenAPI::fromJsonValue(m_street_name, json[QString("street_name")]);
    m_street_name_isSet = !json[QString("street_name")].isNull() && m_street_name_isValid;
}

QString OAI_users_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_users_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_city_id_isSet) {
        obj.insert(QString("city_id"), ::OpenAPI::toJsonValue(m_city_id));
    }
    if (m_cost_price_isSet) {
        obj.insert(QString("cost_price"), ::OpenAPI::toJsonValue(m_cost_price));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_expected_billable_hours_isSet) {
        obj.insert(QString("expected_billable_hours"), ::OpenAPI::toJsonValue(m_expected_billable_hours));
    }
    if (m_extra_price_isSet) {
        obj.insert(QString("extra_price"), ::OpenAPI::toJsonValue(m_extra_price));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_hide_address_isSet) {
        obj.insert(QString("hide_address"), ::OpenAPI::toJsonValue(m_hide_address));
    }
    if (m_hide_phone_isSet) {
        obj.insert(QString("hide_phone"), ::OpenAPI::toJsonValue(m_hide_phone));
    }
    if (m_initials_isSet) {
        obj.insert(QString("initials"), ::OpenAPI::toJsonValue(m_initials));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("is_active"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_language_id_isSet) {
        obj.insert(QString("language_id"), ::OpenAPI::toJsonValue(m_language_id));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_mobile_isSet) {
        obj.insert(QString("mobile"), ::OpenAPI::toJsonValue(m_mobile));
    }
    if (m_mobile_countrycode_isSet) {
        obj.insert(QString("mobile_countrycode"), ::OpenAPI::toJsonValue(m_mobile_countrycode));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_phone_isSet) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_phone_countrycode_isSet) {
        obj.insert(QString("phone_countrycode"), ::OpenAPI::toJsonValue(m_phone_countrycode));
    }
    if (m_receive_form_mails_isSet) {
        obj.insert(QString("receive_form_mails"), ::OpenAPI::toJsonValue(m_receive_form_mails));
    }
    if (m_roles.isSet()) {
        obj.insert(QString("roles"), ::OpenAPI::toJsonValue(m_roles));
    }
    if (m_sale_price_isSet) {
        obj.insert(QString("sale_price"), ::OpenAPI::toJsonValue(m_sale_price));
    }
    if (m_street_name_isSet) {
        obj.insert(QString("street_name"), ::OpenAPI::toJsonValue(m_street_name));
    }
    return obj;
}

QString OAI_users_post_request::getCityId() const {
    return m_city_id;
}
void OAI_users_post_request::setCityId(const QString &city_id) {
    m_city_id = city_id;
    m_city_id_isSet = true;
}

bool OAI_users_post_request::is_city_id_Set() const{
    return m_city_id_isSet;
}

bool OAI_users_post_request::is_city_id_Valid() const{
    return m_city_id_isValid;
}

float OAI_users_post_request::getCostPrice() const {
    return m_cost_price;
}
void OAI_users_post_request::setCostPrice(const float &cost_price) {
    m_cost_price = cost_price;
    m_cost_price_isSet = true;
}

bool OAI_users_post_request::is_cost_price_Set() const{
    return m_cost_price_isSet;
}

bool OAI_users_post_request::is_cost_price_Valid() const{
    return m_cost_price_isValid;
}

QString OAI_users_post_request::getEmail() const {
    return m_email;
}
void OAI_users_post_request::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAI_users_post_request::is_email_Set() const{
    return m_email_isSet;
}

bool OAI_users_post_request::is_email_Valid() const{
    return m_email_isValid;
}

float OAI_users_post_request::getExpectedBillableHours() const {
    return m_expected_billable_hours;
}
void OAI_users_post_request::setExpectedBillableHours(const float &expected_billable_hours) {
    m_expected_billable_hours = expected_billable_hours;
    m_expected_billable_hours_isSet = true;
}

bool OAI_users_post_request::is_expected_billable_hours_Set() const{
    return m_expected_billable_hours_isSet;
}

bool OAI_users_post_request::is_expected_billable_hours_Valid() const{
    return m_expected_billable_hours_isValid;
}

float OAI_users_post_request::getExtraPrice() const {
    return m_extra_price;
}
void OAI_users_post_request::setExtraPrice(const float &extra_price) {
    m_extra_price = extra_price;
    m_extra_price_isSet = true;
}

bool OAI_users_post_request::is_extra_price_Set() const{
    return m_extra_price_isSet;
}

bool OAI_users_post_request::is_extra_price_Valid() const{
    return m_extra_price_isValid;
}

QString OAI_users_post_request::getFirstName() const {
    return m_first_name;
}
void OAI_users_post_request::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAI_users_post_request::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAI_users_post_request::is_first_name_Valid() const{
    return m_first_name_isValid;
}

bool OAI_users_post_request::isHideAddress() const {
    return m_hide_address;
}
void OAI_users_post_request::setHideAddress(const bool &hide_address) {
    m_hide_address = hide_address;
    m_hide_address_isSet = true;
}

bool OAI_users_post_request::is_hide_address_Set() const{
    return m_hide_address_isSet;
}

bool OAI_users_post_request::is_hide_address_Valid() const{
    return m_hide_address_isValid;
}

bool OAI_users_post_request::isHidePhone() const {
    return m_hide_phone;
}
void OAI_users_post_request::setHidePhone(const bool &hide_phone) {
    m_hide_phone = hide_phone;
    m_hide_phone_isSet = true;
}

bool OAI_users_post_request::is_hide_phone_Set() const{
    return m_hide_phone_isSet;
}

bool OAI_users_post_request::is_hide_phone_Valid() const{
    return m_hide_phone_isValid;
}

QString OAI_users_post_request::getInitials() const {
    return m_initials;
}
void OAI_users_post_request::setInitials(const QString &initials) {
    m_initials = initials;
    m_initials_isSet = true;
}

bool OAI_users_post_request::is_initials_Set() const{
    return m_initials_isSet;
}

bool OAI_users_post_request::is_initials_Valid() const{
    return m_initials_isValid;
}

bool OAI_users_post_request::isIsActive() const {
    return m_is_active;
}
void OAI_users_post_request::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAI_users_post_request::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAI_users_post_request::is_is_active_Valid() const{
    return m_is_active_isValid;
}

QString OAI_users_post_request::getLanguageId() const {
    return m_language_id;
}
void OAI_users_post_request::setLanguageId(const QString &language_id) {
    m_language_id = language_id;
    m_language_id_isSet = true;
}

bool OAI_users_post_request::is_language_id_Set() const{
    return m_language_id_isSet;
}

bool OAI_users_post_request::is_language_id_Valid() const{
    return m_language_id_isValid;
}

QString OAI_users_post_request::getLastName() const {
    return m_last_name;
}
void OAI_users_post_request::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAI_users_post_request::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAI_users_post_request::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAI_users_post_request::getMobile() const {
    return m_mobile;
}
void OAI_users_post_request::setMobile(const QString &mobile) {
    m_mobile = mobile;
    m_mobile_isSet = true;
}

bool OAI_users_post_request::is_mobile_Set() const{
    return m_mobile_isSet;
}

bool OAI_users_post_request::is_mobile_Valid() const{
    return m_mobile_isValid;
}

QString OAI_users_post_request::getMobileCountrycode() const {
    return m_mobile_countrycode;
}
void OAI_users_post_request::setMobileCountrycode(const QString &mobile_countrycode) {
    m_mobile_countrycode = mobile_countrycode;
    m_mobile_countrycode_isSet = true;
}

bool OAI_users_post_request::is_mobile_countrycode_Set() const{
    return m_mobile_countrycode_isSet;
}

bool OAI_users_post_request::is_mobile_countrycode_Valid() const{
    return m_mobile_countrycode_isValid;
}

QString OAI_users_post_request::getPassword() const {
    return m_password;
}
void OAI_users_post_request::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAI_users_post_request::is_password_Set() const{
    return m_password_isSet;
}

bool OAI_users_post_request::is_password_Valid() const{
    return m_password_isValid;
}

QString OAI_users_post_request::getPhone() const {
    return m_phone;
}
void OAI_users_post_request::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAI_users_post_request::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAI_users_post_request::is_phone_Valid() const{
    return m_phone_isValid;
}

QString OAI_users_post_request::getPhoneCountrycode() const {
    return m_phone_countrycode;
}
void OAI_users_post_request::setPhoneCountrycode(const QString &phone_countrycode) {
    m_phone_countrycode = phone_countrycode;
    m_phone_countrycode_isSet = true;
}

bool OAI_users_post_request::is_phone_countrycode_Set() const{
    return m_phone_countrycode_isSet;
}

bool OAI_users_post_request::is_phone_countrycode_Valid() const{
    return m_phone_countrycode_isValid;
}

bool OAI_users_post_request::isReceiveFormMails() const {
    return m_receive_form_mails;
}
void OAI_users_post_request::setReceiveFormMails(const bool &receive_form_mails) {
    m_receive_form_mails = receive_form_mails;
    m_receive_form_mails_isSet = true;
}

bool OAI_users_post_request::is_receive_form_mails_Set() const{
    return m_receive_form_mails_isSet;
}

bool OAI_users_post_request::is_receive_form_mails_Valid() const{
    return m_receive_form_mails_isValid;
}

OAI_contacts_post_request_contact_types OAI_users_post_request::getRoles() const {
    return m_roles;
}
void OAI_users_post_request::setRoles(const OAI_contacts_post_request_contact_types &roles) {
    m_roles = roles;
    m_roles_isSet = true;
}

bool OAI_users_post_request::is_roles_Set() const{
    return m_roles_isSet;
}

bool OAI_users_post_request::is_roles_Valid() const{
    return m_roles_isValid;
}

float OAI_users_post_request::getSalePrice() const {
    return m_sale_price;
}
void OAI_users_post_request::setSalePrice(const float &sale_price) {
    m_sale_price = sale_price;
    m_sale_price_isSet = true;
}

bool OAI_users_post_request::is_sale_price_Set() const{
    return m_sale_price_isSet;
}

bool OAI_users_post_request::is_sale_price_Valid() const{
    return m_sale_price_isValid;
}

QString OAI_users_post_request::getStreetName() const {
    return m_street_name;
}
void OAI_users_post_request::setStreetName(const QString &street_name) {
    m_street_name = street_name;
    m_street_name_isSet = true;
}

bool OAI_users_post_request::is_street_name_Set() const{
    return m_street_name_isSet;
}

bool OAI_users_post_request::is_street_name_Valid() const{
    return m_street_name_isValid;
}

bool OAI_users_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cost_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expected_billable_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extra_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hide_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hide_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_initials_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mobile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mobile_countrycode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_countrycode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_receive_form_mails_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_roles.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_sale_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_users_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_first_name_isValid && true;
}

} // namespace OpenAPI
