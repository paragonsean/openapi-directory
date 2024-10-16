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
 * OAICreateOrganizationBrandingPolicy_request.h
 *
 * 
 */

#ifndef OAICreateOrganizationBrandingPolicy_request_H
#define OAICreateOrganizationBrandingPolicy_request_H

#include <QJsonObject>

#include "OAICreateOrganizationBrandingPolicy_request_customLogo.h"
#include "OAICreateOrganizationBrandingPolicy_request_helpSettings.h"
#include "OAIGetOrganizationBrandingPolicies_200_response_inner_adminSettings.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationBrandingPolicies_200_response_inner_adminSettings;
class OAICreateOrganizationBrandingPolicy_request_customLogo;
class OAICreateOrganizationBrandingPolicy_request_helpSettings;

class OAICreateOrganizationBrandingPolicy_request : public OAIObject {
public:
    OAICreateOrganizationBrandingPolicy_request();
    OAICreateOrganizationBrandingPolicy_request(QString json);
    ~OAICreateOrganizationBrandingPolicy_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetOrganizationBrandingPolicies_200_response_inner_adminSettings getAdminSettings() const;
    void setAdminSettings(const OAIGetOrganizationBrandingPolicies_200_response_inner_adminSettings &admin_settings);
    bool is_admin_settings_Set() const;
    bool is_admin_settings_Valid() const;

    OAICreateOrganizationBrandingPolicy_request_customLogo getCustomLogo() const;
    void setCustomLogo(const OAICreateOrganizationBrandingPolicy_request_customLogo &custom_logo);
    bool is_custom_logo_Set() const;
    bool is_custom_logo_Valid() const;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    OAICreateOrganizationBrandingPolicy_request_helpSettings getHelpSettings() const;
    void setHelpSettings(const OAICreateOrganizationBrandingPolicy_request_helpSettings &help_settings);
    bool is_help_settings_Set() const;
    bool is_help_settings_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetOrganizationBrandingPolicies_200_response_inner_adminSettings m_admin_settings;
    bool m_admin_settings_isSet;
    bool m_admin_settings_isValid;

    OAICreateOrganizationBrandingPolicy_request_customLogo m_custom_logo;
    bool m_custom_logo_isSet;
    bool m_custom_logo_isValid;

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    OAICreateOrganizationBrandingPolicy_request_helpSettings m_help_settings;
    bool m_help_settings_isSet;
    bool m_help_settings_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateOrganizationBrandingPolicy_request)

#endif // OAICreateOrganizationBrandingPolicy_request_H
