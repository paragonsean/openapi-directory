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

#ifndef OAI_OAIExpenseFilesApi_H
#define OAI_OAIExpenseFilesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorNotFound.h"
#include "OAIErrorValidation.h"
#include "OAIHttpFileElement.h"
#include "OAI_clocking_records_post_201_response.h"
#include "OAI_expense_files__expense_file_id__get_200_response.h"
#include "OAI_expense_files__expense_file_id__put_200_response.h"
#include "OAI_expense_files_get_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIExpenseFilesApi : public QObject {
    Q_OBJECT

public:
    OAIExpenseFilesApi(const int timeOut = 0);
    ~OAIExpenseFilesApi();

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
    * @param[in]  expense_file_id QString [required]
    */
    virtual void expenseFilesExpenseFileIdDelete(const QString &expense_file_id);

    /**
    * @param[in]  expense_file_id QString [required]
    */
    virtual void expenseFilesExpenseFileIdGet(const QString &expense_file_id);

    /**
    * @param[in]  expense_file_id QString [required]
    */
    virtual void expenseFilesExpenseFileIdPut(const QString &expense_file_id);

    /**
    * @param[in]  created_by_id QString [optional]
    * @param[in]  expense_id QString [optional]
    */
    virtual void expenseFilesGet(const ::OpenAPI::OptionalParam<QString> &created_by_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &expense_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  file OAIHttpFileElement [required]
    * @param[in]  description QString [optional]
    */
    virtual void expenseFilesPost(const OAIHttpFileElement &file, const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>());


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

    void expenseFilesExpenseFileIdDeleteCallback(OAIHttpRequestWorker *worker);
    void expenseFilesExpenseFileIdGetCallback(OAIHttpRequestWorker *worker);
    void expenseFilesExpenseFileIdPutCallback(OAIHttpRequestWorker *worker);
    void expenseFilesGetCallback(OAIHttpRequestWorker *worker);
    void expenseFilesPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void expenseFilesExpenseFileIdDeleteSignal(OAI_expense_files__expense_file_id__get_200_response summary);
    void expenseFilesExpenseFileIdGetSignal(OAI_expense_files__expense_file_id__get_200_response summary);
    void expenseFilesExpenseFileIdPutSignal(OAI_expense_files__expense_file_id__put_200_response summary);
    void expenseFilesGetSignal(OAI_expense_files_get_200_response summary);
    void expenseFilesPostSignal(OAI_clocking_records_post_201_response summary);


    void expenseFilesExpenseFileIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__get_200_response summary);
    void expenseFilesExpenseFileIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__get_200_response summary);
    void expenseFilesExpenseFileIdPutSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__put_200_response summary);
    void expenseFilesGetSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files_get_200_response summary);
    void expenseFilesPostSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records_post_201_response summary);

    Q_DECL_DEPRECATED_X("Use expenseFilesExpenseFileIdDeleteSignalError() instead")
    void expenseFilesExpenseFileIdDeleteSignalE(OAI_expense_files__expense_file_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesExpenseFileIdDeleteSignalError(OAI_expense_files__expense_file_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expenseFilesExpenseFileIdGetSignalError() instead")
    void expenseFilesExpenseFileIdGetSignalE(OAI_expense_files__expense_file_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesExpenseFileIdGetSignalError(OAI_expense_files__expense_file_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expenseFilesExpenseFileIdPutSignalError() instead")
    void expenseFilesExpenseFileIdPutSignalE(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesExpenseFileIdPutSignalError(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expenseFilesGetSignalError() instead")
    void expenseFilesGetSignalE(OAI_expense_files_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesGetSignalError(OAI_expense_files_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expenseFilesPostSignalError() instead")
    void expenseFilesPostSignalE(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesPostSignalError(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use expenseFilesExpenseFileIdDeleteSignalErrorFull() instead")
    void expenseFilesExpenseFileIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesExpenseFileIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expenseFilesExpenseFileIdGetSignalErrorFull() instead")
    void expenseFilesExpenseFileIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesExpenseFileIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expenseFilesExpenseFileIdPutSignalErrorFull() instead")
    void expenseFilesExpenseFileIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesExpenseFileIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expenseFilesGetSignalErrorFull() instead")
    void expenseFilesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expenseFilesPostSignalErrorFull() instead")
    void expenseFilesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expenseFilesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
