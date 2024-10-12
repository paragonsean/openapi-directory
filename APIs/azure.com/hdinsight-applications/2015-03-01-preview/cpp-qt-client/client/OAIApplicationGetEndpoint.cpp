/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApplicationGetEndpoint.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApplicationGetEndpoint::OAIApplicationGetEndpoint(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApplicationGetEndpoint::OAIApplicationGetEndpoint() {
    this->initializeModel();
}

OAIApplicationGetEndpoint::~OAIApplicationGetEndpoint() {}

void OAIApplicationGetEndpoint::initializeModel() {

    m_destination_port_isSet = false;
    m_destination_port_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_public_port_isSet = false;
    m_public_port_isValid = false;
}

void OAIApplicationGetEndpoint::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApplicationGetEndpoint::fromJsonObject(QJsonObject json) {

    m_destination_port_isValid = ::OpenAPI::fromJsonValue(m_destination_port, json[QString("destinationPort")]);
    m_destination_port_isSet = !json[QString("destinationPort")].isNull() && m_destination_port_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_public_port_isValid = ::OpenAPI::fromJsonValue(m_public_port, json[QString("publicPort")]);
    m_public_port_isSet = !json[QString("publicPort")].isNull() && m_public_port_isValid;
}

QString OAIApplicationGetEndpoint::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApplicationGetEndpoint::asJsonObject() const {
    QJsonObject obj;
    if (m_destination_port_isSet) {
        obj.insert(QString("destinationPort"), ::OpenAPI::toJsonValue(m_destination_port));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_public_port_isSet) {
        obj.insert(QString("publicPort"), ::OpenAPI::toJsonValue(m_public_port));
    }
    return obj;
}

qint32 OAIApplicationGetEndpoint::getDestinationPort() const {
    return m_destination_port;
}
void OAIApplicationGetEndpoint::setDestinationPort(const qint32 &destination_port) {
    m_destination_port = destination_port;
    m_destination_port_isSet = true;
}

bool OAIApplicationGetEndpoint::is_destination_port_Set() const{
    return m_destination_port_isSet;
}

bool OAIApplicationGetEndpoint::is_destination_port_Valid() const{
    return m_destination_port_isValid;
}

QString OAIApplicationGetEndpoint::getLocation() const {
    return m_location;
}
void OAIApplicationGetEndpoint::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAIApplicationGetEndpoint::is_location_Set() const{
    return m_location_isSet;
}

bool OAIApplicationGetEndpoint::is_location_Valid() const{
    return m_location_isValid;
}

qint32 OAIApplicationGetEndpoint::getPublicPort() const {
    return m_public_port;
}
void OAIApplicationGetEndpoint::setPublicPort(const qint32 &public_port) {
    m_public_port = public_port;
    m_public_port_isSet = true;
}

bool OAIApplicationGetEndpoint::is_public_port_Set() const{
    return m_public_port_isSet;
}

bool OAIApplicationGetEndpoint::is_public_port_Valid() const{
    return m_public_port_isValid;
}

bool OAIApplicationGetEndpoint::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_destination_port_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_port_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApplicationGetEndpoint::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
