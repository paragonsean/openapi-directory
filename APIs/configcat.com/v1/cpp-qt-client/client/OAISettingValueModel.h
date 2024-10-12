/**
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISettingValueModel.h
 *
 * 
 */

#ifndef OAISettingValueModel_H
#define OAISettingValueModel_H

#include <QJsonObject>

#include "OAIConfigModel.h"
#include "OAIEnvironmentModel.h"
#include "OAIIntegrationLinkModel.h"
#include "OAIRolloutPercentageItemModel.h"
#include "OAIRolloutRuleModel.h"
#include "OAISettingDataModel.h"
#include "OAISettingTagModel.h"
#include <QDateTime>
#include <QJsonValue>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConfigModel;
class OAIEnvironmentModel;
class OAIIntegrationLinkModel;
class OAIRolloutPercentageItemModel;
class OAIRolloutRuleModel;
class OAISettingDataModel;
class OAISettingTagModel;

class OAISettingValueModel : public OAIObject {
public:
    OAISettingValueModel();
    OAISettingValueModel(QString json);
    ~OAISettingValueModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIConfigModel getConfig() const;
    void setConfig(const OAIConfigModel &config);
    bool is_config_Set() const;
    bool is_config_Valid() const;

    OAIEnvironmentModel getEnvironment() const;
    void setEnvironment(const OAIEnvironmentModel &environment);
    bool is_environment_Set() const;
    bool is_environment_Valid() const;

    QList<OAIIntegrationLinkModel> getIntegrationLinks() const;
    void setIntegrationLinks(const QList<OAIIntegrationLinkModel> &integration_links);
    bool is_integration_links_Set() const;
    bool is_integration_links_Valid() const;

    QString getLastUpdaterUserEmail() const;
    void setLastUpdaterUserEmail(const QString &last_updater_user_email);
    bool is_last_updater_user_email_Set() const;
    bool is_last_updater_user_email_Valid() const;

    QString getLastUpdaterUserFullName() const;
    void setLastUpdaterUserFullName(const QString &last_updater_user_full_name);
    bool is_last_updater_user_full_name_Set() const;
    bool is_last_updater_user_full_name_Valid() const;

    bool isReadOnly() const;
    void setReadOnly(const bool &read_only);
    bool is_read_only_Set() const;
    bool is_read_only_Valid() const;

    QList<OAIRolloutPercentageItemModel> getRolloutPercentageItems() const;
    void setRolloutPercentageItems(const QList<OAIRolloutPercentageItemModel> &rollout_percentage_items);
    bool is_rollout_percentage_items_Set() const;
    bool is_rollout_percentage_items_Valid() const;

    QList<OAIRolloutRuleModel> getRolloutRules() const;
    void setRolloutRules(const QList<OAIRolloutRuleModel> &rollout_rules);
    bool is_rollout_rules_Set() const;
    bool is_rollout_rules_Valid() const;

    OAISettingDataModel getSetting() const;
    void setSetting(const OAISettingDataModel &setting);
    bool is_setting_Set() const;
    bool is_setting_Valid() const;

    QList<OAISettingTagModel> getSettingTags() const;
    void setSettingTags(const QList<OAISettingTagModel> &setting_tags);
    bool is_setting_tags_Set() const;
    bool is_setting_tags_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    QJsonValue getValue() const;
    void setValue(const QJsonValue &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIConfigModel m_config;
    bool m_config_isSet;
    bool m_config_isValid;

    OAIEnvironmentModel m_environment;
    bool m_environment_isSet;
    bool m_environment_isValid;

    QList<OAIIntegrationLinkModel> m_integration_links;
    bool m_integration_links_isSet;
    bool m_integration_links_isValid;

    QString m_last_updater_user_email;
    bool m_last_updater_user_email_isSet;
    bool m_last_updater_user_email_isValid;

    QString m_last_updater_user_full_name;
    bool m_last_updater_user_full_name_isSet;
    bool m_last_updater_user_full_name_isValid;

    bool m_read_only;
    bool m_read_only_isSet;
    bool m_read_only_isValid;

    QList<OAIRolloutPercentageItemModel> m_rollout_percentage_items;
    bool m_rollout_percentage_items_isSet;
    bool m_rollout_percentage_items_isValid;

    QList<OAIRolloutRuleModel> m_rollout_rules;
    bool m_rollout_rules_isSet;
    bool m_rollout_rules_isValid;

    OAISettingDataModel m_setting;
    bool m_setting_isSet;
    bool m_setting_isValid;

    QList<OAISettingTagModel> m_setting_tags;
    bool m_setting_tags_isSet;
    bool m_setting_tags_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    QJsonValue m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISettingValueModel)

#endif // OAISettingValueModel_H
