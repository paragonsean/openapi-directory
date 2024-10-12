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

#include "OAISegmentModel_haljson.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISegmentModel_haljson::OAISegmentModel_haljson(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISegmentModel_haljson::OAISegmentModel_haljson() {
    this->initializeModel();
}

OAISegmentModel_haljson::~OAISegmentModel_haljson() {}

void OAISegmentModel_haljson::initializeModel() {

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_comparator_isSet = false;
    m_comparator_isValid = false;

    m_comparison_attribute_isSet = false;
    m_comparison_attribute_isValid = false;

    m_comparison_value_isSet = false;
    m_comparison_value_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_creator_email_isSet = false;
    m_creator_email_isValid = false;

    m_creator_full_name_isSet = false;
    m_creator_full_name_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_last_updater_email_isSet = false;
    m_last_updater_email_isValid = false;

    m_last_updater_full_name_isSet = false;
    m_last_updater_full_name_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_segment_id_isSet = false;
    m_segment_id_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAISegmentModel_haljson::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISegmentModel_haljson::fromJsonObject(QJsonObject json) {

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_comparator_isValid = ::OpenAPI::fromJsonValue(m_comparator, json[QString("comparator")]);
    m_comparator_isSet = !json[QString("comparator")].isNull() && m_comparator_isValid;

    m_comparison_attribute_isValid = ::OpenAPI::fromJsonValue(m_comparison_attribute, json[QString("comparisonAttribute")]);
    m_comparison_attribute_isSet = !json[QString("comparisonAttribute")].isNull() && m_comparison_attribute_isValid;

    m_comparison_value_isValid = ::OpenAPI::fromJsonValue(m_comparison_value, json[QString("comparisonValue")]);
    m_comparison_value_isSet = !json[QString("comparisonValue")].isNull() && m_comparison_value_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_creator_email_isValid = ::OpenAPI::fromJsonValue(m_creator_email, json[QString("creatorEmail")]);
    m_creator_email_isSet = !json[QString("creatorEmail")].isNull() && m_creator_email_isValid;

    m_creator_full_name_isValid = ::OpenAPI::fromJsonValue(m_creator_full_name, json[QString("creatorFullName")]);
    m_creator_full_name_isSet = !json[QString("creatorFullName")].isNull() && m_creator_full_name_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_last_updater_email_isValid = ::OpenAPI::fromJsonValue(m_last_updater_email, json[QString("lastUpdaterEmail")]);
    m_last_updater_email_isSet = !json[QString("lastUpdaterEmail")].isNull() && m_last_updater_email_isValid;

    m_last_updater_full_name_isValid = ::OpenAPI::fromJsonValue(m_last_updater_full_name, json[QString("lastUpdaterFullName")]);
    m_last_updater_full_name_isSet = !json[QString("lastUpdaterFullName")].isNull() && m_last_updater_full_name_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_segment_id_isValid = ::OpenAPI::fromJsonValue(m_segment_id, json[QString("segmentId")]);
    m_segment_id_isSet = !json[QString("segmentId")].isNull() && m_segment_id_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;
}

QString OAISegmentModel_haljson::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISegmentModel_haljson::asJsonObject() const {
    QJsonObject obj;
    if (m__embedded.isSet()) {
        obj.insert(QString("_embedded"), ::OpenAPI::toJsonValue(m__embedded));
    }
    if (m__links.isSet()) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_comparator.isSet()) {
        obj.insert(QString("comparator"), ::OpenAPI::toJsonValue(m_comparator));
    }
    if (m_comparison_attribute_isSet) {
        obj.insert(QString("comparisonAttribute"), ::OpenAPI::toJsonValue(m_comparison_attribute));
    }
    if (m_comparison_value_isSet) {
        obj.insert(QString("comparisonValue"), ::OpenAPI::toJsonValue(m_comparison_value));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_creator_email_isSet) {
        obj.insert(QString("creatorEmail"), ::OpenAPI::toJsonValue(m_creator_email));
    }
    if (m_creator_full_name_isSet) {
        obj.insert(QString("creatorFullName"), ::OpenAPI::toJsonValue(m_creator_full_name));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_last_updater_email_isSet) {
        obj.insert(QString("lastUpdaterEmail"), ::OpenAPI::toJsonValue(m_last_updater_email));
    }
    if (m_last_updater_full_name_isSet) {
        obj.insert(QString("lastUpdaterFullName"), ::OpenAPI::toJsonValue(m_last_updater_full_name));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_segment_id_isSet) {
        obj.insert(QString("segmentId"), ::OpenAPI::toJsonValue(m_segment_id));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

OAIConfigModel_haljson__embedded OAISegmentModel_haljson::getEmbedded() const {
    return m__embedded;
}
void OAISegmentModel_haljson::setEmbedded(const OAIConfigModel_haljson__embedded &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAISegmentModel_haljson::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAISegmentModel_haljson::is__embedded_Valid() const{
    return m__embedded_isValid;
}

OAIEnvironmentModel_haljson__links OAISegmentModel_haljson::getLinks() const {
    return m__links;
}
void OAISegmentModel_haljson::setLinks(const OAIEnvironmentModel_haljson__links &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAISegmentModel_haljson::is__links_Set() const{
    return m__links_isSet;
}

bool OAISegmentModel_haljson::is__links_Valid() const{
    return m__links_isValid;
}

OAIRolloutRuleComparator OAISegmentModel_haljson::getComparator() const {
    return m_comparator;
}
void OAISegmentModel_haljson::setComparator(const OAIRolloutRuleComparator &comparator) {
    m_comparator = comparator;
    m_comparator_isSet = true;
}

bool OAISegmentModel_haljson::is_comparator_Set() const{
    return m_comparator_isSet;
}

bool OAISegmentModel_haljson::is_comparator_Valid() const{
    return m_comparator_isValid;
}

QString OAISegmentModel_haljson::getComparisonAttribute() const {
    return m_comparison_attribute;
}
void OAISegmentModel_haljson::setComparisonAttribute(const QString &comparison_attribute) {
    m_comparison_attribute = comparison_attribute;
    m_comparison_attribute_isSet = true;
}

bool OAISegmentModel_haljson::is_comparison_attribute_Set() const{
    return m_comparison_attribute_isSet;
}

bool OAISegmentModel_haljson::is_comparison_attribute_Valid() const{
    return m_comparison_attribute_isValid;
}

QString OAISegmentModel_haljson::getComparisonValue() const {
    return m_comparison_value;
}
void OAISegmentModel_haljson::setComparisonValue(const QString &comparison_value) {
    m_comparison_value = comparison_value;
    m_comparison_value_isSet = true;
}

bool OAISegmentModel_haljson::is_comparison_value_Set() const{
    return m_comparison_value_isSet;
}

bool OAISegmentModel_haljson::is_comparison_value_Valid() const{
    return m_comparison_value_isValid;
}

QDateTime OAISegmentModel_haljson::getCreatedAt() const {
    return m_created_at;
}
void OAISegmentModel_haljson::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAISegmentModel_haljson::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAISegmentModel_haljson::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAISegmentModel_haljson::getCreatorEmail() const {
    return m_creator_email;
}
void OAISegmentModel_haljson::setCreatorEmail(const QString &creator_email) {
    m_creator_email = creator_email;
    m_creator_email_isSet = true;
}

bool OAISegmentModel_haljson::is_creator_email_Set() const{
    return m_creator_email_isSet;
}

bool OAISegmentModel_haljson::is_creator_email_Valid() const{
    return m_creator_email_isValid;
}

QString OAISegmentModel_haljson::getCreatorFullName() const {
    return m_creator_full_name;
}
void OAISegmentModel_haljson::setCreatorFullName(const QString &creator_full_name) {
    m_creator_full_name = creator_full_name;
    m_creator_full_name_isSet = true;
}

bool OAISegmentModel_haljson::is_creator_full_name_Set() const{
    return m_creator_full_name_isSet;
}

bool OAISegmentModel_haljson::is_creator_full_name_Valid() const{
    return m_creator_full_name_isValid;
}

QString OAISegmentModel_haljson::getDescription() const {
    return m_description;
}
void OAISegmentModel_haljson::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAISegmentModel_haljson::is_description_Set() const{
    return m_description_isSet;
}

bool OAISegmentModel_haljson::is_description_Valid() const{
    return m_description_isValid;
}

QString OAISegmentModel_haljson::getLastUpdaterEmail() const {
    return m_last_updater_email;
}
void OAISegmentModel_haljson::setLastUpdaterEmail(const QString &last_updater_email) {
    m_last_updater_email = last_updater_email;
    m_last_updater_email_isSet = true;
}

bool OAISegmentModel_haljson::is_last_updater_email_Set() const{
    return m_last_updater_email_isSet;
}

bool OAISegmentModel_haljson::is_last_updater_email_Valid() const{
    return m_last_updater_email_isValid;
}

QString OAISegmentModel_haljson::getLastUpdaterFullName() const {
    return m_last_updater_full_name;
}
void OAISegmentModel_haljson::setLastUpdaterFullName(const QString &last_updater_full_name) {
    m_last_updater_full_name = last_updater_full_name;
    m_last_updater_full_name_isSet = true;
}

bool OAISegmentModel_haljson::is_last_updater_full_name_Set() const{
    return m_last_updater_full_name_isSet;
}

bool OAISegmentModel_haljson::is_last_updater_full_name_Valid() const{
    return m_last_updater_full_name_isValid;
}

QString OAISegmentModel_haljson::getName() const {
    return m_name;
}
void OAISegmentModel_haljson::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISegmentModel_haljson::is_name_Set() const{
    return m_name_isSet;
}

bool OAISegmentModel_haljson::is_name_Valid() const{
    return m_name_isValid;
}

QString OAISegmentModel_haljson::getSegmentId() const {
    return m_segment_id;
}
void OAISegmentModel_haljson::setSegmentId(const QString &segment_id) {
    m_segment_id = segment_id;
    m_segment_id_isSet = true;
}

bool OAISegmentModel_haljson::is_segment_id_Set() const{
    return m_segment_id_isSet;
}

bool OAISegmentModel_haljson::is_segment_id_Valid() const{
    return m_segment_id_isValid;
}

QDateTime OAISegmentModel_haljson::getUpdatedAt() const {
    return m_updated_at;
}
void OAISegmentModel_haljson::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAISegmentModel_haljson::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAISegmentModel_haljson::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAISegmentModel_haljson::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__embedded.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m__links.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_comparator.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_comparison_attribute_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comparison_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creator_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creator_full_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_updater_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_updater_full_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_segment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISegmentModel_haljson::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
