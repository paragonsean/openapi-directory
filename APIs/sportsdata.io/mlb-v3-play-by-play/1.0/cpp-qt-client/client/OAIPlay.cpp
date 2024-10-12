/**
 * MLB v3 Play-by-Play
 * MLB play-by-play API.
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

    m_at_bat_isSet = false;
    m_at_bat_isValid = false;

    m_away_team_runs_isSet = false;
    m_away_team_runs_isValid = false;

    m_balls_isSet = false;
    m_balls_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_hit_isSet = false;
    m_hit_isValid = false;

    m_hitter_bat_hand_isSet = false;
    m_hitter_bat_hand_isValid = false;

    m_hitter_id_isSet = false;
    m_hitter_id_isValid = false;

    m_hitter_name_isSet = false;
    m_hitter_name_isValid = false;

    m_hitter_position_isSet = false;
    m_hitter_position_isValid = false;

    m_hitter_team_id_isSet = false;
    m_hitter_team_id_isValid = false;

    m_home_team_runs_isSet = false;
    m_home_team_runs_isValid = false;

    m_inning_batter_number_isSet = false;
    m_inning_batter_number_isValid = false;

    m_inning_half_isSet = false;
    m_inning_half_isValid = false;

    m_inning_id_isSet = false;
    m_inning_id_isValid = false;

    m_inning_number_isSet = false;
    m_inning_number_isValid = false;

    m_number_of_outs_on_play_isSet = false;
    m_number_of_outs_on_play_isValid = false;

    m_out_isSet = false;
    m_out_isValid = false;

    m_outs_isSet = false;
    m_outs_isValid = false;

    m_pitch_number_this_at_bat_isSet = false;
    m_pitch_number_this_at_bat_isValid = false;

    m_pitcher_id_isSet = false;
    m_pitcher_id_isValid = false;

    m_pitcher_name_isSet = false;
    m_pitcher_name_isValid = false;

    m_pitcher_team_id_isSet = false;
    m_pitcher_team_id_isValid = false;

    m_pitcher_throw_hand_isSet = false;
    m_pitcher_throw_hand_isValid = false;

    m_pitches_isSet = false;
    m_pitches_isValid = false;

    m_play_id_isSet = false;
    m_play_id_isValid = false;

    m_play_number_isSet = false;
    m_play_number_isValid = false;

    m_result_isSet = false;
    m_result_isValid = false;

    m_runner1_id_isSet = false;
    m_runner1_id_isValid = false;

    m_runner2_id_isSet = false;
    m_runner2_id_isValid = false;

    m_runner3_id_isSet = false;
    m_runner3_id_isValid = false;

    m_runs_batted_in_isSet = false;
    m_runs_batted_in_isValid = false;

    m_sacrifice_isSet = false;
    m_sacrifice_isValid = false;

    m_strikeout_isSet = false;
    m_strikeout_isValid = false;

    m_strikes_isSet = false;
    m_strikes_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;

    m_walk_isSet = false;
    m_walk_isValid = false;
}

void OAIPlay::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlay::fromJsonObject(QJsonObject json) {

    m_at_bat_isValid = ::OpenAPI::fromJsonValue(m_at_bat, json[QString("AtBat")]);
    m_at_bat_isSet = !json[QString("AtBat")].isNull() && m_at_bat_isValid;

    m_away_team_runs_isValid = ::OpenAPI::fromJsonValue(m_away_team_runs, json[QString("AwayTeamRuns")]);
    m_away_team_runs_isSet = !json[QString("AwayTeamRuns")].isNull() && m_away_team_runs_isValid;

    m_balls_isValid = ::OpenAPI::fromJsonValue(m_balls, json[QString("Balls")]);
    m_balls_isSet = !json[QString("Balls")].isNull() && m_balls_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("Error")]);
    m_error_isSet = !json[QString("Error")].isNull() && m_error_isValid;

    m_hit_isValid = ::OpenAPI::fromJsonValue(m_hit, json[QString("Hit")]);
    m_hit_isSet = !json[QString("Hit")].isNull() && m_hit_isValid;

    m_hitter_bat_hand_isValid = ::OpenAPI::fromJsonValue(m_hitter_bat_hand, json[QString("HitterBatHand")]);
    m_hitter_bat_hand_isSet = !json[QString("HitterBatHand")].isNull() && m_hitter_bat_hand_isValid;

    m_hitter_id_isValid = ::OpenAPI::fromJsonValue(m_hitter_id, json[QString("HitterID")]);
    m_hitter_id_isSet = !json[QString("HitterID")].isNull() && m_hitter_id_isValid;

    m_hitter_name_isValid = ::OpenAPI::fromJsonValue(m_hitter_name, json[QString("HitterName")]);
    m_hitter_name_isSet = !json[QString("HitterName")].isNull() && m_hitter_name_isValid;

    m_hitter_position_isValid = ::OpenAPI::fromJsonValue(m_hitter_position, json[QString("HitterPosition")]);
    m_hitter_position_isSet = !json[QString("HitterPosition")].isNull() && m_hitter_position_isValid;

    m_hitter_team_id_isValid = ::OpenAPI::fromJsonValue(m_hitter_team_id, json[QString("HitterTeamID")]);
    m_hitter_team_id_isSet = !json[QString("HitterTeamID")].isNull() && m_hitter_team_id_isValid;

    m_home_team_runs_isValid = ::OpenAPI::fromJsonValue(m_home_team_runs, json[QString("HomeTeamRuns")]);
    m_home_team_runs_isSet = !json[QString("HomeTeamRuns")].isNull() && m_home_team_runs_isValid;

    m_inning_batter_number_isValid = ::OpenAPI::fromJsonValue(m_inning_batter_number, json[QString("InningBatterNumber")]);
    m_inning_batter_number_isSet = !json[QString("InningBatterNumber")].isNull() && m_inning_batter_number_isValid;

    m_inning_half_isValid = ::OpenAPI::fromJsonValue(m_inning_half, json[QString("InningHalf")]);
    m_inning_half_isSet = !json[QString("InningHalf")].isNull() && m_inning_half_isValid;

    m_inning_id_isValid = ::OpenAPI::fromJsonValue(m_inning_id, json[QString("InningID")]);
    m_inning_id_isSet = !json[QString("InningID")].isNull() && m_inning_id_isValid;

    m_inning_number_isValid = ::OpenAPI::fromJsonValue(m_inning_number, json[QString("InningNumber")]);
    m_inning_number_isSet = !json[QString("InningNumber")].isNull() && m_inning_number_isValid;

    m_number_of_outs_on_play_isValid = ::OpenAPI::fromJsonValue(m_number_of_outs_on_play, json[QString("NumberOfOutsOnPlay")]);
    m_number_of_outs_on_play_isSet = !json[QString("NumberOfOutsOnPlay")].isNull() && m_number_of_outs_on_play_isValid;

    m_out_isValid = ::OpenAPI::fromJsonValue(m_out, json[QString("Out")]);
    m_out_isSet = !json[QString("Out")].isNull() && m_out_isValid;

    m_outs_isValid = ::OpenAPI::fromJsonValue(m_outs, json[QString("Outs")]);
    m_outs_isSet = !json[QString("Outs")].isNull() && m_outs_isValid;

    m_pitch_number_this_at_bat_isValid = ::OpenAPI::fromJsonValue(m_pitch_number_this_at_bat, json[QString("PitchNumberThisAtBat")]);
    m_pitch_number_this_at_bat_isSet = !json[QString("PitchNumberThisAtBat")].isNull() && m_pitch_number_this_at_bat_isValid;

    m_pitcher_id_isValid = ::OpenAPI::fromJsonValue(m_pitcher_id, json[QString("PitcherID")]);
    m_pitcher_id_isSet = !json[QString("PitcherID")].isNull() && m_pitcher_id_isValid;

    m_pitcher_name_isValid = ::OpenAPI::fromJsonValue(m_pitcher_name, json[QString("PitcherName")]);
    m_pitcher_name_isSet = !json[QString("PitcherName")].isNull() && m_pitcher_name_isValid;

    m_pitcher_team_id_isValid = ::OpenAPI::fromJsonValue(m_pitcher_team_id, json[QString("PitcherTeamID")]);
    m_pitcher_team_id_isSet = !json[QString("PitcherTeamID")].isNull() && m_pitcher_team_id_isValid;

    m_pitcher_throw_hand_isValid = ::OpenAPI::fromJsonValue(m_pitcher_throw_hand, json[QString("PitcherThrowHand")]);
    m_pitcher_throw_hand_isSet = !json[QString("PitcherThrowHand")].isNull() && m_pitcher_throw_hand_isValid;

    m_pitches_isValid = ::OpenAPI::fromJsonValue(m_pitches, json[QString("Pitches")]);
    m_pitches_isSet = !json[QString("Pitches")].isNull() && m_pitches_isValid;

    m_play_id_isValid = ::OpenAPI::fromJsonValue(m_play_id, json[QString("PlayID")]);
    m_play_id_isSet = !json[QString("PlayID")].isNull() && m_play_id_isValid;

    m_play_number_isValid = ::OpenAPI::fromJsonValue(m_play_number, json[QString("PlayNumber")]);
    m_play_number_isSet = !json[QString("PlayNumber")].isNull() && m_play_number_isValid;

    m_result_isValid = ::OpenAPI::fromJsonValue(m_result, json[QString("Result")]);
    m_result_isSet = !json[QString("Result")].isNull() && m_result_isValid;

    m_runner1_id_isValid = ::OpenAPI::fromJsonValue(m_runner1_id, json[QString("Runner1ID")]);
    m_runner1_id_isSet = !json[QString("Runner1ID")].isNull() && m_runner1_id_isValid;

    m_runner2_id_isValid = ::OpenAPI::fromJsonValue(m_runner2_id, json[QString("Runner2ID")]);
    m_runner2_id_isSet = !json[QString("Runner2ID")].isNull() && m_runner2_id_isValid;

    m_runner3_id_isValid = ::OpenAPI::fromJsonValue(m_runner3_id, json[QString("Runner3ID")]);
    m_runner3_id_isSet = !json[QString("Runner3ID")].isNull() && m_runner3_id_isValid;

    m_runs_batted_in_isValid = ::OpenAPI::fromJsonValue(m_runs_batted_in, json[QString("RunsBattedIn")]);
    m_runs_batted_in_isSet = !json[QString("RunsBattedIn")].isNull() && m_runs_batted_in_isValid;

    m_sacrifice_isValid = ::OpenAPI::fromJsonValue(m_sacrifice, json[QString("Sacrifice")]);
    m_sacrifice_isSet = !json[QString("Sacrifice")].isNull() && m_sacrifice_isValid;

    m_strikeout_isValid = ::OpenAPI::fromJsonValue(m_strikeout, json[QString("Strikeout")]);
    m_strikeout_isSet = !json[QString("Strikeout")].isNull() && m_strikeout_isValid;

    m_strikes_isValid = ::OpenAPI::fromJsonValue(m_strikes, json[QString("Strikes")]);
    m_strikes_isSet = !json[QString("Strikes")].isNull() && m_strikes_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;

    m_walk_isValid = ::OpenAPI::fromJsonValue(m_walk, json[QString("Walk")]);
    m_walk_isSet = !json[QString("Walk")].isNull() && m_walk_isValid;
}

QString OAIPlay::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlay::asJsonObject() const {
    QJsonObject obj;
    if (m_at_bat_isSet) {
        obj.insert(QString("AtBat"), ::OpenAPI::toJsonValue(m_at_bat));
    }
    if (m_away_team_runs_isSet) {
        obj.insert(QString("AwayTeamRuns"), ::OpenAPI::toJsonValue(m_away_team_runs));
    }
    if (m_balls_isSet) {
        obj.insert(QString("Balls"), ::OpenAPI::toJsonValue(m_balls));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_error_isSet) {
        obj.insert(QString("Error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_hit_isSet) {
        obj.insert(QString("Hit"), ::OpenAPI::toJsonValue(m_hit));
    }
    if (m_hitter_bat_hand_isSet) {
        obj.insert(QString("HitterBatHand"), ::OpenAPI::toJsonValue(m_hitter_bat_hand));
    }
    if (m_hitter_id_isSet) {
        obj.insert(QString("HitterID"), ::OpenAPI::toJsonValue(m_hitter_id));
    }
    if (m_hitter_name_isSet) {
        obj.insert(QString("HitterName"), ::OpenAPI::toJsonValue(m_hitter_name));
    }
    if (m_hitter_position_isSet) {
        obj.insert(QString("HitterPosition"), ::OpenAPI::toJsonValue(m_hitter_position));
    }
    if (m_hitter_team_id_isSet) {
        obj.insert(QString("HitterTeamID"), ::OpenAPI::toJsonValue(m_hitter_team_id));
    }
    if (m_home_team_runs_isSet) {
        obj.insert(QString("HomeTeamRuns"), ::OpenAPI::toJsonValue(m_home_team_runs));
    }
    if (m_inning_batter_number_isSet) {
        obj.insert(QString("InningBatterNumber"), ::OpenAPI::toJsonValue(m_inning_batter_number));
    }
    if (m_inning_half_isSet) {
        obj.insert(QString("InningHalf"), ::OpenAPI::toJsonValue(m_inning_half));
    }
    if (m_inning_id_isSet) {
        obj.insert(QString("InningID"), ::OpenAPI::toJsonValue(m_inning_id));
    }
    if (m_inning_number_isSet) {
        obj.insert(QString("InningNumber"), ::OpenAPI::toJsonValue(m_inning_number));
    }
    if (m_number_of_outs_on_play_isSet) {
        obj.insert(QString("NumberOfOutsOnPlay"), ::OpenAPI::toJsonValue(m_number_of_outs_on_play));
    }
    if (m_out_isSet) {
        obj.insert(QString("Out"), ::OpenAPI::toJsonValue(m_out));
    }
    if (m_outs_isSet) {
        obj.insert(QString("Outs"), ::OpenAPI::toJsonValue(m_outs));
    }
    if (m_pitch_number_this_at_bat_isSet) {
        obj.insert(QString("PitchNumberThisAtBat"), ::OpenAPI::toJsonValue(m_pitch_number_this_at_bat));
    }
    if (m_pitcher_id_isSet) {
        obj.insert(QString("PitcherID"), ::OpenAPI::toJsonValue(m_pitcher_id));
    }
    if (m_pitcher_name_isSet) {
        obj.insert(QString("PitcherName"), ::OpenAPI::toJsonValue(m_pitcher_name));
    }
    if (m_pitcher_team_id_isSet) {
        obj.insert(QString("PitcherTeamID"), ::OpenAPI::toJsonValue(m_pitcher_team_id));
    }
    if (m_pitcher_throw_hand_isSet) {
        obj.insert(QString("PitcherThrowHand"), ::OpenAPI::toJsonValue(m_pitcher_throw_hand));
    }
    if (m_pitches.size() > 0) {
        obj.insert(QString("Pitches"), ::OpenAPI::toJsonValue(m_pitches));
    }
    if (m_play_id_isSet) {
        obj.insert(QString("PlayID"), ::OpenAPI::toJsonValue(m_play_id));
    }
    if (m_play_number_isSet) {
        obj.insert(QString("PlayNumber"), ::OpenAPI::toJsonValue(m_play_number));
    }
    if (m_result_isSet) {
        obj.insert(QString("Result"), ::OpenAPI::toJsonValue(m_result));
    }
    if (m_runner1_id_isSet) {
        obj.insert(QString("Runner1ID"), ::OpenAPI::toJsonValue(m_runner1_id));
    }
    if (m_runner2_id_isSet) {
        obj.insert(QString("Runner2ID"), ::OpenAPI::toJsonValue(m_runner2_id));
    }
    if (m_runner3_id_isSet) {
        obj.insert(QString("Runner3ID"), ::OpenAPI::toJsonValue(m_runner3_id));
    }
    if (m_runs_batted_in_isSet) {
        obj.insert(QString("RunsBattedIn"), ::OpenAPI::toJsonValue(m_runs_batted_in));
    }
    if (m_sacrifice_isSet) {
        obj.insert(QString("Sacrifice"), ::OpenAPI::toJsonValue(m_sacrifice));
    }
    if (m_strikeout_isSet) {
        obj.insert(QString("Strikeout"), ::OpenAPI::toJsonValue(m_strikeout));
    }
    if (m_strikes_isSet) {
        obj.insert(QString("Strikes"), ::OpenAPI::toJsonValue(m_strikes));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    if (m_walk_isSet) {
        obj.insert(QString("Walk"), ::OpenAPI::toJsonValue(m_walk));
    }
    return obj;
}

bool OAIPlay::isAtBat() const {
    return m_at_bat;
}
void OAIPlay::setAtBat(const bool &at_bat) {
    m_at_bat = at_bat;
    m_at_bat_isSet = true;
}

bool OAIPlay::is_at_bat_Set() const{
    return m_at_bat_isSet;
}

bool OAIPlay::is_at_bat_Valid() const{
    return m_at_bat_isValid;
}

qint32 OAIPlay::getAwayTeamRuns() const {
    return m_away_team_runs;
}
void OAIPlay::setAwayTeamRuns(const qint32 &away_team_runs) {
    m_away_team_runs = away_team_runs;
    m_away_team_runs_isSet = true;
}

bool OAIPlay::is_away_team_runs_Set() const{
    return m_away_team_runs_isSet;
}

bool OAIPlay::is_away_team_runs_Valid() const{
    return m_away_team_runs_isValid;
}

qint32 OAIPlay::getBalls() const {
    return m_balls;
}
void OAIPlay::setBalls(const qint32 &balls) {
    m_balls = balls;
    m_balls_isSet = true;
}

bool OAIPlay::is_balls_Set() const{
    return m_balls_isSet;
}

bool OAIPlay::is_balls_Valid() const{
    return m_balls_isValid;
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

bool OAIPlay::isError() const {
    return m_error;
}
void OAIPlay::setError(const bool &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIPlay::is_error_Set() const{
    return m_error_isSet;
}

bool OAIPlay::is_error_Valid() const{
    return m_error_isValid;
}

bool OAIPlay::isHit() const {
    return m_hit;
}
void OAIPlay::setHit(const bool &hit) {
    m_hit = hit;
    m_hit_isSet = true;
}

bool OAIPlay::is_hit_Set() const{
    return m_hit_isSet;
}

bool OAIPlay::is_hit_Valid() const{
    return m_hit_isValid;
}

QString OAIPlay::getHitterBatHand() const {
    return m_hitter_bat_hand;
}
void OAIPlay::setHitterBatHand(const QString &hitter_bat_hand) {
    m_hitter_bat_hand = hitter_bat_hand;
    m_hitter_bat_hand_isSet = true;
}

bool OAIPlay::is_hitter_bat_hand_Set() const{
    return m_hitter_bat_hand_isSet;
}

bool OAIPlay::is_hitter_bat_hand_Valid() const{
    return m_hitter_bat_hand_isValid;
}

qint32 OAIPlay::getHitterId() const {
    return m_hitter_id;
}
void OAIPlay::setHitterId(const qint32 &hitter_id) {
    m_hitter_id = hitter_id;
    m_hitter_id_isSet = true;
}

bool OAIPlay::is_hitter_id_Set() const{
    return m_hitter_id_isSet;
}

bool OAIPlay::is_hitter_id_Valid() const{
    return m_hitter_id_isValid;
}

QString OAIPlay::getHitterName() const {
    return m_hitter_name;
}
void OAIPlay::setHitterName(const QString &hitter_name) {
    m_hitter_name = hitter_name;
    m_hitter_name_isSet = true;
}

bool OAIPlay::is_hitter_name_Set() const{
    return m_hitter_name_isSet;
}

bool OAIPlay::is_hitter_name_Valid() const{
    return m_hitter_name_isValid;
}

QString OAIPlay::getHitterPosition() const {
    return m_hitter_position;
}
void OAIPlay::setHitterPosition(const QString &hitter_position) {
    m_hitter_position = hitter_position;
    m_hitter_position_isSet = true;
}

bool OAIPlay::is_hitter_position_Set() const{
    return m_hitter_position_isSet;
}

bool OAIPlay::is_hitter_position_Valid() const{
    return m_hitter_position_isValid;
}

qint32 OAIPlay::getHitterTeamId() const {
    return m_hitter_team_id;
}
void OAIPlay::setHitterTeamId(const qint32 &hitter_team_id) {
    m_hitter_team_id = hitter_team_id;
    m_hitter_team_id_isSet = true;
}

bool OAIPlay::is_hitter_team_id_Set() const{
    return m_hitter_team_id_isSet;
}

bool OAIPlay::is_hitter_team_id_Valid() const{
    return m_hitter_team_id_isValid;
}

qint32 OAIPlay::getHomeTeamRuns() const {
    return m_home_team_runs;
}
void OAIPlay::setHomeTeamRuns(const qint32 &home_team_runs) {
    m_home_team_runs = home_team_runs;
    m_home_team_runs_isSet = true;
}

bool OAIPlay::is_home_team_runs_Set() const{
    return m_home_team_runs_isSet;
}

bool OAIPlay::is_home_team_runs_Valid() const{
    return m_home_team_runs_isValid;
}

qint32 OAIPlay::getInningBatterNumber() const {
    return m_inning_batter_number;
}
void OAIPlay::setInningBatterNumber(const qint32 &inning_batter_number) {
    m_inning_batter_number = inning_batter_number;
    m_inning_batter_number_isSet = true;
}

bool OAIPlay::is_inning_batter_number_Set() const{
    return m_inning_batter_number_isSet;
}

bool OAIPlay::is_inning_batter_number_Valid() const{
    return m_inning_batter_number_isValid;
}

QString OAIPlay::getInningHalf() const {
    return m_inning_half;
}
void OAIPlay::setInningHalf(const QString &inning_half) {
    m_inning_half = inning_half;
    m_inning_half_isSet = true;
}

bool OAIPlay::is_inning_half_Set() const{
    return m_inning_half_isSet;
}

bool OAIPlay::is_inning_half_Valid() const{
    return m_inning_half_isValid;
}

qint32 OAIPlay::getInningId() const {
    return m_inning_id;
}
void OAIPlay::setInningId(const qint32 &inning_id) {
    m_inning_id = inning_id;
    m_inning_id_isSet = true;
}

bool OAIPlay::is_inning_id_Set() const{
    return m_inning_id_isSet;
}

bool OAIPlay::is_inning_id_Valid() const{
    return m_inning_id_isValid;
}

qint32 OAIPlay::getInningNumber() const {
    return m_inning_number;
}
void OAIPlay::setInningNumber(const qint32 &inning_number) {
    m_inning_number = inning_number;
    m_inning_number_isSet = true;
}

bool OAIPlay::is_inning_number_Set() const{
    return m_inning_number_isSet;
}

bool OAIPlay::is_inning_number_Valid() const{
    return m_inning_number_isValid;
}

qint32 OAIPlay::getNumberOfOutsOnPlay() const {
    return m_number_of_outs_on_play;
}
void OAIPlay::setNumberOfOutsOnPlay(const qint32 &number_of_outs_on_play) {
    m_number_of_outs_on_play = number_of_outs_on_play;
    m_number_of_outs_on_play_isSet = true;
}

bool OAIPlay::is_number_of_outs_on_play_Set() const{
    return m_number_of_outs_on_play_isSet;
}

bool OAIPlay::is_number_of_outs_on_play_Valid() const{
    return m_number_of_outs_on_play_isValid;
}

bool OAIPlay::isOut() const {
    return m_out;
}
void OAIPlay::setOut(const bool &out) {
    m_out = out;
    m_out_isSet = true;
}

bool OAIPlay::is_out_Set() const{
    return m_out_isSet;
}

bool OAIPlay::is_out_Valid() const{
    return m_out_isValid;
}

qint32 OAIPlay::getOuts() const {
    return m_outs;
}
void OAIPlay::setOuts(const qint32 &outs) {
    m_outs = outs;
    m_outs_isSet = true;
}

bool OAIPlay::is_outs_Set() const{
    return m_outs_isSet;
}

bool OAIPlay::is_outs_Valid() const{
    return m_outs_isValid;
}

qint32 OAIPlay::getPitchNumberThisAtBat() const {
    return m_pitch_number_this_at_bat;
}
void OAIPlay::setPitchNumberThisAtBat(const qint32 &pitch_number_this_at_bat) {
    m_pitch_number_this_at_bat = pitch_number_this_at_bat;
    m_pitch_number_this_at_bat_isSet = true;
}

bool OAIPlay::is_pitch_number_this_at_bat_Set() const{
    return m_pitch_number_this_at_bat_isSet;
}

bool OAIPlay::is_pitch_number_this_at_bat_Valid() const{
    return m_pitch_number_this_at_bat_isValid;
}

qint32 OAIPlay::getPitcherId() const {
    return m_pitcher_id;
}
void OAIPlay::setPitcherId(const qint32 &pitcher_id) {
    m_pitcher_id = pitcher_id;
    m_pitcher_id_isSet = true;
}

bool OAIPlay::is_pitcher_id_Set() const{
    return m_pitcher_id_isSet;
}

bool OAIPlay::is_pitcher_id_Valid() const{
    return m_pitcher_id_isValid;
}

QString OAIPlay::getPitcherName() const {
    return m_pitcher_name;
}
void OAIPlay::setPitcherName(const QString &pitcher_name) {
    m_pitcher_name = pitcher_name;
    m_pitcher_name_isSet = true;
}

bool OAIPlay::is_pitcher_name_Set() const{
    return m_pitcher_name_isSet;
}

bool OAIPlay::is_pitcher_name_Valid() const{
    return m_pitcher_name_isValid;
}

qint32 OAIPlay::getPitcherTeamId() const {
    return m_pitcher_team_id;
}
void OAIPlay::setPitcherTeamId(const qint32 &pitcher_team_id) {
    m_pitcher_team_id = pitcher_team_id;
    m_pitcher_team_id_isSet = true;
}

bool OAIPlay::is_pitcher_team_id_Set() const{
    return m_pitcher_team_id_isSet;
}

bool OAIPlay::is_pitcher_team_id_Valid() const{
    return m_pitcher_team_id_isValid;
}

QString OAIPlay::getPitcherThrowHand() const {
    return m_pitcher_throw_hand;
}
void OAIPlay::setPitcherThrowHand(const QString &pitcher_throw_hand) {
    m_pitcher_throw_hand = pitcher_throw_hand;
    m_pitcher_throw_hand_isSet = true;
}

bool OAIPlay::is_pitcher_throw_hand_Set() const{
    return m_pitcher_throw_hand_isSet;
}

bool OAIPlay::is_pitcher_throw_hand_Valid() const{
    return m_pitcher_throw_hand_isValid;
}

QList<OAIPitch> OAIPlay::getPitches() const {
    return m_pitches;
}
void OAIPlay::setPitches(const QList<OAIPitch> &pitches) {
    m_pitches = pitches;
    m_pitches_isSet = true;
}

bool OAIPlay::is_pitches_Set() const{
    return m_pitches_isSet;
}

bool OAIPlay::is_pitches_Valid() const{
    return m_pitches_isValid;
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

qint32 OAIPlay::getPlayNumber() const {
    return m_play_number;
}
void OAIPlay::setPlayNumber(const qint32 &play_number) {
    m_play_number = play_number;
    m_play_number_isSet = true;
}

bool OAIPlay::is_play_number_Set() const{
    return m_play_number_isSet;
}

bool OAIPlay::is_play_number_Valid() const{
    return m_play_number_isValid;
}

QString OAIPlay::getResult() const {
    return m_result;
}
void OAIPlay::setResult(const QString &result) {
    m_result = result;
    m_result_isSet = true;
}

bool OAIPlay::is_result_Set() const{
    return m_result_isSet;
}

bool OAIPlay::is_result_Valid() const{
    return m_result_isValid;
}

qint32 OAIPlay::getRunner1Id() const {
    return m_runner1_id;
}
void OAIPlay::setRunner1Id(const qint32 &runner1_id) {
    m_runner1_id = runner1_id;
    m_runner1_id_isSet = true;
}

bool OAIPlay::is_runner1_id_Set() const{
    return m_runner1_id_isSet;
}

bool OAIPlay::is_runner1_id_Valid() const{
    return m_runner1_id_isValid;
}

qint32 OAIPlay::getRunner2Id() const {
    return m_runner2_id;
}
void OAIPlay::setRunner2Id(const qint32 &runner2_id) {
    m_runner2_id = runner2_id;
    m_runner2_id_isSet = true;
}

bool OAIPlay::is_runner2_id_Set() const{
    return m_runner2_id_isSet;
}

bool OAIPlay::is_runner2_id_Valid() const{
    return m_runner2_id_isValid;
}

qint32 OAIPlay::getRunner3Id() const {
    return m_runner3_id;
}
void OAIPlay::setRunner3Id(const qint32 &runner3_id) {
    m_runner3_id = runner3_id;
    m_runner3_id_isSet = true;
}

bool OAIPlay::is_runner3_id_Set() const{
    return m_runner3_id_isSet;
}

bool OAIPlay::is_runner3_id_Valid() const{
    return m_runner3_id_isValid;
}

qint32 OAIPlay::getRunsBattedIn() const {
    return m_runs_batted_in;
}
void OAIPlay::setRunsBattedIn(const qint32 &runs_batted_in) {
    m_runs_batted_in = runs_batted_in;
    m_runs_batted_in_isSet = true;
}

bool OAIPlay::is_runs_batted_in_Set() const{
    return m_runs_batted_in_isSet;
}

bool OAIPlay::is_runs_batted_in_Valid() const{
    return m_runs_batted_in_isValid;
}

bool OAIPlay::isSacrifice() const {
    return m_sacrifice;
}
void OAIPlay::setSacrifice(const bool &sacrifice) {
    m_sacrifice = sacrifice;
    m_sacrifice_isSet = true;
}

bool OAIPlay::is_sacrifice_Set() const{
    return m_sacrifice_isSet;
}

bool OAIPlay::is_sacrifice_Valid() const{
    return m_sacrifice_isValid;
}

bool OAIPlay::isStrikeout() const {
    return m_strikeout;
}
void OAIPlay::setStrikeout(const bool &strikeout) {
    m_strikeout = strikeout;
    m_strikeout_isSet = true;
}

bool OAIPlay::is_strikeout_Set() const{
    return m_strikeout_isSet;
}

bool OAIPlay::is_strikeout_Valid() const{
    return m_strikeout_isValid;
}

qint32 OAIPlay::getStrikes() const {
    return m_strikes;
}
void OAIPlay::setStrikes(const qint32 &strikes) {
    m_strikes = strikes;
    m_strikes_isSet = true;
}

bool OAIPlay::is_strikes_Set() const{
    return m_strikes_isSet;
}

bool OAIPlay::is_strikes_Valid() const{
    return m_strikes_isValid;
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

bool OAIPlay::isWalk() const {
    return m_walk;
}
void OAIPlay::setWalk(const bool &walk) {
    m_walk = walk;
    m_walk_isSet = true;
}

bool OAIPlay::is_walk_Set() const{
    return m_walk_isSet;
}

bool OAIPlay::is_walk_Valid() const{
    return m_walk_isValid;
}

bool OAIPlay::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_at_bat_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_away_team_runs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_balls_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hitter_bat_hand_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hitter_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hitter_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hitter_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hitter_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_team_runs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_inning_batter_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_inning_half_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_inning_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_inning_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_outs_on_play_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_out_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_outs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pitch_number_this_at_bat_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pitcher_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pitcher_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pitcher_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pitcher_throw_hand_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pitches.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_play_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_play_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_result_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_runner1_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_runner2_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_runner3_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_runs_batted_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sacrifice_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_strikeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_strikes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_walk_isSet) {
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
