/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPrivateEndpointConnectionsApi_H
#define OAI_OAIPrivateEndpointConnectionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICloudError.h"
#include "OAIPrivateEndpointConnection.h"
#include "OAIPrivateEndpointConnectionListResult.h"
#include "OAITagsObject.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPrivateEndpointConnectionsApi : public QObject {
    Q_OBJECT

public:
    OAIPrivateEndpointConnectionsApi(const int timeOut = 0);
    ~OAIPrivateEndpointConnectionsApi();

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
    * @param[in]  server_name QString [required]
    * @param[in]  private_endpoint_connection_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  parameters OAIPrivateEndpointConnection [required]
    */
    virtual void privateEndpointConnectionsCreateOrUpdate(const QString &resource_group_name, const QString &server_name, const QString &private_endpoint_connection_name, const QString &subscription_id, const QString &api_version, const OAIPrivateEndpointConnection &parameters);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  server_name QString [required]
    * @param[in]  private_endpoint_connection_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void privateEndpointConnectionsDelete(const QString &resource_group_name, const QString &server_name, const QString &private_endpoint_connection_name, const QString &subscription_id, const QString &api_version);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  server_name QString [required]
    * @param[in]  private_endpoint_connection_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void privateEndpointConnectionsGet(const QString &resource_group_name, const QString &server_name, const QString &private_endpoint_connection_name, const QString &subscription_id, const QString &api_version);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  server_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void privateEndpointConnectionsListByServer(const QString &resource_group_name, const QString &server_name, const QString &subscription_id, const QString &api_version);

    /**
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  server_name QString [required]
    * @param[in]  private_endpoint_connection_name QString [required]
    * @param[in]  parameters OAITagsObject [required]
    */
    virtual void privateEndpointConnectionsUpdateTags(const QString &api_version, const QString &subscription_id, const QString &resource_group_name, const QString &server_name, const QString &private_endpoint_connection_name, const OAITagsObject &parameters);


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

    void privateEndpointConnectionsCreateOrUpdateCallback(OAIHttpRequestWorker *worker);
    void privateEndpointConnectionsDeleteCallback(OAIHttpRequestWorker *worker);
    void privateEndpointConnectionsGetCallback(OAIHttpRequestWorker *worker);
    void privateEndpointConnectionsListByServerCallback(OAIHttpRequestWorker *worker);
    void privateEndpointConnectionsUpdateTagsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void privateEndpointConnectionsCreateOrUpdateSignal(OAIPrivateEndpointConnection summary);
    void privateEndpointConnectionsDeleteSignal();
    void privateEndpointConnectionsGetSignal(OAIPrivateEndpointConnection summary);
    void privateEndpointConnectionsListByServerSignal(OAIPrivateEndpointConnectionListResult summary);
    void privateEndpointConnectionsUpdateTagsSignal(OAIPrivateEndpointConnection summary);


    void privateEndpointConnectionsCreateOrUpdateSignalFull(OAIHttpRequestWorker *worker, OAIPrivateEndpointConnection summary);
    void privateEndpointConnectionsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void privateEndpointConnectionsGetSignalFull(OAIHttpRequestWorker *worker, OAIPrivateEndpointConnection summary);
    void privateEndpointConnectionsListByServerSignalFull(OAIHttpRequestWorker *worker, OAIPrivateEndpointConnectionListResult summary);
    void privateEndpointConnectionsUpdateTagsSignalFull(OAIHttpRequestWorker *worker, OAIPrivateEndpointConnection summary);

    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsCreateOrUpdateSignalError() instead")
    void privateEndpointConnectionsCreateOrUpdateSignalE(OAIPrivateEndpointConnection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsCreateOrUpdateSignalError(OAIPrivateEndpointConnection summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsDeleteSignalError() instead")
    void privateEndpointConnectionsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsGetSignalError() instead")
    void privateEndpointConnectionsGetSignalE(OAIPrivateEndpointConnection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsGetSignalError(OAIPrivateEndpointConnection summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsListByServerSignalError() instead")
    void privateEndpointConnectionsListByServerSignalE(OAIPrivateEndpointConnectionListResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsListByServerSignalError(OAIPrivateEndpointConnectionListResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsUpdateTagsSignalError() instead")
    void privateEndpointConnectionsUpdateTagsSignalE(OAIPrivateEndpointConnection summary, QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsUpdateTagsSignalError(OAIPrivateEndpointConnection summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsCreateOrUpdateSignalErrorFull() instead")
    void privateEndpointConnectionsCreateOrUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsCreateOrUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsDeleteSignalErrorFull() instead")
    void privateEndpointConnectionsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsGetSignalErrorFull() instead")
    void privateEndpointConnectionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsListByServerSignalErrorFull() instead")
    void privateEndpointConnectionsListByServerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsListByServerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use privateEndpointConnectionsUpdateTagsSignalErrorFull() instead")
    void privateEndpointConnectionsUpdateTagsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void privateEndpointConnectionsUpdateTagsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
