/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGroup_throttle.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGroup_throttle::OAIGroup_throttle(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGroup_throttle::OAIGroup_throttle() {
    this->initializeModel();
}

OAIGroup_throttle::~OAIGroup_throttle() {}

void OAIGroup_throttle::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_mode_isSet = false;
    m_mode_isValid = false;

    m_remaining_isSet = false;
    m_remaining_isValid = false;
}

void OAIGroup_throttle::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGroup_throttle::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_mode_isValid = ::OpenAPI::fromJsonValue(m_mode, json[QString("mode")]);
    m_mode_isSet = !json[QString("mode")].isNull() && m_mode_isValid;

    m_remaining_isValid = ::OpenAPI::fromJsonValue(m_remaining, json[QString("remaining")]);
    m_remaining_isSet = !json[QString("remaining")].isNull() && m_remaining_isValid;
}

QString OAIGroup_throttle::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGroup_throttle::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_mode_isSet) {
        obj.insert(QString("mode"), ::OpenAPI::toJsonValue(m_mode));
    }
    if (m_remaining_isSet) {
        obj.insert(QString("remaining"), ::OpenAPI::toJsonValue(m_remaining));
    }
    return obj;
}

qint32 OAIGroup_throttle::getCount() const {
    return m_count;
}
void OAIGroup_throttle::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIGroup_throttle::is_count_Set() const{
    return m_count_isSet;
}

bool OAIGroup_throttle::is_count_Valid() const{
    return m_count_isValid;
}

QString OAIGroup_throttle::getMode() const {
    return m_mode;
}
void OAIGroup_throttle::setMode(const QString &mode) {
    m_mode = mode;
    m_mode_isSet = true;
}

bool OAIGroup_throttle::is_mode_Set() const{
    return m_mode_isSet;
}

bool OAIGroup_throttle::is_mode_Valid() const{
    return m_mode_isValid;
}

QString OAIGroup_throttle::getRemaining() const {
    return m_remaining;
}
void OAIGroup_throttle::setRemaining(const QString &remaining) {
    m_remaining = remaining;
    m_remaining_isSet = true;
}

bool OAIGroup_throttle::is_remaining_Set() const{
    return m_remaining_isSet;
}

bool OAIGroup_throttle::is_remaining_Valid() const{
    return m_remaining_isValid;
}

bool OAIGroup_throttle::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_remaining_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGroup_throttle::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
