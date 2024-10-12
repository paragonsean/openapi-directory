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

#include "OAISearchApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAISearchApi::OAISearchApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAISearchApi::~OAISearchApi() {
}

void OAISearchApi::initializeServerConfigs() {
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
    _serverConfigs.insert("searchChannels", defaultConf);
    _serverIndices.insert("searchChannels", 0);
    _serverConfigs.insert("searchPlaylists", defaultConf);
    _serverIndices.insert("searchPlaylists", 0);
    _serverConfigs.insert("searchVideos", defaultConf);
    _serverIndices.insert("searchVideos", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAISearchApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAISearchApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAISearchApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAISearchApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAISearchApi::setUsername(const QString &username) {
    _username = username;
}

void OAISearchApi::setPassword(const QString &password) {
    _password = password;
}


void OAISearchApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAISearchApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAISearchApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAISearchApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAISearchApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAISearchApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAISearchApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAISearchApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAISearchApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAISearchApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAISearchApi::getParamStylePrefix(const QString &style) {
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

QString OAISearchApi::getParamStyleSuffix(const QString &style) {
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

QString OAISearchApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAISearchApi::searchChannels(const QString &search, const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &search_target, const ::OpenAPI::OptionalParam<QString> &sort) {
    QString fullPath = QString(_serverConfigs["searchChannels"][_serverIndices.value("searchChannels")].URL()+"/api/v1/search/video-channels");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
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

        fullPath.append(QUrl::toPercentEncoding("search")).append(querySuffix).append(QUrl::toPercentEncoding(search));
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
    if (search_target.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "searchTarget", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("searchTarget")).append(querySuffix).append(QUrl::toPercentEncoding(search_target.stringValue()));
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAISearchApi::searchChannelsCallback);
    connect(this, &OAISearchApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAISearchApi::searchChannelsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVideoChannelList output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT searchChannelsSignal(output);
        Q_EMIT searchChannelsSignalFull(worker, output);
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

        Q_EMIT searchChannelsSignalE(output, error_type, error_str);
        Q_EMIT searchChannelsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT searchChannelsSignalError(output, error_type, error_str);
        Q_EMIT searchChannelsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAISearchApi::searchPlaylists(const QString &search, const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &search_target, const ::OpenAPI::OptionalParam<QString> &sort) {
    QString fullPath = QString(_serverConfigs["searchPlaylists"][_serverIndices.value("searchPlaylists")].URL()+"/api/v1/search/video-playlists");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
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

        fullPath.append(QUrl::toPercentEncoding("search")).append(querySuffix).append(QUrl::toPercentEncoding(search));
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
    if (search_target.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "searchTarget", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("searchTarget")).append(querySuffix).append(QUrl::toPercentEncoding(search_target.stringValue()));
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAISearchApi::searchPlaylistsCallback);
    connect(this, &OAISearchApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAISearchApi::searchPlaylistsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_v1_accounts__name__video_playlists_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT searchPlaylistsSignal(output);
        Q_EMIT searchPlaylistsSignalFull(worker, output);
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

        Q_EMIT searchPlaylistsSignalE(output, error_type, error_str);
        Q_EMIT searchPlaylistsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT searchPlaylistsSignalError(output, error_type, error_str);
        Q_EMIT searchPlaylistsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAISearchApi::searchVideos(const QString &search, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter> &category_one_of, const ::OpenAPI::OptionalParam<bool> &is_live, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter> &tags_one_of, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter> &tags_all_of, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter> &licence_one_of, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter> &language_one_of, const ::OpenAPI::OptionalParam<QString> &nsfw, const ::OpenAPI::OptionalParam<bool> &is_local, const ::OpenAPI::OptionalParam<qint32> &include, const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy_one_of, const ::OpenAPI::OptionalParam<QList<QString>> &uuids, const ::OpenAPI::OptionalParam<bool> &has_hls_files, const ::OpenAPI::OptionalParam<bool> &has_webtorrent_files, const ::OpenAPI::OptionalParam<QString> &skip_count, const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &search_target, const ::OpenAPI::OptionalParam<QString> &sort, const ::OpenAPI::OptionalParam<bool> &exclude_already_watched, const ::OpenAPI::OptionalParam<QDateTime> &start_date, const ::OpenAPI::OptionalParam<QDateTime> &end_date, const ::OpenAPI::OptionalParam<QDateTime> &originally_published_start_date, const ::OpenAPI::OptionalParam<QDateTime> &originally_published_end_date, const ::OpenAPI::OptionalParam<qint32> &duration_min, const ::OpenAPI::OptionalParam<qint32> &duration_max) {
    QString fullPath = QString(_serverConfigs["searchVideos"][_serverIndices.value("searchVideos")].URL()+"/api/v1/search/videos");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
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

        fullPath.append(QUrl::toPercentEncoding("search")).append(querySuffix).append(QUrl::toPercentEncoding(search));
    }
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
    if (uuids.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "uuids", true);
        if (uuids.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : uuids.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("uuids=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("uuids").append(querySuffix);
                qint32 count = 0;
                for (QString t : uuids.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("uuids").append(querySuffix);
                qint32 count = 0;
                for (QString t : uuids.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("uuids").append(querySuffix);
                qint32 count = 0;
                for (QString t : uuids.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("uuids").append(querySuffix);
                qint32 count = 0;
                for (QString t : uuids.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("uuids").append(querySuffix);
                qint32 count = 0;
                for (QString t : uuids.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
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
    if (search_target.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "searchTarget", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("searchTarget")).append(querySuffix).append(QUrl::toPercentEncoding(search_target.stringValue()));
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
    if (start_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "startDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("startDate")).append(querySuffix).append(QUrl::toPercentEncoding(start_date.stringValue()));
    }
    if (end_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "endDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("endDate")).append(querySuffix).append(QUrl::toPercentEncoding(end_date.stringValue()));
    }
    if (originally_published_start_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "originallyPublishedStartDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("originallyPublishedStartDate")).append(querySuffix).append(QUrl::toPercentEncoding(originally_published_start_date.stringValue()));
    }
    if (originally_published_end_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "originallyPublishedEndDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("originallyPublishedEndDate")).append(querySuffix).append(QUrl::toPercentEncoding(originally_published_end_date.stringValue()));
    }
    if (duration_min.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "durationMin", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("durationMin")).append(querySuffix).append(QUrl::toPercentEncoding(duration_min.stringValue()));
    }
    if (duration_max.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "durationMax", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("durationMax")).append(querySuffix).append(QUrl::toPercentEncoding(duration_max.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAISearchApi::searchVideosCallback);
    connect(this, &OAISearchApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAISearchApi::searchVideosCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVideoListResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT searchVideosSignal(output);
        Q_EMIT searchVideosSignalFull(worker, output);
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

        Q_EMIT searchVideosSignalE(output, error_type, error_str);
        Q_EMIT searchVideosSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT searchVideosSignalError(output, error_type, error_str);
        Q_EMIT searchVideosSignalErrorFull(worker, error_type, error_str);
    }
}

void OAISearchApi::tokenAvailable(){

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
