/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateNetworkSwitchSettingsQosRule_request.h
 *
 * 
 */

#ifndef OAIUpdateNetworkSwitchSettingsQosRule_request_H
#define OAIUpdateNetworkSwitchSettingsQosRule_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNetworkSwitchSettingsQosRule_request : public OAIObject {
public:
    OAIUpdateNetworkSwitchSettingsQosRule_request();
    OAIUpdateNetworkSwitchSettingsQosRule_request(QString json);
    ~OAIUpdateNetworkSwitchSettingsQosRule_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getDscp() const;
    void setDscp(const qint32 &dscp);
    bool is_dscp_Set() const;
    bool is_dscp_Valid() const;

    qint32 getDstPort() const;
    void setDstPort(const qint32 &dst_port);
    bool is_dst_port_Set() const;
    bool is_dst_port_Valid() const;

    QString getDstPortRange() const;
    void setDstPortRange(const QString &dst_port_range);
    bool is_dst_port_range_Set() const;
    bool is_dst_port_range_Valid() const;

    QString getProtocol() const;
    void setProtocol(const QString &protocol);
    bool is_protocol_Set() const;
    bool is_protocol_Valid() const;

    qint32 getSrcPort() const;
    void setSrcPort(const qint32 &src_port);
    bool is_src_port_Set() const;
    bool is_src_port_Valid() const;

    QString getSrcPortRange() const;
    void setSrcPortRange(const QString &src_port_range);
    bool is_src_port_range_Set() const;
    bool is_src_port_range_Valid() const;

    qint32 getVlan() const;
    void setVlan(const qint32 &vlan);
    bool is_vlan_Set() const;
    bool is_vlan_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_dscp;
    bool m_dscp_isSet;
    bool m_dscp_isValid;

    qint32 m_dst_port;
    bool m_dst_port_isSet;
    bool m_dst_port_isValid;

    QString m_dst_port_range;
    bool m_dst_port_range_isSet;
    bool m_dst_port_range_isValid;

    QString m_protocol;
    bool m_protocol_isSet;
    bool m_protocol_isValid;

    qint32 m_src_port;
    bool m_src_port_isSet;
    bool m_src_port_isValid;

    QString m_src_port_range;
    bool m_src_port_range_isSet;
    bool m_src_port_range_isValid;

    qint32 m_vlan;
    bool m_vlan_isSet;
    bool m_vlan_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkSwitchSettingsQosRule_request)

#endif // OAIUpdateNetworkSwitchSettingsQosRule_request_H
