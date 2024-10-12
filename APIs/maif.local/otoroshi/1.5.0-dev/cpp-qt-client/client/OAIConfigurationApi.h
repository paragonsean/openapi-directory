/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIConfigurationApi_H
#define OAI_OAIConfigurationApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGlobalConfig.h"
#include "OAIPatch_inner.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIConfigurationApi : public QObject {
    Q_OBJECT

public:
    OAIConfigurationApi(const int timeOut = 0);
    ~OAIConfigurationApi();

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


    virtual void globalConfig();

    /**
    * @param[in]  oai_patch_inner QList<OAIPatch_inner> [optional]
    */
    virtual void patchGlobalConfig(const ::OpenAPI::OptionalParam<QList<OAIPatch_inner>> &oai_patch_inner = ::OpenAPI::OptionalParam<QList<OAIPatch_inner>>());

    /**
    * @param[in]  oai_global_config OAIGlobalConfig [optional]
    */
    virtual void putGlobalConfig(const ::OpenAPI::OptionalParam<OAIGlobalConfig> &oai_global_config = ::OpenAPI::OptionalParam<OAIGlobalConfig>());


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

    void globalConfigCallback(OAIHttpRequestWorker *worker);
    void patchGlobalConfigCallback(OAIHttpRequestWorker *worker);
    void putGlobalConfigCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void globalConfigSignal(OAIGlobalConfig summary);
    void patchGlobalConfigSignal(OAIGlobalConfig summary);
    void putGlobalConfigSignal(OAIGlobalConfig summary);


    void globalConfigSignalFull(OAIHttpRequestWorker *worker, OAIGlobalConfig summary);
    void patchGlobalConfigSignalFull(OAIHttpRequestWorker *worker, OAIGlobalConfig summary);
    void putGlobalConfigSignalFull(OAIHttpRequestWorker *worker, OAIGlobalConfig summary);

    Q_DECL_DEPRECATED_X("Use globalConfigSignalError() instead")
    void globalConfigSignalE(OAIGlobalConfig summary, QNetworkReply::NetworkError error_type, QString error_str);
    void globalConfigSignalError(OAIGlobalConfig summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchGlobalConfigSignalError() instead")
    void patchGlobalConfigSignalE(OAIGlobalConfig summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patchGlobalConfigSignalError(OAIGlobalConfig summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putGlobalConfigSignalError() instead")
    void putGlobalConfigSignalE(OAIGlobalConfig summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putGlobalConfigSignalError(OAIGlobalConfig summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use globalConfigSignalErrorFull() instead")
    void globalConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void globalConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchGlobalConfigSignalErrorFull() instead")
    void patchGlobalConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patchGlobalConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putGlobalConfigSignalErrorFull() instead")
    void putGlobalConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putGlobalConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
