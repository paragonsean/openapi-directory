/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIStorageAccountCredentialsApi_H
#define OAI_OAIStorageAccountCredentialsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIStorageAccountCredential.h"
#include "OAIStorageAccountCredentialList.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIStorageAccountCredentialsApi : public QObject {
    Q_OBJECT

public:
    OAIStorageAccountCredentialsApi(const int timeOut = 0);
    ~OAIStorageAccountCredentialsApi();

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
    * @param[in]  storage_account_credential_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  parameters OAIStorageAccountCredential [required]
    */
    virtual void storageAccountCredentialsCreateOrUpdate(const QString &storage_account_credential_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version, const OAIStorageAccountCredential &parameters);

    /**
    * @param[in]  storage_account_credential_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void storageAccountCredentialsDelete(const QString &storage_account_credential_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version);

    /**
    * @param[in]  storage_account_credential_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void storageAccountCredentialsGet(const QString &storage_account_credential_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void storageAccountCredentialsListByManager(const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version);


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

    void storageAccountCredentialsCreateOrUpdateCallback(OAIHttpRequestWorker *worker);
    void storageAccountCredentialsDeleteCallback(OAIHttpRequestWorker *worker);
    void storageAccountCredentialsGetCallback(OAIHttpRequestWorker *worker);
    void storageAccountCredentialsListByManagerCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void storageAccountCredentialsCreateOrUpdateSignal(OAIStorageAccountCredential summary);
    void storageAccountCredentialsDeleteSignal();
    void storageAccountCredentialsGetSignal(OAIStorageAccountCredential summary);
    void storageAccountCredentialsListByManagerSignal(OAIStorageAccountCredentialList summary);


    void storageAccountCredentialsCreateOrUpdateSignalFull(OAIHttpRequestWorker *worker, OAIStorageAccountCredential summary);
    void storageAccountCredentialsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void storageAccountCredentialsGetSignalFull(OAIHttpRequestWorker *worker, OAIStorageAccountCredential summary);
    void storageAccountCredentialsListByManagerSignalFull(OAIHttpRequestWorker *worker, OAIStorageAccountCredentialList summary);

    Q_DECL_DEPRECATED_X("Use storageAccountCredentialsCreateOrUpdateSignalError() instead")
    void storageAccountCredentialsCreateOrUpdateSignalE(OAIStorageAccountCredential summary, QNetworkReply::NetworkError error_type, QString error_str);
    void storageAccountCredentialsCreateOrUpdateSignalError(OAIStorageAccountCredential summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageAccountCredentialsDeleteSignalError() instead")
    void storageAccountCredentialsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void storageAccountCredentialsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageAccountCredentialsGetSignalError() instead")
    void storageAccountCredentialsGetSignalE(OAIStorageAccountCredential summary, QNetworkReply::NetworkError error_type, QString error_str);
    void storageAccountCredentialsGetSignalError(OAIStorageAccountCredential summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageAccountCredentialsListByManagerSignalError() instead")
    void storageAccountCredentialsListByManagerSignalE(OAIStorageAccountCredentialList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void storageAccountCredentialsListByManagerSignalError(OAIStorageAccountCredentialList summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use storageAccountCredentialsCreateOrUpdateSignalErrorFull() instead")
    void storageAccountCredentialsCreateOrUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void storageAccountCredentialsCreateOrUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageAccountCredentialsDeleteSignalErrorFull() instead")
    void storageAccountCredentialsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void storageAccountCredentialsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageAccountCredentialsGetSignalErrorFull() instead")
    void storageAccountCredentialsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void storageAccountCredentialsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use storageAccountCredentialsListByManagerSignalErrorFull() instead")
    void storageAccountCredentialsListByManagerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void storageAccountCredentialsListByManagerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
