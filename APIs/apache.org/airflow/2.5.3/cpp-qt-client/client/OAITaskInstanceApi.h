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

#ifndef OAI_OAITaskInstanceApi_H
#define OAI_OAITaskInstanceApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError.h"
#include "OAIExtraLinkCollection.h"
#include "OAIGet_log_200_response.h"
#include "OAIListTaskInstanceForm.h"
#include "OAISetTaskInstanceNote.h"
#include "OAITaskInstance.h"
#include "OAITaskInstanceCollection.h"
#include "OAITaskInstanceReference.h"
#include "OAIUpdateTaskInstance.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITaskInstanceApi : public QObject {
    Q_OBJECT

public:
    OAITaskInstanceApi(const int timeOut = 0);
    ~OAITaskInstanceApi();

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
    * @param[in]  task_id QString [required]
    */
    virtual void getExtraLinks(const QString &dag_id, const QString &dag_run_id, const QString &task_id);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  task_id QString [required]
    * @param[in]  task_try_number qint32 [required]
    * @param[in]  full_content bool [optional]
    * @param[in]  map_index qint32 [optional]
    * @param[in]  token QString [optional]
    */
    virtual void getLog(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const qint32 &task_try_number, const ::OpenAPI::OptionalParam<bool> &full_content = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &map_index = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  task_id QString [required]
    * @param[in]  map_index qint32 [required]
    */
    virtual void getMappedTaskInstance(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const qint32 &map_index);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  task_id QString [required]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  execution_date_gte QDateTime [optional]
    * @param[in]  execution_date_lte QDateTime [optional]
    * @param[in]  start_date_gte QDateTime [optional]
    * @param[in]  start_date_lte QDateTime [optional]
    * @param[in]  end_date_gte QDateTime [optional]
    * @param[in]  end_date_lte QDateTime [optional]
    * @param[in]  duration_gte double [optional]
    * @param[in]  duration_lte double [optional]
    * @param[in]  state QList<QString> [optional]
    * @param[in]  pool QList<QString> [optional]
    * @param[in]  queue QList<QString> [optional]
    * @param[in]  order_by QString [optional]
    */
    virtual void getMappedTaskInstances(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QDateTime> &execution_date_gte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &execution_date_lte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &start_date_gte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &start_date_lte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date_gte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date_lte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<double> &duration_gte = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &duration_lte = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QList<QString>> &state = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &pool = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &queue = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &order_by = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  task_id QString [required]
    */
    virtual void getTaskInstance(const QString &dag_id, const QString &dag_run_id, const QString &task_id);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  execution_date_gte QDateTime [optional]
    * @param[in]  execution_date_lte QDateTime [optional]
    * @param[in]  start_date_gte QDateTime [optional]
    * @param[in]  start_date_lte QDateTime [optional]
    * @param[in]  end_date_gte QDateTime [optional]
    * @param[in]  end_date_lte QDateTime [optional]
    * @param[in]  duration_gte double [optional]
    * @param[in]  duration_lte double [optional]
    * @param[in]  state QList<QString> [optional]
    * @param[in]  pool QList<QString> [optional]
    * @param[in]  queue QList<QString> [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void getTaskInstances(const QString &dag_id, const QString &dag_run_id, const ::OpenAPI::OptionalParam<QDateTime> &execution_date_gte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &execution_date_lte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &start_date_gte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &start_date_lte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date_gte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date_lte = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<double> &duration_gte = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &duration_lte = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QList<QString>> &state = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &pool = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &queue = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  oai_list_task_instance_form OAIListTaskInstanceForm [required]
    */
    virtual void getTaskInstancesBatch(const OAIListTaskInstanceForm &oai_list_task_instance_form);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  task_id QString [required]
    * @param[in]  map_index qint32 [required]
    * @param[in]  oai_update_task_instance OAIUpdateTaskInstance [optional]
    */
    virtual void patchMappedTaskInstance(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const qint32 &map_index, const ::OpenAPI::OptionalParam<OAIUpdateTaskInstance> &oai_update_task_instance = ::OpenAPI::OptionalParam<OAIUpdateTaskInstance>());

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  task_id QString [required]
    * @param[in]  oai_update_task_instance OAIUpdateTaskInstance [required]
    */
    virtual void patchTaskInstance(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const OAIUpdateTaskInstance &oai_update_task_instance);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  task_id QString [required]
    * @param[in]  map_index qint32 [required]
    * @param[in]  oai_set_task_instance_note OAISetTaskInstanceNote [required]
    */
    virtual void setMappedTaskInstanceNote(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const qint32 &map_index, const OAISetTaskInstanceNote &oai_set_task_instance_note);

    /**
    * @param[in]  dag_id QString [required]
    * @param[in]  dag_run_id QString [required]
    * @param[in]  task_id QString [required]
    * @param[in]  oai_set_task_instance_note OAISetTaskInstanceNote [required]
    */
    virtual void setTaskInstanceNote(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const OAISetTaskInstanceNote &oai_set_task_instance_note);


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

    void getExtraLinksCallback(OAIHttpRequestWorker *worker);
    void getLogCallback(OAIHttpRequestWorker *worker);
    void getMappedTaskInstanceCallback(OAIHttpRequestWorker *worker);
    void getMappedTaskInstancesCallback(OAIHttpRequestWorker *worker);
    void getTaskInstanceCallback(OAIHttpRequestWorker *worker);
    void getTaskInstancesCallback(OAIHttpRequestWorker *worker);
    void getTaskInstancesBatchCallback(OAIHttpRequestWorker *worker);
    void patchMappedTaskInstanceCallback(OAIHttpRequestWorker *worker);
    void patchTaskInstanceCallback(OAIHttpRequestWorker *worker);
    void setMappedTaskInstanceNoteCallback(OAIHttpRequestWorker *worker);
    void setTaskInstanceNoteCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getExtraLinksSignal(OAIExtraLinkCollection summary);
    void getLogSignal(OAIGet_log_200_response summary);
    void getMappedTaskInstanceSignal(OAITaskInstance summary);
    void getMappedTaskInstancesSignal(OAITaskInstanceCollection summary);
    void getTaskInstanceSignal(OAITaskInstance summary);
    void getTaskInstancesSignal(OAITaskInstanceCollection summary);
    void getTaskInstancesBatchSignal(OAITaskInstanceCollection summary);
    void patchMappedTaskInstanceSignal(OAITaskInstanceReference summary);
    void patchTaskInstanceSignal(OAITaskInstanceReference summary);
    void setMappedTaskInstanceNoteSignal(OAITaskInstance summary);
    void setTaskInstanceNoteSignal(OAITaskInstance summary);


    void getExtraLinksSignalFull(OAIHttpRequestWorker *worker, OAIExtraLinkCollection summary);
    void getLogSignalFull(OAIHttpRequestWorker *worker, OAIGet_log_200_response summary);
    void getMappedTaskInstanceSignalFull(OAIHttpRequestWorker *worker, OAITaskInstance summary);
    void getMappedTaskInstancesSignalFull(OAIHttpRequestWorker *worker, OAITaskInstanceCollection summary);
    void getTaskInstanceSignalFull(OAIHttpRequestWorker *worker, OAITaskInstance summary);
    void getTaskInstancesSignalFull(OAIHttpRequestWorker *worker, OAITaskInstanceCollection summary);
    void getTaskInstancesBatchSignalFull(OAIHttpRequestWorker *worker, OAITaskInstanceCollection summary);
    void patchMappedTaskInstanceSignalFull(OAIHttpRequestWorker *worker, OAITaskInstanceReference summary);
    void patchTaskInstanceSignalFull(OAIHttpRequestWorker *worker, OAITaskInstanceReference summary);
    void setMappedTaskInstanceNoteSignalFull(OAIHttpRequestWorker *worker, OAITaskInstance summary);
    void setTaskInstanceNoteSignalFull(OAIHttpRequestWorker *worker, OAITaskInstance summary);

    Q_DECL_DEPRECATED_X("Use getExtraLinksSignalError() instead")
    void getExtraLinksSignalE(OAIExtraLinkCollection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getExtraLinksSignalError(OAIExtraLinkCollection summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLogSignalError() instead")
    void getLogSignalE(OAIGet_log_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLogSignalError(OAIGet_log_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMappedTaskInstanceSignalError() instead")
    void getMappedTaskInstanceSignalE(OAITaskInstance summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMappedTaskInstanceSignalError(OAITaskInstance summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMappedTaskInstancesSignalError() instead")
    void getMappedTaskInstancesSignalE(OAITaskInstanceCollection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMappedTaskInstancesSignalError(OAITaskInstanceCollection summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTaskInstanceSignalError() instead")
    void getTaskInstanceSignalE(OAITaskInstance summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTaskInstanceSignalError(OAITaskInstance summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTaskInstancesSignalError() instead")
    void getTaskInstancesSignalE(OAITaskInstanceCollection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTaskInstancesSignalError(OAITaskInstanceCollection summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTaskInstancesBatchSignalError() instead")
    void getTaskInstancesBatchSignalE(OAITaskInstanceCollection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTaskInstancesBatchSignalError(OAITaskInstanceCollection summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchMappedTaskInstanceSignalError() instead")
    void patchMappedTaskInstanceSignalE(OAITaskInstanceReference summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patchMappedTaskInstanceSignalError(OAITaskInstanceReference summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchTaskInstanceSignalError() instead")
    void patchTaskInstanceSignalE(OAITaskInstanceReference summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patchTaskInstanceSignalError(OAITaskInstanceReference summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setMappedTaskInstanceNoteSignalError() instead")
    void setMappedTaskInstanceNoteSignalE(OAITaskInstance summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setMappedTaskInstanceNoteSignalError(OAITaskInstance summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setTaskInstanceNoteSignalError() instead")
    void setTaskInstanceNoteSignalE(OAITaskInstance summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setTaskInstanceNoteSignalError(OAITaskInstance summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getExtraLinksSignalErrorFull() instead")
    void getExtraLinksSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getExtraLinksSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLogSignalErrorFull() instead")
    void getLogSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLogSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMappedTaskInstanceSignalErrorFull() instead")
    void getMappedTaskInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMappedTaskInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMappedTaskInstancesSignalErrorFull() instead")
    void getMappedTaskInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMappedTaskInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTaskInstanceSignalErrorFull() instead")
    void getTaskInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTaskInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTaskInstancesSignalErrorFull() instead")
    void getTaskInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTaskInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTaskInstancesBatchSignalErrorFull() instead")
    void getTaskInstancesBatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTaskInstancesBatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchMappedTaskInstanceSignalErrorFull() instead")
    void patchMappedTaskInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patchMappedTaskInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchTaskInstanceSignalErrorFull() instead")
    void patchTaskInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patchTaskInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setMappedTaskInstanceNoteSignalErrorFull() instead")
    void setMappedTaskInstanceNoteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setMappedTaskInstanceNoteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setTaskInstanceNoteSignalErrorFull() instead")
    void setTaskInstanceNoteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setTaskInstanceNoteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
