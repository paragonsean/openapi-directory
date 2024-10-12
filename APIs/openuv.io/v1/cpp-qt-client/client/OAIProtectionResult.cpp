/**
 * OpenUV - Global Real-Time UV Index Forecast API
 * The missing minimalistic JSON real-time UV Index API for awesome Developers, Innovators and Smart Home Enthusiasts
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProtectionResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProtectionResult::OAIProtectionResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProtectionResult::OAIProtectionResult() {
    this->initializeModel();
}

OAIProtectionResult::~OAIProtectionResult() {}

void OAIProtectionResult::initializeModel() {

    m_ozone_isSet = false;
    m_ozone_isValid = false;

    m_ozone_time_isSet = false;
    m_ozone_time_isValid = false;

    m_uv_isSet = false;
    m_uv_isValid = false;

    m_uv_max_isSet = false;
    m_uv_max_isValid = false;

    m_uv_max_time_isSet = false;
    m_uv_max_time_isValid = false;

    m_uv_time_isSet = false;
    m_uv_time_isValid = false;
}

void OAIProtectionResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProtectionResult::fromJsonObject(QJsonObject json) {

    m_ozone_isValid = ::OpenAPI::fromJsonValue(m_ozone, json[QString("ozone")]);
    m_ozone_isSet = !json[QString("ozone")].isNull() && m_ozone_isValid;

    m_ozone_time_isValid = ::OpenAPI::fromJsonValue(m_ozone_time, json[QString("ozone_time")]);
    m_ozone_time_isSet = !json[QString("ozone_time")].isNull() && m_ozone_time_isValid;

    m_uv_isValid = ::OpenAPI::fromJsonValue(m_uv, json[QString("uv")]);
    m_uv_isSet = !json[QString("uv")].isNull() && m_uv_isValid;

    m_uv_max_isValid = ::OpenAPI::fromJsonValue(m_uv_max, json[QString("uv_max")]);
    m_uv_max_isSet = !json[QString("uv_max")].isNull() && m_uv_max_isValid;

    m_uv_max_time_isValid = ::OpenAPI::fromJsonValue(m_uv_max_time, json[QString("uv_max_time")]);
    m_uv_max_time_isSet = !json[QString("uv_max_time")].isNull() && m_uv_max_time_isValid;

    m_uv_time_isValid = ::OpenAPI::fromJsonValue(m_uv_time, json[QString("uv_time")]);
    m_uv_time_isSet = !json[QString("uv_time")].isNull() && m_uv_time_isValid;
}

QString OAIProtectionResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProtectionResult::asJsonObject() const {
    QJsonObject obj;
    if (m_ozone_isSet) {
        obj.insert(QString("ozone"), ::OpenAPI::toJsonValue(m_ozone));
    }
    if (m_ozone_time_isSet) {
        obj.insert(QString("ozone_time"), ::OpenAPI::toJsonValue(m_ozone_time));
    }
    if (m_uv_isSet) {
        obj.insert(QString("uv"), ::OpenAPI::toJsonValue(m_uv));
    }
    if (m_uv_max_isSet) {
        obj.insert(QString("uv_max"), ::OpenAPI::toJsonValue(m_uv_max));
    }
    if (m_uv_max_time_isSet) {
        obj.insert(QString("uv_max_time"), ::OpenAPI::toJsonValue(m_uv_max_time));
    }
    if (m_uv_time_isSet) {
        obj.insert(QString("uv_time"), ::OpenAPI::toJsonValue(m_uv_time));
    }
    return obj;
}

double OAIProtectionResult::getOzone() const {
    return m_ozone;
}
void OAIProtectionResult::setOzone(const double &ozone) {
    m_ozone = ozone;
    m_ozone_isSet = true;
}

bool OAIProtectionResult::is_ozone_Set() const{
    return m_ozone_isSet;
}

bool OAIProtectionResult::is_ozone_Valid() const{
    return m_ozone_isValid;
}

QString OAIProtectionResult::getOzoneTime() const {
    return m_ozone_time;
}
void OAIProtectionResult::setOzoneTime(const QString &ozone_time) {
    m_ozone_time = ozone_time;
    m_ozone_time_isSet = true;
}

bool OAIProtectionResult::is_ozone_time_Set() const{
    return m_ozone_time_isSet;
}

bool OAIProtectionResult::is_ozone_time_Valid() const{
    return m_ozone_time_isValid;
}

double OAIProtectionResult::getUv() const {
    return m_uv;
}
void OAIProtectionResult::setUv(const double &uv) {
    m_uv = uv;
    m_uv_isSet = true;
}

bool OAIProtectionResult::is_uv_Set() const{
    return m_uv_isSet;
}

bool OAIProtectionResult::is_uv_Valid() const{
    return m_uv_isValid;
}

double OAIProtectionResult::getUvMax() const {
    return m_uv_max;
}
void OAIProtectionResult::setUvMax(const double &uv_max) {
    m_uv_max = uv_max;
    m_uv_max_isSet = true;
}

bool OAIProtectionResult::is_uv_max_Set() const{
    return m_uv_max_isSet;
}

bool OAIProtectionResult::is_uv_max_Valid() const{
    return m_uv_max_isValid;
}

QString OAIProtectionResult::getUvMaxTime() const {
    return m_uv_max_time;
}
void OAIProtectionResult::setUvMaxTime(const QString &uv_max_time) {
    m_uv_max_time = uv_max_time;
    m_uv_max_time_isSet = true;
}

bool OAIProtectionResult::is_uv_max_time_Set() const{
    return m_uv_max_time_isSet;
}

bool OAIProtectionResult::is_uv_max_time_Valid() const{
    return m_uv_max_time_isValid;
}

QString OAIProtectionResult::getUvTime() const {
    return m_uv_time;
}
void OAIProtectionResult::setUvTime(const QString &uv_time) {
    m_uv_time = uv_time;
    m_uv_time_isSet = true;
}

bool OAIProtectionResult::is_uv_time_Set() const{
    return m_uv_time_isSet;
}

bool OAIProtectionResult::is_uv_time_Valid() const{
    return m_uv_time_isValid;
}

bool OAIProtectionResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ozone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ozone_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uv_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uv_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uv_max_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uv_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProtectionResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_ozone_isValid && m_ozone_time_isValid && m_uv_isValid && m_uv_max_isValid && m_uv_max_time_isValid && m_uv_time_isValid && true;
}

} // namespace OpenAPI
