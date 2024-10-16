/**
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEpisodeBase.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEpisodeBase::OAIEpisodeBase(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEpisodeBase::OAIEpisodeBase() {
    this->initializeModel();
}

OAIEpisodeBase::~OAIEpisodeBase() {}

void OAIEpisodeBase::initializeModel() {

    m_audio_preview_url_isSet = false;
    m_audio_preview_url_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_duration_ms_isSet = false;
    m_duration_ms_isValid = false;

    m_r_explicit_isSet = false;
    m_r_explicit_isValid = false;

    m_external_urls_isSet = false;
    m_external_urls_isValid = false;

    m_href_isSet = false;
    m_href_isValid = false;

    m_html_description_isSet = false;
    m_html_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_images_isSet = false;
    m_images_isValid = false;

    m_is_externally_hosted_isSet = false;
    m_is_externally_hosted_isValid = false;

    m_is_playable_isSet = false;
    m_is_playable_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_languages_isSet = false;
    m_languages_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_release_date_isSet = false;
    m_release_date_isValid = false;

    m_release_date_precision_isSet = false;
    m_release_date_precision_isValid = false;

    m_restrictions_isSet = false;
    m_restrictions_isValid = false;

    m_resume_point_isSet = false;
    m_resume_point_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_uri_isSet = false;
    m_uri_isValid = false;
}

void OAIEpisodeBase::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEpisodeBase::fromJsonObject(QJsonObject json) {

    m_audio_preview_url_isValid = ::OpenAPI::fromJsonValue(m_audio_preview_url, json[QString("audio_preview_url")]);
    m_audio_preview_url_isSet = !json[QString("audio_preview_url")].isNull() && m_audio_preview_url_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_duration_ms_isValid = ::OpenAPI::fromJsonValue(m_duration_ms, json[QString("duration_ms")]);
    m_duration_ms_isSet = !json[QString("duration_ms")].isNull() && m_duration_ms_isValid;

    m_r_explicit_isValid = ::OpenAPI::fromJsonValue(m_r_explicit, json[QString("explicit")]);
    m_r_explicit_isSet = !json[QString("explicit")].isNull() && m_r_explicit_isValid;

    m_external_urls_isValid = ::OpenAPI::fromJsonValue(m_external_urls, json[QString("external_urls")]);
    m_external_urls_isSet = !json[QString("external_urls")].isNull() && m_external_urls_isValid;

    m_href_isValid = ::OpenAPI::fromJsonValue(m_href, json[QString("href")]);
    m_href_isSet = !json[QString("href")].isNull() && m_href_isValid;

    m_html_description_isValid = ::OpenAPI::fromJsonValue(m_html_description, json[QString("html_description")]);
    m_html_description_isSet = !json[QString("html_description")].isNull() && m_html_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_images_isValid = ::OpenAPI::fromJsonValue(m_images, json[QString("images")]);
    m_images_isSet = !json[QString("images")].isNull() && m_images_isValid;

    m_is_externally_hosted_isValid = ::OpenAPI::fromJsonValue(m_is_externally_hosted, json[QString("is_externally_hosted")]);
    m_is_externally_hosted_isSet = !json[QString("is_externally_hosted")].isNull() && m_is_externally_hosted_isValid;

    m_is_playable_isValid = ::OpenAPI::fromJsonValue(m_is_playable, json[QString("is_playable")]);
    m_is_playable_isSet = !json[QString("is_playable")].isNull() && m_is_playable_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_languages_isValid = ::OpenAPI::fromJsonValue(m_languages, json[QString("languages")]);
    m_languages_isSet = !json[QString("languages")].isNull() && m_languages_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_release_date_isValid = ::OpenAPI::fromJsonValue(m_release_date, json[QString("release_date")]);
    m_release_date_isSet = !json[QString("release_date")].isNull() && m_release_date_isValid;

    m_release_date_precision_isValid = ::OpenAPI::fromJsonValue(m_release_date_precision, json[QString("release_date_precision")]);
    m_release_date_precision_isSet = !json[QString("release_date_precision")].isNull() && m_release_date_precision_isValid;

    m_restrictions_isValid = ::OpenAPI::fromJsonValue(m_restrictions, json[QString("restrictions")]);
    m_restrictions_isSet = !json[QString("restrictions")].isNull() && m_restrictions_isValid;

    m_resume_point_isValid = ::OpenAPI::fromJsonValue(m_resume_point, json[QString("resume_point")]);
    m_resume_point_isSet = !json[QString("resume_point")].isNull() && m_resume_point_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_uri_isValid = ::OpenAPI::fromJsonValue(m_uri, json[QString("uri")]);
    m_uri_isSet = !json[QString("uri")].isNull() && m_uri_isValid;
}

QString OAIEpisodeBase::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEpisodeBase::asJsonObject() const {
    QJsonObject obj;
    if (m_audio_preview_url_isSet) {
        obj.insert(QString("audio_preview_url"), ::OpenAPI::toJsonValue(m_audio_preview_url));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_duration_ms_isSet) {
        obj.insert(QString("duration_ms"), ::OpenAPI::toJsonValue(m_duration_ms));
    }
    if (m_r_explicit_isSet) {
        obj.insert(QString("explicit"), ::OpenAPI::toJsonValue(m_r_explicit));
    }
    if (m_external_urls.isSet()) {
        obj.insert(QString("external_urls"), ::OpenAPI::toJsonValue(m_external_urls));
    }
    if (m_href_isSet) {
        obj.insert(QString("href"), ::OpenAPI::toJsonValue(m_href));
    }
    if (m_html_description_isSet) {
        obj.insert(QString("html_description"), ::OpenAPI::toJsonValue(m_html_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_images.size() > 0) {
        obj.insert(QString("images"), ::OpenAPI::toJsonValue(m_images));
    }
    if (m_is_externally_hosted_isSet) {
        obj.insert(QString("is_externally_hosted"), ::OpenAPI::toJsonValue(m_is_externally_hosted));
    }
    if (m_is_playable_isSet) {
        obj.insert(QString("is_playable"), ::OpenAPI::toJsonValue(m_is_playable));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_languages.size() > 0) {
        obj.insert(QString("languages"), ::OpenAPI::toJsonValue(m_languages));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_release_date_isSet) {
        obj.insert(QString("release_date"), ::OpenAPI::toJsonValue(m_release_date));
    }
    if (m_release_date_precision_isSet) {
        obj.insert(QString("release_date_precision"), ::OpenAPI::toJsonValue(m_release_date_precision));
    }
    if (m_restrictions.isSet()) {
        obj.insert(QString("restrictions"), ::OpenAPI::toJsonValue(m_restrictions));
    }
    if (m_resume_point.isSet()) {
        obj.insert(QString("resume_point"), ::OpenAPI::toJsonValue(m_resume_point));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_uri_isSet) {
        obj.insert(QString("uri"), ::OpenAPI::toJsonValue(m_uri));
    }
    return obj;
}

QString OAIEpisodeBase::getAudioPreviewUrl() const {
    return m_audio_preview_url;
}
void OAIEpisodeBase::setAudioPreviewUrl(const QString &audio_preview_url) {
    m_audio_preview_url = audio_preview_url;
    m_audio_preview_url_isSet = true;
}

bool OAIEpisodeBase::is_audio_preview_url_Set() const{
    return m_audio_preview_url_isSet;
}

bool OAIEpisodeBase::is_audio_preview_url_Valid() const{
    return m_audio_preview_url_isValid;
}

QString OAIEpisodeBase::getDescription() const {
    return m_description;
}
void OAIEpisodeBase::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIEpisodeBase::is_description_Set() const{
    return m_description_isSet;
}

bool OAIEpisodeBase::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIEpisodeBase::getDurationMs() const {
    return m_duration_ms;
}
void OAIEpisodeBase::setDurationMs(const qint32 &duration_ms) {
    m_duration_ms = duration_ms;
    m_duration_ms_isSet = true;
}

bool OAIEpisodeBase::is_duration_ms_Set() const{
    return m_duration_ms_isSet;
}

bool OAIEpisodeBase::is_duration_ms_Valid() const{
    return m_duration_ms_isValid;
}

bool OAIEpisodeBase::isRExplicit() const {
    return m_r_explicit;
}
void OAIEpisodeBase::setRExplicit(const bool &r_explicit) {
    m_r_explicit = r_explicit;
    m_r_explicit_isSet = true;
}

bool OAIEpisodeBase::is_r_explicit_Set() const{
    return m_r_explicit_isSet;
}

bool OAIEpisodeBase::is_r_explicit_Valid() const{
    return m_r_explicit_isValid;
}

OAIExternalUrlObject OAIEpisodeBase::getExternalUrls() const {
    return m_external_urls;
}
void OAIEpisodeBase::setExternalUrls(const OAIExternalUrlObject &external_urls) {
    m_external_urls = external_urls;
    m_external_urls_isSet = true;
}

bool OAIEpisodeBase::is_external_urls_Set() const{
    return m_external_urls_isSet;
}

bool OAIEpisodeBase::is_external_urls_Valid() const{
    return m_external_urls_isValid;
}

QString OAIEpisodeBase::getHref() const {
    return m_href;
}
void OAIEpisodeBase::setHref(const QString &href) {
    m_href = href;
    m_href_isSet = true;
}

bool OAIEpisodeBase::is_href_Set() const{
    return m_href_isSet;
}

bool OAIEpisodeBase::is_href_Valid() const{
    return m_href_isValid;
}

QString OAIEpisodeBase::getHtmlDescription() const {
    return m_html_description;
}
void OAIEpisodeBase::setHtmlDescription(const QString &html_description) {
    m_html_description = html_description;
    m_html_description_isSet = true;
}

bool OAIEpisodeBase::is_html_description_Set() const{
    return m_html_description_isSet;
}

bool OAIEpisodeBase::is_html_description_Valid() const{
    return m_html_description_isValid;
}

QString OAIEpisodeBase::getId() const {
    return m_id;
}
void OAIEpisodeBase::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIEpisodeBase::is_id_Set() const{
    return m_id_isSet;
}

bool OAIEpisodeBase::is_id_Valid() const{
    return m_id_isValid;
}

QList<OAIImageObject> OAIEpisodeBase::getImages() const {
    return m_images;
}
void OAIEpisodeBase::setImages(const QList<OAIImageObject> &images) {
    m_images = images;
    m_images_isSet = true;
}

bool OAIEpisodeBase::is_images_Set() const{
    return m_images_isSet;
}

bool OAIEpisodeBase::is_images_Valid() const{
    return m_images_isValid;
}

bool OAIEpisodeBase::isIsExternallyHosted() const {
    return m_is_externally_hosted;
}
void OAIEpisodeBase::setIsExternallyHosted(const bool &is_externally_hosted) {
    m_is_externally_hosted = is_externally_hosted;
    m_is_externally_hosted_isSet = true;
}

bool OAIEpisodeBase::is_is_externally_hosted_Set() const{
    return m_is_externally_hosted_isSet;
}

bool OAIEpisodeBase::is_is_externally_hosted_Valid() const{
    return m_is_externally_hosted_isValid;
}

bool OAIEpisodeBase::isIsPlayable() const {
    return m_is_playable;
}
void OAIEpisodeBase::setIsPlayable(const bool &is_playable) {
    m_is_playable = is_playable;
    m_is_playable_isSet = true;
}

bool OAIEpisodeBase::is_is_playable_Set() const{
    return m_is_playable_isSet;
}

bool OAIEpisodeBase::is_is_playable_Valid() const{
    return m_is_playable_isValid;
}

QString OAIEpisodeBase::getLanguage() const {
    return m_language;
}
void OAIEpisodeBase::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIEpisodeBase::is_language_Set() const{
    return m_language_isSet;
}

bool OAIEpisodeBase::is_language_Valid() const{
    return m_language_isValid;
}

QList<QString> OAIEpisodeBase::getLanguages() const {
    return m_languages;
}
void OAIEpisodeBase::setLanguages(const QList<QString> &languages) {
    m_languages = languages;
    m_languages_isSet = true;
}

bool OAIEpisodeBase::is_languages_Set() const{
    return m_languages_isSet;
}

bool OAIEpisodeBase::is_languages_Valid() const{
    return m_languages_isValid;
}

QString OAIEpisodeBase::getName() const {
    return m_name;
}
void OAIEpisodeBase::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIEpisodeBase::is_name_Set() const{
    return m_name_isSet;
}

bool OAIEpisodeBase::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIEpisodeBase::getReleaseDate() const {
    return m_release_date;
}
void OAIEpisodeBase::setReleaseDate(const QString &release_date) {
    m_release_date = release_date;
    m_release_date_isSet = true;
}

bool OAIEpisodeBase::is_release_date_Set() const{
    return m_release_date_isSet;
}

bool OAIEpisodeBase::is_release_date_Valid() const{
    return m_release_date_isValid;
}

QString OAIEpisodeBase::getReleaseDatePrecision() const {
    return m_release_date_precision;
}
void OAIEpisodeBase::setReleaseDatePrecision(const QString &release_date_precision) {
    m_release_date_precision = release_date_precision;
    m_release_date_precision_isSet = true;
}

bool OAIEpisodeBase::is_release_date_precision_Set() const{
    return m_release_date_precision_isSet;
}

bool OAIEpisodeBase::is_release_date_precision_Valid() const{
    return m_release_date_precision_isValid;
}

OAIEpisodeRestrictionObject OAIEpisodeBase::getRestrictions() const {
    return m_restrictions;
}
void OAIEpisodeBase::setRestrictions(const OAIEpisodeRestrictionObject &restrictions) {
    m_restrictions = restrictions;
    m_restrictions_isSet = true;
}

bool OAIEpisodeBase::is_restrictions_Set() const{
    return m_restrictions_isSet;
}

bool OAIEpisodeBase::is_restrictions_Valid() const{
    return m_restrictions_isValid;
}

OAIResumePointObject OAIEpisodeBase::getResumePoint() const {
    return m_resume_point;
}
void OAIEpisodeBase::setResumePoint(const OAIResumePointObject &resume_point) {
    m_resume_point = resume_point;
    m_resume_point_isSet = true;
}

bool OAIEpisodeBase::is_resume_point_Set() const{
    return m_resume_point_isSet;
}

bool OAIEpisodeBase::is_resume_point_Valid() const{
    return m_resume_point_isValid;
}

QString OAIEpisodeBase::getType() const {
    return m_type;
}
void OAIEpisodeBase::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIEpisodeBase::is_type_Set() const{
    return m_type_isSet;
}

bool OAIEpisodeBase::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIEpisodeBase::getUri() const {
    return m_uri;
}
void OAIEpisodeBase::setUri(const QString &uri) {
    m_uri = uri;
    m_uri_isSet = true;
}

bool OAIEpisodeBase::is_uri_Set() const{
    return m_uri_isSet;
}

bool OAIEpisodeBase::is_uri_Valid() const{
    return m_uri_isValid;
}

bool OAIEpisodeBase::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_audio_preview_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_ms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_explicit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_urls.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_href_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_html_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_images.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_externally_hosted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_playable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_languages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_date_precision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_restrictions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_resume_point.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uri_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEpisodeBase::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_audio_preview_url_isValid && m_description_isValid && m_duration_ms_isValid && m_r_explicit_isValid && m_external_urls_isValid && m_href_isValid && m_html_description_isValid && m_id_isValid && m_images_isValid && m_is_externally_hosted_isValid && m_is_playable_isValid && m_languages_isValid && m_name_isValid && m_release_date_isValid && m_release_date_precision_isValid && m_resume_point_isValid && m_type_isValid && m_uri_isValid && true;
}

} // namespace OpenAPI
