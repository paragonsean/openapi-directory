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
 * OAISegmentModel_haljson.h
 *
 * 
 */

#ifndef OAISegmentModel_haljson_H
#define OAISegmentModel_haljson_H

#include <QJsonObject>

#include "OAIConfigModel_haljson__embedded.h"
#include "OAIEnvironmentModel_haljson__links.h"
#include "OAIRolloutRuleComparator.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConfigModel_haljson__embedded;
class OAIEnvironmentModel_haljson__links;

class OAISegmentModel_haljson : public OAIObject {
public:
    OAISegmentModel_haljson();
    OAISegmentModel_haljson(QString json);
    ~OAISegmentModel_haljson() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIConfigModel_haljson__embedded getEmbedded() const;
    void setEmbedded(const OAIConfigModel_haljson__embedded &_embedded);
    bool is__embedded_Set() const;
    bool is__embedded_Valid() const;

    OAIEnvironmentModel_haljson__links getLinks() const;
    void setLinks(const OAIEnvironmentModel_haljson__links &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    OAIRolloutRuleComparator getComparator() const;
    void setComparator(const OAIRolloutRuleComparator &comparator);
    bool is_comparator_Set() const;
    bool is_comparator_Valid() const;

    QString getComparisonAttribute() const;
    void setComparisonAttribute(const QString &comparison_attribute);
    bool is_comparison_attribute_Set() const;
    bool is_comparison_attribute_Valid() const;

    QString getComparisonValue() const;
    void setComparisonValue(const QString &comparison_value);
    bool is_comparison_value_Set() const;
    bool is_comparison_value_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getCreatorEmail() const;
    void setCreatorEmail(const QString &creator_email);
    bool is_creator_email_Set() const;
    bool is_creator_email_Valid() const;

    QString getCreatorFullName() const;
    void setCreatorFullName(const QString &creator_full_name);
    bool is_creator_full_name_Set() const;
    bool is_creator_full_name_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getLastUpdaterEmail() const;
    void setLastUpdaterEmail(const QString &last_updater_email);
    bool is_last_updater_email_Set() const;
    bool is_last_updater_email_Valid() const;

    QString getLastUpdaterFullName() const;
    void setLastUpdaterFullName(const QString &last_updater_full_name);
    bool is_last_updater_full_name_Set() const;
    bool is_last_updater_full_name_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getSegmentId() const;
    void setSegmentId(const QString &segment_id);
    bool is_segment_id_Set() const;
    bool is_segment_id_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIConfigModel_haljson__embedded m__embedded;
    bool m__embedded_isSet;
    bool m__embedded_isValid;

    OAIEnvironmentModel_haljson__links m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    OAIRolloutRuleComparator m_comparator;
    bool m_comparator_isSet;
    bool m_comparator_isValid;

    QString m_comparison_attribute;
    bool m_comparison_attribute_isSet;
    bool m_comparison_attribute_isValid;

    QString m_comparison_value;
    bool m_comparison_value_isSet;
    bool m_comparison_value_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_creator_email;
    bool m_creator_email_isSet;
    bool m_creator_email_isValid;

    QString m_creator_full_name;
    bool m_creator_full_name_isSet;
    bool m_creator_full_name_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_last_updater_email;
    bool m_last_updater_email_isSet;
    bool m_last_updater_email_isValid;

    QString m_last_updater_full_name;
    bool m_last_updater_full_name_isSet;
    bool m_last_updater_full_name_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_segment_id;
    bool m_segment_id_isSet;
    bool m_segment_id_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISegmentModel_haljson)

#endif // OAISegmentModel_haljson_H
