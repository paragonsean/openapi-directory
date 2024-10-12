/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRedisAccessKeys.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRedisAccessKeys::OAIRedisAccessKeys(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRedisAccessKeys::OAIRedisAccessKeys() {
    this->initializeModel();
}

OAIRedisAccessKeys::~OAIRedisAccessKeys() {}

void OAIRedisAccessKeys::initializeModel() {

    m_primary_key_isSet = false;
    m_primary_key_isValid = false;

    m_secondary_key_isSet = false;
    m_secondary_key_isValid = false;
}

void OAIRedisAccessKeys::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRedisAccessKeys::fromJsonObject(QJsonObject json) {

    m_primary_key_isValid = ::OpenAPI::fromJsonValue(m_primary_key, json[QString("primaryKey")]);
    m_primary_key_isSet = !json[QString("primaryKey")].isNull() && m_primary_key_isValid;

    m_secondary_key_isValid = ::OpenAPI::fromJsonValue(m_secondary_key, json[QString("secondaryKey")]);
    m_secondary_key_isSet = !json[QString("secondaryKey")].isNull() && m_secondary_key_isValid;
}

QString OAIRedisAccessKeys::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRedisAccessKeys::asJsonObject() const {
    QJsonObject obj;
    if (m_primary_key_isSet) {
        obj.insert(QString("primaryKey"), ::OpenAPI::toJsonValue(m_primary_key));
    }
    if (m_secondary_key_isSet) {
        obj.insert(QString("secondaryKey"), ::OpenAPI::toJsonValue(m_secondary_key));
    }
    return obj;
}

QString OAIRedisAccessKeys::getPrimaryKey() const {
    return m_primary_key;
}
void OAIRedisAccessKeys::setPrimaryKey(const QString &primary_key) {
    m_primary_key = primary_key;
    m_primary_key_isSet = true;
}

bool OAIRedisAccessKeys::is_primary_key_Set() const{
    return m_primary_key_isSet;
}

bool OAIRedisAccessKeys::is_primary_key_Valid() const{
    return m_primary_key_isValid;
}

QString OAIRedisAccessKeys::getSecondaryKey() const {
    return m_secondary_key;
}
void OAIRedisAccessKeys::setSecondaryKey(const QString &secondary_key) {
    m_secondary_key = secondary_key;
    m_secondary_key_isSet = true;
}

bool OAIRedisAccessKeys::is_secondary_key_Set() const{
    return m_secondary_key_isSet;
}

bool OAIRedisAccessKeys::is_secondary_key_Valid() const{
    return m_secondary_key_isValid;
}

bool OAIRedisAccessKeys::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_primary_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secondary_key_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRedisAccessKeys::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
