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
 * OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner_H
#define OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner_H

#include <QJsonObject>

#include "OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner_ipv4.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner_ipv4;

class OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner : public OAIObject {
public:
    OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner();
    OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner(QString json);
    ~OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner_ipv4 getIpv4() const;
    void setIpv4(const OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner_ipv4 &ipv4);
    bool is_ipv4_Set() const;
    bool is_ipv4_Valid() const;

    QString getMac() const;
    void setMac(const QString &mac);
    bool is_mac_Set() const;
    bool is_mac_Valid() const;

    QString getTrustedServerId() const;
    void setTrustedServerId(const QString &trusted_server_id);
    bool is_trusted_server_id_Set() const;
    bool is_trusted_server_id_Valid() const;

    qint32 getVlan() const;
    void setVlan(const qint32 &vlan);
    bool is_vlan_Set() const;
    bool is_vlan_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner_ipv4 m_ipv4;
    bool m_ipv4_isSet;
    bool m_ipv4_isValid;

    QString m_mac;
    bool m_mac_isSet;
    bool m_mac_isValid;

    QString m_trusted_server_id;
    bool m_trusted_server_id_isSet;
    bool m_trusted_server_id_isValid;

    qint32 m_vlan;
    bool m_vlan_isSet;
    bool m_vlan_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner)

#endif // OAIGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_200_response_inner_H
