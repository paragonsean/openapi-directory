/**
 * AzureStack Azure Bridge Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICustomerSubscriptionApi_H
#define OAI_OAICustomerSubscriptionApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICustomerSubscription.h"
#include "OAICustomerSubscriptionList.h"
#include "OAICustomerSubscriptions_List_default_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICustomerSubscriptionApi : public QObject {
    Q_OBJECT

public:
    OAICustomerSubscriptionApi(const int timeOut = 0);
    ~OAICustomerSubscriptionApi();

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
    * @param[in]  resource_group QString [required]
    * @param[in]  registration_name QString [required]
    * @param[in]  customer_subscription_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  customer_creation_parameters OAICustomerSubscription [required]
    */
    virtual void customerSubscriptionsCreate(const QString &subscription_id, const QString &resource_group, const QString &registration_name, const QString &customer_subscription_name, const QString &api_version, const OAICustomerSubscription &customer_creation_parameters);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group QString [required]
    * @param[in]  registration_name QString [required]
    * @param[in]  customer_subscription_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void customerSubscriptionsDelete(const QString &subscription_id, const QString &resource_group, const QString &registration_name, const QString &customer_subscription_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group QString [required]
    * @param[in]  registration_name QString [required]
    * @param[in]  customer_subscription_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void customerSubscriptionsGet(const QString &subscription_id, const QString &resource_group, const QString &registration_name, const QString &customer_subscription_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group QString [required]
    * @param[in]  registration_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void customerSubscriptionsList(const QString &subscription_id, const QString &resource_group, const QString &registration_name, const QString &api_version);


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

    void customerSubscriptionsCreateCallback(OAIHttpRequestWorker *worker);
    void customerSubscriptionsDeleteCallback(OAIHttpRequestWorker *worker);
    void customerSubscriptionsGetCallback(OAIHttpRequestWorker *worker);
    void customerSubscriptionsListCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void customerSubscriptionsCreateSignal(OAICustomerSubscription summary);
    void customerSubscriptionsDeleteSignal();
    void customerSubscriptionsGetSignal(OAICustomerSubscription summary);
    void customerSubscriptionsListSignal(OAICustomerSubscriptionList summary);


    void customerSubscriptionsCreateSignalFull(OAIHttpRequestWorker *worker, OAICustomerSubscription summary);
    void customerSubscriptionsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void customerSubscriptionsGetSignalFull(OAIHttpRequestWorker *worker, OAICustomerSubscription summary);
    void customerSubscriptionsListSignalFull(OAIHttpRequestWorker *worker, OAICustomerSubscriptionList summary);

    Q_DECL_DEPRECATED_X("Use customerSubscriptionsCreateSignalError() instead")
    void customerSubscriptionsCreateSignalE(OAICustomerSubscription summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customerSubscriptionsCreateSignalError(OAICustomerSubscription summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customerSubscriptionsDeleteSignalError() instead")
    void customerSubscriptionsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void customerSubscriptionsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customerSubscriptionsGetSignalError() instead")
    void customerSubscriptionsGetSignalE(OAICustomerSubscription summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customerSubscriptionsGetSignalError(OAICustomerSubscription summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customerSubscriptionsListSignalError() instead")
    void customerSubscriptionsListSignalE(OAICustomerSubscriptionList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customerSubscriptionsListSignalError(OAICustomerSubscriptionList summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use customerSubscriptionsCreateSignalErrorFull() instead")
    void customerSubscriptionsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customerSubscriptionsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customerSubscriptionsDeleteSignalErrorFull() instead")
    void customerSubscriptionsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customerSubscriptionsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customerSubscriptionsGetSignalErrorFull() instead")
    void customerSubscriptionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customerSubscriptionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customerSubscriptionsListSignalErrorFull() instead")
    void customerSubscriptionsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customerSubscriptionsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
