/**
 * CFB v3 Scores
 * CFB schedules, scores, team stats, odds, weather, and news API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITeam.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITeam::OAITeam(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITeam::OAITeam() {
    this->initializeModel();
}

OAITeam::~OAITeam() {}

void OAITeam::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_ap_rank_isSet = false;
    m_ap_rank_isValid = false;

    m_coaches_rank_isSet = false;
    m_coaches_rank_isValid = false;

    m_conference_isSet = false;
    m_conference_isValid = false;

    m_conference_id_isSet = false;
    m_conference_id_isValid = false;

    m_conference_losses_isSet = false;
    m_conference_losses_isValid = false;

    m_conference_wins_isSet = false;
    m_conference_wins_isValid = false;

    m_global_team_id_isSet = false;
    m_global_team_id_isValid = false;

    m_key_isSet = false;
    m_key_isValid = false;

    m_losses_isSet = false;
    m_losses_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_playoff_rank_isSet = false;
    m_playoff_rank_isValid = false;

    m_rank_season_isSet = false;
    m_rank_season_isValid = false;

    m_rank_season_type_isSet = false;
    m_rank_season_type_isValid = false;

    m_rank_week_isSet = false;
    m_rank_week_isValid = false;

    m_school_isSet = false;
    m_school_isValid = false;

    m_short_display_name_isSet = false;
    m_short_display_name_isValid = false;

    m_stadium_id_isSet = false;
    m_stadium_id_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;

    m_team_logo_url_isSet = false;
    m_team_logo_url_isValid = false;

    m_wins_isSet = false;
    m_wins_isValid = false;
}

void OAITeam::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITeam::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("Active")]);
    m_active_isSet = !json[QString("Active")].isNull() && m_active_isValid;

    m_ap_rank_isValid = ::OpenAPI::fromJsonValue(m_ap_rank, json[QString("ApRank")]);
    m_ap_rank_isSet = !json[QString("ApRank")].isNull() && m_ap_rank_isValid;

    m_coaches_rank_isValid = ::OpenAPI::fromJsonValue(m_coaches_rank, json[QString("CoachesRank")]);
    m_coaches_rank_isSet = !json[QString("CoachesRank")].isNull() && m_coaches_rank_isValid;

    m_conference_isValid = ::OpenAPI::fromJsonValue(m_conference, json[QString("Conference")]);
    m_conference_isSet = !json[QString("Conference")].isNull() && m_conference_isValid;

    m_conference_id_isValid = ::OpenAPI::fromJsonValue(m_conference_id, json[QString("ConferenceID")]);
    m_conference_id_isSet = !json[QString("ConferenceID")].isNull() && m_conference_id_isValid;

    m_conference_losses_isValid = ::OpenAPI::fromJsonValue(m_conference_losses, json[QString("ConferenceLosses")]);
    m_conference_losses_isSet = !json[QString("ConferenceLosses")].isNull() && m_conference_losses_isValid;

    m_conference_wins_isValid = ::OpenAPI::fromJsonValue(m_conference_wins, json[QString("ConferenceWins")]);
    m_conference_wins_isSet = !json[QString("ConferenceWins")].isNull() && m_conference_wins_isValid;

    m_global_team_id_isValid = ::OpenAPI::fromJsonValue(m_global_team_id, json[QString("GlobalTeamID")]);
    m_global_team_id_isSet = !json[QString("GlobalTeamID")].isNull() && m_global_team_id_isValid;

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("Key")]);
    m_key_isSet = !json[QString("Key")].isNull() && m_key_isValid;

    m_losses_isValid = ::OpenAPI::fromJsonValue(m_losses, json[QString("Losses")]);
    m_losses_isSet = !json[QString("Losses")].isNull() && m_losses_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_playoff_rank_isValid = ::OpenAPI::fromJsonValue(m_playoff_rank, json[QString("PlayoffRank")]);
    m_playoff_rank_isSet = !json[QString("PlayoffRank")].isNull() && m_playoff_rank_isValid;

    m_rank_season_isValid = ::OpenAPI::fromJsonValue(m_rank_season, json[QString("RankSeason")]);
    m_rank_season_isSet = !json[QString("RankSeason")].isNull() && m_rank_season_isValid;

    m_rank_season_type_isValid = ::OpenAPI::fromJsonValue(m_rank_season_type, json[QString("RankSeasonType")]);
    m_rank_season_type_isSet = !json[QString("RankSeasonType")].isNull() && m_rank_season_type_isValid;

    m_rank_week_isValid = ::OpenAPI::fromJsonValue(m_rank_week, json[QString("RankWeek")]);
    m_rank_week_isSet = !json[QString("RankWeek")].isNull() && m_rank_week_isValid;

    m_school_isValid = ::OpenAPI::fromJsonValue(m_school, json[QString("School")]);
    m_school_isSet = !json[QString("School")].isNull() && m_school_isValid;

    m_short_display_name_isValid = ::OpenAPI::fromJsonValue(m_short_display_name, json[QString("ShortDisplayName")]);
    m_short_display_name_isSet = !json[QString("ShortDisplayName")].isNull() && m_short_display_name_isValid;

    m_stadium_id_isValid = ::OpenAPI::fromJsonValue(m_stadium_id, json[QString("StadiumID")]);
    m_stadium_id_isSet = !json[QString("StadiumID")].isNull() && m_stadium_id_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamID")]);
    m_team_id_isSet = !json[QString("TeamID")].isNull() && m_team_id_isValid;

    m_team_logo_url_isValid = ::OpenAPI::fromJsonValue(m_team_logo_url, json[QString("TeamLogoUrl")]);
    m_team_logo_url_isSet = !json[QString("TeamLogoUrl")].isNull() && m_team_logo_url_isValid;

    m_wins_isValid = ::OpenAPI::fromJsonValue(m_wins, json[QString("Wins")]);
    m_wins_isSet = !json[QString("Wins")].isNull() && m_wins_isValid;
}

QString OAITeam::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITeam::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("Active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_ap_rank_isSet) {
        obj.insert(QString("ApRank"), ::OpenAPI::toJsonValue(m_ap_rank));
    }
    if (m_coaches_rank_isSet) {
        obj.insert(QString("CoachesRank"), ::OpenAPI::toJsonValue(m_coaches_rank));
    }
    if (m_conference_isSet) {
        obj.insert(QString("Conference"), ::OpenAPI::toJsonValue(m_conference));
    }
    if (m_conference_id_isSet) {
        obj.insert(QString("ConferenceID"), ::OpenAPI::toJsonValue(m_conference_id));
    }
    if (m_conference_losses_isSet) {
        obj.insert(QString("ConferenceLosses"), ::OpenAPI::toJsonValue(m_conference_losses));
    }
    if (m_conference_wins_isSet) {
        obj.insert(QString("ConferenceWins"), ::OpenAPI::toJsonValue(m_conference_wins));
    }
    if (m_global_team_id_isSet) {
        obj.insert(QString("GlobalTeamID"), ::OpenAPI::toJsonValue(m_global_team_id));
    }
    if (m_key_isSet) {
        obj.insert(QString("Key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_losses_isSet) {
        obj.insert(QString("Losses"), ::OpenAPI::toJsonValue(m_losses));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_playoff_rank_isSet) {
        obj.insert(QString("PlayoffRank"), ::OpenAPI::toJsonValue(m_playoff_rank));
    }
    if (m_rank_season_isSet) {
        obj.insert(QString("RankSeason"), ::OpenAPI::toJsonValue(m_rank_season));
    }
    if (m_rank_season_type_isSet) {
        obj.insert(QString("RankSeasonType"), ::OpenAPI::toJsonValue(m_rank_season_type));
    }
    if (m_rank_week_isSet) {
        obj.insert(QString("RankWeek"), ::OpenAPI::toJsonValue(m_rank_week));
    }
    if (m_school_isSet) {
        obj.insert(QString("School"), ::OpenAPI::toJsonValue(m_school));
    }
    if (m_short_display_name_isSet) {
        obj.insert(QString("ShortDisplayName"), ::OpenAPI::toJsonValue(m_short_display_name));
    }
    if (m_stadium_id_isSet) {
        obj.insert(QString("StadiumID"), ::OpenAPI::toJsonValue(m_stadium_id));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamID"), ::OpenAPI::toJsonValue(m_team_id));
    }
    if (m_team_logo_url_isSet) {
        obj.insert(QString("TeamLogoUrl"), ::OpenAPI::toJsonValue(m_team_logo_url));
    }
    if (m_wins_isSet) {
        obj.insert(QString("Wins"), ::OpenAPI::toJsonValue(m_wins));
    }
    return obj;
}

bool OAITeam::isActive() const {
    return m_active;
}
void OAITeam::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAITeam::is_active_Set() const{
    return m_active_isSet;
}

bool OAITeam::is_active_Valid() const{
    return m_active_isValid;
}

qint32 OAITeam::getApRank() const {
    return m_ap_rank;
}
void OAITeam::setApRank(const qint32 &ap_rank) {
    m_ap_rank = ap_rank;
    m_ap_rank_isSet = true;
}

bool OAITeam::is_ap_rank_Set() const{
    return m_ap_rank_isSet;
}

bool OAITeam::is_ap_rank_Valid() const{
    return m_ap_rank_isValid;
}

qint32 OAITeam::getCoachesRank() const {
    return m_coaches_rank;
}
void OAITeam::setCoachesRank(const qint32 &coaches_rank) {
    m_coaches_rank = coaches_rank;
    m_coaches_rank_isSet = true;
}

bool OAITeam::is_coaches_rank_Set() const{
    return m_coaches_rank_isSet;
}

bool OAITeam::is_coaches_rank_Valid() const{
    return m_coaches_rank_isValid;
}

QString OAITeam::getConference() const {
    return m_conference;
}
void OAITeam::setConference(const QString &conference) {
    m_conference = conference;
    m_conference_isSet = true;
}

bool OAITeam::is_conference_Set() const{
    return m_conference_isSet;
}

bool OAITeam::is_conference_Valid() const{
    return m_conference_isValid;
}

qint32 OAITeam::getConferenceId() const {
    return m_conference_id;
}
void OAITeam::setConferenceId(const qint32 &conference_id) {
    m_conference_id = conference_id;
    m_conference_id_isSet = true;
}

bool OAITeam::is_conference_id_Set() const{
    return m_conference_id_isSet;
}

bool OAITeam::is_conference_id_Valid() const{
    return m_conference_id_isValid;
}

qint32 OAITeam::getConferenceLosses() const {
    return m_conference_losses;
}
void OAITeam::setConferenceLosses(const qint32 &conference_losses) {
    m_conference_losses = conference_losses;
    m_conference_losses_isSet = true;
}

bool OAITeam::is_conference_losses_Set() const{
    return m_conference_losses_isSet;
}

bool OAITeam::is_conference_losses_Valid() const{
    return m_conference_losses_isValid;
}

qint32 OAITeam::getConferenceWins() const {
    return m_conference_wins;
}
void OAITeam::setConferenceWins(const qint32 &conference_wins) {
    m_conference_wins = conference_wins;
    m_conference_wins_isSet = true;
}

bool OAITeam::is_conference_wins_Set() const{
    return m_conference_wins_isSet;
}

bool OAITeam::is_conference_wins_Valid() const{
    return m_conference_wins_isValid;
}

qint32 OAITeam::getGlobalTeamId() const {
    return m_global_team_id;
}
void OAITeam::setGlobalTeamId(const qint32 &global_team_id) {
    m_global_team_id = global_team_id;
    m_global_team_id_isSet = true;
}

bool OAITeam::is_global_team_id_Set() const{
    return m_global_team_id_isSet;
}

bool OAITeam::is_global_team_id_Valid() const{
    return m_global_team_id_isValid;
}

QString OAITeam::getKey() const {
    return m_key;
}
void OAITeam::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAITeam::is_key_Set() const{
    return m_key_isSet;
}

bool OAITeam::is_key_Valid() const{
    return m_key_isValid;
}

qint32 OAITeam::getLosses() const {
    return m_losses;
}
void OAITeam::setLosses(const qint32 &losses) {
    m_losses = losses;
    m_losses_isSet = true;
}

bool OAITeam::is_losses_Set() const{
    return m_losses_isSet;
}

bool OAITeam::is_losses_Valid() const{
    return m_losses_isValid;
}

QString OAITeam::getName() const {
    return m_name;
}
void OAITeam::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITeam::is_name_Set() const{
    return m_name_isSet;
}

bool OAITeam::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAITeam::getPlayoffRank() const {
    return m_playoff_rank;
}
void OAITeam::setPlayoffRank(const qint32 &playoff_rank) {
    m_playoff_rank = playoff_rank;
    m_playoff_rank_isSet = true;
}

bool OAITeam::is_playoff_rank_Set() const{
    return m_playoff_rank_isSet;
}

bool OAITeam::is_playoff_rank_Valid() const{
    return m_playoff_rank_isValid;
}

qint32 OAITeam::getRankSeason() const {
    return m_rank_season;
}
void OAITeam::setRankSeason(const qint32 &rank_season) {
    m_rank_season = rank_season;
    m_rank_season_isSet = true;
}

bool OAITeam::is_rank_season_Set() const{
    return m_rank_season_isSet;
}

bool OAITeam::is_rank_season_Valid() const{
    return m_rank_season_isValid;
}

qint32 OAITeam::getRankSeasonType() const {
    return m_rank_season_type;
}
void OAITeam::setRankSeasonType(const qint32 &rank_season_type) {
    m_rank_season_type = rank_season_type;
    m_rank_season_type_isSet = true;
}

bool OAITeam::is_rank_season_type_Set() const{
    return m_rank_season_type_isSet;
}

bool OAITeam::is_rank_season_type_Valid() const{
    return m_rank_season_type_isValid;
}

qint32 OAITeam::getRankWeek() const {
    return m_rank_week;
}
void OAITeam::setRankWeek(const qint32 &rank_week) {
    m_rank_week = rank_week;
    m_rank_week_isSet = true;
}

bool OAITeam::is_rank_week_Set() const{
    return m_rank_week_isSet;
}

bool OAITeam::is_rank_week_Valid() const{
    return m_rank_week_isValid;
}

QString OAITeam::getSchool() const {
    return m_school;
}
void OAITeam::setSchool(const QString &school) {
    m_school = school;
    m_school_isSet = true;
}

bool OAITeam::is_school_Set() const{
    return m_school_isSet;
}

bool OAITeam::is_school_Valid() const{
    return m_school_isValid;
}

QString OAITeam::getShortDisplayName() const {
    return m_short_display_name;
}
void OAITeam::setShortDisplayName(const QString &short_display_name) {
    m_short_display_name = short_display_name;
    m_short_display_name_isSet = true;
}

bool OAITeam::is_short_display_name_Set() const{
    return m_short_display_name_isSet;
}

bool OAITeam::is_short_display_name_Valid() const{
    return m_short_display_name_isValid;
}

qint32 OAITeam::getStadiumId() const {
    return m_stadium_id;
}
void OAITeam::setStadiumId(const qint32 &stadium_id) {
    m_stadium_id = stadium_id;
    m_stadium_id_isSet = true;
}

bool OAITeam::is_stadium_id_Set() const{
    return m_stadium_id_isSet;
}

bool OAITeam::is_stadium_id_Valid() const{
    return m_stadium_id_isValid;
}

qint32 OAITeam::getTeamId() const {
    return m_team_id;
}
void OAITeam::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAITeam::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAITeam::is_team_id_Valid() const{
    return m_team_id_isValid;
}

QString OAITeam::getTeamLogoUrl() const {
    return m_team_logo_url;
}
void OAITeam::setTeamLogoUrl(const QString &team_logo_url) {
    m_team_logo_url = team_logo_url;
    m_team_logo_url_isSet = true;
}

bool OAITeam::is_team_logo_url_Set() const{
    return m_team_logo_url_isSet;
}

bool OAITeam::is_team_logo_url_Valid() const{
    return m_team_logo_url_isValid;
}

qint32 OAITeam::getWins() const {
    return m_wins;
}
void OAITeam::setWins(const qint32 &wins) {
    m_wins = wins;
    m_wins_isSet = true;
}

bool OAITeam::is_wins_Set() const{
    return m_wins_isSet;
}

bool OAITeam::is_wins_Valid() const{
    return m_wins_isValid;
}

bool OAITeam::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ap_rank_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coaches_rank_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conference_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conference_losses_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conference_wins_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_losses_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_playoff_rank_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rank_season_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rank_season_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rank_week_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_school_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stadium_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_logo_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wins_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITeam::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
