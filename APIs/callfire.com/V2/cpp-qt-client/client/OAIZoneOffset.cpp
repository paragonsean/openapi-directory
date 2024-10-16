/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIZoneOffset.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIZoneOffset::OAIZoneOffset(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIZoneOffset::OAIZoneOffset() {
    this->initializeModel();
}

OAIZoneOffset::~OAIZoneOffset() {}

void OAIZoneOffset::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_rules_isSet = false;
    m_rules_isValid = false;

    m_total_seconds_isSet = false;
    m_total_seconds_isValid = false;
}

void OAIZoneOffset::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIZoneOffset::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_rules_isValid = ::OpenAPI::fromJsonValue(m_rules, json[QString("rules")]);
    m_rules_isSet = !json[QString("rules")].isNull() && m_rules_isValid;

    m_total_seconds_isValid = ::OpenAPI::fromJsonValue(m_total_seconds, json[QString("totalSeconds")]);
    m_total_seconds_isSet = !json[QString("totalSeconds")].isNull() && m_total_seconds_isValid;
}

QString OAIZoneOffset::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIZoneOffset::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_rules.isSet()) {
        obj.insert(QString("rules"), ::OpenAPI::toJsonValue(m_rules));
    }
    if (m_total_seconds_isSet) {
        obj.insert(QString("totalSeconds"), ::OpenAPI::toJsonValue(m_total_seconds));
    }
    return obj;
}

QString OAIZoneOffset::getId() const {
    return m_id;
}
void OAIZoneOffset::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIZoneOffset::is_id_Set() const{
    return m_id_isSet;
}

bool OAIZoneOffset::is_id_Valid() const{
    return m_id_isValid;
}

OAIZoneRules OAIZoneOffset::getRules() const {
    return m_rules;
}
void OAIZoneOffset::setRules(const OAIZoneRules &rules) {
    m_rules = rules;
    m_rules_isSet = true;
}

bool OAIZoneOffset::is_rules_Set() const{
    return m_rules_isSet;
}

bool OAIZoneOffset::is_rules_Valid() const{
    return m_rules_isValid;
}

qint32 OAIZoneOffset::getTotalSeconds() const {
    return m_total_seconds;
}
void OAIZoneOffset::setTotalSeconds(const qint32 &total_seconds) {
    m_total_seconds = total_seconds;
    m_total_seconds_isSet = true;
}

bool OAIZoneOffset::is_total_seconds_Set() const{
    return m_total_seconds_isSet;
}

bool OAIZoneOffset::is_total_seconds_Valid() const{
    return m_total_seconds_isValid;
}

bool OAIZoneOffset::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rules.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_seconds_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIZoneOffset::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
