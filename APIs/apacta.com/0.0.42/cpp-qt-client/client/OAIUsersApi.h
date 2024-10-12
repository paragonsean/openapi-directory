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

#ifndef OAI_OAIUsersApi_H
#define OAI_OAIUsersApi_H

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
#include "OAIForbiddenError.h"
#include "OAIHttpFileElement.h"
#include "OAI_clocking_records__clocking_record_id__put_200_response.h"
#include "OAI_clocking_records_post_201_response.h"
#include "OAI_companies__company_id__integration_settings_post_request.h"
#include "OAI_projects__project_id__users__get_200_response.h"
#include "OAI_projects__project_id__users__user_id__get_200_response.h"
#include "OAI_users__user_id__integration_settings__integration_settings_user_id__get_200_response.h"
#include "OAI_users__user_id__integration_settings_get_200_response.h"
#include "OAI_users_post_request.h"
#include "OAI_users_resendWelcomeSms_get_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIUsersApi : public QObject {
    Q_OBJECT

public:
    OAIUsersApi(const int timeOut = 0);
    ~OAIUsersApi();

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
    * @param[in]  oai_bulk_action_request_body OAIBulkActionRequestBody [optional]
    */
    virtual void usersBulkActivate(const ::OpenAPI::OptionalParam<OAIBulkActionRequestBody> &oai_bulk_action_request_body = ::OpenAPI::OptionalParam<OAIBulkActionRequestBody>());

    /**
    * @param[in]  oai_bulk_action_request_body OAIBulkActionRequestBody [optional]
    */
    virtual void usersBulkDeactivate(const ::OpenAPI::OptionalParam<OAIBulkActionRequestBody> &oai_bulk_action_request_body = ::OpenAPI::OptionalParam<OAIBulkActionRequestBody>());

    /**
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  stock_location_id QString [optional]
    * @param[in]  is_active bool [optional]
    */
    virtual void usersGet(const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &stock_location_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &is_active = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  oai_users_post_request OAI_users_post_request [optional]
    */
    virtual void usersPost(const ::OpenAPI::OptionalParam<OAI_users_post_request> &oai_users_post_request = ::OpenAPI::OptionalParam<OAI_users_post_request>());


    virtual void usersResendWelcomeSmsGet();

    /**
    * @param[in]  user_id QString [required]
    */
    virtual void usersUserIdDelete(const QString &user_id);

    /**
    * @param[in]  user_id QString [required]
    */
    virtual void usersUserIdGet(const QString &user_id);

    /**
    * @param[in]  user_id QString [required]
    */
    virtual void usersUserIdIntegrationSettingsGet(const QString &user_id);

    /**
    * @param[in]  user_id QString [required]
    * @param[in]  integration_settings_user_id QString [required]
    */
    virtual void usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete(const QString &user_id, const QString &integration_settings_user_id);

    /**
    * @param[in]  user_id QString [required]
    * @param[in]  integration_settings_user_id QString [required]
    */
    virtual void usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet(const QString &user_id, const QString &integration_settings_user_id);

    /**
    * @param[in]  user_id QString [required]
    * @param[in]  integration_settings_user_id QString [required]
    */
    virtual void usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut(const QString &user_id, const QString &integration_settings_user_id);

    /**
    * @param[in]  user_id QString [required]
    * @param[in]  oai_companies__company_id__integration_settings_post_request OAI_companies__company_id__integration_settings_post_request [optional]
    */
    virtual void usersUserIdIntegrationSettingsPost(const QString &user_id, const ::OpenAPI::OptionalParam<OAI_companies__company_id__integration_settings_post_request> &oai_companies__company_id__integration_settings_post_request = ::OpenAPI::OptionalParam<OAI_companies__company_id__integration_settings_post_request>());

    /**
    * @param[in]  user_id QString [required]
    */
    virtual void usersUserIdPut(const QString &user_id);

    /**
    * @param[in]  user_id QString [required]
    * @param[in]  image OAIHttpFileElement [optional]
    */
    virtual void usersUserIdUploadImagePost(const QString &user_id, const ::OpenAPI::OptionalParam<OAIHttpFileElement> &image = ::OpenAPI::OptionalParam<OAIHttpFileElement>());


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

    void usersBulkActivateCallback(OAIHttpRequestWorker *worker);
    void usersBulkDeactivateCallback(OAIHttpRequestWorker *worker);
    void usersGetCallback(OAIHttpRequestWorker *worker);
    void usersPostCallback(OAIHttpRequestWorker *worker);
    void usersResendWelcomeSmsGetCallback(OAIHttpRequestWorker *worker);
    void usersUserIdDeleteCallback(OAIHttpRequestWorker *worker);
    void usersUserIdGetCallback(OAIHttpRequestWorker *worker);
    void usersUserIdIntegrationSettingsGetCallback(OAIHttpRequestWorker *worker);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteCallback(OAIHttpRequestWorker *worker);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetCallback(OAIHttpRequestWorker *worker);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutCallback(OAIHttpRequestWorker *worker);
    void usersUserIdIntegrationSettingsPostCallback(OAIHttpRequestWorker *worker);
    void usersUserIdPutCallback(OAIHttpRequestWorker *worker);
    void usersUserIdUploadImagePostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void usersBulkActivateSignal(OAIEmptySuccessResponse summary);
    void usersBulkDeactivateSignal(OAIEmptySuccessResponse summary);
    void usersGetSignal(OAI_projects__project_id__users__get_200_response summary);
    void usersPostSignal(OAI_clocking_records_post_201_response summary);
    void usersResendWelcomeSmsGetSignal(OAI_users_resendWelcomeSms_get_200_response summary);
    void usersUserIdDeleteSignal(OAI_clocking_records__clocking_record_id__put_200_response summary);
    void usersUserIdGetSignal(OAI_projects__project_id__users__user_id__get_200_response summary);
    void usersUserIdIntegrationSettingsGetSignal(OAI_users__user_id__integration_settings_get_200_response summary);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignal(OAIEmptySuccessResponse summary);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignal(OAI_users__user_id__integration_settings__integration_settings_user_id__get_200_response summary);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignal(OAIEmptySuccessResponse summary);
    void usersUserIdIntegrationSettingsPostSignal(OAICreateSuccessResponse summary);
    void usersUserIdPutSignal(OAI_clocking_records__clocking_record_id__put_200_response summary);
    void usersUserIdUploadImagePostSignal(OAICreateSuccessResponse summary);


    void usersBulkActivateSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void usersBulkDeactivateSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void usersGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects__project_id__users__get_200_response summary);
    void usersPostSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records_post_201_response summary);
    void usersResendWelcomeSmsGetSignalFull(OAIHttpRequestWorker *worker, OAI_users_resendWelcomeSms_get_200_response summary);
    void usersUserIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records__clocking_record_id__put_200_response summary);
    void usersUserIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects__project_id__users__user_id__get_200_response summary);
    void usersUserIdIntegrationSettingsGetSignalFull(OAIHttpRequestWorker *worker, OAI_users__user_id__integration_settings_get_200_response summary);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_users__user_id__integration_settings__integration_settings_user_id__get_200_response summary);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void usersUserIdIntegrationSettingsPostSignalFull(OAIHttpRequestWorker *worker, OAICreateSuccessResponse summary);
    void usersUserIdPutSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records__clocking_record_id__put_200_response summary);
    void usersUserIdUploadImagePostSignalFull(OAIHttpRequestWorker *worker, OAICreateSuccessResponse summary);

    Q_DECL_DEPRECATED_X("Use usersBulkActivateSignalError() instead")
    void usersBulkActivateSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersBulkActivateSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersBulkDeactivateSignalError() instead")
    void usersBulkDeactivateSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersBulkDeactivateSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersGetSignalError() instead")
    void usersGetSignalE(OAI_projects__project_id__users__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersGetSignalError(OAI_projects__project_id__users__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersPostSignalError() instead")
    void usersPostSignalE(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersPostSignalError(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersResendWelcomeSmsGetSignalError() instead")
    void usersResendWelcomeSmsGetSignalE(OAI_users_resendWelcomeSms_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersResendWelcomeSmsGetSignalError(OAI_users_resendWelcomeSms_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdDeleteSignalError() instead")
    void usersUserIdDeleteSignalE(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdDeleteSignalError(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdGetSignalError() instead")
    void usersUserIdGetSignalE(OAI_projects__project_id__users__user_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdGetSignalError(OAI_projects__project_id__users__user_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsGetSignalError() instead")
    void usersUserIdIntegrationSettingsGetSignalE(OAI_users__user_id__integration_settings_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsGetSignalError(OAI_users__user_id__integration_settings_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalError() instead")
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalError() instead")
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalE(OAI_users__user_id__integration_settings__integration_settings_user_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalError(OAI_users__user_id__integration_settings__integration_settings_user_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalError() instead")
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsPostSignalError() instead")
    void usersUserIdIntegrationSettingsPostSignalE(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsPostSignalError(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdPutSignalError() instead")
    void usersUserIdPutSignalE(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdPutSignalError(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdUploadImagePostSignalError() instead")
    void usersUserIdUploadImagePostSignalE(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdUploadImagePostSignalError(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use usersBulkActivateSignalErrorFull() instead")
    void usersBulkActivateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersBulkActivateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersBulkDeactivateSignalErrorFull() instead")
    void usersBulkDeactivateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersBulkDeactivateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersGetSignalErrorFull() instead")
    void usersGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersPostSignalErrorFull() instead")
    void usersPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersResendWelcomeSmsGetSignalErrorFull() instead")
    void usersResendWelcomeSmsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersResendWelcomeSmsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdDeleteSignalErrorFull() instead")
    void usersUserIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdGetSignalErrorFull() instead")
    void usersUserIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsGetSignalErrorFull() instead")
    void usersUserIdIntegrationSettingsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalErrorFull() instead")
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalErrorFull() instead")
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalErrorFull() instead")
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdIntegrationSettingsPostSignalErrorFull() instead")
    void usersUserIdIntegrationSettingsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdIntegrationSettingsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdPutSignalErrorFull() instead")
    void usersUserIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersUserIdUploadImagePostSignalErrorFull() instead")
    void usersUserIdUploadImagePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersUserIdUploadImagePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
