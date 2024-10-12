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

#ifndef OAI_OAIInvoicesApi_H
#define OAI_OAIInvoicesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBadRequestResponse.h"
#include "OAIBulkActionRequestBody.h"
#include "OAICreateSuccessResponse.h"
#include "OAIEmptySuccessResponse.h"
#include "OAIErrorNotFound.h"
#include "OAIErrorValidation.h"
#include "OAI_clocking_records__clocking_record_id__put_200_response.h"
#include "OAI_clocking_records_post_201_response.h"
#include "OAI_integrations_productsSync_get_200_response.h"
#include "OAI_invoices__invoice_id__get_200_response.h"
#include "OAI_invoices__invoice_id__put_request.h"
#include "OAI_invoices_get_200_response.h"
#include "OAI_invoices_post_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIInvoicesApi : public QObject {
    Q_OBJECT

public:
    OAIInvoicesApi(const int timeOut = 0);
    ~OAIInvoicesApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  oai_bulk_action_request_body OAIBulkActionRequestBody [required]
    */
    virtual void bulkDeleteInvoices(const OAIBulkActionRequestBody &oai_bulk_action_request_body);

    /**
    * @param[in]  contact_id QString [optional]
    * @param[in]  project_id QString [optional]
    * @param[in]  invoice_number QString [optional]
    * @param[in]  offer_number QString [optional]
    * @param[in]  is_draft qint32 [optional]
    * @param[in]  is_offer qint32 [optional]
    * @param[in]  is_locked qint32 [optional]
    * @param[in]  is_fixed_price qint32 [optional]
    * @param[in]  date_from QDate [optional]
    * @param[in]  date_to QDate [optional]
    * @param[in]  issued_date QDate [optional]
    * @param[in]  sent_as_draft qint32 [optional]
    */
    virtual void invoicesGet(const ::OpenAPI::OptionalParam<QString> &contact_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &invoice_number = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &offer_number = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &is_draft = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &is_offer = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &is_locked = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &is_fixed_price = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QDate> &date_from = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &date_to = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &issued_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<qint32> &sent_as_draft = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  invoice_id QString [required]
    * @param[in]  project_id QString [optional]
    * @param[in]  contact_id QString [optional]
    */
    virtual void invoicesInvoiceIdCopyPost(const QString &invoice_id, const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &contact_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  invoice_id QString [required]
    */
    virtual void invoicesInvoiceIdDelete(const QString &invoice_id);

    /**
    * @param[in]  invoice_id QString [required]
    */
    virtual void invoicesInvoiceIdGet(const QString &invoice_id);

    /**
    * @param[in]  invoice_id QString [required]
    */
    virtual void invoicesInvoiceIdLinkProjectPdfPost(const QString &invoice_id);

    /**
    * @param[in]  invoice_id QString [required]
    * @param[in]  oai_invoices__invoice_id__put_request OAI_invoices__invoice_id__put_request [optional]
    */
    virtual void invoicesInvoiceIdPut(const QString &invoice_id, const ::OpenAPI::OptionalParam<OAI_invoices__invoice_id__put_request> &oai_invoices__invoice_id__put_request = ::OpenAPI::OptionalParam<OAI_invoices__invoice_id__put_request>());

    /**
    * @param[in]  invoice_id QString [required]
    */
    virtual void invoicesInvoiceIdUnlinkProjectPdfPost(const QString &invoice_id);

    /**
    * @param[in]  oai_invoices_post_request OAI_invoices_post_request [optional]
    */
    virtual void invoicesPost(const ::OpenAPI::OptionalParam<OAI_invoices_post_request> &oai_invoices_post_request = ::OpenAPI::OptionalParam<OAI_invoices_post_request>());


    virtual void invoicesVatOptionsGet();


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void bulkDeleteInvoicesCallback(OAIHttpRequestWorker *worker);
    void invoicesGetCallback(OAIHttpRequestWorker *worker);
    void invoicesInvoiceIdCopyPostCallback(OAIHttpRequestWorker *worker);
    void invoicesInvoiceIdDeleteCallback(OAIHttpRequestWorker *worker);
    void invoicesInvoiceIdGetCallback(OAIHttpRequestWorker *worker);
    void invoicesInvoiceIdLinkProjectPdfPostCallback(OAIHttpRequestWorker *worker);
    void invoicesInvoiceIdPutCallback(OAIHttpRequestWorker *worker);
    void invoicesInvoiceIdUnlinkProjectPdfPostCallback(OAIHttpRequestWorker *worker);
    void invoicesPostCallback(OAIHttpRequestWorker *worker);
    void invoicesVatOptionsGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void bulkDeleteInvoicesSignal(OAIEmptySuccessResponse summary);
    void invoicesGetSignal(OAI_invoices_get_200_response summary);
    void invoicesInvoiceIdCopyPostSignal(OAICreateSuccessResponse summary);
    void invoicesInvoiceIdDeleteSignal(OAI_clocking_records__clocking_record_id__put_200_response summary);
    void invoicesInvoiceIdGetSignal(OAI_invoices__invoice_id__get_200_response summary);
    void invoicesInvoiceIdLinkProjectPdfPostSignal(OAIEmptySuccessResponse summary);
    void invoicesInvoiceIdPutSignal(OAI_clocking_records__clocking_record_id__put_200_response summary);
    void invoicesInvoiceIdUnlinkProjectPdfPostSignal(OAIEmptySuccessResponse summary);
    void invoicesPostSignal(OAI_clocking_records_post_201_response summary);
    void invoicesVatOptionsGetSignal(OAI_integrations_productsSync_get_200_response summary);


    void bulkDeleteInvoicesSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void invoicesGetSignalFull(OAIHttpRequestWorker *worker, OAI_invoices_get_200_response summary);
    void invoicesInvoiceIdCopyPostSignalFull(OAIHttpRequestWorker *worker, OAICreateSuccessResponse summary);
    void invoicesInvoiceIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records__clocking_record_id__put_200_response summary);
    void invoicesInvoiceIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_invoices__invoice_id__get_200_response summary);
    void invoicesInvoiceIdLinkProjectPdfPostSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void invoicesInvoiceIdPutSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records__clocking_record_id__put_200_response summary);
    void invoicesInvoiceIdUnlinkProjectPdfPostSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void invoicesPostSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records_post_201_response summary);
    void invoicesVatOptionsGetSignalFull(OAIHttpRequestWorker *worker, OAI_integrations_productsSync_get_200_response summary);

    Q_DECL_DEPRECATED_X("Use bulkDeleteInvoicesSignalError() instead")
    void bulkDeleteInvoicesSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void bulkDeleteInvoicesSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesGetSignalError() instead")
    void invoicesGetSignalE(OAI_invoices_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesGetSignalError(OAI_invoices_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdCopyPostSignalError() instead")
    void invoicesInvoiceIdCopyPostSignalE(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdCopyPostSignalError(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdDeleteSignalError() instead")
    void invoicesInvoiceIdDeleteSignalE(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdDeleteSignalError(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdGetSignalError() instead")
    void invoicesInvoiceIdGetSignalE(OAI_invoices__invoice_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdGetSignalError(OAI_invoices__invoice_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdLinkProjectPdfPostSignalError() instead")
    void invoicesInvoiceIdLinkProjectPdfPostSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdLinkProjectPdfPostSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdPutSignalError() instead")
    void invoicesInvoiceIdPutSignalE(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdPutSignalError(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdUnlinkProjectPdfPostSignalError() instead")
    void invoicesInvoiceIdUnlinkProjectPdfPostSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdUnlinkProjectPdfPostSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesPostSignalError() instead")
    void invoicesPostSignalE(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesPostSignalError(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesVatOptionsGetSignalError() instead")
    void invoicesVatOptionsGetSignalE(OAI_integrations_productsSync_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesVatOptionsGetSignalError(OAI_integrations_productsSync_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use bulkDeleteInvoicesSignalErrorFull() instead")
    void bulkDeleteInvoicesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void bulkDeleteInvoicesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesGetSignalErrorFull() instead")
    void invoicesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdCopyPostSignalErrorFull() instead")
    void invoicesInvoiceIdCopyPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdCopyPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdDeleteSignalErrorFull() instead")
    void invoicesInvoiceIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdGetSignalErrorFull() instead")
    void invoicesInvoiceIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdLinkProjectPdfPostSignalErrorFull() instead")
    void invoicesInvoiceIdLinkProjectPdfPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdLinkProjectPdfPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdPutSignalErrorFull() instead")
    void invoicesInvoiceIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesInvoiceIdUnlinkProjectPdfPostSignalErrorFull() instead")
    void invoicesInvoiceIdUnlinkProjectPdfPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesInvoiceIdUnlinkProjectPdfPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesPostSignalErrorFull() instead")
    void invoicesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use invoicesVatOptionsGetSignalErrorFull() instead")
    void invoicesVatOptionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void invoicesVatOptionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
