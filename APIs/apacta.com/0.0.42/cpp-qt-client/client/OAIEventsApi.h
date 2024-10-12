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

#ifndef OAI_OAIEventsApi_H
#define OAI_OAIEventsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBadRequestResponse.h"
#include "OAIErrorNotFound.h"
#include "OAIErrorValidation.h"
#include "OAI_clocking_records_post_201_response.h"
#include "OAI_events__event_id__get_200_response.h"
#include "OAI_events_get_200_response.h"
#include "OAI_events_is_user_free_get_200_response.h"
#include "OAI_events_post_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIEventsApi : public QObject {
    Q_OBJECT

public:
    OAIEventsApi(const int timeOut = 0);
    ~OAIEventsApi();

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
    * @param[in]  event_id QString [required]
    */
    virtual void eventsEventIdDelete(const QString &event_id);

    /**
    * @param[in]  event_id QString [required]
    */
    virtual void eventsEventIdGet(const QString &event_id);

    /**
    * @param[in]  event_id QString [required]
    */
    virtual void eventsEventIdPut(const QString &event_id);

    /**
    * @param[in]  user_id QString [optional]
    * @param[in]  project_id QString [optional]
    * @param[in]  start_gt QString [optional]
    * @param[in]  start_lt QString [optional]
    * @param[in]  start_eq QString [optional]
    * @param[in]  end_gt QString [optional]
    * @param[in]  end_lt QString [optional]
    * @param[in]  end_eq QString [optional]
    * @param[in]  tags QString [optional]
    * @param[in]  without_users bool [optional]
    */
    virtual void eventsGet(const ::OpenAPI::OptionalParam<QString> &user_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &start_gt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &start_lt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &start_eq = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &end_gt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &end_lt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &end_eq = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &tags = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &without_users = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  user_id QString [required]
    * @param[in]  start QString [required]
    * @param[in]  end QString [required]
    */
    virtual void eventsIsUserFreeGet(const QString &user_id, const QString &start, const QString &end);

    /**
    * @param[in]  oai_events_post_request OAI_events_post_request [optional]
    */
    virtual void eventsPost(const ::OpenAPI::OptionalParam<OAI_events_post_request> &oai_events_post_request = ::OpenAPI::OptionalParam<OAI_events_post_request>());


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

    void eventsEventIdDeleteCallback(OAIHttpRequestWorker *worker);
    void eventsEventIdGetCallback(OAIHttpRequestWorker *worker);
    void eventsEventIdPutCallback(OAIHttpRequestWorker *worker);
    void eventsGetCallback(OAIHttpRequestWorker *worker);
    void eventsIsUserFreeGetCallback(OAIHttpRequestWorker *worker);
    void eventsPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void eventsEventIdDeleteSignal(OAI_events__event_id__get_200_response summary);
    void eventsEventIdGetSignal(OAI_events__event_id__get_200_response summary);
    void eventsEventIdPutSignal(OAI_events__event_id__get_200_response summary);
    void eventsGetSignal(OAI_events_get_200_response summary);
    void eventsIsUserFreeGetSignal(OAI_events_is_user_free_get_200_response summary);
    void eventsPostSignal(OAI_clocking_records_post_201_response summary);


    void eventsEventIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAI_events__event_id__get_200_response summary);
    void eventsEventIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_events__event_id__get_200_response summary);
    void eventsEventIdPutSignalFull(OAIHttpRequestWorker *worker, OAI_events__event_id__get_200_response summary);
    void eventsGetSignalFull(OAIHttpRequestWorker *worker, OAI_events_get_200_response summary);
    void eventsIsUserFreeGetSignalFull(OAIHttpRequestWorker *worker, OAI_events_is_user_free_get_200_response summary);
    void eventsPostSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records_post_201_response summary);

    Q_DECL_DEPRECATED_X("Use eventsEventIdDeleteSignalError() instead")
    void eventsEventIdDeleteSignalE(OAI_events__event_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsEventIdDeleteSignalError(OAI_events__event_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsEventIdGetSignalError() instead")
    void eventsEventIdGetSignalE(OAI_events__event_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsEventIdGetSignalError(OAI_events__event_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsEventIdPutSignalError() instead")
    void eventsEventIdPutSignalE(OAI_events__event_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsEventIdPutSignalError(OAI_events__event_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsGetSignalError() instead")
    void eventsGetSignalE(OAI_events_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsGetSignalError(OAI_events_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsIsUserFreeGetSignalError() instead")
    void eventsIsUserFreeGetSignalE(OAI_events_is_user_free_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsIsUserFreeGetSignalError(OAI_events_is_user_free_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsPostSignalError() instead")
    void eventsPostSignalE(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsPostSignalError(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use eventsEventIdDeleteSignalErrorFull() instead")
    void eventsEventIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsEventIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsEventIdGetSignalErrorFull() instead")
    void eventsEventIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsEventIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsEventIdPutSignalErrorFull() instead")
    void eventsEventIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsEventIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsGetSignalErrorFull() instead")
    void eventsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsIsUserFreeGetSignalErrorFull() instead")
    void eventsIsUserFreeGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsIsUserFreeGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventsPostSignalErrorFull() instead")
    void eventsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eventsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
