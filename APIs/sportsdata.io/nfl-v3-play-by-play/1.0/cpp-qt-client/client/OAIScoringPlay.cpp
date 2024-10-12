/**
 * NFL v3 Play-by-Play
 * NFL play-by-play API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIScoringPlay.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIScoringPlay::OAIScoringPlay(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIScoringPlay::OAIScoringPlay() {
    this->initializeModel();
}

OAIScoringPlay::~OAIScoringPlay() {}

void OAIScoringPlay::initializeModel() {

    m_away_score_isSet = false;
    m_away_score_isValid = false;

    m_away_team_isSet = false;
    m_away_team_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_game_key_isSet = false;
    m_game_key_isValid = false;

    m_home_score_isSet = false;
    m_home_score_isValid = false;

    m_home_team_isSet = false;
    m_home_team_isValid = false;

    m_play_description_isSet = false;
    m_play_description_isValid = false;

    m_quarter_isSet = false;
    m_quarter_isValid = false;

    m_score_id_isSet = false;
    m_score_id_isValid = false;

    m_scoring_play_id_isSet = false;
    m_scoring_play_id_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_season_type_isSet = false;
    m_season_type_isValid = false;

    m_sequence_isSet = false;
    m_sequence_isValid = false;

    m_team_isSet = false;
    m_team_isValid = false;

    m_time_remaining_isSet = false;
    m_time_remaining_isValid = false;

    m_week_isSet = false;
    m_week_isValid = false;
}

void OAIScoringPlay::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIScoringPlay::fromJsonObject(QJsonObject json) {

    m_away_score_isValid = ::OpenAPI::fromJsonValue(m_away_score, json[QString("AwayScore")]);
    m_away_score_isSet = !json[QString("AwayScore")].isNull() && m_away_score_isValid;

    m_away_team_isValid = ::OpenAPI::fromJsonValue(m_away_team, json[QString("AwayTeam")]);
    m_away_team_isSet = !json[QString("AwayTeam")].isNull() && m_away_team_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("Date")]);
    m_date_isSet = !json[QString("Date")].isNull() && m_date_isValid;

    m_game_key_isValid = ::OpenAPI::fromJsonValue(m_game_key, json[QString("GameKey")]);
    m_game_key_isSet = !json[QString("GameKey")].isNull() && m_game_key_isValid;

    m_home_score_isValid = ::OpenAPI::fromJsonValue(m_home_score, json[QString("HomeScore")]);
    m_home_score_isSet = !json[QString("HomeScore")].isNull() && m_home_score_isValid;

    m_home_team_isValid = ::OpenAPI::fromJsonValue(m_home_team, json[QString("HomeTeam")]);
    m_home_team_isSet = !json[QString("HomeTeam")].isNull() && m_home_team_isValid;

    m_play_description_isValid = ::OpenAPI::fromJsonValue(m_play_description, json[QString("PlayDescription")]);
    m_play_description_isSet = !json[QString("PlayDescription")].isNull() && m_play_description_isValid;

    m_quarter_isValid = ::OpenAPI::fromJsonValue(m_quarter, json[QString("Quarter")]);
    m_quarter_isSet = !json[QString("Quarter")].isNull() && m_quarter_isValid;

    m_score_id_isValid = ::OpenAPI::fromJsonValue(m_score_id, json[QString("ScoreID")]);
    m_score_id_isSet = !json[QString("ScoreID")].isNull() && m_score_id_isValid;

    m_scoring_play_id_isValid = ::OpenAPI::fromJsonValue(m_scoring_play_id, json[QString("ScoringPlayID")]);
    m_scoring_play_id_isSet = !json[QString("ScoringPlayID")].isNull() && m_scoring_play_id_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("Season")]);
    m_season_isSet = !json[QString("Season")].isNull() && m_season_isValid;

    m_season_type_isValid = ::OpenAPI::fromJsonValue(m_season_type, json[QString("SeasonType")]);
    m_season_type_isSet = !json[QString("SeasonType")].isNull() && m_season_type_isValid;

    m_sequence_isValid = ::OpenAPI::fromJsonValue(m_sequence, json[QString("Sequence")]);
    m_sequence_isSet = !json[QString("Sequence")].isNull() && m_sequence_isValid;

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("Team")]);
    m_team_isSet = !json[QString("Team")].isNull() && m_team_isValid;

    m_time_remaining_isValid = ::OpenAPI::fromJsonValue(m_time_remaining, json[QString("TimeRemaining")]);
    m_time_remaining_isSet = !json[QString("TimeRemaining")].isNull() && m_time_remaining_isValid;

    m_week_isValid = ::OpenAPI::fromJsonValue(m_week, json[QString("Week")]);
    m_week_isSet = !json[QString("Week")].isNull() && m_week_isValid;
}

QString OAIScoringPlay::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIScoringPlay::asJsonObject() const {
    QJsonObject obj;
    if (m_away_score_isSet) {
        obj.insert(QString("AwayScore"), ::OpenAPI::toJsonValue(m_away_score));
    }
    if (m_away_team_isSet) {
        obj.insert(QString("AwayTeam"), ::OpenAPI::toJsonValue(m_away_team));
    }
    if (m_date_isSet) {
        obj.insert(QString("Date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_game_key_isSet) {
        obj.insert(QString("GameKey"), ::OpenAPI::toJsonValue(m_game_key));
    }
    if (m_home_score_isSet) {
        obj.insert(QString("HomeScore"), ::OpenAPI::toJsonValue(m_home_score));
    }
    if (m_home_team_isSet) {
        obj.insert(QString("HomeTeam"), ::OpenAPI::toJsonValue(m_home_team));
    }
    if (m_play_description_isSet) {
        obj.insert(QString("PlayDescription"), ::OpenAPI::toJsonValue(m_play_description));
    }
    if (m_quarter_isSet) {
        obj.insert(QString("Quarter"), ::OpenAPI::toJsonValue(m_quarter));
    }
    if (m_score_id_isSet) {
        obj.insert(QString("ScoreID"), ::OpenAPI::toJsonValue(m_score_id));
    }
    if (m_scoring_play_id_isSet) {
        obj.insert(QString("ScoringPlayID"), ::OpenAPI::toJsonValue(m_scoring_play_id));
    }
    if (m_season_isSet) {
        obj.insert(QString("Season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_season_type_isSet) {
        obj.insert(QString("SeasonType"), ::OpenAPI::toJsonValue(m_season_type));
    }
    if (m_sequence_isSet) {
        obj.insert(QString("Sequence"), ::OpenAPI::toJsonValue(m_sequence));
    }
    if (m_team_isSet) {
        obj.insert(QString("Team"), ::OpenAPI::toJsonValue(m_team));
    }
    if (m_time_remaining_isSet) {
        obj.insert(QString("TimeRemaining"), ::OpenAPI::toJsonValue(m_time_remaining));
    }
    if (m_week_isSet) {
        obj.insert(QString("Week"), ::OpenAPI::toJsonValue(m_week));
    }
    return obj;
}

qint32 OAIScoringPlay::getAwayScore() const {
    return m_away_score;
}
void OAIScoringPlay::setAwayScore(const qint32 &away_score) {
    m_away_score = away_score;
    m_away_score_isSet = true;
}

bool OAIScoringPlay::is_away_score_Set() const{
    return m_away_score_isSet;
}

bool OAIScoringPlay::is_away_score_Valid() const{
    return m_away_score_isValid;
}

QString OAIScoringPlay::getAwayTeam() const {
    return m_away_team;
}
void OAIScoringPlay::setAwayTeam(const QString &away_team) {
    m_away_team = away_team;
    m_away_team_isSet = true;
}

bool OAIScoringPlay::is_away_team_Set() const{
    return m_away_team_isSet;
}

bool OAIScoringPlay::is_away_team_Valid() const{
    return m_away_team_isValid;
}

QString OAIScoringPlay::getDate() const {
    return m_date;
}
void OAIScoringPlay::setDate(const QString &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIScoringPlay::is_date_Set() const{
    return m_date_isSet;
}

bool OAIScoringPlay::is_date_Valid() const{
    return m_date_isValid;
}

QString OAIScoringPlay::getGameKey() const {
    return m_game_key;
}
void OAIScoringPlay::setGameKey(const QString &game_key) {
    m_game_key = game_key;
    m_game_key_isSet = true;
}

bool OAIScoringPlay::is_game_key_Set() const{
    return m_game_key_isSet;
}

bool OAIScoringPlay::is_game_key_Valid() const{
    return m_game_key_isValid;
}

qint32 OAIScoringPlay::getHomeScore() const {
    return m_home_score;
}
void OAIScoringPlay::setHomeScore(const qint32 &home_score) {
    m_home_score = home_score;
    m_home_score_isSet = true;
}

bool OAIScoringPlay::is_home_score_Set() const{
    return m_home_score_isSet;
}

bool OAIScoringPlay::is_home_score_Valid() const{
    return m_home_score_isValid;
}

QString OAIScoringPlay::getHomeTeam() const {
    return m_home_team;
}
void OAIScoringPlay::setHomeTeam(const QString &home_team) {
    m_home_team = home_team;
    m_home_team_isSet = true;
}

bool OAIScoringPlay::is_home_team_Set() const{
    return m_home_team_isSet;
}

bool OAIScoringPlay::is_home_team_Valid() const{
    return m_home_team_isValid;
}

QString OAIScoringPlay::getPlayDescription() const {
    return m_play_description;
}
void OAIScoringPlay::setPlayDescription(const QString &play_description) {
    m_play_description = play_description;
    m_play_description_isSet = true;
}

bool OAIScoringPlay::is_play_description_Set() const{
    return m_play_description_isSet;
}

bool OAIScoringPlay::is_play_description_Valid() const{
    return m_play_description_isValid;
}

QString OAIScoringPlay::getQuarter() const {
    return m_quarter;
}
void OAIScoringPlay::setQuarter(const QString &quarter) {
    m_quarter = quarter;
    m_quarter_isSet = true;
}

bool OAIScoringPlay::is_quarter_Set() const{
    return m_quarter_isSet;
}

bool OAIScoringPlay::is_quarter_Valid() const{
    return m_quarter_isValid;
}

qint32 OAIScoringPlay::getScoreId() const {
    return m_score_id;
}
void OAIScoringPlay::setScoreId(const qint32 &score_id) {
    m_score_id = score_id;
    m_score_id_isSet = true;
}

bool OAIScoringPlay::is_score_id_Set() const{
    return m_score_id_isSet;
}

bool OAIScoringPlay::is_score_id_Valid() const{
    return m_score_id_isValid;
}

qint32 OAIScoringPlay::getScoringPlayId() const {
    return m_scoring_play_id;
}
void OAIScoringPlay::setScoringPlayId(const qint32 &scoring_play_id) {
    m_scoring_play_id = scoring_play_id;
    m_scoring_play_id_isSet = true;
}

bool OAIScoringPlay::is_scoring_play_id_Set() const{
    return m_scoring_play_id_isSet;
}

bool OAIScoringPlay::is_scoring_play_id_Valid() const{
    return m_scoring_play_id_isValid;
}

qint32 OAIScoringPlay::getSeason() const {
    return m_season;
}
void OAIScoringPlay::setSeason(const qint32 &season) {
    m_season = season;
    m_season_isSet = true;
}

bool OAIScoringPlay::is_season_Set() const{
    return m_season_isSet;
}

bool OAIScoringPlay::is_season_Valid() const{
    return m_season_isValid;
}

qint32 OAIScoringPlay::getSeasonType() const {
    return m_season_type;
}
void OAIScoringPlay::setSeasonType(const qint32 &season_type) {
    m_season_type = season_type;
    m_season_type_isSet = true;
}

bool OAIScoringPlay::is_season_type_Set() const{
    return m_season_type_isSet;
}

bool OAIScoringPlay::is_season_type_Valid() const{
    return m_season_type_isValid;
}

qint32 OAIScoringPlay::getSequence() const {
    return m_sequence;
}
void OAIScoringPlay::setSequence(const qint32 &sequence) {
    m_sequence = sequence;
    m_sequence_isSet = true;
}

bool OAIScoringPlay::is_sequence_Set() const{
    return m_sequence_isSet;
}

bool OAIScoringPlay::is_sequence_Valid() const{
    return m_sequence_isValid;
}

QString OAIScoringPlay::getTeam() const {
    return m_team;
}
void OAIScoringPlay::setTeam(const QString &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAIScoringPlay::is_team_Set() const{
    return m_team_isSet;
}

bool OAIScoringPlay::is_team_Valid() const{
    return m_team_isValid;
}

QString OAIScoringPlay::getTimeRemaining() const {
    return m_time_remaining;
}
void OAIScoringPlay::setTimeRemaining(const QString &time_remaining) {
    m_time_remaining = time_remaining;
    m_time_remaining_isSet = true;
}

bool OAIScoringPlay::is_time_remaining_Set() const{
    return m_time_remaining_isSet;
}

bool OAIScoringPlay::is_time_remaining_Valid() const{
    return m_time_remaining_isValid;
}

qint32 OAIScoringPlay::getWeek() const {
    return m_week;
}
void OAIScoringPlay::setWeek(const qint32 &week) {
    m_week = week;
    m_week_isSet = true;
}

bool OAIScoringPlay::is_week_Set() const{
    return m_week_isSet;
}

bool OAIScoringPlay::is_week_Valid() const{
    return m_week_isValid;
}

bool OAIScoringPlay::isSet() const {
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

        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_key_isSet) {
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

        if (m_play_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quarter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scoring_play_id_isSet) {
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

        if (m_sequence_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_isSet) {
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

bool OAIScoringPlay::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
