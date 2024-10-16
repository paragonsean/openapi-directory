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

#include "OAILocalTime.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILocalTime::OAILocalTime(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILocalTime::OAILocalTime() {
    this->initializeModel();
}

OAILocalTime::~OAILocalTime() {}

void OAILocalTime::initializeModel() {

    m_hour_isSet = false;
    m_hour_isValid = false;

    m_minute_isSet = false;
    m_minute_isValid = false;

    m_nano_isSet = false;
    m_nano_isValid = false;

    m_second_isSet = false;
    m_second_isValid = false;
}

void OAILocalTime::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILocalTime::fromJsonObject(QJsonObject json) {

    m_hour_isValid = ::OpenAPI::fromJsonValue(m_hour, json[QString("hour")]);
    m_hour_isSet = !json[QString("hour")].isNull() && m_hour_isValid;

    m_minute_isValid = ::OpenAPI::fromJsonValue(m_minute, json[QString("minute")]);
    m_minute_isSet = !json[QString("minute")].isNull() && m_minute_isValid;

    m_nano_isValid = ::OpenAPI::fromJsonValue(m_nano, json[QString("nano")]);
    m_nano_isSet = !json[QString("nano")].isNull() && m_nano_isValid;

    m_second_isValid = ::OpenAPI::fromJsonValue(m_second, json[QString("second")]);
    m_second_isSet = !json[QString("second")].isNull() && m_second_isValid;
}

QString OAILocalTime::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILocalTime::asJsonObject() const {
    QJsonObject obj;
    if (m_hour_isSet) {
        obj.insert(QString("hour"), ::OpenAPI::toJsonValue(m_hour));
    }
    if (m_minute_isSet) {
        obj.insert(QString("minute"), ::OpenAPI::toJsonValue(m_minute));
    }
    if (m_nano_isSet) {
        obj.insert(QString("nano"), ::OpenAPI::toJsonValue(m_nano));
    }
    if (m_second_isSet) {
        obj.insert(QString("second"), ::OpenAPI::toJsonValue(m_second));
    }
    return obj;
}

qint32 OAILocalTime::getHour() const {
    return m_hour;
}
void OAILocalTime::setHour(const qint32 &hour) {
    m_hour = hour;
    m_hour_isSet = true;
}

bool OAILocalTime::is_hour_Set() const{
    return m_hour_isSet;
}

bool OAILocalTime::is_hour_Valid() const{
    return m_hour_isValid;
}

qint32 OAILocalTime::getMinute() const {
    return m_minute;
}
void OAILocalTime::setMinute(const qint32 &minute) {
    m_minute = minute;
    m_minute_isSet = true;
}

bool OAILocalTime::is_minute_Set() const{
    return m_minute_isSet;
}

bool OAILocalTime::is_minute_Valid() const{
    return m_minute_isValid;
}

qint32 OAILocalTime::getNano() const {
    return m_nano;
}
void OAILocalTime::setNano(const qint32 &nano) {
    m_nano = nano;
    m_nano_isSet = true;
}

bool OAILocalTime::is_nano_Set() const{
    return m_nano_isSet;
}

bool OAILocalTime::is_nano_Valid() const{
    return m_nano_isValid;
}

qint32 OAILocalTime::getSecond() const {
    return m_second;
}
void OAILocalTime::setSecond(const qint32 &second) {
    m_second = second;
    m_second_isSet = true;
}

bool OAILocalTime::is_second_Set() const{
    return m_second_isSet;
}

bool OAILocalTime::is_second_Valid() const{
    return m_second_isValid;
}

bool OAILocalTime::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_hour_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minute_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nano_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_second_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILocalTime::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
