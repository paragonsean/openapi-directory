/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOriginalFlightEndPoint.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOriginalFlightEndPoint::OAIOriginalFlightEndPoint(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOriginalFlightEndPoint::OAIOriginalFlightEndPoint() {
    this->initializeModel();
}

OAIOriginalFlightEndPoint::~OAIOriginalFlightEndPoint() {}

void OAIOriginalFlightEndPoint::initializeModel() {

    m_iata_code_isSet = false;
    m_iata_code_isValid = false;

    m_terminal_isSet = false;
    m_terminal_isValid = false;
}

void OAIOriginalFlightEndPoint::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOriginalFlightEndPoint::fromJsonObject(QJsonObject json) {

    m_iata_code_isValid = ::OpenAPI::fromJsonValue(m_iata_code, json[QString("iataCode")]);
    m_iata_code_isSet = !json[QString("iataCode")].isNull() && m_iata_code_isValid;

    m_terminal_isValid = ::OpenAPI::fromJsonValue(m_terminal, json[QString("terminal")]);
    m_terminal_isSet = !json[QString("terminal")].isNull() && m_terminal_isValid;
}

QString OAIOriginalFlightEndPoint::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOriginalFlightEndPoint::asJsonObject() const {
    QJsonObject obj;
    if (m_iata_code_isSet) {
        obj.insert(QString("iataCode"), ::OpenAPI::toJsonValue(m_iata_code));
    }
    if (m_terminal_isSet) {
        obj.insert(QString("terminal"), ::OpenAPI::toJsonValue(m_terminal));
    }
    return obj;
}

QString OAIOriginalFlightEndPoint::getIataCode() const {
    return m_iata_code;
}
void OAIOriginalFlightEndPoint::setIataCode(const QString &iata_code) {
    m_iata_code = iata_code;
    m_iata_code_isSet = true;
}

bool OAIOriginalFlightEndPoint::is_iata_code_Set() const{
    return m_iata_code_isSet;
}

bool OAIOriginalFlightEndPoint::is_iata_code_Valid() const{
    return m_iata_code_isValid;
}

QString OAIOriginalFlightEndPoint::getTerminal() const {
    return m_terminal;
}
void OAIOriginalFlightEndPoint::setTerminal(const QString &terminal) {
    m_terminal = terminal;
    m_terminal_isSet = true;
}

bool OAIOriginalFlightEndPoint::is_terminal_Set() const{
    return m_terminal_isSet;
}

bool OAIOriginalFlightEndPoint::is_terminal_Valid() const{
    return m_terminal_isValid;
}

bool OAIOriginalFlightEndPoint::isSet() const {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIOriginalFlightEndPoint::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
