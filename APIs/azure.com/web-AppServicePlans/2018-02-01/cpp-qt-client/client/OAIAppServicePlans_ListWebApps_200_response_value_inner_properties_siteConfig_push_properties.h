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
 * OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_push_properties.h
 *
 * PushSettings resource specific properties
 */

#ifndef OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_push_properties_H
#define OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_push_properties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_push_properties : public OAIObject {
public:
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_push_properties();
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_push_properties(QString json);
    ~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_push_properties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDynamicTagsJson() const;
    void setDynamicTagsJson(const QString &dynamic_tags_json);
    bool is_dynamic_tags_json_Set() const;
    bool is_dynamic_tags_json_Valid() const;

    bool isIsPushEnabled() const;
    void setIsPushEnabled(const bool &is_push_enabled);
    bool is_is_push_enabled_Set() const;
    bool is_is_push_enabled_Valid() const;

    QString getTagWhitelistJson() const;
    void setTagWhitelistJson(const QString &tag_whitelist_json);
    bool is_tag_whitelist_json_Set() const;
    bool is_tag_whitelist_json_Valid() const;

    QString getTagsRequiringAuth() const;
    void setTagsRequiringAuth(const QString &tags_requiring_auth);
    bool is_tags_requiring_auth_Set() const;
    bool is_tags_requiring_auth_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_dynamic_tags_json;
    bool m_dynamic_tags_json_isSet;
    bool m_dynamic_tags_json_isValid;

    bool m_is_push_enabled;
    bool m_is_push_enabled_isSet;
    bool m_is_push_enabled_isValid;

    QString m_tag_whitelist_json;
    bool m_tag_whitelist_json_isSet;
    bool m_tag_whitelist_json_isValid;

    QString m_tags_requiring_auth;
    bool m_tags_requiring_auth_isSet;
    bool m_tags_requiring_auth_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_push_properties)

#endif // OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_push_properties_H
