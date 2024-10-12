/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICouponsGenerateApi_H
#define OAI_OAICouponsGenerateApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError_response.h"
#include "OAISalesRuleCouponManagementV1GeneratePost_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICouponsGenerateApi : public QObject {
    Q_OBJECT

public:
    OAICouponsGenerateApi(const int timeOut = 0);
    ~OAICouponsGenerateApi();

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
    * @param[in]  oai_sales_rule_coupon_management_v1_generate_post_request OAISalesRuleCouponManagementV1GeneratePost_request [optional]
    */
    virtual void salesRuleCouponManagementV1GeneratePost(const ::OpenAPI::OptionalParam<OAISalesRuleCouponManagementV1GeneratePost_request> &oai_sales_rule_coupon_management_v1_generate_post_request = ::OpenAPI::OptionalParam<OAISalesRuleCouponManagementV1GeneratePost_request>());


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

    void salesRuleCouponManagementV1GeneratePostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void salesRuleCouponManagementV1GeneratePostSignal(QList<QString> summary);


    void salesRuleCouponManagementV1GeneratePostSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);

    Q_DECL_DEPRECATED_X("Use salesRuleCouponManagementV1GeneratePostSignalError() instead")
    void salesRuleCouponManagementV1GeneratePostSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRuleCouponManagementV1GeneratePostSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use salesRuleCouponManagementV1GeneratePostSignalErrorFull() instead")
    void salesRuleCouponManagementV1GeneratePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRuleCouponManagementV1GeneratePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
