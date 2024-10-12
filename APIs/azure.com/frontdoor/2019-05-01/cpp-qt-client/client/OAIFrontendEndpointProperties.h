/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFrontendEndpointProperties.h
 *
 * The JSON object that contains the properties required to create a frontend endpoint.
 */

#ifndef OAIFrontendEndpointProperties_H
#define OAIFrontendEndpointProperties_H

#include <QJsonObject>

#include "OAICustomHttpsConfiguration.h"
#include "OAIFrontendEndpointUpdateParameters_webApplicationFirewallPolicyLink.h"
#include "OAIResourceState.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICustomHttpsConfiguration;
class OAIFrontendEndpointUpdateParameters_webApplicationFirewallPolicyLink;

class OAIFrontendEndpointProperties : public OAIObject {
public:
    OAIFrontendEndpointProperties();
    OAIFrontendEndpointProperties(QString json);
    ~OAIFrontendEndpointProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICustomHttpsConfiguration getCustomHttpsConfiguration() const;
    void setCustomHttpsConfiguration(const OAICustomHttpsConfiguration &custom_https_configuration);
    bool is_custom_https_configuration_Set() const;
    bool is_custom_https_configuration_Valid() const;

    QString getCustomHttpsProvisioningState() const;
    void setCustomHttpsProvisioningState(const QString &custom_https_provisioning_state);
    bool is_custom_https_provisioning_state_Set() const;
    bool is_custom_https_provisioning_state_Valid() const;

    QString getCustomHttpsProvisioningSubstate() const;
    void setCustomHttpsProvisioningSubstate(const QString &custom_https_provisioning_substate);
    bool is_custom_https_provisioning_substate_Set() const;
    bool is_custom_https_provisioning_substate_Valid() const;

    OAIResourceState getResourceState() const;
    void setResourceState(const OAIResourceState &resource_state);
    bool is_resource_state_Set() const;
    bool is_resource_state_Valid() const;

    QString getHostName() const;
    void setHostName(const QString &host_name);
    bool is_host_name_Set() const;
    bool is_host_name_Valid() const;

    QString getSessionAffinityEnabledState() const;
    void setSessionAffinityEnabledState(const QString &session_affinity_enabled_state);
    bool is_session_affinity_enabled_state_Set() const;
    bool is_session_affinity_enabled_state_Valid() const;

    qint32 getSessionAffinityTtlSeconds() const;
    void setSessionAffinityTtlSeconds(const qint32 &session_affinity_ttl_seconds);
    bool is_session_affinity_ttl_seconds_Set() const;
    bool is_session_affinity_ttl_seconds_Valid() const;

    OAIFrontendEndpointUpdateParameters_webApplicationFirewallPolicyLink getWebApplicationFirewallPolicyLink() const;
    void setWebApplicationFirewallPolicyLink(const OAIFrontendEndpointUpdateParameters_webApplicationFirewallPolicyLink &web_application_firewall_policy_link);
    bool is_web_application_firewall_policy_link_Set() const;
    bool is_web_application_firewall_policy_link_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICustomHttpsConfiguration m_custom_https_configuration;
    bool m_custom_https_configuration_isSet;
    bool m_custom_https_configuration_isValid;

    QString m_custom_https_provisioning_state;
    bool m_custom_https_provisioning_state_isSet;
    bool m_custom_https_provisioning_state_isValid;

    QString m_custom_https_provisioning_substate;
    bool m_custom_https_provisioning_substate_isSet;
    bool m_custom_https_provisioning_substate_isValid;

    OAIResourceState m_resource_state;
    bool m_resource_state_isSet;
    bool m_resource_state_isValid;

    QString m_host_name;
    bool m_host_name_isSet;
    bool m_host_name_isValid;

    QString m_session_affinity_enabled_state;
    bool m_session_affinity_enabled_state_isSet;
    bool m_session_affinity_enabled_state_isValid;

    qint32 m_session_affinity_ttl_seconds;
    bool m_session_affinity_ttl_seconds_isSet;
    bool m_session_affinity_ttl_seconds_isValid;

    OAIFrontendEndpointUpdateParameters_webApplicationFirewallPolicyLink m_web_application_firewall_policy_link;
    bool m_web_application_firewall_policy_link_isSet;
    bool m_web_application_firewall_policy_link_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFrontendEndpointProperties)

#endif // OAIFrontendEndpointProperties_H
