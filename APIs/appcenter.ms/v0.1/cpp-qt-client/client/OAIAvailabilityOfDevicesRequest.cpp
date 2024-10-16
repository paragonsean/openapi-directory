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

#include "OAIAvailabilityOfDevicesRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAvailabilityOfDevicesRequest::OAIAvailabilityOfDevicesRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAvailabilityOfDevicesRequest::OAIAvailabilityOfDevicesRequest() {
    this->initializeModel();
}

OAIAvailabilityOfDevicesRequest::~OAIAvailabilityOfDevicesRequest() {}

void OAIAvailabilityOfDevicesRequest::initializeModel() {

    m_password_isSet = false;
    m_password_isValid = false;

    m_service_connection_id_isSet = false;
    m_service_connection_id_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIAvailabilityOfDevicesRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAvailabilityOfDevicesRequest::fromJsonObject(QJsonObject json) {

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_service_connection_id_isValid = ::OpenAPI::fromJsonValue(m_service_connection_id, json[QString("service_connection_id")]);
    m_service_connection_id_isSet = !json[QString("service_connection_id")].isNull() && m_service_connection_id_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIAvailabilityOfDevicesRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAvailabilityOfDevicesRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_service_connection_id_isSet) {
        obj.insert(QString("service_connection_id"), ::OpenAPI::toJsonValue(m_service_connection_id));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIAvailabilityOfDevicesRequest::getPassword() const {
    return m_password;
}
void OAIAvailabilityOfDevicesRequest::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIAvailabilityOfDevicesRequest::is_password_Set() const{
    return m_password_isSet;
}

bool OAIAvailabilityOfDevicesRequest::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIAvailabilityOfDevicesRequest::getServiceConnectionId() const {
    return m_service_connection_id;
}
void OAIAvailabilityOfDevicesRequest::setServiceConnectionId(const QString &service_connection_id) {
    m_service_connection_id = service_connection_id;
    m_service_connection_id_isSet = true;
}

bool OAIAvailabilityOfDevicesRequest::is_service_connection_id_Set() const{
    return m_service_connection_id_isSet;
}

bool OAIAvailabilityOfDevicesRequest::is_service_connection_id_Valid() const{
    return m_service_connection_id_isValid;
}

QString OAIAvailabilityOfDevicesRequest::getUsername() const {
    return m_username;
}
void OAIAvailabilityOfDevicesRequest::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIAvailabilityOfDevicesRequest::is_username_Set() const{
    return m_username_isSet;
}

bool OAIAvailabilityOfDevicesRequest::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIAvailabilityOfDevicesRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_connection_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAvailabilityOfDevicesRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
