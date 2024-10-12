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

#include "OAISettingModel_haljson.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISettingModel_haljson::OAISettingModel_haljson(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISettingModel_haljson::OAISettingModel_haljson() {
    this->initializeModel();
}

OAISettingModel_haljson::~OAISettingModel_haljson() {}

void OAISettingModel_haljson::initializeModel() {

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_config_id_isSet = false;
    m_config_id_isValid = false;

    m_config_name_isSet = false;
    m_config_name_isValid = false;

    m_hint_isSet = false;
    m_hint_isValid = false;

    m_key_isSet = false;
    m_key_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_order_isSet = false;
    m_order_isValid = false;

    m_setting_id_isSet = false;
    m_setting_id_isValid = false;

    m_setting_type_isSet = false;
    m_setting_type_isValid = false;
}

void OAISettingModel_haljson::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISettingModel_haljson::fromJsonObject(QJsonObject json) {

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_config_id_isValid = ::OpenAPI::fromJsonValue(m_config_id, json[QString("configId")]);
    m_config_id_isSet = !json[QString("configId")].isNull() && m_config_id_isValid;

    m_config_name_isValid = ::OpenAPI::fromJsonValue(m_config_name, json[QString("configName")]);
    m_config_name_isSet = !json[QString("configName")].isNull() && m_config_name_isValid;

    m_hint_isValid = ::OpenAPI::fromJsonValue(m_hint, json[QString("hint")]);
    m_hint_isSet = !json[QString("hint")].isNull() && m_hint_isValid;

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("key")]);
    m_key_isSet = !json[QString("key")].isNull() && m_key_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_order_isValid = ::OpenAPI::fromJsonValue(m_order, json[QString("order")]);
    m_order_isSet = !json[QString("order")].isNull() && m_order_isValid;

    m_setting_id_isValid = ::OpenAPI::fromJsonValue(m_setting_id, json[QString("settingId")]);
    m_setting_id_isSet = !json[QString("settingId")].isNull() && m_setting_id_isValid;

    m_setting_type_isValid = ::OpenAPI::fromJsonValue(m_setting_type, json[QString("settingType")]);
    m_setting_type_isSet = !json[QString("settingType")].isNull() && m_setting_type_isValid;
}

QString OAISettingModel_haljson::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISettingModel_haljson::asJsonObject() const {
    QJsonObject obj;
    if (m__embedded.isSet()) {
        obj.insert(QString("_embedded"), ::OpenAPI::toJsonValue(m__embedded));
    }
    if (m__links.isSet()) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_config_id_isSet) {
        obj.insert(QString("configId"), ::OpenAPI::toJsonValue(m_config_id));
    }
    if (m_config_name_isSet) {
        obj.insert(QString("configName"), ::OpenAPI::toJsonValue(m_config_name));
    }
    if (m_hint_isSet) {
        obj.insert(QString("hint"), ::OpenAPI::toJsonValue(m_hint));
    }
    if (m_key_isSet) {
        obj.insert(QString("key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_order_isSet) {
        obj.insert(QString("order"), ::OpenAPI::toJsonValue(m_order));
    }
    if (m_setting_id_isSet) {
        obj.insert(QString("settingId"), ::OpenAPI::toJsonValue(m_setting_id));
    }
    if (m_setting_type.isSet()) {
        obj.insert(QString("settingType"), ::OpenAPI::toJsonValue(m_setting_type));
    }
    return obj;
}

OAISettingModel_haljson__embedded OAISettingModel_haljson::getEmbedded() const {
    return m__embedded;
}
void OAISettingModel_haljson::setEmbedded(const OAISettingModel_haljson__embedded &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAISettingModel_haljson::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAISettingModel_haljson::is__embedded_Valid() const{
    return m__embedded_isValid;
}

OAIEnvironmentModel_haljson__links OAISettingModel_haljson::getLinks() const {
    return m__links;
}
void OAISettingModel_haljson::setLinks(const OAIEnvironmentModel_haljson__links &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAISettingModel_haljson::is__links_Set() const{
    return m__links_isSet;
}

bool OAISettingModel_haljson::is__links_Valid() const{
    return m__links_isValid;
}

QString OAISettingModel_haljson::getConfigId() const {
    return m_config_id;
}
void OAISettingModel_haljson::setConfigId(const QString &config_id) {
    m_config_id = config_id;
    m_config_id_isSet = true;
}

bool OAISettingModel_haljson::is_config_id_Set() const{
    return m_config_id_isSet;
}

bool OAISettingModel_haljson::is_config_id_Valid() const{
    return m_config_id_isValid;
}

QString OAISettingModel_haljson::getConfigName() const {
    return m_config_name;
}
void OAISettingModel_haljson::setConfigName(const QString &config_name) {
    m_config_name = config_name;
    m_config_name_isSet = true;
}

bool OAISettingModel_haljson::is_config_name_Set() const{
    return m_config_name_isSet;
}

bool OAISettingModel_haljson::is_config_name_Valid() const{
    return m_config_name_isValid;
}

QString OAISettingModel_haljson::getHint() const {
    return m_hint;
}
void OAISettingModel_haljson::setHint(const QString &hint) {
    m_hint = hint;
    m_hint_isSet = true;
}

bool OAISettingModel_haljson::is_hint_Set() const{
    return m_hint_isSet;
}

bool OAISettingModel_haljson::is_hint_Valid() const{
    return m_hint_isValid;
}

QString OAISettingModel_haljson::getKey() const {
    return m_key;
}
void OAISettingModel_haljson::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAISettingModel_haljson::is_key_Set() const{
    return m_key_isSet;
}

bool OAISettingModel_haljson::is_key_Valid() const{
    return m_key_isValid;
}

QString OAISettingModel_haljson::getName() const {
    return m_name;
}
void OAISettingModel_haljson::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISettingModel_haljson::is_name_Set() const{
    return m_name_isSet;
}

bool OAISettingModel_haljson::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAISettingModel_haljson::getOrder() const {
    return m_order;
}
void OAISettingModel_haljson::setOrder(const qint32 &order) {
    m_order = order;
    m_order_isSet = true;
}

bool OAISettingModel_haljson::is_order_Set() const{
    return m_order_isSet;
}

bool OAISettingModel_haljson::is_order_Valid() const{
    return m_order_isValid;
}

qint32 OAISettingModel_haljson::getSettingId() const {
    return m_setting_id;
}
void OAISettingModel_haljson::setSettingId(const qint32 &setting_id) {
    m_setting_id = setting_id;
    m_setting_id_isSet = true;
}

bool OAISettingModel_haljson::is_setting_id_Set() const{
    return m_setting_id_isSet;
}

bool OAISettingModel_haljson::is_setting_id_Valid() const{
    return m_setting_id_isValid;
}

OAISettingType OAISettingModel_haljson::getSettingType() const {
    return m_setting_type;
}
void OAISettingModel_haljson::setSettingType(const OAISettingType &setting_type) {
    m_setting_type = setting_type;
    m_setting_type_isSet = true;
}

bool OAISettingModel_haljson::is_setting_type_Set() const{
    return m_setting_type_isSet;
}

bool OAISettingModel_haljson::is_setting_type_Valid() const{
    return m_setting_type_isValid;
}

bool OAISettingModel_haljson::isSet() const {
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

        if (m_config_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_config_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_isSet) {
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

        if (m_setting_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_setting_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISettingModel_haljson::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
