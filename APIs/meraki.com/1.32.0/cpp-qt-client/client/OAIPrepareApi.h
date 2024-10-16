/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPrepareApi_H
#define OAI_OAIPrepareApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner.h"
#include "OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPrepareApi : public QObject {
    Q_OBJECT

public:
    OAIPrepareApi(const int timeOut = 0);
    ~OAIPrepareApi();

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
    * @param[in]  organization_id QString [required]
    * @param[in]  oai_create_organization_inventory_onboarding_cloud_monitoring_prepare_request OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_request [required]
    */
    virtual void createOrganizationInventoryOnboardingCloudMonitoringPrepare(const QString &organization_id, const OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_request &oai_create_organization_inventory_onboarding_cloud_monitoring_prepare_request);


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

    void createOrganizationInventoryOnboardingCloudMonitoringPrepareCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignal(QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner> summary);


    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalFull(OAIHttpRequestWorker *worker, QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner> summary);

    Q_DECL_DEPRECATED_X("Use createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalError() instead")
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalE(QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalError(QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalErrorFull() instead")
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
