/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDepartureAirportLocation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDepartureAirportLocation::OAIDepartureAirportLocation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDepartureAirportLocation::OAIDepartureAirportLocation() {
    this->initializeModel();
}

OAIDepartureAirportLocation::~OAIDepartureAirportLocation() {}

void OAIDepartureAirportLocation::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIDepartureAirportLocation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDepartureAirportLocation::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIDepartureAirportLocation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDepartureAirportLocation::asJsonObject() const {
    QJsonObject obj;
    if (m_address.isSet()) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

OAIAddress OAIDepartureAirportLocation::getAddress() const {
    return m_address;
}
void OAIDepartureAirportLocation::setAddress(const OAIAddress &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIDepartureAirportLocation::is_address_Set() const{
    return m_address_isSet;
}

bool OAIDepartureAirportLocation::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIDepartureAirportLocation::getName() const {
    return m_name;
}
void OAIDepartureAirportLocation::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDepartureAirportLocation::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDepartureAirportLocation::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIDepartureAirportLocation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDepartureAirportLocation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
