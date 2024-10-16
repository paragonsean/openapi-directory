/**
 * NHL v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPlay.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlay::OAIPlay(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlay::OAIPlay() {
    this->initializeModel();
}

OAIPlay::~OAIPlay() {}

void OAIPlay::initializeModel() {

    m_away_team_score_isSet = false;
    m_away_team_score_isValid = false;

    m_category_isSet = false;
    m_category_isValid = false;

    m_clock_minutes_isSet = false;
    m_clock_minutes_isValid = false;

    m_clock_seconds_isSet = false;
    m_clock_seconds_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_first_assisted_by_player_id_isSet = false;
    m_first_assisted_by_player_id_isValid = false;

    m_home_team_score_isSet = false;
    m_home_team_score_isValid = false;

    m_opponent_isSet = false;
    m_opponent_isValid = false;

    m_opponent_id_isSet = false;
    m_opponent_id_isValid = false;

    m_opposing_player_id_isSet = false;
    m_opposing_player_id_isValid = false;

    m_period_id_isSet = false;
    m_period_id_isValid = false;

    m_period_name_isSet = false;
    m_period_name_isValid = false;

    m_play_id_isSet = false;
    m_play_id_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_power_play_team_isSet = false;
    m_power_play_team_isValid = false;

    m_power_play_team_id_isSet = false;
    m_power_play_team_id_isValid = false;

    m_second_assisted_by_player_id_isSet = false;
    m_second_assisted_by_player_id_isValid = false;

    m_sequence_isSet = false;
    m_sequence_isValid = false;

    m_team_isSet = false;
    m_team_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;
}

void OAIPlay::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlay::fromJsonObject(QJsonObject json) {

    m_away_team_score_isValid = ::OpenAPI::fromJsonValue(m_away_team_score, json[QString("AwayTeamScore")]);
    m_away_team_score_isSet = !json[QString("AwayTeamScore")].isNull() && m_away_team_score_isValid;

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("Category")]);
    m_category_isSet = !json[QString("Category")].isNull() && m_category_isValid;

    m_clock_minutes_isValid = ::OpenAPI::fromJsonValue(m_clock_minutes, json[QString("ClockMinutes")]);
    m_clock_minutes_isSet = !json[QString("ClockMinutes")].isNull() && m_clock_minutes_isValid;

    m_clock_seconds_isValid = ::OpenAPI::fromJsonValue(m_clock_seconds, json[QString("ClockSeconds")]);
    m_clock_seconds_isSet = !json[QString("ClockSeconds")].isNull() && m_clock_seconds_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("Created")]);
    m_created_isSet = !json[QString("Created")].isNull() && m_created_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_first_assisted_by_player_id_isValid = ::OpenAPI::fromJsonValue(m_first_assisted_by_player_id, json[QString("FirstAssistedByPlayerID")]);
    m_first_assisted_by_player_id_isSet = !json[QString("FirstAssistedByPlayerID")].isNull() && m_first_assisted_by_player_id_isValid;

    m_home_team_score_isValid = ::OpenAPI::fromJsonValue(m_home_team_score, json[QString("HomeTeamScore")]);
    m_home_team_score_isSet = !json[QString("HomeTeamScore")].isNull() && m_home_team_score_isValid;

    m_opponent_isValid = ::OpenAPI::fromJsonValue(m_opponent, json[QString("Opponent")]);
    m_opponent_isSet = !json[QString("Opponent")].isNull() && m_opponent_isValid;

    m_opponent_id_isValid = ::OpenAPI::fromJsonValue(m_opponent_id, json[QString("OpponentID")]);
    m_opponent_id_isSet = !json[QString("OpponentID")].isNull() && m_opponent_id_isValid;

    m_opposing_player_id_isValid = ::OpenAPI::fromJsonValue(m_opposing_player_id, json[QString("OpposingPlayerID")]);
    m_opposing_player_id_isSet = !json[QString("OpposingPlayerID")].isNull() && m_opposing_player_id_isValid;

    m_period_id_isValid = ::OpenAPI::fromJsonValue(m_period_id, json[QString("PeriodID")]);
    m_period_id_isSet = !json[QString("PeriodID")].isNull() && m_period_id_isValid;

    m_period_name_isValid = ::OpenAPI::fromJsonValue(m_period_name, json[QString("PeriodName")]);
    m_period_name_isSet = !json[QString("PeriodName")].isNull() && m_period_name_isValid;

    m_play_id_isValid = ::OpenAPI::fromJsonValue(m_play_id, json[QString("PlayID")]);
    m_play_id_isSet = !json[QString("PlayID")].isNull() && m_play_id_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerID")]);
    m_player_id_isSet = !json[QString("PlayerID")].isNull() && m_player_id_isValid;

    m_power_play_team_isValid = ::OpenAPI::fromJsonValue(m_power_play_team, json[QString("PowerPlayTeam")]);
    m_power_play_team_isSet = !json[QString("PowerPlayTeam")].isNull() && m_power_play_team_isValid;

    m_power_play_team_id_isValid = ::OpenAPI::fromJsonValue(m_power_play_team_id, json[QString("PowerPlayTeamID")]);
    m_power_play_team_id_isSet = !json[QString("PowerPlayTeamID")].isNull() && m_power_play_team_id_isValid;

    m_second_assisted_by_player_id_isValid = ::OpenAPI::fromJsonValue(m_second_assisted_by_player_id, json[QString("SecondAssistedByPlayerID")]);
    m_second_assisted_by_player_id_isSet = !json[QString("SecondAssistedByPlayerID")].isNull() && m_second_assisted_by_player_id_isValid;

    m_sequence_isValid = ::OpenAPI::fromJsonValue(m_sequence, json[QString("Sequence")]);
    m_sequence_isSet = !json[QString("Sequence")].isNull() && m_sequence_isValid;

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("Team")]);
    m_team_isSet = !json[QString("Team")].isNull() && m_team_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamID")]);
    m_team_id_isSet = !json[QString("TeamID")].isNull() && m_team_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("Type")]);
    m_type_isSet = !json[QString("Type")].isNull() && m_type_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;
}

QString OAIPlay::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlay::asJsonObject() const {
    QJsonObject obj;
    if (m_away_team_score_isSet) {
        obj.insert(QString("AwayTeamScore"), ::OpenAPI::toJsonValue(m_away_team_score));
    }
    if (m_category_isSet) {
        obj.insert(QString("Category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_clock_minutes_isSet) {
        obj.insert(QString("ClockMinutes"), ::OpenAPI::toJsonValue(m_clock_minutes));
    }
    if (m_clock_seconds_isSet) {
        obj.insert(QString("ClockSeconds"), ::OpenAPI::toJsonValue(m_clock_seconds));
    }
    if (m_created_isSet) {
        obj.insert(QString("Created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_first_assisted_by_player_id_isSet) {
        obj.insert(QString("FirstAssistedByPlayerID"), ::OpenAPI::toJsonValue(m_first_assisted_by_player_id));
    }
    if (m_home_team_score_isSet) {
        obj.insert(QString("HomeTeamScore"), ::OpenAPI::toJsonValue(m_home_team_score));
    }
    if (m_opponent_isSet) {
        obj.insert(QString("Opponent"), ::OpenAPI::toJsonValue(m_opponent));
    }
    if (m_opponent_id_isSet) {
        obj.insert(QString("OpponentID"), ::OpenAPI::toJsonValue(m_opponent_id));
    }
    if (m_opposing_player_id_isSet) {
        obj.insert(QString("OpposingPlayerID"), ::OpenAPI::toJsonValue(m_opposing_player_id));
    }
    if (m_period_id_isSet) {
        obj.insert(QString("PeriodID"), ::OpenAPI::toJsonValue(m_period_id));
    }
    if (m_period_name_isSet) {
        obj.insert(QString("PeriodName"), ::OpenAPI::toJsonValue(m_period_name));
    }
    if (m_play_id_isSet) {
        obj.insert(QString("PlayID"), ::OpenAPI::toJsonValue(m_play_id));
    }
    if (m_player_id_isSet) {
        obj.insert(QString("PlayerID"), ::OpenAPI::toJsonValue(m_player_id));
    }
    if (m_power_play_team_isSet) {
        obj.insert(QString("PowerPlayTeam"), ::OpenAPI::toJsonValue(m_power_play_team));
    }
    if (m_power_play_team_id_isSet) {
        obj.insert(QString("PowerPlayTeamID"), ::OpenAPI::toJsonValue(m_power_play_team_id));
    }
    if (m_second_assisted_by_player_id_isSet) {
        obj.insert(QString("SecondAssistedByPlayerID"), ::OpenAPI::toJsonValue(m_second_assisted_by_player_id));
    }
    if (m_sequence_isSet) {
        obj.insert(QString("Sequence"), ::OpenAPI::toJsonValue(m_sequence));
    }
    if (m_team_isSet) {
        obj.insert(QString("Team"), ::OpenAPI::toJsonValue(m_team));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamID"), ::OpenAPI::toJsonValue(m_team_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("Type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    return obj;
}

qint32 OAIPlay::getAwayTeamScore() const {
    return m_away_team_score;
}
void OAIPlay::setAwayTeamScore(const qint32 &away_team_score) {
    m_away_team_score = away_team_score;
    m_away_team_score_isSet = true;
}

bool OAIPlay::is_away_team_score_Set() const{
    return m_away_team_score_isSet;
}

bool OAIPlay::is_away_team_score_Valid() const{
    return m_away_team_score_isValid;
}

QString OAIPlay::getCategory() const {
    return m_category;
}
void OAIPlay::setCategory(const QString &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAIPlay::is_category_Set() const{
    return m_category_isSet;
}

bool OAIPlay::is_category_Valid() const{
    return m_category_isValid;
}

qint32 OAIPlay::getClockMinutes() const {
    return m_clock_minutes;
}
void OAIPlay::setClockMinutes(const qint32 &clock_minutes) {
    m_clock_minutes = clock_minutes;
    m_clock_minutes_isSet = true;
}

bool OAIPlay::is_clock_minutes_Set() const{
    return m_clock_minutes_isSet;
}

bool OAIPlay::is_clock_minutes_Valid() const{
    return m_clock_minutes_isValid;
}

qint32 OAIPlay::getClockSeconds() const {
    return m_clock_seconds;
}
void OAIPlay::setClockSeconds(const qint32 &clock_seconds) {
    m_clock_seconds = clock_seconds;
    m_clock_seconds_isSet = true;
}

bool OAIPlay::is_clock_seconds_Set() const{
    return m_clock_seconds_isSet;
}

bool OAIPlay::is_clock_seconds_Valid() const{
    return m_clock_seconds_isValid;
}

QString OAIPlay::getCreated() const {
    return m_created;
}
void OAIPlay::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIPlay::is_created_Set() const{
    return m_created_isSet;
}

bool OAIPlay::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIPlay::getDescription() const {
    return m_description;
}
void OAIPlay::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIPlay::is_description_Set() const{
    return m_description_isSet;
}

bool OAIPlay::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIPlay::getFirstAssistedByPlayerId() const {
    return m_first_assisted_by_player_id;
}
void OAIPlay::setFirstAssistedByPlayerId(const qint32 &first_assisted_by_player_id) {
    m_first_assisted_by_player_id = first_assisted_by_player_id;
    m_first_assisted_by_player_id_isSet = true;
}

bool OAIPlay::is_first_assisted_by_player_id_Set() const{
    return m_first_assisted_by_player_id_isSet;
}

bool OAIPlay::is_first_assisted_by_player_id_Valid() const{
    return m_first_assisted_by_player_id_isValid;
}

qint32 OAIPlay::getHomeTeamScore() const {
    return m_home_team_score;
}
void OAIPlay::setHomeTeamScore(const qint32 &home_team_score) {
    m_home_team_score = home_team_score;
    m_home_team_score_isSet = true;
}

bool OAIPlay::is_home_team_score_Set() const{
    return m_home_team_score_isSet;
}

bool OAIPlay::is_home_team_score_Valid() const{
    return m_home_team_score_isValid;
}

QString OAIPlay::getOpponent() const {
    return m_opponent;
}
void OAIPlay::setOpponent(const QString &opponent) {
    m_opponent = opponent;
    m_opponent_isSet = true;
}

bool OAIPlay::is_opponent_Set() const{
    return m_opponent_isSet;
}

bool OAIPlay::is_opponent_Valid() const{
    return m_opponent_isValid;
}

qint32 OAIPlay::getOpponentId() const {
    return m_opponent_id;
}
void OAIPlay::setOpponentId(const qint32 &opponent_id) {
    m_opponent_id = opponent_id;
    m_opponent_id_isSet = true;
}

bool OAIPlay::is_opponent_id_Set() const{
    return m_opponent_id_isSet;
}

bool OAIPlay::is_opponent_id_Valid() const{
    return m_opponent_id_isValid;
}

qint32 OAIPlay::getOpposingPlayerId() const {
    return m_opposing_player_id;
}
void OAIPlay::setOpposingPlayerId(const qint32 &opposing_player_id) {
    m_opposing_player_id = opposing_player_id;
    m_opposing_player_id_isSet = true;
}

bool OAIPlay::is_opposing_player_id_Set() const{
    return m_opposing_player_id_isSet;
}

bool OAIPlay::is_opposing_player_id_Valid() const{
    return m_opposing_player_id_isValid;
}

qint32 OAIPlay::getPeriodId() const {
    return m_period_id;
}
void OAIPlay::setPeriodId(const qint32 &period_id) {
    m_period_id = period_id;
    m_period_id_isSet = true;
}

bool OAIPlay::is_period_id_Set() const{
    return m_period_id_isSet;
}

bool OAIPlay::is_period_id_Valid() const{
    return m_period_id_isValid;
}

QString OAIPlay::getPeriodName() const {
    return m_period_name;
}
void OAIPlay::setPeriodName(const QString &period_name) {
    m_period_name = period_name;
    m_period_name_isSet = true;
}

bool OAIPlay::is_period_name_Set() const{
    return m_period_name_isSet;
}

bool OAIPlay::is_period_name_Valid() const{
    return m_period_name_isValid;
}

qint32 OAIPlay::getPlayId() const {
    return m_play_id;
}
void OAIPlay::setPlayId(const qint32 &play_id) {
    m_play_id = play_id;
    m_play_id_isSet = true;
}

bool OAIPlay::is_play_id_Set() const{
    return m_play_id_isSet;
}

bool OAIPlay::is_play_id_Valid() const{
    return m_play_id_isValid;
}

qint32 OAIPlay::getPlayerId() const {
    return m_player_id;
}
void OAIPlay::setPlayerId(const qint32 &player_id) {
    m_player_id = player_id;
    m_player_id_isSet = true;
}

bool OAIPlay::is_player_id_Set() const{
    return m_player_id_isSet;
}

bool OAIPlay::is_player_id_Valid() const{
    return m_player_id_isValid;
}

QString OAIPlay::getPowerPlayTeam() const {
    return m_power_play_team;
}
void OAIPlay::setPowerPlayTeam(const QString &power_play_team) {
    m_power_play_team = power_play_team;
    m_power_play_team_isSet = true;
}

bool OAIPlay::is_power_play_team_Set() const{
    return m_power_play_team_isSet;
}

bool OAIPlay::is_power_play_team_Valid() const{
    return m_power_play_team_isValid;
}

qint32 OAIPlay::getPowerPlayTeamId() const {
    return m_power_play_team_id;
}
void OAIPlay::setPowerPlayTeamId(const qint32 &power_play_team_id) {
    m_power_play_team_id = power_play_team_id;
    m_power_play_team_id_isSet = true;
}

bool OAIPlay::is_power_play_team_id_Set() const{
    return m_power_play_team_id_isSet;
}

bool OAIPlay::is_power_play_team_id_Valid() const{
    return m_power_play_team_id_isValid;
}

qint32 OAIPlay::getSecondAssistedByPlayerId() const {
    return m_second_assisted_by_player_id;
}
void OAIPlay::setSecondAssistedByPlayerId(const qint32 &second_assisted_by_player_id) {
    m_second_assisted_by_player_id = second_assisted_by_player_id;
    m_second_assisted_by_player_id_isSet = true;
}

bool OAIPlay::is_second_assisted_by_player_id_Set() const{
    return m_second_assisted_by_player_id_isSet;
}

bool OAIPlay::is_second_assisted_by_player_id_Valid() const{
    return m_second_assisted_by_player_id_isValid;
}

qint32 OAIPlay::getSequence() const {
    return m_sequence;
}
void OAIPlay::setSequence(const qint32 &sequence) {
    m_sequence = sequence;
    m_sequence_isSet = true;
}

bool OAIPlay::is_sequence_Set() const{
    return m_sequence_isSet;
}

bool OAIPlay::is_sequence_Valid() const{
    return m_sequence_isValid;
}

QString OAIPlay::getTeam() const {
    return m_team;
}
void OAIPlay::setTeam(const QString &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAIPlay::is_team_Set() const{
    return m_team_isSet;
}

bool OAIPlay::is_team_Valid() const{
    return m_team_isValid;
}

qint32 OAIPlay::getTeamId() const {
    return m_team_id;
}
void OAIPlay::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAIPlay::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAIPlay::is_team_id_Valid() const{
    return m_team_id_isValid;
}

QString OAIPlay::getType() const {
    return m_type;
}
void OAIPlay::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPlay::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPlay::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIPlay::getUpdated() const {
    return m_updated;
}
void OAIPlay::setUpdated(const QString &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIPlay::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIPlay::is_updated_Valid() const{
    return m_updated_isValid;
}

bool OAIPlay::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_away_team_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_clock_minutes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_clock_seconds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_assisted_by_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_team_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_opponent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_opponent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_opposing_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_period_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_period_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_play_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_power_play_team_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_power_play_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_second_assisted_by_player_id_isSet) {
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

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
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

bool OAIPlay::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
