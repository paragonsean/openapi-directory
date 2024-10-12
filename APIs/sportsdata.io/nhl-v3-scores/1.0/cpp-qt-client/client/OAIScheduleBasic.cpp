/**
 * NHL v3 Scores
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIScheduleBasic.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIScheduleBasic::OAIScheduleBasic(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIScheduleBasic::OAIScheduleBasic() {
    this->initializeModel();
}

OAIScheduleBasic::~OAIScheduleBasic() {}

void OAIScheduleBasic::initializeModel() {

    m_away_team_isSet = false;
    m_away_team_isValid = false;

    m_away_team_id_isSet = false;
    m_away_team_id_isValid = false;

    m_away_team_score_isSet = false;
    m_away_team_score_isValid = false;

    m_date_time_isSet = false;
    m_date_time_isValid = false;

    m_date_time_utc_isSet = false;
    m_date_time_utc_isValid = false;

    m_day_isSet = false;
    m_day_isValid = false;

    m_game_end_date_time_isSet = false;
    m_game_end_date_time_isValid = false;

    m_game_id_isSet = false;
    m_game_id_isValid = false;

    m_global_away_team_id_isSet = false;
    m_global_away_team_id_isValid = false;

    m_global_game_id_isSet = false;
    m_global_game_id_isValid = false;

    m_global_home_team_id_isSet = false;
    m_global_home_team_id_isValid = false;

    m_home_team_isSet = false;
    m_home_team_isValid = false;

    m_home_team_id_isSet = false;
    m_home_team_id_isValid = false;

    m_home_team_score_isSet = false;
    m_home_team_score_isValid = false;

    m_is_closed_isSet = false;
    m_is_closed_isValid = false;

    m_neutral_venue_isSet = false;
    m_neutral_venue_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_season_type_isSet = false;
    m_season_type_isValid = false;

    m_series_info_isSet = false;
    m_series_info_isValid = false;

    m_stadium_id_isSet = false;
    m_stadium_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;
}

void OAIScheduleBasic::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIScheduleBasic::fromJsonObject(QJsonObject json) {

    m_away_team_isValid = ::OpenAPI::fromJsonValue(m_away_team, json[QString("AwayTeam")]);
    m_away_team_isSet = !json[QString("AwayTeam")].isNull() && m_away_team_isValid;

    m_away_team_id_isValid = ::OpenAPI::fromJsonValue(m_away_team_id, json[QString("AwayTeamID")]);
    m_away_team_id_isSet = !json[QString("AwayTeamID")].isNull() && m_away_team_id_isValid;

    m_away_team_score_isValid = ::OpenAPI::fromJsonValue(m_away_team_score, json[QString("AwayTeamScore")]);
    m_away_team_score_isSet = !json[QString("AwayTeamScore")].isNull() && m_away_team_score_isValid;

    m_date_time_isValid = ::OpenAPI::fromJsonValue(m_date_time, json[QString("DateTime")]);
    m_date_time_isSet = !json[QString("DateTime")].isNull() && m_date_time_isValid;

    m_date_time_utc_isValid = ::OpenAPI::fromJsonValue(m_date_time_utc, json[QString("DateTimeUTC")]);
    m_date_time_utc_isSet = !json[QString("DateTimeUTC")].isNull() && m_date_time_utc_isValid;

    m_day_isValid = ::OpenAPI::fromJsonValue(m_day, json[QString("Day")]);
    m_day_isSet = !json[QString("Day")].isNull() && m_day_isValid;

    m_game_end_date_time_isValid = ::OpenAPI::fromJsonValue(m_game_end_date_time, json[QString("GameEndDateTime")]);
    m_game_end_date_time_isSet = !json[QString("GameEndDateTime")].isNull() && m_game_end_date_time_isValid;

    m_game_id_isValid = ::OpenAPI::fromJsonValue(m_game_id, json[QString("GameID")]);
    m_game_id_isSet = !json[QString("GameID")].isNull() && m_game_id_isValid;

    m_global_away_team_id_isValid = ::OpenAPI::fromJsonValue(m_global_away_team_id, json[QString("GlobalAwayTeamID")]);
    m_global_away_team_id_isSet = !json[QString("GlobalAwayTeamID")].isNull() && m_global_away_team_id_isValid;

    m_global_game_id_isValid = ::OpenAPI::fromJsonValue(m_global_game_id, json[QString("GlobalGameID")]);
    m_global_game_id_isSet = !json[QString("GlobalGameID")].isNull() && m_global_game_id_isValid;

    m_global_home_team_id_isValid = ::OpenAPI::fromJsonValue(m_global_home_team_id, json[QString("GlobalHomeTeamID")]);
    m_global_home_team_id_isSet = !json[QString("GlobalHomeTeamID")].isNull() && m_global_home_team_id_isValid;

    m_home_team_isValid = ::OpenAPI::fromJsonValue(m_home_team, json[QString("HomeTeam")]);
    m_home_team_isSet = !json[QString("HomeTeam")].isNull() && m_home_team_isValid;

    m_home_team_id_isValid = ::OpenAPI::fromJsonValue(m_home_team_id, json[QString("HomeTeamID")]);
    m_home_team_id_isSet = !json[QString("HomeTeamID")].isNull() && m_home_team_id_isValid;

    m_home_team_score_isValid = ::OpenAPI::fromJsonValue(m_home_team_score, json[QString("HomeTeamScore")]);
    m_home_team_score_isSet = !json[QString("HomeTeamScore")].isNull() && m_home_team_score_isValid;

    m_is_closed_isValid = ::OpenAPI::fromJsonValue(m_is_closed, json[QString("IsClosed")]);
    m_is_closed_isSet = !json[QString("IsClosed")].isNull() && m_is_closed_isValid;

    m_neutral_venue_isValid = ::OpenAPI::fromJsonValue(m_neutral_venue, json[QString("NeutralVenue")]);
    m_neutral_venue_isSet = !json[QString("NeutralVenue")].isNull() && m_neutral_venue_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("Season")]);
    m_season_isSet = !json[QString("Season")].isNull() && m_season_isValid;

    m_season_type_isValid = ::OpenAPI::fromJsonValue(m_season_type, json[QString("SeasonType")]);
    m_season_type_isSet = !json[QString("SeasonType")].isNull() && m_season_type_isValid;

    m_series_info_isValid = ::OpenAPI::fromJsonValue(m_series_info, json[QString("SeriesInfo")]);
    m_series_info_isSet = !json[QString("SeriesInfo")].isNull() && m_series_info_isValid;

    m_stadium_id_isValid = ::OpenAPI::fromJsonValue(m_stadium_id, json[QString("StadiumID")]);
    m_stadium_id_isSet = !json[QString("StadiumID")].isNull() && m_stadium_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;
}

QString OAIScheduleBasic::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIScheduleBasic::asJsonObject() const {
    QJsonObject obj;
    if (m_away_team_isSet) {
        obj.insert(QString("AwayTeam"), ::OpenAPI::toJsonValue(m_away_team));
    }
    if (m_away_team_id_isSet) {
        obj.insert(QString("AwayTeamID"), ::OpenAPI::toJsonValue(m_away_team_id));
    }
    if (m_away_team_score_isSet) {
        obj.insert(QString("AwayTeamScore"), ::OpenAPI::toJsonValue(m_away_team_score));
    }
    if (m_date_time_isSet) {
        obj.insert(QString("DateTime"), ::OpenAPI::toJsonValue(m_date_time));
    }
    if (m_date_time_utc_isSet) {
        obj.insert(QString("DateTimeUTC"), ::OpenAPI::toJsonValue(m_date_time_utc));
    }
    if (m_day_isSet) {
        obj.insert(QString("Day"), ::OpenAPI::toJsonValue(m_day));
    }
    if (m_game_end_date_time_isSet) {
        obj.insert(QString("GameEndDateTime"), ::OpenAPI::toJsonValue(m_game_end_date_time));
    }
    if (m_game_id_isSet) {
        obj.insert(QString("GameID"), ::OpenAPI::toJsonValue(m_game_id));
    }
    if (m_global_away_team_id_isSet) {
        obj.insert(QString("GlobalAwayTeamID"), ::OpenAPI::toJsonValue(m_global_away_team_id));
    }
    if (m_global_game_id_isSet) {
        obj.insert(QString("GlobalGameID"), ::OpenAPI::toJsonValue(m_global_game_id));
    }
    if (m_global_home_team_id_isSet) {
        obj.insert(QString("GlobalHomeTeamID"), ::OpenAPI::toJsonValue(m_global_home_team_id));
    }
    if (m_home_team_isSet) {
        obj.insert(QString("HomeTeam"), ::OpenAPI::toJsonValue(m_home_team));
    }
    if (m_home_team_id_isSet) {
        obj.insert(QString("HomeTeamID"), ::OpenAPI::toJsonValue(m_home_team_id));
    }
    if (m_home_team_score_isSet) {
        obj.insert(QString("HomeTeamScore"), ::OpenAPI::toJsonValue(m_home_team_score));
    }
    if (m_is_closed_isSet) {
        obj.insert(QString("IsClosed"), ::OpenAPI::toJsonValue(m_is_closed));
    }
    if (m_neutral_venue_isSet) {
        obj.insert(QString("NeutralVenue"), ::OpenAPI::toJsonValue(m_neutral_venue));
    }
    if (m_season_isSet) {
        obj.insert(QString("Season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_season_type_isSet) {
        obj.insert(QString("SeasonType"), ::OpenAPI::toJsonValue(m_season_type));
    }
    if (m_series_info.isSet()) {
        obj.insert(QString("SeriesInfo"), ::OpenAPI::toJsonValue(m_series_info));
    }
    if (m_stadium_id_isSet) {
        obj.insert(QString("StadiumID"), ::OpenAPI::toJsonValue(m_stadium_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    return obj;
}

QString OAIScheduleBasic::getAwayTeam() const {
    return m_away_team;
}
void OAIScheduleBasic::setAwayTeam(const QString &away_team) {
    m_away_team = away_team;
    m_away_team_isSet = true;
}

bool OAIScheduleBasic::is_away_team_Set() const{
    return m_away_team_isSet;
}

bool OAIScheduleBasic::is_away_team_Valid() const{
    return m_away_team_isValid;
}

qint32 OAIScheduleBasic::getAwayTeamId() const {
    return m_away_team_id;
}
void OAIScheduleBasic::setAwayTeamId(const qint32 &away_team_id) {
    m_away_team_id = away_team_id;
    m_away_team_id_isSet = true;
}

bool OAIScheduleBasic::is_away_team_id_Set() const{
    return m_away_team_id_isSet;
}

bool OAIScheduleBasic::is_away_team_id_Valid() const{
    return m_away_team_id_isValid;
}

qint32 OAIScheduleBasic::getAwayTeamScore() const {
    return m_away_team_score;
}
void OAIScheduleBasic::setAwayTeamScore(const qint32 &away_team_score) {
    m_away_team_score = away_team_score;
    m_away_team_score_isSet = true;
}

bool OAIScheduleBasic::is_away_team_score_Set() const{
    return m_away_team_score_isSet;
}

bool OAIScheduleBasic::is_away_team_score_Valid() const{
    return m_away_team_score_isValid;
}

QString OAIScheduleBasic::getDateTime() const {
    return m_date_time;
}
void OAIScheduleBasic::setDateTime(const QString &date_time) {
    m_date_time = date_time;
    m_date_time_isSet = true;
}

bool OAIScheduleBasic::is_date_time_Set() const{
    return m_date_time_isSet;
}

bool OAIScheduleBasic::is_date_time_Valid() const{
    return m_date_time_isValid;
}

QString OAIScheduleBasic::getDateTimeUtc() const {
    return m_date_time_utc;
}
void OAIScheduleBasic::setDateTimeUtc(const QString &date_time_utc) {
    m_date_time_utc = date_time_utc;
    m_date_time_utc_isSet = true;
}

bool OAIScheduleBasic::is_date_time_utc_Set() const{
    return m_date_time_utc_isSet;
}

bool OAIScheduleBasic::is_date_time_utc_Valid() const{
    return m_date_time_utc_isValid;
}

QString OAIScheduleBasic::getDay() const {
    return m_day;
}
void OAIScheduleBasic::setDay(const QString &day) {
    m_day = day;
    m_day_isSet = true;
}

bool OAIScheduleBasic::is_day_Set() const{
    return m_day_isSet;
}

bool OAIScheduleBasic::is_day_Valid() const{
    return m_day_isValid;
}

QString OAIScheduleBasic::getGameEndDateTime() const {
    return m_game_end_date_time;
}
void OAIScheduleBasic::setGameEndDateTime(const QString &game_end_date_time) {
    m_game_end_date_time = game_end_date_time;
    m_game_end_date_time_isSet = true;
}

bool OAIScheduleBasic::is_game_end_date_time_Set() const{
    return m_game_end_date_time_isSet;
}

bool OAIScheduleBasic::is_game_end_date_time_Valid() const{
    return m_game_end_date_time_isValid;
}

qint32 OAIScheduleBasic::getGameId() const {
    return m_game_id;
}
void OAIScheduleBasic::setGameId(const qint32 &game_id) {
    m_game_id = game_id;
    m_game_id_isSet = true;
}

bool OAIScheduleBasic::is_game_id_Set() const{
    return m_game_id_isSet;
}

bool OAIScheduleBasic::is_game_id_Valid() const{
    return m_game_id_isValid;
}

qint32 OAIScheduleBasic::getGlobalAwayTeamId() const {
    return m_global_away_team_id;
}
void OAIScheduleBasic::setGlobalAwayTeamId(const qint32 &global_away_team_id) {
    m_global_away_team_id = global_away_team_id;
    m_global_away_team_id_isSet = true;
}

bool OAIScheduleBasic::is_global_away_team_id_Set() const{
    return m_global_away_team_id_isSet;
}

bool OAIScheduleBasic::is_global_away_team_id_Valid() const{
    return m_global_away_team_id_isValid;
}

qint32 OAIScheduleBasic::getGlobalGameId() const {
    return m_global_game_id;
}
void OAIScheduleBasic::setGlobalGameId(const qint32 &global_game_id) {
    m_global_game_id = global_game_id;
    m_global_game_id_isSet = true;
}

bool OAIScheduleBasic::is_global_game_id_Set() const{
    return m_global_game_id_isSet;
}

bool OAIScheduleBasic::is_global_game_id_Valid() const{
    return m_global_game_id_isValid;
}

qint32 OAIScheduleBasic::getGlobalHomeTeamId() const {
    return m_global_home_team_id;
}
void OAIScheduleBasic::setGlobalHomeTeamId(const qint32 &global_home_team_id) {
    m_global_home_team_id = global_home_team_id;
    m_global_home_team_id_isSet = true;
}

bool OAIScheduleBasic::is_global_home_team_id_Set() const{
    return m_global_home_team_id_isSet;
}

bool OAIScheduleBasic::is_global_home_team_id_Valid() const{
    return m_global_home_team_id_isValid;
}

QString OAIScheduleBasic::getHomeTeam() const {
    return m_home_team;
}
void OAIScheduleBasic::setHomeTeam(const QString &home_team) {
    m_home_team = home_team;
    m_home_team_isSet = true;
}

bool OAIScheduleBasic::is_home_team_Set() const{
    return m_home_team_isSet;
}

bool OAIScheduleBasic::is_home_team_Valid() const{
    return m_home_team_isValid;
}

qint32 OAIScheduleBasic::getHomeTeamId() const {
    return m_home_team_id;
}
void OAIScheduleBasic::setHomeTeamId(const qint32 &home_team_id) {
    m_home_team_id = home_team_id;
    m_home_team_id_isSet = true;
}

bool OAIScheduleBasic::is_home_team_id_Set() const{
    return m_home_team_id_isSet;
}

bool OAIScheduleBasic::is_home_team_id_Valid() const{
    return m_home_team_id_isValid;
}

qint32 OAIScheduleBasic::getHomeTeamScore() const {
    return m_home_team_score;
}
void OAIScheduleBasic::setHomeTeamScore(const qint32 &home_team_score) {
    m_home_team_score = home_team_score;
    m_home_team_score_isSet = true;
}

bool OAIScheduleBasic::is_home_team_score_Set() const{
    return m_home_team_score_isSet;
}

bool OAIScheduleBasic::is_home_team_score_Valid() const{
    return m_home_team_score_isValid;
}

bool OAIScheduleBasic::isIsClosed() const {
    return m_is_closed;
}
void OAIScheduleBasic::setIsClosed(const bool &is_closed) {
    m_is_closed = is_closed;
    m_is_closed_isSet = true;
}

bool OAIScheduleBasic::is_is_closed_Set() const{
    return m_is_closed_isSet;
}

bool OAIScheduleBasic::is_is_closed_Valid() const{
    return m_is_closed_isValid;
}

bool OAIScheduleBasic::isNeutralVenue() const {
    return m_neutral_venue;
}
void OAIScheduleBasic::setNeutralVenue(const bool &neutral_venue) {
    m_neutral_venue = neutral_venue;
    m_neutral_venue_isSet = true;
}

bool OAIScheduleBasic::is_neutral_venue_Set() const{
    return m_neutral_venue_isSet;
}

bool OAIScheduleBasic::is_neutral_venue_Valid() const{
    return m_neutral_venue_isValid;
}

qint32 OAIScheduleBasic::getSeason() const {
    return m_season;
}
void OAIScheduleBasic::setSeason(const qint32 &season) {
    m_season = season;
    m_season_isSet = true;
}

bool OAIScheduleBasic::is_season_Set() const{
    return m_season_isSet;
}

bool OAIScheduleBasic::is_season_Valid() const{
    return m_season_isValid;
}

qint32 OAIScheduleBasic::getSeasonType() const {
    return m_season_type;
}
void OAIScheduleBasic::setSeasonType(const qint32 &season_type) {
    m_season_type = season_type;
    m_season_type_isSet = true;
}

bool OAIScheduleBasic::is_season_type_Set() const{
    return m_season_type_isSet;
}

bool OAIScheduleBasic::is_season_type_Valid() const{
    return m_season_type_isValid;
}

OAISeries OAIScheduleBasic::getSeriesInfo() const {
    return m_series_info;
}
void OAIScheduleBasic::setSeriesInfo(const OAISeries &series_info) {
    m_series_info = series_info;
    m_series_info_isSet = true;
}

bool OAIScheduleBasic::is_series_info_Set() const{
    return m_series_info_isSet;
}

bool OAIScheduleBasic::is_series_info_Valid() const{
    return m_series_info_isValid;
}

qint32 OAIScheduleBasic::getStadiumId() const {
    return m_stadium_id;
}
void OAIScheduleBasic::setStadiumId(const qint32 &stadium_id) {
    m_stadium_id = stadium_id;
    m_stadium_id_isSet = true;
}

bool OAIScheduleBasic::is_stadium_id_Set() const{
    return m_stadium_id_isSet;
}

bool OAIScheduleBasic::is_stadium_id_Valid() const{
    return m_stadium_id_isValid;
}

QString OAIScheduleBasic::getStatus() const {
    return m_status;
}
void OAIScheduleBasic::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIScheduleBasic::is_status_Set() const{
    return m_status_isSet;
}

bool OAIScheduleBasic::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIScheduleBasic::getUpdated() const {
    return m_updated;
}
void OAIScheduleBasic::setUpdated(const QString &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIScheduleBasic::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIScheduleBasic::is_updated_Valid() const{
    return m_updated_isValid;
}

bool OAIScheduleBasic::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_away_team_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_away_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_away_team_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_time_utc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_day_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_end_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_away_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_game_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_home_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_team_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_team_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_closed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_neutral_venue_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_series_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_stadium_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIScheduleBasic::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
