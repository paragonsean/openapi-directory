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
 * OAICompany.h
 *
 * 
 */

#ifndef OAICompany_H
#define OAICompany_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICompany : public OAIObject {
public:
    OAICompany();
    OAICompany(QString json);
    ~OAICompany() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCityId() const;
    void setCityId(const QString &city_id);
    bool is_city_id_Set() const;
    bool is_city_id_Valid() const;

    QString getContactPersonId() const;
    void setContactPersonId(const QString &contact_person_id);
    bool is_contact_person_id_Set() const;
    bool is_contact_person_id_Valid() const;

    QString getCountryId() const;
    void setCountryId(const QString &country_id);
    bool is_country_id_Set() const;
    bool is_country_id_Valid() const;

    QString getCreated() const;
    void setCreated(const QString &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    QString getCreatedById() const;
    void setCreatedById(const QString &created_by_id);
    bool is_created_by_id_Set() const;
    bool is_created_by_id_Valid() const;

    QString getCvr() const;
    void setCvr(const QString &cvr);
    bool is_cvr_Set() const;
    bool is_cvr_Valid() const;

    QString getDeleted() const;
    void setDeleted(const QString &deleted);
    bool is_deleted_Set() const;
    bool is_deleted_Valid() const;

    QDateTime getExpired() const;
    void setExpired(const QDateTime &expired);
    bool is_expired_Set() const;
    bool is_expired_Valid() const;

    QString getFileId() const;
    void setFileId(const QString &file_id);
    bool is_file_id_Set() const;
    bool is_file_id_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getInvoiceEmail() const;
    void setInvoiceEmail(const QString &invoice_email);
    bool is_invoice_email_Set() const;
    bool is_invoice_email_Valid() const;

    QString getLanguageId() const;
    void setLanguageId(const QString &language_id);
    bool is_language_id_Set() const;
    bool is_language_id_Valid() const;

    QString getModified() const;
    void setModified(const QString &modified);
    bool is_modified_Set() const;
    bool is_modified_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNextInvoiceNumber() const;
    void setNextInvoiceNumber(const qint32 &next_invoice_number);
    bool is_next_invoice_number_Set() const;
    bool is_next_invoice_number_Valid() const;

    qint32 getNextOfferNumber() const;
    void setNextOfferNumber(const qint32 &next_offer_number);
    bool is_next_offer_number_Set() const;
    bool is_next_offer_number_Valid() const;

    qint32 getNextProjectNumber() const;
    void setNextProjectNumber(const qint32 &next_project_number);
    bool is_next_project_number_Set() const;
    bool is_next_project_number_Valid() const;

    QString getPhone() const;
    void setPhone(const QString &phone);
    bool is_phone_Set() const;
    bool is_phone_Valid() const;

    QString getPhoneCountrycode() const;
    void setPhoneCountrycode(const QString &phone_countrycode);
    bool is_phone_countrycode_Set() const;
    bool is_phone_countrycode_Valid() const;

    QString getReceiveFormMails() const;
    void setReceiveFormMails(const QString &receive_form_mails);
    bool is_receive_form_mails_Set() const;
    bool is_receive_form_mails_Valid() const;

    QString getStreetName() const;
    void setStreetName(const QString &street_name);
    bool is_street_name_Set() const;
    bool is_street_name_Valid() const;

    qint32 getVatPercent() const;
    void setVatPercent(const qint32 &vat_percent);
    bool is_vat_percent_Set() const;
    bool is_vat_percent_Valid() const;

    QString getWebsite() const;
    void setWebsite(const QString &website);
    bool is_website_Set() const;
    bool is_website_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_city_id;
    bool m_city_id_isSet;
    bool m_city_id_isValid;

    QString m_contact_person_id;
    bool m_contact_person_id_isSet;
    bool m_contact_person_id_isValid;

    QString m_country_id;
    bool m_country_id_isSet;
    bool m_country_id_isValid;

    QString m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    QString m_created_by_id;
    bool m_created_by_id_isSet;
    bool m_created_by_id_isValid;

    QString m_cvr;
    bool m_cvr_isSet;
    bool m_cvr_isValid;

    QString m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    QDateTime m_expired;
    bool m_expired_isSet;
    bool m_expired_isValid;

    QString m_file_id;
    bool m_file_id_isSet;
    bool m_file_id_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_invoice_email;
    bool m_invoice_email_isSet;
    bool m_invoice_email_isValid;

    QString m_language_id;
    bool m_language_id_isSet;
    bool m_language_id_isValid;

    QString m_modified;
    bool m_modified_isSet;
    bool m_modified_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_next_invoice_number;
    bool m_next_invoice_number_isSet;
    bool m_next_invoice_number_isValid;

    qint32 m_next_offer_number;
    bool m_next_offer_number_isSet;
    bool m_next_offer_number_isValid;

    qint32 m_next_project_number;
    bool m_next_project_number_isSet;
    bool m_next_project_number_isValid;

    QString m_phone;
    bool m_phone_isSet;
    bool m_phone_isValid;

    QString m_phone_countrycode;
    bool m_phone_countrycode_isSet;
    bool m_phone_countrycode_isValid;

    QString m_receive_form_mails;
    bool m_receive_form_mails_isSet;
    bool m_receive_form_mails_isValid;

    QString m_street_name;
    bool m_street_name_isSet;
    bool m_street_name_isValid;

    qint32 m_vat_percent;
    bool m_vat_percent_isSet;
    bool m_vat_percent_isValid;

    QString m_website;
    bool m_website_isSet;
    bool m_website_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICompany)

#endif // OAICompany_H
