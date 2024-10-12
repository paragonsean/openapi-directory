/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApplicationProperties_computeProfile_roles_inner_osProfile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApplicationProperties_computeProfile_roles_inner_osProfile::OAIApplicationProperties_computeProfile_roles_inner_osProfile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApplicationProperties_computeProfile_roles_inner_osProfile::OAIApplicationProperties_computeProfile_roles_inner_osProfile() {
    this->initializeModel();
}

OAIApplicationProperties_computeProfile_roles_inner_osProfile::~OAIApplicationProperties_computeProfile_roles_inner_osProfile() {}

void OAIApplicationProperties_computeProfile_roles_inner_osProfile::initializeModel() {

    m_linux_operating_system_profile_isSet = false;
    m_linux_operating_system_profile_isValid = false;
}

void OAIApplicationProperties_computeProfile_roles_inner_osProfile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApplicationProperties_computeProfile_roles_inner_osProfile::fromJsonObject(QJsonObject json) {

    m_linux_operating_system_profile_isValid = ::OpenAPI::fromJsonValue(m_linux_operating_system_profile, json[QString("linuxOperatingSystemProfile")]);
    m_linux_operating_system_profile_isSet = !json[QString("linuxOperatingSystemProfile")].isNull() && m_linux_operating_system_profile_isValid;
}

QString OAIApplicationProperties_computeProfile_roles_inner_osProfile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApplicationProperties_computeProfile_roles_inner_osProfile::asJsonObject() const {
    QJsonObject obj;
    if (m_linux_operating_system_profile.isSet()) {
        obj.insert(QString("linuxOperatingSystemProfile"), ::OpenAPI::toJsonValue(m_linux_operating_system_profile));
    }
    return obj;
}

OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile OAIApplicationProperties_computeProfile_roles_inner_osProfile::getLinuxOperatingSystemProfile() const {
    return m_linux_operating_system_profile;
}
void OAIApplicationProperties_computeProfile_roles_inner_osProfile::setLinuxOperatingSystemProfile(const OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile &linux_operating_system_profile) {
    m_linux_operating_system_profile = linux_operating_system_profile;
    m_linux_operating_system_profile_isSet = true;
}

bool OAIApplicationProperties_computeProfile_roles_inner_osProfile::is_linux_operating_system_profile_Set() const{
    return m_linux_operating_system_profile_isSet;
}

bool OAIApplicationProperties_computeProfile_roles_inner_osProfile::is_linux_operating_system_profile_Valid() const{
    return m_linux_operating_system_profile_isValid;
}

bool OAIApplicationProperties_computeProfile_roles_inner_osProfile::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_linux_operating_system_profile.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApplicationProperties_computeProfile_roles_inner_osProfile::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
