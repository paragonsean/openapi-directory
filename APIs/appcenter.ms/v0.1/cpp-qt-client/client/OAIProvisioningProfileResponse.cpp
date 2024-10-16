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

#include "OAIProvisioningProfileResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProvisioningProfileResponse::OAIProvisioningProfileResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProvisioningProfileResponse::OAIProvisioningProfileResponse() {
    this->initializeModel();
}

OAIProvisioningProfileResponse::~OAIProvisioningProfileResponse() {}

void OAIProvisioningProfileResponse::initializeModel() {

    m_appex_profiles_isSet = false;
    m_appex_profiles_isValid = false;

    m_provisioning_bundle_id_isSet = false;
    m_provisioning_bundle_id_isValid = false;

    m_provisioning_profile_name_isSet = false;
    m_provisioning_profile_name_isValid = false;

    m_provisioning_profile_type_isSet = false;
    m_provisioning_profile_type_isValid = false;

    m_team_identifier_isSet = false;
    m_team_identifier_isValid = false;

    m_udids_isSet = false;
    m_udids_isValid = false;
}

void OAIProvisioningProfileResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProvisioningProfileResponse::fromJsonObject(QJsonObject json) {

    m_appex_profiles_isValid = ::OpenAPI::fromJsonValue(m_appex_profiles, json[QString("appex_profiles")]);
    m_appex_profiles_isSet = !json[QString("appex_profiles")].isNull() && m_appex_profiles_isValid;

    m_provisioning_bundle_id_isValid = ::OpenAPI::fromJsonValue(m_provisioning_bundle_id, json[QString("provisioning_bundle_id")]);
    m_provisioning_bundle_id_isSet = !json[QString("provisioning_bundle_id")].isNull() && m_provisioning_bundle_id_isValid;

    m_provisioning_profile_name_isValid = ::OpenAPI::fromJsonValue(m_provisioning_profile_name, json[QString("provisioning_profile_name")]);
    m_provisioning_profile_name_isSet = !json[QString("provisioning_profile_name")].isNull() && m_provisioning_profile_name_isValid;

    m_provisioning_profile_type_isValid = ::OpenAPI::fromJsonValue(m_provisioning_profile_type, json[QString("provisioning_profile_type")]);
    m_provisioning_profile_type_isSet = !json[QString("provisioning_profile_type")].isNull() && m_provisioning_profile_type_isValid;

    m_team_identifier_isValid = ::OpenAPI::fromJsonValue(m_team_identifier, json[QString("team_identifier")]);
    m_team_identifier_isSet = !json[QString("team_identifier")].isNull() && m_team_identifier_isValid;

    m_udids_isValid = ::OpenAPI::fromJsonValue(m_udids, json[QString("udids")]);
    m_udids_isSet = !json[QString("udids")].isNull() && m_udids_isValid;
}

QString OAIProvisioningProfileResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProvisioningProfileResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_appex_profiles.size() > 0) {
        obj.insert(QString("appex_profiles"), ::OpenAPI::toJsonValue(m_appex_profiles));
    }
    if (m_provisioning_bundle_id_isSet) {
        obj.insert(QString("provisioning_bundle_id"), ::OpenAPI::toJsonValue(m_provisioning_bundle_id));
    }
    if (m_provisioning_profile_name_isSet) {
        obj.insert(QString("provisioning_profile_name"), ::OpenAPI::toJsonValue(m_provisioning_profile_name));
    }
    if (m_provisioning_profile_type_isSet) {
        obj.insert(QString("provisioning_profile_type"), ::OpenAPI::toJsonValue(m_provisioning_profile_type));
    }
    if (m_team_identifier_isSet) {
        obj.insert(QString("team_identifier"), ::OpenAPI::toJsonValue(m_team_identifier));
    }
    if (m_udids.size() > 0) {
        obj.insert(QString("udids"), ::OpenAPI::toJsonValue(m_udids));
    }
    return obj;
}

QList<OAIProvisioningProfileResponse> OAIProvisioningProfileResponse::getAppexProfiles() const {
    return m_appex_profiles;
}
void OAIProvisioningProfileResponse::setAppexProfiles(const QList<OAIProvisioningProfileResponse> &appex_profiles) {
    m_appex_profiles = appex_profiles;
    m_appex_profiles_isSet = true;
}

bool OAIProvisioningProfileResponse::is_appex_profiles_Set() const{
    return m_appex_profiles_isSet;
}

bool OAIProvisioningProfileResponse::is_appex_profiles_Valid() const{
    return m_appex_profiles_isValid;
}

QString OAIProvisioningProfileResponse::getProvisioningBundleId() const {
    return m_provisioning_bundle_id;
}
void OAIProvisioningProfileResponse::setProvisioningBundleId(const QString &provisioning_bundle_id) {
    m_provisioning_bundle_id = provisioning_bundle_id;
    m_provisioning_bundle_id_isSet = true;
}

bool OAIProvisioningProfileResponse::is_provisioning_bundle_id_Set() const{
    return m_provisioning_bundle_id_isSet;
}

bool OAIProvisioningProfileResponse::is_provisioning_bundle_id_Valid() const{
    return m_provisioning_bundle_id_isValid;
}

QString OAIProvisioningProfileResponse::getProvisioningProfileName() const {
    return m_provisioning_profile_name;
}
void OAIProvisioningProfileResponse::setProvisioningProfileName(const QString &provisioning_profile_name) {
    m_provisioning_profile_name = provisioning_profile_name;
    m_provisioning_profile_name_isSet = true;
}

bool OAIProvisioningProfileResponse::is_provisioning_profile_name_Set() const{
    return m_provisioning_profile_name_isSet;
}

bool OAIProvisioningProfileResponse::is_provisioning_profile_name_Valid() const{
    return m_provisioning_profile_name_isValid;
}

QString OAIProvisioningProfileResponse::getProvisioningProfileType() const {
    return m_provisioning_profile_type;
}
void OAIProvisioningProfileResponse::setProvisioningProfileType(const QString &provisioning_profile_type) {
    m_provisioning_profile_type = provisioning_profile_type;
    m_provisioning_profile_type_isSet = true;
}

bool OAIProvisioningProfileResponse::is_provisioning_profile_type_Set() const{
    return m_provisioning_profile_type_isSet;
}

bool OAIProvisioningProfileResponse::is_provisioning_profile_type_Valid() const{
    return m_provisioning_profile_type_isValid;
}

QString OAIProvisioningProfileResponse::getTeamIdentifier() const {
    return m_team_identifier;
}
void OAIProvisioningProfileResponse::setTeamIdentifier(const QString &team_identifier) {
    m_team_identifier = team_identifier;
    m_team_identifier_isSet = true;
}

bool OAIProvisioningProfileResponse::is_team_identifier_Set() const{
    return m_team_identifier_isSet;
}

bool OAIProvisioningProfileResponse::is_team_identifier_Valid() const{
    return m_team_identifier_isValid;
}

QList<QString> OAIProvisioningProfileResponse::getUdids() const {
    return m_udids;
}
void OAIProvisioningProfileResponse::setUdids(const QList<QString> &udids) {
    m_udids = udids;
    m_udids_isSet = true;
}

bool OAIProvisioningProfileResponse::is_udids_Set() const{
    return m_udids_isSet;
}

bool OAIProvisioningProfileResponse::is_udids_Valid() const{
    return m_udids_isValid;
}

bool OAIProvisioningProfileResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_appex_profiles.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_provisioning_bundle_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_provisioning_profile_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_provisioning_profile_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_udids.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProvisioningProfileResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_provisioning_profile_type_isValid && true;
}

} // namespace OpenAPI
