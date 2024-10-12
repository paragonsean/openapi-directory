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

#include "OAITagModel_haljson.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITagModel_haljson::OAITagModel_haljson(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITagModel_haljson::OAITagModel_haljson() {
    this->initializeModel();
}

OAITagModel_haljson::~OAITagModel_haljson() {}

void OAITagModel_haljson::initializeModel() {

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_color_isSet = false;
    m_color_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_tag_id_isSet = false;
    m_tag_id_isValid = false;
}

void OAITagModel_haljson::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITagModel_haljson::fromJsonObject(QJsonObject json) {

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_color_isValid = ::OpenAPI::fromJsonValue(m_color, json[QString("color")]);
    m_color_isSet = !json[QString("color")].isNull() && m_color_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_tag_id_isValid = ::OpenAPI::fromJsonValue(m_tag_id, json[QString("tagId")]);
    m_tag_id_isSet = !json[QString("tagId")].isNull() && m_tag_id_isValid;
}

QString OAITagModel_haljson::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITagModel_haljson::asJsonObject() const {
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
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_tag_id_isSet) {
        obj.insert(QString("tagId"), ::OpenAPI::toJsonValue(m_tag_id));
    }
    return obj;
}

OAIConfigModel_haljson__embedded OAITagModel_haljson::getEmbedded() const {
    return m__embedded;
}
void OAITagModel_haljson::setEmbedded(const OAIConfigModel_haljson__embedded &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAITagModel_haljson::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAITagModel_haljson::is__embedded_Valid() const{
    return m__embedded_isValid;
}

OAIEnvironmentModel_haljson__links OAITagModel_haljson::getLinks() const {
    return m__links;
}
void OAITagModel_haljson::setLinks(const OAIEnvironmentModel_haljson__links &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAITagModel_haljson::is__links_Set() const{
    return m__links_isSet;
}

bool OAITagModel_haljson::is__links_Valid() const{
    return m__links_isValid;
}

QString OAITagModel_haljson::getColor() const {
    return m_color;
}
void OAITagModel_haljson::setColor(const QString &color) {
    m_color = color;
    m_color_isSet = true;
}

bool OAITagModel_haljson::is_color_Set() const{
    return m_color_isSet;
}

bool OAITagModel_haljson::is_color_Valid() const{
    return m_color_isValid;
}

QString OAITagModel_haljson::getName() const {
    return m_name;
}
void OAITagModel_haljson::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITagModel_haljson::is_name_Set() const{
    return m_name_isSet;
}

bool OAITagModel_haljson::is_name_Valid() const{
    return m_name_isValid;
}

qint64 OAITagModel_haljson::getTagId() const {
    return m_tag_id;
}
void OAITagModel_haljson::setTagId(const qint64 &tag_id) {
    m_tag_id = tag_id;
    m_tag_id_isSet = true;
}

bool OAITagModel_haljson::is_tag_id_Set() const{
    return m_tag_id_isSet;
}

bool OAITagModel_haljson::is_tag_id_Valid() const{
    return m_tag_id_isValid;
}

bool OAITagModel_haljson::isSet() const {
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

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITagModel_haljson::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
