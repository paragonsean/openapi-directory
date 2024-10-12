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

#include "OAIArtistForApiContract.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArtistForApiContract::OAIArtistForApiContract(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArtistForApiContract::OAIArtistForApiContract() {
    this->initializeModel();
}

OAIArtistForApiContract::~OAIArtistForApiContract() {}

void OAIArtistForApiContract::initializeModel() {

    m_additional_names_isSet = false;
    m_additional_names_isValid = false;

    m_artist_links_isSet = false;
    m_artist_links_isValid = false;

    m_artist_links_reverse_isSet = false;
    m_artist_links_reverse_isValid = false;

    m_artist_type_isSet = false;
    m_artist_type_isValid = false;

    m_base_voicebank_isSet = false;
    m_base_voicebank_isValid = false;

    m_create_date_isSet = false;
    m_create_date_isValid = false;

    m_default_name_isSet = false;
    m_default_name_isValid = false;

    m_default_name_language_isSet = false;
    m_default_name_language_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_main_picture_isSet = false;
    m_main_picture_isValid = false;

    m_merged_to_isSet = false;
    m_merged_to_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_names_isSet = false;
    m_names_isValid = false;

    m_picture_mime_isSet = false;
    m_picture_mime_isValid = false;

    m_relations_isSet = false;
    m_relations_isValid = false;

    m_release_date_isSet = false;
    m_release_date_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;

    m_web_links_isSet = false;
    m_web_links_isValid = false;
}

void OAIArtistForApiContract::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArtistForApiContract::fromJsonObject(QJsonObject json) {

    m_additional_names_isValid = ::OpenAPI::fromJsonValue(m_additional_names, json[QString("additionalNames")]);
    m_additional_names_isSet = !json[QString("additionalNames")].isNull() && m_additional_names_isValid;

    m_artist_links_isValid = ::OpenAPI::fromJsonValue(m_artist_links, json[QString("artistLinks")]);
    m_artist_links_isSet = !json[QString("artistLinks")].isNull() && m_artist_links_isValid;

    m_artist_links_reverse_isValid = ::OpenAPI::fromJsonValue(m_artist_links_reverse, json[QString("artistLinksReverse")]);
    m_artist_links_reverse_isSet = !json[QString("artistLinksReverse")].isNull() && m_artist_links_reverse_isValid;

    m_artist_type_isValid = ::OpenAPI::fromJsonValue(m_artist_type, json[QString("artistType")]);
    m_artist_type_isSet = !json[QString("artistType")].isNull() && m_artist_type_isValid;

    m_base_voicebank_isValid = ::OpenAPI::fromJsonValue(m_base_voicebank, json[QString("baseVoicebank")]);
    m_base_voicebank_isSet = !json[QString("baseVoicebank")].isNull() && m_base_voicebank_isValid;

    m_create_date_isValid = ::OpenAPI::fromJsonValue(m_create_date, json[QString("createDate")]);
    m_create_date_isSet = !json[QString("createDate")].isNull() && m_create_date_isValid;

    m_default_name_isValid = ::OpenAPI::fromJsonValue(m_default_name, json[QString("defaultName")]);
    m_default_name_isSet = !json[QString("defaultName")].isNull() && m_default_name_isValid;

    m_default_name_language_isValid = ::OpenAPI::fromJsonValue(m_default_name_language, json[QString("defaultNameLanguage")]);
    m_default_name_language_isSet = !json[QString("defaultNameLanguage")].isNull() && m_default_name_language_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_main_picture_isValid = ::OpenAPI::fromJsonValue(m_main_picture, json[QString("mainPicture")]);
    m_main_picture_isSet = !json[QString("mainPicture")].isNull() && m_main_picture_isValid;

    m_merged_to_isValid = ::OpenAPI::fromJsonValue(m_merged_to, json[QString("mergedTo")]);
    m_merged_to_isSet = !json[QString("mergedTo")].isNull() && m_merged_to_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_names_isValid = ::OpenAPI::fromJsonValue(m_names, json[QString("names")]);
    m_names_isSet = !json[QString("names")].isNull() && m_names_isValid;

    m_picture_mime_isValid = ::OpenAPI::fromJsonValue(m_picture_mime, json[QString("pictureMime")]);
    m_picture_mime_isSet = !json[QString("pictureMime")].isNull() && m_picture_mime_isValid;

    m_relations_isValid = ::OpenAPI::fromJsonValue(m_relations, json[QString("relations")]);
    m_relations_isSet = !json[QString("relations")].isNull() && m_relations_isValid;

    m_release_date_isValid = ::OpenAPI::fromJsonValue(m_release_date, json[QString("releaseDate")]);
    m_release_date_isSet = !json[QString("releaseDate")].isNull() && m_release_date_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;

    m_web_links_isValid = ::OpenAPI::fromJsonValue(m_web_links, json[QString("webLinks")]);
    m_web_links_isSet = !json[QString("webLinks")].isNull() && m_web_links_isValid;
}

QString OAIArtistForApiContract::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArtistForApiContract::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_names_isSet) {
        obj.insert(QString("additionalNames"), ::OpenAPI::toJsonValue(m_additional_names));
    }
    if (m_artist_links.size() > 0) {
        obj.insert(QString("artistLinks"), ::OpenAPI::toJsonValue(m_artist_links));
    }
    if (m_artist_links_reverse.size() > 0) {
        obj.insert(QString("artistLinksReverse"), ::OpenAPI::toJsonValue(m_artist_links_reverse));
    }
    if (m_artist_type.isSet()) {
        obj.insert(QString("artistType"), ::OpenAPI::toJsonValue(m_artist_type));
    }
    if (m_base_voicebank.isSet()) {
        obj.insert(QString("baseVoicebank"), ::OpenAPI::toJsonValue(m_base_voicebank));
    }
    if (m_create_date_isSet) {
        obj.insert(QString("createDate"), ::OpenAPI::toJsonValue(m_create_date));
    }
    if (m_default_name_isSet) {
        obj.insert(QString("defaultName"), ::OpenAPI::toJsonValue(m_default_name));
    }
    if (m_default_name_language.isSet()) {
        obj.insert(QString("defaultNameLanguage"), ::OpenAPI::toJsonValue(m_default_name_language));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_main_picture.isSet()) {
        obj.insert(QString("mainPicture"), ::OpenAPI::toJsonValue(m_main_picture));
    }
    if (m_merged_to_isSet) {
        obj.insert(QString("mergedTo"), ::OpenAPI::toJsonValue(m_merged_to));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_names.size() > 0) {
        obj.insert(QString("names"), ::OpenAPI::toJsonValue(m_names));
    }
    if (m_picture_mime_isSet) {
        obj.insert(QString("pictureMime"), ::OpenAPI::toJsonValue(m_picture_mime));
    }
    if (m_relations.isSet()) {
        obj.insert(QString("relations"), ::OpenAPI::toJsonValue(m_relations));
    }
    if (m_release_date_isSet) {
        obj.insert(QString("releaseDate"), ::OpenAPI::toJsonValue(m_release_date));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    if (m_web_links.size() > 0) {
        obj.insert(QString("webLinks"), ::OpenAPI::toJsonValue(m_web_links));
    }
    return obj;
}

QString OAIArtistForApiContract::getAdditionalNames() const {
    return m_additional_names;
}
void OAIArtistForApiContract::setAdditionalNames(const QString &additional_names) {
    m_additional_names = additional_names;
    m_additional_names_isSet = true;
}

bool OAIArtistForApiContract::is_additional_names_Set() const{
    return m_additional_names_isSet;
}

bool OAIArtistForApiContract::is_additional_names_Valid() const{
    return m_additional_names_isValid;
}

QList<OAIArtistForArtistForApiContract> OAIArtistForApiContract::getArtistLinks() const {
    return m_artist_links;
}
void OAIArtistForApiContract::setArtistLinks(const QList<OAIArtistForArtistForApiContract> &artist_links) {
    m_artist_links = artist_links;
    m_artist_links_isSet = true;
}

bool OAIArtistForApiContract::is_artist_links_Set() const{
    return m_artist_links_isSet;
}

bool OAIArtistForApiContract::is_artist_links_Valid() const{
    return m_artist_links_isValid;
}

QList<OAIArtistForArtistForApiContract> OAIArtistForApiContract::getArtistLinksReverse() const {
    return m_artist_links_reverse;
}
void OAIArtistForApiContract::setArtistLinksReverse(const QList<OAIArtistForArtistForApiContract> &artist_links_reverse) {
    m_artist_links_reverse = artist_links_reverse;
    m_artist_links_reverse_isSet = true;
}

bool OAIArtistForApiContract::is_artist_links_reverse_Set() const{
    return m_artist_links_reverse_isSet;
}

bool OAIArtistForApiContract::is_artist_links_reverse_Valid() const{
    return m_artist_links_reverse_isValid;
}

OAIArtistType OAIArtistForApiContract::getArtistType() const {
    return m_artist_type;
}
void OAIArtistForApiContract::setArtistType(const OAIArtistType &artist_type) {
    m_artist_type = artist_type;
    m_artist_type_isSet = true;
}

bool OAIArtistForApiContract::is_artist_type_Set() const{
    return m_artist_type_isSet;
}

bool OAIArtistForApiContract::is_artist_type_Valid() const{
    return m_artist_type_isValid;
}

OAIArtistContract OAIArtistForApiContract::getBaseVoicebank() const {
    return m_base_voicebank;
}
void OAIArtistForApiContract::setBaseVoicebank(const OAIArtistContract &base_voicebank) {
    m_base_voicebank = base_voicebank;
    m_base_voicebank_isSet = true;
}

bool OAIArtistForApiContract::is_base_voicebank_Set() const{
    return m_base_voicebank_isSet;
}

bool OAIArtistForApiContract::is_base_voicebank_Valid() const{
    return m_base_voicebank_isValid;
}

QDateTime OAIArtistForApiContract::getCreateDate() const {
    return m_create_date;
}
void OAIArtistForApiContract::setCreateDate(const QDateTime &create_date) {
    m_create_date = create_date;
    m_create_date_isSet = true;
}

bool OAIArtistForApiContract::is_create_date_Set() const{
    return m_create_date_isSet;
}

bool OAIArtistForApiContract::is_create_date_Valid() const{
    return m_create_date_isValid;
}

QString OAIArtistForApiContract::getDefaultName() const {
    return m_default_name;
}
void OAIArtistForApiContract::setDefaultName(const QString &default_name) {
    m_default_name = default_name;
    m_default_name_isSet = true;
}

bool OAIArtistForApiContract::is_default_name_Set() const{
    return m_default_name_isSet;
}

bool OAIArtistForApiContract::is_default_name_Valid() const{
    return m_default_name_isValid;
}

OAIContentLanguageSelection OAIArtistForApiContract::getDefaultNameLanguage() const {
    return m_default_name_language;
}
void OAIArtistForApiContract::setDefaultNameLanguage(const OAIContentLanguageSelection &default_name_language) {
    m_default_name_language = default_name_language;
    m_default_name_language_isSet = true;
}

bool OAIArtistForApiContract::is_default_name_language_Set() const{
    return m_default_name_language_isSet;
}

bool OAIArtistForApiContract::is_default_name_language_Valid() const{
    return m_default_name_language_isValid;
}

bool OAIArtistForApiContract::isDeleted() const {
    return m_deleted;
}
void OAIArtistForApiContract::setDeleted(const bool &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIArtistForApiContract::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIArtistForApiContract::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIArtistForApiContract::getDescription() const {
    return m_description;
}
void OAIArtistForApiContract::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIArtistForApiContract::is_description_Set() const{
    return m_description_isSet;
}

bool OAIArtistForApiContract::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIArtistForApiContract::getId() const {
    return m_id;
}
void OAIArtistForApiContract::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIArtistForApiContract::is_id_Set() const{
    return m_id_isSet;
}

bool OAIArtistForApiContract::is_id_Valid() const{
    return m_id_isValid;
}

OAIEntryThumbForApiContract OAIArtistForApiContract::getMainPicture() const {
    return m_main_picture;
}
void OAIArtistForApiContract::setMainPicture(const OAIEntryThumbForApiContract &main_picture) {
    m_main_picture = main_picture;
    m_main_picture_isSet = true;
}

bool OAIArtistForApiContract::is_main_picture_Set() const{
    return m_main_picture_isSet;
}

bool OAIArtistForApiContract::is_main_picture_Valid() const{
    return m_main_picture_isValid;
}

qint32 OAIArtistForApiContract::getMergedTo() const {
    return m_merged_to;
}
void OAIArtistForApiContract::setMergedTo(const qint32 &merged_to) {
    m_merged_to = merged_to;
    m_merged_to_isSet = true;
}

bool OAIArtistForApiContract::is_merged_to_Set() const{
    return m_merged_to_isSet;
}

bool OAIArtistForApiContract::is_merged_to_Valid() const{
    return m_merged_to_isValid;
}

QString OAIArtistForApiContract::getName() const {
    return m_name;
}
void OAIArtistForApiContract::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIArtistForApiContract::is_name_Set() const{
    return m_name_isSet;
}

bool OAIArtistForApiContract::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAILocalizedStringContract> OAIArtistForApiContract::getNames() const {
    return m_names;
}
void OAIArtistForApiContract::setNames(const QList<OAILocalizedStringContract> &names) {
    m_names = names;
    m_names_isSet = true;
}

bool OAIArtistForApiContract::is_names_Set() const{
    return m_names_isSet;
}

bool OAIArtistForApiContract::is_names_Valid() const{
    return m_names_isValid;
}

QString OAIArtistForApiContract::getPictureMime() const {
    return m_picture_mime;
}
void OAIArtistForApiContract::setPictureMime(const QString &picture_mime) {
    m_picture_mime = picture_mime;
    m_picture_mime_isSet = true;
}

bool OAIArtistForApiContract::is_picture_mime_Set() const{
    return m_picture_mime_isSet;
}

bool OAIArtistForApiContract::is_picture_mime_Valid() const{
    return m_picture_mime_isValid;
}

OAIArtistRelationsForApi OAIArtistForApiContract::getRelations() const {
    return m_relations;
}
void OAIArtistForApiContract::setRelations(const OAIArtistRelationsForApi &relations) {
    m_relations = relations;
    m_relations_isSet = true;
}

bool OAIArtistForApiContract::is_relations_Set() const{
    return m_relations_isSet;
}

bool OAIArtistForApiContract::is_relations_Valid() const{
    return m_relations_isValid;
}

QDateTime OAIArtistForApiContract::getReleaseDate() const {
    return m_release_date;
}
void OAIArtistForApiContract::setReleaseDate(const QDateTime &release_date) {
    m_release_date = release_date;
    m_release_date_isSet = true;
}

bool OAIArtistForApiContract::is_release_date_Set() const{
    return m_release_date_isSet;
}

bool OAIArtistForApiContract::is_release_date_Valid() const{
    return m_release_date_isValid;
}

OAIEntryStatus OAIArtistForApiContract::getStatus() const {
    return m_status;
}
void OAIArtistForApiContract::setStatus(const OAIEntryStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIArtistForApiContract::is_status_Set() const{
    return m_status_isSet;
}

bool OAIArtistForApiContract::is_status_Valid() const{
    return m_status_isValid;
}

QList<OAITagUsageForApiContract> OAIArtistForApiContract::getTags() const {
    return m_tags;
}
void OAIArtistForApiContract::setTags(const QList<OAITagUsageForApiContract> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIArtistForApiContract::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIArtistForApiContract::is_tags_Valid() const{
    return m_tags_isValid;
}

qint32 OAIArtistForApiContract::getVersion() const {
    return m_version;
}
void OAIArtistForApiContract::setVersion(const qint32 &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIArtistForApiContract::is_version_Set() const{
    return m_version_isSet;
}

bool OAIArtistForApiContract::is_version_Valid() const{
    return m_version_isValid;
}

QList<OAIWebLinkForApiContract> OAIArtistForApiContract::getWebLinks() const {
    return m_web_links;
}
void OAIArtistForApiContract::setWebLinks(const QList<OAIWebLinkForApiContract> &web_links) {
    m_web_links = web_links;
    m_web_links_isSet = true;
}

bool OAIArtistForApiContract::is_web_links_Set() const{
    return m_web_links_isSet;
}

bool OAIArtistForApiContract::is_web_links_Valid() const{
    return m_web_links_isValid;
}

bool OAIArtistForApiContract::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_names_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_links_reverse.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_voicebank.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_create_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_default_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_default_name_language.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_main_picture.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_merged_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_names.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_picture_mime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relations.isSet()) {
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

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_web_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArtistForApiContract::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
