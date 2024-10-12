/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIItem::OAIItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIItem::OAIItem() {
    this->initializeModel();
}

OAIItem::~OAIItem() {}

void OAIItem::initializeModel() {

    m_catalogue_number_isSet = false;
    m_catalogue_number_isValid = false;

    m_contributions_mixin_isSet = false;
    m_contributions_mixin_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_identifiers_isSet = false;
    m_identifiers_isValid = false;

    m_ids_isSet = false;
    m_ids_isValid = false;

    m_images_mixin_isSet = false;
    m_images_mixin_isValid = false;

    m_item_of_isSet = false;
    m_item_of_isValid = false;

    m_music_code_isSet = false;
    m_music_code_isValid = false;

    m_offsets_isSet = false;
    m_offsets_isValid = false;

    m_partner_isSet = false;
    m_partner_isValid = false;

    m_pid_isSet = false;
    m_pid_isValid = false;

    m_play_events_isSet = false;
    m_play_events_isValid = false;

    m_publisher_isSet = false;
    m_publisher_isValid = false;

    m_record_label_isSet = false;
    m_record_label_isValid = false;

    m_recording_date_isSet = false;
    m_recording_date_isValid = false;

    m_release_title_isSet = false;
    m_release_title_isValid = false;

    m_snippet_url_isSet = false;
    m_snippet_url_isValid = false;

    m_source_media_isSet = false;
    m_source_media_isValid = false;

    m_synopses_isSet = false;
    m_synopses_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_track_number_isSet = false;
    m_track_number_isValid = false;

    m_track_side_isSet = false;
    m_track_side_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;
}

void OAIItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIItem::fromJsonObject(QJsonObject json) {

    m_catalogue_number_isValid = ::OpenAPI::fromJsonValue(m_catalogue_number, json[QString("catalogue_number")]);
    m_catalogue_number_isSet = !json[QString("catalogue_number")].isNull() && m_catalogue_number_isValid;

    m_contributions_mixin_isValid = ::OpenAPI::fromJsonValue(m_contributions_mixin, json[QString("contributions_mixin")]);
    m_contributions_mixin_isSet = !json[QString("contributions_mixin")].isNull() && m_contributions_mixin_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_identifiers_isValid = ::OpenAPI::fromJsonValue(m_identifiers, json[QString("identifiers")]);
    m_identifiers_isSet = !json[QString("identifiers")].isNull() && m_identifiers_isValid;

    m_ids_isValid = ::OpenAPI::fromJsonValue(m_ids, json[QString("ids")]);
    m_ids_isSet = !json[QString("ids")].isNull() && m_ids_isValid;

    m_images_mixin_isValid = ::OpenAPI::fromJsonValue(m_images_mixin, json[QString("images_mixin")]);
    m_images_mixin_isSet = !json[QString("images_mixin")].isNull() && m_images_mixin_isValid;

    m_item_of_isValid = ::OpenAPI::fromJsonValue(m_item_of, json[QString("item_of")]);
    m_item_of_isSet = !json[QString("item_of")].isNull() && m_item_of_isValid;

    m_music_code_isValid = ::OpenAPI::fromJsonValue(m_music_code, json[QString("music_code")]);
    m_music_code_isSet = !json[QString("music_code")].isNull() && m_music_code_isValid;

    m_offsets_isValid = ::OpenAPI::fromJsonValue(m_offsets, json[QString("offsets")]);
    m_offsets_isSet = !json[QString("offsets")].isNull() && m_offsets_isValid;

    m_partner_isValid = ::OpenAPI::fromJsonValue(m_partner, json[QString("partner")]);
    m_partner_isSet = !json[QString("partner")].isNull() && m_partner_isValid;

    m_pid_isValid = ::OpenAPI::fromJsonValue(m_pid, json[QString("pid")]);
    m_pid_isSet = !json[QString("pid")].isNull() && m_pid_isValid;

    m_play_events_isValid = ::OpenAPI::fromJsonValue(m_play_events, json[QString("play_events")]);
    m_play_events_isSet = !json[QString("play_events")].isNull() && m_play_events_isValid;

    m_publisher_isValid = ::OpenAPI::fromJsonValue(m_publisher, json[QString("publisher")]);
    m_publisher_isSet = !json[QString("publisher")].isNull() && m_publisher_isValid;

    m_record_label_isValid = ::OpenAPI::fromJsonValue(m_record_label, json[QString("record_label")]);
    m_record_label_isSet = !json[QString("record_label")].isNull() && m_record_label_isValid;

    m_recording_date_isValid = ::OpenAPI::fromJsonValue(m_recording_date, json[QString("recording_date")]);
    m_recording_date_isSet = !json[QString("recording_date")].isNull() && m_recording_date_isValid;

    m_release_title_isValid = ::OpenAPI::fromJsonValue(m_release_title, json[QString("release_title")]);
    m_release_title_isSet = !json[QString("release_title")].isNull() && m_release_title_isValid;

    m_snippet_url_isValid = ::OpenAPI::fromJsonValue(m_snippet_url, json[QString("snippet_url")]);
    m_snippet_url_isSet = !json[QString("snippet_url")].isNull() && m_snippet_url_isValid;

    m_source_media_isValid = ::OpenAPI::fromJsonValue(m_source_media, json[QString("source_media")]);
    m_source_media_isSet = !json[QString("source_media")].isNull() && m_source_media_isValid;

    m_synopses_isValid = ::OpenAPI::fromJsonValue(m_synopses, json[QString("synopses")]);
    m_synopses_isSet = !json[QString("synopses")].isNull() && m_synopses_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_track_number_isValid = ::OpenAPI::fromJsonValue(m_track_number, json[QString("track_number")]);
    m_track_number_isSet = !json[QString("track_number")].isNull() && m_track_number_isValid;

    m_track_side_isValid = ::OpenAPI::fromJsonValue(m_track_side, json[QString("track_side")]);
    m_track_side_isSet = !json[QString("track_side")].isNull() && m_track_side_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updated_time")]);
    m_updated_time_isSet = !json[QString("updated_time")].isNull() && m_updated_time_isValid;
}

QString OAIItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIItem::asJsonObject() const {
    QJsonObject obj;
    if (m_catalogue_number_isSet) {
        obj.insert(QString("catalogue_number"), ::OpenAPI::toJsonValue(m_catalogue_number));
    }
    if (m_contributions_mixin.isSet()) {
        obj.insert(QString("contributions_mixin"), ::OpenAPI::toJsonValue(m_contributions_mixin));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_identifiers.isSet()) {
        obj.insert(QString("identifiers"), ::OpenAPI::toJsonValue(m_identifiers));
    }
    if (m_ids.isSet()) {
        obj.insert(QString("ids"), ::OpenAPI::toJsonValue(m_ids));
    }
    if (m_images_mixin.isSet()) {
        obj.insert(QString("images_mixin"), ::OpenAPI::toJsonValue(m_images_mixin));
    }
    if (m_item_of.isSet()) {
        obj.insert(QString("item_of"), ::OpenAPI::toJsonValue(m_item_of));
    }
    if (m_music_code_isSet) {
        obj.insert(QString("music_code"), ::OpenAPI::toJsonValue(m_music_code));
    }
    if (m_offsets.isSet()) {
        obj.insert(QString("offsets"), ::OpenAPI::toJsonValue(m_offsets));
    }
    if (m_partner_isSet) {
        obj.insert(QString("partner"), ::OpenAPI::toJsonValue(m_partner));
    }
    if (m_pid_isSet) {
        obj.insert(QString("pid"), ::OpenAPI::toJsonValue(m_pid));
    }
    if (m_play_events.isSet()) {
        obj.insert(QString("play_events"), ::OpenAPI::toJsonValue(m_play_events));
    }
    if (m_publisher_isSet) {
        obj.insert(QString("publisher"), ::OpenAPI::toJsonValue(m_publisher));
    }
    if (m_record_label_isSet) {
        obj.insert(QString("record_label"), ::OpenAPI::toJsonValue(m_record_label));
    }
    if (m_recording_date_isSet) {
        obj.insert(QString("recording_date"), ::OpenAPI::toJsonValue(m_recording_date));
    }
    if (m_release_title_isSet) {
        obj.insert(QString("release_title"), ::OpenAPI::toJsonValue(m_release_title));
    }
    if (m_snippet_url_isSet) {
        obj.insert(QString("snippet_url"), ::OpenAPI::toJsonValue(m_snippet_url));
    }
    if (m_source_media_isSet) {
        obj.insert(QString("source_media"), ::OpenAPI::toJsonValue(m_source_media));
    }
    if (m_synopses.isSet()) {
        obj.insert(QString("synopses"), ::OpenAPI::toJsonValue(m_synopses));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_track_number_isSet) {
        obj.insert(QString("track_number"), ::OpenAPI::toJsonValue(m_track_number));
    }
    if (m_track_side_isSet) {
        obj.insert(QString("track_side"), ::OpenAPI::toJsonValue(m_track_side));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updated_time"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    return obj;
}

QString OAIItem::getCatalogueNumber() const {
    return m_catalogue_number;
}
void OAIItem::setCatalogueNumber(const QString &catalogue_number) {
    m_catalogue_number = catalogue_number;
    m_catalogue_number_isSet = true;
}

bool OAIItem::is_catalogue_number_Set() const{
    return m_catalogue_number_isSet;
}

bool OAIItem::is_catalogue_number_Valid() const{
    return m_catalogue_number_isValid;
}

OAIContributions_mixin OAIItem::getContributionsMixin() const {
    return m_contributions_mixin;
}
void OAIItem::setContributionsMixin(const OAIContributions_mixin &contributions_mixin) {
    m_contributions_mixin = contributions_mixin;
    m_contributions_mixin_isSet = true;
}

bool OAIItem::is_contributions_mixin_Set() const{
    return m_contributions_mixin_isSet;
}

bool OAIItem::is_contributions_mixin_Valid() const{
    return m_contributions_mixin_isValid;
}

float OAIItem::getDuration() const {
    return m_duration;
}
void OAIItem::setDuration(const float &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIItem::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIItem::is_duration_Valid() const{
    return m_duration_isValid;
}

OAIIdentifiers OAIItem::getIdentifiers() const {
    return m_identifiers;
}
void OAIItem::setIdentifiers(const OAIIdentifiers &identifiers) {
    m_identifiers = identifiers;
    m_identifiers_isSet = true;
}

bool OAIItem::is_identifiers_Set() const{
    return m_identifiers_isSet;
}

bool OAIItem::is_identifiers_Valid() const{
    return m_identifiers_isValid;
}

OAIIds OAIItem::getIds() const {
    return m_ids;
}
void OAIItem::setIds(const OAIIds &ids) {
    m_ids = ids;
    m_ids_isSet = true;
}

bool OAIItem::is_ids_Set() const{
    return m_ids_isSet;
}

bool OAIItem::is_ids_Valid() const{
    return m_ids_isValid;
}

OAIImages_mixin OAIItem::getImagesMixin() const {
    return m_images_mixin;
}
void OAIItem::setImagesMixin(const OAIImages_mixin &images_mixin) {
    m_images_mixin = images_mixin;
    m_images_mixin_isSet = true;
}

bool OAIItem::is_images_mixin_Set() const{
    return m_images_mixin_isSet;
}

bool OAIItem::is_images_mixin_Valid() const{
    return m_images_mixin_isValid;
}

OAIReference OAIItem::getItemOf() const {
    return m_item_of;
}
void OAIItem::setItemOf(const OAIReference &item_of) {
    m_item_of = item_of;
    m_item_of_isSet = true;
}

bool OAIItem::is_item_of_Set() const{
    return m_item_of_isSet;
}

bool OAIItem::is_item_of_Valid() const{
    return m_item_of_isValid;
}

QString OAIItem::getMusicCode() const {
    return m_music_code;
}
void OAIItem::setMusicCode(const QString &music_code) {
    m_music_code = music_code;
    m_music_code_isSet = true;
}

bool OAIItem::is_music_code_Set() const{
    return m_music_code_isSet;
}

bool OAIItem::is_music_code_Valid() const{
    return m_music_code_isValid;
}

OAIOffsets OAIItem::getOffsets() const {
    return m_offsets;
}
void OAIItem::setOffsets(const OAIOffsets &offsets) {
    m_offsets = offsets;
    m_offsets_isSet = true;
}

bool OAIItem::is_offsets_Set() const{
    return m_offsets_isSet;
}

bool OAIItem::is_offsets_Valid() const{
    return m_offsets_isValid;
}

QString OAIItem::getPartner() const {
    return m_partner;
}
void OAIItem::setPartner(const QString &partner) {
    m_partner = partner;
    m_partner_isSet = true;
}

bool OAIItem::is_partner_Set() const{
    return m_partner_isSet;
}

bool OAIItem::is_partner_Valid() const{
    return m_partner_isValid;
}

QString OAIItem::getPid() const {
    return m_pid;
}
void OAIItem::setPid(const QString &pid) {
    m_pid = pid;
    m_pid_isSet = true;
}

bool OAIItem::is_pid_Set() const{
    return m_pid_isSet;
}

bool OAIItem::is_pid_Valid() const{
    return m_pid_isValid;
}

OAIPlay_events OAIItem::getPlayEvents() const {
    return m_play_events;
}
void OAIItem::setPlayEvents(const OAIPlay_events &play_events) {
    m_play_events = play_events;
    m_play_events_isSet = true;
}

bool OAIItem::is_play_events_Set() const{
    return m_play_events_isSet;
}

bool OAIItem::is_play_events_Valid() const{
    return m_play_events_isValid;
}

QString OAIItem::getPublisher() const {
    return m_publisher;
}
void OAIItem::setPublisher(const QString &publisher) {
    m_publisher = publisher;
    m_publisher_isSet = true;
}

bool OAIItem::is_publisher_Set() const{
    return m_publisher_isSet;
}

bool OAIItem::is_publisher_Valid() const{
    return m_publisher_isValid;
}

QString OAIItem::getRecordLabel() const {
    return m_record_label;
}
void OAIItem::setRecordLabel(const QString &record_label) {
    m_record_label = record_label;
    m_record_label_isSet = true;
}

bool OAIItem::is_record_label_Set() const{
    return m_record_label_isSet;
}

bool OAIItem::is_record_label_Valid() const{
    return m_record_label_isValid;
}

QString OAIItem::getRecordingDate() const {
    return m_recording_date;
}
void OAIItem::setRecordingDate(const QString &recording_date) {
    m_recording_date = recording_date;
    m_recording_date_isSet = true;
}

bool OAIItem::is_recording_date_Set() const{
    return m_recording_date_isSet;
}

bool OAIItem::is_recording_date_Valid() const{
    return m_recording_date_isValid;
}

QString OAIItem::getReleaseTitle() const {
    return m_release_title;
}
void OAIItem::setReleaseTitle(const QString &release_title) {
    m_release_title = release_title;
    m_release_title_isSet = true;
}

bool OAIItem::is_release_title_Set() const{
    return m_release_title_isSet;
}

bool OAIItem::is_release_title_Valid() const{
    return m_release_title_isValid;
}

QString OAIItem::getSnippetUrl() const {
    return m_snippet_url;
}
void OAIItem::setSnippetUrl(const QString &snippet_url) {
    m_snippet_url = snippet_url;
    m_snippet_url_isSet = true;
}

bool OAIItem::is_snippet_url_Set() const{
    return m_snippet_url_isSet;
}

bool OAIItem::is_snippet_url_Valid() const{
    return m_snippet_url_isValid;
}

QString OAIItem::getSourceMedia() const {
    return m_source_media;
}
void OAIItem::setSourceMedia(const QString &source_media) {
    m_source_media = source_media;
    m_source_media_isSet = true;
}

bool OAIItem::is_source_media_Set() const{
    return m_source_media_isSet;
}

bool OAIItem::is_source_media_Valid() const{
    return m_source_media_isValid;
}

OAISynopses OAIItem::getSynopses() const {
    return m_synopses;
}
void OAIItem::setSynopses(const OAISynopses &synopses) {
    m_synopses = synopses;
    m_synopses_isSet = true;
}

bool OAIItem::is_synopses_Set() const{
    return m_synopses_isSet;
}

bool OAIItem::is_synopses_Valid() const{
    return m_synopses_isValid;
}

QString OAIItem::getTitle() const {
    return m_title;
}
void OAIItem::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIItem::is_title_Set() const{
    return m_title_isSet;
}

bool OAIItem::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIItem::getTrackNumber() const {
    return m_track_number;
}
void OAIItem::setTrackNumber(const QString &track_number) {
    m_track_number = track_number;
    m_track_number_isSet = true;
}

bool OAIItem::is_track_number_Set() const{
    return m_track_number_isSet;
}

bool OAIItem::is_track_number_Valid() const{
    return m_track_number_isValid;
}

QString OAIItem::getTrackSide() const {
    return m_track_side;
}
void OAIItem::setTrackSide(const QString &track_side) {
    m_track_side = track_side;
    m_track_side_isSet = true;
}

bool OAIItem::is_track_side_Set() const{
    return m_track_side_isSet;
}

bool OAIItem::is_track_side_Valid() const{
    return m_track_side_isValid;
}

QString OAIItem::getType() const {
    return m_type;
}
void OAIItem::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIItem::is_type_Set() const{
    return m_type_isSet;
}

bool OAIItem::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAIItem::getUpdatedTime() const {
    return m_updated_time;
}
void OAIItem::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIItem::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIItem::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAIItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_catalogue_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contributions_mixin.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifiers.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ids.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_images_mixin.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_of.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_music_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offsets.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_partner_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_play_events.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_publisher_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_record_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recording_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_snippet_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_media_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_synopses.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_side_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_partner_isValid && m_pid_isValid && true;
}

} // namespace OpenAPI
