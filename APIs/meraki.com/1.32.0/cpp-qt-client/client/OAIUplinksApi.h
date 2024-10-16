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

#ifndef OAI_OAIUplinksApi_H
#define OAI_OAIUplinksApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetDeviceApplianceUplinksSettings_200_response.h"
#include "OAIGetOrganizationDevicesUplinksAddressesByDevice_200_response_inner.h"
#include "OAIGetOrganizationDevicesUplinksLossAndLatency_200_response_inner.h"
#include "OAIGetOrganizationUplinksStatuses_200_response_inner.h"
#include "OAIObject.h"
#include "OAIUpdateDeviceApplianceUplinksSettings_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIUplinksApi : public QObject {
    Q_OBJECT

public:
    OAIUplinksApi(const int timeOut = 0);
    ~OAIUplinksApi();

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
    * @param[in]  serial QString [required]
    */
    virtual void getDeviceApplianceUplinksSettings(const QString &serial);

    /**
    * @param[in]  serial QString [required]
    * @param[in]  ip QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    * @param[in]  resolution qint32 [optional]
    * @param[in]  uplink QString [optional]
    */
    virtual void getDeviceLossAndLatencyHistory(const QString &serial, const QString &ip, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>(), const ::OpenAPI::OptionalParam<qint32> &resolution = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &uplink = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    * @param[in]  resolution qint32 [optional]
    */
    virtual void getNetworkApplianceUplinksUsageHistory(const QString &network_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>(), const ::OpenAPI::OptionalParam<qint32> &resolution = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  starting_after QString [optional]
    * @param[in]  ending_before QString [optional]
    * @param[in]  network_ids QList<QString> [optional]
    * @param[in]  serials QList<QString> [optional]
    * @param[in]  iccids QList<QString> [optional]
    */
    virtual void getOrganizationApplianceUplinkStatuses(const QString &organization_id, const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &starting_after = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ending_before = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &network_ids = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &serials = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &iccids = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  starting_after QString [optional]
    * @param[in]  ending_before QString [optional]
    * @param[in]  network_ids QList<QString> [optional]
    * @param[in]  product_types QList<QString> [optional]
    * @param[in]  serials QList<QString> [optional]
    * @param[in]  tags QList<QString> [optional]
    * @param[in]  tags_filter_type QString [optional]
    */
    virtual void getOrganizationDevicesUplinksAddressesByDevice(const QString &organization_id, const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &starting_after = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ending_before = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &network_ids = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &product_types = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &serials = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &tags = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &tags_filter_type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    * @param[in]  uplink QString [optional]
    * @param[in]  ip QString [optional]
    */
    virtual void getOrganizationDevicesUplinksLossAndLatency(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>(), const ::OpenAPI::OptionalParam<QString> &uplink = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ip = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  starting_after QString [optional]
    * @param[in]  ending_before QString [optional]
    * @param[in]  network_ids QList<QString> [optional]
    * @param[in]  serials QList<QString> [optional]
    * @param[in]  iccids QList<QString> [optional]
    */
    virtual void getOrganizationUplinksStatuses(const QString &organization_id, const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &starting_after = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ending_before = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &network_ids = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &serials = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &iccids = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  serial QString [required]
    * @param[in]  oai_update_device_appliance_uplinks_settings_request OAIUpdateDeviceApplianceUplinksSettings_request [required]
    */
    virtual void updateDeviceApplianceUplinksSettings(const QString &serial, const OAIUpdateDeviceApplianceUplinksSettings_request &oai_update_device_appliance_uplinks_settings_request);


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

    void getDeviceApplianceUplinksSettingsCallback(OAIHttpRequestWorker *worker);
    void getDeviceLossAndLatencyHistoryCallback(OAIHttpRequestWorker *worker);
    void getNetworkApplianceUplinksUsageHistoryCallback(OAIHttpRequestWorker *worker);
    void getOrganizationApplianceUplinkStatusesCallback(OAIHttpRequestWorker *worker);
    void getOrganizationDevicesUplinksAddressesByDeviceCallback(OAIHttpRequestWorker *worker);
    void getOrganizationDevicesUplinksLossAndLatencyCallback(OAIHttpRequestWorker *worker);
    void getOrganizationUplinksStatusesCallback(OAIHttpRequestWorker *worker);
    void updateDeviceApplianceUplinksSettingsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getDeviceApplianceUplinksSettingsSignal(OAIGetDeviceApplianceUplinksSettings_200_response summary);
    void getDeviceLossAndLatencyHistorySignal(QList<OAIObject> summary);
    void getNetworkApplianceUplinksUsageHistorySignal(QList<OAIObject> summary);
    void getOrganizationApplianceUplinkStatusesSignal(QList<OAIObject> summary);
    void getOrganizationDevicesUplinksAddressesByDeviceSignal(QList<OAIGetOrganizationDevicesUplinksAddressesByDevice_200_response_inner> summary);
    void getOrganizationDevicesUplinksLossAndLatencySignal(QList<OAIGetOrganizationDevicesUplinksLossAndLatency_200_response_inner> summary);
    void getOrganizationUplinksStatusesSignal(QList<OAIGetOrganizationUplinksStatuses_200_response_inner> summary);
    void updateDeviceApplianceUplinksSettingsSignal(OAIGetDeviceApplianceUplinksSettings_200_response summary);


    void getDeviceApplianceUplinksSettingsSignalFull(OAIHttpRequestWorker *worker, OAIGetDeviceApplianceUplinksSettings_200_response summary);
    void getDeviceLossAndLatencyHistorySignalFull(OAIHttpRequestWorker *worker, QList<OAIObject> summary);
    void getNetworkApplianceUplinksUsageHistorySignalFull(OAIHttpRequestWorker *worker, QList<OAIObject> summary);
    void getOrganizationApplianceUplinkStatusesSignalFull(OAIHttpRequestWorker *worker, QList<OAIObject> summary);
    void getOrganizationDevicesUplinksAddressesByDeviceSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationDevicesUplinksAddressesByDevice_200_response_inner> summary);
    void getOrganizationDevicesUplinksLossAndLatencySignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationDevicesUplinksLossAndLatency_200_response_inner> summary);
    void getOrganizationUplinksStatusesSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationUplinksStatuses_200_response_inner> summary);
    void updateDeviceApplianceUplinksSettingsSignalFull(OAIHttpRequestWorker *worker, OAIGetDeviceApplianceUplinksSettings_200_response summary);

    Q_DECL_DEPRECATED_X("Use getDeviceApplianceUplinksSettingsSignalError() instead")
    void getDeviceApplianceUplinksSettingsSignalE(OAIGetDeviceApplianceUplinksSettings_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceApplianceUplinksSettingsSignalError(OAIGetDeviceApplianceUplinksSettings_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDeviceLossAndLatencyHistorySignalError() instead")
    void getDeviceLossAndLatencyHistorySignalE(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceLossAndLatencyHistorySignalError(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkApplianceUplinksUsageHistorySignalError() instead")
    void getNetworkApplianceUplinksUsageHistorySignalE(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkApplianceUplinksUsageHistorySignalError(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationApplianceUplinkStatusesSignalError() instead")
    void getOrganizationApplianceUplinkStatusesSignalE(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationApplianceUplinkStatusesSignalError(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationDevicesUplinksAddressesByDeviceSignalError() instead")
    void getOrganizationDevicesUplinksAddressesByDeviceSignalE(QList<OAIGetOrganizationDevicesUplinksAddressesByDevice_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationDevicesUplinksAddressesByDeviceSignalError(QList<OAIGetOrganizationDevicesUplinksAddressesByDevice_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationDevicesUplinksLossAndLatencySignalError() instead")
    void getOrganizationDevicesUplinksLossAndLatencySignalE(QList<OAIGetOrganizationDevicesUplinksLossAndLatency_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationDevicesUplinksLossAndLatencySignalError(QList<OAIGetOrganizationDevicesUplinksLossAndLatency_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationUplinksStatusesSignalError() instead")
    void getOrganizationUplinksStatusesSignalE(QList<OAIGetOrganizationUplinksStatuses_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationUplinksStatusesSignalError(QList<OAIGetOrganizationUplinksStatuses_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceApplianceUplinksSettingsSignalError() instead")
    void updateDeviceApplianceUplinksSettingsSignalE(OAIGetDeviceApplianceUplinksSettings_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceApplianceUplinksSettingsSignalError(OAIGetDeviceApplianceUplinksSettings_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getDeviceApplianceUplinksSettingsSignalErrorFull() instead")
    void getDeviceApplianceUplinksSettingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceApplianceUplinksSettingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDeviceLossAndLatencyHistorySignalErrorFull() instead")
    void getDeviceLossAndLatencyHistorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceLossAndLatencyHistorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkApplianceUplinksUsageHistorySignalErrorFull() instead")
    void getNetworkApplianceUplinksUsageHistorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkApplianceUplinksUsageHistorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationApplianceUplinkStatusesSignalErrorFull() instead")
    void getOrganizationApplianceUplinkStatusesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationApplianceUplinkStatusesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationDevicesUplinksAddressesByDeviceSignalErrorFull() instead")
    void getOrganizationDevicesUplinksAddressesByDeviceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationDevicesUplinksAddressesByDeviceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationDevicesUplinksLossAndLatencySignalErrorFull() instead")
    void getOrganizationDevicesUplinksLossAndLatencySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationDevicesUplinksLossAndLatencySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationUplinksStatusesSignalErrorFull() instead")
    void getOrganizationUplinksStatusesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationUplinksStatusesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceApplianceUplinksSettingsSignalErrorFull() instead")
    void updateDeviceApplianceUplinksSettingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceApplianceUplinksSettingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
