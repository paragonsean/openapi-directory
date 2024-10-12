/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIForgotHealthIdNumberApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIForgotHealthIdNumberApi::OAIForgotHealthIdNumberApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIForgotHealthIdNumberApi::~OAIForgotHealthIdNumberApi() {
}

void OAIForgotHealthIdNumberApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://healthidsbx.ndhm.gov.in/api"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("generateAadharOTPUsingPOST1", defaultConf);
    _serverIndices.insert("generateAadharOTPUsingPOST1", 0);
    _serverConfigs.insert("generateMobileOTPUsingPOST", defaultConf);
    _serverIndices.insert("generateMobileOTPUsingPOST", 0);
    _serverConfigs.insert("retrievalHealthIdByAadharUsingPOST", defaultConf);
    _serverIndices.insert("retrievalHealthIdByAadharUsingPOST", 0);
    _serverConfigs.insert("retrievalHealthIdByMobileUsingPOST", defaultConf);
    _serverIndices.insert("retrievalHealthIdByMobileUsingPOST", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIForgotHealthIdNumberApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIForgotHealthIdNumberApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIForgotHealthIdNumberApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIForgotHealthIdNumberApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIForgotHealthIdNumberApi::setUsername(const QString &username) {
    _username = username;
}

void OAIForgotHealthIdNumberApi::setPassword(const QString &password) {
    _password = password;
}


void OAIForgotHealthIdNumberApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIForgotHealthIdNumberApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIForgotHealthIdNumberApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIForgotHealthIdNumberApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIForgotHealthIdNumberApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIForgotHealthIdNumberApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIForgotHealthIdNumberApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIForgotHealthIdNumberApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIForgotHealthIdNumberApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIForgotHealthIdNumberApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIForgotHealthIdNumberApi::getParamStylePrefix(const QString &style) {
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

QString OAIForgotHealthIdNumberApi::getParamStyleSuffix(const QString &style) {
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

QString OAIForgotHealthIdNumberApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIForgotHealthIdNumberApi::generateAadharOTPUsingPOST1(const OAIAadharOtpGenerateRequestPayLoad &generate_otp_request, const ::OpenAPI::OptionalParam<QString> &accept_language) {
    QString fullPath = QString(_serverConfigs["generateAadharOTPUsingPOST1"][_serverIndices.value("generateAadharOTPUsingPOST1")].URL()+"/v1/forgot/healthId/aadhaar/generateOtp");
    
    if (_apiKeys.contains("Authorization")) {
        addHeaders("Authorization",_apiKeys.find("Authorization").value());
    }
    
    if (_apiKeys.contains("X-HIP-ID")) {
        addHeaders("X-HIP-ID",_apiKeys.find("X-HIP-ID").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = generate_otp_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (accept_language.hasValue())
    {
        if (!::OpenAPI::toStringValue(accept_language.value()).isEmpty()) {
            input.headers.insert("Accept-Language", ::OpenAPI::toStringValue(accept_language.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIForgotHealthIdNumberApi::generateAadharOTPUsingPOST1Callback);
    connect(this, &OAIForgotHealthIdNumberApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIForgotHealthIdNumberApi::generateAadharOTPUsingPOST1Callback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITxnResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT generateAadharOTPUsingPOST1Signal(output);
        Q_EMIT generateAadharOTPUsingPOST1SignalFull(worker, output);
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

        Q_EMIT generateAadharOTPUsingPOST1SignalE(output, error_type, error_str);
        Q_EMIT generateAadharOTPUsingPOST1SignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT generateAadharOTPUsingPOST1SignalError(output, error_type, error_str);
        Q_EMIT generateAadharOTPUsingPOST1SignalErrorFull(worker, error_type, error_str);
    }
}

void OAIForgotHealthIdNumberApi::generateMobileOTPUsingPOST(const OAIGenerateMobileOTPRequest &generate_otp_request, const ::OpenAPI::OptionalParam<QString> &accept_language) {
    QString fullPath = QString(_serverConfigs["generateMobileOTPUsingPOST"][_serverIndices.value("generateMobileOTPUsingPOST")].URL()+"/v1/forgot/healthId/mobile/generateOtp");
    
    if (_apiKeys.contains("Authorization")) {
        addHeaders("Authorization",_apiKeys.find("Authorization").value());
    }
    
    if (_apiKeys.contains("X-HIP-ID")) {
        addHeaders("X-HIP-ID",_apiKeys.find("X-HIP-ID").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = generate_otp_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (accept_language.hasValue())
    {
        if (!::OpenAPI::toStringValue(accept_language.value()).isEmpty()) {
            input.headers.insert("Accept-Language", ::OpenAPI::toStringValue(accept_language.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIForgotHealthIdNumberApi::generateMobileOTPUsingPOSTCallback);
    connect(this, &OAIForgotHealthIdNumberApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIForgotHealthIdNumberApi::generateMobileOTPUsingPOSTCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITxnResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT generateMobileOTPUsingPOSTSignal(output);
        Q_EMIT generateMobileOTPUsingPOSTSignalFull(worker, output);
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

        Q_EMIT generateMobileOTPUsingPOSTSignalE(output, error_type, error_str);
        Q_EMIT generateMobileOTPUsingPOSTSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT generateMobileOTPUsingPOSTSignalError(output, error_type, error_str);
        Q_EMIT generateMobileOTPUsingPOSTSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIForgotHealthIdNumberApi::retrievalHealthIdByAadharUsingPOST(const OAIAuthAccountAadhaarOTPRequest &auth_account_aadhaar_otp_request, const ::OpenAPI::OptionalParam<QString> &accept_language) {
    QString fullPath = QString(_serverConfigs["retrievalHealthIdByAadharUsingPOST"][_serverIndices.value("retrievalHealthIdByAadharUsingPOST")].URL()+"/v1/forgot/healthId/aadhaar");
    
    if (_apiKeys.contains("Authorization")) {
        addHeaders("Authorization",_apiKeys.find("Authorization").value());
    }
    
    if (_apiKeys.contains("X-HIP-ID")) {
        addHeaders("X-HIP-ID",_apiKeys.find("X-HIP-ID").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = auth_account_aadhaar_otp_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (accept_language.hasValue())
    {
        if (!::OpenAPI::toStringValue(accept_language.value()).isEmpty()) {
            input.headers.insert("Accept-Language", ::OpenAPI::toStringValue(accept_language.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIForgotHealthIdNumberApi::retrievalHealthIdByAadharUsingPOSTCallback);
    connect(this, &OAIForgotHealthIdNumberApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIForgotHealthIdNumberApi::retrievalHealthIdByAadharUsingPOSTCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIRetrieveHealthIdPayloadResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT retrievalHealthIdByAadharUsingPOSTSignal(output);
        Q_EMIT retrievalHealthIdByAadharUsingPOSTSignalFull(worker, output);
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

        Q_EMIT retrievalHealthIdByAadharUsingPOSTSignalE(output, error_type, error_str);
        Q_EMIT retrievalHealthIdByAadharUsingPOSTSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT retrievalHealthIdByAadharUsingPOSTSignalError(output, error_type, error_str);
        Q_EMIT retrievalHealthIdByAadharUsingPOSTSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIForgotHealthIdNumberApi::retrievalHealthIdByMobileUsingPOST(const OAIRetriveHealthIdMobilePayLoad &retrive_health_id_mobile_pay_load, const ::OpenAPI::OptionalParam<QString> &accept_language) {
    QString fullPath = QString(_serverConfigs["retrievalHealthIdByMobileUsingPOST"][_serverIndices.value("retrievalHealthIdByMobileUsingPOST")].URL()+"/v1/forgot/healthId/mobile");
    
    if (_apiKeys.contains("Authorization")) {
        addHeaders("Authorization",_apiKeys.find("Authorization").value());
    }
    
    if (_apiKeys.contains("X-HIP-ID")) {
        addHeaders("X-HIP-ID",_apiKeys.find("X-HIP-ID").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = retrive_health_id_mobile_pay_load.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (accept_language.hasValue())
    {
        if (!::OpenAPI::toStringValue(accept_language.value()).isEmpty()) {
            input.headers.insert("Accept-Language", ::OpenAPI::toStringValue(accept_language.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIForgotHealthIdNumberApi::retrievalHealthIdByMobileUsingPOSTCallback);
    connect(this, &OAIForgotHealthIdNumberApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIForgotHealthIdNumberApi::retrievalHealthIdByMobileUsingPOSTCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIRetrieveHealthIdPayloadResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT retrievalHealthIdByMobileUsingPOSTSignal(output);
        Q_EMIT retrievalHealthIdByMobileUsingPOSTSignalFull(worker, output);
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

        Q_EMIT retrievalHealthIdByMobileUsingPOSTSignalE(output, error_type, error_str);
        Q_EMIT retrievalHealthIdByMobileUsingPOSTSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT retrievalHealthIdByMobileUsingPOSTSignalError(output, error_type, error_str);
        Q_EMIT retrievalHealthIdByMobileUsingPOSTSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIForgotHealthIdNumberApi::tokenAvailable(){

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
