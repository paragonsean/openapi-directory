/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo.h
 *
 * Information needed for cloning operation.
 */

#ifndef OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo_H
#define OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo_H

#include <QJsonObject>

#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo : public OAIObject {
public:
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo();
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo(QString json);
    ~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, QString> getAppSettingsOverrides() const;
    void setAppSettingsOverrides(const QMap<QString, QString> &app_settings_overrides);
    bool is_app_settings_overrides_Set() const;
    bool is_app_settings_overrides_Valid() const;

    bool isCloneCustomHostNames() const;
    void setCloneCustomHostNames(const bool &clone_custom_host_names);
    bool is_clone_custom_host_names_Set() const;
    bool is_clone_custom_host_names_Valid() const;

    bool isCloneSourceControl() const;
    void setCloneSourceControl(const bool &clone_source_control);
    bool is_clone_source_control_Set() const;
    bool is_clone_source_control_Valid() const;

    bool isConfigureLoadBalancing() const;
    void setConfigureLoadBalancing(const bool &configure_load_balancing);
    bool is_configure_load_balancing_Set() const;
    bool is_configure_load_balancing_Valid() const;

    QString getCorrelationId() const;
    void setCorrelationId(const QString &correlation_id);
    bool is_correlation_id_Set() const;
    bool is_correlation_id_Valid() const;

    QString getHostingEnvironment() const;
    void setHostingEnvironment(const QString &hosting_environment);
    bool is_hosting_environment_Set() const;
    bool is_hosting_environment_Valid() const;

    bool isIgnoreQuotas() const;
    void setIgnoreQuotas(const bool &ignore_quotas);
    bool is_ignore_quotas_Set() const;
    bool is_ignore_quotas_Valid() const;

    bool isOverwrite() const;
    void setOverwrite(const bool &overwrite);
    bool is_overwrite_Set() const;
    bool is_overwrite_Valid() const;

    QString getSourceWebAppId() const;
    void setSourceWebAppId(const QString &source_web_app_id);
    bool is_source_web_app_id_Set() const;
    bool is_source_web_app_id_Valid() const;

    QString getTrafficManagerProfileId() const;
    void setTrafficManagerProfileId(const QString &traffic_manager_profile_id);
    bool is_traffic_manager_profile_id_Set() const;
    bool is_traffic_manager_profile_id_Valid() const;

    QString getTrafficManagerProfileName() const;
    void setTrafficManagerProfileName(const QString &traffic_manager_profile_name);
    bool is_traffic_manager_profile_name_Set() const;
    bool is_traffic_manager_profile_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, QString> m_app_settings_overrides;
    bool m_app_settings_overrides_isSet;
    bool m_app_settings_overrides_isValid;

    bool m_clone_custom_host_names;
    bool m_clone_custom_host_names_isSet;
    bool m_clone_custom_host_names_isValid;

    bool m_clone_source_control;
    bool m_clone_source_control_isSet;
    bool m_clone_source_control_isValid;

    bool m_configure_load_balancing;
    bool m_configure_load_balancing_isSet;
    bool m_configure_load_balancing_isValid;

    QString m_correlation_id;
    bool m_correlation_id_isSet;
    bool m_correlation_id_isValid;

    QString m_hosting_environment;
    bool m_hosting_environment_isSet;
    bool m_hosting_environment_isValid;

    bool m_ignore_quotas;
    bool m_ignore_quotas_isSet;
    bool m_ignore_quotas_isValid;

    bool m_overwrite;
    bool m_overwrite_isSet;
    bool m_overwrite_isValid;

    QString m_source_web_app_id;
    bool m_source_web_app_id_isSet;
    bool m_source_web_app_id_isValid;

    QString m_traffic_manager_profile_id;
    bool m_traffic_manager_profile_id_isSet;
    bool m_traffic_manager_profile_id_isValid;

    QString m_traffic_manager_profile_name;
    bool m_traffic_manager_profile_name_isSet;
    bool m_traffic_manager_profile_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo)

#endif // OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo_H
