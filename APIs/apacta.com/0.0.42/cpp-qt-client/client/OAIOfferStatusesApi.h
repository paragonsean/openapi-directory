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

#ifndef OAI_OAIOfferStatusesApi_H
#define OAI_OAIOfferStatusesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBadRequestResponse.h"
#include "OAIBulkActionRequestBody.h"
#include "OAIEmptySuccessResponse.h"
#include "OAIErrorNotFound.h"
#include "OAIErrorValidation.h"
#include "OAIForbiddenError.h"
#include "OAI_offer_statuses__offer_status_id__get_200_response.h"
#include "OAI_offer_statuses_get_200_response.h"
#include "OAI_offer_statuses_post_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIOfferStatusesApi : public QObject {
    Q_OBJECT

public:
    OAIOfferStatusesApi(const int timeOut = 0);
    ~OAIOfferStatusesApi();

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
    virtual void offerStatusesBulkDeleteDelete(const OAIBulkActionRequestBody &oai_bulk_action_request_body);


    virtual void offerStatusesGet();

    /**
    * @param[in]  offer_status_id QString [required]
    */
    virtual void offerStatusesOfferStatusIdDelete(const QString &offer_status_id);

    /**
    * @param[in]  offer_status_id QString [required]
    */
    virtual void offerStatusesOfferStatusIdGet(const QString &offer_status_id);

    /**
    * @param[in]  offer_status_id QString [required]
    */
    virtual void offerStatusesOfferStatusIdPut(const QString &offer_status_id);

    /**
    * @param[in]  oai_offer_statuses_post_request OAI_offer_statuses_post_request [required]
    */
    virtual void offerStatusesPost(const OAI_offer_statuses_post_request &oai_offer_statuses_post_request);


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

    void offerStatusesBulkDeleteDeleteCallback(OAIHttpRequestWorker *worker);
    void offerStatusesGetCallback(OAIHttpRequestWorker *worker);
    void offerStatusesOfferStatusIdDeleteCallback(OAIHttpRequestWorker *worker);
    void offerStatusesOfferStatusIdGetCallback(OAIHttpRequestWorker *worker);
    void offerStatusesOfferStatusIdPutCallback(OAIHttpRequestWorker *worker);
    void offerStatusesPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void offerStatusesBulkDeleteDeleteSignal(OAIEmptySuccessResponse summary);
    void offerStatusesGetSignal(OAI_offer_statuses_get_200_response summary);
    void offerStatusesOfferStatusIdDeleteSignal(OAIEmptySuccessResponse summary);
    void offerStatusesOfferStatusIdGetSignal(OAI_offer_statuses__offer_status_id__get_200_response summary);
    void offerStatusesOfferStatusIdPutSignal(OAIEmptySuccessResponse summary);
    void offerStatusesPostSignal(OAIEmptySuccessResponse summary);


    void offerStatusesBulkDeleteDeleteSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void offerStatusesGetSignalFull(OAIHttpRequestWorker *worker, OAI_offer_statuses_get_200_response summary);
    void offerStatusesOfferStatusIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void offerStatusesOfferStatusIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_offer_statuses__offer_status_id__get_200_response summary);
    void offerStatusesOfferStatusIdPutSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void offerStatusesPostSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);

    Q_DECL_DEPRECATED_X("Use offerStatusesBulkDeleteDeleteSignalError() instead")
    void offerStatusesBulkDeleteDeleteSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesBulkDeleteDeleteSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesGetSignalError() instead")
    void offerStatusesGetSignalE(OAI_offer_statuses_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesGetSignalError(OAI_offer_statuses_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesOfferStatusIdDeleteSignalError() instead")
    void offerStatusesOfferStatusIdDeleteSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesOfferStatusIdDeleteSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesOfferStatusIdGetSignalError() instead")
    void offerStatusesOfferStatusIdGetSignalE(OAI_offer_statuses__offer_status_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesOfferStatusIdGetSignalError(OAI_offer_statuses__offer_status_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesOfferStatusIdPutSignalError() instead")
    void offerStatusesOfferStatusIdPutSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesOfferStatusIdPutSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesPostSignalError() instead")
    void offerStatusesPostSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesPostSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use offerStatusesBulkDeleteDeleteSignalErrorFull() instead")
    void offerStatusesBulkDeleteDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesBulkDeleteDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesGetSignalErrorFull() instead")
    void offerStatusesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesOfferStatusIdDeleteSignalErrorFull() instead")
    void offerStatusesOfferStatusIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesOfferStatusIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesOfferStatusIdGetSignalErrorFull() instead")
    void offerStatusesOfferStatusIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesOfferStatusIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesOfferStatusIdPutSignalErrorFull() instead")
    void offerStatusesOfferStatusIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesOfferStatusIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerStatusesPostSignalErrorFull() instead")
    void offerStatusesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void offerStatusesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
