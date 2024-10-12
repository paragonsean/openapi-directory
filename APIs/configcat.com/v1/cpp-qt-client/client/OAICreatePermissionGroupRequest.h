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
 * OAICreatePermissionGroupRequest.h
 *
 * 
 */

#ifndef OAICreatePermissionGroupRequest_H
#define OAICreatePermissionGroupRequest_H

#include <QJsonObject>

#include "OAIAccessType.h"
#include "OAICreateOrUpdateEnvironmentAccessModel.h"
#include "OAIEnvironmentAccessType.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICreateOrUpdateEnvironmentAccessModel;

class OAICreatePermissionGroupRequest : public OAIObject {
public:
    OAICreatePermissionGroupRequest();
    OAICreatePermissionGroupRequest(QString json);
    ~OAICreatePermissionGroupRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAccessType getAccessType() const;
    void setAccessType(const OAIAccessType &access_type);
    bool is_access_type_Set() const;
    bool is_access_type_Valid() const;

    bool isCanCreateOrUpdateConfig() const;
    void setCanCreateOrUpdateConfig(const bool &can_create_or_update_config);
    bool is_can_create_or_update_config_Set() const;
    bool is_can_create_or_update_config_Valid() const;

    bool isCanCreateOrUpdateEnvironment() const;
    void setCanCreateOrUpdateEnvironment(const bool &can_create_or_update_environment);
    bool is_can_create_or_update_environment_Set() const;
    bool is_can_create_or_update_environment_Valid() const;

    bool isCanCreateOrUpdateSegments() const;
    void setCanCreateOrUpdateSegments(const bool &can_create_or_update_segments);
    bool is_can_create_or_update_segments_Set() const;
    bool is_can_create_or_update_segments_Valid() const;

    bool isCanCreateOrUpdateSetting() const;
    void setCanCreateOrUpdateSetting(const bool &can_create_or_update_setting);
    bool is_can_create_or_update_setting_Set() const;
    bool is_can_create_or_update_setting_Valid() const;

    bool isCanCreateOrUpdateTag() const;
    void setCanCreateOrUpdateTag(const bool &can_create_or_update_tag);
    bool is_can_create_or_update_tag_Set() const;
    bool is_can_create_or_update_tag_Valid() const;

    bool isCanDeleteConfig() const;
    void setCanDeleteConfig(const bool &can_delete_config);
    bool is_can_delete_config_Set() const;
    bool is_can_delete_config_Valid() const;

    bool isCanDeleteEnvironment() const;
    void setCanDeleteEnvironment(const bool &can_delete_environment);
    bool is_can_delete_environment_Set() const;
    bool is_can_delete_environment_Valid() const;

    bool isCanDeleteSegments() const;
    void setCanDeleteSegments(const bool &can_delete_segments);
    bool is_can_delete_segments_Set() const;
    bool is_can_delete_segments_Valid() const;

    bool isCanDeleteSetting() const;
    void setCanDeleteSetting(const bool &can_delete_setting);
    bool is_can_delete_setting_Set() const;
    bool is_can_delete_setting_Valid() const;

    bool isCanDeleteTag() const;
    void setCanDeleteTag(const bool &can_delete_tag);
    bool is_can_delete_tag_Set() const;
    bool is_can_delete_tag_Valid() const;

    bool isCanManageIntegrations() const;
    void setCanManageIntegrations(const bool &can_manage_integrations);
    bool is_can_manage_integrations_Set() const;
    bool is_can_manage_integrations_Valid() const;

    bool isCanManageMembers() const;
    void setCanManageMembers(const bool &can_manage_members);
    bool is_can_manage_members_Set() const;
    bool is_can_manage_members_Valid() const;

    bool isCanManageProductPreferences() const;
    void setCanManageProductPreferences(const bool &can_manage_product_preferences);
    bool is_can_manage_product_preferences_Set() const;
    bool is_can_manage_product_preferences_Valid() const;

    bool isCanManageWebhook() const;
    void setCanManageWebhook(const bool &can_manage_webhook);
    bool is_can_manage_webhook_Set() const;
    bool is_can_manage_webhook_Valid() const;

    bool isCanRotateSdkKey() const;
    void setCanRotateSdkKey(const bool &can_rotate_sdk_key);
    bool is_can_rotate_sdk_key_Set() const;
    bool is_can_rotate_sdk_key_Valid() const;

    bool isCanTagSetting() const;
    void setCanTagSetting(const bool &can_tag_setting);
    bool is_can_tag_setting_Set() const;
    bool is_can_tag_setting_Valid() const;

    bool isCanUseExportImport() const;
    void setCanUseExportImport(const bool &can_use_export_import);
    bool is_can_use_export_import_Set() const;
    bool is_can_use_export_import_Valid() const;

    bool isCanViewProductAuditLog() const;
    void setCanViewProductAuditLog(const bool &can_view_product_audit_log);
    bool is_can_view_product_audit_log_Set() const;
    bool is_can_view_product_audit_log_Valid() const;

    bool isCanViewProductStatistics() const;
    void setCanViewProductStatistics(const bool &can_view_product_statistics);
    bool is_can_view_product_statistics_Set() const;
    bool is_can_view_product_statistics_Valid() const;

    bool isCanViewSdkKey() const;
    void setCanViewSdkKey(const bool &can_view_sdk_key);
    bool is_can_view_sdk_key_Set() const;
    bool is_can_view_sdk_key_Valid() const;

    QList<OAICreateOrUpdateEnvironmentAccessModel> getEnvironmentAccesses() const;
    void setEnvironmentAccesses(const QList<OAICreateOrUpdateEnvironmentAccessModel> &environment_accesses);
    bool is_environment_accesses_Set() const;
    bool is_environment_accesses_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAIEnvironmentAccessType getNewEnvironmentAccessType() const;
    void setNewEnvironmentAccessType(const OAIEnvironmentAccessType &new_environment_access_type);
    bool is_new_environment_access_type_Set() const;
    bool is_new_environment_access_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAccessType m_access_type;
    bool m_access_type_isSet;
    bool m_access_type_isValid;

    bool m_can_create_or_update_config;
    bool m_can_create_or_update_config_isSet;
    bool m_can_create_or_update_config_isValid;

    bool m_can_create_or_update_environment;
    bool m_can_create_or_update_environment_isSet;
    bool m_can_create_or_update_environment_isValid;

    bool m_can_create_or_update_segments;
    bool m_can_create_or_update_segments_isSet;
    bool m_can_create_or_update_segments_isValid;

    bool m_can_create_or_update_setting;
    bool m_can_create_or_update_setting_isSet;
    bool m_can_create_or_update_setting_isValid;

    bool m_can_create_or_update_tag;
    bool m_can_create_or_update_tag_isSet;
    bool m_can_create_or_update_tag_isValid;

    bool m_can_delete_config;
    bool m_can_delete_config_isSet;
    bool m_can_delete_config_isValid;

    bool m_can_delete_environment;
    bool m_can_delete_environment_isSet;
    bool m_can_delete_environment_isValid;

    bool m_can_delete_segments;
    bool m_can_delete_segments_isSet;
    bool m_can_delete_segments_isValid;

    bool m_can_delete_setting;
    bool m_can_delete_setting_isSet;
    bool m_can_delete_setting_isValid;

    bool m_can_delete_tag;
    bool m_can_delete_tag_isSet;
    bool m_can_delete_tag_isValid;

    bool m_can_manage_integrations;
    bool m_can_manage_integrations_isSet;
    bool m_can_manage_integrations_isValid;

    bool m_can_manage_members;
    bool m_can_manage_members_isSet;
    bool m_can_manage_members_isValid;

    bool m_can_manage_product_preferences;
    bool m_can_manage_product_preferences_isSet;
    bool m_can_manage_product_preferences_isValid;

    bool m_can_manage_webhook;
    bool m_can_manage_webhook_isSet;
    bool m_can_manage_webhook_isValid;

    bool m_can_rotate_sdk_key;
    bool m_can_rotate_sdk_key_isSet;
    bool m_can_rotate_sdk_key_isValid;

    bool m_can_tag_setting;
    bool m_can_tag_setting_isSet;
    bool m_can_tag_setting_isValid;

    bool m_can_use_export_import;
    bool m_can_use_export_import_isSet;
    bool m_can_use_export_import_isValid;

    bool m_can_view_product_audit_log;
    bool m_can_view_product_audit_log_isSet;
    bool m_can_view_product_audit_log_isValid;

    bool m_can_view_product_statistics;
    bool m_can_view_product_statistics_isSet;
    bool m_can_view_product_statistics_isValid;

    bool m_can_view_sdk_key;
    bool m_can_view_sdk_key_isSet;
    bool m_can_view_sdk_key_isValid;

    QList<OAICreateOrUpdateEnvironmentAccessModel> m_environment_accesses;
    bool m_environment_accesses_isSet;
    bool m_environment_accesses_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAIEnvironmentAccessType m_new_environment_access_type;
    bool m_new_environment_access_type_isSet;
    bool m_new_environment_access_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreatePermissionGroupRequest)

#endif // OAICreatePermissionGroupRequest_H
