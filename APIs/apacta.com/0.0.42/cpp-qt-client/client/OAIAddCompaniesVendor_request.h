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
 * OAIAddCompaniesVendor_request.h
 *
 * 
 */

#ifndef OAIAddCompaniesVendor_request_H
#define OAIAddCompaniesVendor_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAddCompaniesVendor_request : public OAIObject {
public:
    OAIAddCompaniesVendor_request();
    OAIAddCompaniesVendor_request(QString json);
    ~OAIAddCompaniesVendor_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCompanyId() const;
    void setCompanyId(const QString &company_id);
    bool is_company_id_Set() const;
    bool is_company_id_Valid() const;

    float getDeliveryPrice() const;
    void setDeliveryPrice(const float &delivery_price);
    bool is_delivery_price_Set() const;
    bool is_delivery_price_Valid() const;

    float getFreeDeliveryPrice() const;
    void setFreeDeliveryPrice(const float &free_delivery_price);
    bool is_free_delivery_price_Set() const;
    bool is_free_delivery_price_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    bool isReceiveAutomaticPriceFiles() const;
    void setReceiveAutomaticPriceFiles(const bool &receive_automatic_price_files);
    bool is_receive_automatic_price_files_Set() const;
    bool is_receive_automatic_price_files_Valid() const;

    bool isReceiveInvoiceMails() const;
    void setReceiveInvoiceMails(const bool &receive_invoice_mails);
    bool is_receive_invoice_mails_Set() const;
    bool is_receive_invoice_mails_Valid() const;

    bool isReviewed() const;
    void setReviewed(const bool &reviewed);
    bool is_reviewed_Set() const;
    bool is_reviewed_Valid() const;

    bool isUsePriceFiles() const;
    void setUsePriceFiles(const bool &use_price_files);
    bool is_use_price_files_Set() const;
    bool is_use_price_files_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    QString getVendorAccountReference() const;
    void setVendorAccountReference(const QString &vendor_account_reference);
    bool is_vendor_account_reference_Set() const;
    bool is_vendor_account_reference_Valid() const;

    QString getVendorDepartmentId() const;
    void setVendorDepartmentId(const QString &vendor_department_id);
    bool is_vendor_department_id_Set() const;
    bool is_vendor_department_id_Valid() const;

    QString getVendorEmail() const;
    void setVendorEmail(const QString &vendor_email);
    bool is_vendor_email_Set() const;
    bool is_vendor_email_Valid() const;

    QString getVendorId() const;
    void setVendorId(const QString &vendor_id);
    bool is_vendor_id_Set() const;
    bool is_vendor_id_Valid() const;

    QString getVendorName() const;
    void setVendorName(const QString &vendor_name);
    bool is_vendor_name_Set() const;
    bool is_vendor_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_company_id;
    bool m_company_id_isSet;
    bool m_company_id_isValid;

    float m_delivery_price;
    bool m_delivery_price_isSet;
    bool m_delivery_price_isValid;

    float m_free_delivery_price;
    bool m_free_delivery_price_isSet;
    bool m_free_delivery_price_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    bool m_receive_automatic_price_files;
    bool m_receive_automatic_price_files_isSet;
    bool m_receive_automatic_price_files_isValid;

    bool m_receive_invoice_mails;
    bool m_receive_invoice_mails_isSet;
    bool m_receive_invoice_mails_isValid;

    bool m_reviewed;
    bool m_reviewed_isSet;
    bool m_reviewed_isValid;

    bool m_use_price_files;
    bool m_use_price_files_isSet;
    bool m_use_price_files_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;

    QString m_vendor_account_reference;
    bool m_vendor_account_reference_isSet;
    bool m_vendor_account_reference_isValid;

    QString m_vendor_department_id;
    bool m_vendor_department_id_isSet;
    bool m_vendor_department_id_isValid;

    QString m_vendor_email;
    bool m_vendor_email_isSet;
    bool m_vendor_email_isValid;

    QString m_vendor_id;
    bool m_vendor_id_isSet;
    bool m_vendor_id_isValid;

    QString m_vendor_name;
    bool m_vendor_name_isSet;
    bool m_vendor_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddCompaniesVendor_request)

#endif // OAIAddCompaniesVendor_request_H
