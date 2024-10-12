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

#ifndef OAI_OAISubscriptionsApi_H
#define OAI_OAISubscriptionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorResponse.h"
#include "OAIHIUSubscriptionNotification.h"
#include "OAIHIUSubscriptionRequestReceipt.h"
#include "OAISubscriptionApprovalNotification.h"
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
    * @param[in]  x_hiu_id QString [required]
    * @param[in]  oai_subscription_approval_notification OAISubscriptionApprovalNotification [required]
    */
    virtual void v05SubscriptionRequestsHiuNotifyPost(const QString &authorization, const QString &x_hiu_id, const OAISubscriptionApprovalNotification &oai_subscription_approval_notification);

    /**
    * @param[in]  authorization QString [required]
    * @param[in]  x_hiu_id QString [required]
    * @param[in]  oaihiu_subscription_request_receipt OAIHIUSubscriptionRequestReceipt [required]
    */
    virtual void v05SubscriptionRequestsHiuOnInitPost(const QString &authorization, const QString &x_hiu_id, const OAIHIUSubscriptionRequestReceipt &oaihiu_subscription_request_receipt);

    /**
    * @param[in]  authorization QString [required]
    * @param[in]  x_hiu_id QString [required]
    * @param[in]  oaihiu_subscription_notification OAIHIUSubscriptionNotification [required]
    */
    virtual void v05SubscriptionsHiuNotifyPost(const QString &authorization, const QString &x_hiu_id, const OAIHIUSubscriptionNotification &oaihiu_subscription_notification);


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

    void v05SubscriptionRequestsHiuNotifyPostCallback(OAIHttpRequestWorker *worker);
    void v05SubscriptionRequestsHiuOnInitPostCallback(OAIHttpRequestWorker *worker);
    void v05SubscriptionsHiuNotifyPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void v05SubscriptionRequestsHiuNotifyPostSignal();
    void v05SubscriptionRequestsHiuOnInitPostSignal();
    void v05SubscriptionsHiuNotifyPostSignal();


    void v05SubscriptionRequestsHiuNotifyPostSignalFull(OAIHttpRequestWorker *worker);
    void v05SubscriptionRequestsHiuOnInitPostSignalFull(OAIHttpRequestWorker *worker);
    void v05SubscriptionsHiuNotifyPostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use v05SubscriptionRequestsHiuNotifyPostSignalError() instead")
    void v05SubscriptionRequestsHiuNotifyPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionRequestsHiuNotifyPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05SubscriptionRequestsHiuOnInitPostSignalError() instead")
    void v05SubscriptionRequestsHiuOnInitPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionRequestsHiuOnInitPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05SubscriptionsHiuNotifyPostSignalError() instead")
    void v05SubscriptionsHiuNotifyPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionsHiuNotifyPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use v05SubscriptionRequestsHiuNotifyPostSignalErrorFull() instead")
    void v05SubscriptionRequestsHiuNotifyPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionRequestsHiuNotifyPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05SubscriptionRequestsHiuOnInitPostSignalErrorFull() instead")
    void v05SubscriptionRequestsHiuOnInitPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionRequestsHiuOnInitPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05SubscriptionsHiuNotifyPostSignalErrorFull() instead")
    void v05SubscriptionsHiuNotifyPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v05SubscriptionsHiuNotifyPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
