/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIUpdateSystemApi_H
#define OAI_OAIUpdateSystemApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAPI_Models_ApiError.h"
#include "OAIUpdateSystem_Models_CheckinResult.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIUpdateSystemApi : public QObject {
    Q_OBJECT

public:
    OAIUpdateSystemApi(const int timeOut = 0);
    ~OAIUpdateSystemApi();

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

    /**
    * @param[in]  client_id QString [required]
    * @param[in]  expired bool [required]
    */
    virtual void updateSystemGetCachedFiles(const QString &client_id, const bool &expired);

    /**
    * @param[in]  client_id QString [required]
    * @param[in]  preview bool [required]
    * @param[in]  run_all_inventories bool [optional]
    */
    virtual void updateSystemGetCheckin(const QString &client_id, const bool &preview, const ::OpenAPI::OptionalParam<bool> &run_all_inventories = ::OpenAPI::OptionalParam<bool>());


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

    void updateSystemGetCachedFilesCallback(OAIHttpRequestWorker *worker);
    void updateSystemGetCheckinCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void updateSystemGetCachedFilesSignal(QList<QString> summary);
    void updateSystemGetCheckinSignal(OAIUpdateSystem_Models_CheckinResult summary);


    void updateSystemGetCachedFilesSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void updateSystemGetCheckinSignalFull(OAIHttpRequestWorker *worker, OAIUpdateSystem_Models_CheckinResult summary);

    Q_DECL_DEPRECATED_X("Use updateSystemGetCachedFilesSignalError() instead")
    void updateSystemGetCachedFilesSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateSystemGetCachedFilesSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateSystemGetCheckinSignalError() instead")
    void updateSystemGetCheckinSignalE(OAIUpdateSystem_Models_CheckinResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateSystemGetCheckinSignalError(OAIUpdateSystem_Models_CheckinResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use updateSystemGetCachedFilesSignalErrorFull() instead")
    void updateSystemGetCachedFilesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateSystemGetCachedFilesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateSystemGetCheckinSignalErrorFull() instead")
    void updateSystemGetCheckinSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateSystemGetCheckinSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
