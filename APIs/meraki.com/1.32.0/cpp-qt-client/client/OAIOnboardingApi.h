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

#ifndef OAI_OAIOnboardingApi_H
#define OAI_OAIOnboardingApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateOrganizationInventoryOnboardingCloudMonitoringExportEvent_request.h"
#include "OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner.h"
#include "OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_request.h"
#include "OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner.h"
#include "OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_request.h"
#include "OAIGetNetwork_200_response.h"
#include "OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner.h"
#include "OAIObject.h"
#include "OAIUpdateOrganizationCameraOnboardingStatuses_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIOnboardingApi : public QObject {
    Q_OBJECT

public:
    OAIOnboardingApi(const int timeOut = 0);
    ~OAIOnboardingApi();

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
    * @param[in]  oai_create_organization_inventory_onboarding_cloud_monitoring_export_event_request OAICreateOrganizationInventoryOnboardingCloudMonitoringExportEvent_request [required]
    */
    virtual void createOrganizationInventoryOnboardingCloudMonitoringExportEvent(const QString &organization_id, const OAICreateOrganizationInventoryOnboardingCloudMonitoringExportEvent_request &oai_create_organization_inventory_onboarding_cloud_monitoring_export_event_request);

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  oai_create_organization_inventory_onboarding_cloud_monitoring_import_request OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_request [required]
    */
    virtual void createOrganizationInventoryOnboardingCloudMonitoringImport(const QString &organization_id, const OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_request &oai_create_organization_inventory_onboarding_cloud_monitoring_import_request);

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  oai_create_organization_inventory_onboarding_cloud_monitoring_prepare_request OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_request [required]
    */
    virtual void createOrganizationInventoryOnboardingCloudMonitoringPrepare(const QString &organization_id, const OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_request &oai_create_organization_inventory_onboarding_cloud_monitoring_prepare_request);

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  serials QList<QString> [optional]
    * @param[in]  network_ids QList<QString> [optional]
    */
    virtual void getOrganizationCameraOnboardingStatuses(const QString &organization_id, const ::OpenAPI::OptionalParam<QList<QString>> &serials = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &network_ids = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  import_ids QList<QString> [required]
    */
    virtual void getOrganizationInventoryOnboardingCloudMonitoringImports(const QString &organization_id, const QList<QString> &import_ids);

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  device_type QString [required]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  starting_after QString [optional]
    * @param[in]  ending_before QString [optional]
    */
    virtual void getOrganizationInventoryOnboardingCloudMonitoringNetworks(const QString &organization_id, const QString &device_type, const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &starting_after = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ending_before = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  oai_update_organization_camera_onboarding_statuses_request OAIUpdateOrganizationCameraOnboardingStatuses_request [optional]
    */
    virtual void updateOrganizationCameraOnboardingStatuses(const QString &organization_id, const ::OpenAPI::OptionalParam<OAIUpdateOrganizationCameraOnboardingStatuses_request> &oai_update_organization_camera_onboarding_statuses_request = ::OpenAPI::OptionalParam<OAIUpdateOrganizationCameraOnboardingStatuses_request>());


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

    void createOrganizationInventoryOnboardingCloudMonitoringExportEventCallback(OAIHttpRequestWorker *worker);
    void createOrganizationInventoryOnboardingCloudMonitoringImportCallback(OAIHttpRequestWorker *worker);
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareCallback(OAIHttpRequestWorker *worker);
    void getOrganizationCameraOnboardingStatusesCallback(OAIHttpRequestWorker *worker);
    void getOrganizationInventoryOnboardingCloudMonitoringImportsCallback(OAIHttpRequestWorker *worker);
    void getOrganizationInventoryOnboardingCloudMonitoringNetworksCallback(OAIHttpRequestWorker *worker);
    void updateOrganizationCameraOnboardingStatusesCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createOrganizationInventoryOnboardingCloudMonitoringExportEventSignal(OAIObject summary);
    void createOrganizationInventoryOnboardingCloudMonitoringImportSignal(QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner> summary);
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignal(QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner> summary);
    void getOrganizationCameraOnboardingStatusesSignal(QList<OAIObject> summary);
    void getOrganizationInventoryOnboardingCloudMonitoringImportsSignal(QList<OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner> summary);
    void getOrganizationInventoryOnboardingCloudMonitoringNetworksSignal(QList<OAIGetNetwork_200_response> summary);
    void updateOrganizationCameraOnboardingStatusesSignal(OAIObject summary);


    void createOrganizationInventoryOnboardingCloudMonitoringExportEventSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void createOrganizationInventoryOnboardingCloudMonitoringImportSignalFull(OAIHttpRequestWorker *worker, QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner> summary);
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalFull(OAIHttpRequestWorker *worker, QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner> summary);
    void getOrganizationCameraOnboardingStatusesSignalFull(OAIHttpRequestWorker *worker, QList<OAIObject> summary);
    void getOrganizationInventoryOnboardingCloudMonitoringImportsSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner> summary);
    void getOrganizationInventoryOnboardingCloudMonitoringNetworksSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetNetwork_200_response> summary);
    void updateOrganizationCameraOnboardingStatusesSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use createOrganizationInventoryOnboardingCloudMonitoringExportEventSignalError() instead")
    void createOrganizationInventoryOnboardingCloudMonitoringExportEventSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationInventoryOnboardingCloudMonitoringExportEventSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createOrganizationInventoryOnboardingCloudMonitoringImportSignalError() instead")
    void createOrganizationInventoryOnboardingCloudMonitoringImportSignalE(QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationInventoryOnboardingCloudMonitoringImportSignalError(QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalError() instead")
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalE(QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalError(QList<OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationCameraOnboardingStatusesSignalError() instead")
    void getOrganizationCameraOnboardingStatusesSignalE(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationCameraOnboardingStatusesSignalError(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationInventoryOnboardingCloudMonitoringImportsSignalError() instead")
    void getOrganizationInventoryOnboardingCloudMonitoringImportsSignalE(QList<OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationInventoryOnboardingCloudMonitoringImportsSignalError(QList<OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationInventoryOnboardingCloudMonitoringNetworksSignalError() instead")
    void getOrganizationInventoryOnboardingCloudMonitoringNetworksSignalE(QList<OAIGetNetwork_200_response> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationInventoryOnboardingCloudMonitoringNetworksSignalError(QList<OAIGetNetwork_200_response> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateOrganizationCameraOnboardingStatusesSignalError() instead")
    void updateOrganizationCameraOnboardingStatusesSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateOrganizationCameraOnboardingStatusesSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createOrganizationInventoryOnboardingCloudMonitoringExportEventSignalErrorFull() instead")
    void createOrganizationInventoryOnboardingCloudMonitoringExportEventSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationInventoryOnboardingCloudMonitoringExportEventSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createOrganizationInventoryOnboardingCloudMonitoringImportSignalErrorFull() instead")
    void createOrganizationInventoryOnboardingCloudMonitoringImportSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationInventoryOnboardingCloudMonitoringImportSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalErrorFull() instead")
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationInventoryOnboardingCloudMonitoringPrepareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationCameraOnboardingStatusesSignalErrorFull() instead")
    void getOrganizationCameraOnboardingStatusesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationCameraOnboardingStatusesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationInventoryOnboardingCloudMonitoringImportsSignalErrorFull() instead")
    void getOrganizationInventoryOnboardingCloudMonitoringImportsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationInventoryOnboardingCloudMonitoringImportsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationInventoryOnboardingCloudMonitoringNetworksSignalErrorFull() instead")
    void getOrganizationInventoryOnboardingCloudMonitoringNetworksSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationInventoryOnboardingCloudMonitoringNetworksSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateOrganizationCameraOnboardingStatusesSignalErrorFull() instead")
    void updateOrganizationCameraOnboardingStatusesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateOrganizationCameraOnboardingStatusesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
