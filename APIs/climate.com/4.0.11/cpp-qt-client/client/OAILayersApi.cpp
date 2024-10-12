/**
 * Climate FieldView Platform APIs
 * **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at `https://platform.climate.com` (e.g. `https://platform.climate.com/v4/fields`).  * The authorization token endpoint is located at `https://api.climate.com/api/oauth/token`.  ## Troubleshooting  `X-Http-Request-Id` response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the `X-Http-Request-Id` header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your `x-api-key` is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a `429` response code is returned. Optionally, the [`Retry-After`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 32     {\"message\":\"Too Many Requests\"}  2. Quota exhausted: <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 29      {\"message\":\"Limit Exceeded\"}  ## Pagination  Pagination is performed via headers. Any request which returns a `\"results\"` array may be paginated. The following figure shows how query results are laid out with X-Limit=4 and no filter applied.  <img style=\"width:70%;height:auto;\" src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\">  * If there are no results, a response code of `304` will be returned.  * If the response is the last set of results, a response code of `200` or `206` will be returned.  * If there are more results, a response code of `206` will be returned.  * If `X-Next-Token` is provided in the request headers but the token has expired, a response code of `409` will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the `X-Limit` header. Valid values are `1-100` and defaults to `100`.  #### X-Next-Token  If the results are paginated, a response header of `X-Next-Token` will be returned. Use the associated value in the subsequent request (via the `X-Next-Token` request header) to retrieve the next page. The following sequence diagram shows how to use `X-Next-Token` to fetch all the records.  <img src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\">   ## Chunked Uploads  Uploads larger than `5MiB` (`5242880 bytes`) must be done in `5MiB` chunks (with the exception of the final chunk). Each chunk request MUST contain a `Content-Range` header specifying the portion of the upload, and a `Content-Type` header specifying binary content type (`application/octet-stream`). Range uploads must be contiguous. The maximum upload size is capped at `500MiB` (`524288000 bytes`).  ## Chunked Downloads  Downloads larger than `5MiB` (`5242880 bytes`) must be done in `1-5MiB` chunks (with the exception of the final chunk, which may be less than `1MiB`). Each chunk request MUST contain a `Range` header specifying the requested portion of the download, and an `Accept` header specifying binary and json content types  (`application/octet-stream,application/json`) or all content types (`*_/_*`).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) <br>Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). <br>Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  <br>Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. <br>For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) <br>To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- 
 *
 * The version of the OpenAPI document: 4.0.11
 * Contact: developer@climate.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILayersApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAILayersApi::OAILayersApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAILayersApi::~OAILayersApi() {
}

void OAILayersApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://platform.climate.com/"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("v4LayersAsAppliedActivityIdContentsGet", defaultConf);
    _serverIndices.insert("v4LayersAsAppliedActivityIdContentsGet", 0);
    _serverConfigs.insert("v4LayersAsAppliedGet", defaultConf);
    _serverIndices.insert("v4LayersAsAppliedGet", 0);
    _serverConfigs.insert("v4LayersAsHarvestedActivityIdContentsGet", defaultConf);
    _serverIndices.insert("v4LayersAsHarvestedActivityIdContentsGet", 0);
    _serverConfigs.insert("v4LayersAsHarvestedGet", defaultConf);
    _serverIndices.insert("v4LayersAsHarvestedGet", 0);
    _serverConfigs.insert("v4LayersAsPlantedActivityIdContentsGet", defaultConf);
    _serverIndices.insert("v4LayersAsPlantedActivityIdContentsGet", 0);
    _serverConfigs.insert("v4LayersAsPlantedGet", defaultConf);
    _serverIndices.insert("v4LayersAsPlantedGet", 0);
    _serverConfigs.insert("v4LayersScoutingObservationsGet", defaultConf);
    _serverIndices.insert("v4LayersScoutingObservationsGet", 0);
    _serverConfigs.insert("v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet", defaultConf);
    _serverIndices.insert("v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet", 0);
    _serverConfigs.insert("v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet", defaultConf);
    _serverIndices.insert("v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet", 0);
    _serverConfigs.insert("v4LayersScoutingObservationsScoutingObservationIdGet", defaultConf);
    _serverIndices.insert("v4LayersScoutingObservationsScoutingObservationIdGet", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAILayersApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAILayersApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAILayersApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAILayersApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAILayersApi::setUsername(const QString &username) {
    _username = username;
}

void OAILayersApi::setPassword(const QString &password) {
    _password = password;
}


void OAILayersApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAILayersApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAILayersApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAILayersApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAILayersApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAILayersApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAILayersApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAILayersApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAILayersApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAILayersApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAILayersApi::getParamStylePrefix(const QString &style) {
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

QString OAILayersApi::getParamStyleSuffix(const QString &style) {
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

QString OAILayersApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAILayersApi::v4LayersAsAppliedActivityIdContentsGet(const QString &accept, const QString &activity_id, const QString &range) {
    QString fullPath = QString(_serverConfigs["v4LayersAsAppliedActivityIdContentsGet"][_serverIndices.value("v4LayersAsAppliedActivityIdContentsGet")].URL()+"/v4/layers/asApplied/{activityId}/contents");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    
    {
        QString activity_idPathParam("{");
        activity_idPathParam.append("activityId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "activityId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"activityId"+pathSuffix : pathPrefix;
        fullPath.replace(activity_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(activity_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(range).isEmpty()) {
            input.headers.insert("Range", ::OpenAPI::toStringValue(range));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsAppliedActivityIdContentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("asApplied:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsAppliedActivityIdContentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersAsAppliedActivityIdContentsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIApplicationActivityContents output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersAsAppliedActivityIdContentsGetSignal(output);
        Q_EMIT v4LayersAsAppliedActivityIdContentsGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("asApplied:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersAsAppliedActivityIdContentsGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersAsAppliedActivityIdContentsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersAsAppliedActivityIdContentsGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersAsAppliedActivityIdContentsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::v4LayersAsAppliedGet(const QString &accept, const ::OpenAPI::OptionalParam<QString> &x_next_token, const ::OpenAPI::OptionalParam<qint32> &x_limit, const ::OpenAPI::OptionalParam<QString> &resource_owner_id, const ::OpenAPI::OptionalParam<QDateTime> &occurred_after, const ::OpenAPI::OptionalParam<QDateTime> &occurred_before, const ::OpenAPI::OptionalParam<QDateTime> &updated_after) {
    QString fullPath = QString(_serverConfigs["v4LayersAsAppliedGet"][_serverIndices.value("v4LayersAsAppliedGet")].URL()+"/v4/layers/asApplied");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (resource_owner_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "resourceOwnerId", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("resourceOwnerId")).append(querySuffix).append(QUrl::toPercentEncoding(resource_owner_id.stringValue()));
    }
    if (occurred_after.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "occurredAfter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("occurredAfter")).append(querySuffix).append(QUrl::toPercentEncoding(occurred_after.stringValue()));
    }
    if (occurred_before.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "occurredBefore", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("occurredBefore")).append(querySuffix).append(QUrl::toPercentEncoding(occurred_before.stringValue()));
    }
    if (updated_after.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "updatedAfter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("updatedAfter")).append(querySuffix).append(QUrl::toPercentEncoding(updated_after.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    if (x_next_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_next_token.value()).isEmpty()) {
            input.headers.insert("X-Next-Token", ::OpenAPI::toStringValue(x_next_token.value()));
        }
        }
    if (x_limit.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_limit.value()).isEmpty()) {
            input.headers.insert("X-Limit", ::OpenAPI::toStringValue(x_limit.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsAppliedGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("platform");
    scope.append("asApplied:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsAppliedGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersAsAppliedGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIApplicationActivities output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersAsAppliedGetSignal(output);
        Q_EMIT v4LayersAsAppliedGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("platform");
        scope.append("asApplied:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersAsAppliedGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersAsAppliedGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersAsAppliedGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersAsAppliedGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::v4LayersAsHarvestedActivityIdContentsGet(const QString &accept, const QString &activity_id, const QString &range) {
    QString fullPath = QString(_serverConfigs["v4LayersAsHarvestedActivityIdContentsGet"][_serverIndices.value("v4LayersAsHarvestedActivityIdContentsGet")].URL()+"/v4/layers/asHarvested/{activityId}/contents");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    
    {
        QString activity_idPathParam("{");
        activity_idPathParam.append("activityId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "activityId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"activityId"+pathSuffix : pathPrefix;
        fullPath.replace(activity_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(activity_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(range).isEmpty()) {
            input.headers.insert("Range", ::OpenAPI::toStringValue(range));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsHarvestedActivityIdContentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("asHarvested:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsHarvestedActivityIdContentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersAsHarvestedActivityIdContentsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIHarvestActivityContents output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersAsHarvestedActivityIdContentsGetSignal(output);
        Q_EMIT v4LayersAsHarvestedActivityIdContentsGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("asHarvested:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersAsHarvestedActivityIdContentsGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersAsHarvestedActivityIdContentsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersAsHarvestedActivityIdContentsGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersAsHarvestedActivityIdContentsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::v4LayersAsHarvestedGet(const QString &accept, const ::OpenAPI::OptionalParam<QString> &x_next_token, const ::OpenAPI::OptionalParam<qint32> &x_limit, const ::OpenAPI::OptionalParam<QString> &resource_owner_id, const ::OpenAPI::OptionalParam<QDateTime> &occurred_after, const ::OpenAPI::OptionalParam<QDateTime> &occurred_before, const ::OpenAPI::OptionalParam<QDateTime> &updated_after) {
    QString fullPath = QString(_serverConfigs["v4LayersAsHarvestedGet"][_serverIndices.value("v4LayersAsHarvestedGet")].URL()+"/v4/layers/asHarvested");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (resource_owner_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "resourceOwnerId", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("resourceOwnerId")).append(querySuffix).append(QUrl::toPercentEncoding(resource_owner_id.stringValue()));
    }
    if (occurred_after.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "occurredAfter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("occurredAfter")).append(querySuffix).append(QUrl::toPercentEncoding(occurred_after.stringValue()));
    }
    if (occurred_before.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "occurredBefore", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("occurredBefore")).append(querySuffix).append(QUrl::toPercentEncoding(occurred_before.stringValue()));
    }
    if (updated_after.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "updatedAfter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("updatedAfter")).append(querySuffix).append(QUrl::toPercentEncoding(updated_after.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    if (x_next_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_next_token.value()).isEmpty()) {
            input.headers.insert("X-Next-Token", ::OpenAPI::toStringValue(x_next_token.value()));
        }
        }
    if (x_limit.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_limit.value()).isEmpty()) {
            input.headers.insert("X-Limit", ::OpenAPI::toStringValue(x_limit.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsHarvestedGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("platform");
    scope.append("asHarvested:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsHarvestedGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersAsHarvestedGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIHarvestActivities output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersAsHarvestedGetSignal(output);
        Q_EMIT v4LayersAsHarvestedGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("platform");
        scope.append("asHarvested:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersAsHarvestedGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersAsHarvestedGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersAsHarvestedGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersAsHarvestedGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::v4LayersAsPlantedActivityIdContentsGet(const QString &accept, const QString &activity_id, const QString &range) {
    QString fullPath = QString(_serverConfigs["v4LayersAsPlantedActivityIdContentsGet"][_serverIndices.value("v4LayersAsPlantedActivityIdContentsGet")].URL()+"/v4/layers/asPlanted/{activityId}/contents");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    
    {
        QString activity_idPathParam("{");
        activity_idPathParam.append("activityId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "activityId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"activityId"+pathSuffix : pathPrefix;
        fullPath.replace(activity_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(activity_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(range).isEmpty()) {
            input.headers.insert("Range", ::OpenAPI::toStringValue(range));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsPlantedActivityIdContentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("asPlanted:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsPlantedActivityIdContentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersAsPlantedActivityIdContentsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPlantingActivityContents output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersAsPlantedActivityIdContentsGetSignal(output);
        Q_EMIT v4LayersAsPlantedActivityIdContentsGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("asPlanted:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersAsPlantedActivityIdContentsGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersAsPlantedActivityIdContentsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersAsPlantedActivityIdContentsGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersAsPlantedActivityIdContentsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::v4LayersAsPlantedGet(const QString &accept, const ::OpenAPI::OptionalParam<QString> &x_next_token, const ::OpenAPI::OptionalParam<qint32> &x_limit, const ::OpenAPI::OptionalParam<QString> &resource_owner_id, const ::OpenAPI::OptionalParam<QDateTime> &occurred_after, const ::OpenAPI::OptionalParam<QDateTime> &occurred_before, const ::OpenAPI::OptionalParam<QDateTime> &updated_after) {
    QString fullPath = QString(_serverConfigs["v4LayersAsPlantedGet"][_serverIndices.value("v4LayersAsPlantedGet")].URL()+"/v4/layers/asPlanted");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (resource_owner_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "resourceOwnerId", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("resourceOwnerId")).append(querySuffix).append(QUrl::toPercentEncoding(resource_owner_id.stringValue()));
    }
    if (occurred_after.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "occurredAfter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("occurredAfter")).append(querySuffix).append(QUrl::toPercentEncoding(occurred_after.stringValue()));
    }
    if (occurred_before.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "occurredBefore", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("occurredBefore")).append(querySuffix).append(QUrl::toPercentEncoding(occurred_before.stringValue()));
    }
    if (updated_after.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "updatedAfter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("updatedAfter")).append(querySuffix).append(QUrl::toPercentEncoding(updated_after.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    if (x_next_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_next_token.value()).isEmpty()) {
            input.headers.insert("X-Next-Token", ::OpenAPI::toStringValue(x_next_token.value()));
        }
        }
    if (x_limit.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_limit.value()).isEmpty()) {
            input.headers.insert("X-Limit", ::OpenAPI::toStringValue(x_limit.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsPlantedGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("platform");
    scope.append("asPlanted:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersAsPlantedGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersAsPlantedGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPlantingActivities output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersAsPlantedGetSignal(output);
        Q_EMIT v4LayersAsPlantedGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("platform");
        scope.append("asPlanted:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersAsPlantedGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersAsPlantedGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersAsPlantedGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersAsPlantedGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::v4LayersScoutingObservationsGet(const ::OpenAPI::OptionalParam<QString> &x_next_token, const ::OpenAPI::OptionalParam<qint32> &x_limit, const ::OpenAPI::OptionalParam<QDateTime> &occurred_after, const ::OpenAPI::OptionalParam<QDateTime> &occurred_before) {
    QString fullPath = QString(_serverConfigs["v4LayersScoutingObservationsGet"][_serverIndices.value("v4LayersScoutingObservationsGet")].URL()+"/v4/layers/scoutingObservations");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (occurred_after.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "occurredAfter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("occurredAfter")).append(querySuffix).append(QUrl::toPercentEncoding(occurred_after.stringValue()));
    }
    if (occurred_before.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "occurredBefore", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("occurredBefore")).append(querySuffix).append(QUrl::toPercentEncoding(occurred_before.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_next_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_next_token.value()).isEmpty()) {
            input.headers.insert("X-Next-Token", ::OpenAPI::toStringValue(x_next_token.value()));
        }
        }
    if (x_limit.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_limit.value()).isEmpty()) {
            input.headers.insert("X-Limit", ::OpenAPI::toStringValue(x_limit.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersScoutingObservationsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("platform");
    scope.append("scouting:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersScoutingObservationsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersScoutingObservationsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIScoutingObservations output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersScoutingObservationsGetSignal(output);
        Q_EMIT v4LayersScoutingObservationsGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("platform");
        scope.append("scouting:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersScoutingObservationsGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersScoutingObservationsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersScoutingObservationsGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersScoutingObservationsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(const QString &accept, const QString &scouting_observation_id, const QString &attachment_id, const QString &range) {
    QString fullPath = QString(_serverConfigs["v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet"][_serverIndices.value("v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet")].URL()+"/v4/layers/scoutingObservations/{scoutingObservationId}/attachments/{attachmentId}/contents");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    
    {
        QString scouting_observation_idPathParam("{");
        scouting_observation_idPathParam.append("scoutingObservationId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "scoutingObservationId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"scoutingObservationId"+pathSuffix : pathPrefix;
        fullPath.replace(scouting_observation_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(scouting_observation_id)));
    }
    
    {
        QString attachment_idPathParam("{");
        attachment_idPathParam.append("attachmentId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "attachmentId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"attachmentId"+pathSuffix : pathPrefix;
        fullPath.replace(attachment_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(attachment_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(range).isEmpty()) {
            input.headers.insert("Range", ::OpenAPI::toStringValue(range));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("platform");
    scope.append("scouting:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIScoutingObservationAttachmentContents output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignal(output);
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("platform");
        scope.append("scouting:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet(const QString &scouting_observation_id, const ::OpenAPI::OptionalParam<QString> &x_next_token, const ::OpenAPI::OptionalParam<qint32> &x_limit) {
    QString fullPath = QString(_serverConfigs["v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet"][_serverIndices.value("v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet")].URL()+"/v4/layers/scoutingObservations/{scoutingObservationId}/attachments");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    
    {
        QString scouting_observation_idPathParam("{");
        scouting_observation_idPathParam.append("scoutingObservationId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "scoutingObservationId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"scoutingObservationId"+pathSuffix : pathPrefix;
        fullPath.replace(scouting_observation_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(scouting_observation_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_next_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_next_token.value()).isEmpty()) {
            input.headers.insert("X-Next-Token", ::OpenAPI::toStringValue(x_next_token.value()));
        }
        }
    if (x_limit.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_limit.value()).isEmpty()) {
            input.headers.insert("X-Limit", ::OpenAPI::toStringValue(x_limit.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("platform");
    scope.append("scouting:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIScoutingObservationAttachments output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignal(output);
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("platform");
        scope.append("scouting:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdGet(const QString &scouting_observation_id) {
    QString fullPath = QString(_serverConfigs["v4LayersScoutingObservationsScoutingObservationIdGet"][_serverIndices.value("v4LayersScoutingObservationsScoutingObservationIdGet")].URL()+"/v4/layers/scoutingObservations/{scoutingObservationId}");
    
    if (_apiKeys.contains("api_key")) {
        addHeaders("api_key",_apiKeys.find("api_key").value());
    }
    
    
    {
        QString scouting_observation_idPathParam("{");
        scouting_observation_idPathParam.append("scoutingObservationId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "scoutingObservationId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"scoutingObservationId"+pathSuffix : pathPrefix;
        fullPath.replace(scouting_observation_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(scouting_observation_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("platform");
    scope.append("scouting:read");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdGetCallback);
    connect(this, &OAILayersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAILayersApi::v4LayersScoutingObservationsScoutingObservationIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIScoutingObservation output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdGetSignal(output);
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("platform");
        scope.append("scouting:read");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://climate.com/static/app-login/");
        QString tokenUrl("https://api.climate.com/api/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdGetSignalE(output, error_type, error_str);
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdGetSignalError(output, error_type, error_str);
        Q_EMIT v4LayersScoutingObservationsScoutingObservationIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILayersApi::tokenAvailable(){

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
