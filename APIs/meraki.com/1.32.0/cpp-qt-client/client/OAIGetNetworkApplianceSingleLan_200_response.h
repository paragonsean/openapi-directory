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
 * OAIGetNetworkApplianceSingleLan_200_response.h
 *
 * 
 */

#ifndef OAIGetNetworkApplianceSingleLan_200_response_H
#define OAIGetNetworkApplianceSingleLan_200_response_H

#include <QJsonObject>

#include "OAIGetNetworkApplianceSingleLan_200_response_ipv6.h"
#include "OAIGetNetworkApplianceSingleLan_200_response_mandatoryDhcp.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNetworkApplianceSingleLan_200_response_ipv6;
class OAIGetNetworkApplianceSingleLan_200_response_mandatoryDhcp;

class OAIGetNetworkApplianceSingleLan_200_response : public OAIObject {
public:
    OAIGetNetworkApplianceSingleLan_200_response();
    OAIGetNetworkApplianceSingleLan_200_response(QString json);
    ~OAIGetNetworkApplianceSingleLan_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getApplianceIp() const;
    void setApplianceIp(const QString &appliance_ip);
    bool is_appliance_ip_Set() const;
    bool is_appliance_ip_Valid() const;

    OAIGetNetworkApplianceSingleLan_200_response_ipv6 getIpv6() const;
    void setIpv6(const OAIGetNetworkApplianceSingleLan_200_response_ipv6 &ipv6);
    bool is_ipv6_Set() const;
    bool is_ipv6_Valid() const;

    OAIGetNetworkApplianceSingleLan_200_response_mandatoryDhcp getMandatoryDhcp() const;
    void setMandatoryDhcp(const OAIGetNetworkApplianceSingleLan_200_response_mandatoryDhcp &mandatory_dhcp);
    bool is_mandatory_dhcp_Set() const;
    bool is_mandatory_dhcp_Valid() const;

    QString getSubnet() const;
    void setSubnet(const QString &subnet);
    bool is_subnet_Set() const;
    bool is_subnet_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_appliance_ip;
    bool m_appliance_ip_isSet;
    bool m_appliance_ip_isValid;

    OAIGetNetworkApplianceSingleLan_200_response_ipv6 m_ipv6;
    bool m_ipv6_isSet;
    bool m_ipv6_isValid;

    OAIGetNetworkApplianceSingleLan_200_response_mandatoryDhcp m_mandatory_dhcp;
    bool m_mandatory_dhcp_isSet;
    bool m_mandatory_dhcp_isValid;

    QString m_subnet;
    bool m_subnet_isSet;
    bool m_subnet_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkApplianceSingleLan_200_response)

#endif // OAIGetNetworkApplianceSingleLan_200_response_H
