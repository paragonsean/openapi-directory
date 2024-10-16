/**
 * NFL v3 Stats
 * NFL rosters, player stats, team stats, and fantasy stats API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPlayerRushing.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlayerRushing::OAIPlayerRushing(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlayerRushing::OAIPlayerRushing() {
    this->initializeModel();
}

OAIPlayerRushing::~OAIPlayerRushing() {}

void OAIPlayerRushing::initializeModel() {

    m_fantasy_points_isSet = false;
    m_fantasy_points_isValid = false;

    m_fantasy_position_isSet = false;
    m_fantasy_position_isValid = false;

    m_fumbles_lost_isSet = false;
    m_fumbles_lost_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_player_game_id_isSet = false;
    m_player_game_id_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_position_category_isSet = false;
    m_position_category_isValid = false;

    m_rushing_attempts_isSet = false;
    m_rushing_attempts_isValid = false;

    m_rushing_long_isSet = false;
    m_rushing_long_isValid = false;

    m_rushing_touchdowns_isSet = false;
    m_rushing_touchdowns_isValid = false;

    m_rushing_yards_isSet = false;
    m_rushing_yards_isValid = false;

    m_rushing_yards_per_attempt_isSet = false;
    m_rushing_yards_per_attempt_isValid = false;

    m_short_name_isSet = false;
    m_short_name_isValid = false;

    m_team_isSet = false;
    m_team_isValid = false;

    m_two_point_conversion_runs_isSet = false;
    m_two_point_conversion_runs_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;
}

void OAIPlayerRushing::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlayerRushing::fromJsonObject(QJsonObject json) {

    m_fantasy_points_isValid = ::OpenAPI::fromJsonValue(m_fantasy_points, json[QString("FantasyPoints")]);
    m_fantasy_points_isSet = !json[QString("FantasyPoints")].isNull() && m_fantasy_points_isValid;

    m_fantasy_position_isValid = ::OpenAPI::fromJsonValue(m_fantasy_position, json[QString("FantasyPosition")]);
    m_fantasy_position_isSet = !json[QString("FantasyPosition")].isNull() && m_fantasy_position_isValid;

    m_fumbles_lost_isValid = ::OpenAPI::fromJsonValue(m_fumbles_lost, json[QString("FumblesLost")]);
    m_fumbles_lost_isSet = !json[QString("FumblesLost")].isNull() && m_fumbles_lost_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("Number")]);
    m_number_isSet = !json[QString("Number")].isNull() && m_number_isValid;

    m_player_game_id_isValid = ::OpenAPI::fromJsonValue(m_player_game_id, json[QString("PlayerGameID")]);
    m_player_game_id_isSet = !json[QString("PlayerGameID")].isNull() && m_player_game_id_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerID")]);
    m_player_id_isSet = !json[QString("PlayerID")].isNull() && m_player_id_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("Position")]);
    m_position_isSet = !json[QString("Position")].isNull() && m_position_isValid;

    m_position_category_isValid = ::OpenAPI::fromJsonValue(m_position_category, json[QString("PositionCategory")]);
    m_position_category_isSet = !json[QString("PositionCategory")].isNull() && m_position_category_isValid;

    m_rushing_attempts_isValid = ::OpenAPI::fromJsonValue(m_rushing_attempts, json[QString("RushingAttempts")]);
    m_rushing_attempts_isSet = !json[QString("RushingAttempts")].isNull() && m_rushing_attempts_isValid;

    m_rushing_long_isValid = ::OpenAPI::fromJsonValue(m_rushing_long, json[QString("RushingLong")]);
    m_rushing_long_isSet = !json[QString("RushingLong")].isNull() && m_rushing_long_isValid;

    m_rushing_touchdowns_isValid = ::OpenAPI::fromJsonValue(m_rushing_touchdowns, json[QString("RushingTouchdowns")]);
    m_rushing_touchdowns_isSet = !json[QString("RushingTouchdowns")].isNull() && m_rushing_touchdowns_isValid;

    m_rushing_yards_isValid = ::OpenAPI::fromJsonValue(m_rushing_yards, json[QString("RushingYards")]);
    m_rushing_yards_isSet = !json[QString("RushingYards")].isNull() && m_rushing_yards_isValid;

    m_rushing_yards_per_attempt_isValid = ::OpenAPI::fromJsonValue(m_rushing_yards_per_attempt, json[QString("RushingYardsPerAttempt")]);
    m_rushing_yards_per_attempt_isSet = !json[QString("RushingYardsPerAttempt")].isNull() && m_rushing_yards_per_attempt_isValid;

    m_short_name_isValid = ::OpenAPI::fromJsonValue(m_short_name, json[QString("ShortName")]);
    m_short_name_isSet = !json[QString("ShortName")].isNull() && m_short_name_isValid;

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("Team")]);
    m_team_isSet = !json[QString("Team")].isNull() && m_team_isValid;

    m_two_point_conversion_runs_isValid = ::OpenAPI::fromJsonValue(m_two_point_conversion_runs, json[QString("TwoPointConversionRuns")]);
    m_two_point_conversion_runs_isSet = !json[QString("TwoPointConversionRuns")].isNull() && m_two_point_conversion_runs_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;
}

QString OAIPlayerRushing::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlayerRushing::asJsonObject() const {
    QJsonObject obj;
    if (m_fantasy_points_isSet) {
        obj.insert(QString("FantasyPoints"), ::OpenAPI::toJsonValue(m_fantasy_points));
    }
    if (m_fantasy_position_isSet) {
        obj.insert(QString("FantasyPosition"), ::OpenAPI::toJsonValue(m_fantasy_position));
    }
    if (m_fumbles_lost_isSet) {
        obj.insert(QString("FumblesLost"), ::OpenAPI::toJsonValue(m_fumbles_lost));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_number_isSet) {
        obj.insert(QString("Number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_player_game_id_isSet) {
        obj.insert(QString("PlayerGameID"), ::OpenAPI::toJsonValue(m_player_game_id));
    }
    if (m_player_id_isSet) {
        obj.insert(QString("PlayerID"), ::OpenAPI::toJsonValue(m_player_id));
    }
    if (m_position_isSet) {
        obj.insert(QString("Position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_position_category_isSet) {
        obj.insert(QString("PositionCategory"), ::OpenAPI::toJsonValue(m_position_category));
    }
    if (m_rushing_attempts_isSet) {
        obj.insert(QString("RushingAttempts"), ::OpenAPI::toJsonValue(m_rushing_attempts));
    }
    if (m_rushing_long_isSet) {
        obj.insert(QString("RushingLong"), ::OpenAPI::toJsonValue(m_rushing_long));
    }
    if (m_rushing_touchdowns_isSet) {
        obj.insert(QString("RushingTouchdowns"), ::OpenAPI::toJsonValue(m_rushing_touchdowns));
    }
    if (m_rushing_yards_isSet) {
        obj.insert(QString("RushingYards"), ::OpenAPI::toJsonValue(m_rushing_yards));
    }
    if (m_rushing_yards_per_attempt_isSet) {
        obj.insert(QString("RushingYardsPerAttempt"), ::OpenAPI::toJsonValue(m_rushing_yards_per_attempt));
    }
    if (m_short_name_isSet) {
        obj.insert(QString("ShortName"), ::OpenAPI::toJsonValue(m_short_name));
    }
    if (m_team_isSet) {
        obj.insert(QString("Team"), ::OpenAPI::toJsonValue(m_team));
    }
    if (m_two_point_conversion_runs_isSet) {
        obj.insert(QString("TwoPointConversionRuns"), ::OpenAPI::toJsonValue(m_two_point_conversion_runs));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    return obj;
}

double OAIPlayerRushing::getFantasyPoints() const {
    return m_fantasy_points;
}
void OAIPlayerRushing::setFantasyPoints(const double &fantasy_points) {
    m_fantasy_points = fantasy_points;
    m_fantasy_points_isSet = true;
}

bool OAIPlayerRushing::is_fantasy_points_Set() const{
    return m_fantasy_points_isSet;
}

bool OAIPlayerRushing::is_fantasy_points_Valid() const{
    return m_fantasy_points_isValid;
}

QString OAIPlayerRushing::getFantasyPosition() const {
    return m_fantasy_position;
}
void OAIPlayerRushing::setFantasyPosition(const QString &fantasy_position) {
    m_fantasy_position = fantasy_position;
    m_fantasy_position_isSet = true;
}

bool OAIPlayerRushing::is_fantasy_position_Set() const{
    return m_fantasy_position_isSet;
}

bool OAIPlayerRushing::is_fantasy_position_Valid() const{
    return m_fantasy_position_isValid;
}

qint32 OAIPlayerRushing::getFumblesLost() const {
    return m_fumbles_lost;
}
void OAIPlayerRushing::setFumblesLost(const qint32 &fumbles_lost) {
    m_fumbles_lost = fumbles_lost;
    m_fumbles_lost_isSet = true;
}

bool OAIPlayerRushing::is_fumbles_lost_Set() const{
    return m_fumbles_lost_isSet;
}

bool OAIPlayerRushing::is_fumbles_lost_Valid() const{
    return m_fumbles_lost_isValid;
}

QString OAIPlayerRushing::getName() const {
    return m_name;
}
void OAIPlayerRushing::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPlayerRushing::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPlayerRushing::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIPlayerRushing::getNumber() const {
    return m_number;
}
void OAIPlayerRushing::setNumber(const qint32 &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIPlayerRushing::is_number_Set() const{
    return m_number_isSet;
}

bool OAIPlayerRushing::is_number_Valid() const{
    return m_number_isValid;
}

qint32 OAIPlayerRushing::getPlayerGameId() const {
    return m_player_game_id;
}
void OAIPlayerRushing::setPlayerGameId(const qint32 &player_game_id) {
    m_player_game_id = player_game_id;
    m_player_game_id_isSet = true;
}

bool OAIPlayerRushing::is_player_game_id_Set() const{
    return m_player_game_id_isSet;
}

bool OAIPlayerRushing::is_player_game_id_Valid() const{
    return m_player_game_id_isValid;
}

qint32 OAIPlayerRushing::getPlayerId() const {
    return m_player_id;
}
void OAIPlayerRushing::setPlayerId(const qint32 &player_id) {
    m_player_id = player_id;
    m_player_id_isSet = true;
}

bool OAIPlayerRushing::is_player_id_Set() const{
    return m_player_id_isSet;
}

bool OAIPlayerRushing::is_player_id_Valid() const{
    return m_player_id_isValid;
}

QString OAIPlayerRushing::getPosition() const {
    return m_position;
}
void OAIPlayerRushing::setPosition(const QString &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIPlayerRushing::is_position_Set() const{
    return m_position_isSet;
}

bool OAIPlayerRushing::is_position_Valid() const{
    return m_position_isValid;
}

QString OAIPlayerRushing::getPositionCategory() const {
    return m_position_category;
}
void OAIPlayerRushing::setPositionCategory(const QString &position_category) {
    m_position_category = position_category;
    m_position_category_isSet = true;
}

bool OAIPlayerRushing::is_position_category_Set() const{
    return m_position_category_isSet;
}

bool OAIPlayerRushing::is_position_category_Valid() const{
    return m_position_category_isValid;
}

qint32 OAIPlayerRushing::getRushingAttempts() const {
    return m_rushing_attempts;
}
void OAIPlayerRushing::setRushingAttempts(const qint32 &rushing_attempts) {
    m_rushing_attempts = rushing_attempts;
    m_rushing_attempts_isSet = true;
}

bool OAIPlayerRushing::is_rushing_attempts_Set() const{
    return m_rushing_attempts_isSet;
}

bool OAIPlayerRushing::is_rushing_attempts_Valid() const{
    return m_rushing_attempts_isValid;
}

qint32 OAIPlayerRushing::getRushingLong() const {
    return m_rushing_long;
}
void OAIPlayerRushing::setRushingLong(const qint32 &rushing_long) {
    m_rushing_long = rushing_long;
    m_rushing_long_isSet = true;
}

bool OAIPlayerRushing::is_rushing_long_Set() const{
    return m_rushing_long_isSet;
}

bool OAIPlayerRushing::is_rushing_long_Valid() const{
    return m_rushing_long_isValid;
}

qint32 OAIPlayerRushing::getRushingTouchdowns() const {
    return m_rushing_touchdowns;
}
void OAIPlayerRushing::setRushingTouchdowns(const qint32 &rushing_touchdowns) {
    m_rushing_touchdowns = rushing_touchdowns;
    m_rushing_touchdowns_isSet = true;
}

bool OAIPlayerRushing::is_rushing_touchdowns_Set() const{
    return m_rushing_touchdowns_isSet;
}

bool OAIPlayerRushing::is_rushing_touchdowns_Valid() const{
    return m_rushing_touchdowns_isValid;
}

qint32 OAIPlayerRushing::getRushingYards() const {
    return m_rushing_yards;
}
void OAIPlayerRushing::setRushingYards(const qint32 &rushing_yards) {
    m_rushing_yards = rushing_yards;
    m_rushing_yards_isSet = true;
}

bool OAIPlayerRushing::is_rushing_yards_Set() const{
    return m_rushing_yards_isSet;
}

bool OAIPlayerRushing::is_rushing_yards_Valid() const{
    return m_rushing_yards_isValid;
}

double OAIPlayerRushing::getRushingYardsPerAttempt() const {
    return m_rushing_yards_per_attempt;
}
void OAIPlayerRushing::setRushingYardsPerAttempt(const double &rushing_yards_per_attempt) {
    m_rushing_yards_per_attempt = rushing_yards_per_attempt;
    m_rushing_yards_per_attempt_isSet = true;
}

bool OAIPlayerRushing::is_rushing_yards_per_attempt_Set() const{
    return m_rushing_yards_per_attempt_isSet;
}

bool OAIPlayerRushing::is_rushing_yards_per_attempt_Valid() const{
    return m_rushing_yards_per_attempt_isValid;
}

QString OAIPlayerRushing::getShortName() const {
    return m_short_name;
}
void OAIPlayerRushing::setShortName(const QString &short_name) {
    m_short_name = short_name;
    m_short_name_isSet = true;
}

bool OAIPlayerRushing::is_short_name_Set() const{
    return m_short_name_isSet;
}

bool OAIPlayerRushing::is_short_name_Valid() const{
    return m_short_name_isValid;
}

QString OAIPlayerRushing::getTeam() const {
    return m_team;
}
void OAIPlayerRushing::setTeam(const QString &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAIPlayerRushing::is_team_Set() const{
    return m_team_isSet;
}

bool OAIPlayerRushing::is_team_Valid() const{
    return m_team_isValid;
}

qint32 OAIPlayerRushing::getTwoPointConversionRuns() const {
    return m_two_point_conversion_runs;
}
void OAIPlayerRushing::setTwoPointConversionRuns(const qint32 &two_point_conversion_runs) {
    m_two_point_conversion_runs = two_point_conversion_runs;
    m_two_point_conversion_runs_isSet = true;
}

bool OAIPlayerRushing::is_two_point_conversion_runs_Set() const{
    return m_two_point_conversion_runs_isSet;
}

bool OAIPlayerRushing::is_two_point_conversion_runs_Valid() const{
    return m_two_point_conversion_runs_isValid;
}

QString OAIPlayerRushing::getUpdated() const {
    return m_updated;
}
void OAIPlayerRushing::setUpdated(const QString &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIPlayerRushing::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIPlayerRushing::is_updated_Valid() const{
    return m_updated_isValid;
}

bool OAIPlayerRushing::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_fantasy_points_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fantasy_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fumbles_lost_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_game_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_player_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rushing_attempts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rushing_long_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rushing_touchdowns_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rushing_yards_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rushing_yards_per_attempt_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_two_point_conversion_runs_isSet) {
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

bool OAIPlayerRushing::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
