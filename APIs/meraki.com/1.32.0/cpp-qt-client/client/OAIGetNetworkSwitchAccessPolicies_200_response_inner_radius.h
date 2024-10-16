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
 * OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius.h
 *
 * Object for RADIUS Settings
 */

#ifndef OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius_H
#define OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius_H

#include <QJsonObject>

#include "OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius_criticalAuth.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius_criticalAuth;

class OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius : public OAIObject {
public:
    OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius();
    OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius(QString json);
    ~OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius_criticalAuth getCriticalAuth() const;
    void setCriticalAuth(const OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius_criticalAuth &critical_auth);
    bool is_critical_auth_Set() const;
    bool is_critical_auth_Valid() const;

    qint32 getFailedAuthVlanId() const;
    void setFailedAuthVlanId(const qint32 &failed_auth_vlan_id);
    bool is_failed_auth_vlan_id_Set() const;
    bool is_failed_auth_vlan_id_Valid() const;

    qint32 getReAuthenticationInterval() const;
    void setReAuthenticationInterval(const qint32 &re_authentication_interval);
    bool is_re_authentication_interval_Set() const;
    bool is_re_authentication_interval_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius_criticalAuth m_critical_auth;
    bool m_critical_auth_isSet;
    bool m_critical_auth_isValid;

    qint32 m_failed_auth_vlan_id;
    bool m_failed_auth_vlan_id_isSet;
    bool m_failed_auth_vlan_id_isValid;

    qint32 m_re_authentication_interval;
    bool m_re_authentication_interval_isSet;
    bool m_re_authentication_interval_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius)

#endif // OAIGetNetworkSwitchAccessPolicies_200_response_inner_radius_H
