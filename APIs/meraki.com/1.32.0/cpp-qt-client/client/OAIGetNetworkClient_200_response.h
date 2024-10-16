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
 * OAIGetNetworkClient_200_response.h
 *
 * 
 */

#ifndef OAIGetNetworkClient_200_response_H
#define OAIGetNetworkClient_200_response_H

#include <QJsonObject>

#include "OAIGetNetworkClient_200_response_clientVpnConnections_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNetworkClient_200_response_clientVpnConnections_inner;

class OAIGetNetworkClient_200_response : public OAIObject {
public:
    OAIGetNetworkClient_200_response();
    OAIGetNetworkClient_200_response(QString json);
    ~OAIGetNetworkClient_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QList<QString>> getCdp() const;
    void setCdp(const QList<QList<QString>> &cdp);
    bool is_cdp_Set() const;
    bool is_cdp_Valid() const;

    QList<OAIGetNetworkClient_200_response_clientVpnConnections_inner> getClientVpnConnections() const;
    void setClientVpnConnections(const QList<OAIGetNetworkClient_200_response_clientVpnConnections_inner> &client_vpn_connections);
    bool is_client_vpn_connections_Set() const;
    bool is_client_vpn_connections_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    qint32 getFirstSeen() const;
    void setFirstSeen(const qint32 &first_seen);
    bool is_first_seen_Set() const;
    bool is_first_seen_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getIp() const;
    void setIp(const QString &ip);
    bool is_ip_Set() const;
    bool is_ip_Valid() const;

    QString getIp6() const;
    void setIp6(const QString &ip6);
    bool is_ip6_Set() const;
    bool is_ip6_Valid() const;

    qint32 getLastSeen() const;
    void setLastSeen(const qint32 &last_seen);
    bool is_last_seen_Set() const;
    bool is_last_seen_Valid() const;

    QList<QList<QString>> getLldp() const;
    void setLldp(const QList<QList<QString>> &lldp);
    bool is_lldp_Set() const;
    bool is_lldp_Valid() const;

    QString getMac() const;
    void setMac(const QString &mac);
    bool is_mac_Set() const;
    bool is_mac_Valid() const;

    QString getManufacturer() const;
    void setManufacturer(const QString &manufacturer);
    bool is_manufacturer_Set() const;
    bool is_manufacturer_Valid() const;

    QString getOs() const;
    void setOs(const QString &os);
    bool is_os_Set() const;
    bool is_os_Valid() const;

    QString getRecentDeviceMac() const;
    void setRecentDeviceMac(const QString &recent_device_mac);
    bool is_recent_device_mac_Set() const;
    bool is_recent_device_mac_Valid() const;

    bool isSmInstalled() const;
    void setSmInstalled(const bool &sm_installed);
    bool is_sm_installed_Set() const;
    bool is_sm_installed_Valid() const;

    QString getSsid() const;
    void setSsid(const QString &ssid);
    bool is_ssid_Set() const;
    bool is_ssid_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getSwitchport() const;
    void setSwitchport(const QString &switchport);
    bool is_switchport_Set() const;
    bool is_switchport_Valid() const;

    QString getUser() const;
    void setUser(const QString &user);
    bool is_user_Set() const;
    bool is_user_Valid() const;

    QString getVlan() const;
    void setVlan(const QString &vlan);
    bool is_vlan_Set() const;
    bool is_vlan_Valid() const;

    QString getWirelessCapabilities() const;
    void setWirelessCapabilities(const QString &wireless_capabilities);
    bool is_wireless_capabilities_Set() const;
    bool is_wireless_capabilities_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QList<QString>> m_cdp;
    bool m_cdp_isSet;
    bool m_cdp_isValid;

    QList<OAIGetNetworkClient_200_response_clientVpnConnections_inner> m_client_vpn_connections;
    bool m_client_vpn_connections_isSet;
    bool m_client_vpn_connections_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    qint32 m_first_seen;
    bool m_first_seen_isSet;
    bool m_first_seen_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_ip;
    bool m_ip_isSet;
    bool m_ip_isValid;

    QString m_ip6;
    bool m_ip6_isSet;
    bool m_ip6_isValid;

    qint32 m_last_seen;
    bool m_last_seen_isSet;
    bool m_last_seen_isValid;

    QList<QList<QString>> m_lldp;
    bool m_lldp_isSet;
    bool m_lldp_isValid;

    QString m_mac;
    bool m_mac_isSet;
    bool m_mac_isValid;

    QString m_manufacturer;
    bool m_manufacturer_isSet;
    bool m_manufacturer_isValid;

    QString m_os;
    bool m_os_isSet;
    bool m_os_isValid;

    QString m_recent_device_mac;
    bool m_recent_device_mac_isSet;
    bool m_recent_device_mac_isValid;

    bool m_sm_installed;
    bool m_sm_installed_isSet;
    bool m_sm_installed_isValid;

    QString m_ssid;
    bool m_ssid_isSet;
    bool m_ssid_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_switchport;
    bool m_switchport_isSet;
    bool m_switchport_isValid;

    QString m_user;
    bool m_user_isSet;
    bool m_user_isValid;

    QString m_vlan;
    bool m_vlan_isSet;
    bool m_vlan_isValid;

    QString m_wireless_capabilities;
    bool m_wireless_capabilities_isSet;
    bool m_wireless_capabilities_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkClient_200_response)

#endif // OAIGetNetworkClient_200_response_H
