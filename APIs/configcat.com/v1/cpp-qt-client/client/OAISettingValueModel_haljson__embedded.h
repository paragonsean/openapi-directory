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
 * OAISettingValueModel_haljson__embedded.h
 *
 * 
 */

#ifndef OAISettingValueModel_haljson__embedded_H
#define OAISettingValueModel_haljson__embedded_H

#include <QJsonObject>

#include "OAISettingValueModel_haljson__embedded_config.h"
#include "OAISettingValueModel_haljson__embedded_environment.h"
#include "OAISettingValueModel_haljson__embedded_integrationLinks_inner.h"
#include "OAISettingValueModel_haljson__embedded_setting.h"
#include "OAISettingValueModel_haljson__embedded_settingTags_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISettingValueModel_haljson__embedded_config;
class OAISettingValueModel_haljson__embedded_environment;
class OAISettingValueModel_haljson__embedded_integrationLinks_inner;
class OAISettingValueModel_haljson__embedded_setting;
class OAISettingValueModel_haljson__embedded_settingTags_inner;

class OAISettingValueModel_haljson__embedded : public OAIObject {
public:
    OAISettingValueModel_haljson__embedded();
    OAISettingValueModel_haljson__embedded(QString json);
    ~OAISettingValueModel_haljson__embedded() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISettingValueModel_haljson__embedded_config getConfig() const;
    void setConfig(const OAISettingValueModel_haljson__embedded_config &config);
    bool is_config_Set() const;
    bool is_config_Valid() const;

    OAISettingValueModel_haljson__embedded_environment getEnvironment() const;
    void setEnvironment(const OAISettingValueModel_haljson__embedded_environment &environment);
    bool is_environment_Set() const;
    bool is_environment_Valid() const;

    QList<OAISettingValueModel_haljson__embedded_integrationLinks_inner> getIntegrationLinks() const;
    void setIntegrationLinks(const QList<OAISettingValueModel_haljson__embedded_integrationLinks_inner> &integration_links);
    bool is_integration_links_Set() const;
    bool is_integration_links_Valid() const;

    OAISettingValueModel_haljson__embedded_setting getSetting() const;
    void setSetting(const OAISettingValueModel_haljson__embedded_setting &setting);
    bool is_setting_Set() const;
    bool is_setting_Valid() const;

    QList<OAISettingValueModel_haljson__embedded_settingTags_inner> getSettingTags() const;
    void setSettingTags(const QList<OAISettingValueModel_haljson__embedded_settingTags_inner> &setting_tags);
    bool is_setting_tags_Set() const;
    bool is_setting_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISettingValueModel_haljson__embedded_config m_config;
    bool m_config_isSet;
    bool m_config_isValid;

    OAISettingValueModel_haljson__embedded_environment m_environment;
    bool m_environment_isSet;
    bool m_environment_isValid;

    QList<OAISettingValueModel_haljson__embedded_integrationLinks_inner> m_integration_links;
    bool m_integration_links_isSet;
    bool m_integration_links_isValid;

    OAISettingValueModel_haljson__embedded_setting m_setting;
    bool m_setting_isSet;
    bool m_setting_isValid;

    QList<OAISettingValueModel_haljson__embedded_settingTags_inner> m_setting_tags;
    bool m_setting_tags_isSet;
    bool m_setting_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISettingValueModel_haljson__embedded)

#endif // OAISettingValueModel_haljson__embedded_H
