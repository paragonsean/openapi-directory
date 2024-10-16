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

#include "OAIPlayerPassing.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlayerPassing::OAIPlayerPassing(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlayerPassing::OAIPlayerPassing() {
    this->initializeModel();
}

OAIPlayerPassing::~OAIPlayerPassing() {}

void OAIPlayerPassing::initializeModel() {

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

    m_passing_attempts_isSet = false;
    m_passing_attempts_isValid = false;

    m_passing_completion_percentage_isSet = false;
    m_passing_completion_percentage_isValid = false;

    m_passing_completions_isSet = false;
    m_passing_completions_isValid = false;

    m_passing_interceptions_isSet = false;
    m_passing_interceptions_isValid = false;

    m_passing_long_isSet = false;
    m_passing_long_isValid = false;

    m_passing_rating_isSet = false;
    m_passing_rating_isValid = false;

    m_passing_sack_yards_isSet = false;
    m_passing_sack_yards_isValid = false;

    m_passing_sacks_isSet = false;
    m_passing_sacks_isValid = false;

    m_passing_touchdowns_isSet = false;
    m_passing_touchdowns_isValid = false;

    m_passing_yards_isSet = false;
    m_passing_yards_isValid = false;

    m_passing_yards_per_attempt_isSet = false;
    m_passing_yards_per_attempt_isValid = false;

    m_passing_yards_per_completion_isSet = false;
    m_passing_yards_per_completion_isValid = false;

    m_player_game_id_isSet = false;
    m_player_game_id_isValid = false;

    m_player_id_isSet = false;
    m_player_id_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_position_category_isSet = false;
    m_position_category_isValid = false;

    m_short_name_isSet = false;
    m_short_name_isValid = false;

    m_team_isSet = false;
    m_team_isValid = false;

    m_two_point_conversion_passes_isSet = false;
    m_two_point_conversion_passes_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;
}

void OAIPlayerPassing::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlayerPassing::fromJsonObject(QJsonObject json) {

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

    m_passing_attempts_isValid = ::OpenAPI::fromJsonValue(m_passing_attempts, json[QString("PassingAttempts")]);
    m_passing_attempts_isSet = !json[QString("PassingAttempts")].isNull() && m_passing_attempts_isValid;

    m_passing_completion_percentage_isValid = ::OpenAPI::fromJsonValue(m_passing_completion_percentage, json[QString("PassingCompletionPercentage")]);
    m_passing_completion_percentage_isSet = !json[QString("PassingCompletionPercentage")].isNull() && m_passing_completion_percentage_isValid;

    m_passing_completions_isValid = ::OpenAPI::fromJsonValue(m_passing_completions, json[QString("PassingCompletions")]);
    m_passing_completions_isSet = !json[QString("PassingCompletions")].isNull() && m_passing_completions_isValid;

    m_passing_interceptions_isValid = ::OpenAPI::fromJsonValue(m_passing_interceptions, json[QString("PassingInterceptions")]);
    m_passing_interceptions_isSet = !json[QString("PassingInterceptions")].isNull() && m_passing_interceptions_isValid;

    m_passing_long_isValid = ::OpenAPI::fromJsonValue(m_passing_long, json[QString("PassingLong")]);
    m_passing_long_isSet = !json[QString("PassingLong")].isNull() && m_passing_long_isValid;

    m_passing_rating_isValid = ::OpenAPI::fromJsonValue(m_passing_rating, json[QString("PassingRating")]);
    m_passing_rating_isSet = !json[QString("PassingRating")].isNull() && m_passing_rating_isValid;

    m_passing_sack_yards_isValid = ::OpenAPI::fromJsonValue(m_passing_sack_yards, json[QString("PassingSackYards")]);
    m_passing_sack_yards_isSet = !json[QString("PassingSackYards")].isNull() && m_passing_sack_yards_isValid;

    m_passing_sacks_isValid = ::OpenAPI::fromJsonValue(m_passing_sacks, json[QString("PassingSacks")]);
    m_passing_sacks_isSet = !json[QString("PassingSacks")].isNull() && m_passing_sacks_isValid;

    m_passing_touchdowns_isValid = ::OpenAPI::fromJsonValue(m_passing_touchdowns, json[QString("PassingTouchdowns")]);
    m_passing_touchdowns_isSet = !json[QString("PassingTouchdowns")].isNull() && m_passing_touchdowns_isValid;

    m_passing_yards_isValid = ::OpenAPI::fromJsonValue(m_passing_yards, json[QString("PassingYards")]);
    m_passing_yards_isSet = !json[QString("PassingYards")].isNull() && m_passing_yards_isValid;

    m_passing_yards_per_attempt_isValid = ::OpenAPI::fromJsonValue(m_passing_yards_per_attempt, json[QString("PassingYardsPerAttempt")]);
    m_passing_yards_per_attempt_isSet = !json[QString("PassingYardsPerAttempt")].isNull() && m_passing_yards_per_attempt_isValid;

    m_passing_yards_per_completion_isValid = ::OpenAPI::fromJsonValue(m_passing_yards_per_completion, json[QString("PassingYardsPerCompletion")]);
    m_passing_yards_per_completion_isSet = !json[QString("PassingYardsPerCompletion")].isNull() && m_passing_yards_per_completion_isValid;

    m_player_game_id_isValid = ::OpenAPI::fromJsonValue(m_player_game_id, json[QString("PlayerGameID")]);
    m_player_game_id_isSet = !json[QString("PlayerGameID")].isNull() && m_player_game_id_isValid;

    m_player_id_isValid = ::OpenAPI::fromJsonValue(m_player_id, json[QString("PlayerID")]);
    m_player_id_isSet = !json[QString("PlayerID")].isNull() && m_player_id_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("Position")]);
    m_position_isSet = !json[QString("Position")].isNull() && m_position_isValid;

    m_position_category_isValid = ::OpenAPI::fromJsonValue(m_position_category, json[QString("PositionCategory")]);
    m_position_category_isSet = !json[QString("PositionCategory")].isNull() && m_position_category_isValid;

    m_short_name_isValid = ::OpenAPI::fromJsonValue(m_short_name, json[QString("ShortName")]);
    m_short_name_isSet = !json[QString("ShortName")].isNull() && m_short_name_isValid;

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("Team")]);
    m_team_isSet = !json[QString("Team")].isNull() && m_team_isValid;

    m_two_point_conversion_passes_isValid = ::OpenAPI::fromJsonValue(m_two_point_conversion_passes, json[QString("TwoPointConversionPasses")]);
    m_two_point_conversion_passes_isSet = !json[QString("TwoPointConversionPasses")].isNull() && m_two_point_conversion_passes_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;
}

QString OAIPlayerPassing::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlayerPassing::asJsonObject() const {
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
    if (m_passing_attempts_isSet) {
        obj.insert(QString("PassingAttempts"), ::OpenAPI::toJsonValue(m_passing_attempts));
    }
    if (m_passing_completion_percentage_isSet) {
        obj.insert(QString("PassingCompletionPercentage"), ::OpenAPI::toJsonValue(m_passing_completion_percentage));
    }
    if (m_passing_completions_isSet) {
        obj.insert(QString("PassingCompletions"), ::OpenAPI::toJsonValue(m_passing_completions));
    }
    if (m_passing_interceptions_isSet) {
        obj.insert(QString("PassingInterceptions"), ::OpenAPI::toJsonValue(m_passing_interceptions));
    }
    if (m_passing_long_isSet) {
        obj.insert(QString("PassingLong"), ::OpenAPI::toJsonValue(m_passing_long));
    }
    if (m_passing_rating_isSet) {
        obj.insert(QString("PassingRating"), ::OpenAPI::toJsonValue(m_passing_rating));
    }
    if (m_passing_sack_yards_isSet) {
        obj.insert(QString("PassingSackYards"), ::OpenAPI::toJsonValue(m_passing_sack_yards));
    }
    if (m_passing_sacks_isSet) {
        obj.insert(QString("PassingSacks"), ::OpenAPI::toJsonValue(m_passing_sacks));
    }
    if (m_passing_touchdowns_isSet) {
        obj.insert(QString("PassingTouchdowns"), ::OpenAPI::toJsonValue(m_passing_touchdowns));
    }
    if (m_passing_yards_isSet) {
        obj.insert(QString("PassingYards"), ::OpenAPI::toJsonValue(m_passing_yards));
    }
    if (m_passing_yards_per_attempt_isSet) {
        obj.insert(QString("PassingYardsPerAttempt"), ::OpenAPI::toJsonValue(m_passing_yards_per_attempt));
    }
    if (m_passing_yards_per_completion_isSet) {
        obj.insert(QString("PassingYardsPerCompletion"), ::OpenAPI::toJsonValue(m_passing_yards_per_completion));
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
    if (m_short_name_isSet) {
        obj.insert(QString("ShortName"), ::OpenAPI::toJsonValue(m_short_name));
    }
    if (m_team_isSet) {
        obj.insert(QString("Team"), ::OpenAPI::toJsonValue(m_team));
    }
    if (m_two_point_conversion_passes_isSet) {
        obj.insert(QString("TwoPointConversionPasses"), ::OpenAPI::toJsonValue(m_two_point_conversion_passes));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    return obj;
}

double OAIPlayerPassing::getFantasyPoints() const {
    return m_fantasy_points;
}
void OAIPlayerPassing::setFantasyPoints(const double &fantasy_points) {
    m_fantasy_points = fantasy_points;
    m_fantasy_points_isSet = true;
}

bool OAIPlayerPassing::is_fantasy_points_Set() const{
    return m_fantasy_points_isSet;
}

bool OAIPlayerPassing::is_fantasy_points_Valid() const{
    return m_fantasy_points_isValid;
}

QString OAIPlayerPassing::getFantasyPosition() const {
    return m_fantasy_position;
}
void OAIPlayerPassing::setFantasyPosition(const QString &fantasy_position) {
    m_fantasy_position = fantasy_position;
    m_fantasy_position_isSet = true;
}

bool OAIPlayerPassing::is_fantasy_position_Set() const{
    return m_fantasy_position_isSet;
}

bool OAIPlayerPassing::is_fantasy_position_Valid() const{
    return m_fantasy_position_isValid;
}

qint32 OAIPlayerPassing::getFumblesLost() const {
    return m_fumbles_lost;
}
void OAIPlayerPassing::setFumblesLost(const qint32 &fumbles_lost) {
    m_fumbles_lost = fumbles_lost;
    m_fumbles_lost_isSet = true;
}

bool OAIPlayerPassing::is_fumbles_lost_Set() const{
    return m_fumbles_lost_isSet;
}

bool OAIPlayerPassing::is_fumbles_lost_Valid() const{
    return m_fumbles_lost_isValid;
}

QString OAIPlayerPassing::getName() const {
    return m_name;
}
void OAIPlayerPassing::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPlayerPassing::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPlayerPassing::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIPlayerPassing::getNumber() const {
    return m_number;
}
void OAIPlayerPassing::setNumber(const qint32 &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIPlayerPassing::is_number_Set() const{
    return m_number_isSet;
}

bool OAIPlayerPassing::is_number_Valid() const{
    return m_number_isValid;
}

qint32 OAIPlayerPassing::getPassingAttempts() const {
    return m_passing_attempts;
}
void OAIPlayerPassing::setPassingAttempts(const qint32 &passing_attempts) {
    m_passing_attempts = passing_attempts;
    m_passing_attempts_isSet = true;
}

bool OAIPlayerPassing::is_passing_attempts_Set() const{
    return m_passing_attempts_isSet;
}

bool OAIPlayerPassing::is_passing_attempts_Valid() const{
    return m_passing_attempts_isValid;
}

double OAIPlayerPassing::getPassingCompletionPercentage() const {
    return m_passing_completion_percentage;
}
void OAIPlayerPassing::setPassingCompletionPercentage(const double &passing_completion_percentage) {
    m_passing_completion_percentage = passing_completion_percentage;
    m_passing_completion_percentage_isSet = true;
}

bool OAIPlayerPassing::is_passing_completion_percentage_Set() const{
    return m_passing_completion_percentage_isSet;
}

bool OAIPlayerPassing::is_passing_completion_percentage_Valid() const{
    return m_passing_completion_percentage_isValid;
}

qint32 OAIPlayerPassing::getPassingCompletions() const {
    return m_passing_completions;
}
void OAIPlayerPassing::setPassingCompletions(const qint32 &passing_completions) {
    m_passing_completions = passing_completions;
    m_passing_completions_isSet = true;
}

bool OAIPlayerPassing::is_passing_completions_Set() const{
    return m_passing_completions_isSet;
}

bool OAIPlayerPassing::is_passing_completions_Valid() const{
    return m_passing_completions_isValid;
}

qint32 OAIPlayerPassing::getPassingInterceptions() const {
    return m_passing_interceptions;
}
void OAIPlayerPassing::setPassingInterceptions(const qint32 &passing_interceptions) {
    m_passing_interceptions = passing_interceptions;
    m_passing_interceptions_isSet = true;
}

bool OAIPlayerPassing::is_passing_interceptions_Set() const{
    return m_passing_interceptions_isSet;
}

bool OAIPlayerPassing::is_passing_interceptions_Valid() const{
    return m_passing_interceptions_isValid;
}

qint32 OAIPlayerPassing::getPassingLong() const {
    return m_passing_long;
}
void OAIPlayerPassing::setPassingLong(const qint32 &passing_long) {
    m_passing_long = passing_long;
    m_passing_long_isSet = true;
}

bool OAIPlayerPassing::is_passing_long_Set() const{
    return m_passing_long_isSet;
}

bool OAIPlayerPassing::is_passing_long_Valid() const{
    return m_passing_long_isValid;
}

double OAIPlayerPassing::getPassingRating() const {
    return m_passing_rating;
}
void OAIPlayerPassing::setPassingRating(const double &passing_rating) {
    m_passing_rating = passing_rating;
    m_passing_rating_isSet = true;
}

bool OAIPlayerPassing::is_passing_rating_Set() const{
    return m_passing_rating_isSet;
}

bool OAIPlayerPassing::is_passing_rating_Valid() const{
    return m_passing_rating_isValid;
}

qint32 OAIPlayerPassing::getPassingSackYards() const {
    return m_passing_sack_yards;
}
void OAIPlayerPassing::setPassingSackYards(const qint32 &passing_sack_yards) {
    m_passing_sack_yards = passing_sack_yards;
    m_passing_sack_yards_isSet = true;
}

bool OAIPlayerPassing::is_passing_sack_yards_Set() const{
    return m_passing_sack_yards_isSet;
}

bool OAIPlayerPassing::is_passing_sack_yards_Valid() const{
    return m_passing_sack_yards_isValid;
}

qint32 OAIPlayerPassing::getPassingSacks() const {
    return m_passing_sacks;
}
void OAIPlayerPassing::setPassingSacks(const qint32 &passing_sacks) {
    m_passing_sacks = passing_sacks;
    m_passing_sacks_isSet = true;
}

bool OAIPlayerPassing::is_passing_sacks_Set() const{
    return m_passing_sacks_isSet;
}

bool OAIPlayerPassing::is_passing_sacks_Valid() const{
    return m_passing_sacks_isValid;
}

qint32 OAIPlayerPassing::getPassingTouchdowns() const {
    return m_passing_touchdowns;
}
void OAIPlayerPassing::setPassingTouchdowns(const qint32 &passing_touchdowns) {
    m_passing_touchdowns = passing_touchdowns;
    m_passing_touchdowns_isSet = true;
}

bool OAIPlayerPassing::is_passing_touchdowns_Set() const{
    return m_passing_touchdowns_isSet;
}

bool OAIPlayerPassing::is_passing_touchdowns_Valid() const{
    return m_passing_touchdowns_isValid;
}

qint32 OAIPlayerPassing::getPassingYards() const {
    return m_passing_yards;
}
void OAIPlayerPassing::setPassingYards(const qint32 &passing_yards) {
    m_passing_yards = passing_yards;
    m_passing_yards_isSet = true;
}

bool OAIPlayerPassing::is_passing_yards_Set() const{
    return m_passing_yards_isSet;
}

bool OAIPlayerPassing::is_passing_yards_Valid() const{
    return m_passing_yards_isValid;
}

double OAIPlayerPassing::getPassingYardsPerAttempt() const {
    return m_passing_yards_per_attempt;
}
void OAIPlayerPassing::setPassingYardsPerAttempt(const double &passing_yards_per_attempt) {
    m_passing_yards_per_attempt = passing_yards_per_attempt;
    m_passing_yards_per_attempt_isSet = true;
}

bool OAIPlayerPassing::is_passing_yards_per_attempt_Set() const{
    return m_passing_yards_per_attempt_isSet;
}

bool OAIPlayerPassing::is_passing_yards_per_attempt_Valid() const{
    return m_passing_yards_per_attempt_isValid;
}

double OAIPlayerPassing::getPassingYardsPerCompletion() const {
    return m_passing_yards_per_completion;
}
void OAIPlayerPassing::setPassingYardsPerCompletion(const double &passing_yards_per_completion) {
    m_passing_yards_per_completion = passing_yards_per_completion;
    m_passing_yards_per_completion_isSet = true;
}

bool OAIPlayerPassing::is_passing_yards_per_completion_Set() const{
    return m_passing_yards_per_completion_isSet;
}

bool OAIPlayerPassing::is_passing_yards_per_completion_Valid() const{
    return m_passing_yards_per_completion_isValid;
}

qint32 OAIPlayerPassing::getPlayerGameId() const {
    return m_player_game_id;
}
void OAIPlayerPassing::setPlayerGameId(const qint32 &player_game_id) {
    m_player_game_id = player_game_id;
    m_player_game_id_isSet = true;
}

bool OAIPlayerPassing::is_player_game_id_Set() const{
    return m_player_game_id_isSet;
}

bool OAIPlayerPassing::is_player_game_id_Valid() const{
    return m_player_game_id_isValid;
}

qint32 OAIPlayerPassing::getPlayerId() const {
    return m_player_id;
}
void OAIPlayerPassing::setPlayerId(const qint32 &player_id) {
    m_player_id = player_id;
    m_player_id_isSet = true;
}

bool OAIPlayerPassing::is_player_id_Set() const{
    return m_player_id_isSet;
}

bool OAIPlayerPassing::is_player_id_Valid() const{
    return m_player_id_isValid;
}

QString OAIPlayerPassing::getPosition() const {
    return m_position;
}
void OAIPlayerPassing::setPosition(const QString &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIPlayerPassing::is_position_Set() const{
    return m_position_isSet;
}

bool OAIPlayerPassing::is_position_Valid() const{
    return m_position_isValid;
}

QString OAIPlayerPassing::getPositionCategory() const {
    return m_position_category;
}
void OAIPlayerPassing::setPositionCategory(const QString &position_category) {
    m_position_category = position_category;
    m_position_category_isSet = true;
}

bool OAIPlayerPassing::is_position_category_Set() const{
    return m_position_category_isSet;
}

bool OAIPlayerPassing::is_position_category_Valid() const{
    return m_position_category_isValid;
}

QString OAIPlayerPassing::getShortName() const {
    return m_short_name;
}
void OAIPlayerPassing::setShortName(const QString &short_name) {
    m_short_name = short_name;
    m_short_name_isSet = true;
}

bool OAIPlayerPassing::is_short_name_Set() const{
    return m_short_name_isSet;
}

bool OAIPlayerPassing::is_short_name_Valid() const{
    return m_short_name_isValid;
}

QString OAIPlayerPassing::getTeam() const {
    return m_team;
}
void OAIPlayerPassing::setTeam(const QString &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAIPlayerPassing::is_team_Set() const{
    return m_team_isSet;
}

bool OAIPlayerPassing::is_team_Valid() const{
    return m_team_isValid;
}

qint32 OAIPlayerPassing::getTwoPointConversionPasses() const {
    return m_two_point_conversion_passes;
}
void OAIPlayerPassing::setTwoPointConversionPasses(const qint32 &two_point_conversion_passes) {
    m_two_point_conversion_passes = two_point_conversion_passes;
    m_two_point_conversion_passes_isSet = true;
}

bool OAIPlayerPassing::is_two_point_conversion_passes_Set() const{
    return m_two_point_conversion_passes_isSet;
}

bool OAIPlayerPassing::is_two_point_conversion_passes_Valid() const{
    return m_two_point_conversion_passes_isValid;
}

QString OAIPlayerPassing::getUpdated() const {
    return m_updated;
}
void OAIPlayerPassing::setUpdated(const QString &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIPlayerPassing::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIPlayerPassing::is_updated_Valid() const{
    return m_updated_isValid;
}

bool OAIPlayerPassing::isSet() const {
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

        if (m_passing_attempts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_completion_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_completions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_interceptions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_long_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_rating_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_sack_yards_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_sacks_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_touchdowns_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_yards_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_yards_per_attempt_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passing_yards_per_completion_isSet) {
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

        if (m_short_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_two_point_conversion_passes_isSet) {
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

bool OAIPlayerPassing::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
