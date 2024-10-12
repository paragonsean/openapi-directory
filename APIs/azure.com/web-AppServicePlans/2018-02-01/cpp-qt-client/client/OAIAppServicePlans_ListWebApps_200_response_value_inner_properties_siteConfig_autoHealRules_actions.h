/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions.h
 *
 * Actions which to take by the auto-heal module when a rule is triggered.
 */

#ifndef OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions_H
#define OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions_H

#include <QJsonObject>

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions_customAction.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions_customAction;

class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions : public OAIObject {
public:
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions();
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions(QString json);
    ~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getActionType() const;
    void setActionType(const QString &action_type);
    bool is_action_type_Set() const;
    bool is_action_type_Valid() const;

    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions_customAction getCustomAction() const;
    void setCustomAction(const OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions_customAction &custom_action);
    bool is_custom_action_Set() const;
    bool is_custom_action_Valid() const;

    QString getMinProcessExecutionTime() const;
    void setMinProcessExecutionTime(const QString &min_process_execution_time);
    bool is_min_process_execution_time_Set() const;
    bool is_min_process_execution_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_action_type;
    bool m_action_type_isSet;
    bool m_action_type_isValid;

    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions_customAction m_custom_action;
    bool m_custom_action_isSet;
    bool m_custom_action_isValid;

    QString m_min_process_execution_time;
    bool m_min_process_execution_time_isSet;
    bool m_min_process_execution_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions)

#endif // OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_actions_H
