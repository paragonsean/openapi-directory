/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage Caches.
 *
 * The version of the OpenAPI document: 2019-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIStorageTargetsApi_H
#define OAI_OAIStorageTargetsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICloudError.h"
#include "OAIObject.h"
#include "OAIStorageTarget.h"
#include "OAIStorageTargetsResult.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIStorageTargetsApi : public QObject {
    Q_OBJECT

public:
    OAIStorageTargetsApi(const int timeOut = 0);
    ~OAIStorageTargetsApi();

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
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  cache_name QString [required]
    * @param[in]  storage_target_name QString [required]
    * @param[in]  storagetarget OAIStorageTarget [optional]
    */
    virtual void storageTargetsCreateOrUpdate(const QString &resource_group_name, const QString &api_version, const QString &subscription_id, const QString &cache_name, const QString &storage_target_name, const ::OpenAPI::OptionalParam<OAIStorageTarget> &storagetarget = ::OpenAPI::OptionalParam<OAIStorageTarget>());

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  cache_name QString [required]
    * @param[in]  storage_target_name QString [required]
    */
    virtual void storageTargetsDelete(const QString &resource_group_name, const QString &api_version, const QString &subscription_id, const QString &cache_name, const QString &storage_target_name);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  cache_name QString [required]
    * @param[in]  storage_target_name QString [required]
    */
    virtual void storageTargetsGet(const QString &resource_group_name, const QString &api_version, const QString &subscription_id, const QString &cache_name, const QString &storage_target_name);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  cache_name QString [required]
    */
    virtual void storageTargetsListByCache(const QString &resource_group_name, const QString &api_version, const QString &subscription_id, const QString &cache_name);


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

    void storageTargetsCreateOrUpdateCallback(OAIHttpRequestWorker *worker);
    void storageTargetsDeleteCallback(OAIHttpRequestWorker *worker);
    void storageTargetsGetCallback(OAIHttpRequestWorker *worker);
    void storageTargetsListByCacheCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void storageTargetsCreateOrUpdateSignal(OAIStorageTarget summary);
    void storageTargetsDeleteSignal(OAIObject summary);
    void storageTargetsGetSignal(OAIStorageTarget summary);
    void storageTargetsListByCacheSignal(OAIStorageTargetsResult summary);


    void storageTargetsCreateOrUpdateSignalFull(OAIHttpRequestWorker *worker, OAIStorageTarget summary);
    void storageTargetsDeleteSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void storageTargetsGetSignalFull(OAIHttpRequestWorker *worker, OAIStorageTarget summary);
    void storageTargetsListByCacheSignalFull(OAIHttpRequestWorker *worker, OAIStorageTargetsResult summary);

    Q_DECL_DEPRECATED_X("Use storageTargetsCreateOrUpdateSignalError() instead")
    void storageTargetsCreateOrUpdateSignalE(OAIStorageTarget summary, QNetworkReply::NetworkError error_type, QString error_str);
    void storageTargetsCreateOrUpdateSignalError(OAIStorageTarget summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageTargetsDeleteSignalError() instead")
    void storageTargetsDeleteSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void storageTargetsDeleteSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageTargetsGetSignalError() instead")
    void storageTargetsGetSignalE(OAIStorageTarget summary, QNetworkReply::NetworkError error_type, QString error_str);
    void storageTargetsGetSignalError(OAIStorageTarget summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageTargetsListByCacheSignalError() instead")
    void storageTargetsListByCacheSignalE(OAIStorageTargetsResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void storageTargetsListByCacheSignalError(OAIStorageTargetsResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use storageTargetsCreateOrUpdateSignalErrorFull() instead")
    void storageTargetsCreateOrUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void storageTargetsCreateOrUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageTargetsDeleteSignalErrorFull() instead")
    void storageTargetsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void storageTargetsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageTargetsGetSignalErrorFull() instead")
    void storageTargetsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void storageTargetsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageTargetsListByCacheSignalErrorFull() instead")
    void storageTargetsListByCacheSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void storageTargetsListByCacheSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
