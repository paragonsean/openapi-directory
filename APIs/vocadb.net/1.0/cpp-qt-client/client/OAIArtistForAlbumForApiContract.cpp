/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArtistForAlbumForApiContract.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArtistForAlbumForApiContract::OAIArtistForAlbumForApiContract(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArtistForAlbumForApiContract::OAIArtistForAlbumForApiContract() {
    this->initializeModel();
}

OAIArtistForAlbumForApiContract::~OAIArtistForAlbumForApiContract() {}

void OAIArtistForAlbumForApiContract::initializeModel() {

    m_artist_isSet = false;
    m_artist_isValid = false;

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_effective_roles_isSet = false;
    m_effective_roles_isValid = false;

    m_is_support_isSet = false;
    m_is_support_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_roles_isSet = false;
    m_roles_isValid = false;
}

void OAIArtistForAlbumForApiContract::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArtistForAlbumForApiContract::fromJsonObject(QJsonObject json) {

    m_artist_isValid = ::OpenAPI::fromJsonValue(m_artist, json[QString("artist")]);
    m_artist_isSet = !json[QString("artist")].isNull() && m_artist_isValid;

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("categories")]);
    m_categories_isSet = !json[QString("categories")].isNull() && m_categories_isValid;

    m_effective_roles_isValid = ::OpenAPI::fromJsonValue(m_effective_roles, json[QString("effectiveRoles")]);
    m_effective_roles_isSet = !json[QString("effectiveRoles")].isNull() && m_effective_roles_isValid;

    m_is_support_isValid = ::OpenAPI::fromJsonValue(m_is_support, json[QString("isSupport")]);
    m_is_support_isSet = !json[QString("isSupport")].isNull() && m_is_support_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_roles_isValid = ::OpenAPI::fromJsonValue(m_roles, json[QString("roles")]);
    m_roles_isSet = !json[QString("roles")].isNull() && m_roles_isValid;
}

QString OAIArtistForAlbumForApiContract::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArtistForAlbumForApiContract::asJsonObject() const {
    QJsonObject obj;
    if (m_artist.isSet()) {
        obj.insert(QString("artist"), ::OpenAPI::toJsonValue(m_artist));
    }
    if (m_categories.isSet()) {
        obj.insert(QString("categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_effective_roles.isSet()) {
        obj.insert(QString("effectiveRoles"), ::OpenAPI::toJsonValue(m_effective_roles));
    }
    if (m_is_support_isSet) {
        obj.insert(QString("isSupport"), ::OpenAPI::toJsonValue(m_is_support));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_roles.isSet()) {
        obj.insert(QString("roles"), ::OpenAPI::toJsonValue(m_roles));
    }
    return obj;
}

OAIArtistContract OAIArtistForAlbumForApiContract::getArtist() const {
    return m_artist;
}
void OAIArtistForAlbumForApiContract::setArtist(const OAIArtistContract &artist) {
    m_artist = artist;
    m_artist_isSet = true;
}

bool OAIArtistForAlbumForApiContract::is_artist_Set() const{
    return m_artist_isSet;
}

bool OAIArtistForAlbumForApiContract::is_artist_Valid() const{
    return m_artist_isValid;
}

OAIArtistCategories OAIArtistForAlbumForApiContract::getCategories() const {
    return m_categories;
}
void OAIArtistForAlbumForApiContract::setCategories(const OAIArtistCategories &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIArtistForAlbumForApiContract::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIArtistForAlbumForApiContract::is_categories_Valid() const{
    return m_categories_isValid;
}

OAIArtistRoles OAIArtistForAlbumForApiContract::getEffectiveRoles() const {
    return m_effective_roles;
}
void OAIArtistForAlbumForApiContract::setEffectiveRoles(const OAIArtistRoles &effective_roles) {
    m_effective_roles = effective_roles;
    m_effective_roles_isSet = true;
}

bool OAIArtistForAlbumForApiContract::is_effective_roles_Set() const{
    return m_effective_roles_isSet;
}

bool OAIArtistForAlbumForApiContract::is_effective_roles_Valid() const{
    return m_effective_roles_isValid;
}

bool OAIArtistForAlbumForApiContract::isIsSupport() const {
    return m_is_support;
}
void OAIArtistForAlbumForApiContract::setIsSupport(const bool &is_support) {
    m_is_support = is_support;
    m_is_support_isSet = true;
}

bool OAIArtistForAlbumForApiContract::is_is_support_Set() const{
    return m_is_support_isSet;
}

bool OAIArtistForAlbumForApiContract::is_is_support_Valid() const{
    return m_is_support_isValid;
}

QString OAIArtistForAlbumForApiContract::getName() const {
    return m_name;
}
void OAIArtistForAlbumForApiContract::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIArtistForAlbumForApiContract::is_name_Set() const{
    return m_name_isSet;
}

bool OAIArtistForAlbumForApiContract::is_name_Valid() const{
    return m_name_isValid;
}

OAIArtistRoles OAIArtistForAlbumForApiContract::getRoles() const {
    return m_roles;
}
void OAIArtistForAlbumForApiContract::setRoles(const OAIArtistRoles &roles) {
    m_roles = roles;
    m_roles_isSet = true;
}

bool OAIArtistForAlbumForApiContract::is_roles_Set() const{
    return m_roles_isSet;
}

bool OAIArtistForAlbumForApiContract::is_roles_Valid() const{
    return m_roles_isValid;
}

bool OAIArtistForAlbumForApiContract::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_artist.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_effective_roles.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_support_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_roles.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArtistForAlbumForApiContract::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
