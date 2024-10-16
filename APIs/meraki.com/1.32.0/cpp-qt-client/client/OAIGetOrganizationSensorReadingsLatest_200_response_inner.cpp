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

#include "OAIGetOrganizationSensorReadingsLatest_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetOrganizationSensorReadingsLatest_200_response_inner::OAIGetOrganizationSensorReadingsLatest_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetOrganizationSensorReadingsLatest_200_response_inner::OAIGetOrganizationSensorReadingsLatest_200_response_inner() {
    this->initializeModel();
}

OAIGetOrganizationSensorReadingsLatest_200_response_inner::~OAIGetOrganizationSensorReadingsLatest_200_response_inner() {}

void OAIGetOrganizationSensorReadingsLatest_200_response_inner::initializeModel() {

    m_network_isSet = false;
    m_network_isValid = false;

    m_readings_isSet = false;
    m_readings_isValid = false;

    m_serial_isSet = false;
    m_serial_isValid = false;
}

void OAIGetOrganizationSensorReadingsLatest_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetOrganizationSensorReadingsLatest_200_response_inner::fromJsonObject(QJsonObject json) {

    m_network_isValid = ::OpenAPI::fromJsonValue(m_network, json[QString("network")]);
    m_network_isSet = !json[QString("network")].isNull() && m_network_isValid;

    m_readings_isValid = ::OpenAPI::fromJsonValue(m_readings, json[QString("readings")]);
    m_readings_isSet = !json[QString("readings")].isNull() && m_readings_isValid;

    m_serial_isValid = ::OpenAPI::fromJsonValue(m_serial, json[QString("serial")]);
    m_serial_isSet = !json[QString("serial")].isNull() && m_serial_isValid;
}

QString OAIGetOrganizationSensorReadingsLatest_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetOrganizationSensorReadingsLatest_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_network.isSet()) {
        obj.insert(QString("network"), ::OpenAPI::toJsonValue(m_network));
    }
    if (m_readings.size() > 0) {
        obj.insert(QString("readings"), ::OpenAPI::toJsonValue(m_readings));
    }
    if (m_serial_isSet) {
        obj.insert(QString("serial"), ::OpenAPI::toJsonValue(m_serial));
    }
    return obj;
}

OAIGetOrganizationSensorReadingsHistory_200_response_inner_network OAIGetOrganizationSensorReadingsLatest_200_response_inner::getNetwork() const {
    return m_network;
}
void OAIGetOrganizationSensorReadingsLatest_200_response_inner::setNetwork(const OAIGetOrganizationSensorReadingsHistory_200_response_inner_network &network) {
    m_network = network;
    m_network_isSet = true;
}

bool OAIGetOrganizationSensorReadingsLatest_200_response_inner::is_network_Set() const{
    return m_network_isSet;
}

bool OAIGetOrganizationSensorReadingsLatest_200_response_inner::is_network_Valid() const{
    return m_network_isValid;
}

QList<OAIGetOrganizationSensorReadingsLatest_200_response_inner_readings_inner> OAIGetOrganizationSensorReadingsLatest_200_response_inner::getReadings() const {
    return m_readings;
}
void OAIGetOrganizationSensorReadingsLatest_200_response_inner::setReadings(const QList<OAIGetOrganizationSensorReadingsLatest_200_response_inner_readings_inner> &readings) {
    m_readings = readings;
    m_readings_isSet = true;
}

bool OAIGetOrganizationSensorReadingsLatest_200_response_inner::is_readings_Set() const{
    return m_readings_isSet;
}

bool OAIGetOrganizationSensorReadingsLatest_200_response_inner::is_readings_Valid() const{
    return m_readings_isValid;
}

QString OAIGetOrganizationSensorReadingsLatest_200_response_inner::getSerial() const {
    return m_serial;
}
void OAIGetOrganizationSensorReadingsLatest_200_response_inner::setSerial(const QString &serial) {
    m_serial = serial;
    m_serial_isSet = true;
}

bool OAIGetOrganizationSensorReadingsLatest_200_response_inner::is_serial_Set() const{
    return m_serial_isSet;
}

bool OAIGetOrganizationSensorReadingsLatest_200_response_inner::is_serial_Valid() const{
    return m_serial_isValid;
}

bool OAIGetOrganizationSensorReadingsLatest_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_network.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_readings.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_serial_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetOrganizationSensorReadingsLatest_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
