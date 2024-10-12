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
 * OAIProject.h
 *
 * 
 */

#ifndef OAIProject_H
#define OAIProject_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProject : public OAIObject {
public:
    OAIProject();
    OAIProject(QString json);
    ~OAIProject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

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

    QString getEndTime() const;
    void setEndTime(const QString &end_time);
    bool is_end_time_Set() const;
    bool is_end_time_Valid() const;

    QString getErpProjectId() const;
    void setErpProjectId(const QString &erp_project_id);
    bool is_erp_project_id_Set() const;
    bool is_erp_project_id_Valid() const;

    QString getErpTaskId() const;
    void setErpTaskId(const QString &erp_task_id);
    bool is_erp_task_id_Set() const;
    bool is_erp_task_id_Valid() const;

    QString getFullName() const;
    void setFullName(const QString &full_name);
    bool is_full_name_Set() const;
    bool is_full_name_Valid() const;

    bool isHasFinalInvoice() const;
    void setHasFinalInvoice(const bool &has_final_invoice);
    bool is_has_final_invoice_Set() const;
    bool is_has_final_invoice_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsFixedPrice() const;
    void setIsFixedPrice(const bool &is_fixed_price);
    bool is_is_fixed_price_Set() const;
    bool is_is_fixed_price_Valid() const;

    bool getIsOffer() const;
    void setIsOffer(const bool &is_offer);
    bool is_is_offer_Set() const;
    bool is_is_offer_Valid() const;

    QString getIsRotten() const;
    void setIsRotten(const QString &is_rotten);
    bool is_is_rotten_Set() const;
    bool is_is_rotten_Valid() const;

    QString getLatitude() const;
    void setLatitude(const QString &latitude);
    bool is_latitude_Set() const;
    bool is_latitude_Valid() const;

    QString getLongitude() const;
    void setLongitude(const QString &longitude);
    bool is_longitude_Set() const;
    bool is_longitude_Valid() const;

    QString getModified() const;
    void setModified(const QString &modified);
    bool is_modified_Set() const;
    bool is_modified_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    float getNotInvoicedAmount() const;
    void setNotInvoicedAmount(const float &not_invoiced_amount);
    bool is_not_invoiced_amount_Set() const;
    bool is_not_invoiced_amount_Valid() const;

    QString getOfferId() const;
    void setOfferId(const QString &offer_id);
    bool is_offer_id_Set() const;
    bool is_offer_id_Valid() const;

    QString getParentId() const;
    void setParentId(const QString &parent_id);
    bool is_parent_id_Set() const;
    bool is_parent_id_Valid() const;

    QString getPreCalculationId() const;
    void setPreCalculationId(const QString &pre_calculation_id);
    bool is_pre_calculation_id_Set() const;
    bool is_pre_calculation_id_Valid() const;

    float getProductsTotalCostPrice() const;
    void setProductsTotalCostPrice(const float &products_total_cost_price);
    bool is_products_total_cost_price_Set() const;
    bool is_products_total_cost_price_Valid() const;

    QString getProjectImageUrl() const;
    void setProjectImageUrl(const QString &project_image_url);
    bool is_project_image_url_Set() const;
    bool is_project_image_url_Valid() const;

    double getProjectNumber() const;
    void setProjectNumber(const double &project_number);
    bool is_project_number_Set() const;
    bool is_project_number_Valid() const;

    QString getProjectStatusId() const;
    void setProjectStatusId(const QString &project_status_id);
    bool is_project_status_id_Set() const;
    bool is_project_status_id_Valid() const;

    QString getSharedProjectId() const;
    void setSharedProjectId(const QString &shared_project_id);
    bool is_shared_project_id_Set() const;
    bool is_shared_project_id_Valid() const;

    QString getStartTime() const;
    void setStartTime(const QString &start_time);
    bool is_start_time_Set() const;
    bool is_start_time_Valid() const;

    QString getStreetName() const;
    void setStreetName(const QString &street_name);
    bool is_street_name_Set() const;
    bool is_street_name_Valid() const;

    QString getThumbnail() const;
    void setThumbnail(const QString &thumbnail);
    bool is_thumbnail_Set() const;
    bool is_thumbnail_Valid() const;

    float getTotalSalesPrice() const;
    void setTotalSalesPrice(const float &total_sales_price);
    bool is_total_sales_price_Set() const;
    bool is_total_sales_price_Valid() const;

    float getWorkingHoursTotalCostPrice() const;
    void setWorkingHoursTotalCostPrice(const float &working_hours_total_cost_price);
    bool is_working_hours_total_cost_price_Set() const;
    bool is_working_hours_total_cost_price_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

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

    QString m_end_time;
    bool m_end_time_isSet;
    bool m_end_time_isValid;

    QString m_erp_project_id;
    bool m_erp_project_id_isSet;
    bool m_erp_project_id_isValid;

    QString m_erp_task_id;
    bool m_erp_task_id_isSet;
    bool m_erp_task_id_isValid;

    QString m_full_name;
    bool m_full_name_isSet;
    bool m_full_name_isValid;

    bool m_has_final_invoice;
    bool m_has_final_invoice_isSet;
    bool m_has_final_invoice_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_fixed_price;
    bool m_is_fixed_price_isSet;
    bool m_is_fixed_price_isValid;

    bool m_is_offer;
    bool m_is_offer_isSet;
    bool m_is_offer_isValid;

    QString m_is_rotten;
    bool m_is_rotten_isSet;
    bool m_is_rotten_isValid;

    QString m_latitude;
    bool m_latitude_isSet;
    bool m_latitude_isValid;

    QString m_longitude;
    bool m_longitude_isSet;
    bool m_longitude_isValid;

    QString m_modified;
    bool m_modified_isSet;
    bool m_modified_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    float m_not_invoiced_amount;
    bool m_not_invoiced_amount_isSet;
    bool m_not_invoiced_amount_isValid;

    QString m_offer_id;
    bool m_offer_id_isSet;
    bool m_offer_id_isValid;

    QString m_parent_id;
    bool m_parent_id_isSet;
    bool m_parent_id_isValid;

    QString m_pre_calculation_id;
    bool m_pre_calculation_id_isSet;
    bool m_pre_calculation_id_isValid;

    float m_products_total_cost_price;
    bool m_products_total_cost_price_isSet;
    bool m_products_total_cost_price_isValid;

    QString m_project_image_url;
    bool m_project_image_url_isSet;
    bool m_project_image_url_isValid;

    double m_project_number;
    bool m_project_number_isSet;
    bool m_project_number_isValid;

    QString m_project_status_id;
    bool m_project_status_id_isSet;
    bool m_project_status_id_isValid;

    QString m_shared_project_id;
    bool m_shared_project_id_isSet;
    bool m_shared_project_id_isValid;

    QString m_start_time;
    bool m_start_time_isSet;
    bool m_start_time_isValid;

    QString m_street_name;
    bool m_street_name_isSet;
    bool m_street_name_isValid;

    QString m_thumbnail;
    bool m_thumbnail_isSet;
    bool m_thumbnail_isValid;

    float m_total_sales_price;
    bool m_total_sales_price_isSet;
    bool m_total_sales_price_isValid;

    float m_working_hours_total_cost_price;
    bool m_working_hours_total_cost_price_isSet;
    bool m_working_hours_total_cost_price_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProject)

#endif // OAIProject_H
