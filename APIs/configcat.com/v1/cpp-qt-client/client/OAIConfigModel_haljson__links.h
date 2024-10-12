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
 * OAIConfigModel_haljson__links.h
 *
 * 
 */

#ifndef OAIConfigModel_haljson__links_H
#define OAIConfigModel_haljson__links_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIConfigModel_haljson__links : public OAIObject {
public:
    OAIConfigModel_haljson__links();
    OAIConfigModel_haljson__links(QString json);
    ~OAIConfigModel_haljson__links() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getSelf() const;
    void setSelf(const QString &self);
    bool is_self_Set() const;
    bool is_self_Valid() const;

    QString getSettings() const;
    void setSettings(const QString &settings);
    bool is_settings_Set() const;
    bool is_settings_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_self;
    bool m_self_isSet;
    bool m_self_isValid;

    QString m_settings;
    bool m_settings_isSet;
    bool m_settings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfigModel_haljson__links)

#endif // OAIConfigModel_haljson__links_H
