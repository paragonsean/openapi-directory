/**
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISubscriptionsApi_H
#define OAI_OAISubscriptionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorResponse.h"
#include "OAIHIUSubscriptionNotificationAcknowledgment.h"
#include "OAIHIUSubscriptionRequestNotificationAcknowledgement.h"
#include "OAISubscriptionRequest.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISubscriptionsApi : public QObject {
    Q_OBJECT

public:
    OAISubscriptionsApi(const int timeOut = 0);
    ~OAISubscriptionsApi();

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
    * @param[in]  authorization QString [required]
    * @param[in]  oai_subscription_request OAISubscriptionRequest [required]
    */
    virtual void v05SubscriptionRequestsCmInitPost(const QString &authorization, const OAISubscriptionRequest &oai_subscription_request);

    /**
    * @param[in]  authorization QString [required]
    * @param[in]  oaihiu_subscription_request_notification_acknowledgement OAIHIUSubscriptionRequestNotificationAcknowledgement [required]
    */
    virtual void v05SubscriptionRequestsHiuOnNotifyPost(const QString &authorization, const OAIHIUSubscriptionRequestNotificationAcknowledgement &oaihiu_subscription_request_notification_acknowledgement);

    /**
    * @param[in]  authorization QString [required]
    * @param[in]  oaihiu_subscription_notification_acknowledgment OAIHIUSubscriptionNotificationAcknowledgment [required]
    */
    virtual void v05SubscriptionsHiuOnNotifyPost(const QString &authorization, const OAIHIUSubscriptionNotificationAcknowledgment &oaihiu_subscription_notification_acknowledgment);


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

    void v05SubscriptionRequestsCmInitPostCallback(OAIHttpRequestWorker *worker);
    void v05SubscriptionRequestsHiuOnNotifyPostCallback(OAIHttpRequestWorker *worker);
    void v05SubscriptionsHiuOnNotifyPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void v05SubscriptionRequestsCmInitPostSignal();
    void v05SubscriptionRequestsHiuOnNotifyPostSignal();
    void v05SubscriptionsHiuOnNotifyPostSignal();


    void v05SubscriptionRequestsCmInitPostSignalFull(OAIHttpRequestWorker *worker);
    void v05SubscriptionRequestsHiuOnNotifyPostSignalFull(OAIHttpRequestWorker *worker);
    void v05SubscriptionsHiuOnNotifyPostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use v05SubscriptionRequestsCmInitPostSignalError() instead")
    void v05SubscriptionRequestsCmInitPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionRequestsCmInitPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05SubscriptionRequestsHiuOnNotifyPostSignalError() instead")
    void v05SubscriptionRequestsHiuOnNotifyPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionRequestsHiuOnNotifyPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05SubscriptionsHiuOnNotifyPostSignalError() instead")
    void v05SubscriptionsHiuOnNotifyPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionsHiuOnNotifyPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use v05SubscriptionRequestsCmInitPostSignalErrorFull() instead")
    void v05SubscriptionRequestsCmInitPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionRequestsCmInitPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05SubscriptionRequestsHiuOnNotifyPostSignalErrorFull() instead")
    void v05SubscriptionRequestsHiuOnNotifyPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionRequestsHiuOnNotifyPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05SubscriptionsHiuOnNotifyPostSignalErrorFull() instead")
    void v05SubscriptionsHiuOnNotifyPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionsHiuOnNotifyPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
