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
 * OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data.h
 *
 * 
 */

#ifndef OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data_H
#define OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data : public OAIObject {
public:
    OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data();
    OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data(QString json);
    ~OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCompaniesVendorId() const;
    void setCompaniesVendorId(const QString &companies_vendor_id);
    bool is_companies_vendor_id_Set() const;
    bool is_companies_vendor_id_Valid() const;

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

    QString getDir() const;
    void setDir(const QString &dir);
    bool is_dir_Set() const;
    bool is_dir_Valid() const;

    QString getFile() const;
    void setFile(const QString &file);
    bool is_file_Set() const;
    bool is_file_Valid() const;

    bool isFinished() const;
    void setFinished(const bool &finished);
    bool is_finished_Set() const;
    bool is_finished_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getModified() const;
    void setModified(const QString &modified);
    bool is_modified_Set() const;
    bool is_modified_Valid() const;

    QString getOriginalFileName() const;
    void setOriginalFileName(const QString &original_file_name);
    bool is_original_file_name_Set() const;
    bool is_original_file_name_Valid() const;

    qint32 getProgress() const;
    void setProgress(const qint32 &progress);
    bool is_progress_Set() const;
    bool is_progress_Valid() const;

    qint32 getSize() const;
    void setSize(const qint32 &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    qint32 getVendorProductsCount() const;
    void setVendorProductsCount(const qint32 &vendor_products_count);
    bool is_vendor_products_count_Set() const;
    bool is_vendor_products_count_Valid() const;

    qint32 getVendorProductsCountTotal() const;
    void setVendorProductsCountTotal(const qint32 &vendor_products_count_total);
    bool is_vendor_products_count_total_Set() const;
    bool is_vendor_products_count_total_Valid() const;

    QString getDownloadLink() const;
    void setDownloadLink(const QString &download_link);
    bool is_download_link_Set() const;
    bool is_download_link_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_companies_vendor_id;
    bool m_companies_vendor_id_isSet;
    bool m_companies_vendor_id_isValid;

    QString m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    QString m_created_by_id;
    bool m_created_by_id_isSet;
    bool m_created_by_id_isValid;

    QString m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    QString m_dir;
    bool m_dir_isSet;
    bool m_dir_isValid;

    QString m_file;
    bool m_file_isSet;
    bool m_file_isValid;

    bool m_finished;
    bool m_finished_isSet;
    bool m_finished_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_modified;
    bool m_modified_isSet;
    bool m_modified_isValid;

    QString m_original_file_name;
    bool m_original_file_name_isSet;
    bool m_original_file_name_isValid;

    qint32 m_progress;
    bool m_progress_isSet;
    bool m_progress_isValid;

    qint32 m_size;
    bool m_size_isSet;
    bool m_size_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    qint32 m_vendor_products_count;
    bool m_vendor_products_count_isSet;
    bool m_vendor_products_count_isValid;

    qint32 m_vendor_products_count_total;
    bool m_vendor_products_count_total_isSet;
    bool m_vendor_products_count_total_isValid;

    QString m_download_link;
    bool m_download_link_isSet;
    bool m_download_link_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data)

#endif // OAI_vendor_product_price_files__vendor_product_price_file_id__get_200_response_data_H
