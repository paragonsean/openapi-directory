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

#ifndef OAI_OAICellularGatewayApi_H
#define OAI_OAICellularGatewayApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetNetworkCellularGatewayDhcp_200_response.h"
#include "OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner.h"
#include "OAIObject.h"
#include "OAIUpdateDeviceCellularGatewayLan_request.h"
#include "OAIUpdateDeviceCellularGatewayPortForwardingRules_request.h"
#include "OAIUpdateNetworkCellularGatewayConnectivityMonitoringDestinations_request.h"
#include "OAIUpdateNetworkCellularGatewayDhcp_request.h"
#include "OAIUpdateNetworkCellularGatewaySubnetPool_request.h"
#include "OAIUpdateNetworkCellularGatewayUplink_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICellularGatewayApi : public QObject {
    Q_OBJECT

public:
    OAICellularGatewayApi(const int timeOut = 0);
    ~OAICellularGatewayApi();

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
    virtual void getDeviceCellularGatewayLan(const QString &serial);

    /**
    * @param[in]  serial QString [required]
    */
    virtual void getDeviceCellularGatewayPortForwardingRules(const QString &serial);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkCellularGatewayConnectivityMonitoringDestinations(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkCellularGatewayDhcp(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkCellularGatewaySubnetPool(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkCellularGatewayUplink(const QString &network_id);

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  starting_after QString [optional]
    * @param[in]  ending_before QString [optional]
    * @param[in]  network_ids QList<QString> [optional]
    * @param[in]  serials QList<QString> [optional]
    * @param[in]  iccids QList<QString> [optional]
    */
    virtual void getOrganizationCellularGatewayUplinkStatuses(const QString &organization_id, const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &starting_after = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ending_before = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &network_ids = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &serials = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &iccids = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  serial QString [required]
    * @param[in]  oai_update_device_cellular_gateway_lan_request OAIUpdateDeviceCellularGatewayLan_request [optional]
    */
    virtual void updateDeviceCellularGatewayLan(const QString &serial, const ::OpenAPI::OptionalParam<OAIUpdateDeviceCellularGatewayLan_request> &oai_update_device_cellular_gateway_lan_request = ::OpenAPI::OptionalParam<OAIUpdateDeviceCellularGatewayLan_request>());

    /**
    * @param[in]  serial QString [required]
    * @param[in]  oai_update_device_cellular_gateway_port_forwarding_rules_request OAIUpdateDeviceCellularGatewayPortForwardingRules_request [optional]
    */
    virtual void updateDeviceCellularGatewayPortForwardingRules(const QString &serial, const ::OpenAPI::OptionalParam<OAIUpdateDeviceCellularGatewayPortForwardingRules_request> &oai_update_device_cellular_gateway_port_forwarding_rules_request = ::OpenAPI::OptionalParam<OAIUpdateDeviceCellularGatewayPortForwardingRules_request>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_update_network_cellular_gateway_connectivity_monitoring_destinations_request OAIUpdateNetworkCellularGatewayConnectivityMonitoringDestinations_request [optional]
    */
    virtual void updateNetworkCellularGatewayConnectivityMonitoringDestinations(const QString &network_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkCellularGatewayConnectivityMonitoringDestinations_request> &oai_update_network_cellular_gateway_connectivity_monitoring_destinations_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkCellularGatewayConnectivityMonitoringDestinations_request>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_update_network_cellular_gateway_dhcp_request OAIUpdateNetworkCellularGatewayDhcp_request [optional]
    */
    virtual void updateNetworkCellularGatewayDhcp(const QString &network_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkCellularGatewayDhcp_request> &oai_update_network_cellular_gateway_dhcp_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkCellularGatewayDhcp_request>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_update_network_cellular_gateway_subnet_pool_request OAIUpdateNetworkCellularGatewaySubnetPool_request [optional]
    */
    virtual void updateNetworkCellularGatewaySubnetPool(const QString &network_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkCellularGatewaySubnetPool_request> &oai_update_network_cellular_gateway_subnet_pool_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkCellularGatewaySubnetPool_request>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_update_network_cellular_gateway_uplink_request OAIUpdateNetworkCellularGatewayUplink_request [optional]
    */
    virtual void updateNetworkCellularGatewayUplink(const QString &network_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkCellularGatewayUplink_request> &oai_update_network_cellular_gateway_uplink_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkCellularGatewayUplink_request>());


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

    void getDeviceCellularGatewayLanCallback(OAIHttpRequestWorker *worker);
    void getDeviceCellularGatewayPortForwardingRulesCallback(OAIHttpRequestWorker *worker);
    void getNetworkCellularGatewayConnectivityMonitoringDestinationsCallback(OAIHttpRequestWorker *worker);
    void getNetworkCellularGatewayDhcpCallback(OAIHttpRequestWorker *worker);
    void getNetworkCellularGatewaySubnetPoolCallback(OAIHttpRequestWorker *worker);
    void getNetworkCellularGatewayUplinkCallback(OAIHttpRequestWorker *worker);
    void getOrganizationCellularGatewayUplinkStatusesCallback(OAIHttpRequestWorker *worker);
    void updateDeviceCellularGatewayLanCallback(OAIHttpRequestWorker *worker);
    void updateDeviceCellularGatewayPortForwardingRulesCallback(OAIHttpRequestWorker *worker);
    void updateNetworkCellularGatewayConnectivityMonitoringDestinationsCallback(OAIHttpRequestWorker *worker);
    void updateNetworkCellularGatewayDhcpCallback(OAIHttpRequestWorker *worker);
    void updateNetworkCellularGatewaySubnetPoolCallback(OAIHttpRequestWorker *worker);
    void updateNetworkCellularGatewayUplinkCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getDeviceCellularGatewayLanSignal(OAIObject summary);
    void getDeviceCellularGatewayPortForwardingRulesSignal(OAIObject summary);
    void getNetworkCellularGatewayConnectivityMonitoringDestinationsSignal(OAIObject summary);
    void getNetworkCellularGatewayDhcpSignal(OAIGetNetworkCellularGatewayDhcp_200_response summary);
    void getNetworkCellularGatewaySubnetPoolSignal(OAIObject summary);
    void getNetworkCellularGatewayUplinkSignal(OAIObject summary);
    void getOrganizationCellularGatewayUplinkStatusesSignal(QList<OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner> summary);
    void updateDeviceCellularGatewayLanSignal(OAIObject summary);
    void updateDeviceCellularGatewayPortForwardingRulesSignal(OAIObject summary);
    void updateNetworkCellularGatewayConnectivityMonitoringDestinationsSignal(OAIObject summary);
    void updateNetworkCellularGatewayDhcpSignal(OAIGetNetworkCellularGatewayDhcp_200_response summary);
    void updateNetworkCellularGatewaySubnetPoolSignal(OAIObject summary);
    void updateNetworkCellularGatewayUplinkSignal(OAIObject summary);


    void getDeviceCellularGatewayLanSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getDeviceCellularGatewayPortForwardingRulesSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getNetworkCellularGatewayConnectivityMonitoringDestinationsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getNetworkCellularGatewayDhcpSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkCellularGatewayDhcp_200_response summary);
    void getNetworkCellularGatewaySubnetPoolSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getNetworkCellularGatewayUplinkSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getOrganizationCellularGatewayUplinkStatusesSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner> summary);
    void updateDeviceCellularGatewayLanSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateDeviceCellularGatewayPortForwardingRulesSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateNetworkCellularGatewayConnectivityMonitoringDestinationsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateNetworkCellularGatewayDhcpSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkCellularGatewayDhcp_200_response summary);
    void updateNetworkCellularGatewaySubnetPoolSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateNetworkCellularGatewayUplinkSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use getDeviceCellularGatewayLanSignalError() instead")
    void getDeviceCellularGatewayLanSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceCellularGatewayLanSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDeviceCellularGatewayPortForwardingRulesSignalError() instead")
    void getDeviceCellularGatewayPortForwardingRulesSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceCellularGatewayPortForwardingRulesSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkCellularGatewayConnectivityMonitoringDestinationsSignalError() instead")
    void getNetworkCellularGatewayConnectivityMonitoringDestinationsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkCellularGatewayConnectivityMonitoringDestinationsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkCellularGatewayDhcpSignalError() instead")
    void getNetworkCellularGatewayDhcpSignalE(OAIGetNetworkCellularGatewayDhcp_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkCellularGatewayDhcpSignalError(OAIGetNetworkCellularGatewayDhcp_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkCellularGatewaySubnetPoolSignalError() instead")
    void getNetworkCellularGatewaySubnetPoolSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkCellularGatewaySubnetPoolSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkCellularGatewayUplinkSignalError() instead")
    void getNetworkCellularGatewayUplinkSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkCellularGatewayUplinkSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationCellularGatewayUplinkStatusesSignalError() instead")
    void getOrganizationCellularGatewayUplinkStatusesSignalE(QList<OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationCellularGatewayUplinkStatusesSignalError(QList<OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceCellularGatewayLanSignalError() instead")
    void updateDeviceCellularGatewayLanSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceCellularGatewayLanSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceCellularGatewayPortForwardingRulesSignalError() instead")
    void updateDeviceCellularGatewayPortForwardingRulesSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceCellularGatewayPortForwardingRulesSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkCellularGatewayConnectivityMonitoringDestinationsSignalError() instead")
    void updateNetworkCellularGatewayConnectivityMonitoringDestinationsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkCellularGatewayConnectivityMonitoringDestinationsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkCellularGatewayDhcpSignalError() instead")
    void updateNetworkCellularGatewayDhcpSignalE(OAIGetNetworkCellularGatewayDhcp_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkCellularGatewayDhcpSignalError(OAIGetNetworkCellularGatewayDhcp_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkCellularGatewaySubnetPoolSignalError() instead")
    void updateNetworkCellularGatewaySubnetPoolSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkCellularGatewaySubnetPoolSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkCellularGatewayUplinkSignalError() instead")
    void updateNetworkCellularGatewayUplinkSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkCellularGatewayUplinkSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getDeviceCellularGatewayLanSignalErrorFull() instead")
    void getDeviceCellularGatewayLanSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceCellularGatewayLanSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDeviceCellularGatewayPortForwardingRulesSignalErrorFull() instead")
    void getDeviceCellularGatewayPortForwardingRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceCellularGatewayPortForwardingRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkCellularGatewayConnectivityMonitoringDestinationsSignalErrorFull() instead")
    void getNetworkCellularGatewayConnectivityMonitoringDestinationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkCellularGatewayConnectivityMonitoringDestinationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkCellularGatewayDhcpSignalErrorFull() instead")
    void getNetworkCellularGatewayDhcpSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkCellularGatewayDhcpSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkCellularGatewaySubnetPoolSignalErrorFull() instead")
    void getNetworkCellularGatewaySubnetPoolSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkCellularGatewaySubnetPoolSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkCellularGatewayUplinkSignalErrorFull() instead")
    void getNetworkCellularGatewayUplinkSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkCellularGatewayUplinkSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationCellularGatewayUplinkStatusesSignalErrorFull() instead")
    void getOrganizationCellularGatewayUplinkStatusesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationCellularGatewayUplinkStatusesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceCellularGatewayLanSignalErrorFull() instead")
    void updateDeviceCellularGatewayLanSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceCellularGatewayLanSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceCellularGatewayPortForwardingRulesSignalErrorFull() instead")
    void updateDeviceCellularGatewayPortForwardingRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceCellularGatewayPortForwardingRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkCellularGatewayConnectivityMonitoringDestinationsSignalErrorFull() instead")
    void updateNetworkCellularGatewayConnectivityMonitoringDestinationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkCellularGatewayConnectivityMonitoringDestinationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkCellularGatewayDhcpSignalErrorFull() instead")
    void updateNetworkCellularGatewayDhcpSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkCellularGatewayDhcpSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkCellularGatewaySubnetPoolSignalErrorFull() instead")
    void updateNetworkCellularGatewaySubnetPoolSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkCellularGatewaySubnetPoolSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkCellularGatewayUplinkSignalErrorFull() instead")
    void updateNetworkCellularGatewayUplinkSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkCellularGatewayUplinkSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
