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

#include "OAIDeparture.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDeparture::OAIDeparture(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDeparture::OAIDeparture() {
    this->initializeModel();
}

OAIDeparture::~OAIDeparture() {}

void OAIDeparture::initializeModel() {

    m_iata_code_isSet = false;
    m_iata_code_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_sub_type_isSet = false;
    m_sub_type_isValid = false;
}

void OAIDeparture::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDeparture::fromJsonObject(QJsonObject json) {

    m_iata_code_isValid = ::OpenAPI::fromJsonValue(m_iata_code, json[QString("iataCode")]);
    m_iata_code_isSet = !json[QString("iataCode")].isNull() && m_iata_code_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_sub_type_isValid = ::OpenAPI::fromJsonValue(m_sub_type, json[QString("subType")]);
    m_sub_type_isSet = !json[QString("subType")].isNull() && m_sub_type_isValid;
}

QString OAIDeparture::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDeparture::asJsonObject() const {
    QJsonObject obj;
    if (m_iata_code_isSet) {
        obj.insert(QString("iataCode"), ::OpenAPI::toJsonValue(m_iata_code));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_sub_type_isSet) {
        obj.insert(QString("subType"), ::OpenAPI::toJsonValue(m_sub_type));
    }
    return obj;
}

QString OAIDeparture::getIataCode() const {
    return m_iata_code;
}
void OAIDeparture::setIataCode(const QString &iata_code) {
    m_iata_code = iata_code;
    m_iata_code_isSet = true;
}

bool OAIDeparture::is_iata_code_Set() const{
    return m_iata_code_isSet;
}

bool OAIDeparture::is_iata_code_Valid() const{
    return m_iata_code_isValid;
}

QString OAIDeparture::getName() const {
    return m_name;
}
void OAIDeparture::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDeparture::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDeparture::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIDeparture::getSubType() const {
    return m_sub_type;
}
void OAIDeparture::setSubType(const QString &sub_type) {
    m_sub_type = sub_type;
    m_sub_type_isSet = true;
}

bool OAIDeparture::is_sub_type_Set() const{
    return m_sub_type_isSet;
}

bool OAIDeparture::is_sub_type_Valid() const{
    return m_sub_type_isValid;
}

bool OAIDeparture::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_iata_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDeparture::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
