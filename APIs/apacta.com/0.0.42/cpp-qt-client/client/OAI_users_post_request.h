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

/*
 * OAI_users_post_request.h
 *
 * 
 */

#ifndef OAI_users_post_request_H
#define OAI_users_post_request_H

#include <QJsonObject>

#include "OAI_contacts_post_request_contact_types.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAI_contacts_post_request_contact_types;

class OAI_users_post_request : public OAIObject {
public:
    OAI_users_post_request();
    OAI_users_post_request(QString json);
    ~OAI_users_post_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCityId() const;
    void setCityId(const QString &city_id);
    bool is_city_id_Set() const;
    bool is_city_id_Valid() const;

    float getCostPrice() const;
    void setCostPrice(const float &cost_price);
    bool is_cost_price_Set() const;
    bool is_cost_price_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    float getExpectedBillableHours() const;
    void setExpectedBillableHours(const float &expected_billable_hours);
    bool is_expected_billable_hours_Set() const;
    bool is_expected_billable_hours_Valid() const;

    float getExtraPrice() const;
    void setExtraPrice(const float &extra_price);
    bool is_extra_price_Set() const;
    bool is_extra_price_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    bool isHideAddress() const;
    void setHideAddress(const bool &hide_address);
    bool is_hide_address_Set() const;
    bool is_hide_address_Valid() const;

    bool isHidePhone() const;
    void setHidePhone(const bool &hide_phone);
    bool is_hide_phone_Set() const;
    bool is_hide_phone_Valid() const;

    QString getInitials() const;
    void setInitials(const QString &initials);
    bool is_initials_Set() const;
    bool is_initials_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    QString getLanguageId() const;
    void setLanguageId(const QString &language_id);
    bool is_language_id_Set() const;
    bool is_language_id_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QString getMobile() const;
    void setMobile(const QString &mobile);
    bool is_mobile_Set() const;
    bool is_mobile_Valid() const;

    QString getMobileCountrycode() const;
    void setMobileCountrycode(const QString &mobile_countrycode);
    bool is_mobile_countrycode_Set() const;
    bool is_mobile_countrycode_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getPhone() const;
    void setPhone(const QString &phone);
    bool is_phone_Set() const;
    bool is_phone_Valid() const;

    QString getPhoneCountrycode() const;
    void setPhoneCountrycode(const QString &phone_countrycode);
    bool is_phone_countrycode_Set() const;
    bool is_phone_countrycode_Valid() const;

    bool isReceiveFormMails() const;
    void setReceiveFormMails(const bool &receive_form_mails);
    bool is_receive_form_mails_Set() const;
    bool is_receive_form_mails_Valid() const;

    OAI_contacts_post_request_contact_types getRoles() const;
    void setRoles(const OAI_contacts_post_request_contact_types &roles);
    bool is_roles_Set() const;
    bool is_roles_Valid() const;

    float getSalePrice() const;
    void setSalePrice(const float &sale_price);
    bool is_sale_price_Set() const;
    bool is_sale_price_Valid() const;

    QString getStreetName() const;
    void setStreetName(const QString &street_name);
    bool is_street_name_Set() const;
    bool is_street_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_city_id;
    bool m_city_id_isSet;
    bool m_city_id_isValid;

    float m_cost_price;
    bool m_cost_price_isSet;
    bool m_cost_price_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    float m_expected_billable_hours;
    bool m_expected_billable_hours_isSet;
    bool m_expected_billable_hours_isValid;

    float m_extra_price;
    bool m_extra_price_isSet;
    bool m_extra_price_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    bool m_hide_address;
    bool m_hide_address_isSet;
    bool m_hide_address_isValid;

    bool m_hide_phone;
    bool m_hide_phone_isSet;
    bool m_hide_phone_isValid;

    QString m_initials;
    bool m_initials_isSet;
    bool m_initials_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    QString m_language_id;
    bool m_language_id_isSet;
    bool m_language_id_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QString m_mobile;
    bool m_mobile_isSet;
    bool m_mobile_isValid;

    QString m_mobile_countrycode;
    bool m_mobile_countrycode_isSet;
    bool m_mobile_countrycode_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_phone;
    bool m_phone_isSet;
    bool m_phone_isValid;

    QString m_phone_countrycode;
    bool m_phone_countrycode_isSet;
    bool m_phone_countrycode_isValid;

    bool m_receive_form_mails;
    bool m_receive_form_mails_isSet;
    bool m_receive_form_mails_isValid;

    OAI_contacts_post_request_contact_types m_roles;
    bool m_roles_isSet;
    bool m_roles_isValid;

    float m_sale_price;
    bool m_sale_price_isSet;
    bool m_sale_price_isValid;

    QString m_street_name;
    bool m_street_name_isSet;
    bool m_street_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_users_post_request)

#endif // OAI_users_post_request_H
