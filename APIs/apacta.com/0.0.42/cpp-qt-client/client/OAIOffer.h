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
 * OAIOffer.h
 *
 * 
 */

#ifndef OAIOffer_H
#define OAIOffer_H

#include <QJsonObject>

#include <QDate>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOffer : public OAIObject {
public:
    OAIOffer();
    OAIOffer(QString json);
    ~OAIOffer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddress() const;
    void setAddress(const QString &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    bool isAllLinesOneLine() const;
    void setAllLinesOneLine(const bool &all_lines_one_line);
    bool is_all_lines_one_line_Set() const;
    bool is_all_lines_one_line_Valid() const;

    bool isAllProductsOneLine() const;
    void setAllProductsOneLine(const bool &all_products_one_line);
    bool is_all_products_one_line_Set() const;
    bool is_all_products_one_line_Valid() const;

    bool isAllWorkingHoursOneLine() const;
    void setAllWorkingHoursOneLine(const bool &all_working_hours_one_line);
    bool is_all_working_hours_one_line_Set() const;
    bool is_all_working_hours_one_line_Valid() const;

    QString getCityId() const;
    void setCityId(const QString &city_id);
    bool is_city_id_Set() const;
    bool is_city_id_Valid() const;

    QString getCompanyId() const;
    void setCompanyId(const QString &company_id);
    bool is_company_id_Set() const;
    bool is_company_id_Valid() const;

    QString getContactId() const;
    void setContactId(const QString &contact_id);
    bool is_contact_id_Set() const;
    bool is_contact_id_Valid() const;

    QString getCreated() const;
    void setCreated(const QString &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    QString getCreatedById() const;
    void setCreatedById(const QString &created_by_id);
    bool is_created_by_id_Set() const;
    bool is_created_by_id_Valid() const;

    QString getDeleted() const;
    void setDeleted(const QString &deleted);
    bool is_deleted_Set() const;
    bool is_deleted_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    qint32 getDiscountPercent() const;
    void setDiscountPercent(const qint32 &discount_percent);
    bool is_discount_percent_Set() const;
    bool is_discount_percent_Valid() const;

    QString getErpPaymentTermId() const;
    void setErpPaymentTermId(const QString &erp_payment_term_id);
    bool is_erp_payment_term_id_Set() const;
    bool is_erp_payment_term_id_Valid() const;

    QString getExpiratonDate() const;
    void setExpiratonDate(const QString &expiraton_date);
    bool is_expiraton_date_Set() const;
    bool is_expiraton_date_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QDate getIssueDate() const;
    void setIssueDate(const QDate &issue_date);
    bool is_issue_date_Set() const;
    bool is_issue_date_Valid() const;

    QString getModified() const;
    void setModified(const QString &modified);
    bool is_modified_Set() const;
    bool is_modified_Valid() const;

    QString getModifiedById() const;
    void setModifiedById(const QString &modified_by_id);
    bool is_modified_by_id_Set() const;
    bool is_modified_by_id_Valid() const;

    qint32 getOfferNumber() const;
    void setOfferNumber(const qint32 &offer_number);
    bool is_offer_number_Set() const;
    bool is_offer_number_Valid() const;

    QString getOfferStatusId() const;
    void setOfferStatusId(const QString &offer_status_id);
    bool is_offer_status_id_Set() const;
    bool is_offer_status_id_Valid() const;

    QString getPaymentTermId() const;
    void setPaymentTermId(const QString &payment_term_id);
    bool is_payment_term_id_Set() const;
    bool is_payment_term_id_Valid() const;

    QString getRejectionReason() const;
    void setRejectionReason(const QString &rejection_reason);
    bool is_rejection_reason_Set() const;
    bool is_rejection_reason_Valid() const;

    QString getSenderId() const;
    void setSenderId(const QString &sender_id);
    bool is_sender_id_Set() const;
    bool is_sender_id_Valid() const;

    bool isShowEmployeeName() const;
    void setShowEmployeeName(const bool &show_employee_name);
    bool is_show_employee_name_Set() const;
    bool is_show_employee_name_Valid() const;

    bool isShowOfferLines() const;
    void setShowOfferLines(const bool &show_offer_lines);
    bool is_show_offer_lines_Set() const;
    bool is_show_offer_lines_Valid() const;

    bool isShowPaymentTerm() const;
    void setShowPaymentTerm(const bool &show_payment_term);
    bool is_show_payment_term_Set() const;
    bool is_show_payment_term_Valid() const;

    bool isShowPrices() const;
    void setShowPrices(const bool &show_prices);
    bool is_show_prices_Set() const;
    bool is_show_prices_Valid() const;

    bool isShowProductImages() const;
    void setShowProductImages(const bool &show_product_images);
    bool is_show_product_images_Set() const;
    bool is_show_product_images_Valid() const;

    bool isShowProductsProductBundle() const;
    void setShowProductsProductBundle(const bool &show_products_product_bundle);
    bool is_show_products_product_bundle_Set() const;
    bool is_show_products_product_bundle_Valid() const;

    QString getSlug() const;
    void setSlug(const QString &slug);
    bool is_slug_Set() const;
    bool is_slug_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    qint32 getVatPercent() const;
    void setVatPercent(const qint32 &vat_percent);
    bool is_vat_percent_Set() const;
    bool is_vat_percent_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    bool m_all_lines_one_line;
    bool m_all_lines_one_line_isSet;
    bool m_all_lines_one_line_isValid;

    bool m_all_products_one_line;
    bool m_all_products_one_line_isSet;
    bool m_all_products_one_line_isValid;

    bool m_all_working_hours_one_line;
    bool m_all_working_hours_one_line_isSet;
    bool m_all_working_hours_one_line_isValid;

    QString m_city_id;
    bool m_city_id_isSet;
    bool m_city_id_isValid;

    QString m_company_id;
    bool m_company_id_isSet;
    bool m_company_id_isValid;

    QString m_contact_id;
    bool m_contact_id_isSet;
    bool m_contact_id_isValid;

    QString m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    QString m_created_by_id;
    bool m_created_by_id_isSet;
    bool m_created_by_id_isValid;

    QString m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    qint32 m_discount_percent;
    bool m_discount_percent_isSet;
    bool m_discount_percent_isValid;

    QString m_erp_payment_term_id;
    bool m_erp_payment_term_id_isSet;
    bool m_erp_payment_term_id_isValid;

    QString m_expiraton_date;
    bool m_expiraton_date_isSet;
    bool m_expiraton_date_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QDate m_issue_date;
    bool m_issue_date_isSet;
    bool m_issue_date_isValid;

    QString m_modified;
    bool m_modified_isSet;
    bool m_modified_isValid;

    QString m_modified_by_id;
    bool m_modified_by_id_isSet;
    bool m_modified_by_id_isValid;

    qint32 m_offer_number;
    bool m_offer_number_isSet;
    bool m_offer_number_isValid;

    QString m_offer_status_id;
    bool m_offer_status_id_isSet;
    bool m_offer_status_id_isValid;

    QString m_payment_term_id;
    bool m_payment_term_id_isSet;
    bool m_payment_term_id_isValid;

    QString m_rejection_reason;
    bool m_rejection_reason_isSet;
    bool m_rejection_reason_isValid;

    QString m_sender_id;
    bool m_sender_id_isSet;
    bool m_sender_id_isValid;

    bool m_show_employee_name;
    bool m_show_employee_name_isSet;
    bool m_show_employee_name_isValid;

    bool m_show_offer_lines;
    bool m_show_offer_lines_isSet;
    bool m_show_offer_lines_isValid;

    bool m_show_payment_term;
    bool m_show_payment_term_isSet;
    bool m_show_payment_term_isValid;

    bool m_show_prices;
    bool m_show_prices_isSet;
    bool m_show_prices_isValid;

    bool m_show_product_images;
    bool m_show_product_images_isSet;
    bool m_show_product_images_isValid;

    bool m_show_products_product_bundle;
    bool m_show_products_product_bundle_isSet;
    bool m_show_products_product_bundle_isValid;

    QString m_slug;
    bool m_slug_isSet;
    bool m_slug_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    qint32 m_vat_percent;
    bool m_vat_percent_isSet;
    bool m_vat_percent_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOffer)

#endif // OAIOffer_H
