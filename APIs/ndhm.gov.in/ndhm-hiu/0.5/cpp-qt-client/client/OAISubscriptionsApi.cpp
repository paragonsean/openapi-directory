/**
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISubscriptionsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAISubscriptionsApi::OAISubscriptionsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAISubscriptionsApi::~OAISubscriptionsApi() {
}

void OAISubscriptionsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://dev.ndhm.gov.in/gateway"),
    "Sandbox",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("v05SubscriptionRequestsHiuNotifyPost", defaultConf);
    _serverIndices.insert("v05SubscriptionRequestsHiuNotifyPost", 0);
    _serverConfigs.insert("v05SubscriptionRequestsHiuOnInitPost", defaultConf);
    _serverIndices.insert("v05SubscriptionRequestsHiuOnInitPost", 0);
    _serverConfigs.insert("v05SubscriptionsHiuNotifyPost", defaultConf);
    _serverIndices.insert("v05SubscriptionsHiuNotifyPost", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAISubscriptionsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAISubscriptionsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAISubscriptionsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAISubscriptionsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAISubscriptionsApi::setUsername(const QString &username) {
    _username = username;
}

void OAISubscriptionsApi::setPassword(const QString &password) {
    _password = password;
}


void OAISubscriptionsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAISubscriptionsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAISubscriptionsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAISubscriptionsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAISubscriptionsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAISubscriptionsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAISubscriptionsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAISubscriptionsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAISubscriptionsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAISubscriptionsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAISubscriptionsApi::getParamStylePrefix(const QString &style) {
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

QString OAISubscriptionsApi::getParamStyleSuffix(const QString &style) {
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

QString OAISubscriptionsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAISubscriptionsApi::v05SubscriptionRequestsHiuNotifyPost(const QString &authorization, const QString &x_hiu_id, const OAISubscriptionApprovalNotification &oai_subscription_approval_notification) {
    QString fullPath = QString(_serverConfigs["v05SubscriptionRequestsHiuNotifyPost"][_serverIndices.value("v05SubscriptionRequestsHiuNotifyPost")].URL()+"/v0.5/subscription-requests/hiu/notify");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_subscription_approval_notification.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(authorization).isEmpty()) {
            input.headers.insert("Authorization", ::OpenAPI::toStringValue(authorization));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_hiu_id).isEmpty()) {
            input.headers.insert("X-HIU-ID", ::OpenAPI::toStringValue(x_hiu_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAISubscriptionsApi::v05SubscriptionRequestsHiuNotifyPostCallback);
    connect(this, &OAISubscriptionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAISubscriptionsApi::v05SubscriptionRequestsHiuNotifyPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v05SubscriptionRequestsHiuNotifyPostSignal();
        Q_EMIT v05SubscriptionRequestsHiuNotifyPostSignalFull(worker);
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

        Q_EMIT v05SubscriptionRequestsHiuNotifyPostSignalE(error_type, error_str);
        Q_EMIT v05SubscriptionRequestsHiuNotifyPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v05SubscriptionRequestsHiuNotifyPostSignalError(error_type, error_str);
        Q_EMIT v05SubscriptionRequestsHiuNotifyPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAISubscriptionsApi::v05SubscriptionRequestsHiuOnInitPost(const QString &authorization, const QString &x_hiu_id, const OAIHIUSubscriptionRequestReceipt &oaihiu_subscription_request_receipt) {
    QString fullPath = QString(_serverConfigs["v05SubscriptionRequestsHiuOnInitPost"][_serverIndices.value("v05SubscriptionRequestsHiuOnInitPost")].URL()+"/v0.5/subscription-requests/hiu/on-init");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oaihiu_subscription_request_receipt.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(authorization).isEmpty()) {
            input.headers.insert("Authorization", ::OpenAPI::toStringValue(authorization));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_hiu_id).isEmpty()) {
            input.headers.insert("X-HIU-ID", ::OpenAPI::toStringValue(x_hiu_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAISubscriptionsApi::v05SubscriptionRequestsHiuOnInitPostCallback);
    connect(this, &OAISubscriptionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAISubscriptionsApi::v05SubscriptionRequestsHiuOnInitPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v05SubscriptionRequestsHiuOnInitPostSignal();
        Q_EMIT v05SubscriptionRequestsHiuOnInitPostSignalFull(worker);
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

        Q_EMIT v05SubscriptionRequestsHiuOnInitPostSignalE(error_type, error_str);
        Q_EMIT v05SubscriptionRequestsHiuOnInitPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v05SubscriptionRequestsHiuOnInitPostSignalError(error_type, error_str);
        Q_EMIT v05SubscriptionRequestsHiuOnInitPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAISubscriptionsApi::v05SubscriptionsHiuNotifyPost(const QString &authorization, const QString &x_hiu_id, const OAIHIUSubscriptionNotification &oaihiu_subscription_notification) {
    QString fullPath = QString(_serverConfigs["v05SubscriptionsHiuNotifyPost"][_serverIndices.value("v05SubscriptionsHiuNotifyPost")].URL()+"/v0.5/subscriptions/hiu/notify");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oaihiu_subscription_notification.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(authorization).isEmpty()) {
            input.headers.insert("Authorization", ::OpenAPI::toStringValue(authorization));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_hiu_id).isEmpty()) {
            input.headers.insert("X-HIU-ID", ::OpenAPI::toStringValue(x_hiu_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAISubscriptionsApi::v05SubscriptionsHiuNotifyPostCallback);
    connect(this, &OAISubscriptionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAISubscriptionsApi::v05SubscriptionsHiuNotifyPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v05SubscriptionsHiuNotifyPostSignal();
        Q_EMIT v05SubscriptionsHiuNotifyPostSignalFull(worker);
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

        Q_EMIT v05SubscriptionsHiuNotifyPostSignalE(error_type, error_str);
        Q_EMIT v05SubscriptionsHiuNotifyPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v05SubscriptionsHiuNotifyPostSignalError(error_type, error_str);
        Q_EMIT v05SubscriptionsHiuNotifyPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAISubscriptionsApi::tokenAvailable(){

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
