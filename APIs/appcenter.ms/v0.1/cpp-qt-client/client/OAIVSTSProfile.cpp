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

#include "OAIVSTSProfile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVSTSProfile::OAIVSTSProfile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVSTSProfile::OAIVSTSProfile() {
    this->initializeModel();
}

OAIVSTSProfile::~OAIVSTSProfile() {}

void OAIVSTSProfile::initializeModel() {

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_email_address_isSet = false;
    m_email_address_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_public_alias_isSet = false;
    m_public_alias_isValid = false;
}

void OAIVSTSProfile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVSTSProfile::fromJsonObject(QJsonObject json) {

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_email_address_isValid = ::OpenAPI::fromJsonValue(m_email_address, json[QString("emailAddress")]);
    m_email_address_isSet = !json[QString("emailAddress")].isNull() && m_email_address_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_public_alias_isValid = ::OpenAPI::fromJsonValue(m_public_alias, json[QString("publicAlias")]);
    m_public_alias_isSet = !json[QString("publicAlias")].isNull() && m_public_alias_isValid;
}

QString OAIVSTSProfile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVSTSProfile::asJsonObject() const {
    QJsonObject obj;
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_email_address_isSet) {
        obj.insert(QString("emailAddress"), ::OpenAPI::toJsonValue(m_email_address));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_public_alias_isSet) {
        obj.insert(QString("publicAlias"), ::OpenAPI::toJsonValue(m_public_alias));
    }
    return obj;
}

QString OAIVSTSProfile::getDisplayName() const {
    return m_display_name;
}
void OAIVSTSProfile::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIVSTSProfile::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIVSTSProfile::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIVSTSProfile::getEmailAddress() const {
    return m_email_address;
}
void OAIVSTSProfile::setEmailAddress(const QString &email_address) {
    m_email_address = email_address;
    m_email_address_isSet = true;
}

bool OAIVSTSProfile::is_email_address_Set() const{
    return m_email_address_isSet;
}

bool OAIVSTSProfile::is_email_address_Valid() const{
    return m_email_address_isValid;
}

QString OAIVSTSProfile::getId() const {
    return m_id;
}
void OAIVSTSProfile::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVSTSProfile::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVSTSProfile::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIVSTSProfile::getPublicAlias() const {
    return m_public_alias;
}
void OAIVSTSProfile::setPublicAlias(const QString &public_alias) {
    m_public_alias = public_alias;
    m_public_alias_isSet = true;
}

bool OAIVSTSProfile::is_public_alias_Set() const{
    return m_public_alias_isSet;
}

bool OAIVSTSProfile::is_public_alias_Valid() const{
    return m_public_alias_isValid;
}

bool OAIVSTSProfile::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_alias_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVSTSProfile::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
