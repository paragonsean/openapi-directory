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

#include "OAICreateSettingInitialValues.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateSettingInitialValues::OAICreateSettingInitialValues(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateSettingInitialValues::OAICreateSettingInitialValues() {
    this->initializeModel();
}

OAICreateSettingInitialValues::~OAICreateSettingInitialValues() {}

void OAICreateSettingInitialValues::initializeModel() {

    m_hint_isSet = false;
    m_hint_isValid = false;

    m_initial_values_isSet = false;
    m_initial_values_isValid = false;

    m_key_isSet = false;
    m_key_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_setting_type_isSet = false;
    m_setting_type_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAICreateSettingInitialValues::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateSettingInitialValues::fromJsonObject(QJsonObject json) {

    m_hint_isValid = ::OpenAPI::fromJsonValue(m_hint, json[QString("hint")]);
    m_hint_isSet = !json[QString("hint")].isNull() && m_hint_isValid;

    m_initial_values_isValid = ::OpenAPI::fromJsonValue(m_initial_values, json[QString("initialValues")]);
    m_initial_values_isSet = !json[QString("initialValues")].isNull() && m_initial_values_isValid;

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("key")]);
    m_key_isSet = !json[QString("key")].isNull() && m_key_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_setting_type_isValid = ::OpenAPI::fromJsonValue(m_setting_type, json[QString("settingType")]);
    m_setting_type_isSet = !json[QString("settingType")].isNull() && m_setting_type_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;
}

QString OAICreateSettingInitialValues::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateSettingInitialValues::asJsonObject() const {
    QJsonObject obj;
    if (m_hint_isSet) {
        obj.insert(QString("hint"), ::OpenAPI::toJsonValue(m_hint));
    }
    if (m_initial_values.size() > 0) {
        obj.insert(QString("initialValues"), ::OpenAPI::toJsonValue(m_initial_values));
    }
    if (m_key_isSet) {
        obj.insert(QString("key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_setting_type.isSet()) {
        obj.insert(QString("settingType"), ::OpenAPI::toJsonValue(m_setting_type));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

QString OAICreateSettingInitialValues::getHint() const {
    return m_hint;
}
void OAICreateSettingInitialValues::setHint(const QString &hint) {
    m_hint = hint;
    m_hint_isSet = true;
}

bool OAICreateSettingInitialValues::is_hint_Set() const{
    return m_hint_isSet;
}

bool OAICreateSettingInitialValues::is_hint_Valid() const{
    return m_hint_isValid;
}

QList<OAIInitialValue> OAICreateSettingInitialValues::getInitialValues() const {
    return m_initial_values;
}
void OAICreateSettingInitialValues::setInitialValues(const QList<OAIInitialValue> &initial_values) {
    m_initial_values = initial_values;
    m_initial_values_isSet = true;
}

bool OAICreateSettingInitialValues::is_initial_values_Set() const{
    return m_initial_values_isSet;
}

bool OAICreateSettingInitialValues::is_initial_values_Valid() const{
    return m_initial_values_isValid;
}

QString OAICreateSettingInitialValues::getKey() const {
    return m_key;
}
void OAICreateSettingInitialValues::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAICreateSettingInitialValues::is_key_Set() const{
    return m_key_isSet;
}

bool OAICreateSettingInitialValues::is_key_Valid() const{
    return m_key_isValid;
}

QString OAICreateSettingInitialValues::getName() const {
    return m_name;
}
void OAICreateSettingInitialValues::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateSettingInitialValues::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateSettingInitialValues::is_name_Valid() const{
    return m_name_isValid;
}

OAISettingType OAICreateSettingInitialValues::getSettingType() const {
    return m_setting_type;
}
void OAICreateSettingInitialValues::setSettingType(const OAISettingType &setting_type) {
    m_setting_type = setting_type;
    m_setting_type_isSet = true;
}

bool OAICreateSettingInitialValues::is_setting_type_Set() const{
    return m_setting_type_isSet;
}

bool OAICreateSettingInitialValues::is_setting_type_Valid() const{
    return m_setting_type_isValid;
}

QList<qint64> OAICreateSettingInitialValues::getTags() const {
    return m_tags;
}
void OAICreateSettingInitialValues::setTags(const QList<qint64> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAICreateSettingInitialValues::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAICreateSettingInitialValues::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAICreateSettingInitialValues::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_hint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_initial_values.size() > 0) {
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

        if (m_setting_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateSettingInitialValues::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_key_isValid && m_name_isValid && m_setting_type_isValid && true;
}

} // namespace OpenAPI
