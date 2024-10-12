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

#include "OAISettingValueModel_haljson__embedded_environment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISettingValueModel_haljson__embedded_environment::OAISettingValueModel_haljson__embedded_environment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISettingValueModel_haljson__embedded_environment::OAISettingValueModel_haljson__embedded_environment() {
    this->initializeModel();
}

OAISettingValueModel_haljson__embedded_environment::~OAISettingValueModel_haljson__embedded_environment() {}

void OAISettingValueModel_haljson__embedded_environment::initializeModel() {

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_color_isSet = false;
    m_color_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_environment_id_isSet = false;
    m_environment_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_order_isSet = false;
    m_order_isValid = false;

    m_reason_required_isSet = false;
    m_reason_required_isValid = false;
}

void OAISettingValueModel_haljson__embedded_environment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISettingValueModel_haljson__embedded_environment::fromJsonObject(QJsonObject json) {

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_color_isValid = ::OpenAPI::fromJsonValue(m_color, json[QString("color")]);
    m_color_isSet = !json[QString("color")].isNull() && m_color_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_environment_id_isValid = ::OpenAPI::fromJsonValue(m_environment_id, json[QString("environmentId")]);
    m_environment_id_isSet = !json[QString("environmentId")].isNull() && m_environment_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_order_isValid = ::OpenAPI::fromJsonValue(m_order, json[QString("order")]);
    m_order_isSet = !json[QString("order")].isNull() && m_order_isValid;

    m_reason_required_isValid = ::OpenAPI::fromJsonValue(m_reason_required, json[QString("reasonRequired")]);
    m_reason_required_isSet = !json[QString("reasonRequired")].isNull() && m_reason_required_isValid;
}

QString OAISettingValueModel_haljson__embedded_environment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISettingValueModel_haljson__embedded_environment::asJsonObject() const {
    QJsonObject obj;
    if (m__embedded.isSet()) {
        obj.insert(QString("_embedded"), ::OpenAPI::toJsonValue(m__embedded));
    }
    if (m__links.isSet()) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_color_isSet) {
        obj.insert(QString("color"), ::OpenAPI::toJsonValue(m_color));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_environment_id_isSet) {
        obj.insert(QString("environmentId"), ::OpenAPI::toJsonValue(m_environment_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_order_isSet) {
        obj.insert(QString("order"), ::OpenAPI::toJsonValue(m_order));
    }
    if (m_reason_required_isSet) {
        obj.insert(QString("reasonRequired"), ::OpenAPI::toJsonValue(m_reason_required));
    }
    return obj;
}

OAIConfigModel_haljson__embedded OAISettingValueModel_haljson__embedded_environment::getEmbedded() const {
    return m__embedded;
}
void OAISettingValueModel_haljson__embedded_environment::setEmbedded(const OAIConfigModel_haljson__embedded &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAISettingValueModel_haljson__embedded_environment::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAISettingValueModel_haljson__embedded_environment::is__embedded_Valid() const{
    return m__embedded_isValid;
}

OAIEnvironmentModel_haljson__links OAISettingValueModel_haljson__embedded_environment::getLinks() const {
    return m__links;
}
void OAISettingValueModel_haljson__embedded_environment::setLinks(const OAIEnvironmentModel_haljson__links &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAISettingValueModel_haljson__embedded_environment::is__links_Set() const{
    return m__links_isSet;
}

bool OAISettingValueModel_haljson__embedded_environment::is__links_Valid() const{
    return m__links_isValid;
}

QString OAISettingValueModel_haljson__embedded_environment::getColor() const {
    return m_color;
}
void OAISettingValueModel_haljson__embedded_environment::setColor(const QString &color) {
    m_color = color;
    m_color_isSet = true;
}

bool OAISettingValueModel_haljson__embedded_environment::is_color_Set() const{
    return m_color_isSet;
}

bool OAISettingValueModel_haljson__embedded_environment::is_color_Valid() const{
    return m_color_isValid;
}

QString OAISettingValueModel_haljson__embedded_environment::getDescription() const {
    return m_description;
}
void OAISettingValueModel_haljson__embedded_environment::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAISettingValueModel_haljson__embedded_environment::is_description_Set() const{
    return m_description_isSet;
}

bool OAISettingValueModel_haljson__embedded_environment::is_description_Valid() const{
    return m_description_isValid;
}

QString OAISettingValueModel_haljson__embedded_environment::getEnvironmentId() const {
    return m_environment_id;
}
void OAISettingValueModel_haljson__embedded_environment::setEnvironmentId(const QString &environment_id) {
    m_environment_id = environment_id;
    m_environment_id_isSet = true;
}

bool OAISettingValueModel_haljson__embedded_environment::is_environment_id_Set() const{
    return m_environment_id_isSet;
}

bool OAISettingValueModel_haljson__embedded_environment::is_environment_id_Valid() const{
    return m_environment_id_isValid;
}

QString OAISettingValueModel_haljson__embedded_environment::getName() const {
    return m_name;
}
void OAISettingValueModel_haljson__embedded_environment::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISettingValueModel_haljson__embedded_environment::is_name_Set() const{
    return m_name_isSet;
}

bool OAISettingValueModel_haljson__embedded_environment::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAISettingValueModel_haljson__embedded_environment::getOrder() const {
    return m_order;
}
void OAISettingValueModel_haljson__embedded_environment::setOrder(const qint32 &order) {
    m_order = order;
    m_order_isSet = true;
}

bool OAISettingValueModel_haljson__embedded_environment::is_order_Set() const{
    return m_order_isSet;
}

bool OAISettingValueModel_haljson__embedded_environment::is_order_Valid() const{
    return m_order_isValid;
}

bool OAISettingValueModel_haljson__embedded_environment::isReasonRequired() const {
    return m_reason_required;
}
void OAISettingValueModel_haljson__embedded_environment::setReasonRequired(const bool &reason_required) {
    m_reason_required = reason_required;
    m_reason_required_isSet = true;
}

bool OAISettingValueModel_haljson__embedded_environment::is_reason_required_Set() const{
    return m_reason_required_isSet;
}

bool OAISettingValueModel_haljson__embedded_environment::is_reason_required_Valid() const{
    return m_reason_required_isValid;
}

bool OAISettingValueModel_haljson__embedded_environment::isSet() const {
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

        if (m_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_environment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_required_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISettingValueModel_haljson__embedded_environment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
