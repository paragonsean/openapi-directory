/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISecuritySettingsProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISecuritySettingsProperties::OAISecuritySettingsProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISecuritySettingsProperties::OAISecuritySettingsProperties() {
    this->initializeModel();
}

OAISecuritySettingsProperties::~OAISecuritySettingsProperties() {}

void OAISecuritySettingsProperties::initializeModel() {

    m_chap_settings_isSet = false;
    m_chap_settings_isValid = false;

    m_remote_management_settings_isSet = false;
    m_remote_management_settings_isValid = false;
}

void OAISecuritySettingsProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISecuritySettingsProperties::fromJsonObject(QJsonObject json) {

    m_chap_settings_isValid = ::OpenAPI::fromJsonValue(m_chap_settings, json[QString("chapSettings")]);
    m_chap_settings_isSet = !json[QString("chapSettings")].isNull() && m_chap_settings_isValid;

    m_remote_management_settings_isValid = ::OpenAPI::fromJsonValue(m_remote_management_settings, json[QString("remoteManagementSettings")]);
    m_remote_management_settings_isSet = !json[QString("remoteManagementSettings")].isNull() && m_remote_management_settings_isValid;
}

QString OAISecuritySettingsProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISecuritySettingsProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_chap_settings.isSet()) {
        obj.insert(QString("chapSettings"), ::OpenAPI::toJsonValue(m_chap_settings));
    }
    if (m_remote_management_settings.isSet()) {
        obj.insert(QString("remoteManagementSettings"), ::OpenAPI::toJsonValue(m_remote_management_settings));
    }
    return obj;
}

OAIChapSettings OAISecuritySettingsProperties::getChapSettings() const {
    return m_chap_settings;
}
void OAISecuritySettingsProperties::setChapSettings(const OAIChapSettings &chap_settings) {
    m_chap_settings = chap_settings;
    m_chap_settings_isSet = true;
}

bool OAISecuritySettingsProperties::is_chap_settings_Set() const{
    return m_chap_settings_isSet;
}

bool OAISecuritySettingsProperties::is_chap_settings_Valid() const{
    return m_chap_settings_isValid;
}

OAIRemoteManagementSettings OAISecuritySettingsProperties::getRemoteManagementSettings() const {
    return m_remote_management_settings;
}
void OAISecuritySettingsProperties::setRemoteManagementSettings(const OAIRemoteManagementSettings &remote_management_settings) {
    m_remote_management_settings = remote_management_settings;
    m_remote_management_settings_isSet = true;
}

bool OAISecuritySettingsProperties::is_remote_management_settings_Set() const{
    return m_remote_management_settings_isSet;
}

bool OAISecuritySettingsProperties::is_remote_management_settings_Valid() const{
    return m_remote_management_settings_isValid;
}

bool OAISecuritySettingsProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_chap_settings.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_remote_management_settings.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISecuritySettingsProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_chap_settings_isValid && m_remote_management_settings_isValid && true;
}

} // namespace OpenAPI
