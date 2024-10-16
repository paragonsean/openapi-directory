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
 * OAIGetOrganizationLoginSecurity_200_response_apiAuthentication.h
 *
 * Details for indicating whether organization will restrict access to API (but not Dashboard) to certain IP addresses.
 */

#ifndef OAIGetOrganizationLoginSecurity_200_response_apiAuthentication_H
#define OAIGetOrganizationLoginSecurity_200_response_apiAuthentication_H

#include <QJsonObject>

#include "OAIGetOrganizationLoginSecurity_200_response_apiAuthentication_ipRestrictionsForKeys.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationLoginSecurity_200_response_apiAuthentication_ipRestrictionsForKeys;

class OAIGetOrganizationLoginSecurity_200_response_apiAuthentication : public OAIObject {
public:
    OAIGetOrganizationLoginSecurity_200_response_apiAuthentication();
    OAIGetOrganizationLoginSecurity_200_response_apiAuthentication(QString json);
    ~OAIGetOrganizationLoginSecurity_200_response_apiAuthentication() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetOrganizationLoginSecurity_200_response_apiAuthentication_ipRestrictionsForKeys getIpRestrictionsForKeys() const;
    void setIpRestrictionsForKeys(const OAIGetOrganizationLoginSecurity_200_response_apiAuthentication_ipRestrictionsForKeys &ip_restrictions_for_keys);
    bool is_ip_restrictions_for_keys_Set() const;
    bool is_ip_restrictions_for_keys_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetOrganizationLoginSecurity_200_response_apiAuthentication_ipRestrictionsForKeys m_ip_restrictions_for_keys;
    bool m_ip_restrictions_for_keys_isSet;
    bool m_ip_restrictions_for_keys_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationLoginSecurity_200_response_apiAuthentication)

#endif // OAIGetOrganizationLoginSecurity_200_response_apiAuthentication_H
