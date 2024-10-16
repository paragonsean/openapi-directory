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

#include "OAIGetNetworkSmUsers_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkSmUsers_200_response_inner::OAIGetNetworkSmUsers_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkSmUsers_200_response_inner::OAIGetNetworkSmUsers_200_response_inner() {
    this->initializeModel();
}

OAIGetNetworkSmUsers_200_response_inner::~OAIGetNetworkSmUsers_200_response_inner() {}

void OAIGetNetworkSmUsers_200_response_inner::initializeModel() {

    m_ad_groups_isSet = false;
    m_ad_groups_isValid = false;

    m_asm_groups_isSet = false;
    m_asm_groups_isValid = false;

    m_azure_ad_groups_isSet = false;
    m_azure_ad_groups_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_full_name_isSet = false;
    m_full_name_isValid = false;

    m_has_identity_certificate_isSet = false;
    m_has_identity_certificate_isValid = false;

    m_has_password_isSet = false;
    m_has_password_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_external_isSet = false;
    m_is_external_isValid = false;

    m_saml_groups_isSet = false;
    m_saml_groups_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_user_thumbnail_isSet = false;
    m_user_thumbnail_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIGetNetworkSmUsers_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkSmUsers_200_response_inner::fromJsonObject(QJsonObject json) {

    m_ad_groups_isValid = ::OpenAPI::fromJsonValue(m_ad_groups, json[QString("adGroups")]);
    m_ad_groups_isSet = !json[QString("adGroups")].isNull() && m_ad_groups_isValid;

    m_asm_groups_isValid = ::OpenAPI::fromJsonValue(m_asm_groups, json[QString("asmGroups")]);
    m_asm_groups_isSet = !json[QString("asmGroups")].isNull() && m_asm_groups_isValid;

    m_azure_ad_groups_isValid = ::OpenAPI::fromJsonValue(m_azure_ad_groups, json[QString("azureAdGroups")]);
    m_azure_ad_groups_isSet = !json[QString("azureAdGroups")].isNull() && m_azure_ad_groups_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_full_name_isValid = ::OpenAPI::fromJsonValue(m_full_name, json[QString("fullName")]);
    m_full_name_isSet = !json[QString("fullName")].isNull() && m_full_name_isValid;

    m_has_identity_certificate_isValid = ::OpenAPI::fromJsonValue(m_has_identity_certificate, json[QString("hasIdentityCertificate")]);
    m_has_identity_certificate_isSet = !json[QString("hasIdentityCertificate")].isNull() && m_has_identity_certificate_isValid;

    m_has_password_isValid = ::OpenAPI::fromJsonValue(m_has_password, json[QString("hasPassword")]);
    m_has_password_isSet = !json[QString("hasPassword")].isNull() && m_has_password_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_external_isValid = ::OpenAPI::fromJsonValue(m_is_external, json[QString("isExternal")]);
    m_is_external_isSet = !json[QString("isExternal")].isNull() && m_is_external_isValid;

    m_saml_groups_isValid = ::OpenAPI::fromJsonValue(m_saml_groups, json[QString("samlGroups")]);
    m_saml_groups_isSet = !json[QString("samlGroups")].isNull() && m_saml_groups_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_user_thumbnail_isValid = ::OpenAPI::fromJsonValue(m_user_thumbnail, json[QString("userThumbnail")]);
    m_user_thumbnail_isSet = !json[QString("userThumbnail")].isNull() && m_user_thumbnail_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIGetNetworkSmUsers_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkSmUsers_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_ad_groups.size() > 0) {
        obj.insert(QString("adGroups"), ::OpenAPI::toJsonValue(m_ad_groups));
    }
    if (m_asm_groups.size() > 0) {
        obj.insert(QString("asmGroups"), ::OpenAPI::toJsonValue(m_asm_groups));
    }
    if (m_azure_ad_groups.size() > 0) {
        obj.insert(QString("azureAdGroups"), ::OpenAPI::toJsonValue(m_azure_ad_groups));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_full_name_isSet) {
        obj.insert(QString("fullName"), ::OpenAPI::toJsonValue(m_full_name));
    }
    if (m_has_identity_certificate_isSet) {
        obj.insert(QString("hasIdentityCertificate"), ::OpenAPI::toJsonValue(m_has_identity_certificate));
    }
    if (m_has_password_isSet) {
        obj.insert(QString("hasPassword"), ::OpenAPI::toJsonValue(m_has_password));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_external_isSet) {
        obj.insert(QString("isExternal"), ::OpenAPI::toJsonValue(m_is_external));
    }
    if (m_saml_groups.size() > 0) {
        obj.insert(QString("samlGroups"), ::OpenAPI::toJsonValue(m_saml_groups));
    }
    if (m_tags_isSet) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_user_thumbnail_isSet) {
        obj.insert(QString("userThumbnail"), ::OpenAPI::toJsonValue(m_user_thumbnail));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QList<QString> OAIGetNetworkSmUsers_200_response_inner::getAdGroups() const {
    return m_ad_groups;
}
void OAIGetNetworkSmUsers_200_response_inner::setAdGroups(const QList<QString> &ad_groups) {
    m_ad_groups = ad_groups;
    m_ad_groups_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_ad_groups_Set() const{
    return m_ad_groups_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_ad_groups_Valid() const{
    return m_ad_groups_isValid;
}

QList<QString> OAIGetNetworkSmUsers_200_response_inner::getAsmGroups() const {
    return m_asm_groups;
}
void OAIGetNetworkSmUsers_200_response_inner::setAsmGroups(const QList<QString> &asm_groups) {
    m_asm_groups = asm_groups;
    m_asm_groups_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_asm_groups_Set() const{
    return m_asm_groups_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_asm_groups_Valid() const{
    return m_asm_groups_isValid;
}

QList<QString> OAIGetNetworkSmUsers_200_response_inner::getAzureAdGroups() const {
    return m_azure_ad_groups;
}
void OAIGetNetworkSmUsers_200_response_inner::setAzureAdGroups(const QList<QString> &azure_ad_groups) {
    m_azure_ad_groups = azure_ad_groups;
    m_azure_ad_groups_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_azure_ad_groups_Set() const{
    return m_azure_ad_groups_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_azure_ad_groups_Valid() const{
    return m_azure_ad_groups_isValid;
}

QString OAIGetNetworkSmUsers_200_response_inner::getDisplayName() const {
    return m_display_name;
}
void OAIGetNetworkSmUsers_200_response_inner::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIGetNetworkSmUsers_200_response_inner::getEmail() const {
    return m_email;
}
void OAIGetNetworkSmUsers_200_response_inner::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_email_Set() const{
    return m_email_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIGetNetworkSmUsers_200_response_inner::getFullName() const {
    return m_full_name;
}
void OAIGetNetworkSmUsers_200_response_inner::setFullName(const QString &full_name) {
    m_full_name = full_name;
    m_full_name_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_full_name_Set() const{
    return m_full_name_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_full_name_Valid() const{
    return m_full_name_isValid;
}

bool OAIGetNetworkSmUsers_200_response_inner::isHasIdentityCertificate() const {
    return m_has_identity_certificate;
}
void OAIGetNetworkSmUsers_200_response_inner::setHasIdentityCertificate(const bool &has_identity_certificate) {
    m_has_identity_certificate = has_identity_certificate;
    m_has_identity_certificate_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_has_identity_certificate_Set() const{
    return m_has_identity_certificate_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_has_identity_certificate_Valid() const{
    return m_has_identity_certificate_isValid;
}

bool OAIGetNetworkSmUsers_200_response_inner::isHasPassword() const {
    return m_has_password;
}
void OAIGetNetworkSmUsers_200_response_inner::setHasPassword(const bool &has_password) {
    m_has_password = has_password;
    m_has_password_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_has_password_Set() const{
    return m_has_password_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_has_password_Valid() const{
    return m_has_password_isValid;
}

QString OAIGetNetworkSmUsers_200_response_inner::getId() const {
    return m_id;
}
void OAIGetNetworkSmUsers_200_response_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIGetNetworkSmUsers_200_response_inner::isIsExternal() const {
    return m_is_external;
}
void OAIGetNetworkSmUsers_200_response_inner::setIsExternal(const bool &is_external) {
    m_is_external = is_external;
    m_is_external_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_is_external_Set() const{
    return m_is_external_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_is_external_Valid() const{
    return m_is_external_isValid;
}

QList<QString> OAIGetNetworkSmUsers_200_response_inner::getSamlGroups() const {
    return m_saml_groups;
}
void OAIGetNetworkSmUsers_200_response_inner::setSamlGroups(const QList<QString> &saml_groups) {
    m_saml_groups = saml_groups;
    m_saml_groups_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_saml_groups_Set() const{
    return m_saml_groups_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_saml_groups_Valid() const{
    return m_saml_groups_isValid;
}

QString OAIGetNetworkSmUsers_200_response_inner::getTags() const {
    return m_tags;
}
void OAIGetNetworkSmUsers_200_response_inner::setTags(const QString &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIGetNetworkSmUsers_200_response_inner::getUserThumbnail() const {
    return m_user_thumbnail;
}
void OAIGetNetworkSmUsers_200_response_inner::setUserThumbnail(const QString &user_thumbnail) {
    m_user_thumbnail = user_thumbnail;
    m_user_thumbnail_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_user_thumbnail_Set() const{
    return m_user_thumbnail_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_user_thumbnail_Valid() const{
    return m_user_thumbnail_isValid;
}

QString OAIGetNetworkSmUsers_200_response_inner::getUsername() const {
    return m_username;
}
void OAIGetNetworkSmUsers_200_response_inner::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_username_Set() const{
    return m_username_isSet;
}

bool OAIGetNetworkSmUsers_200_response_inner::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIGetNetworkSmUsers_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ad_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_asm_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_azure_ad_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_full_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_identity_certificate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_external_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_saml_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_thumbnail_isSet) {
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

bool OAIGetNetworkSmUsers_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
