/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGalleryImagePropertiesFragment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGalleryImagePropertiesFragment::OAIGalleryImagePropertiesFragment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGalleryImagePropertiesFragment::OAIGalleryImagePropertiesFragment() {
    this->initializeModel();
}

OAIGalleryImagePropertiesFragment::~OAIGalleryImagePropertiesFragment() {}

void OAIGalleryImagePropertiesFragment::initializeModel() {

    m_is_enabled_isSet = false;
    m_is_enabled_isValid = false;

    m_is_override_isSet = false;
    m_is_override_isValid = false;

    m_is_plan_authorized_isSet = false;
    m_is_plan_authorized_isValid = false;

    m_provisioning_state_isSet = false;
    m_provisioning_state_isValid = false;

    m_unique_identifier_isSet = false;
    m_unique_identifier_isValid = false;
}

void OAIGalleryImagePropertiesFragment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGalleryImagePropertiesFragment::fromJsonObject(QJsonObject json) {

    m_is_enabled_isValid = ::OpenAPI::fromJsonValue(m_is_enabled, json[QString("isEnabled")]);
    m_is_enabled_isSet = !json[QString("isEnabled")].isNull() && m_is_enabled_isValid;

    m_is_override_isValid = ::OpenAPI::fromJsonValue(m_is_override, json[QString("isOverride")]);
    m_is_override_isSet = !json[QString("isOverride")].isNull() && m_is_override_isValid;

    m_is_plan_authorized_isValid = ::OpenAPI::fromJsonValue(m_is_plan_authorized, json[QString("isPlanAuthorized")]);
    m_is_plan_authorized_isSet = !json[QString("isPlanAuthorized")].isNull() && m_is_plan_authorized_isValid;

    m_provisioning_state_isValid = ::OpenAPI::fromJsonValue(m_provisioning_state, json[QString("provisioningState")]);
    m_provisioning_state_isSet = !json[QString("provisioningState")].isNull() && m_provisioning_state_isValid;

    m_unique_identifier_isValid = ::OpenAPI::fromJsonValue(m_unique_identifier, json[QString("uniqueIdentifier")]);
    m_unique_identifier_isSet = !json[QString("uniqueIdentifier")].isNull() && m_unique_identifier_isValid;
}

QString OAIGalleryImagePropertiesFragment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGalleryImagePropertiesFragment::asJsonObject() const {
    QJsonObject obj;
    if (m_is_enabled_isSet) {
        obj.insert(QString("isEnabled"), ::OpenAPI::toJsonValue(m_is_enabled));
    }
    if (m_is_override_isSet) {
        obj.insert(QString("isOverride"), ::OpenAPI::toJsonValue(m_is_override));
    }
    if (m_is_plan_authorized_isSet) {
        obj.insert(QString("isPlanAuthorized"), ::OpenAPI::toJsonValue(m_is_plan_authorized));
    }
    if (m_provisioning_state_isSet) {
        obj.insert(QString("provisioningState"), ::OpenAPI::toJsonValue(m_provisioning_state));
    }
    if (m_unique_identifier_isSet) {
        obj.insert(QString("uniqueIdentifier"), ::OpenAPI::toJsonValue(m_unique_identifier));
    }
    return obj;
}

bool OAIGalleryImagePropertiesFragment::isIsEnabled() const {
    return m_is_enabled;
}
void OAIGalleryImagePropertiesFragment::setIsEnabled(const bool &is_enabled) {
    m_is_enabled = is_enabled;
    m_is_enabled_isSet = true;
}

bool OAIGalleryImagePropertiesFragment::is_is_enabled_Set() const{
    return m_is_enabled_isSet;
}

bool OAIGalleryImagePropertiesFragment::is_is_enabled_Valid() const{
    return m_is_enabled_isValid;
}

bool OAIGalleryImagePropertiesFragment::isIsOverride() const {
    return m_is_override;
}
void OAIGalleryImagePropertiesFragment::setIsOverride(const bool &is_override) {
    m_is_override = is_override;
    m_is_override_isSet = true;
}

bool OAIGalleryImagePropertiesFragment::is_is_override_Set() const{
    return m_is_override_isSet;
}

bool OAIGalleryImagePropertiesFragment::is_is_override_Valid() const{
    return m_is_override_isValid;
}

bool OAIGalleryImagePropertiesFragment::isIsPlanAuthorized() const {
    return m_is_plan_authorized;
}
void OAIGalleryImagePropertiesFragment::setIsPlanAuthorized(const bool &is_plan_authorized) {
    m_is_plan_authorized = is_plan_authorized;
    m_is_plan_authorized_isSet = true;
}

bool OAIGalleryImagePropertiesFragment::is_is_plan_authorized_Set() const{
    return m_is_plan_authorized_isSet;
}

bool OAIGalleryImagePropertiesFragment::is_is_plan_authorized_Valid() const{
    return m_is_plan_authorized_isValid;
}

QString OAIGalleryImagePropertiesFragment::getProvisioningState() const {
    return m_provisioning_state;
}
void OAIGalleryImagePropertiesFragment::setProvisioningState(const QString &provisioning_state) {
    m_provisioning_state = provisioning_state;
    m_provisioning_state_isSet = true;
}

bool OAIGalleryImagePropertiesFragment::is_provisioning_state_Set() const{
    return m_provisioning_state_isSet;
}

bool OAIGalleryImagePropertiesFragment::is_provisioning_state_Valid() const{
    return m_provisioning_state_isValid;
}

QString OAIGalleryImagePropertiesFragment::getUniqueIdentifier() const {
    return m_unique_identifier;
}
void OAIGalleryImagePropertiesFragment::setUniqueIdentifier(const QString &unique_identifier) {
    m_unique_identifier = unique_identifier;
    m_unique_identifier_isSet = true;
}

bool OAIGalleryImagePropertiesFragment::is_unique_identifier_Set() const{
    return m_unique_identifier_isSet;
}

bool OAIGalleryImagePropertiesFragment::is_unique_identifier_Valid() const{
    return m_unique_identifier_isValid;
}

bool OAIGalleryImagePropertiesFragment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_override_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_plan_authorized_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_provisioning_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unique_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGalleryImagePropertiesFragment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
