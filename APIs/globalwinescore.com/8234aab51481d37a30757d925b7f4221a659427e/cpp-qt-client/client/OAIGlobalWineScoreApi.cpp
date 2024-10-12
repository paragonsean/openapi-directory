/**
 * GlobalWineScore API Documentation
 *   The GlobalWineScore API is designed as a RESTful API, providing several resources and methods depending on your usage plan.  For further information please refer to <a href=\"https://www.globalwinescore.com/plans\" target=\"_blank\">our plans</a>.  # Authentication The API uses token-based authentication. In order to authenticate your requests, you need to include a specific header in each of your requests:  ``` Authorization: Token {YOUR-API-TOKEN} ``` The word <b>Token</b> must be written. Your requests must also use the <b>HTTPS</b> protocol.  If you don't have a token yet, you need to apply for one [here](https://www.globalwinescore.com/api/).  Your personal token can be found under the <a href=\"https://www.globalwinescore.com/account/api/\" target=\"_blank\">My account > API</a> section of the GlobalWineScore website  # Format The API provides several rendering formats which you can control using the `Accept` header or `format` query parameter.  - JSON (default): no header or `Accept: application/json` - XML: `Accept: application/xml` # Rate limiting For API requests, the rate limit allows for up to 10 requests per minute.  # Error handling  Whether a request succeeded is indicated by the HTTP status code. A 2xx status code indicates success, whereas a 4xx status code indicates failure.  When a request fails, the response body is still JSON, but always contains a `detail` field with a description of the error, which you can inspect for debugging.  For example, trying to access the API without proper authentication will return code 403 along with the message:  `{\"detail\": \"Authentication credentials were not provided.\"}`  Found a bug ? send us an email at <a href=\"mailto:api@globalwinescore.com\">api@globalwinescore.com</a>  # Ordering  At the moment, GlobalWineScores may be sorted by `date` and `score`. Use \"-\" to sort in descending order.  # Continuous synchronization  If you need to synchronize your database with our API, you can query our API using `?ordering=-date` to get the newest scores first, which means you won't have to crawl the whole catalog every time :-)  # Quick search interface If you need to search our catalog (e.g. to align it with yours), we're providing you with a handy interface accessible here: <a href=\"https://api.globalwinescore.com/search/\" target=\"_blank\">https://api.globalwinescore.com/search/</a>  You need to be logged in (email/password) to access this page, but other than that you can share it with anyone in your team and start searching right away !  # Resources  The details about available endpoints can be found below. You can click on each endpoint to find information about their parameters. 
 *
 * The version of the OpenAPI document: 8234aab51481d37a30757d925b7f4221a659427e
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGlobalWineScoreApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIGlobalWineScoreApi::OAIGlobalWineScoreApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIGlobalWineScoreApi::~OAIGlobalWineScoreApi() {
}

void OAIGlobalWineScoreApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.globalwinescore.com"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("globalwinescoresLatestGet", defaultConf);
    _serverIndices.insert("globalwinescoresLatestGet", 0);
    _serverConfigs.insert("listHistoricalGWS", defaultConf);
    _serverIndices.insert("listHistoricalGWS", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIGlobalWineScoreApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIGlobalWineScoreApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIGlobalWineScoreApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIGlobalWineScoreApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIGlobalWineScoreApi::setUsername(const QString &username) {
    _username = username;
}

void OAIGlobalWineScoreApi::setPassword(const QString &password) {
    _password = password;
}


void OAIGlobalWineScoreApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIGlobalWineScoreApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIGlobalWineScoreApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIGlobalWineScoreApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIGlobalWineScoreApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIGlobalWineScoreApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIGlobalWineScoreApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIGlobalWineScoreApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIGlobalWineScoreApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIGlobalWineScoreApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIGlobalWineScoreApi::getParamStylePrefix(const QString &style) {
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

QString OAIGlobalWineScoreApi::getParamStyleSuffix(const QString &style) {
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

QString OAIGlobalWineScoreApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIGlobalWineScoreApi::globalwinescoresLatestGet(const ::OpenAPI::OptionalParam<QString> &authorization, const ::OpenAPI::OptionalParam<QList<qint32>> &wine_id, const ::OpenAPI::OptionalParam<QString> &vintage, const ::OpenAPI::OptionalParam<QString> &color, const ::OpenAPI::OptionalParam<bool> &is_primeurs, const ::OpenAPI::OptionalParam<QString> &lwin, const ::OpenAPI::OptionalParam<QString> &lwin_11, const ::OpenAPI::OptionalParam<qint32> &limit, const ::OpenAPI::OptionalParam<qint32> &offset, const ::OpenAPI::OptionalParam<QString> &ordering) {
    QString fullPath = QString(_serverConfigs["globalwinescoresLatestGet"][_serverIndices.value("globalwinescoresLatestGet")].URL()+"/globalwinescores/latest/");
    
    if (_apiKeys.contains("TokenAuthentication")) {
        addHeaders("TokenAuthentication",_apiKeys.find("TokenAuthentication").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (wine_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "wine_id", true);
        if (wine_id.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (qint32 t : wine_id.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("wine_id=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (vintage.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "vintage", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("vintage")).append(querySuffix).append(QUrl::toPercentEncoding(vintage.stringValue()));
    }
    if (color.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "color", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("color")).append(querySuffix).append(QUrl::toPercentEncoding(color.stringValue()));
    }
    if (is_primeurs.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "is_primeurs", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("is_primeurs")).append(querySuffix).append(QUrl::toPercentEncoding(is_primeurs.stringValue()));
    }
    if (lwin.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "lwin", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("lwin")).append(querySuffix).append(QUrl::toPercentEncoding(lwin.stringValue()));
    }
    if (lwin_11.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "lwin_11", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("lwin_11")).append(querySuffix).append(QUrl::toPercentEncoding(lwin_11.stringValue()));
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
    if (ordering.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "ordering", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("ordering")).append(querySuffix).append(QUrl::toPercentEncoding(ordering.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (authorization.hasValue())
    {
        if (!::OpenAPI::toStringValue(authorization.value()).isEmpty()) {
            input.headers.insert("Authorization", ::OpenAPI::toStringValue(authorization.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIGlobalWineScoreApi::globalwinescoresLatestGetCallback);
    connect(this, &OAIGlobalWineScoreApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIGlobalWineScoreApi::globalwinescoresLatestGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT globalwinescoresLatestGetSignal();
        Q_EMIT globalwinescoresLatestGetSignalFull(worker);
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

        Q_EMIT globalwinescoresLatestGetSignalE(error_type, error_str);
        Q_EMIT globalwinescoresLatestGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT globalwinescoresLatestGetSignalError(error_type, error_str);
        Q_EMIT globalwinescoresLatestGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIGlobalWineScoreApi::listHistoricalGWS(const ::OpenAPI::OptionalParam<QString> &authorization, const ::OpenAPI::OptionalParam<QList<qint32>> &wine_id, const ::OpenAPI::OptionalParam<QString> &vintage, const ::OpenAPI::OptionalParam<QString> &color, const ::OpenAPI::OptionalParam<bool> &is_primeurs, const ::OpenAPI::OptionalParam<QString> &lwin, const ::OpenAPI::OptionalParam<QString> &lwin_11, const ::OpenAPI::OptionalParam<qint32> &limit, const ::OpenAPI::OptionalParam<qint32> &offset, const ::OpenAPI::OptionalParam<QString> &ordering) {
    QString fullPath = QString(_serverConfigs["listHistoricalGWS"][_serverIndices.value("listHistoricalGWS")].URL()+"/globalwinescores/");
    
    if (_apiKeys.contains("TokenAuthentication")) {
        addHeaders("TokenAuthentication",_apiKeys.find("TokenAuthentication").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (wine_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "wine_id", true);
        if (wine_id.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (qint32 t : wine_id.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("wine_id=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
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
                    fullPath.append("?").append(queryPrefix).append("wine_id").append(querySuffix);
                qint32 count = 0;
                for (qint32 t : wine_id.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (vintage.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "vintage", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("vintage")).append(querySuffix).append(QUrl::toPercentEncoding(vintage.stringValue()));
    }
    if (color.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "color", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("color")).append(querySuffix).append(QUrl::toPercentEncoding(color.stringValue()));
    }
    if (is_primeurs.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "is_primeurs", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("is_primeurs")).append(querySuffix).append(QUrl::toPercentEncoding(is_primeurs.stringValue()));
    }
    if (lwin.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "lwin", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("lwin")).append(querySuffix).append(QUrl::toPercentEncoding(lwin.stringValue()));
    }
    if (lwin_11.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "lwin_11", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("lwin_11")).append(querySuffix).append(QUrl::toPercentEncoding(lwin_11.stringValue()));
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
    if (ordering.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "ordering", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("ordering")).append(querySuffix).append(QUrl::toPercentEncoding(ordering.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (authorization.hasValue())
    {
        if (!::OpenAPI::toStringValue(authorization.value()).isEmpty()) {
            input.headers.insert("Authorization", ::OpenAPI::toStringValue(authorization.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIGlobalWineScoreApi::listHistoricalGWSCallback);
    connect(this, &OAIGlobalWineScoreApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIGlobalWineScoreApi::listHistoricalGWSCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listHistoricalGWSSignal();
        Q_EMIT listHistoricalGWSSignalFull(worker);
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

        Q_EMIT listHistoricalGWSSignalE(error_type, error_str);
        Q_EMIT listHistoricalGWSSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listHistoricalGWSSignalError(error_type, error_str);
        Q_EMIT listHistoricalGWSSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIGlobalWineScoreApi::tokenAvailable(){

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
