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
 * OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner.h
 *
 * 
 */

#ifndef OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner_H
#define OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner_H

#include <QJsonObject>

#include "OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner_ipv6.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner_ipv6;

class OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner : public OAIObject {
public:
    OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner();
    OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner(QString json);
    ~OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowTransit() const;
    void setAllowTransit(const bool &allow_transit);
    bool is_allow_transit_Set() const;
    bool is_allow_transit_Valid() const;

    qint32 getEbgpHoldTimer() const;
    void setEbgpHoldTimer(const qint32 &ebgp_hold_timer);
    bool is_ebgp_hold_timer_Set() const;
    bool is_ebgp_hold_timer_Valid() const;

    qint32 getEbgpMultihop() const;
    void setEbgpMultihop(const qint32 &ebgp_multihop);
    bool is_ebgp_multihop_Set() const;
    bool is_ebgp_multihop_Valid() const;

    QString getIp() const;
    void setIp(const QString &ip);
    bool is_ip_Set() const;
    bool is_ip_Valid() const;

    OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner_ipv6 getIpv6() const;
    void setIpv6(const OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner_ipv6 &ipv6);
    bool is_ipv6_Set() const;
    bool is_ipv6_Valid() const;

    qint32 getReceiveLimit() const;
    void setReceiveLimit(const qint32 &receive_limit);
    bool is_receive_limit_Set() const;
    bool is_receive_limit_Valid() const;

    qint32 getRemoteAsNumber() const;
    void setRemoteAsNumber(const qint32 &remote_as_number);
    bool is_remote_as_number_Set() const;
    bool is_remote_as_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_allow_transit;
    bool m_allow_transit_isSet;
    bool m_allow_transit_isValid;

    qint32 m_ebgp_hold_timer;
    bool m_ebgp_hold_timer_isSet;
    bool m_ebgp_hold_timer_isValid;

    qint32 m_ebgp_multihop;
    bool m_ebgp_multihop_isSet;
    bool m_ebgp_multihop_isValid;

    QString m_ip;
    bool m_ip_isSet;
    bool m_ip_isValid;

    OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner_ipv6 m_ipv6;
    bool m_ipv6_isSet;
    bool m_ipv6_isValid;

    qint32 m_receive_limit;
    bool m_receive_limit_isSet;
    bool m_receive_limit_isValid;

    qint32 m_remote_as_number;
    bool m_remote_as_number_isSet;
    bool m_remote_as_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner)

#endif // OAIUpdateNetworkApplianceVpnBgp_request_neighbors_inner_H
