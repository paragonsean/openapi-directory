/**
 * Stationsdatenbereitstellung
 * An API providing master data for German railway stations by DB Station&Service AG.
 *
 * The version of the OpenAPI document: 2.2.01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStationManagement.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStationManagement::OAIStationManagement(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStationManagement::OAIStationManagement() {
    this->initializeModel();
}

OAIStationManagement::~OAIStationManagement() {}

void OAIStationManagement::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;
}

void OAIStationManagement::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStationManagement::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;
}

QString OAIStationManagement::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStationManagement::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    return obj;
}

QString OAIStationManagement::getName() const {
    return m_name;
}
void OAIStationManagement::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIStationManagement::is_name_Set() const{
    return m_name_isSet;
}

bool OAIStationManagement::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIStationManagement::getNumber() const {
    return m_number;
}
void OAIStationManagement::setNumber(const qint32 &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIStationManagement::is_number_Set() const{
    return m_number_isSet;
}

bool OAIStationManagement::is_number_Valid() const{
    return m_number_isValid;
}

bool OAIStationManagement::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStationManagement::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
