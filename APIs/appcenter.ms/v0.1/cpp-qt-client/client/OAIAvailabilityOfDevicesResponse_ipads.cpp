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

#include "OAIAvailabilityOfDevicesResponse_ipads.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAvailabilityOfDevicesResponse_ipads::OAIAvailabilityOfDevicesResponse_ipads(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAvailabilityOfDevicesResponse_ipads::OAIAvailabilityOfDevicesResponse_ipads() {
    this->initializeModel();
}

OAIAvailabilityOfDevicesResponse_ipads::~OAIAvailabilityOfDevicesResponse_ipads() {}

void OAIAvailabilityOfDevicesResponse_ipads::initializeModel() {

    m_available_isSet = false;
    m_available_isValid = false;

    m_maximum_isSet = false;
    m_maximum_isValid = false;

    m_registered_isSet = false;
    m_registered_isValid = false;
}

void OAIAvailabilityOfDevicesResponse_ipads::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAvailabilityOfDevicesResponse_ipads::fromJsonObject(QJsonObject json) {

    m_available_isValid = ::OpenAPI::fromJsonValue(m_available, json[QString("available")]);
    m_available_isSet = !json[QString("available")].isNull() && m_available_isValid;

    m_maximum_isValid = ::OpenAPI::fromJsonValue(m_maximum, json[QString("maximum")]);
    m_maximum_isSet = !json[QString("maximum")].isNull() && m_maximum_isValid;

    m_registered_isValid = ::OpenAPI::fromJsonValue(m_registered, json[QString("registered")]);
    m_registered_isSet = !json[QString("registered")].isNull() && m_registered_isValid;
}

QString OAIAvailabilityOfDevicesResponse_ipads::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAvailabilityOfDevicesResponse_ipads::asJsonObject() const {
    QJsonObject obj;
    if (m_available_isSet) {
        obj.insert(QString("available"), ::OpenAPI::toJsonValue(m_available));
    }
    if (m_maximum_isSet) {
        obj.insert(QString("maximum"), ::OpenAPI::toJsonValue(m_maximum));
    }
    if (m_registered_isSet) {
        obj.insert(QString("registered"), ::OpenAPI::toJsonValue(m_registered));
    }
    return obj;
}

double OAIAvailabilityOfDevicesResponse_ipads::getAvailable() const {
    return m_available;
}
void OAIAvailabilityOfDevicesResponse_ipads::setAvailable(const double &available) {
    m_available = available;
    m_available_isSet = true;
}

bool OAIAvailabilityOfDevicesResponse_ipads::is_available_Set() const{
    return m_available_isSet;
}

bool OAIAvailabilityOfDevicesResponse_ipads::is_available_Valid() const{
    return m_available_isValid;
}

double OAIAvailabilityOfDevicesResponse_ipads::getMaximum() const {
    return m_maximum;
}
void OAIAvailabilityOfDevicesResponse_ipads::setMaximum(const double &maximum) {
    m_maximum = maximum;
    m_maximum_isSet = true;
}

bool OAIAvailabilityOfDevicesResponse_ipads::is_maximum_Set() const{
    return m_maximum_isSet;
}

bool OAIAvailabilityOfDevicesResponse_ipads::is_maximum_Valid() const{
    return m_maximum_isValid;
}

double OAIAvailabilityOfDevicesResponse_ipads::getRegistered() const {
    return m_registered;
}
void OAIAvailabilityOfDevicesResponse_ipads::setRegistered(const double &registered) {
    m_registered = registered;
    m_registered_isSet = true;
}

bool OAIAvailabilityOfDevicesResponse_ipads::is_registered_Set() const{
    return m_registered_isSet;
}

bool OAIAvailabilityOfDevicesResponse_ipads::is_registered_Valid() const{
    return m_registered_isValid;
}

bool OAIAvailabilityOfDevicesResponse_ipads::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_maximum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_registered_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAvailabilityOfDevicesResponse_ipads::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_available_isValid && m_maximum_isValid && m_registered_isValid && true;
}

} // namespace OpenAPI
