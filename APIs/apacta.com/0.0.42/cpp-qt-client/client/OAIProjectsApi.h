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

#ifndef OAI_OAIProjectsApi_H
#define OAI_OAIProjectsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIEmptySuccessResponse.h"
#include "OAIErrorNotFound.h"
#include "OAIErrorValidation.h"
#include "OAIHttpFileElement.h"
#include "OAI_clocking_records__clocking_record_id__delete_200_response.h"
#include "OAI_clocking_records__clocking_record_id__put_200_response.h"
#include "OAI_clocking_records_post_201_response.h"
#include "OAI_expense_files__expense_file_id__put_200_response.h"
#include "OAI_projects__project_id__all_files_get_200_response.h"
#include "OAI_projects__project_id__get_200_response.h"
#include "OAI_projects__project_id__put_request.h"
#include "OAI_projects__project_id__send_bulk_pdf_post_request.h"
#include "OAI_projects__project_id__users__get_200_response.h"
#include "OAI_projects__project_id__users__post_request.h"
#include "OAI_projects__project_id__users__user_id__get_200_response.h"
#include "OAI_projects_get_200_response.h"
#include "OAI_projects_has_projects_with_custom_statuses_get_200_response.h"
#include "OAI_projects_post_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIProjectsApi : public QObject {
    Q_OBJECT

public:
    OAIProjectsApi(const int timeOut = 0);
    ~OAIProjectsApi();

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
    * @param[in]  show_all bool [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  direction QString [optional]
    * @param[in]  contact_id QString [optional]
    * @param[in]  company_id QString [optional]
    * @param[in]  project_status_id QString [optional]
    * @param[in]  project_status_ids QList<QString> [optional]
    * @param[in]  name QString [optional]
    * @param[in]  erp_project_id QString [optional]
    * @param[in]  erp_task_id QString [optional]
    * @param[in]  start_time_gte QString [optional]
    * @param[in]  start_time_lte QString [optional]
    * @param[in]  start_time_eq QString [optional]
    * @param[in]  event_start_gt QString [optional]
    * @param[in]  event_start_lt QString [optional]
    * @param[in]  event_start_eq QString [optional]
    * @param[in]  event_end_gt QString [optional]
    * @param[in]  event_end_lt QString [optional]
    * @param[in]  event_end_eq QString [optional]
    */
    virtual void projectsGet(const ::OpenAPI::OptionalParam<bool> &show_all = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &direction = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &contact_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &company_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &project_status_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &project_status_ids = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &erp_project_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &erp_task_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &start_time_gte = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &start_time_lte = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &start_time_eq = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &event_start_gt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &event_start_lt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &event_start_eq = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &event_end_gt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &event_end_lt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &event_end_eq = ::OpenAPI::OptionalParam<QString>());


    virtual void projectsHasProjectsWithCustomStatusesGet();

    /**
    * @param[in]  oai_projects_post_request OAI_projects_post_request [optional]
    */
    virtual void projectsPost(const ::OpenAPI::OptionalParam<OAI_projects_post_request> &oai_projects_post_request = ::OpenAPI::OptionalParam<OAI_projects_post_request>());

    /**
    * @param[in]  project_id QString [required]
    */
    virtual void projectsProjectIdAllFilesGet(const QString &project_id);

    /**
    * @param[in]  project_id QString [required]
    */
    virtual void projectsProjectIdDelete(const QString &project_id);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  file_id QString [required]
    */
    virtual void projectsProjectIdFilesFileIdDelete(const QString &project_id, const QString &file_id);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  file_id QString [required]
    */
    virtual void projectsProjectIdFilesFileIdGet(const QString &project_id, const QString &file_id);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  file_id QString [required]
    */
    virtual void projectsProjectIdFilesFileIdPut(const QString &project_id, const QString &file_id);

    /**
    * @param[in]  project_id QString [required]
    */
    virtual void projectsProjectIdFilesGet(const QString &project_id);

    /**
    * @param[in]  project_id QString [required]
    */
    virtual void projectsProjectIdGet(const QString &project_id);

    /**
    * @param[in]  project_id QString [required]
    */
    virtual void projectsProjectIdProjectFilesGet(const QString &project_id);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  file OAIHttpFileElement [required]
    */
    virtual void projectsProjectIdProjectFilesPost(const QString &project_id, const OAIHttpFileElement &file);

    /**
    * @param[in]  project_file_id QString [required]
    * @param[in]  project_id QString [required]
    */
    virtual void projectsProjectIdProjectFilesProjectFileIdDelete(const QString &project_file_id, const QString &project_id);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  project_file_id QString [required]
    */
    virtual void projectsProjectIdProjectFilesProjectFileIdGet(const QString &project_id, const QString &project_file_id);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  project_file_id QString [required]
    */
    virtual void projectsProjectIdProjectFilesProjectFileIdPut(const QString &project_id, const QString &project_file_id);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  oai_projects__project_id__put_request OAI_projects__project_id__put_request [optional]
    */
    virtual void projectsProjectIdPut(const QString &project_id, const ::OpenAPI::OptionalParam<OAI_projects__project_id__put_request> &oai_projects__project_id__put_request = ::OpenAPI::OptionalParam<OAI_projects__project_id__put_request>());

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  oai_projects__project_id__send_bulk_pdf_post_request OAI_projects__project_id__send_bulk_pdf_post_request [required]
    */
    virtual void projectsProjectIdSendBulkPdfPost(const QString &project_id, const OAI_projects__project_id__send_bulk_pdf_post_request &oai_projects__project_id__send_bulk_pdf_post_request);

    /**
    * @param[in]  project_id QString [required]
    */
    virtual void projectsProjectIdUsersGet(const QString &project_id);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  oai_projects__project_id__users__post_request OAI_projects__project_id__users__post_request [optional]
    */
    virtual void projectsProjectIdUsersPost(const QString &project_id, const ::OpenAPI::OptionalParam<OAI_projects__project_id__users__post_request> &oai_projects__project_id__users__post_request = ::OpenAPI::OptionalParam<OAI_projects__project_id__users__post_request>());

    /**
    * @param[in]  user_id QString [required]
    * @param[in]  project_id QString [required]
    */
    virtual void projectsProjectIdUsersUserIdDelete(const QString &user_id, const QString &project_id);

    /**
    * @param[in]  user_id QString [required]
    * @param[in]  project_id QString [required]
    */
    virtual void projectsProjectIdUsersUserIdGet(const QString &user_id, const QString &project_id);


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

    void projectsGetCallback(OAIHttpRequestWorker *worker);
    void projectsHasProjectsWithCustomStatusesGetCallback(OAIHttpRequestWorker *worker);
    void projectsPostCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdAllFilesGetCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdDeleteCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdFilesFileIdDeleteCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdFilesFileIdGetCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdFilesFileIdPutCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdFilesGetCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdGetCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdProjectFilesGetCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdProjectFilesPostCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdProjectFilesProjectFileIdDeleteCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdProjectFilesProjectFileIdGetCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdProjectFilesProjectFileIdPutCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdPutCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdSendBulkPdfPostCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdUsersGetCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdUsersPostCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdUsersUserIdDeleteCallback(OAIHttpRequestWorker *worker);
    void projectsProjectIdUsersUserIdGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void projectsGetSignal(OAI_projects_get_200_response summary);
    void projectsHasProjectsWithCustomStatusesGetSignal(OAI_projects_has_projects_with_custom_statuses_get_200_response summary);
    void projectsPostSignal(OAI_clocking_records_post_201_response summary);
    void projectsProjectIdAllFilesGetSignal(OAI_projects__project_id__all_files_get_200_response summary);
    void projectsProjectIdDeleteSignal(OAI_clocking_records__clocking_record_id__delete_200_response summary);
    void projectsProjectIdFilesFileIdDeleteSignal(OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdFilesFileIdGetSignal(OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdFilesFileIdPutSignal(OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdFilesGetSignal(OAI_projects__project_id__all_files_get_200_response summary);
    void projectsProjectIdGetSignal(OAI_projects__project_id__get_200_response summary);
    void projectsProjectIdProjectFilesGetSignal(OAI_projects__project_id__all_files_get_200_response summary);
    void projectsProjectIdProjectFilesPostSignal(OAI_clocking_records_post_201_response summary);
    void projectsProjectIdProjectFilesProjectFileIdDeleteSignal(OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdProjectFilesProjectFileIdGetSignal(OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdProjectFilesProjectFileIdPutSignal(OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdPutSignal(OAI_clocking_records__clocking_record_id__put_200_response summary);
    void projectsProjectIdSendBulkPdfPostSignal(OAIEmptySuccessResponse summary);
    void projectsProjectIdUsersGetSignal(OAI_projects__project_id__users__get_200_response summary);
    void projectsProjectIdUsersPostSignal(OAI_clocking_records_post_201_response summary);
    void projectsProjectIdUsersUserIdDeleteSignal(OAI_clocking_records__clocking_record_id__put_200_response summary);
    void projectsProjectIdUsersUserIdGetSignal(OAI_projects__project_id__users__user_id__get_200_response summary);


    void projectsGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects_get_200_response summary);
    void projectsHasProjectsWithCustomStatusesGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects_has_projects_with_custom_statuses_get_200_response summary);
    void projectsPostSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records_post_201_response summary);
    void projectsProjectIdAllFilesGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects__project_id__all_files_get_200_response summary);
    void projectsProjectIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records__clocking_record_id__delete_200_response summary);
    void projectsProjectIdFilesFileIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdFilesFileIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdFilesFileIdPutSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdFilesGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects__project_id__all_files_get_200_response summary);
    void projectsProjectIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects__project_id__get_200_response summary);
    void projectsProjectIdProjectFilesGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects__project_id__all_files_get_200_response summary);
    void projectsProjectIdProjectFilesPostSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records_post_201_response summary);
    void projectsProjectIdProjectFilesProjectFileIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdProjectFilesProjectFileIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdProjectFilesProjectFileIdPutSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__put_200_response summary);
    void projectsProjectIdPutSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records__clocking_record_id__put_200_response summary);
    void projectsProjectIdSendBulkPdfPostSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void projectsProjectIdUsersGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects__project_id__users__get_200_response summary);
    void projectsProjectIdUsersPostSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records_post_201_response summary);
    void projectsProjectIdUsersUserIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records__clocking_record_id__put_200_response summary);
    void projectsProjectIdUsersUserIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_projects__project_id__users__user_id__get_200_response summary);

    Q_DECL_DEPRECATED_X("Use projectsGetSignalError() instead")
    void projectsGetSignalE(OAI_projects_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsGetSignalError(OAI_projects_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsHasProjectsWithCustomStatusesGetSignalError() instead")
    void projectsHasProjectsWithCustomStatusesGetSignalE(OAI_projects_has_projects_with_custom_statuses_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsHasProjectsWithCustomStatusesGetSignalError(OAI_projects_has_projects_with_custom_statuses_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsPostSignalError() instead")
    void projectsPostSignalE(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsPostSignalError(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdAllFilesGetSignalError() instead")
    void projectsProjectIdAllFilesGetSignalE(OAI_projects__project_id__all_files_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdAllFilesGetSignalError(OAI_projects__project_id__all_files_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdDeleteSignalError() instead")
    void projectsProjectIdDeleteSignalE(OAI_clocking_records__clocking_record_id__delete_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdDeleteSignalError(OAI_clocking_records__clocking_record_id__delete_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdFilesFileIdDeleteSignalError() instead")
    void projectsProjectIdFilesFileIdDeleteSignalE(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdFilesFileIdDeleteSignalError(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdFilesFileIdGetSignalError() instead")
    void projectsProjectIdFilesFileIdGetSignalE(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdFilesFileIdGetSignalError(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdFilesFileIdPutSignalError() instead")
    void projectsProjectIdFilesFileIdPutSignalE(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdFilesFileIdPutSignalError(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdFilesGetSignalError() instead")
    void projectsProjectIdFilesGetSignalE(OAI_projects__project_id__all_files_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdFilesGetSignalError(OAI_projects__project_id__all_files_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdGetSignalError() instead")
    void projectsProjectIdGetSignalE(OAI_projects__project_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdGetSignalError(OAI_projects__project_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesGetSignalError() instead")
    void projectsProjectIdProjectFilesGetSignalE(OAI_projects__project_id__all_files_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesGetSignalError(OAI_projects__project_id__all_files_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesPostSignalError() instead")
    void projectsProjectIdProjectFilesPostSignalE(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesPostSignalError(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesProjectFileIdDeleteSignalError() instead")
    void projectsProjectIdProjectFilesProjectFileIdDeleteSignalE(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesProjectFileIdDeleteSignalError(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesProjectFileIdGetSignalError() instead")
    void projectsProjectIdProjectFilesProjectFileIdGetSignalE(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesProjectFileIdGetSignalError(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesProjectFileIdPutSignalError() instead")
    void projectsProjectIdProjectFilesProjectFileIdPutSignalE(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesProjectFileIdPutSignalError(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdPutSignalError() instead")
    void projectsProjectIdPutSignalE(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdPutSignalError(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdSendBulkPdfPostSignalError() instead")
    void projectsProjectIdSendBulkPdfPostSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdSendBulkPdfPostSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdUsersGetSignalError() instead")
    void projectsProjectIdUsersGetSignalE(OAI_projects__project_id__users__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdUsersGetSignalError(OAI_projects__project_id__users__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdUsersPostSignalError() instead")
    void projectsProjectIdUsersPostSignalE(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdUsersPostSignalError(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdUsersUserIdDeleteSignalError() instead")
    void projectsProjectIdUsersUserIdDeleteSignalE(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdUsersUserIdDeleteSignalError(OAI_clocking_records__clocking_record_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdUsersUserIdGetSignalError() instead")
    void projectsProjectIdUsersUserIdGetSignalE(OAI_projects__project_id__users__user_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdUsersUserIdGetSignalError(OAI_projects__project_id__users__user_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use projectsGetSignalErrorFull() instead")
    void projectsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsHasProjectsWithCustomStatusesGetSignalErrorFull() instead")
    void projectsHasProjectsWithCustomStatusesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsHasProjectsWithCustomStatusesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsPostSignalErrorFull() instead")
    void projectsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdAllFilesGetSignalErrorFull() instead")
    void projectsProjectIdAllFilesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdAllFilesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdDeleteSignalErrorFull() instead")
    void projectsProjectIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdFilesFileIdDeleteSignalErrorFull() instead")
    void projectsProjectIdFilesFileIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdFilesFileIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdFilesFileIdGetSignalErrorFull() instead")
    void projectsProjectIdFilesFileIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdFilesFileIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdFilesFileIdPutSignalErrorFull() instead")
    void projectsProjectIdFilesFileIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdFilesFileIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdFilesGetSignalErrorFull() instead")
    void projectsProjectIdFilesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdFilesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdGetSignalErrorFull() instead")
    void projectsProjectIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesGetSignalErrorFull() instead")
    void projectsProjectIdProjectFilesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesPostSignalErrorFull() instead")
    void projectsProjectIdProjectFilesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesProjectFileIdDeleteSignalErrorFull() instead")
    void projectsProjectIdProjectFilesProjectFileIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesProjectFileIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesProjectFileIdGetSignalErrorFull() instead")
    void projectsProjectIdProjectFilesProjectFileIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesProjectFileIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdProjectFilesProjectFileIdPutSignalErrorFull() instead")
    void projectsProjectIdProjectFilesProjectFileIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdProjectFilesProjectFileIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdPutSignalErrorFull() instead")
    void projectsProjectIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdSendBulkPdfPostSignalErrorFull() instead")
    void projectsProjectIdSendBulkPdfPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdSendBulkPdfPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdUsersGetSignalErrorFull() instead")
    void projectsProjectIdUsersGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdUsersGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdUsersPostSignalErrorFull() instead")
    void projectsProjectIdUsersPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdUsersPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdUsersUserIdDeleteSignalErrorFull() instead")
    void projectsProjectIdUsersUserIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdUsersUserIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsProjectIdUsersUserIdGetSignalErrorFull() instead")
    void projectsProjectIdUsersUserIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsProjectIdUsersUserIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
