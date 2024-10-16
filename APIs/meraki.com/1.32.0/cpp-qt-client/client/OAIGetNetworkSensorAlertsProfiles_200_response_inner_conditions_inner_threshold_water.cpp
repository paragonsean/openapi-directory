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

#include "OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water() {
    this->initializeModel();
}

OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::~OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water() {}

void OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::initializeModel() {

    m_present_isSet = false;
    m_present_isValid = false;
}

void OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::fromJsonObject(QJsonObject json) {

    m_present_isValid = ::OpenAPI::fromJsonValue(m_present, json[QString("present")]);
    m_present_isSet = !json[QString("present")].isNull() && m_present_isValid;
}

QString OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::asJsonObject() const {
    QJsonObject obj;
    if (m_present_isSet) {
        obj.insert(QString("present"), ::OpenAPI::toJsonValue(m_present));
    }
    return obj;
}

bool OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::isPresent() const {
    return m_present;
}
void OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::setPresent(const bool &present) {
    m_present = present;
    m_present_isSet = true;
}

bool OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::is_present_Set() const{
    return m_present_isSet;
}

bool OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::is_present_Valid() const{
    return m_present_isValid;
}

bool OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_present_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_water::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_present_isValid && true;
}

} // namespace OpenAPI
