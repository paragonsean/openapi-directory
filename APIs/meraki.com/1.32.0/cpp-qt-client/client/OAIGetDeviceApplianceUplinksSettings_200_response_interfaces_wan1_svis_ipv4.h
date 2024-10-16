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
 * OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4.h
 *
 * IPv4 settings for static/dynamic mode.
 */

#ifndef OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_H
#define OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_H

#include <QJsonObject>

#include "OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_nameservers.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_nameservers;

class OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4 : public OAIObject {
public:
    OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4();
    OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4(QString json);
    ~OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddress() const;
    void setAddress(const QString &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QString getAssignmentMode() const;
    void setAssignmentMode(const QString &assignment_mode);
    bool is_assignment_mode_Set() const;
    bool is_assignment_mode_Valid() const;

    QString getGateway() const;
    void setGateway(const QString &gateway);
    bool is_gateway_Set() const;
    bool is_gateway_Valid() const;

    OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_nameservers getNameservers() const;
    void setNameservers(const OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_nameservers &nameservers);
    bool is_nameservers_Set() const;
    bool is_nameservers_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QString m_assignment_mode;
    bool m_assignment_mode_isSet;
    bool m_assignment_mode_isValid;

    QString m_gateway;
    bool m_gateway_isSet;
    bool m_gateway_isValid;

    OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_nameservers m_nameservers;
    bool m_nameservers_isSet;
    bool m_nameservers_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4)

#endif // OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_H
