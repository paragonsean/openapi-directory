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

/*
 * OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination.h
 *
 * Destination of this custom type traffic filter
 */

#ifndef OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination_H
#define OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination : public OAIObject {
public:
    OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination();
    OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination(QString json);
    ~OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCidr() const;
    void setCidr(const QString &cidr);
    bool is_cidr_Set() const;
    bool is_cidr_Valid() const;

    QString getFqdn() const;
    void setFqdn(const QString &fqdn);
    bool is_fqdn_Set() const;
    bool is_fqdn_Valid() const;

    qint32 getHost() const;
    void setHost(const qint32 &host);
    bool is_host_Set() const;
    bool is_host_Valid() const;

    QString getNetwork() const;
    void setNetwork(const QString &network);
    bool is_network_Set() const;
    bool is_network_Valid() const;

    QString getPort() const;
    void setPort(const QString &port);
    bool is_port_Set() const;
    bool is_port_Valid() const;

    qint32 getVlan() const;
    void setVlan(const qint32 &vlan);
    bool is_vlan_Set() const;
    bool is_vlan_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_cidr;
    bool m_cidr_isSet;
    bool m_cidr_isValid;

    QString m_fqdn;
    bool m_fqdn_isSet;
    bool m_fqdn_isValid;

    qint32 m_host;
    bool m_host_isSet;
    bool m_host_isValid;

    QString m_network;
    bool m_network_isSet;
    bool m_network_isValid;

    QString m_port;
    bool m_port_isSet;
    bool m_port_isValid;

    qint32 m_vlan;
    bool m_vlan_isSet;
    bool m_vlan_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination)

#endif // OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination_H
