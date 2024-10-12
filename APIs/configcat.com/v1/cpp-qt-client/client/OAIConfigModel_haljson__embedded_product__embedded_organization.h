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
 * OAIConfigModel_haljson__embedded_product__embedded_organization.h
 *
 * 
 */

#ifndef OAIConfigModel_haljson__embedded_product__embedded_organization_H
#define OAIConfigModel_haljson__embedded_product__embedded_organization_H

#include <QJsonObject>

#include "OAIConfigModel_haljson__embedded_product__embedded_organization__links.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConfigModel_haljson__embedded_product__embedded_organization__links;

class OAIConfigModel_haljson__embedded_product__embedded_organization : public OAIObject {
public:
    OAIConfigModel_haljson__embedded_product__embedded_organization();
    OAIConfigModel_haljson__embedded_product__embedded_organization(QString json);
    ~OAIConfigModel_haljson__embedded_product__embedded_organization() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIConfigModel_haljson__embedded_product__embedded_organization__links getLinks() const;
    void setLinks(const OAIConfigModel_haljson__embedded_product__embedded_organization__links &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOrganizationId() const;
    void setOrganizationId(const QString &organization_id);
    bool is_organization_id_Set() const;
    bool is_organization_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIConfigModel_haljson__embedded_product__embedded_organization__links m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_organization_id;
    bool m_organization_id_isSet;
    bool m_organization_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfigModel_haljson__embedded_product__embedded_organization)

#endif // OAIConfigModel_haljson__embedded_product__embedded_organization_H
