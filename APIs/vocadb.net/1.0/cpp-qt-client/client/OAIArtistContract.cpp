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

#include "OAIArtistContract.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArtistContract::OAIArtistContract(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArtistContract::OAIArtistContract() {
    this->initializeModel();
}

OAIArtistContract::~OAIArtistContract() {}

void OAIArtistContract::initializeModel() {

    m_additional_names_isSet = false;
    m_additional_names_isValid = false;

    m_artist_type_isSet = false;
    m_artist_type_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_picture_mime_isSet = false;
    m_picture_mime_isValid = false;

    m_release_date_isSet = false;
    m_release_date_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIArtistContract::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArtistContract::fromJsonObject(QJsonObject json) {

    m_additional_names_isValid = ::OpenAPI::fromJsonValue(m_additional_names, json[QString("additionalNames")]);
    m_additional_names_isSet = !json[QString("additionalNames")].isNull() && m_additional_names_isValid;

    m_artist_type_isValid = ::OpenAPI::fromJsonValue(m_artist_type, json[QString("artistType")]);
    m_artist_type_isSet = !json[QString("artistType")].isNull() && m_artist_type_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_picture_mime_isValid = ::OpenAPI::fromJsonValue(m_picture_mime, json[QString("pictureMime")]);
    m_picture_mime_isSet = !json[QString("pictureMime")].isNull() && m_picture_mime_isValid;

    m_release_date_isValid = ::OpenAPI::fromJsonValue(m_release_date, json[QString("releaseDate")]);
    m_release_date_isSet = !json[QString("releaseDate")].isNull() && m_release_date_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIArtistContract::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArtistContract::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_names_isSet) {
        obj.insert(QString("additionalNames"), ::OpenAPI::toJsonValue(m_additional_names));
    }
    if (m_artist_type.isSet()) {
        obj.insert(QString("artistType"), ::OpenAPI::toJsonValue(m_artist_type));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_picture_mime_isSet) {
        obj.insert(QString("pictureMime"), ::OpenAPI::toJsonValue(m_picture_mime));
    }
    if (m_release_date_isSet) {
        obj.insert(QString("releaseDate"), ::OpenAPI::toJsonValue(m_release_date));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QString OAIArtistContract::getAdditionalNames() const {
    return m_additional_names;
}
void OAIArtistContract::setAdditionalNames(const QString &additional_names) {
    m_additional_names = additional_names;
    m_additional_names_isSet = true;
}

bool OAIArtistContract::is_additional_names_Set() const{
    return m_additional_names_isSet;
}

bool OAIArtistContract::is_additional_names_Valid() const{
    return m_additional_names_isValid;
}

OAIArtistType OAIArtistContract::getArtistType() const {
    return m_artist_type;
}
void OAIArtistContract::setArtistType(const OAIArtistType &artist_type) {
    m_artist_type = artist_type;
    m_artist_type_isSet = true;
}

bool OAIArtistContract::is_artist_type_Set() const{
    return m_artist_type_isSet;
}

bool OAIArtistContract::is_artist_type_Valid() const{
    return m_artist_type_isValid;
}

bool OAIArtistContract::isDeleted() const {
    return m_deleted;
}
void OAIArtistContract::setDeleted(const bool &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIArtistContract::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIArtistContract::is_deleted_Valid() const{
    return m_deleted_isValid;
}

qint32 OAIArtistContract::getId() const {
    return m_id;
}
void OAIArtistContract::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIArtistContract::is_id_Set() const{
    return m_id_isSet;
}

bool OAIArtistContract::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIArtistContract::getName() const {
    return m_name;
}
void OAIArtistContract::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIArtistContract::is_name_Set() const{
    return m_name_isSet;
}

bool OAIArtistContract::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIArtistContract::getPictureMime() const {
    return m_picture_mime;
}
void OAIArtistContract::setPictureMime(const QString &picture_mime) {
    m_picture_mime = picture_mime;
    m_picture_mime_isSet = true;
}

bool OAIArtistContract::is_picture_mime_Set() const{
    return m_picture_mime_isSet;
}

bool OAIArtistContract::is_picture_mime_Valid() const{
    return m_picture_mime_isValid;
}

QDateTime OAIArtistContract::getReleaseDate() const {
    return m_release_date;
}
void OAIArtistContract::setReleaseDate(const QDateTime &release_date) {
    m_release_date = release_date;
    m_release_date_isSet = true;
}

bool OAIArtistContract::is_release_date_Set() const{
    return m_release_date_isSet;
}

bool OAIArtistContract::is_release_date_Valid() const{
    return m_release_date_isValid;
}

OAIEntryStatus OAIArtistContract::getStatus() const {
    return m_status;
}
void OAIArtistContract::setStatus(const OAIEntryStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIArtistContract::is_status_Set() const{
    return m_status_isSet;
}

bool OAIArtistContract::is_status_Valid() const{
    return m_status_isValid;
}

qint32 OAIArtistContract::getVersion() const {
    return m_version;
}
void OAIArtistContract::setVersion(const qint32 &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIArtistContract::is_version_Set() const{
    return m_version_isSet;
}

bool OAIArtistContract::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIArtistContract::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_names_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_picture_mime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArtistContract::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
