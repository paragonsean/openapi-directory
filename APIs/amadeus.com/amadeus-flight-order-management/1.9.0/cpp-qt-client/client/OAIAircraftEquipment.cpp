/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAircraftEquipment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAircraftEquipment::OAIAircraftEquipment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAircraftEquipment::OAIAircraftEquipment() {
    this->initializeModel();
}

OAIAircraftEquipment::~OAIAircraftEquipment() {}

void OAIAircraftEquipment::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;
}

void OAIAircraftEquipment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAircraftEquipment::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;
}

QString OAIAircraftEquipment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAircraftEquipment::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    return obj;
}

QString OAIAircraftEquipment::getCode() const {
    return m_code;
}
void OAIAircraftEquipment::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIAircraftEquipment::is_code_Set() const{
    return m_code_isSet;
}

bool OAIAircraftEquipment::is_code_Valid() const{
    return m_code_isValid;
}

bool OAIAircraftEquipment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAircraftEquipment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
