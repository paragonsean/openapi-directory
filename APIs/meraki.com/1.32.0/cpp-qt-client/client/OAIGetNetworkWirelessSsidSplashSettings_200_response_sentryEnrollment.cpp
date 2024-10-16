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

#include "OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment() {
    this->initializeModel();
}

OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::~OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment() {}

void OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::initializeModel() {

    m_enforced_systems_isSet = false;
    m_enforced_systems_isValid = false;

    m_strength_isSet = false;
    m_strength_isValid = false;

    m_systems_manager_network_isSet = false;
    m_systems_manager_network_isValid = false;
}

void OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::fromJsonObject(QJsonObject json) {

    m_enforced_systems_isValid = ::OpenAPI::fromJsonValue(m_enforced_systems, json[QString("enforcedSystems")]);
    m_enforced_systems_isSet = !json[QString("enforcedSystems")].isNull() && m_enforced_systems_isValid;

    m_strength_isValid = ::OpenAPI::fromJsonValue(m_strength, json[QString("strength")]);
    m_strength_isSet = !json[QString("strength")].isNull() && m_strength_isValid;

    m_systems_manager_network_isValid = ::OpenAPI::fromJsonValue(m_systems_manager_network, json[QString("systemsManagerNetwork")]);
    m_systems_manager_network_isSet = !json[QString("systemsManagerNetwork")].isNull() && m_systems_manager_network_isValid;
}

QString OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::asJsonObject() const {
    QJsonObject obj;
    if (m_enforced_systems.size() > 0) {
        obj.insert(QString("enforcedSystems"), ::OpenAPI::toJsonValue(m_enforced_systems));
    }
    if (m_strength_isSet) {
        obj.insert(QString("strength"), ::OpenAPI::toJsonValue(m_strength));
    }
    if (m_systems_manager_network.isSet()) {
        obj.insert(QString("systemsManagerNetwork"), ::OpenAPI::toJsonValue(m_systems_manager_network));
    }
    return obj;
}

QList<QString> OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::getEnforcedSystems() const {
    return m_enforced_systems;
}
void OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::setEnforcedSystems(const QList<QString> &enforced_systems) {
    m_enforced_systems = enforced_systems;
    m_enforced_systems_isSet = true;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::is_enforced_systems_Set() const{
    return m_enforced_systems_isSet;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::is_enforced_systems_Valid() const{
    return m_enforced_systems_isValid;
}

QString OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::getStrength() const {
    return m_strength;
}
void OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::setStrength(const QString &strength) {
    m_strength = strength;
    m_strength_isSet = true;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::is_strength_Set() const{
    return m_strength_isSet;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::is_strength_Valid() const{
    return m_strength_isValid;
}

OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment_systemsManagerNetwork OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::getSystemsManagerNetwork() const {
    return m_systems_manager_network;
}
void OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::setSystemsManagerNetwork(const OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment_systemsManagerNetwork &systems_manager_network) {
    m_systems_manager_network = systems_manager_network;
    m_systems_manager_network_isSet = true;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::is_systems_manager_network_Set() const{
    return m_systems_manager_network_isSet;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::is_systems_manager_network_Valid() const{
    return m_systems_manager_network_isValid;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enforced_systems.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_strength_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_systems_manager_network.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkWirelessSsidSplashSettings_200_response_sentryEnrollment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
