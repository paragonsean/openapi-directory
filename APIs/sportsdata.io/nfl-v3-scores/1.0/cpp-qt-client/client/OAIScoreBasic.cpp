/**
 * NFL v3 Scores
 * NFL schedules, scores, odds, weather, and news API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIScoreBasic.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIScoreBasic::OAIScoreBasic(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIScoreBasic::OAIScoreBasic() {
    this->initializeModel();
}

OAIScoreBasic::~OAIScoreBasic() {}

void OAIScoreBasic::initializeModel() {

    m_away_score_isSet = false;
    m_away_score_isValid = false;

    m_away_team_isSet = false;
    m_away_team_isValid = false;

    m_away_team_id_isSet = false;
    m_away_team_id_isValid = false;

    m_canceled_isSet = false;
    m_canceled_isValid = false;

    m_closed_isSet = false;
    m_closed_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

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

    m_game_key_isSet = false;
    m_game_key_isValid = false;

    m_global_away_team_id_isSet = false;
    m_global_away_team_id_isValid = false;

    m_global_game_id_isSet = false;
    m_global_game_id_isValid = false;

    m_global_home_team_id_isSet = false;
    m_global_home_team_id_isValid = false;

    m_home_score_isSet = false;
    m_home_score_isValid = false;

    m_home_team_isSet = false;
    m_home_team_isValid = false;

    m_home_team_id_isSet = false;
    m_home_team_id_isValid = false;

    m_last_updated_isSet = false;
    m_last_updated_isValid = false;

    m_quarter_isSet = false;
    m_quarter_isValid = false;

    m_quarter_description_isSet = false;
    m_quarter_description_isValid = false;

    m_score_id_isSet = false;
    m_score_id_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_season_type_isSet = false;
    m_season_type_isValid = false;

    m_stadium_id_isSet = false;
    m_stadium_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_time_remaining_isSet = false;
    m_time_remaining_isValid = false;

    m_week_isSet = false;
    m_week_isValid = false;
}

void OAIScoreBasic::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIScoreBasic::fromJsonObject(QJsonObject json) {

    m_away_score_isValid = ::OpenAPI::fromJsonValue(m_away_score, json[QString("AwayScore")]);
    m_away_score_isSet = !json[QString("AwayScore")].isNull() && m_away_score_isValid;

    m_away_team_isValid = ::OpenAPI::fromJsonValue(m_away_team, json[QString("AwayTeam")]);
    m_away_team_isSet = !json[QString("AwayTeam")].isNull() && m_away_team_isValid;

    m_away_team_id_isValid = ::OpenAPI::fromJsonValue(m_away_team_id, json[QString("AwayTeamID")]);
    m_away_team_id_isSet = !json[QString("AwayTeamID")].isNull() && m_away_team_id_isValid;

    m_canceled_isValid = ::OpenAPI::fromJsonValue(m_canceled, json[QString("Canceled")]);
    m_canceled_isSet = !json[QString("Canceled")].isNull() && m_canceled_isValid;

    m_closed_isValid = ::OpenAPI::fromJsonValue(m_closed, json[QString("Closed")]);
    m_closed_isSet = !json[QString("Closed")].isNull() && m_closed_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("Date")]);
    m_date_isSet = !json[QString("Date")].isNull() && m_date_isValid;

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

    m_game_key_isValid = ::OpenAPI::fromJsonValue(m_game_key, json[QString("GameKey")]);
    m_game_key_isSet = !json[QString("GameKey")].isNull() && m_game_key_isValid;

    m_global_away_team_id_isValid = ::OpenAPI::fromJsonValue(m_global_away_team_id, json[QString("GlobalAwayTeamID")]);
    m_global_away_team_id_isSet = !json[QString("GlobalAwayTeamID")].isNull() && m_global_away_team_id_isValid;

    m_global_game_id_isValid = ::OpenAPI::fromJsonValue(m_global_game_id, json[QString("GlobalGameID")]);
    m_global_game_id_isSet = !json[QString("GlobalGameID")].isNull() && m_global_game_id_isValid;

    m_global_home_team_id_isValid = ::OpenAPI::fromJsonValue(m_global_home_team_id, json[QString("GlobalHomeTeamID")]);
    m_global_home_team_id_isSet = !json[QString("GlobalHomeTeamID")].isNull() && m_global_home_team_id_isValid;

    m_home_score_isValid = ::OpenAPI::fromJsonValue(m_home_score, json[QString("HomeScore")]);
    m_home_score_isSet = !json[QString("HomeScore")].isNull() && m_home_score_isValid;

    m_home_team_isValid = ::OpenAPI::fromJsonValue(m_home_team, json[QString("HomeTeam")]);
    m_home_team_isSet = !json[QString("HomeTeam")].isNull() && m_home_team_isValid;

    m_home_team_id_isValid = ::OpenAPI::fromJsonValue(m_home_team_id, json[QString("HomeTeamID")]);
    m_home_team_id_isSet = !json[QString("HomeTeamID")].isNull() && m_home_team_id_isValid;

    m_last_updated_isValid = ::OpenAPI::fromJsonValue(m_last_updated, json[QString("LastUpdated")]);
    m_last_updated_isSet = !json[QString("LastUpdated")].isNull() && m_last_updated_isValid;

    m_quarter_isValid = ::OpenAPI::fromJsonValue(m_quarter, json[QString("Quarter")]);
    m_quarter_isSet = !json[QString("Quarter")].isNull() && m_quarter_isValid;

    m_quarter_description_isValid = ::OpenAPI::fromJsonValue(m_quarter_description, json[QString("QuarterDescription")]);
    m_quarter_description_isSet = !json[QString("QuarterDescription")].isNull() && m_quarter_description_isValid;

    m_score_id_isValid = ::OpenAPI::fromJsonValue(m_score_id, json[QString("ScoreID")]);
    m_score_id_isSet = !json[QString("ScoreID")].isNull() && m_score_id_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("Season")]);
    m_season_isSet = !json[QString("Season")].isNull() && m_season_isValid;

    m_season_type_isValid = ::OpenAPI::fromJsonValue(m_season_type, json[QString("SeasonType")]);
    m_season_type_isSet = !json[QString("SeasonType")].isNull() && m_season_type_isValid;

    m_stadium_id_isValid = ::OpenAPI::fromJsonValue(m_stadium_id, json[QString("StadiumID")]);
    m_stadium_id_isSet = !json[QString("StadiumID")].isNull() && m_stadium_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;

    m_time_remaining_isValid = ::OpenAPI::fromJsonValue(m_time_remaining, json[QString("TimeRemaining")]);
    m_time_remaining_isSet = !json[QString("TimeRemaining")].isNull() && m_time_remaining_isValid;

    m_week_isValid = ::OpenAPI::fromJsonValue(m_week, json[QString("Week")]);
    m_week_isSet = !json[QString("Week")].isNull() && m_week_isValid;
}

QString OAIScoreBasic::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIScoreBasic::asJsonObject() const {
    QJsonObject obj;
    if (m_away_score_isSet) {
        obj.insert(QString("AwayScore"), ::OpenAPI::toJsonValue(m_away_score));
    }
    if (m_away_team_isSet) {
        obj.insert(QString("AwayTeam"), ::OpenAPI::toJsonValue(m_away_team));
    }
    if (m_away_team_id_isSet) {
        obj.insert(QString("AwayTeamID"), ::OpenAPI::toJsonValue(m_away_team_id));
    }
    if (m_canceled_isSet) {
        obj.insert(QString("Canceled"), ::OpenAPI::toJsonValue(m_canceled));
    }
    if (m_closed_isSet) {
        obj.insert(QString("Closed"), ::OpenAPI::toJsonValue(m_closed));
    }
    if (m_date_isSet) {
        obj.insert(QString("Date"), ::OpenAPI::toJsonValue(m_date));
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
    if (m_game_key_isSet) {
        obj.insert(QString("GameKey"), ::OpenAPI::toJsonValue(m_game_key));
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
    if (m_home_score_isSet) {
        obj.insert(QString("HomeScore"), ::OpenAPI::toJsonValue(m_home_score));
    }
    if (m_home_team_isSet) {
        obj.insert(QString("HomeTeam"), ::OpenAPI::toJsonValue(m_home_team));
    }
    if (m_home_team_id_isSet) {
        obj.insert(QString("HomeTeamID"), ::OpenAPI::toJsonValue(m_home_team_id));
    }
    if (m_last_updated_isSet) {
        obj.insert(QString("LastUpdated"), ::OpenAPI::toJsonValue(m_last_updated));
    }
    if (m_quarter_isSet) {
        obj.insert(QString("Quarter"), ::OpenAPI::toJsonValue(m_quarter));
    }
    if (m_quarter_description_isSet) {
        obj.insert(QString("QuarterDescription"), ::OpenAPI::toJsonValue(m_quarter_description));
    }
    if (m_score_id_isSet) {
        obj.insert(QString("ScoreID"), ::OpenAPI::toJsonValue(m_score_id));
    }
    if (m_season_isSet) {
        obj.insert(QString("Season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_season_type_isSet) {
        obj.insert(QString("SeasonType"), ::OpenAPI::toJsonValue(m_season_type));
    }
    if (m_stadium_id_isSet) {
        obj.insert(QString("StadiumID"), ::OpenAPI::toJsonValue(m_stadium_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_time_remaining_isSet) {
        obj.insert(QString("TimeRemaining"), ::OpenAPI::toJsonValue(m_time_remaining));
    }
    if (m_week_isSet) {
        obj.insert(QString("Week"), ::OpenAPI::toJsonValue(m_week));
    }
    return obj;
}

qint32 OAIScoreBasic::getAwayScore() const {
    return m_away_score;
}
void OAIScoreBasic::setAwayScore(const qint32 &away_score) {
    m_away_score = away_score;
    m_away_score_isSet = true;
}

bool OAIScoreBasic::is_away_score_Set() const{
    return m_away_score_isSet;
}

bool OAIScoreBasic::is_away_score_Valid() const{
    return m_away_score_isValid;
}

QString OAIScoreBasic::getAwayTeam() const {
    return m_away_team;
}
void OAIScoreBasic::setAwayTeam(const QString &away_team) {
    m_away_team = away_team;
    m_away_team_isSet = true;
}

bool OAIScoreBasic::is_away_team_Set() const{
    return m_away_team_isSet;
}

bool OAIScoreBasic::is_away_team_Valid() const{
    return m_away_team_isValid;
}

qint32 OAIScoreBasic::getAwayTeamId() const {
    return m_away_team_id;
}
void OAIScoreBasic::setAwayTeamId(const qint32 &away_team_id) {
    m_away_team_id = away_team_id;
    m_away_team_id_isSet = true;
}

bool OAIScoreBasic::is_away_team_id_Set() const{
    return m_away_team_id_isSet;
}

bool OAIScoreBasic::is_away_team_id_Valid() const{
    return m_away_team_id_isValid;
}

bool OAIScoreBasic::isCanceled() const {
    return m_canceled;
}
void OAIScoreBasic::setCanceled(const bool &canceled) {
    m_canceled = canceled;
    m_canceled_isSet = true;
}

bool OAIScoreBasic::is_canceled_Set() const{
    return m_canceled_isSet;
}

bool OAIScoreBasic::is_canceled_Valid() const{
    return m_canceled_isValid;
}

bool OAIScoreBasic::isClosed() const {
    return m_closed;
}
void OAIScoreBasic::setClosed(const bool &closed) {
    m_closed = closed;
    m_closed_isSet = true;
}

bool OAIScoreBasic::is_closed_Set() const{
    return m_closed_isSet;
}

bool OAIScoreBasic::is_closed_Valid() const{
    return m_closed_isValid;
}

QString OAIScoreBasic::getDate() const {
    return m_date;
}
void OAIScoreBasic::setDate(const QString &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIScoreBasic::is_date_Set() const{
    return m_date_isSet;
}

bool OAIScoreBasic::is_date_Valid() const{
    return m_date_isValid;
}

QString OAIScoreBasic::getDateTime() const {
    return m_date_time;
}
void OAIScoreBasic::setDateTime(const QString &date_time) {
    m_date_time = date_time;
    m_date_time_isSet = true;
}

bool OAIScoreBasic::is_date_time_Set() const{
    return m_date_time_isSet;
}

bool OAIScoreBasic::is_date_time_Valid() const{
    return m_date_time_isValid;
}

QString OAIScoreBasic::getDateTimeUtc() const {
    return m_date_time_utc;
}
void OAIScoreBasic::setDateTimeUtc(const QString &date_time_utc) {
    m_date_time_utc = date_time_utc;
    m_date_time_utc_isSet = true;
}

bool OAIScoreBasic::is_date_time_utc_Set() const{
    return m_date_time_utc_isSet;
}

bool OAIScoreBasic::is_date_time_utc_Valid() const{
    return m_date_time_utc_isValid;
}

QString OAIScoreBasic::getDay() const {
    return m_day;
}
void OAIScoreBasic::setDay(const QString &day) {
    m_day = day;
    m_day_isSet = true;
}

bool OAIScoreBasic::is_day_Set() const{
    return m_day_isSet;
}

bool OAIScoreBasic::is_day_Valid() const{
    return m_day_isValid;
}

QString OAIScoreBasic::getGameEndDateTime() const {
    return m_game_end_date_time;
}
void OAIScoreBasic::setGameEndDateTime(const QString &game_end_date_time) {
    m_game_end_date_time = game_end_date_time;
    m_game_end_date_time_isSet = true;
}

bool OAIScoreBasic::is_game_end_date_time_Set() const{
    return m_game_end_date_time_isSet;
}

bool OAIScoreBasic::is_game_end_date_time_Valid() const{
    return m_game_end_date_time_isValid;
}

qint32 OAIScoreBasic::getGameId() const {
    return m_game_id;
}
void OAIScoreBasic::setGameId(const qint32 &game_id) {
    m_game_id = game_id;
    m_game_id_isSet = true;
}

bool OAIScoreBasic::is_game_id_Set() const{
    return m_game_id_isSet;
}

bool OAIScoreBasic::is_game_id_Valid() const{
    return m_game_id_isValid;
}

QString OAIScoreBasic::getGameKey() const {
    return m_game_key;
}
void OAIScoreBasic::setGameKey(const QString &game_key) {
    m_game_key = game_key;
    m_game_key_isSet = true;
}

bool OAIScoreBasic::is_game_key_Set() const{
    return m_game_key_isSet;
}

bool OAIScoreBasic::is_game_key_Valid() const{
    return m_game_key_isValid;
}

qint32 OAIScoreBasic::getGlobalAwayTeamId() const {
    return m_global_away_team_id;
}
void OAIScoreBasic::setGlobalAwayTeamId(const qint32 &global_away_team_id) {
    m_global_away_team_id = global_away_team_id;
    m_global_away_team_id_isSet = true;
}

bool OAIScoreBasic::is_global_away_team_id_Set() const{
    return m_global_away_team_id_isSet;
}

bool OAIScoreBasic::is_global_away_team_id_Valid() const{
    return m_global_away_team_id_isValid;
}

qint32 OAIScoreBasic::getGlobalGameId() const {
    return m_global_game_id;
}
void OAIScoreBasic::setGlobalGameId(const qint32 &global_game_id) {
    m_global_game_id = global_game_id;
    m_global_game_id_isSet = true;
}

bool OAIScoreBasic::is_global_game_id_Set() const{
    return m_global_game_id_isSet;
}

bool OAIScoreBasic::is_global_game_id_Valid() const{
    return m_global_game_id_isValid;
}

qint32 OAIScoreBasic::getGlobalHomeTeamId() const {
    return m_global_home_team_id;
}
void OAIScoreBasic::setGlobalHomeTeamId(const qint32 &global_home_team_id) {
    m_global_home_team_id = global_home_team_id;
    m_global_home_team_id_isSet = true;
}

bool OAIScoreBasic::is_global_home_team_id_Set() const{
    return m_global_home_team_id_isSet;
}

bool OAIScoreBasic::is_global_home_team_id_Valid() const{
    return m_global_home_team_id_isValid;
}

qint32 OAIScoreBasic::getHomeScore() const {
    return m_home_score;
}
void OAIScoreBasic::setHomeScore(const qint32 &home_score) {
    m_home_score = home_score;
    m_home_score_isSet = true;
}

bool OAIScoreBasic::is_home_score_Set() const{
    return m_home_score_isSet;
}

bool OAIScoreBasic::is_home_score_Valid() const{
    return m_home_score_isValid;
}

QString OAIScoreBasic::getHomeTeam() const {
    return m_home_team;
}
void OAIScoreBasic::setHomeTeam(const QString &home_team) {
    m_home_team = home_team;
    m_home_team_isSet = true;
}

bool OAIScoreBasic::is_home_team_Set() const{
    return m_home_team_isSet;
}

bool OAIScoreBasic::is_home_team_Valid() const{
    return m_home_team_isValid;
}

qint32 OAIScoreBasic::getHomeTeamId() const {
    return m_home_team_id;
}
void OAIScoreBasic::setHomeTeamId(const qint32 &home_team_id) {
    m_home_team_id = home_team_id;
    m_home_team_id_isSet = true;
}

bool OAIScoreBasic::is_home_team_id_Set() const{
    return m_home_team_id_isSet;
}

bool OAIScoreBasic::is_home_team_id_Valid() const{
    return m_home_team_id_isValid;
}

QString OAIScoreBasic::getLastUpdated() const {
    return m_last_updated;
}
void OAIScoreBasic::setLastUpdated(const QString &last_updated) {
    m_last_updated = last_updated;
    m_last_updated_isSet = true;
}

bool OAIScoreBasic::is_last_updated_Set() const{
    return m_last_updated_isSet;
}

bool OAIScoreBasic::is_last_updated_Valid() const{
    return m_last_updated_isValid;
}

QString OAIScoreBasic::getQuarter() const {
    return m_quarter;
}
void OAIScoreBasic::setQuarter(const QString &quarter) {
    m_quarter = quarter;
    m_quarter_isSet = true;
}

bool OAIScoreBasic::is_quarter_Set() const{
    return m_quarter_isSet;
}

bool OAIScoreBasic::is_quarter_Valid() const{
    return m_quarter_isValid;
}

QString OAIScoreBasic::getQuarterDescription() const {
    return m_quarter_description;
}
void OAIScoreBasic::setQuarterDescription(const QString &quarter_description) {
    m_quarter_description = quarter_description;
    m_quarter_description_isSet = true;
}

bool OAIScoreBasic::is_quarter_description_Set() const{
    return m_quarter_description_isSet;
}

bool OAIScoreBasic::is_quarter_description_Valid() const{
    return m_quarter_description_isValid;
}

qint32 OAIScoreBasic::getScoreId() const {
    return m_score_id;
}
void OAIScoreBasic::setScoreId(const qint32 &score_id) {
    m_score_id = score_id;
    m_score_id_isSet = true;
}

bool OAIScoreBasic::is_score_id_Set() const{
    return m_score_id_isSet;
}

bool OAIScoreBasic::is_score_id_Valid() const{
    return m_score_id_isValid;
}

qint32 OAIScoreBasic::getSeason() const {
    return m_season;
}
void OAIScoreBasic::setSeason(const qint32 &season) {
    m_season = season;
    m_season_isSet = true;
}

bool OAIScoreBasic::is_season_Set() const{
    return m_season_isSet;
}

bool OAIScoreBasic::is_season_Valid() const{
    return m_season_isValid;
}

qint32 OAIScoreBasic::getSeasonType() const {
    return m_season_type;
}
void OAIScoreBasic::setSeasonType(const qint32 &season_type) {
    m_season_type = season_type;
    m_season_type_isSet = true;
}

bool OAIScoreBasic::is_season_type_Set() const{
    return m_season_type_isSet;
}

bool OAIScoreBasic::is_season_type_Valid() const{
    return m_season_type_isValid;
}

qint32 OAIScoreBasic::getStadiumId() const {
    return m_stadium_id;
}
void OAIScoreBasic::setStadiumId(const qint32 &stadium_id) {
    m_stadium_id = stadium_id;
    m_stadium_id_isSet = true;
}

bool OAIScoreBasic::is_stadium_id_Set() const{
    return m_stadium_id_isSet;
}

bool OAIScoreBasic::is_stadium_id_Valid() const{
    return m_stadium_id_isValid;
}

QString OAIScoreBasic::getStatus() const {
    return m_status;
}
void OAIScoreBasic::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIScoreBasic::is_status_Set() const{
    return m_status_isSet;
}

bool OAIScoreBasic::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIScoreBasic::getTimeRemaining() const {
    return m_time_remaining;
}
void OAIScoreBasic::setTimeRemaining(const QString &time_remaining) {
    m_time_remaining = time_remaining;
    m_time_remaining_isSet = true;
}

bool OAIScoreBasic::is_time_remaining_Set() const{
    return m_time_remaining_isSet;
}

bool OAIScoreBasic::is_time_remaining_Valid() const{
    return m_time_remaining_isValid;
}

qint32 OAIScoreBasic::getWeek() const {
    return m_week;
}
void OAIScoreBasic::setWeek(const qint32 &week) {
    m_week = week;
    m_week_isSet = true;
}

bool OAIScoreBasic::is_week_Set() const{
    return m_week_isSet;
}

bool OAIScoreBasic::is_week_Valid() const{
    return m_week_isValid;
}

bool OAIScoreBasic::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_away_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_away_team_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_away_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_canceled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_closed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_isSet) {
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

        if (m_game_key_isSet) {
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

        if (m_home_score_isSet) {
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

        if (m_last_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quarter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quarter_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_id_isSet) {
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

        if (m_stadium_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_remaining_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_week_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIScoreBasic::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
