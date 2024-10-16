/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserNameAvailabilityResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserNameAvailabilityResponse::OAIUserNameAvailabilityResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserNameAvailabilityResponse::OAIUserNameAvailabilityResponse() {
    this->initializeModel();
}

OAIUserNameAvailabilityResponse::~OAIUserNameAvailabilityResponse() {}

void OAIUserNameAvailabilityResponse::initializeModel() {

    m_available_isSet = false;
    m_available_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIUserNameAvailabilityResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserNameAvailabilityResponse::fromJsonObject(QJsonObject json) {

    m_available_isValid = ::OpenAPI::fromJsonValue(m_available, json[QString("available")]);
    m_available_isSet = !json[QString("available")].isNull() && m_available_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIUserNameAvailabilityResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserNameAvailabilityResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_available_isSet) {
        obj.insert(QString("available"), ::OpenAPI::toJsonValue(m_available));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

bool OAIUserNameAvailabilityResponse::isAvailable() const {
    return m_available;
}
void OAIUserNameAvailabilityResponse::setAvailable(const bool &available) {
    m_available = available;
    m_available_isSet = true;
}

bool OAIUserNameAvailabilityResponse::is_available_Set() const{
    return m_available_isSet;
}

bool OAIUserNameAvailabilityResponse::is_available_Valid() const{
    return m_available_isValid;
}

QString OAIUserNameAvailabilityResponse::getName() const {
    return m_name;
}
void OAIUserNameAvailabilityResponse::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUserNameAvailabilityResponse::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUserNameAvailabilityResponse::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIUserNameAvailabilityResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_available_isSet) {
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

bool OAIUserNameAvailabilityResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_available_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
