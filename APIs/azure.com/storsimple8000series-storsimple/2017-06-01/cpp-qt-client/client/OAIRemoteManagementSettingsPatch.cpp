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

#include "OAIRemoteManagementSettingsPatch.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRemoteManagementSettingsPatch::OAIRemoteManagementSettingsPatch(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRemoteManagementSettingsPatch::OAIRemoteManagementSettingsPatch() {
    this->initializeModel();
}

OAIRemoteManagementSettingsPatch::~OAIRemoteManagementSettingsPatch() {}

void OAIRemoteManagementSettingsPatch::initializeModel() {

    m_remote_management_mode_isSet = false;
    m_remote_management_mode_isValid = false;
}

void OAIRemoteManagementSettingsPatch::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRemoteManagementSettingsPatch::fromJsonObject(QJsonObject json) {

    m_remote_management_mode_isValid = ::OpenAPI::fromJsonValue(m_remote_management_mode, json[QString("remoteManagementMode")]);
    m_remote_management_mode_isSet = !json[QString("remoteManagementMode")].isNull() && m_remote_management_mode_isValid;
}

QString OAIRemoteManagementSettingsPatch::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRemoteManagementSettingsPatch::asJsonObject() const {
    QJsonObject obj;
    if (m_remote_management_mode_isSet) {
        obj.insert(QString("remoteManagementMode"), ::OpenAPI::toJsonValue(m_remote_management_mode));
    }
    return obj;
}

QString OAIRemoteManagementSettingsPatch::getRemoteManagementMode() const {
    return m_remote_management_mode;
}
void OAIRemoteManagementSettingsPatch::setRemoteManagementMode(const QString &remote_management_mode) {
    m_remote_management_mode = remote_management_mode;
    m_remote_management_mode_isSet = true;
}

bool OAIRemoteManagementSettingsPatch::is_remote_management_mode_Set() const{
    return m_remote_management_mode_isSet;
}

bool OAIRemoteManagementSettingsPatch::is_remote_management_mode_Valid() const{
    return m_remote_management_mode_isValid;
}

bool OAIRemoteManagementSettingsPatch::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_remote_management_mode_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRemoteManagementSettingsPatch::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_remote_management_mode_isValid && true;
}

} // namespace OpenAPI
