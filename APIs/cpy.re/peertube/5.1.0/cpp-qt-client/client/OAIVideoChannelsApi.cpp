/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVideoChannelsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIVideoChannelsApi::OAIVideoChannelsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIVideoChannelsApi::~OAIVideoChannelsApi() {
}

void OAIVideoChannelsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://peertube2.cpy.re"),
    "Live Test Server (live data - latest nightly version)",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://peertube3.cpy.re"),
    "Live Test Server (live data - latest RC version)",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://peertube.cpy.re"),
    "Live Test Server (live data - stable version)",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("addVideoChannel", defaultConf);
    _serverIndices.insert("addVideoChannel", 0);
    _serverConfigs.insert("apiV1AccountsNameVideoChannelSyncsGet", defaultConf);
    _serverIndices.insert("apiV1AccountsNameVideoChannelSyncsGet", 0);
    _serverConfigs.insert("apiV1AccountsNameVideoChannelsGet", defaultConf);
    _serverIndices.insert("apiV1AccountsNameVideoChannelsGet", 0);
    _serverConfigs.insert("apiV1VideoChannelsChannelHandleAvatarDelete", defaultConf);
    _serverIndices.insert("apiV1VideoChannelsChannelHandleAvatarDelete", 0);
    _serverConfigs.insert("apiV1VideoChannelsChannelHandleAvatarPickPost", defaultConf);
    _serverIndices.insert("apiV1VideoChannelsChannelHandleAvatarPickPost", 0);
    _serverConfigs.insert("apiV1VideoChannelsChannelHandleBannerDelete", defaultConf);
    _serverIndices.insert("apiV1VideoChannelsChannelHandleBannerDelete", 0);
    _serverConfigs.insert("apiV1VideoChannelsChannelHandleBannerPickPost", defaultConf);
    _serverIndices.insert("apiV1VideoChannelsChannelHandleBannerPickPost", 0);
    _serverConfigs.insert("apiV1VideoChannelsChannelHandleImportVideosPost", defaultConf);
    _serverIndices.insert("apiV1VideoChannelsChannelHandleImportVideosPost", 0);
    _serverConfigs.insert("apiV1VideoChannelsChannelHandleVideoPlaylistsGet", defaultConf);
    _serverIndices.insert("apiV1VideoChannelsChannelHandleVideoPlaylistsGet", 0);
    _serverConfigs.insert("delVideoChannel", defaultConf);
    _serverIndices.insert("delVideoChannel", 0);
    _serverConfigs.insert("getVideoChannel", defaultConf);
    _serverIndices.insert("getVideoChannel", 0);
    _serverConfigs.insert("getVideoChannelFollowers", defaultConf);
    _serverIndices.insert("getVideoChannelFollowers", 0);
    _serverConfigs.insert("getVideoChannelVideos", defaultConf);
    _serverIndices.insert("getVideoChannelVideos", 0);
    _serverConfigs.insert("getVideoChannels", defaultConf);
    _serverIndices.insert("getVideoChannels", 0);
    _serverConfigs.insert("putVideoChannel", defaultConf);
    _serverIndices.insert("putVideoChannel", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIVideoChannelsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIVideoChannelsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIVideoChannelsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIVideoChannelsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIVideoChannelsApi::setUsername(const QString &username) {
    _username = username;
}

void OAIVideoChannelsApi::setPassword(const QString &password) {
    _password = password;
}


void OAIVideoChannelsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIVideoChannelsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIVideoChannelsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIVideoChannelsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIVideoChannelsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIVideoChannelsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIVideoChannelsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIVideoChannelsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIVideoChannelsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIVideoChannelsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIVideoChannelsApi::getParamStylePrefix(const QString &style) {
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

QString OAIVideoChannelsApi::getParamStyleSuffix(const QString &style) {
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

QString OAIVideoChannelsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIVideoChannelsApi::addVideoChannel(const ::OpenAPI::OptionalParam<OAIVideoChannelCreate> &oai_video_channel_create) {
    QString fullPath = QString(_serverConfigs["addVideoChannel"][_serverIndices.value("addVideoChannel")].URL()+"/api/v1/video-channels");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_video_channel_create.hasValue()){

        
        QByteArray output = oai_video_channel_create.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::addVideoChannelCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::addVideoChannelCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoChannelsApi::addVideoChannelCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAddVideoChannel_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addVideoChannelSignal(output);
        Q_EMIT addVideoChannelSignalFull(worker, output);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT addVideoChannelSignalE(output, error_type, error_str);
        Q_EMIT addVideoChannelSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addVideoChannelSignalError(output, error_type, error_str);
        Q_EMIT addVideoChannelSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::apiV1AccountsNameVideoChannelSyncsGet(const QString &name, const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &sort) {
    QString fullPath = QString(_serverConfigs["apiV1AccountsNameVideoChannelSyncsGet"][_serverIndices.value("apiV1AccountsNameVideoChannelSyncsGet")].URL()+"/api/v1/accounts/{name}/video-channel-syncs");
    
    
    {
        QString namePathParam("{");
        namePathParam.append("name").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "name", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"name"+pathSuffix : pathPrefix;
        fullPath.replace(namePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(name)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (start.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start")).append(querySuffix).append(QUrl::toPercentEncoding(start.stringValue()));
    }
    if (count.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "count", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("count")).append(querySuffix).append(QUrl::toPercentEncoding(count.stringValue()));
    }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1AccountsNameVideoChannelSyncsGetCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVideoChannelsApi::apiV1AccountsNameVideoChannelSyncsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVideoChannelSyncList output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiV1AccountsNameVideoChannelSyncsGetSignal(output);
        Q_EMIT apiV1AccountsNameVideoChannelSyncsGetSignalFull(worker, output);
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

        Q_EMIT apiV1AccountsNameVideoChannelSyncsGetSignalE(output, error_type, error_str);
        Q_EMIT apiV1AccountsNameVideoChannelSyncsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiV1AccountsNameVideoChannelSyncsGetSignalError(output, error_type, error_str);
        Q_EMIT apiV1AccountsNameVideoChannelSyncsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::apiV1AccountsNameVideoChannelsGet(const QString &name, const ::OpenAPI::OptionalParam<bool> &with_stats, const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &sort) {
    QString fullPath = QString(_serverConfigs["apiV1AccountsNameVideoChannelsGet"][_serverIndices.value("apiV1AccountsNameVideoChannelsGet")].URL()+"/api/v1/accounts/{name}/video-channels");
    
    
    {
        QString namePathParam("{");
        namePathParam.append("name").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "name", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"name"+pathSuffix : pathPrefix;
        fullPath.replace(namePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(name)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (with_stats.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "withStats", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("withStats")).append(querySuffix).append(QUrl::toPercentEncoding(with_stats.stringValue()));
    }
    if (start.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start")).append(querySuffix).append(QUrl::toPercentEncoding(start.stringValue()));
    }
    if (count.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "count", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("count")).append(querySuffix).append(QUrl::toPercentEncoding(count.stringValue()));
    }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1AccountsNameVideoChannelsGetCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVideoChannelsApi::apiV1AccountsNameVideoChannelsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVideoChannelList output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiV1AccountsNameVideoChannelsGetSignal(output);
        Q_EMIT apiV1AccountsNameVideoChannelsGetSignalFull(worker, output);
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

        Q_EMIT apiV1AccountsNameVideoChannelsGetSignalE(output, error_type, error_str);
        Q_EMIT apiV1AccountsNameVideoChannelsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiV1AccountsNameVideoChannelsGetSignalError(output, error_type, error_str);
        Q_EMIT apiV1AccountsNameVideoChannelsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleAvatarDelete(const QString &channel_handle) {
    QString fullPath = QString(_serverConfigs["apiV1VideoChannelsChannelHandleAvatarDelete"][_serverIndices.value("apiV1VideoChannelsChannelHandleAvatarDelete")].URL()+"/api/v1/video-channels/{channelHandle}/avatar");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleAvatarDeleteCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleAvatarDeleteCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleAvatarDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiV1VideoChannelsChannelHandleAvatarDeleteSignal();
        Q_EMIT apiV1VideoChannelsChannelHandleAvatarDeleteSignalFull(worker);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT apiV1VideoChannelsChannelHandleAvatarDeleteSignalE(error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleAvatarDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiV1VideoChannelsChannelHandleAvatarDeleteSignalError(error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleAvatarDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleAvatarPickPost(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIHttpFileElement> &avatarfile) {
    QString fullPath = QString(_serverConfigs["apiV1VideoChannelsChannelHandleAvatarPickPost"][_serverIndices.value("apiV1VideoChannelsChannelHandleAvatarPickPost")].URL()+"/api/v1/video-channels/{channelHandle}/avatar/pick");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (avatarfile.hasValue())
    {
        input.add_file("avatarfile", avatarfile.value().local_filename, avatarfile.value().request_filename, avatarfile.value().mime_type);
    }

    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleAvatarPickPostCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleAvatarPickPostCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleAvatarPickPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_v1_users_me_avatar_pick_post_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiV1VideoChannelsChannelHandleAvatarPickPostSignal(output);
        Q_EMIT apiV1VideoChannelsChannelHandleAvatarPickPostSignalFull(worker, output);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT apiV1VideoChannelsChannelHandleAvatarPickPostSignalE(output, error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleAvatarPickPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiV1VideoChannelsChannelHandleAvatarPickPostSignalError(output, error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleAvatarPickPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleBannerDelete(const QString &channel_handle) {
    QString fullPath = QString(_serverConfigs["apiV1VideoChannelsChannelHandleBannerDelete"][_serverIndices.value("apiV1VideoChannelsChannelHandleBannerDelete")].URL()+"/api/v1/video-channels/{channelHandle}/banner");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleBannerDeleteCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleBannerDeleteCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleBannerDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiV1VideoChannelsChannelHandleBannerDeleteSignal();
        Q_EMIT apiV1VideoChannelsChannelHandleBannerDeleteSignalFull(worker);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT apiV1VideoChannelsChannelHandleBannerDeleteSignalE(error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleBannerDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiV1VideoChannelsChannelHandleBannerDeleteSignalError(error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleBannerDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleBannerPickPost(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIHttpFileElement> &bannerfile) {
    QString fullPath = QString(_serverConfigs["apiV1VideoChannelsChannelHandleBannerPickPost"][_serverIndices.value("apiV1VideoChannelsChannelHandleBannerPickPost")].URL()+"/api/v1/video-channels/{channelHandle}/banner/pick");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (bannerfile.hasValue())
    {
        input.add_file("bannerfile", bannerfile.value().local_filename, bannerfile.value().request_filename, bannerfile.value().mime_type);
    }

    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleBannerPickPostCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleBannerPickPostCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleBannerPickPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_v1_video_channels__channelHandle__banner_pick_post_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiV1VideoChannelsChannelHandleBannerPickPostSignal(output);
        Q_EMIT apiV1VideoChannelsChannelHandleBannerPickPostSignalFull(worker, output);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT apiV1VideoChannelsChannelHandleBannerPickPostSignalE(output, error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleBannerPickPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiV1VideoChannelsChannelHandleBannerPickPostSignalError(output, error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleBannerPickPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleImportVideosPost(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIImportVideosInChannelCreate> &oai_import_videos_in_channel_create) {
    QString fullPath = QString(_serverConfigs["apiV1VideoChannelsChannelHandleImportVideosPost"][_serverIndices.value("apiV1VideoChannelsChannelHandleImportVideosPost")].URL()+"/api/v1/video-channels/{channelHandle}/import-videos");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_import_videos_in_channel_create.hasValue()){

        
        QByteArray output = oai_import_videos_in_channel_create.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleImportVideosPostCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleImportVideosPostCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleImportVideosPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiV1VideoChannelsChannelHandleImportVideosPostSignal();
        Q_EMIT apiV1VideoChannelsChannelHandleImportVideosPostSignalFull(worker);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT apiV1VideoChannelsChannelHandleImportVideosPostSignalE(error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleImportVideosPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiV1VideoChannelsChannelHandleImportVideosPostSignalError(error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleImportVideosPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleVideoPlaylistsGet(const QString &channel_handle, const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &sort, const ::OpenAPI::OptionalParam<OAIVideoPlaylistTypeSet> &playlist_type) {
    QString fullPath = QString(_serverConfigs["apiV1VideoChannelsChannelHandleVideoPlaylistsGet"][_serverIndices.value("apiV1VideoChannelsChannelHandleVideoPlaylistsGet")].URL()+"/api/v1/video-channels/{channelHandle}/video-playlists");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (start.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start")).append(querySuffix).append(QUrl::toPercentEncoding(start.stringValue()));
    }
    if (count.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "count", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("count")).append(querySuffix).append(QUrl::toPercentEncoding(count.stringValue()));
    }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    if (playlist_type.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "playlistType", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "playlistType"+querySuffix : "";
        QJsonObject parameter = playlist_type.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("playlistType").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("playlistType").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("playlistType").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("playlistType").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("playlistType").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleVideoPlaylistsGetCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVideoChannelsApi::apiV1VideoChannelsChannelHandleVideoPlaylistsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_v1_accounts__name__video_playlists_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignal(output);
        Q_EMIT apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalFull(worker, output);
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

        Q_EMIT apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalE(output, error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalError(output, error_type, error_str);
        Q_EMIT apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::delVideoChannel(const QString &channel_handle) {
    QString fullPath = QString(_serverConfigs["delVideoChannel"][_serverIndices.value("delVideoChannel")].URL()+"/api/v1/video-channels/{channelHandle}");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::delVideoChannelCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::delVideoChannelCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoChannelsApi::delVideoChannelCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT delVideoChannelSignal();
        Q_EMIT delVideoChannelSignalFull(worker);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT delVideoChannelSignalE(error_type, error_str);
        Q_EMIT delVideoChannelSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT delVideoChannelSignalError(error_type, error_str);
        Q_EMIT delVideoChannelSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::getVideoChannel(const QString &channel_handle) {
    QString fullPath = QString(_serverConfigs["getVideoChannel"][_serverIndices.value("getVideoChannel")].URL()+"/api/v1/video-channels/{channelHandle}");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::getVideoChannelCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVideoChannelsApi::getVideoChannelCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVideoChannel output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getVideoChannelSignal(output);
        Q_EMIT getVideoChannelSignalFull(worker, output);
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

        Q_EMIT getVideoChannelSignalE(output, error_type, error_str);
        Q_EMIT getVideoChannelSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getVideoChannelSignalError(output, error_type, error_str);
        Q_EMIT getVideoChannelSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::getVideoChannelFollowers(const QString &channel_handle, const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &sort, const ::OpenAPI::OptionalParam<QString> &search) {
    QString fullPath = QString(_serverConfigs["getVideoChannelFollowers"][_serverIndices.value("getVideoChannelFollowers")].URL()+"/api/v1/video-channels/{channelHandle}/followers");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (start.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start")).append(querySuffix).append(QUrl::toPercentEncoding(start.stringValue()));
    }
    if (count.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "count", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("count")).append(querySuffix).append(QUrl::toPercentEncoding(count.stringValue()));
    }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    if (search.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("search")).append(querySuffix).append(QUrl::toPercentEncoding(search.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::getVideoChannelFollowersCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::getVideoChannelFollowersCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoChannelsApi::getVideoChannelFollowersCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetAccountFollowers_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getVideoChannelFollowersSignal(output);
        Q_EMIT getVideoChannelFollowersSignalFull(worker, output);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT getVideoChannelFollowersSignalE(output, error_type, error_str);
        Q_EMIT getVideoChannelFollowersSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getVideoChannelFollowersSignalError(output, error_type, error_str);
        Q_EMIT getVideoChannelFollowersSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::getVideoChannelVideos(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter> &category_one_of, const ::OpenAPI::OptionalParam<bool> &is_live, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter> &tags_one_of, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter> &tags_all_of, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter> &licence_one_of, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter> &language_one_of, const ::OpenAPI::OptionalParam<QString> &nsfw, const ::OpenAPI::OptionalParam<bool> &is_local, const ::OpenAPI::OptionalParam<qint32> &include, const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy_one_of, const ::OpenAPI::OptionalParam<bool> &has_hls_files, const ::OpenAPI::OptionalParam<bool> &has_webtorrent_files, const ::OpenAPI::OptionalParam<QString> &skip_count, const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &sort, const ::OpenAPI::OptionalParam<bool> &exclude_already_watched) {
    QString fullPath = QString(_serverConfigs["getVideoChannelVideos"][_serverIndices.value("getVideoChannelVideos")].URL()+"/api/v1/video-channels/{channelHandle}/videos");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (category_one_of.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "categoryOneOf", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && false) ? "" : (queryStyle == "form" && !(false)) ? "categoryOneOf"+querySuffix : "";
        QJsonObject parameter = category_one_of.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && false) ? "&" : getParamStyleDelimiter(queryStyle, key, false);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (false) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (false) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("categoryOneOf").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("categoryOneOf").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("categoryOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("categoryOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("categoryOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (is_live.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "isLive", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("isLive")).append(querySuffix).append(QUrl::toPercentEncoding(is_live.stringValue()));
    }
    if (tags_one_of.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "tagsOneOf", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && false) ? "" : (queryStyle == "form" && !(false)) ? "tagsOneOf"+querySuffix : "";
        QJsonObject parameter = tags_one_of.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && false) ? "&" : getParamStyleDelimiter(queryStyle, key, false);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (false) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (false) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsOneOf").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsOneOf").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (tags_all_of.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "tagsAllOf", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && false) ? "" : (queryStyle == "form" && !(false)) ? "tagsAllOf"+querySuffix : "";
        QJsonObject parameter = tags_all_of.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && false) ? "&" : getParamStyleDelimiter(queryStyle, key, false);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (false) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (false) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsAllOf").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsAllOf").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsAllOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsAllOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("tagsAllOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (licence_one_of.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "licenceOneOf", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && false) ? "" : (queryStyle == "form" && !(false)) ? "licenceOneOf"+querySuffix : "";
        QJsonObject parameter = licence_one_of.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && false) ? "&" : getParamStyleDelimiter(queryStyle, key, false);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (false) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (false) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("licenceOneOf").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("licenceOneOf").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("licenceOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("licenceOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("licenceOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (language_one_of.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "languageOneOf", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && false) ? "" : (queryStyle == "form" && !(false)) ? "languageOneOf"+querySuffix : "";
        QJsonObject parameter = language_one_of.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && false) ? "&" : getParamStyleDelimiter(queryStyle, key, false);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (false) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (false) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("languageOneOf").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("languageOneOf").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("languageOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("languageOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("languageOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (nsfw.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nsfw", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nsfw")).append(querySuffix).append(QUrl::toPercentEncoding(nsfw.stringValue()));
    }
    if (is_local.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "isLocal", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("isLocal")).append(querySuffix).append(QUrl::toPercentEncoding(is_local.stringValue()));
    }
    if (include.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "include", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("include")).append(querySuffix).append(QUrl::toPercentEncoding(include.stringValue()));
    }
    if (privacy_one_of.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "privacyOneOf", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "privacyOneOf"+querySuffix : "";
        QJsonObject parameter = privacy_one_of.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("privacyOneOf").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("privacyOneOf").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("privacyOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("privacyOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("privacyOneOf").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (has_hls_files.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "hasHLSFiles", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("hasHLSFiles")).append(querySuffix).append(QUrl::toPercentEncoding(has_hls_files.stringValue()));
    }
    if (has_webtorrent_files.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "hasWebtorrentFiles", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("hasWebtorrentFiles")).append(querySuffix).append(QUrl::toPercentEncoding(has_webtorrent_files.stringValue()));
    }
    if (skip_count.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "skipCount", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("skipCount")).append(querySuffix).append(QUrl::toPercentEncoding(skip_count.stringValue()));
    }
    if (start.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start")).append(querySuffix).append(QUrl::toPercentEncoding(start.stringValue()));
    }
    if (count.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "count", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("count")).append(querySuffix).append(QUrl::toPercentEncoding(count.stringValue()));
    }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    if (exclude_already_watched.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "excludeAlreadyWatched", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("excludeAlreadyWatched")).append(querySuffix).append(QUrl::toPercentEncoding(exclude_already_watched.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::getVideoChannelVideosCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVideoChannelsApi::getVideoChannelVideosCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVideoListResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getVideoChannelVideosSignal(output);
        Q_EMIT getVideoChannelVideosSignalFull(worker, output);
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

        Q_EMIT getVideoChannelVideosSignalE(output, error_type, error_str);
        Q_EMIT getVideoChannelVideosSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getVideoChannelVideosSignalError(output, error_type, error_str);
        Q_EMIT getVideoChannelVideosSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::getVideoChannels(const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &sort) {
    QString fullPath = QString(_serverConfigs["getVideoChannels"][_serverIndices.value("getVideoChannels")].URL()+"/api/v1/video-channels");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (start.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start")).append(querySuffix).append(QUrl::toPercentEncoding(start.stringValue()));
    }
    if (count.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "count", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("count")).append(querySuffix).append(QUrl::toPercentEncoding(count.stringValue()));
    }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::getVideoChannelsCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVideoChannelsApi::getVideoChannelsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVideoChannelList output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getVideoChannelsSignal(output);
        Q_EMIT getVideoChannelsSignalFull(worker, output);
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

        Q_EMIT getVideoChannelsSignalE(output, error_type, error_str);
        Q_EMIT getVideoChannelsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getVideoChannelsSignalError(output, error_type, error_str);
        Q_EMIT getVideoChannelsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::putVideoChannel(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIVideoChannelUpdate> &oai_video_channel_update) {
    QString fullPath = QString(_serverConfigs["putVideoChannel"][_serverIndices.value("putVideoChannel")].URL()+"/api/v1/video-channels/{channelHandle}");
    
    
    {
        QString channel_handlePathParam("{");
        channel_handlePathParam.append("channelHandle").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "channelHandle", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"channelHandle"+pathSuffix : pathPrefix;
        fullPath.replace(channel_handlePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(channel_handle)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    if (oai_video_channel_update.hasValue()){

        
        QByteArray output = oai_video_channel_update.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::putVideoChannelCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoChannelsApi::putVideoChannelCallback);
    connect(this, &OAIVideoChannelsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoChannelsApi::putVideoChannelCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putVideoChannelSignal();
        Q_EMIT putVideoChannelSignalFull(worker);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT putVideoChannelSignalE(error_type, error_str);
        Q_EMIT putVideoChannelSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putVideoChannelSignalError(error_type, error_str);
        Q_EMIT putVideoChannelSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoChannelsApi::tokenAvailable(){

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
