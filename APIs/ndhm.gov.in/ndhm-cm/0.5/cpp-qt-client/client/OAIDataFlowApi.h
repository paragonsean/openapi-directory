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

#ifndef OAI_OAIDataFlowApi_H
#define OAI_OAIDataFlowApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorResponse.h"
#include "OAIHIPHealthInformationRequestAcknowledgement.h"
#include "OAIHIRequest.h"
#include "OAIHealthInformationNotification.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDataFlowApi : public QObject {
    Q_OBJECT

public:
    OAIDataFlowApi(const int timeOut = 0);
    ~OAIDataFlowApi();

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
    * @param[in]  oai_health_information_notification OAIHealthInformationNotification [required]
    */
    virtual void v05HealthInformationNotifyPost(const QString &authorization, const OAIHealthInformationNotification &oai_health_information_notification);

    /**
    * @param[in]  authorization QString [required]
    * @param[in]  oaihip_health_information_request_acknowledgement OAIHIPHealthInformationRequestAcknowledgement [required]
    */
    virtual void v05HealthInformationOnRequestPost(const QString &authorization, const OAIHIPHealthInformationRequestAcknowledgement &oaihip_health_information_request_acknowledgement);

    /**
    * @param[in]  authorization QString [required]
    * @param[in]  oaihi_request OAIHIRequest [required]
    */
    virtual void v05HealthInformationRequestPost(const QString &authorization, const OAIHIRequest &oaihi_request);


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

    void v05HealthInformationNotifyPostCallback(OAIHttpRequestWorker *worker);
    void v05HealthInformationOnRequestPostCallback(OAIHttpRequestWorker *worker);
    void v05HealthInformationRequestPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void v05HealthInformationNotifyPostSignal();
    void v05HealthInformationOnRequestPostSignal();
    void v05HealthInformationRequestPostSignal();


    void v05HealthInformationNotifyPostSignalFull(OAIHttpRequestWorker *worker);
    void v05HealthInformationOnRequestPostSignalFull(OAIHttpRequestWorker *worker);
    void v05HealthInformationRequestPostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use v05HealthInformationNotifyPostSignalError() instead")
    void v05HealthInformationNotifyPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v05HealthInformationNotifyPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05HealthInformationOnRequestPostSignalError() instead")
    void v05HealthInformationOnRequestPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v05HealthInformationOnRequestPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05HealthInformationRequestPostSignalError() instead")
    void v05HealthInformationRequestPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v05HealthInformationRequestPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use v05HealthInformationNotifyPostSignalErrorFull() instead")
    void v05HealthInformationNotifyPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v05HealthInformationNotifyPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05HealthInformationOnRequestPostSignalErrorFull() instead")
    void v05HealthInformationOnRequestPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v05HealthInformationOnRequestPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v05HealthInformationRequestPostSignalErrorFull() instead")
    void v05HealthInformationRequestPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v05HealthInformationRequestPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
