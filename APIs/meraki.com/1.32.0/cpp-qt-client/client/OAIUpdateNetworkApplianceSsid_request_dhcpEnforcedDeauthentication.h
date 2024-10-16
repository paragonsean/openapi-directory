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
 * OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication.h
 *
 * DHCP Enforced Deauthentication enables the disassociation of wireless clients in addition to Mandatory DHCP. This param is only valid on firmware versions &gt;&#x3D; MX 17.0 where the associated LAN has Mandatory DHCP Enabled 
 */

#ifndef OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication_H
#define OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication : public OAIObject {
public:
    OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication();
    OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication(QString json);
    ~OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication)

#endif // OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication_H
