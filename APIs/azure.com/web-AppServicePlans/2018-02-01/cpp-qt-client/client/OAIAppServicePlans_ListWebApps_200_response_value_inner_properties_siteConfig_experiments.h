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
 * OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments.h
 *
 * Routing rules in production experiments.
 */

#ifndef OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments_H
#define OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments_H

#include <QJsonObject>

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments_rampUpRules_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments_rampUpRules_inner;

class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments : public OAIObject {
public:
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments();
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments(QString json);
    ~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments_rampUpRules_inner> getRampUpRules() const;
    void setRampUpRules(const QList<OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments_rampUpRules_inner> &ramp_up_rules);
    bool is_ramp_up_rules_Set() const;
    bool is_ramp_up_rules_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments_rampUpRules_inner> m_ramp_up_rules;
    bool m_ramp_up_rules_isSet;
    bool m_ramp_up_rules_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments)

#endif // OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_experiments_H
