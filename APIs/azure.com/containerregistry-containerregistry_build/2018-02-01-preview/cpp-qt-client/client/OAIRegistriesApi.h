/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIRegistriesApi_H
#define OAI_OAIRegistriesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBuild.h"
#include "OAIQueueBuildRequest.h"
#include "OAISourceUploadDefinition.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIRegistriesApi : public QObject {
    Q_OBJECT

public:
    OAIRegistriesApi(const int timeOut = 0);
    ~OAIRegistriesApi();

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
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void registriesGetBuildSourceUploadUrl(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  build_request OAIQueueBuildRequest [required]
    */
    virtual void registriesQueueBuild(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const OAIQueueBuildRequest &build_request);


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

    void registriesGetBuildSourceUploadUrlCallback(OAIHttpRequestWorker *worker);
    void registriesQueueBuildCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void registriesGetBuildSourceUploadUrlSignal(OAISourceUploadDefinition summary);
    void registriesQueueBuildSignal(OAIBuild summary);


    void registriesGetBuildSourceUploadUrlSignalFull(OAIHttpRequestWorker *worker, OAISourceUploadDefinition summary);
    void registriesQueueBuildSignalFull(OAIHttpRequestWorker *worker, OAIBuild summary);

    Q_DECL_DEPRECATED_X("Use registriesGetBuildSourceUploadUrlSignalError() instead")
    void registriesGetBuildSourceUploadUrlSignalE(OAISourceUploadDefinition summary, QNetworkReply::NetworkError error_type, QString error_str);
    void registriesGetBuildSourceUploadUrlSignalError(OAISourceUploadDefinition summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use registriesQueueBuildSignalError() instead")
    void registriesQueueBuildSignalE(OAIBuild summary, QNetworkReply::NetworkError error_type, QString error_str);
    void registriesQueueBuildSignalError(OAIBuild summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use registriesGetBuildSourceUploadUrlSignalErrorFull() instead")
    void registriesGetBuildSourceUploadUrlSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void registriesGetBuildSourceUploadUrlSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use registriesQueueBuildSignalErrorFull() instead")
    void registriesQueueBuildSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void registriesQueueBuildSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
