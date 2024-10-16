/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetNetworkSettings_200_response_securePort.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkSettings_200_response_securePort::OAIGetNetworkSettings_200_response_securePort(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkSettings_200_response_securePort::OAIGetNetworkSettings_200_response_securePort() {
    this->initializeModel();
}

OAIGetNetworkSettings_200_response_securePort::~OAIGetNetworkSettings_200_response_securePort() {}

void OAIGetNetworkSettings_200_response_securePort::initializeModel() {

    m_enabled_isSet = false;
    m_enabled_isValid = false;
}

void OAIGetNetworkSettings_200_response_securePort::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkSettings_200_response_securePort::fromJsonObject(QJsonObject json) {

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;
}

QString OAIGetNetworkSettings_200_response_securePort::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkSettings_200_response_securePort::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    return obj;
}

bool OAIGetNetworkSettings_200_response_securePort::isEnabled() const {
    return m_enabled;
}
void OAIGetNetworkSettings_200_response_securePort::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIGetNetworkSettings_200_response_securePort::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIGetNetworkSettings_200_response_securePort::is_enabled_Valid() const{
    return m_enabled_isValid;
}

bool OAIGetNetworkSettings_200_response_securePort::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkSettings_200_response_securePort::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
