/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPlaylistItem_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaylistItem_data::OAIPlaylistItem_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaylistItem_data::OAIPlaylistItem_data() {
    this->initializeModel();
}

OAIPlaylistItem_data::~OAIPlaylistItem_data() {}

void OAIPlaylistItem_data::initializeModel() {

    m_audio_isSet = false;
    m_audio_isValid = false;

    m_audio_length_sec_isSet = false;
    m_audio_length_sec_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_explicit_content_isSet = false;
    m_explicit_content_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_link_isSet = false;
    m_link_isValid = false;

    m_listennotes_edit_url_isSet = false;
    m_listennotes_edit_url_isValid = false;

    m_listennotes_url_isSet = false;
    m_listennotes_url_isValid = false;

    m_maybe_audio_invalid_isSet = false;
    m_maybe_audio_invalid_isValid = false;

    m_podcast_isSet = false;
    m_podcast_isValid = false;

    m_pub_date_ms_isSet = false;
    m_pub_date_ms_isValid = false;

    m_thumbnail_isSet = false;
    m_thumbnail_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_earliest_pub_date_ms_isSet = false;
    m_earliest_pub_date_ms_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_extra_isSet = false;
    m_extra_isValid = false;

    m_genre_ids_isSet = false;
    m_genre_ids_isValid = false;

    m_is_claimed_isSet = false;
    m_is_claimed_isValid = false;

    m_itunes_id_isSet = false;
    m_itunes_id_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_latest_episode_id_isSet = false;
    m_latest_episode_id_isValid = false;

    m_latest_pub_date_ms_isSet = false;
    m_latest_pub_date_ms_isValid = false;

    m_listen_score_isSet = false;
    m_listen_score_isValid = false;

    m_listen_score_global_rank_isSet = false;
    m_listen_score_global_rank_isValid = false;

    m_looking_for_isSet = false;
    m_looking_for_isValid = false;

    m_publisher_isSet = false;
    m_publisher_isValid = false;

    m_rss_isSet = false;
    m_rss_isValid = false;

    m_total_episodes_isSet = false;
    m_total_episodes_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_update_frequency_hours_isSet = false;
    m_update_frequency_hours_isValid = false;

    m_website_isSet = false;
    m_website_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIPlaylistItem_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaylistItem_data::fromJsonObject(QJsonObject json) {

    m_audio_isValid = ::OpenAPI::fromJsonValue(m_audio, json[QString("audio")]);
    m_audio_isSet = !json[QString("audio")].isNull() && m_audio_isValid;

    m_audio_length_sec_isValid = ::OpenAPI::fromJsonValue(m_audio_length_sec, json[QString("audio_length_sec")]);
    m_audio_length_sec_isSet = !json[QString("audio_length_sec")].isNull() && m_audio_length_sec_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_explicit_content_isValid = ::OpenAPI::fromJsonValue(m_explicit_content, json[QString("explicit_content")]);
    m_explicit_content_isSet = !json[QString("explicit_content")].isNull() && m_explicit_content_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_link_isValid = ::OpenAPI::fromJsonValue(m_link, json[QString("link")]);
    m_link_isSet = !json[QString("link")].isNull() && m_link_isValid;

    m_listennotes_edit_url_isValid = ::OpenAPI::fromJsonValue(m_listennotes_edit_url, json[QString("listennotes_edit_url")]);
    m_listennotes_edit_url_isSet = !json[QString("listennotes_edit_url")].isNull() && m_listennotes_edit_url_isValid;

    m_listennotes_url_isValid = ::OpenAPI::fromJsonValue(m_listennotes_url, json[QString("listennotes_url")]);
    m_listennotes_url_isSet = !json[QString("listennotes_url")].isNull() && m_listennotes_url_isValid;

    m_maybe_audio_invalid_isValid = ::OpenAPI::fromJsonValue(m_maybe_audio_invalid, json[QString("maybe_audio_invalid")]);
    m_maybe_audio_invalid_isSet = !json[QString("maybe_audio_invalid")].isNull() && m_maybe_audio_invalid_isValid;

    m_podcast_isValid = ::OpenAPI::fromJsonValue(m_podcast, json[QString("podcast")]);
    m_podcast_isSet = !json[QString("podcast")].isNull() && m_podcast_isValid;

    m_pub_date_ms_isValid = ::OpenAPI::fromJsonValue(m_pub_date_ms, json[QString("pub_date_ms")]);
    m_pub_date_ms_isSet = !json[QString("pub_date_ms")].isNull() && m_pub_date_ms_isValid;

    m_thumbnail_isValid = ::OpenAPI::fromJsonValue(m_thumbnail, json[QString("thumbnail")]);
    m_thumbnail_isSet = !json[QString("thumbnail")].isNull() && m_thumbnail_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_earliest_pub_date_ms_isValid = ::OpenAPI::fromJsonValue(m_earliest_pub_date_ms, json[QString("earliest_pub_date_ms")]);
    m_earliest_pub_date_ms_isSet = !json[QString("earliest_pub_date_ms")].isNull() && m_earliest_pub_date_ms_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_extra_isValid = ::OpenAPI::fromJsonValue(m_extra, json[QString("extra")]);
    m_extra_isSet = !json[QString("extra")].isNull() && m_extra_isValid;

    m_genre_ids_isValid = ::OpenAPI::fromJsonValue(m_genre_ids, json[QString("genre_ids")]);
    m_genre_ids_isSet = !json[QString("genre_ids")].isNull() && m_genre_ids_isValid;

    m_is_claimed_isValid = ::OpenAPI::fromJsonValue(m_is_claimed, json[QString("is_claimed")]);
    m_is_claimed_isSet = !json[QString("is_claimed")].isNull() && m_is_claimed_isValid;

    m_itunes_id_isValid = ::OpenAPI::fromJsonValue(m_itunes_id, json[QString("itunes_id")]);
    m_itunes_id_isSet = !json[QString("itunes_id")].isNull() && m_itunes_id_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_latest_episode_id_isValid = ::OpenAPI::fromJsonValue(m_latest_episode_id, json[QString("latest_episode_id")]);
    m_latest_episode_id_isSet = !json[QString("latest_episode_id")].isNull() && m_latest_episode_id_isValid;

    m_latest_pub_date_ms_isValid = ::OpenAPI::fromJsonValue(m_latest_pub_date_ms, json[QString("latest_pub_date_ms")]);
    m_latest_pub_date_ms_isSet = !json[QString("latest_pub_date_ms")].isNull() && m_latest_pub_date_ms_isValid;

    m_listen_score_isValid = ::OpenAPI::fromJsonValue(m_listen_score, json[QString("listen_score")]);
    m_listen_score_isSet = !json[QString("listen_score")].isNull() && m_listen_score_isValid;

    m_listen_score_global_rank_isValid = ::OpenAPI::fromJsonValue(m_listen_score_global_rank, json[QString("listen_score_global_rank")]);
    m_listen_score_global_rank_isSet = !json[QString("listen_score_global_rank")].isNull() && m_listen_score_global_rank_isValid;

    m_looking_for_isValid = ::OpenAPI::fromJsonValue(m_looking_for, json[QString("looking_for")]);
    m_looking_for_isSet = !json[QString("looking_for")].isNull() && m_looking_for_isValid;

    m_publisher_isValid = ::OpenAPI::fromJsonValue(m_publisher, json[QString("publisher")]);
    m_publisher_isSet = !json[QString("publisher")].isNull() && m_publisher_isValid;

    m_rss_isValid = ::OpenAPI::fromJsonValue(m_rss, json[QString("rss")]);
    m_rss_isSet = !json[QString("rss")].isNull() && m_rss_isValid;

    m_total_episodes_isValid = ::OpenAPI::fromJsonValue(m_total_episodes, json[QString("total_episodes")]);
    m_total_episodes_isSet = !json[QString("total_episodes")].isNull() && m_total_episodes_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_update_frequency_hours_isValid = ::OpenAPI::fromJsonValue(m_update_frequency_hours, json[QString("update_frequency_hours")]);
    m_update_frequency_hours_isSet = !json[QString("update_frequency_hours")].isNull() && m_update_frequency_hours_isValid;

    m_website_isValid = ::OpenAPI::fromJsonValue(m_website, json[QString("website")]);
    m_website_isSet = !json[QString("website")].isNull() && m_website_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIPlaylistItem_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaylistItem_data::asJsonObject() const {
    QJsonObject obj;
    if (m_audio_isSet) {
        obj.insert(QString("audio"), ::OpenAPI::toJsonValue(m_audio));
    }
    if (m_audio_length_sec_isSet) {
        obj.insert(QString("audio_length_sec"), ::OpenAPI::toJsonValue(m_audio_length_sec));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_explicit_content_isSet) {
        obj.insert(QString("explicit_content"), ::OpenAPI::toJsonValue(m_explicit_content));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_link_isSet) {
        obj.insert(QString("link"), ::OpenAPI::toJsonValue(m_link));
    }
    if (m_listennotes_edit_url_isSet) {
        obj.insert(QString("listennotes_edit_url"), ::OpenAPI::toJsonValue(m_listennotes_edit_url));
    }
    if (m_listennotes_url_isSet) {
        obj.insert(QString("listennotes_url"), ::OpenAPI::toJsonValue(m_listennotes_url));
    }
    if (m_maybe_audio_invalid_isSet) {
        obj.insert(QString("maybe_audio_invalid"), ::OpenAPI::toJsonValue(m_maybe_audio_invalid));
    }
    if (m_podcast.isSet()) {
        obj.insert(QString("podcast"), ::OpenAPI::toJsonValue(m_podcast));
    }
    if (m_pub_date_ms_isSet) {
        obj.insert(QString("pub_date_ms"), ::OpenAPI::toJsonValue(m_pub_date_ms));
    }
    if (m_thumbnail_isSet) {
        obj.insert(QString("thumbnail"), ::OpenAPI::toJsonValue(m_thumbnail));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_earliest_pub_date_ms_isSet) {
        obj.insert(QString("earliest_pub_date_ms"), ::OpenAPI::toJsonValue(m_earliest_pub_date_ms));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_extra.isSet()) {
        obj.insert(QString("extra"), ::OpenAPI::toJsonValue(m_extra));
    }
    if (m_genre_ids.size() > 0) {
        obj.insert(QString("genre_ids"), ::OpenAPI::toJsonValue(m_genre_ids));
    }
    if (m_is_claimed_isSet) {
        obj.insert(QString("is_claimed"), ::OpenAPI::toJsonValue(m_is_claimed));
    }
    if (m_itunes_id_isSet) {
        obj.insert(QString("itunes_id"), ::OpenAPI::toJsonValue(m_itunes_id));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_latest_episode_id_isSet) {
        obj.insert(QString("latest_episode_id"), ::OpenAPI::toJsonValue(m_latest_episode_id));
    }
    if (m_latest_pub_date_ms_isSet) {
        obj.insert(QString("latest_pub_date_ms"), ::OpenAPI::toJsonValue(m_latest_pub_date_ms));
    }
    if (m_listen_score_isSet) {
        obj.insert(QString("listen_score"), ::OpenAPI::toJsonValue(m_listen_score));
    }
    if (m_listen_score_global_rank_isSet) {
        obj.insert(QString("listen_score_global_rank"), ::OpenAPI::toJsonValue(m_listen_score_global_rank));
    }
    if (m_looking_for.isSet()) {
        obj.insert(QString("looking_for"), ::OpenAPI::toJsonValue(m_looking_for));
    }
    if (m_publisher_isSet) {
        obj.insert(QString("publisher"), ::OpenAPI::toJsonValue(m_publisher));
    }
    if (m_rss_isSet) {
        obj.insert(QString("rss"), ::OpenAPI::toJsonValue(m_rss));
    }
    if (m_total_episodes_isSet) {
        obj.insert(QString("total_episodes"), ::OpenAPI::toJsonValue(m_total_episodes));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_update_frequency_hours_isSet) {
        obj.insert(QString("update_frequency_hours"), ::OpenAPI::toJsonValue(m_update_frequency_hours));
    }
    if (m_website_isSet) {
        obj.insert(QString("website"), ::OpenAPI::toJsonValue(m_website));
    }
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIPlaylistItem_data::getAudio() const {
    return m_audio;
}
void OAIPlaylistItem_data::setAudio(const QString &audio) {
    m_audio = audio;
    m_audio_isSet = true;
}

bool OAIPlaylistItem_data::is_audio_Set() const{
    return m_audio_isSet;
}

bool OAIPlaylistItem_data::is_audio_Valid() const{
    return m_audio_isValid;
}

qint32 OAIPlaylistItem_data::getAudioLengthSec() const {
    return m_audio_length_sec;
}
void OAIPlaylistItem_data::setAudioLengthSec(const qint32 &audio_length_sec) {
    m_audio_length_sec = audio_length_sec;
    m_audio_length_sec_isSet = true;
}

bool OAIPlaylistItem_data::is_audio_length_sec_Set() const{
    return m_audio_length_sec_isSet;
}

bool OAIPlaylistItem_data::is_audio_length_sec_Valid() const{
    return m_audio_length_sec_isValid;
}

QString OAIPlaylistItem_data::getDescription() const {
    return m_description;
}
void OAIPlaylistItem_data::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIPlaylistItem_data::is_description_Set() const{
    return m_description_isSet;
}

bool OAIPlaylistItem_data::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIPlaylistItem_data::isExplicitContent() const {
    return m_explicit_content;
}
void OAIPlaylistItem_data::setExplicitContent(const bool &explicit_content) {
    m_explicit_content = explicit_content;
    m_explicit_content_isSet = true;
}

bool OAIPlaylistItem_data::is_explicit_content_Set() const{
    return m_explicit_content_isSet;
}

bool OAIPlaylistItem_data::is_explicit_content_Valid() const{
    return m_explicit_content_isValid;
}

QString OAIPlaylistItem_data::getId() const {
    return m_id;
}
void OAIPlaylistItem_data::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPlaylistItem_data::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPlaylistItem_data::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPlaylistItem_data::getImage() const {
    return m_image;
}
void OAIPlaylistItem_data::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIPlaylistItem_data::is_image_Set() const{
    return m_image_isSet;
}

bool OAIPlaylistItem_data::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIPlaylistItem_data::getLink() const {
    return m_link;
}
void OAIPlaylistItem_data::setLink(const QString &link) {
    m_link = link;
    m_link_isSet = true;
}

bool OAIPlaylistItem_data::is_link_Set() const{
    return m_link_isSet;
}

bool OAIPlaylistItem_data::is_link_Valid() const{
    return m_link_isValid;
}

QString OAIPlaylistItem_data::getListennotesEditUrl() const {
    return m_listennotes_edit_url;
}
void OAIPlaylistItem_data::setListennotesEditUrl(const QString &listennotes_edit_url) {
    m_listennotes_edit_url = listennotes_edit_url;
    m_listennotes_edit_url_isSet = true;
}

bool OAIPlaylistItem_data::is_listennotes_edit_url_Set() const{
    return m_listennotes_edit_url_isSet;
}

bool OAIPlaylistItem_data::is_listennotes_edit_url_Valid() const{
    return m_listennotes_edit_url_isValid;
}

QString OAIPlaylistItem_data::getListennotesUrl() const {
    return m_listennotes_url;
}
void OAIPlaylistItem_data::setListennotesUrl(const QString &listennotes_url) {
    m_listennotes_url = listennotes_url;
    m_listennotes_url_isSet = true;
}

bool OAIPlaylistItem_data::is_listennotes_url_Set() const{
    return m_listennotes_url_isSet;
}

bool OAIPlaylistItem_data::is_listennotes_url_Valid() const{
    return m_listennotes_url_isValid;
}

bool OAIPlaylistItem_data::isMaybeAudioInvalid() const {
    return m_maybe_audio_invalid;
}
void OAIPlaylistItem_data::setMaybeAudioInvalid(const bool &maybe_audio_invalid) {
    m_maybe_audio_invalid = maybe_audio_invalid;
    m_maybe_audio_invalid_isSet = true;
}

bool OAIPlaylistItem_data::is_maybe_audio_invalid_Set() const{
    return m_maybe_audio_invalid_isSet;
}

bool OAIPlaylistItem_data::is_maybe_audio_invalid_Valid() const{
    return m_maybe_audio_invalid_isValid;
}

OAIPodcastMinimum OAIPlaylistItem_data::getPodcast() const {
    return m_podcast;
}
void OAIPlaylistItem_data::setPodcast(const OAIPodcastMinimum &podcast) {
    m_podcast = podcast;
    m_podcast_isSet = true;
}

bool OAIPlaylistItem_data::is_podcast_Set() const{
    return m_podcast_isSet;
}

bool OAIPlaylistItem_data::is_podcast_Valid() const{
    return m_podcast_isValid;
}

qint32 OAIPlaylistItem_data::getPubDateMs() const {
    return m_pub_date_ms;
}
void OAIPlaylistItem_data::setPubDateMs(const qint32 &pub_date_ms) {
    m_pub_date_ms = pub_date_ms;
    m_pub_date_ms_isSet = true;
}

bool OAIPlaylistItem_data::is_pub_date_ms_Set() const{
    return m_pub_date_ms_isSet;
}

bool OAIPlaylistItem_data::is_pub_date_ms_Valid() const{
    return m_pub_date_ms_isValid;
}

QString OAIPlaylistItem_data::getThumbnail() const {
    return m_thumbnail;
}
void OAIPlaylistItem_data::setThumbnail(const QString &thumbnail) {
    m_thumbnail = thumbnail;
    m_thumbnail_isSet = true;
}

bool OAIPlaylistItem_data::is_thumbnail_Set() const{
    return m_thumbnail_isSet;
}

bool OAIPlaylistItem_data::is_thumbnail_Valid() const{
    return m_thumbnail_isValid;
}

QString OAIPlaylistItem_data::getTitle() const {
    return m_title;
}
void OAIPlaylistItem_data::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIPlaylistItem_data::is_title_Set() const{
    return m_title_isSet;
}

bool OAIPlaylistItem_data::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIPlaylistItem_data::getCountry() const {
    return m_country;
}
void OAIPlaylistItem_data::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIPlaylistItem_data::is_country_Set() const{
    return m_country_isSet;
}

bool OAIPlaylistItem_data::is_country_Valid() const{
    return m_country_isValid;
}

qint32 OAIPlaylistItem_data::getEarliestPubDateMs() const {
    return m_earliest_pub_date_ms;
}
void OAIPlaylistItem_data::setEarliestPubDateMs(const qint32 &earliest_pub_date_ms) {
    m_earliest_pub_date_ms = earliest_pub_date_ms;
    m_earliest_pub_date_ms_isSet = true;
}

bool OAIPlaylistItem_data::is_earliest_pub_date_ms_Set() const{
    return m_earliest_pub_date_ms_isSet;
}

bool OAIPlaylistItem_data::is_earliest_pub_date_ms_Valid() const{
    return m_earliest_pub_date_ms_isValid;
}

QString OAIPlaylistItem_data::getEmail() const {
    return m_email;
}
void OAIPlaylistItem_data::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIPlaylistItem_data::is_email_Set() const{
    return m_email_isSet;
}

bool OAIPlaylistItem_data::is_email_Valid() const{
    return m_email_isValid;
}

OAIPodcastExtraField OAIPlaylistItem_data::getExtra() const {
    return m_extra;
}
void OAIPlaylistItem_data::setExtra(const OAIPodcastExtraField &extra) {
    m_extra = extra;
    m_extra_isSet = true;
}

bool OAIPlaylistItem_data::is_extra_Set() const{
    return m_extra_isSet;
}

bool OAIPlaylistItem_data::is_extra_Valid() const{
    return m_extra_isValid;
}

QList<qint32> OAIPlaylistItem_data::getGenreIds() const {
    return m_genre_ids;
}
void OAIPlaylistItem_data::setGenreIds(const QList<qint32> &genre_ids) {
    m_genre_ids = genre_ids;
    m_genre_ids_isSet = true;
}

bool OAIPlaylistItem_data::is_genre_ids_Set() const{
    return m_genre_ids_isSet;
}

bool OAIPlaylistItem_data::is_genre_ids_Valid() const{
    return m_genre_ids_isValid;
}

bool OAIPlaylistItem_data::isIsClaimed() const {
    return m_is_claimed;
}
void OAIPlaylistItem_data::setIsClaimed(const bool &is_claimed) {
    m_is_claimed = is_claimed;
    m_is_claimed_isSet = true;
}

bool OAIPlaylistItem_data::is_is_claimed_Set() const{
    return m_is_claimed_isSet;
}

bool OAIPlaylistItem_data::is_is_claimed_Valid() const{
    return m_is_claimed_isValid;
}

qint32 OAIPlaylistItem_data::getItunesId() const {
    return m_itunes_id;
}
void OAIPlaylistItem_data::setItunesId(const qint32 &itunes_id) {
    m_itunes_id = itunes_id;
    m_itunes_id_isSet = true;
}

bool OAIPlaylistItem_data::is_itunes_id_Set() const{
    return m_itunes_id_isSet;
}

bool OAIPlaylistItem_data::is_itunes_id_Valid() const{
    return m_itunes_id_isValid;
}

QString OAIPlaylistItem_data::getLanguage() const {
    return m_language;
}
void OAIPlaylistItem_data::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIPlaylistItem_data::is_language_Set() const{
    return m_language_isSet;
}

bool OAIPlaylistItem_data::is_language_Valid() const{
    return m_language_isValid;
}

QString OAIPlaylistItem_data::getLatestEpisodeId() const {
    return m_latest_episode_id;
}
void OAIPlaylistItem_data::setLatestEpisodeId(const QString &latest_episode_id) {
    m_latest_episode_id = latest_episode_id;
    m_latest_episode_id_isSet = true;
}

bool OAIPlaylistItem_data::is_latest_episode_id_Set() const{
    return m_latest_episode_id_isSet;
}

bool OAIPlaylistItem_data::is_latest_episode_id_Valid() const{
    return m_latest_episode_id_isValid;
}

qint32 OAIPlaylistItem_data::getLatestPubDateMs() const {
    return m_latest_pub_date_ms;
}
void OAIPlaylistItem_data::setLatestPubDateMs(const qint32 &latest_pub_date_ms) {
    m_latest_pub_date_ms = latest_pub_date_ms;
    m_latest_pub_date_ms_isSet = true;
}

bool OAIPlaylistItem_data::is_latest_pub_date_ms_Set() const{
    return m_latest_pub_date_ms_isSet;
}

bool OAIPlaylistItem_data::is_latest_pub_date_ms_Valid() const{
    return m_latest_pub_date_ms_isValid;
}

qint32 OAIPlaylistItem_data::getListenScore() const {
    return m_listen_score;
}
void OAIPlaylistItem_data::setListenScore(const qint32 &listen_score) {
    m_listen_score = listen_score;
    m_listen_score_isSet = true;
}

bool OAIPlaylistItem_data::is_listen_score_Set() const{
    return m_listen_score_isSet;
}

bool OAIPlaylistItem_data::is_listen_score_Valid() const{
    return m_listen_score_isValid;
}

QString OAIPlaylistItem_data::getListenScoreGlobalRank() const {
    return m_listen_score_global_rank;
}
void OAIPlaylistItem_data::setListenScoreGlobalRank(const QString &listen_score_global_rank) {
    m_listen_score_global_rank = listen_score_global_rank;
    m_listen_score_global_rank_isSet = true;
}

bool OAIPlaylistItem_data::is_listen_score_global_rank_Set() const{
    return m_listen_score_global_rank_isSet;
}

bool OAIPlaylistItem_data::is_listen_score_global_rank_Valid() const{
    return m_listen_score_global_rank_isValid;
}

OAIPodcastLookingForField OAIPlaylistItem_data::getLookingFor() const {
    return m_looking_for;
}
void OAIPlaylistItem_data::setLookingFor(const OAIPodcastLookingForField &looking_for) {
    m_looking_for = looking_for;
    m_looking_for_isSet = true;
}

bool OAIPlaylistItem_data::is_looking_for_Set() const{
    return m_looking_for_isSet;
}

bool OAIPlaylistItem_data::is_looking_for_Valid() const{
    return m_looking_for_isValid;
}

QString OAIPlaylistItem_data::getPublisher() const {
    return m_publisher;
}
void OAIPlaylistItem_data::setPublisher(const QString &publisher) {
    m_publisher = publisher;
    m_publisher_isSet = true;
}

bool OAIPlaylistItem_data::is_publisher_Set() const{
    return m_publisher_isSet;
}

bool OAIPlaylistItem_data::is_publisher_Valid() const{
    return m_publisher_isValid;
}

QString OAIPlaylistItem_data::getRss() const {
    return m_rss;
}
void OAIPlaylistItem_data::setRss(const QString &rss) {
    m_rss = rss;
    m_rss_isSet = true;
}

bool OAIPlaylistItem_data::is_rss_Set() const{
    return m_rss_isSet;
}

bool OAIPlaylistItem_data::is_rss_Valid() const{
    return m_rss_isValid;
}

qint32 OAIPlaylistItem_data::getTotalEpisodes() const {
    return m_total_episodes;
}
void OAIPlaylistItem_data::setTotalEpisodes(const qint32 &total_episodes) {
    m_total_episodes = total_episodes;
    m_total_episodes_isSet = true;
}

bool OAIPlaylistItem_data::is_total_episodes_Set() const{
    return m_total_episodes_isSet;
}

bool OAIPlaylistItem_data::is_total_episodes_Valid() const{
    return m_total_episodes_isValid;
}

OAIPodcastTypeField OAIPlaylistItem_data::getType() const {
    return m_type;
}
void OAIPlaylistItem_data::setType(const OAIPodcastTypeField &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPlaylistItem_data::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPlaylistItem_data::is_type_Valid() const{
    return m_type_isValid;
}

qint32 OAIPlaylistItem_data::getUpdateFrequencyHours() const {
    return m_update_frequency_hours;
}
void OAIPlaylistItem_data::setUpdateFrequencyHours(const qint32 &update_frequency_hours) {
    m_update_frequency_hours = update_frequency_hours;
    m_update_frequency_hours_isSet = true;
}

bool OAIPlaylistItem_data::is_update_frequency_hours_Set() const{
    return m_update_frequency_hours_isSet;
}

bool OAIPlaylistItem_data::is_update_frequency_hours_Valid() const{
    return m_update_frequency_hours_isValid;
}

QString OAIPlaylistItem_data::getWebsite() const {
    return m_website;
}
void OAIPlaylistItem_data::setWebsite(const QString &website) {
    m_website = website;
    m_website_isSet = true;
}

bool OAIPlaylistItem_data::is_website_Set() const{
    return m_website_isSet;
}

bool OAIPlaylistItem_data::is_website_Valid() const{
    return m_website_isValid;
}

QString OAIPlaylistItem_data::getError() const {
    return m_error;
}
void OAIPlaylistItem_data::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIPlaylistItem_data::is_error_Set() const{
    return m_error_isSet;
}

bool OAIPlaylistItem_data::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIPlaylistItem_data::getStatus() const {
    return m_status;
}
void OAIPlaylistItem_data::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPlaylistItem_data::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPlaylistItem_data::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIPlaylistItem_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_audio_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_audio_length_sec_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_explicit_content_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_listennotes_edit_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_listennotes_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_maybe_audio_invalid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_podcast.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_pub_date_ms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_earliest_pub_date_ms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extra.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_genre_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_claimed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_itunes_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latest_episode_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latest_pub_date_ms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_listen_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_listen_score_global_rank_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_looking_for.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_publisher_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rss_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_episodes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_frequency_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlaylistItem_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
