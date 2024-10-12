/**
 * MonitorManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRetentionPolicy.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRetentionPolicy::OAIRetentionPolicy(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRetentionPolicy::OAIRetentionPolicy() {
    this->initializeModel();
}

OAIRetentionPolicy::~OAIRetentionPolicy() {}

void OAIRetentionPolicy::initializeModel() {

    m_days_isSet = false;
    m_days_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;
}

void OAIRetentionPolicy::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRetentionPolicy::fromJsonObject(QJsonObject json) {

    m_days_isValid = ::OpenAPI::fromJsonValue(m_days, json[QString("days")]);
    m_days_isSet = !json[QString("days")].isNull() && m_days_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;
}

QString OAIRetentionPolicy::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRetentionPolicy::asJsonObject() const {
    QJsonObject obj;
    if (m_days_isSet) {
        obj.insert(QString("days"), ::OpenAPI::toJsonValue(m_days));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    return obj;
}

qint32 OAIRetentionPolicy::getDays() const {
    return m_days;
}
void OAIRetentionPolicy::setDays(const qint32 &days) {
    m_days = days;
    m_days_isSet = true;
}

bool OAIRetentionPolicy::is_days_Set() const{
    return m_days_isSet;
}

bool OAIRetentionPolicy::is_days_Valid() const{
    return m_days_isValid;
}

bool OAIRetentionPolicy::isEnabled() const {
    return m_enabled;
}
void OAIRetentionPolicy::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIRetentionPolicy::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIRetentionPolicy::is_enabled_Valid() const{
    return m_enabled_isValid;
}

bool OAIRetentionPolicy::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_days_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRetentionPolicy::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_days_isValid && m_enabled_isValid && true;
}

} // namespace OpenAPI
