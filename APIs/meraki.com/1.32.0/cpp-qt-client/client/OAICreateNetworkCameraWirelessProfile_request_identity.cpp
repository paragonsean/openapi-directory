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

#include "OAICreateNetworkCameraWirelessProfile_request_identity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateNetworkCameraWirelessProfile_request_identity::OAICreateNetworkCameraWirelessProfile_request_identity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateNetworkCameraWirelessProfile_request_identity::OAICreateNetworkCameraWirelessProfile_request_identity() {
    this->initializeModel();
}

OAICreateNetworkCameraWirelessProfile_request_identity::~OAICreateNetworkCameraWirelessProfile_request_identity() {}

void OAICreateNetworkCameraWirelessProfile_request_identity::initializeModel() {

    m_password_isSet = false;
    m_password_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAICreateNetworkCameraWirelessProfile_request_identity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateNetworkCameraWirelessProfile_request_identity::fromJsonObject(QJsonObject json) {

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAICreateNetworkCameraWirelessProfile_request_identity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateNetworkCameraWirelessProfile_request_identity::asJsonObject() const {
    QJsonObject obj;
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAICreateNetworkCameraWirelessProfile_request_identity::getPassword() const {
    return m_password;
}
void OAICreateNetworkCameraWirelessProfile_request_identity::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAICreateNetworkCameraWirelessProfile_request_identity::is_password_Set() const{
    return m_password_isSet;
}

bool OAICreateNetworkCameraWirelessProfile_request_identity::is_password_Valid() const{
    return m_password_isValid;
}

QString OAICreateNetworkCameraWirelessProfile_request_identity::getUsername() const {
    return m_username;
}
void OAICreateNetworkCameraWirelessProfile_request_identity::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAICreateNetworkCameraWirelessProfile_request_identity::is_username_Set() const{
    return m_username_isSet;
}

bool OAICreateNetworkCameraWirelessProfile_request_identity::is_username_Valid() const{
    return m_username_isValid;
}

bool OAICreateNetworkCameraWirelessProfile_request_identity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_password_isSet) {
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

bool OAICreateNetworkCameraWirelessProfile_request_identity::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
