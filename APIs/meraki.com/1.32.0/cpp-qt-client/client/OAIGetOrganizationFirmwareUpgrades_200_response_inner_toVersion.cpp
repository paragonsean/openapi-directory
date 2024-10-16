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

#include "OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion() {
    this->initializeModel();
}

OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::~OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion() {}

void OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_release_date_isSet = false;
    m_release_date_isValid = false;

    m_release_type_isSet = false;
    m_release_type_isValid = false;

    m_short_name_isSet = false;
    m_short_name_isValid = false;
}

void OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_release_date_isValid = ::OpenAPI::fromJsonValue(m_release_date, json[QString("releaseDate")]);
    m_release_date_isSet = !json[QString("releaseDate")].isNull() && m_release_date_isValid;

    m_release_type_isValid = ::OpenAPI::fromJsonValue(m_release_type, json[QString("releaseType")]);
    m_release_type_isSet = !json[QString("releaseType")].isNull() && m_release_type_isValid;

    m_short_name_isValid = ::OpenAPI::fromJsonValue(m_short_name, json[QString("shortName")]);
    m_short_name_isSet = !json[QString("shortName")].isNull() && m_short_name_isValid;
}

QString OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_release_date_isSet) {
        obj.insert(QString("releaseDate"), ::OpenAPI::toJsonValue(m_release_date));
    }
    if (m_release_type_isSet) {
        obj.insert(QString("releaseType"), ::OpenAPI::toJsonValue(m_release_type));
    }
    if (m_short_name_isSet) {
        obj.insert(QString("shortName"), ::OpenAPI::toJsonValue(m_short_name));
    }
    return obj;
}

QString OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::getId() const {
    return m_id;
}
void OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::getReleaseDate() const {
    return m_release_date;
}
void OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::setReleaseDate(const QDateTime &release_date) {
    m_release_date = release_date;
    m_release_date_isSet = true;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::is_release_date_Set() const{
    return m_release_date_isSet;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::is_release_date_Valid() const{
    return m_release_date_isValid;
}

QString OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::getReleaseType() const {
    return m_release_type;
}
void OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::setReleaseType(const QString &release_type) {
    m_release_type = release_type;
    m_release_type_isSet = true;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::is_release_type_Set() const{
    return m_release_type_isSet;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::is_release_type_Valid() const{
    return m_release_type_isValid;
}

QString OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::getShortName() const {
    return m_short_name;
}
void OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::setShortName(const QString &short_name) {
    m_short_name = short_name;
    m_short_name_isSet = true;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::is_short_name_Set() const{
    return m_short_name_isSet;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::is_short_name_Valid() const{
    return m_short_name_isValid;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetOrganizationFirmwareUpgrades_200_response_inner_toVersion::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
