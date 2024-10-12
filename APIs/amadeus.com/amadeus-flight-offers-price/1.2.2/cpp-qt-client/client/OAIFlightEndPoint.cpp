/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFlightEndPoint.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFlightEndPoint::OAIFlightEndPoint(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFlightEndPoint::OAIFlightEndPoint() {
    this->initializeModel();
}

OAIFlightEndPoint::~OAIFlightEndPoint() {}

void OAIFlightEndPoint::initializeModel() {

    m_iata_code_isSet = false;
    m_iata_code_isValid = false;

    m_terminal_isSet = false;
    m_terminal_isValid = false;

    m_at_isSet = false;
    m_at_isValid = false;
}

void OAIFlightEndPoint::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFlightEndPoint::fromJsonObject(QJsonObject json) {

    m_iata_code_isValid = ::OpenAPI::fromJsonValue(m_iata_code, json[QString("iataCode")]);
    m_iata_code_isSet = !json[QString("iataCode")].isNull() && m_iata_code_isValid;

    m_terminal_isValid = ::OpenAPI::fromJsonValue(m_terminal, json[QString("terminal")]);
    m_terminal_isSet = !json[QString("terminal")].isNull() && m_terminal_isValid;

    m_at_isValid = ::OpenAPI::fromJsonValue(m_at, json[QString("at")]);
    m_at_isSet = !json[QString("at")].isNull() && m_at_isValid;
}

QString OAIFlightEndPoint::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFlightEndPoint::asJsonObject() const {
    QJsonObject obj;
    if (m_iata_code_isSet) {
        obj.insert(QString("iataCode"), ::OpenAPI::toJsonValue(m_iata_code));
    }
    if (m_terminal_isSet) {
        obj.insert(QString("terminal"), ::OpenAPI::toJsonValue(m_terminal));
    }
    if (m_at_isSet) {
        obj.insert(QString("at"), ::OpenAPI::toJsonValue(m_at));
    }
    return obj;
}

QString OAIFlightEndPoint::getIataCode() const {
    return m_iata_code;
}
void OAIFlightEndPoint::setIataCode(const QString &iata_code) {
    m_iata_code = iata_code;
    m_iata_code_isSet = true;
}

bool OAIFlightEndPoint::is_iata_code_Set() const{
    return m_iata_code_isSet;
}

bool OAIFlightEndPoint::is_iata_code_Valid() const{
    return m_iata_code_isValid;
}

QString OAIFlightEndPoint::getTerminal() const {
    return m_terminal;
}
void OAIFlightEndPoint::setTerminal(const QString &terminal) {
    m_terminal = terminal;
    m_terminal_isSet = true;
}

bool OAIFlightEndPoint::is_terminal_Set() const{
    return m_terminal_isSet;
}

bool OAIFlightEndPoint::is_terminal_Valid() const{
    return m_terminal_isValid;
}

QDateTime OAIFlightEndPoint::getAt() const {
    return m_at;
}
void OAIFlightEndPoint::setAt(const QDateTime &at) {
    m_at = at;
    m_at_isSet = true;
}

bool OAIFlightEndPoint::is_at_Set() const{
    return m_at_isSet;
}

bool OAIFlightEndPoint::is_at_Valid() const{
    return m_at_isValid;
}

bool OAIFlightEndPoint::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_iata_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_terminal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFlightEndPoint::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
