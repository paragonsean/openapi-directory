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

#include "OAITaskInstanceApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAITaskInstanceApi::OAITaskInstanceApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAITaskInstanceApi::~OAITaskInstanceApi() {
}

void OAITaskInstanceApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("/api/v1"),
    "Apache Airflow Stable API.",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://apache.local"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("getExtraLinks", defaultConf);
    _serverIndices.insert("getExtraLinks", 0);
    _serverConfigs.insert("getLog", defaultConf);
    _serverIndices.insert("getLog", 0);
    _serverConfigs.insert("getMappedTaskInstance", defaultConf);
    _serverIndices.insert("getMappedTaskInstance", 0);
    _serverConfigs.insert("getMappedTaskInstances", defaultConf);
    _serverIndices.insert("getMappedTaskInstances", 0);
    _serverConfigs.insert("getTaskInstance", defaultConf);
    _serverIndices.insert("getTaskInstance", 0);
    _serverConfigs.insert("getTaskInstances", defaultConf);
    _serverIndices.insert("getTaskInstances", 0);
    _serverConfigs.insert("getTaskInstancesBatch", defaultConf);
    _serverIndices.insert("getTaskInstancesBatch", 0);
    _serverConfigs.insert("patchMappedTaskInstance", defaultConf);
    _serverIndices.insert("patchMappedTaskInstance", 0);
    _serverConfigs.insert("patchTaskInstance", defaultConf);
    _serverIndices.insert("patchTaskInstance", 0);
    _serverConfigs.insert("setMappedTaskInstanceNote", defaultConf);
    _serverIndices.insert("setMappedTaskInstanceNote", 0);
    _serverConfigs.insert("setTaskInstanceNote", defaultConf);
    _serverIndices.insert("setTaskInstanceNote", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAITaskInstanceApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAITaskInstanceApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAITaskInstanceApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAITaskInstanceApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAITaskInstanceApi::setUsername(const QString &username) {
    _username = username;
}

void OAITaskInstanceApi::setPassword(const QString &password) {
    _password = password;
}


void OAITaskInstanceApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAITaskInstanceApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAITaskInstanceApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
    _manager = manager;
}

/**
    * Appends a new ServerConfiguration to the config map for a specific operation.
    * @param operation The id to the target operation.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    * returns the index of the new server config on success and -1 if the operation is not found
    */
int OAITaskInstanceApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    if (_serverConfigs.contains(operation)) {
        _serverConfigs[operation].append(OAIServerConfiguration(
                    url,
                    description,
                    variables));
        return _serverConfigs[operation].size()-1;
    } else {
        return -1;
    }
}

/**
    * Appends a new ServerConfiguration to the config map for a all operations and sets the index to that server.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAITaskInstanceApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    for (auto keyIt = _serverIndices.keyBegin(); keyIt != _serverIndices.keyEnd(); keyIt++) {
        setServerIndex(*keyIt, addServerConfiguration(*keyIt, url, description, variables));
    }
}

/**
    * Appends a new ServerConfiguration to the config map for an operations and sets the index to that server.
    * @param URL A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAITaskInstanceApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAITaskInstanceApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAITaskInstanceApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAITaskInstanceApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAITaskInstanceApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAITaskInstanceApi::getParamStylePrefix(const QString &style) {
    if (style == "matrix") {
        return ";";
    } else if (style == "label") {
        return ".";
    } else if (style == "form") {
        return "&";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "&";
    } else if (style == "pipeDelimited") {
        return "&";
    } else {
        return "none";
    }
}

QString OAITaskInstanceApi::getParamStyleSuffix(const QString &style) {
    if (style == "matrix") {
        return "=";
    } else if (style == "label") {
        return "";
    } else if (style == "form") {
        return "=";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "=";
    } else if (style == "pipeDelimited") {
        return "=";
    } else {
        return "none";
    }
}

QString OAITaskInstanceApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

    if (style == "matrix") {
        return (isExplode) ? ";" + name + "=" : ",";

    } else if (style == "label") {
        return (isExplode) ? "." : ",";

    } else if (style == "form") {
        return (isExplode) ? "&" + name + "=" : ",";

    } else if (style == "simple") {
        return ",";
    } else if (style == "spaceDelimited") {
        return (isExplode) ? "&" + name + "=" : " ";

    } else if (style == "pipeDelimited") {
        return (isExplode) ? "&" + name + "=" : "|";

    } else if (style == "deepObject") {
        return (isExplode) ? "&" : "none";

    } else {
        return "none";
    }
}

void OAITaskInstanceApi::getExtraLinks(const QString &dag_id, const QString &dag_run_id, const QString &task_id) {
    QString fullPath = QString(_serverConfigs["getExtraLinks"][_serverIndices.value("getExtraLinks")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    
    {
        QString task_idPathParam("{");
        task_idPathParam.append("task_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_id"+pathSuffix : pathPrefix;
        fullPath.replace(task_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::getExtraLinksCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::getExtraLinksCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIExtraLinkCollection output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getExtraLinksSignal(output);
        Q_EMIT getExtraLinksSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getExtraLinksSignalE(output, error_type, error_str);
        Q_EMIT getExtraLinksSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getExtraLinksSignalError(output, error_type, error_str);
        Q_EMIT getExtraLinksSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::getLog(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const qint32 &task_try_number, const ::OpenAPI::OptionalParam<bool> &full_content, const ::OpenAPI::OptionalParam<qint32> &map_index, const ::OpenAPI::OptionalParam<QString> &token) {
    QString fullPath = QString(_serverConfigs["getLog"][_serverIndices.value("getLog")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number}");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    
    {
        QString task_idPathParam("{");
        task_idPathParam.append("task_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_id"+pathSuffix : pathPrefix;
        fullPath.replace(task_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_id)));
    }
    
    {
        QString task_try_numberPathParam("{");
        task_try_numberPathParam.append("task_try_number").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_try_number", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_try_number"+pathSuffix : pathPrefix;
        fullPath.replace(task_try_numberPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_try_number)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (full_content.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "full_content", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("full_content")).append(querySuffix).append(QUrl::toPercentEncoding(full_content.stringValue()));
    }
    if (map_index.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "map_index", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("map_index")).append(querySuffix).append(QUrl::toPercentEncoding(map_index.stringValue()));
    }
    if (token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "token", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("token")).append(querySuffix).append(QUrl::toPercentEncoding(token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::getLogCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::getLogCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGet_log_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getLogSignal(output);
        Q_EMIT getLogSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getLogSignalE(output, error_type, error_str);
        Q_EMIT getLogSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getLogSignalError(output, error_type, error_str);
        Q_EMIT getLogSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::getMappedTaskInstance(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const qint32 &map_index) {
    QString fullPath = QString(_serverConfigs["getMappedTaskInstance"][_serverIndices.value("getMappedTaskInstance")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    
    {
        QString task_idPathParam("{");
        task_idPathParam.append("task_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_id"+pathSuffix : pathPrefix;
        fullPath.replace(task_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_id)));
    }
    
    {
        QString map_indexPathParam("{");
        map_indexPathParam.append("map_index").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "map_index", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"map_index"+pathSuffix : pathPrefix;
        fullPath.replace(map_indexPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(map_index)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::getMappedTaskInstanceCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::getMappedTaskInstanceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITaskInstance output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getMappedTaskInstanceSignal(output);
        Q_EMIT getMappedTaskInstanceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getMappedTaskInstanceSignalE(output, error_type, error_str);
        Q_EMIT getMappedTaskInstanceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getMappedTaskInstanceSignalError(output, error_type, error_str);
        Q_EMIT getMappedTaskInstanceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::getMappedTaskInstances(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const ::OpenAPI::OptionalParam<qint32> &limit, const ::OpenAPI::OptionalParam<qint32> &offset, const ::OpenAPI::OptionalParam<QDateTime> &execution_date_gte, const ::OpenAPI::OptionalParam<QDateTime> &execution_date_lte, const ::OpenAPI::OptionalParam<QDateTime> &start_date_gte, const ::OpenAPI::OptionalParam<QDateTime> &start_date_lte, const ::OpenAPI::OptionalParam<QDateTime> &end_date_gte, const ::OpenAPI::OptionalParam<QDateTime> &end_date_lte, const ::OpenAPI::OptionalParam<double> &duration_gte, const ::OpenAPI::OptionalParam<double> &duration_lte, const ::OpenAPI::OptionalParam<QList<QString>> &state, const ::OpenAPI::OptionalParam<QList<QString>> &pool, const ::OpenAPI::OptionalParam<QList<QString>> &queue, const ::OpenAPI::OptionalParam<QString> &order_by) {
    QString fullPath = QString(_serverConfigs["getMappedTaskInstances"][_serverIndices.value("getMappedTaskInstances")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    
    {
        QString task_idPathParam("{");
        task_idPathParam.append("task_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_id"+pathSuffix : pathPrefix;
        fullPath.replace(task_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (limit.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "limit", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("limit")).append(querySuffix).append(QUrl::toPercentEncoding(limit.stringValue()));
    }
    if (offset.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "offset", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("offset")).append(querySuffix).append(QUrl::toPercentEncoding(offset.stringValue()));
    }
    if (execution_date_gte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "execution_date_gte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("execution_date_gte")).append(querySuffix).append(QUrl::toPercentEncoding(execution_date_gte.stringValue()));
    }
    if (execution_date_lte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "execution_date_lte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("execution_date_lte")).append(querySuffix).append(QUrl::toPercentEncoding(execution_date_lte.stringValue()));
    }
    if (start_date_gte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start_date_gte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start_date_gte")).append(querySuffix).append(QUrl::toPercentEncoding(start_date_gte.stringValue()));
    }
    if (start_date_lte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start_date_lte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start_date_lte")).append(querySuffix).append(QUrl::toPercentEncoding(start_date_lte.stringValue()));
    }
    if (end_date_gte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "end_date_gte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("end_date_gte")).append(querySuffix).append(QUrl::toPercentEncoding(end_date_gte.stringValue()));
    }
    if (end_date_lte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "end_date_lte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("end_date_lte")).append(querySuffix).append(QUrl::toPercentEncoding(end_date_lte.stringValue()));
    }
    if (duration_gte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "duration_gte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("duration_gte")).append(querySuffix).append(QUrl::toPercentEncoding(duration_gte.stringValue()));
    }
    if (duration_lte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "duration_lte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("duration_lte")).append(querySuffix).append(QUrl::toPercentEncoding(duration_lte.stringValue()));
    }
    if (state.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "state", true);
        if (state.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : state.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("state=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (pool.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "pool", true);
        if (pool.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : pool.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("pool=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (queue.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "queue", true);
        if (queue.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : queue.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("queue=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (order_by.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "order_by", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("order_by")).append(querySuffix).append(QUrl::toPercentEncoding(order_by.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::getMappedTaskInstancesCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::getMappedTaskInstancesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITaskInstanceCollection output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getMappedTaskInstancesSignal(output);
        Q_EMIT getMappedTaskInstancesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getMappedTaskInstancesSignalE(output, error_type, error_str);
        Q_EMIT getMappedTaskInstancesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getMappedTaskInstancesSignalError(output, error_type, error_str);
        Q_EMIT getMappedTaskInstancesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::getTaskInstance(const QString &dag_id, const QString &dag_run_id, const QString &task_id) {
    QString fullPath = QString(_serverConfigs["getTaskInstance"][_serverIndices.value("getTaskInstance")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    
    {
        QString task_idPathParam("{");
        task_idPathParam.append("task_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_id"+pathSuffix : pathPrefix;
        fullPath.replace(task_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::getTaskInstanceCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::getTaskInstanceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITaskInstance output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTaskInstanceSignal(output);
        Q_EMIT getTaskInstanceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getTaskInstanceSignalE(output, error_type, error_str);
        Q_EMIT getTaskInstanceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTaskInstanceSignalError(output, error_type, error_str);
        Q_EMIT getTaskInstanceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::getTaskInstances(const QString &dag_id, const QString &dag_run_id, const ::OpenAPI::OptionalParam<QDateTime> &execution_date_gte, const ::OpenAPI::OptionalParam<QDateTime> &execution_date_lte, const ::OpenAPI::OptionalParam<QDateTime> &start_date_gte, const ::OpenAPI::OptionalParam<QDateTime> &start_date_lte, const ::OpenAPI::OptionalParam<QDateTime> &end_date_gte, const ::OpenAPI::OptionalParam<QDateTime> &end_date_lte, const ::OpenAPI::OptionalParam<double> &duration_gte, const ::OpenAPI::OptionalParam<double> &duration_lte, const ::OpenAPI::OptionalParam<QList<QString>> &state, const ::OpenAPI::OptionalParam<QList<QString>> &pool, const ::OpenAPI::OptionalParam<QList<QString>> &queue, const ::OpenAPI::OptionalParam<qint32> &limit, const ::OpenAPI::OptionalParam<qint32> &offset) {
    QString fullPath = QString(_serverConfigs["getTaskInstances"][_serverIndices.value("getTaskInstances")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (execution_date_gte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "execution_date_gte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("execution_date_gte")).append(querySuffix).append(QUrl::toPercentEncoding(execution_date_gte.stringValue()));
    }
    if (execution_date_lte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "execution_date_lte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("execution_date_lte")).append(querySuffix).append(QUrl::toPercentEncoding(execution_date_lte.stringValue()));
    }
    if (start_date_gte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start_date_gte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start_date_gte")).append(querySuffix).append(QUrl::toPercentEncoding(start_date_gte.stringValue()));
    }
    if (start_date_lte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start_date_lte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start_date_lte")).append(querySuffix).append(QUrl::toPercentEncoding(start_date_lte.stringValue()));
    }
    if (end_date_gte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "end_date_gte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("end_date_gte")).append(querySuffix).append(QUrl::toPercentEncoding(end_date_gte.stringValue()));
    }
    if (end_date_lte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "end_date_lte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("end_date_lte")).append(querySuffix).append(QUrl::toPercentEncoding(end_date_lte.stringValue()));
    }
    if (duration_gte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "duration_gte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("duration_gte")).append(querySuffix).append(QUrl::toPercentEncoding(duration_gte.stringValue()));
    }
    if (duration_lte.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "duration_lte", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("duration_lte")).append(querySuffix).append(QUrl::toPercentEncoding(duration_lte.stringValue()));
    }
    if (state.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "state", true);
        if (state.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : state.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("state=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("state").append(querySuffix);
                qint32 count = 0;
                for (QString t : state.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (pool.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "pool", true);
        if (pool.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : pool.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("pool=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("pool").append(querySuffix);
                qint32 count = 0;
                for (QString t : pool.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (queue.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "queue", true);
        if (queue.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : queue.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("queue=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("queue").append(querySuffix);
                qint32 count = 0;
                for (QString t : queue.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (limit.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "limit", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("limit")).append(querySuffix).append(QUrl::toPercentEncoding(limit.stringValue()));
    }
    if (offset.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "offset", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("offset")).append(querySuffix).append(QUrl::toPercentEncoding(offset.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::getTaskInstancesCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::getTaskInstancesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITaskInstanceCollection output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTaskInstancesSignal(output);
        Q_EMIT getTaskInstancesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getTaskInstancesSignalE(output, error_type, error_str);
        Q_EMIT getTaskInstancesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTaskInstancesSignalError(output, error_type, error_str);
        Q_EMIT getTaskInstancesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::getTaskInstancesBatch(const OAIListTaskInstanceForm &oai_list_task_instance_form) {
    QString fullPath = QString(_serverConfigs["getTaskInstancesBatch"][_serverIndices.value("getTaskInstancesBatch")].URL()+"/dags/~/dagRuns/~/taskInstances/list");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_list_task_instance_form.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::getTaskInstancesBatchCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::getTaskInstancesBatchCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITaskInstanceCollection output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTaskInstancesBatchSignal(output);
        Q_EMIT getTaskInstancesBatchSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getTaskInstancesBatchSignalE(output, error_type, error_str);
        Q_EMIT getTaskInstancesBatchSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTaskInstancesBatchSignalError(output, error_type, error_str);
        Q_EMIT getTaskInstancesBatchSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::patchMappedTaskInstance(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const qint32 &map_index, const ::OpenAPI::OptionalParam<OAIUpdateTaskInstance> &oai_update_task_instance) {
    QString fullPath = QString(_serverConfigs["patchMappedTaskInstance"][_serverIndices.value("patchMappedTaskInstance")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    
    {
        QString task_idPathParam("{");
        task_idPathParam.append("task_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_id"+pathSuffix : pathPrefix;
        fullPath.replace(task_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_id)));
    }
    
    {
        QString map_indexPathParam("{");
        map_indexPathParam.append("map_index").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "map_index", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"map_index"+pathSuffix : pathPrefix;
        fullPath.replace(map_indexPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(map_index)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PATCH");

    if (oai_update_task_instance.hasValue()){

        
        QByteArray output = oai_update_task_instance.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::patchMappedTaskInstanceCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::patchMappedTaskInstanceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITaskInstanceReference output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT patchMappedTaskInstanceSignal(output);
        Q_EMIT patchMappedTaskInstanceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT patchMappedTaskInstanceSignalE(output, error_type, error_str);
        Q_EMIT patchMappedTaskInstanceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT patchMappedTaskInstanceSignalError(output, error_type, error_str);
        Q_EMIT patchMappedTaskInstanceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::patchTaskInstance(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const OAIUpdateTaskInstance &oai_update_task_instance) {
    QString fullPath = QString(_serverConfigs["patchTaskInstance"][_serverIndices.value("patchTaskInstance")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    
    {
        QString task_idPathParam("{");
        task_idPathParam.append("task_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_id"+pathSuffix : pathPrefix;
        fullPath.replace(task_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PATCH");

    {

        
        QByteArray output = oai_update_task_instance.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::patchTaskInstanceCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::patchTaskInstanceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITaskInstanceReference output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT patchTaskInstanceSignal(output);
        Q_EMIT patchTaskInstanceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT patchTaskInstanceSignalE(output, error_type, error_str);
        Q_EMIT patchTaskInstanceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT patchTaskInstanceSignalError(output, error_type, error_str);
        Q_EMIT patchTaskInstanceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::setMappedTaskInstanceNote(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const qint32 &map_index, const OAISetTaskInstanceNote &oai_set_task_instance_note) {
    QString fullPath = QString(_serverConfigs["setMappedTaskInstanceNote"][_serverIndices.value("setMappedTaskInstanceNote")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/setNote");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    
    {
        QString task_idPathParam("{");
        task_idPathParam.append("task_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_id"+pathSuffix : pathPrefix;
        fullPath.replace(task_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_id)));
    }
    
    {
        QString map_indexPathParam("{");
        map_indexPathParam.append("map_index").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "map_index", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"map_index"+pathSuffix : pathPrefix;
        fullPath.replace(map_indexPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(map_index)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PATCH");

    {

        
        QByteArray output = oai_set_task_instance_note.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::setMappedTaskInstanceNoteCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::setMappedTaskInstanceNoteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITaskInstance output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT setMappedTaskInstanceNoteSignal(output);
        Q_EMIT setMappedTaskInstanceNoteSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT setMappedTaskInstanceNoteSignalE(output, error_type, error_str);
        Q_EMIT setMappedTaskInstanceNoteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT setMappedTaskInstanceNoteSignalError(output, error_type, error_str);
        Q_EMIT setMappedTaskInstanceNoteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::setTaskInstanceNote(const QString &dag_id, const QString &dag_run_id, const QString &task_id, const OAISetTaskInstanceNote &oai_set_task_instance_note) {
    QString fullPath = QString(_serverConfigs["setTaskInstanceNote"][_serverIndices.value("setTaskInstanceNote")].URL()+"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/setNote");
    
    
    {
        QString dag_idPathParam("{");
        dag_idPathParam.append("dag_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_id)));
    }
    
    {
        QString dag_run_idPathParam("{");
        dag_run_idPathParam.append("dag_run_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "dag_run_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"dag_run_id"+pathSuffix : pathPrefix;
        fullPath.replace(dag_run_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dag_run_id)));
    }
    
    {
        QString task_idPathParam("{");
        task_idPathParam.append("task_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "task_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"task_id"+pathSuffix : pathPrefix;
        fullPath.replace(task_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(task_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PATCH");

    {

        
        QByteArray output = oai_set_task_instance_note.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITaskInstanceApi::setTaskInstanceNoteCallback);
    connect(this, &OAITaskInstanceApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITaskInstanceApi::setTaskInstanceNoteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITaskInstance output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT setTaskInstanceNoteSignal(output);
        Q_EMIT setTaskInstanceNoteSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT setTaskInstanceNoteSignalE(output, error_type, error_str);
        Q_EMIT setTaskInstanceNoteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT setTaskInstanceNoteSignalError(output, error_type, error_str);
        Q_EMIT setTaskInstanceNoteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITaskInstanceApi::tokenAvailable(){

    oauthToken token;
    switch (_OauthMethod) {
    case 1: //implicit flow
        token = _implicitFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _implicitFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 2: //authorization flow
        token = _authFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _authFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 3: //client credentials flow
        token = _credentialFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 4: //resource owner password flow
        token = _passwordFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    default:
        qDebug() << "No Oauth method set!";
        break;
    }
}
} // namespace OpenAPI
