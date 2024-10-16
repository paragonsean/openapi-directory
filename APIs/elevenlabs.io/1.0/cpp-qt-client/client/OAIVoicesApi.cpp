/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVoicesApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIVoicesApi::OAIVoicesApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIVoicesApi::~OAIVoicesApi() {
}

void OAIVoicesApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("/"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("addVoiceV1VoicesAddPost", defaultConf);
    _serverIndices.insert("addVoiceV1VoicesAddPost", 0);
    _serverConfigs.insert("deleteVoiceV1VoicesVoiceIdDelete", defaultConf);
    _serverIndices.insert("deleteVoiceV1VoicesVoiceIdDelete", 0);
    _serverConfigs.insert("editVoiceSettingsV1VoicesVoiceIdSettingsEditPost", defaultConf);
    _serverIndices.insert("editVoiceSettingsV1VoicesVoiceIdSettingsEditPost", 0);
    _serverConfigs.insert("editVoiceV1VoicesVoiceIdEditPost", defaultConf);
    _serverIndices.insert("editVoiceV1VoicesVoiceIdEditPost", 0);
    _serverConfigs.insert("getDefaultVoiceSettingsV1VoicesSettingsDefaultGet", defaultConf);
    _serverIndices.insert("getDefaultVoiceSettingsV1VoicesSettingsDefaultGet", 0);
    _serverConfigs.insert("getVoiceSettingsV1VoicesVoiceIdSettingsGet", defaultConf);
    _serverIndices.insert("getVoiceSettingsV1VoicesVoiceIdSettingsGet", 0);
    _serverConfigs.insert("getVoiceV1VoicesVoiceIdGet", defaultConf);
    _serverIndices.insert("getVoiceV1VoicesVoiceIdGet", 0);
    _serverConfigs.insert("getVoicesV1VoicesGet", defaultConf);
    _serverIndices.insert("getVoicesV1VoicesGet", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIVoicesApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIVoicesApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIVoicesApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIVoicesApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIVoicesApi::setUsername(const QString &username) {
    _username = username;
}

void OAIVoicesApi::setPassword(const QString &password) {
    _password = password;
}


void OAIVoicesApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIVoicesApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIVoicesApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIVoicesApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIVoicesApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIVoicesApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIVoicesApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIVoicesApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIVoicesApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIVoicesApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIVoicesApi::getParamStylePrefix(const QString &style) {
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

QString OAIVoicesApi::getParamStyleSuffix(const QString &style) {
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

QString OAIVoicesApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIVoicesApi::addVoiceV1VoicesAddPost(const QList<OAIHttpFileElement> &files, const QString &name, const ::OpenAPI::OptionalParam<QString> &xi_api_key, const ::OpenAPI::OptionalParam<QString> &description, const ::OpenAPI::OptionalParam<QString> &labels) {
    QString fullPath = QString(_serverConfigs["addVoiceV1VoicesAddPost"][_serverIndices.value("addVoiceV1VoicesAddPost")].URL()+"/v1/voices/add");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (description.hasValue())
    {
        input.add_var("description", ::OpenAPI::toStringValue(description.value()));
    }
    
    {
        input.add_file("files", files.local_filename, files.request_filename, files.mime_type);
    }
    if (labels.hasValue())
    {
        input.add_var("labels", ::OpenAPI::toStringValue(labels.value()));
    }
    
    {
        input.add_var("name", ::OpenAPI::toStringValue(name));
    }

    if (xi_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(xi_api_key.value()).isEmpty()) {
            input.headers.insert("xi-api-key", ::OpenAPI::toStringValue(xi_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVoicesApi::addVoiceV1VoicesAddPostCallback);
    connect(this, &OAIVoicesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVoicesApi::addVoiceV1VoicesAddPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAddVoiceResponseModel output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addVoiceV1VoicesAddPostSignal(output);
        Q_EMIT addVoiceV1VoicesAddPostSignalFull(worker, output);
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

        Q_EMIT addVoiceV1VoicesAddPostSignalE(output, error_type, error_str);
        Q_EMIT addVoiceV1VoicesAddPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addVoiceV1VoicesAddPostSignalError(output, error_type, error_str);
        Q_EMIT addVoiceV1VoicesAddPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVoicesApi::deleteVoiceV1VoicesVoiceIdDelete(const QString &voice_id, const ::OpenAPI::OptionalParam<QString> &xi_api_key) {
    QString fullPath = QString(_serverConfigs["deleteVoiceV1VoicesVoiceIdDelete"][_serverIndices.value("deleteVoiceV1VoicesVoiceIdDelete")].URL()+"/v1/voices/{voice_id}");
    
    
    {
        QString voice_idPathParam("{");
        voice_idPathParam.append("voice_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "voice_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"voice_id"+pathSuffix : pathPrefix;
        fullPath.replace(voice_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(voice_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    if (xi_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(xi_api_key.value()).isEmpty()) {
            input.headers.insert("xi-api-key", ::OpenAPI::toStringValue(xi_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVoicesApi::deleteVoiceV1VoicesVoiceIdDeleteCallback);
    connect(this, &OAIVoicesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVoicesApi::deleteVoiceV1VoicesVoiceIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteVoiceV1VoicesVoiceIdDeleteSignal(output);
        Q_EMIT deleteVoiceV1VoicesVoiceIdDeleteSignalFull(worker, output);
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

        Q_EMIT deleteVoiceV1VoicesVoiceIdDeleteSignalE(output, error_type, error_str);
        Q_EMIT deleteVoiceV1VoicesVoiceIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteVoiceV1VoicesVoiceIdDeleteSignalError(output, error_type, error_str);
        Q_EMIT deleteVoiceV1VoicesVoiceIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVoicesApi::editVoiceSettingsV1VoicesVoiceIdSettingsEditPost(const QString &voice_id, const OAIVoiceSettingsResponseModel &oai_voice_settings_response_model, const ::OpenAPI::OptionalParam<QString> &xi_api_key) {
    QString fullPath = QString(_serverConfigs["editVoiceSettingsV1VoicesVoiceIdSettingsEditPost"][_serverIndices.value("editVoiceSettingsV1VoicesVoiceIdSettingsEditPost")].URL()+"/v1/voices/{voice_id}/settings/edit");
    
    
    {
        QString voice_idPathParam("{");
        voice_idPathParam.append("voice_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "voice_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"voice_id"+pathSuffix : pathPrefix;
        fullPath.replace(voice_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(voice_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_voice_settings_response_model.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (xi_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(xi_api_key.value()).isEmpty()) {
            input.headers.insert("xi-api-key", ::OpenAPI::toStringValue(xi_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVoicesApi::editVoiceSettingsV1VoicesVoiceIdSettingsEditPostCallback);
    connect(this, &OAIVoicesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVoicesApi::editVoiceSettingsV1VoicesVoiceIdSettingsEditPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignal(output);
        Q_EMIT editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalFull(worker, output);
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

        Q_EMIT editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalE(output, error_type, error_str);
        Q_EMIT editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalError(output, error_type, error_str);
        Q_EMIT editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVoicesApi::editVoiceV1VoicesVoiceIdEditPost(const QString &voice_id, const QString &name, const ::OpenAPI::OptionalParam<QString> &xi_api_key, const ::OpenAPI::OptionalParam<QString> &description, const ::OpenAPI::OptionalParam<QList<OAIHttpFileElement>> &files, const ::OpenAPI::OptionalParam<QString> &labels) {
    QString fullPath = QString(_serverConfigs["editVoiceV1VoicesVoiceIdEditPost"][_serverIndices.value("editVoiceV1VoicesVoiceIdEditPost")].URL()+"/v1/voices/{voice_id}/edit");
    
    
    {
        QString voice_idPathParam("{");
        voice_idPathParam.append("voice_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "voice_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"voice_id"+pathSuffix : pathPrefix;
        fullPath.replace(voice_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(voice_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (description.hasValue())
    {
        input.add_var("description", ::OpenAPI::toStringValue(description.value()));
    }
    if (files.hasValue())
    {
        input.add_file("files", files.value().local_filename, files.value().request_filename, files.value().mime_type);
    }
    if (labels.hasValue())
    {
        input.add_var("labels", ::OpenAPI::toStringValue(labels.value()));
    }
    
    {
        input.add_var("name", ::OpenAPI::toStringValue(name));
    }

    if (xi_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(xi_api_key.value()).isEmpty()) {
            input.headers.insert("xi-api-key", ::OpenAPI::toStringValue(xi_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVoicesApi::editVoiceV1VoicesVoiceIdEditPostCallback);
    connect(this, &OAIVoicesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVoicesApi::editVoiceV1VoicesVoiceIdEditPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT editVoiceV1VoicesVoiceIdEditPostSignal(output);
        Q_EMIT editVoiceV1VoicesVoiceIdEditPostSignalFull(worker, output);
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

        Q_EMIT editVoiceV1VoicesVoiceIdEditPostSignalE(output, error_type, error_str);
        Q_EMIT editVoiceV1VoicesVoiceIdEditPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT editVoiceV1VoicesVoiceIdEditPostSignalError(output, error_type, error_str);
        Q_EMIT editVoiceV1VoicesVoiceIdEditPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVoicesApi::getDefaultVoiceSettingsV1VoicesSettingsDefaultGet() {
    QString fullPath = QString(_serverConfigs["getDefaultVoiceSettingsV1VoicesSettingsDefaultGet"][_serverIndices.value("getDefaultVoiceSettingsV1VoicesSettingsDefaultGet")].URL()+"/v1/voices/settings/default");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVoicesApi::getDefaultVoiceSettingsV1VoicesSettingsDefaultGetCallback);
    connect(this, &OAIVoicesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVoicesApi::getDefaultVoiceSettingsV1VoicesSettingsDefaultGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVoiceSettingsResponseModel output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignal(output);
        Q_EMIT getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalFull(worker, output);
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

        Q_EMIT getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalE(output, error_type, error_str);
        Q_EMIT getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalError(output, error_type, error_str);
        Q_EMIT getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVoicesApi::getVoiceSettingsV1VoicesVoiceIdSettingsGet(const QString &voice_id, const ::OpenAPI::OptionalParam<QString> &xi_api_key) {
    QString fullPath = QString(_serverConfigs["getVoiceSettingsV1VoicesVoiceIdSettingsGet"][_serverIndices.value("getVoiceSettingsV1VoicesVoiceIdSettingsGet")].URL()+"/v1/voices/{voice_id}/settings");
    
    
    {
        QString voice_idPathParam("{");
        voice_idPathParam.append("voice_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "voice_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"voice_id"+pathSuffix : pathPrefix;
        fullPath.replace(voice_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(voice_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (xi_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(xi_api_key.value()).isEmpty()) {
            input.headers.insert("xi-api-key", ::OpenAPI::toStringValue(xi_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVoicesApi::getVoiceSettingsV1VoicesVoiceIdSettingsGetCallback);
    connect(this, &OAIVoicesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVoicesApi::getVoiceSettingsV1VoicesVoiceIdSettingsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVoiceSettingsResponseModel output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getVoiceSettingsV1VoicesVoiceIdSettingsGetSignal(output);
        Q_EMIT getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalFull(worker, output);
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

        Q_EMIT getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalE(output, error_type, error_str);
        Q_EMIT getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalError(output, error_type, error_str);
        Q_EMIT getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVoicesApi::getVoiceV1VoicesVoiceIdGet(const QString &voice_id, const ::OpenAPI::OptionalParam<bool> &with_settings, const ::OpenAPI::OptionalParam<QString> &xi_api_key) {
    QString fullPath = QString(_serverConfigs["getVoiceV1VoicesVoiceIdGet"][_serverIndices.value("getVoiceV1VoicesVoiceIdGet")].URL()+"/v1/voices/{voice_id}");
    
    
    {
        QString voice_idPathParam("{");
        voice_idPathParam.append("voice_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "voice_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"voice_id"+pathSuffix : pathPrefix;
        fullPath.replace(voice_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(voice_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (with_settings.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "with_settings", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("with_settings")).append(querySuffix).append(QUrl::toPercentEncoding(with_settings.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (xi_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(xi_api_key.value()).isEmpty()) {
            input.headers.insert("xi-api-key", ::OpenAPI::toStringValue(xi_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVoicesApi::getVoiceV1VoicesVoiceIdGetCallback);
    connect(this, &OAIVoicesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVoicesApi::getVoiceV1VoicesVoiceIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIVoiceResponseModel output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getVoiceV1VoicesVoiceIdGetSignal(output);
        Q_EMIT getVoiceV1VoicesVoiceIdGetSignalFull(worker, output);
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

        Q_EMIT getVoiceV1VoicesVoiceIdGetSignalE(output, error_type, error_str);
        Q_EMIT getVoiceV1VoicesVoiceIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getVoiceV1VoicesVoiceIdGetSignalError(output, error_type, error_str);
        Q_EMIT getVoiceV1VoicesVoiceIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVoicesApi::getVoicesV1VoicesGet(const ::OpenAPI::OptionalParam<QString> &xi_api_key) {
    QString fullPath = QString(_serverConfigs["getVoicesV1VoicesGet"][_serverIndices.value("getVoicesV1VoicesGet")].URL()+"/v1/voices");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (xi_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(xi_api_key.value()).isEmpty()) {
            input.headers.insert("xi-api-key", ::OpenAPI::toStringValue(xi_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVoicesApi::getVoicesV1VoicesGetCallback);
    connect(this, &OAIVoicesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIVoicesApi::getVoicesV1VoicesGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetVoicesResponseModel output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getVoicesV1VoicesGetSignal(output);
        Q_EMIT getVoicesV1VoicesGetSignalFull(worker, output);
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

        Q_EMIT getVoicesV1VoicesGetSignalE(output, error_type, error_str);
        Q_EMIT getVoicesV1VoicesGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getVoicesV1VoicesGetSignalError(output, error_type, error_str);
        Q_EMIT getVoicesV1VoicesGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVoicesApi::tokenAvailable(){

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
