/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIConfiguration_services_appdotnet_types_profile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConfiguration_services_appdotnet_types_profile::OAIConfiguration_services_appdotnet_types_profile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConfiguration_services_appdotnet_types_profile::OAIConfiguration_services_appdotnet_types_profile() {
    this->initializeModel();
}

OAIConfiguration_services_appdotnet_types_profile::~OAIConfiguration_services_appdotnet_types_profile() {}

void OAIConfiguration_services_appdotnet_types_profile::initializeModel() {

    m_character_limit_isSet = false;
    m_character_limit_isValid = false;

    m_icons_isSet = false;
    m_icons_isValid = false;

    m_link_attachments_isSet = false;
    m_link_attachments_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_schedule_limit_isSet = false;
    m_schedule_limit_isValid = false;

    m_supported_interactions_isSet = false;
    m_supported_interactions_isValid = false;
}

void OAIConfiguration_services_appdotnet_types_profile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConfiguration_services_appdotnet_types_profile::fromJsonObject(QJsonObject json) {

    m_character_limit_isValid = ::OpenAPI::fromJsonValue(m_character_limit, json[QString("character_limit")]);
    m_character_limit_isSet = !json[QString("character_limit")].isNull() && m_character_limit_isValid;

    m_icons_isValid = ::OpenAPI::fromJsonValue(m_icons, json[QString("icons")]);
    m_icons_isSet = !json[QString("icons")].isNull() && m_icons_isValid;

    m_link_attachments_isValid = ::OpenAPI::fromJsonValue(m_link_attachments, json[QString("link_attachments")]);
    m_link_attachments_isSet = !json[QString("link_attachments")].isNull() && m_link_attachments_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_schedule_limit_isValid = ::OpenAPI::fromJsonValue(m_schedule_limit, json[QString("schedule_limit")]);
    m_schedule_limit_isSet = !json[QString("schedule_limit")].isNull() && m_schedule_limit_isValid;

    m_supported_interactions_isValid = ::OpenAPI::fromJsonValue(m_supported_interactions, json[QString("supported_interactions")]);
    m_supported_interactions_isSet = !json[QString("supported_interactions")].isNull() && m_supported_interactions_isValid;
}

QString OAIConfiguration_services_appdotnet_types_profile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConfiguration_services_appdotnet_types_profile::asJsonObject() const {
    QJsonObject obj;
    if (m_character_limit_isSet) {
        obj.insert(QString("character_limit"), ::OpenAPI::toJsonValue(m_character_limit));
    }
    if (m_icons.isSet()) {
        obj.insert(QString("icons"), ::OpenAPI::toJsonValue(m_icons));
    }
    if (m_link_attachments_isSet) {
        obj.insert(QString("link_attachments"), ::OpenAPI::toJsonValue(m_link_attachments));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_schedule_limit_isSet) {
        obj.insert(QString("schedule_limit"), ::OpenAPI::toJsonValue(m_schedule_limit));
    }
    if (m_supported_interactions.size() > 0) {
        obj.insert(QString("supported_interactions"), ::OpenAPI::toJsonValue(m_supported_interactions));
    }
    return obj;
}

double OAIConfiguration_services_appdotnet_types_profile::getCharacterLimit() const {
    return m_character_limit;
}
void OAIConfiguration_services_appdotnet_types_profile::setCharacterLimit(const double &character_limit) {
    m_character_limit = character_limit;
    m_character_limit_isSet = true;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_character_limit_Set() const{
    return m_character_limit_isSet;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_character_limit_Valid() const{
    return m_character_limit_isValid;
}

OAIConfiguration_services_appdotnet_types_profile_icons OAIConfiguration_services_appdotnet_types_profile::getIcons() const {
    return m_icons;
}
void OAIConfiguration_services_appdotnet_types_profile::setIcons(const OAIConfiguration_services_appdotnet_types_profile_icons &icons) {
    m_icons = icons;
    m_icons_isSet = true;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_icons_Set() const{
    return m_icons_isSet;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_icons_Valid() const{
    return m_icons_isValid;
}

bool OAIConfiguration_services_appdotnet_types_profile::isLinkAttachments() const {
    return m_link_attachments;
}
void OAIConfiguration_services_appdotnet_types_profile::setLinkAttachments(const bool &link_attachments) {
    m_link_attachments = link_attachments;
    m_link_attachments_isSet = true;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_link_attachments_Set() const{
    return m_link_attachments_isSet;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_link_attachments_Valid() const{
    return m_link_attachments_isValid;
}

QString OAIConfiguration_services_appdotnet_types_profile::getName() const {
    return m_name;
}
void OAIConfiguration_services_appdotnet_types_profile::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_name_Set() const{
    return m_name_isSet;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_name_Valid() const{
    return m_name_isValid;
}

double OAIConfiguration_services_appdotnet_types_profile::getScheduleLimit() const {
    return m_schedule_limit;
}
void OAIConfiguration_services_appdotnet_types_profile::setScheduleLimit(const double &schedule_limit) {
    m_schedule_limit = schedule_limit;
    m_schedule_limit_isSet = true;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_schedule_limit_Set() const{
    return m_schedule_limit_isSet;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_schedule_limit_Valid() const{
    return m_schedule_limit_isValid;
}

QList<OAIObject> OAIConfiguration_services_appdotnet_types_profile::getSupportedInteractions() const {
    return m_supported_interactions;
}
void OAIConfiguration_services_appdotnet_types_profile::setSupportedInteractions(const QList<OAIObject> &supported_interactions) {
    m_supported_interactions = supported_interactions;
    m_supported_interactions_isSet = true;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_supported_interactions_Set() const{
    return m_supported_interactions_isSet;
}

bool OAIConfiguration_services_appdotnet_types_profile::is_supported_interactions_Valid() const{
    return m_supported_interactions_isValid;
}

bool OAIConfiguration_services_appdotnet_types_profile::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_character_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icons.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_link_attachments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_supported_interactions.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConfiguration_services_appdotnet_types_profile::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
