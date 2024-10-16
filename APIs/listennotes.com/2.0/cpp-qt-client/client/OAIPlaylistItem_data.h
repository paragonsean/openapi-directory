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

/*
 * OAIPlaylistItem_data.h
 *
 * 
 */

#ifndef OAIPlaylistItem_data_H
#define OAIPlaylistItem_data_H

#include <QJsonObject>

#include "OAICustomAudio.h"
#include "OAIDeletedItem.h"
#include "OAIEpisodeSimple.h"
#include "OAIPodcastExtraField.h"
#include "OAIPodcastLookingForField.h"
#include "OAIPodcastMinimum.h"
#include "OAIPodcastSimple.h"
#include "OAIPodcastTypeField.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPodcastMinimum;
class OAIPodcastExtraField;
class OAIPodcastLookingForField;

class OAIPlaylistItem_data : public OAIObject {
public:
    OAIPlaylistItem_data();
    OAIPlaylistItem_data(QString json);
    ~OAIPlaylistItem_data() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAudio() const;
    void setAudio(const QString &audio);
    bool is_audio_Set() const;
    bool is_audio_Valid() const;

    qint32 getAudioLengthSec() const;
    void setAudioLengthSec(const qint32 &audio_length_sec);
    bool is_audio_length_sec_Set() const;
    bool is_audio_length_sec_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    bool isExplicitContent() const;
    void setExplicitContent(const bool &explicit_content);
    bool is_explicit_content_Set() const;
    bool is_explicit_content_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getImage() const;
    void setImage(const QString &image);
    bool is_image_Set() const;
    bool is_image_Valid() const;

    QString getLink() const;
    void setLink(const QString &link);
    bool is_link_Set() const;
    bool is_link_Valid() const;

    QString getListennotesEditUrl() const;
    void setListennotesEditUrl(const QString &listennotes_edit_url);
    bool is_listennotes_edit_url_Set() const;
    bool is_listennotes_edit_url_Valid() const;

    QString getListennotesUrl() const;
    void setListennotesUrl(const QString &listennotes_url);
    bool is_listennotes_url_Set() const;
    bool is_listennotes_url_Valid() const;

    bool isMaybeAudioInvalid() const;
    void setMaybeAudioInvalid(const bool &maybe_audio_invalid);
    bool is_maybe_audio_invalid_Set() const;
    bool is_maybe_audio_invalid_Valid() const;

    OAIPodcastMinimum getPodcast() const;
    void setPodcast(const OAIPodcastMinimum &podcast);
    bool is_podcast_Set() const;
    bool is_podcast_Valid() const;

    qint32 getPubDateMs() const;
    void setPubDateMs(const qint32 &pub_date_ms);
    bool is_pub_date_ms_Set() const;
    bool is_pub_date_ms_Valid() const;

    QString getThumbnail() const;
    void setThumbnail(const QString &thumbnail);
    bool is_thumbnail_Set() const;
    bool is_thumbnail_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    qint32 getEarliestPubDateMs() const;
    void setEarliestPubDateMs(const qint32 &earliest_pub_date_ms);
    bool is_earliest_pub_date_ms_Set() const;
    bool is_earliest_pub_date_ms_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    OAIPodcastExtraField getExtra() const;
    void setExtra(const OAIPodcastExtraField &extra);
    bool is_extra_Set() const;
    bool is_extra_Valid() const;

    QList<qint32> getGenreIds() const;
    void setGenreIds(const QList<qint32> &genre_ids);
    bool is_genre_ids_Set() const;
    bool is_genre_ids_Valid() const;

    bool isIsClaimed() const;
    void setIsClaimed(const bool &is_claimed);
    bool is_is_claimed_Set() const;
    bool is_is_claimed_Valid() const;

    qint32 getItunesId() const;
    void setItunesId(const qint32 &itunes_id);
    bool is_itunes_id_Set() const;
    bool is_itunes_id_Valid() const;

    QString getLanguage() const;
    void setLanguage(const QString &language);
    bool is_language_Set() const;
    bool is_language_Valid() const;

    QString getLatestEpisodeId() const;
    void setLatestEpisodeId(const QString &latest_episode_id);
    bool is_latest_episode_id_Set() const;
    bool is_latest_episode_id_Valid() const;

    qint32 getLatestPubDateMs() const;
    void setLatestPubDateMs(const qint32 &latest_pub_date_ms);
    bool is_latest_pub_date_ms_Set() const;
    bool is_latest_pub_date_ms_Valid() const;

    qint32 getListenScore() const;
    void setListenScore(const qint32 &listen_score);
    bool is_listen_score_Set() const;
    bool is_listen_score_Valid() const;

    QString getListenScoreGlobalRank() const;
    void setListenScoreGlobalRank(const QString &listen_score_global_rank);
    bool is_listen_score_global_rank_Set() const;
    bool is_listen_score_global_rank_Valid() const;

    OAIPodcastLookingForField getLookingFor() const;
    void setLookingFor(const OAIPodcastLookingForField &looking_for);
    bool is_looking_for_Set() const;
    bool is_looking_for_Valid() const;

    QString getPublisher() const;
    void setPublisher(const QString &publisher);
    bool is_publisher_Set() const;
    bool is_publisher_Valid() const;

    QString getRss() const;
    void setRss(const QString &rss);
    bool is_rss_Set() const;
    bool is_rss_Valid() const;

    qint32 getTotalEpisodes() const;
    void setTotalEpisodes(const qint32 &total_episodes);
    bool is_total_episodes_Set() const;
    bool is_total_episodes_Valid() const;

    OAIPodcastTypeField getType() const;
    void setType(const OAIPodcastTypeField &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    qint32 getUpdateFrequencyHours() const;
    void setUpdateFrequencyHours(const qint32 &update_frequency_hours);
    bool is_update_frequency_hours_Set() const;
    bool is_update_frequency_hours_Valid() const;

    QString getWebsite() const;
    void setWebsite(const QString &website);
    bool is_website_Set() const;
    bool is_website_Valid() const;

    QString getError() const;
    void setError(const QString &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_audio;
    bool m_audio_isSet;
    bool m_audio_isValid;

    qint32 m_audio_length_sec;
    bool m_audio_length_sec_isSet;
    bool m_audio_length_sec_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    bool m_explicit_content;
    bool m_explicit_content_isSet;
    bool m_explicit_content_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_image;
    bool m_image_isSet;
    bool m_image_isValid;

    QString m_link;
    bool m_link_isSet;
    bool m_link_isValid;

    QString m_listennotes_edit_url;
    bool m_listennotes_edit_url_isSet;
    bool m_listennotes_edit_url_isValid;

    QString m_listennotes_url;
    bool m_listennotes_url_isSet;
    bool m_listennotes_url_isValid;

    bool m_maybe_audio_invalid;
    bool m_maybe_audio_invalid_isSet;
    bool m_maybe_audio_invalid_isValid;

    OAIPodcastMinimum m_podcast;
    bool m_podcast_isSet;
    bool m_podcast_isValid;

    qint32 m_pub_date_ms;
    bool m_pub_date_ms_isSet;
    bool m_pub_date_ms_isValid;

    QString m_thumbnail;
    bool m_thumbnail_isSet;
    bool m_thumbnail_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    qint32 m_earliest_pub_date_ms;
    bool m_earliest_pub_date_ms_isSet;
    bool m_earliest_pub_date_ms_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    OAIPodcastExtraField m_extra;
    bool m_extra_isSet;
    bool m_extra_isValid;

    QList<qint32> m_genre_ids;
    bool m_genre_ids_isSet;
    bool m_genre_ids_isValid;

    bool m_is_claimed;
    bool m_is_claimed_isSet;
    bool m_is_claimed_isValid;

    qint32 m_itunes_id;
    bool m_itunes_id_isSet;
    bool m_itunes_id_isValid;

    QString m_language;
    bool m_language_isSet;
    bool m_language_isValid;

    QString m_latest_episode_id;
    bool m_latest_episode_id_isSet;
    bool m_latest_episode_id_isValid;

    qint32 m_latest_pub_date_ms;
    bool m_latest_pub_date_ms_isSet;
    bool m_latest_pub_date_ms_isValid;

    qint32 m_listen_score;
    bool m_listen_score_isSet;
    bool m_listen_score_isValid;

    QString m_listen_score_global_rank;
    bool m_listen_score_global_rank_isSet;
    bool m_listen_score_global_rank_isValid;

    OAIPodcastLookingForField m_looking_for;
    bool m_looking_for_isSet;
    bool m_looking_for_isValid;

    QString m_publisher;
    bool m_publisher_isSet;
    bool m_publisher_isValid;

    QString m_rss;
    bool m_rss_isSet;
    bool m_rss_isValid;

    qint32 m_total_episodes;
    bool m_total_episodes_isSet;
    bool m_total_episodes_isValid;

    OAIPodcastTypeField m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    qint32 m_update_frequency_hours;
    bool m_update_frequency_hours_isSet;
    bool m_update_frequency_hours_isValid;

    QString m_website;
    bool m_website_isSet;
    bool m_website_isValid;

    QString m_error;
    bool m_error_isSet;
    bool m_error_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlaylistItem_data)

#endif // OAIPlaylistItem_data_H
