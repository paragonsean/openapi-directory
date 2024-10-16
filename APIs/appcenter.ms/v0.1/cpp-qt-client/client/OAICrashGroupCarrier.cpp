/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICrashGroupCarrier.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICrashGroupCarrier::OAICrashGroupCarrier(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICrashGroupCarrier::OAICrashGroupCarrier() {
    this->initializeModel();
}

OAICrashGroupCarrier::~OAICrashGroupCarrier() {}

void OAICrashGroupCarrier::initializeModel() {

    m_carrier_name_isSet = false;
    m_carrier_name_isValid = false;

    m_crash_count_isSet = false;
    m_crash_count_isValid = false;
}

void OAICrashGroupCarrier::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICrashGroupCarrier::fromJsonObject(QJsonObject json) {

    m_carrier_name_isValid = ::OpenAPI::fromJsonValue(m_carrier_name, json[QString("carrier_name")]);
    m_carrier_name_isSet = !json[QString("carrier_name")].isNull() && m_carrier_name_isValid;

    m_crash_count_isValid = ::OpenAPI::fromJsonValue(m_crash_count, json[QString("crash_count")]);
    m_crash_count_isSet = !json[QString("crash_count")].isNull() && m_crash_count_isValid;
}

QString OAICrashGroupCarrier::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICrashGroupCarrier::asJsonObject() const {
    QJsonObject obj;
    if (m_carrier_name_isSet) {
        obj.insert(QString("carrier_name"), ::OpenAPI::toJsonValue(m_carrier_name));
    }
    if (m_crash_count_isSet) {
        obj.insert(QString("crash_count"), ::OpenAPI::toJsonValue(m_crash_count));
    }
    return obj;
}

QString OAICrashGroupCarrier::getCarrierName() const {
    return m_carrier_name;
}
void OAICrashGroupCarrier::setCarrierName(const QString &carrier_name) {
    m_carrier_name = carrier_name;
    m_carrier_name_isSet = true;
}

bool OAICrashGroupCarrier::is_carrier_name_Set() const{
    return m_carrier_name_isSet;
}

bool OAICrashGroupCarrier::is_carrier_name_Valid() const{
    return m_carrier_name_isValid;
}

qint64 OAICrashGroupCarrier::getCrashCount() const {
    return m_crash_count;
}
void OAICrashGroupCarrier::setCrashCount(const qint64 &crash_count) {
    m_crash_count = crash_count;
    m_crash_count_isSet = true;
}

bool OAICrashGroupCarrier::is_crash_count_Set() const{
    return m_crash_count_isSet;
}

bool OAICrashGroupCarrier::is_crash_count_Valid() const{
    return m_crash_count_isValid;
}

bool OAICrashGroupCarrier::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_carrier_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_crash_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICrashGroupCarrier::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
