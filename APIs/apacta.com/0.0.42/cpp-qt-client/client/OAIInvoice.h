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
 * OAIInvoice.h
 *
 * 
 */

#ifndef OAIInvoice_H
#define OAIInvoice_H

#include <QJsonObject>

#include <QDate>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInvoice : public OAIObject {
public:
    OAIInvoice();
    OAIInvoice(QString json);
    ~OAIInvoice() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllProductsOneLine() const;
    void setAllProductsOneLine(const bool &all_products_one_line);
    bool is_all_products_one_line_Set() const;
    bool is_all_products_one_line_Valid() const;

    bool isAllWorkingHoursOneLine() const;
    void setAllWorkingHoursOneLine(const bool &all_working_hours_one_line);
    bool is_all_working_hours_one_line_Set() const;
    bool is_all_working_hours_one_line_Valid() const;

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

    QString getCurrencyId() const;
    void setCurrencyId(const QString &currency_id);
    bool is_currency_id_Set() const;
    bool is_currency_id_Valid() const;

    QDate getDateFrom() const;
    void setDateFrom(const QDate &date_from);
    bool is_date_from_Set() const;
    bool is_date_from_Valid() const;

    QDate getDateTo() const;
    void setDateTo(const QDate &date_to);
    bool is_date_to_Set() const;
    bool is_date_to_Valid() const;

    QString getDeleted() const;
    void setDeleted(const QString &deleted);
    bool is_deleted_Set() const;
    bool is_deleted_Valid() const;

    QString getDownloaded() const;
    void setDownloaded(const QString &downloaded);
    bool is_downloaded_Set() const;
    bool is_downloaded_Valid() const;

    QString getErpId() const;
    void setErpId(const QString &erp_id);
    bool is_erp_id_Set() const;
    bool is_erp_id_Valid() const;

    QString getErpPaymentTermId() const;
    void setErpPaymentTermId(const QString &erp_payment_term_id);
    bool is_erp_payment_term_id_Set() const;
    bool is_erp_payment_term_id_Valid() const;

    bool isEuCustomer() const;
    void setEuCustomer(const bool &eu_customer);
    bool is_eu_customer_Set() const;
    bool is_eu_customer_Valid() const;

    float getGrossPayment() const;
    void setGrossPayment(const float &gross_payment);
    bool is_gross_payment_Set() const;
    bool is_gross_payment_Valid() const;

    bool isGroupByForms() const;
    void setGroupByForms(const bool &group_by_forms);
    bool is_group_by_forms_Set() const;
    bool is_group_by_forms_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIncludeInvoicedLines() const;
    void setIncludeInvoicedLines(const bool &include_invoiced_lines);
    bool is_include_invoiced_lines_Set() const;
    bool is_include_invoiced_lines_Valid() const;

    QString getIntegrationId() const;
    void setIntegrationId(const QString &integration_id);
    bool is_integration_id_Set() const;
    bool is_integration_id_Valid() const;

    qint32 getInvoiceNumber() const;
    void setInvoiceNumber(const qint32 &invoice_number);
    bool is_invoice_number_Set() const;
    bool is_invoice_number_Valid() const;

    bool isIsDraft() const;
    void setIsDraft(const bool &is_draft);
    bool is_is_draft_Set() const;
    bool is_is_draft_Valid() const;

    bool isIsFinalInvoice() const;
    void setIsFinalInvoice(const bool &is_final_invoice);
    bool is_is_final_invoice_Set() const;
    bool is_is_final_invoice_Valid() const;

    bool isIsLocked() const;
    void setIsLocked(const bool &is_locked);
    bool is_is_locked_Set() const;
    bool is_is_locked_Valid() const;

    bool isIsOffer() const;
    void setIsOffer(const bool &is_offer);
    bool is_is_offer_Set() const;
    bool is_is_offer_Valid() const;

    QDate getIssuedDate() const;
    void setIssuedDate(const QDate &issued_date);
    bool is_issued_date_Set() const;
    bool is_issued_date_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QString getModified() const;
    void setModified(const QString &modified);
    bool is_modified_Set() const;
    bool is_modified_Valid() const;

    float getNetPayment() const;
    void setNetPayment(const float &net_payment);
    bool is_net_payment_Set() const;
    bool is_net_payment_Valid() const;

    qint32 getOfferNumber() const;
    void setOfferNumber(const qint32 &offer_number);
    bool is_offer_number_Set() const;
    bool is_offer_number_Valid() const;

    QString getOrderLineGroupId() const;
    void setOrderLineGroupId(const QString &order_line_group_id);
    bool is_order_line_group_id_Set() const;
    bool is_order_line_group_id_Valid() const;

    QDate getPaymentDueDate() const;
    void setPaymentDueDate(const QDate &payment_due_date);
    bool is_payment_due_date_Set() const;
    bool is_payment_due_date_Valid() const;

    QString getPaymentTermId() const;
    void setPaymentTermId(const QString &payment_term_id);
    bool is_payment_term_id_Set() const;
    bool is_payment_term_id_Valid() const;

    QString getProjectId() const;
    void setProjectId(const QString &project_id);
    bool is_project_id_Set() const;
    bool is_project_id_Valid() const;

    bool isProjectOverviewAttached() const;
    void setProjectOverviewAttached(const bool &project_overview_attached);
    bool is_project_overview_attached_Set() const;
    bool is_project_overview_attached_Valid() const;

    QString getReference() const;
    void setReference(const QString &reference);
    bool is_reference_Set() const;
    bool is_reference_Valid() const;

    bool isShowEmployeeName() const;
    void setShowEmployeeName(const bool &show_employee_name);
    bool is_show_employee_name_Set() const;
    bool is_show_employee_name_Valid() const;

    bool isShowPriceProductBundle() const;
    void setShowPriceProductBundle(const bool &show_price_product_bundle);
    bool is_show_price_product_bundle_Set() const;
    bool is_show_price_product_bundle_Valid() const;

    bool isShowPricesProductsAndHours() const;
    void setShowPricesProductsAndHours(const bool &show_prices_products_and_hours);
    bool is_show_prices_products_and_hours_Set() const;
    bool is_show_prices_products_and_hours_Valid() const;

    bool isShowProductImages() const;
    void setShowProductImages(const bool &show_product_images);
    bool is_show_product_images_Set() const;
    bool is_show_product_images_Valid() const;

    bool isShowProductsProductBundle() const;
    void setShowProductsProductBundle(const bool &show_products_product_bundle);
    bool is_show_products_product_bundle_Set() const;
    bool is_show_products_product_bundle_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    float getTotalCostPrice() const;
    void setTotalCostPrice(const float &total_cost_price);
    bool is_total_cost_price_Set() const;
    bool is_total_cost_price_Valid() const;

    float getTotalDiscountPercent() const;
    void setTotalDiscountPercent(const float &total_discount_percent);
    bool is_total_discount_percent_Set() const;
    bool is_total_discount_percent_Valid() const;

    qint32 getVatPercent() const;
    void setVatPercent(const qint32 &vat_percent);
    bool is_vat_percent_Set() const;
    bool is_vat_percent_Valid() const;

    QString getVendorId() const;
    void setVendorId(const QString &vendor_id);
    bool is_vendor_id_Set() const;
    bool is_vendor_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_all_products_one_line;
    bool m_all_products_one_line_isSet;
    bool m_all_products_one_line_isValid;

    bool m_all_working_hours_one_line;
    bool m_all_working_hours_one_line_isSet;
    bool m_all_working_hours_one_line_isValid;

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

    QString m_currency_id;
    bool m_currency_id_isSet;
    bool m_currency_id_isValid;

    QDate m_date_from;
    bool m_date_from_isSet;
    bool m_date_from_isValid;

    QDate m_date_to;
    bool m_date_to_isSet;
    bool m_date_to_isValid;

    QString m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    QString m_downloaded;
    bool m_downloaded_isSet;
    bool m_downloaded_isValid;

    QString m_erp_id;
    bool m_erp_id_isSet;
    bool m_erp_id_isValid;

    QString m_erp_payment_term_id;
    bool m_erp_payment_term_id_isSet;
    bool m_erp_payment_term_id_isValid;

    bool m_eu_customer;
    bool m_eu_customer_isSet;
    bool m_eu_customer_isValid;

    float m_gross_payment;
    bool m_gross_payment_isSet;
    bool m_gross_payment_isValid;

    bool m_group_by_forms;
    bool m_group_by_forms_isSet;
    bool m_group_by_forms_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_include_invoiced_lines;
    bool m_include_invoiced_lines_isSet;
    bool m_include_invoiced_lines_isValid;

    QString m_integration_id;
    bool m_integration_id_isSet;
    bool m_integration_id_isValid;

    qint32 m_invoice_number;
    bool m_invoice_number_isSet;
    bool m_invoice_number_isValid;

    bool m_is_draft;
    bool m_is_draft_isSet;
    bool m_is_draft_isValid;

    bool m_is_final_invoice;
    bool m_is_final_invoice_isSet;
    bool m_is_final_invoice_isValid;

    bool m_is_locked;
    bool m_is_locked_isSet;
    bool m_is_locked_isValid;

    bool m_is_offer;
    bool m_is_offer_isSet;
    bool m_is_offer_isValid;

    QDate m_issued_date;
    bool m_issued_date_isSet;
    bool m_issued_date_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QString m_modified;
    bool m_modified_isSet;
    bool m_modified_isValid;

    float m_net_payment;
    bool m_net_payment_isSet;
    bool m_net_payment_isValid;

    qint32 m_offer_number;
    bool m_offer_number_isSet;
    bool m_offer_number_isValid;

    QString m_order_line_group_id;
    bool m_order_line_group_id_isSet;
    bool m_order_line_group_id_isValid;

    QDate m_payment_due_date;
    bool m_payment_due_date_isSet;
    bool m_payment_due_date_isValid;

    QString m_payment_term_id;
    bool m_payment_term_id_isSet;
    bool m_payment_term_id_isValid;

    QString m_project_id;
    bool m_project_id_isSet;
    bool m_project_id_isValid;

    bool m_project_overview_attached;
    bool m_project_overview_attached_isSet;
    bool m_project_overview_attached_isValid;

    QString m_reference;
    bool m_reference_isSet;
    bool m_reference_isValid;

    bool m_show_employee_name;
    bool m_show_employee_name_isSet;
    bool m_show_employee_name_isValid;

    bool m_show_price_product_bundle;
    bool m_show_price_product_bundle_isSet;
    bool m_show_price_product_bundle_isValid;

    bool m_show_prices_products_and_hours;
    bool m_show_prices_products_and_hours_isSet;
    bool m_show_prices_products_and_hours_isValid;

    bool m_show_product_images;
    bool m_show_product_images_isSet;
    bool m_show_product_images_isValid;

    bool m_show_products_product_bundle;
    bool m_show_products_product_bundle_isSet;
    bool m_show_products_product_bundle_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    float m_total_cost_price;
    bool m_total_cost_price_isSet;
    bool m_total_cost_price_isValid;

    float m_total_discount_percent;
    bool m_total_discount_percent_isSet;
    bool m_total_discount_percent_isValid;

    qint32 m_vat_percent;
    bool m_vat_percent_isSet;
    bool m_vat_percent_isValid;

    QString m_vendor_id;
    bool m_vendor_id_isSet;
    bool m_vendor_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInvoice)

#endif // OAIInvoice_H
