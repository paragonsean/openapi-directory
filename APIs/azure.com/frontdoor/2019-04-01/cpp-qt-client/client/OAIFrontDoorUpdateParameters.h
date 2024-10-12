/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFrontDoorUpdateParameters.h
 *
 * The properties needed to update a Front Door
 */

#ifndef OAIFrontDoorUpdateParameters_H
#define OAIFrontDoorUpdateParameters_H

#include <QJsonObject>

#include "OAIBackendPool.h"
#include "OAIBackendPoolsSettings.h"
#include "OAIFrontendEndpoint.h"
#include "OAIHealthProbeSettingsModel.h"
#include "OAILoadBalancingSettingsModel.h"
#include "OAIRoutingRule.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBackendPool;
class OAIBackendPoolsSettings;
class OAIFrontendEndpoint;
class OAIHealthProbeSettingsModel;
class OAILoadBalancingSettingsModel;
class OAIRoutingRule;

class OAIFrontDoorUpdateParameters : public OAIObject {
public:
    OAIFrontDoorUpdateParameters();
    OAIFrontDoorUpdateParameters(QString json);
    ~OAIFrontDoorUpdateParameters() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIBackendPool> getBackendPools() const;
    void setBackendPools(const QList<OAIBackendPool> &backend_pools);
    bool is_backend_pools_Set() const;
    bool is_backend_pools_Valid() const;

    OAIBackendPoolsSettings getBackendPoolsSettings() const;
    void setBackendPoolsSettings(const OAIBackendPoolsSettings &backend_pools_settings);
    bool is_backend_pools_settings_Set() const;
    bool is_backend_pools_settings_Valid() const;

    QString getEnabledState() const;
    void setEnabledState(const QString &enabled_state);
    bool is_enabled_state_Set() const;
    bool is_enabled_state_Valid() const;

    QString getFriendlyName() const;
    void setFriendlyName(const QString &friendly_name);
    bool is_friendly_name_Set() const;
    bool is_friendly_name_Valid() const;

    QList<OAIFrontendEndpoint> getFrontendEndpoints() const;
    void setFrontendEndpoints(const QList<OAIFrontendEndpoint> &frontend_endpoints);
    bool is_frontend_endpoints_Set() const;
    bool is_frontend_endpoints_Valid() const;

    QList<OAIHealthProbeSettingsModel> getHealthProbeSettings() const;
    void setHealthProbeSettings(const QList<OAIHealthProbeSettingsModel> &health_probe_settings);
    bool is_health_probe_settings_Set() const;
    bool is_health_probe_settings_Valid() const;

    QList<OAILoadBalancingSettingsModel> getLoadBalancingSettings() const;
    void setLoadBalancingSettings(const QList<OAILoadBalancingSettingsModel> &load_balancing_settings);
    bool is_load_balancing_settings_Set() const;
    bool is_load_balancing_settings_Valid() const;

    QList<OAIRoutingRule> getRoutingRules() const;
    void setRoutingRules(const QList<OAIRoutingRule> &routing_rules);
    bool is_routing_rules_Set() const;
    bool is_routing_rules_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIBackendPool> m_backend_pools;
    bool m_backend_pools_isSet;
    bool m_backend_pools_isValid;

    OAIBackendPoolsSettings m_backend_pools_settings;
    bool m_backend_pools_settings_isSet;
    bool m_backend_pools_settings_isValid;

    QString m_enabled_state;
    bool m_enabled_state_isSet;
    bool m_enabled_state_isValid;

    QString m_friendly_name;
    bool m_friendly_name_isSet;
    bool m_friendly_name_isValid;

    QList<OAIFrontendEndpoint> m_frontend_endpoints;
    bool m_frontend_endpoints_isSet;
    bool m_frontend_endpoints_isValid;

    QList<OAIHealthProbeSettingsModel> m_health_probe_settings;
    bool m_health_probe_settings_isSet;
    bool m_health_probe_settings_isValid;

    QList<OAILoadBalancingSettingsModel> m_load_balancing_settings;
    bool m_load_balancing_settings_isSet;
    bool m_load_balancing_settings_isValid;

    QList<OAIRoutingRule> m_routing_rules;
    bool m_routing_rules_isSet;
    bool m_routing_rules_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFrontDoorUpdateParameters)

#endif // OAIFrontDoorUpdateParameters_H
