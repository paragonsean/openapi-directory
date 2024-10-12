/**
 * Airflow API (Stable)
 * # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executing via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"name\": \"string\",     \"slots\": 0,     \"occupied_slots\": 0,     \"used_slots\": 0,     \"queued_slots\": 0,     \"open_slots\": 0 } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. 
 *
 * The version of the OpenAPI document: 2.5.3
 * Contact: dev@airflow.apache.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDAGRunApi_H
#define OAI_OAIDAGRunApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIClearDagRun.h"
#include "OAIClear_dag_run_200_response.h"
#include "OAIDAGRun.h"
#include "OAIDAGRunCollection.h"
#include "OAIDatasetEventCollection.h"
#include "OAIError.h"
#include "OAIListDagRunsForm.h"
#include "OAISetDagRunNote.h"
#include "OAIUpdateDagRunState.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDAGRunApi : public QObject {
    Q_OBJECT

public:
    OAIDAGRunApi(const int timeOut = 0);
    ~OAIDAGRunApi();

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
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  oai_clear_dag_run OAIClearDagRun [required]
    */
    virtual void clearDagRun(const QString &dag_id, const QString &dag_run_id, const OAIClearDagRun &oai_clear_dag_run);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    */
    virtual void deleteDagRun(const QString &dag_id, const QString &dag_run_id);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    */
    virtual void getDagRun(const QString &dag_id, const QString &dag_run_id);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  execution_date_gte QDateTime [optional]
    * @param[in]  execution_date_lte QDateTime [optional]
    * @param[in]  start_date_gte QDateTime [optional]
    * @param[in]  start_date_lte QDateTime [optional]
    * @param[in]  end_date_gte QDateTime [optional]
    * @param[in]  end_date_lte QDateTime [optional]
    * @param[in]  state QList<QString> [optional]
    * @param[in]  order_by QString [optional]
    */
    virtual void getDagRuns(const QString &dag_id, const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QDateTime> &execution_date_gte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &execution_date_lte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &start_date_gte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &start_date_lte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date_gte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date_lte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QList<QString>> &state = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &order_by = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_dag_runs_form OAIListDagRunsForm [required]
    */
    virtual void getDagRunsBatch(const OAIListDagRunsForm &oai_list_dag_runs_form);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    */
    virtual void getUpstreamDatasetEvents(const QString &dag_id, const QString &dag_run_id);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  oaidag_run OAIDAGRun [required]
    */
    virtual void postDagRun(const QString &dag_id, const OAIDAGRun &oaidag_run);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  oai_set_dag_run_note OAISetDagRunNote [required]
    */
    virtual void setDagRunNote(const QString &dag_id, const QString &dag_run_id, const OAISetDagRunNote &oai_set_dag_run_note);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  oai_update_dag_run_state OAIUpdateDagRunState [required]
    */
    virtual void updateDagRunState(const QString &dag_id, const QString &dag_run_id, const OAIUpdateDagRunState &oai_update_dag_run_state);


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

    void clearDagRunCallback(OAIHttpRequestWorker *worker);
    void deleteDagRunCallback(OAIHttpRequestWorker *worker);
    void getDagRunCallback(OAIHttpRequestWorker *worker);
    void getDagRunsCallback(OAIHttpRequestWorker *worker);
    void getDagRunsBatchCallback(OAIHttpRequestWorker *worker);
    void getUpstreamDatasetEventsCallback(OAIHttpRequestWorker *worker);
    void postDagRunCallback(OAIHttpRequestWorker *worker);
    void setDagRunNoteCallback(OAIHttpRequestWorker *worker);
    void updateDagRunStateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void clearDagRunSignal(OAIClear_dag_run_200_response summary);
    void deleteDagRunSignal();
    void getDagRunSignal(OAIDAGRun summary);
    void getDagRunsSignal(OAIDAGRunCollection summary);
    void getDagRunsBatchSignal(OAIDAGRunCollection summary);
    void getUpstreamDatasetEventsSignal(OAIDatasetEventCollection summary);
    void postDagRunSignal(OAIDAGRun summary);
    void setDagRunNoteSignal(OAIDAGRun summary);
    void updateDagRunStateSignal(OAIDAGRun summary);


    void clearDagRunSignalFull(OAIHttpRequestWorker *worker, OAIClear_dag_run_200_response summary);
    void deleteDagRunSignalFull(OAIHttpRequestWorker *worker);
    void getDagRunSignalFull(OAIHttpRequestWorker *worker, OAIDAGRun summary);
    void getDagRunsSignalFull(OAIHttpRequestWorker *worker, OAIDAGRunCollection summary);
    void getDagRunsBatchSignalFull(OAIHttpRequestWorker *worker, OAIDAGRunCollection summary);
    void getUpstreamDatasetEventsSignalFull(OAIHttpRequestWorker *worker, OAIDatasetEventCollection summary);
    void postDagRunSignalFull(OAIHttpRequestWorker *worker, OAIDAGRun summary);
    void setDagRunNoteSignalFull(OAIHttpRequestWorker *worker, OAIDAGRun summary);
    void updateDagRunStateSignalFull(OAIHttpRequestWorker *worker, OAIDAGRun summary);

    Q_DECL_DEPRECATED_X("Use clearDagRunSignalError() instead")
    void clearDagRunSignalE(OAIClear_dag_run_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clearDagRunSignalError(OAIClear_dag_run_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDagRunSignalError() instead")
    void deleteDagRunSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDagRunSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDagRunSignalError() instead")
    void getDagRunSignalE(OAIDAGRun summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDagRunSignalError(OAIDAGRun summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDagRunsSignalError() instead")
    void getDagRunsSignalE(OAIDAGRunCollection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDagRunsSignalError(OAIDAGRunCollection summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDagRunsBatchSignalError() instead")
    void getDagRunsBatchSignalE(OAIDAGRunCollection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDagRunsBatchSignalError(OAIDAGRunCollection summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUpstreamDatasetEventsSignalError() instead")
    void getUpstreamDatasetEventsSignalE(OAIDatasetEventCollection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUpstreamDatasetEventsSignalError(OAIDatasetEventCollection summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDagRunSignalError() instead")
    void postDagRunSignalE(OAIDAGRun summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDagRunSignalError(OAIDAGRun summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setDagRunNoteSignalError() instead")
    void setDagRunNoteSignalE(OAIDAGRun summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setDagRunNoteSignalError(OAIDAGRun summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDagRunStateSignalError() instead")
    void updateDagRunStateSignalE(OAIDAGRun summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDagRunStateSignalError(OAIDAGRun summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use clearDagRunSignalErrorFull() instead")
    void clearDagRunSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clearDagRunSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDagRunSignalErrorFull() instead")
    void deleteDagRunSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDagRunSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDagRunSignalErrorFull() instead")
    void getDagRunSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDagRunSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDagRunsSignalErrorFull() instead")
    void getDagRunsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDagRunsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDagRunsBatchSignalErrorFull() instead")
    void getDagRunsBatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDagRunsBatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUpstreamDatasetEventsSignalErrorFull() instead")
    void getUpstreamDatasetEventsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUpstreamDatasetEventsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDagRunSignalErrorFull() instead")
    void postDagRunSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDagRunSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setDagRunNoteSignalErrorFull() instead")
    void setDagRunNoteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setDagRunNoteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDagRunStateSignalErrorFull() instead")
    void updateDagRunStateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDagRunStateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
