/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIExpressRouteGatewaysApi_H
#define OAI_OAIExpressRouteGatewaysApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIExpressRouteGateway.h"
#include "OAIExpressRouteGatewayList.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIExpressRouteGatewaysApi : public QObject {
    Q_OBJECT

public:
    OAIExpressRouteGatewaysApi(const int timeOut = 0);
    ~OAIExpressRouteGatewaysApi();

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
    * @param[in]  express_route_gateway_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  put_express_route_gateway_parameters OAIExpressRouteGateway [required]
    */
    virtual void expressRouteGatewaysCreateOrUpdate(const QString &resource_group_name, const QString &express_route_gateway_name, const QString &api_version, const QString &subscription_id, const OAIExpressRouteGateway &put_express_route_gateway_parameters);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  express_route_gateway_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    */
    virtual void expressRouteGatewaysDelete(const QString &resource_group_name, const QString &express_route_gateway_name, const QString &api_version, const QString &subscription_id);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  express_route_gateway_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    */
    virtual void expressRouteGatewaysGet(const QString &resource_group_name, const QString &express_route_gateway_name, const QString &api_version, const QString &subscription_id);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    */
    virtual void expressRouteGatewaysListByResourceGroup(const QString &resource_group_name, const QString &api_version, const QString &subscription_id);

    /**
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    */
    virtual void expressRouteGatewaysListBySubscription(const QString &api_version, const QString &subscription_id);


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

    void expressRouteGatewaysCreateOrUpdateCallback(OAIHttpRequestWorker *worker);
    void expressRouteGatewaysDeleteCallback(OAIHttpRequestWorker *worker);
    void expressRouteGatewaysGetCallback(OAIHttpRequestWorker *worker);
    void expressRouteGatewaysListByResourceGroupCallback(OAIHttpRequestWorker *worker);
    void expressRouteGatewaysListBySubscriptionCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void expressRouteGatewaysCreateOrUpdateSignal(OAIExpressRouteGateway summary);
    void expressRouteGatewaysDeleteSignal();
    void expressRouteGatewaysGetSignal(OAIExpressRouteGateway summary);
    void expressRouteGatewaysListByResourceGroupSignal(OAIExpressRouteGatewayList summary);
    void expressRouteGatewaysListBySubscriptionSignal(OAIExpressRouteGatewayList summary);


    void expressRouteGatewaysCreateOrUpdateSignalFull(OAIHttpRequestWorker *worker, OAIExpressRouteGateway summary);
    void expressRouteGatewaysDeleteSignalFull(OAIHttpRequestWorker *worker);
    void expressRouteGatewaysGetSignalFull(OAIHttpRequestWorker *worker, OAIExpressRouteGateway summary);
    void expressRouteGatewaysListByResourceGroupSignalFull(OAIHttpRequestWorker *worker, OAIExpressRouteGatewayList summary);
    void expressRouteGatewaysListBySubscriptionSignalFull(OAIHttpRequestWorker *worker, OAIExpressRouteGatewayList summary);

    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysCreateOrUpdateSignalError() instead")
    void expressRouteGatewaysCreateOrUpdateSignalE(OAIExpressRouteGateway summary, QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysCreateOrUpdateSignalError(OAIExpressRouteGateway summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysDeleteSignalError() instead")
    void expressRouteGatewaysDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysGetSignalError() instead")
    void expressRouteGatewaysGetSignalE(OAIExpressRouteGateway summary, QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysGetSignalError(OAIExpressRouteGateway summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysListByResourceGroupSignalError() instead")
    void expressRouteGatewaysListByResourceGroupSignalE(OAIExpressRouteGatewayList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysListByResourceGroupSignalError(OAIExpressRouteGatewayList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysListBySubscriptionSignalError() instead")
    void expressRouteGatewaysListBySubscriptionSignalE(OAIExpressRouteGatewayList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysListBySubscriptionSignalError(OAIExpressRouteGatewayList summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysCreateOrUpdateSignalErrorFull() instead")
    void expressRouteGatewaysCreateOrUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysCreateOrUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysDeleteSignalErrorFull() instead")
    void expressRouteGatewaysDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysGetSignalErrorFull() instead")
    void expressRouteGatewaysGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysListByResourceGroupSignalErrorFull() instead")
    void expressRouteGatewaysListByResourceGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysListByResourceGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use expressRouteGatewaysListBySubscriptionSignalErrorFull() instead")
    void expressRouteGatewaysListBySubscriptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void expressRouteGatewaysListBySubscriptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
