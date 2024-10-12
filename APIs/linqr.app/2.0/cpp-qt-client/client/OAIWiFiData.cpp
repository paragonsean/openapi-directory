/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWiFiData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWiFiData::OAIWiFiData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWiFiData::OAIWiFiData() {
    this->initializeModel();
}

OAIWiFiData::~OAIWiFiData() {}

void OAIWiFiData::initializeModel() {

    m_hidden_isSet = false;
    m_hidden_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_security_isSet = false;
    m_security_isValid = false;

    m_ssid_isSet = false;
    m_ssid_isValid = false;
}

void OAIWiFiData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWiFiData::fromJsonObject(QJsonObject json) {

    m_hidden_isValid = ::OpenAPI::fromJsonValue(m_hidden, json[QString("hidden")]);
    m_hidden_isSet = !json[QString("hidden")].isNull() && m_hidden_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_security_isValid = ::OpenAPI::fromJsonValue(m_security, json[QString("security")]);
    m_security_isSet = !json[QString("security")].isNull() && m_security_isValid;

    m_ssid_isValid = ::OpenAPI::fromJsonValue(m_ssid, json[QString("ssid")]);
    m_ssid_isSet = !json[QString("ssid")].isNull() && m_ssid_isValid;
}

QString OAIWiFiData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWiFiData::asJsonObject() const {
    QJsonObject obj;
    if (m_hidden_isSet) {
        obj.insert(QString("hidden"), ::OpenAPI::toJsonValue(m_hidden));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_security.isSet()) {
        obj.insert(QString("security"), ::OpenAPI::toJsonValue(m_security));
    }
    if (m_ssid_isSet) {
        obj.insert(QString("ssid"), ::OpenAPI::toJsonValue(m_ssid));
    }
    return obj;
}

bool OAIWiFiData::isHidden() const {
    return m_hidden;
}
void OAIWiFiData::setHidden(const bool &hidden) {
    m_hidden = hidden;
    m_hidden_isSet = true;
}

bool OAIWiFiData::is_hidden_Set() const{
    return m_hidden_isSet;
}

bool OAIWiFiData::is_hidden_Valid() const{
    return m_hidden_isValid;
}

QString OAIWiFiData::getPassword() const {
    return m_password;
}
void OAIWiFiData::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIWiFiData::is_password_Set() const{
    return m_password_isSet;
}

bool OAIWiFiData::is_password_Valid() const{
    return m_password_isValid;
}

OAIWiFiSecurity OAIWiFiData::getSecurity() const {
    return m_security;
}
void OAIWiFiData::setSecurity(const OAIWiFiSecurity &security) {
    m_security = security;
    m_security_isSet = true;
}

bool OAIWiFiData::is_security_Set() const{
    return m_security_isSet;
}

bool OAIWiFiData::is_security_Valid() const{
    return m_security_isValid;
}

QString OAIWiFiData::getSsid() const {
    return m_ssid;
}
void OAIWiFiData::setSsid(const QString &ssid) {
    m_ssid = ssid;
    m_ssid_isSet = true;
}

bool OAIWiFiData::is_ssid_Set() const{
    return m_ssid_isSet;
}

bool OAIWiFiData::is_ssid_Valid() const{
    return m_ssid_isValid;
}

bool OAIWiFiData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_hidden_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_security.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWiFiData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_ssid_isValid && true;
}

} // namespace OpenAPI
