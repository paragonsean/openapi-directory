/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::~OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi() {
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.hillbillysoftware.com/"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("magnetsByDateGetAsync", defaultConf);
    _serverIndices.insert("magnetsByDateGetAsync", 0);
    _serverConfigs.insert("magnetsByimdbIDGetAsync", defaultConf);
    _serverIndices.insert("magnetsByimdbIDGetAsync", 0);
    _serverConfigs.insert("magnetsMovieByIDGetAsync", defaultConf);
    _serverIndices.insert("magnetsMovieByIDGetAsync", 0);
    _serverConfigs.insert("tVShowsearchGet", defaultConf);
    _serverIndices.insert("tVShowsearchGet", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setUsername(const QString &username) {
    _username = username;
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setPassword(const QString &password) {
    _password = password;
}


void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::getParamStylePrefix(const QString &style) {
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

QString OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::getParamStyleSuffix(const QString &style) {
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

QString OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::magnetsByDateGetAsync(const QString &access_token, const QString &date) {
    QString fullPath = QString(_serverConfigs["magnetsByDateGetAsync"][_serverIndices.value("magnetsByDateGetAsync")].URL()+"/Magnets/ByDate/{AccessToken}/{Date}");
    
    
    {
        QString access_tokenPathParam("{");
        access_tokenPathParam.append("AccessToken").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "AccessToken", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"AccessToken"+pathSuffix : pathPrefix;
        fullPath.replace(access_tokenPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(access_token)));
    }
    
    {
        QString datePathParam("{");
        datePathParam.append("Date").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "Date", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"Date"+pathSuffix : pathPrefix;
        fullPath.replace(datePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(date)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::magnetsByDateGetAsyncCallback);
    connect(this, &OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::magnetsByDateGetAsyncCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIMagnets> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIMagnets val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT magnetsByDateGetAsyncSignal(output);
        Q_EMIT magnetsByDateGetAsyncSignalFull(worker, output);
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

        Q_EMIT magnetsByDateGetAsyncSignalE(output, error_type, error_str);
        Q_EMIT magnetsByDateGetAsyncSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT magnetsByDateGetAsyncSignalError(output, error_type, error_str);
        Q_EMIT magnetsByDateGetAsyncSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::magnetsByimdbIDGetAsync(const QString &access_token, const QString &imdb_id) {
    QString fullPath = QString(_serverConfigs["magnetsByimdbIDGetAsync"][_serverIndices.value("magnetsByimdbIDGetAsync")].URL()+"/Magnets/ByIMDB/{AccessToken}/{imdbID}");
    
    
    {
        QString access_tokenPathParam("{");
        access_tokenPathParam.append("AccessToken").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "AccessToken", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"AccessToken"+pathSuffix : pathPrefix;
        fullPath.replace(access_tokenPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(access_token)));
    }
    
    {
        QString imdb_idPathParam("{");
        imdb_idPathParam.append("imdbID").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "imdbID", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"imdbID"+pathSuffix : pathPrefix;
        fullPath.replace(imdb_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(imdb_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::magnetsByimdbIDGetAsyncCallback);
    connect(this, &OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::magnetsByimdbIDGetAsyncCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIMagnets> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIMagnets val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT magnetsByimdbIDGetAsyncSignal(output);
        Q_EMIT magnetsByimdbIDGetAsyncSignalFull(worker, output);
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

        Q_EMIT magnetsByimdbIDGetAsyncSignalE(output, error_type, error_str);
        Q_EMIT magnetsByimdbIDGetAsyncSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT magnetsByimdbIDGetAsyncSignalError(output, error_type, error_str);
        Q_EMIT magnetsByimdbIDGetAsyncSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::magnetsMovieByIDGetAsync(const QString &access_token, const QString &query) {
    QString fullPath = QString(_serverConfigs["magnetsMovieByIDGetAsync"][_serverIndices.value("magnetsMovieByIDGetAsync")].URL()+"/Magnets/Search/{AccessToken}/{Query}");
    
    
    {
        QString access_tokenPathParam("{");
        access_tokenPathParam.append("AccessToken").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "AccessToken", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"AccessToken"+pathSuffix : pathPrefix;
        fullPath.replace(access_tokenPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(access_token)));
    }
    
    {
        QString queryPathParam("{");
        queryPathParam.append("Query").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "Query", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"Query"+pathSuffix : pathPrefix;
        fullPath.replace(queryPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(query)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::magnetsMovieByIDGetAsyncCallback);
    connect(this, &OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::magnetsMovieByIDGetAsyncCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIMagnets> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIMagnets val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT magnetsMovieByIDGetAsyncSignal(output);
        Q_EMIT magnetsMovieByIDGetAsyncSignalFull(worker, output);
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

        Q_EMIT magnetsMovieByIDGetAsyncSignalE(output, error_type, error_str);
        Q_EMIT magnetsMovieByIDGetAsyncSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT magnetsMovieByIDGetAsyncSignalError(output, error_type, error_str);
        Q_EMIT magnetsMovieByIDGetAsyncSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::tVShowsearchGet(const QString &access_token, const QString &tv_show) {
    QString fullPath = QString(_serverConfigs["tVShowsearchGet"][_serverIndices.value("tVShowsearchGet")].URL()+"/Magnets/TVShow/{AccessToken}/{TVShow}");
    
    
    {
        QString access_tokenPathParam("{");
        access_tokenPathParam.append("AccessToken").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "AccessToken", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"AccessToken"+pathSuffix : pathPrefix;
        fullPath.replace(access_tokenPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(access_token)));
    }
    
    {
        QString tv_showPathParam("{");
        tv_showPathParam.append("TVShow").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "TVShow", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"TVShow"+pathSuffix : pathPrefix;
        fullPath.replace(tv_showPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(tv_show)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::tVShowsearchGetCallback);
    connect(this, &OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::tVShowsearchGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIMagnets> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIMagnets val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT tVShowsearchGetSignal(output);
        Q_EMIT tVShowsearchGetSignalFull(worker, output);
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

        Q_EMIT tVShowsearchGetSignalE(output, error_type, error_str);
        Q_EMIT tVShowsearchGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT tVShowsearchGetSignalError(output, error_type, error_str);
        Q_EMIT tVShowsearchGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMagnetsMagnetHashesOfMoviesTelevisionShowsApi::tokenAvailable(){

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
