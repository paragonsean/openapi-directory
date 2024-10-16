/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEvent_Insights_2017.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEvent_Insights_2017::OAIEvent_Insights_2017(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEvent_Insights_2017::OAIEvent_Insights_2017() {
    this->initializeModel();
}

OAIEvent_Insights_2017::~OAIEvent_Insights_2017() {}

void OAIEvent_Insights_2017::initializeModel() {

    m_average_foul_score_isSet = false;
    m_average_foul_score_isValid = false;

    m_average_fuel_points_isSet = false;
    m_average_fuel_points_isValid = false;

    m_average_fuel_points_auto_isSet = false;
    m_average_fuel_points_auto_isValid = false;

    m_average_fuel_points_teleop_isSet = false;
    m_average_fuel_points_teleop_isValid = false;

    m_average_high_goals_isSet = false;
    m_average_high_goals_isValid = false;

    m_average_high_goals_auto_isSet = false;
    m_average_high_goals_auto_isValid = false;

    m_average_high_goals_teleop_isSet = false;
    m_average_high_goals_teleop_isValid = false;

    m_average_low_goals_isSet = false;
    m_average_low_goals_isValid = false;

    m_average_low_goals_auto_isSet = false;
    m_average_low_goals_auto_isValid = false;

    m_average_low_goals_teleop_isSet = false;
    m_average_low_goals_teleop_isValid = false;

    m_average_mobility_points_auto_isSet = false;
    m_average_mobility_points_auto_isValid = false;

    m_average_points_auto_isSet = false;
    m_average_points_auto_isValid = false;

    m_average_points_teleop_isSet = false;
    m_average_points_teleop_isValid = false;

    m_average_rotor_points_isSet = false;
    m_average_rotor_points_isValid = false;

    m_average_rotor_points_auto_isSet = false;
    m_average_rotor_points_auto_isValid = false;

    m_average_rotor_points_teleop_isSet = false;
    m_average_rotor_points_teleop_isValid = false;

    m_average_score_isSet = false;
    m_average_score_isValid = false;

    m_average_takeoff_points_teleop_isSet = false;
    m_average_takeoff_points_teleop_isValid = false;

    m_average_win_margin_isSet = false;
    m_average_win_margin_isValid = false;

    m_average_win_score_isSet = false;
    m_average_win_score_isValid = false;

    m_high_kpa_isSet = false;
    m_high_kpa_isValid = false;

    m_high_score_isSet = false;
    m_high_score_isValid = false;

    m_kpa_achieved_isSet = false;
    m_kpa_achieved_isValid = false;

    m_mobility_counts_isSet = false;
    m_mobility_counts_isValid = false;

    m_rotor_1_engaged_isSet = false;
    m_rotor_1_engaged_isValid = false;

    m_rotor_1_engaged_auto_isSet = false;
    m_rotor_1_engaged_auto_isValid = false;

    m_rotor_2_engaged_isSet = false;
    m_rotor_2_engaged_isValid = false;

    m_rotor_2_engaged_auto_isSet = false;
    m_rotor_2_engaged_auto_isValid = false;

    m_rotor_3_engaged_isSet = false;
    m_rotor_3_engaged_isValid = false;

    m_rotor_4_engaged_isSet = false;
    m_rotor_4_engaged_isValid = false;

    m_takeoff_counts_isSet = false;
    m_takeoff_counts_isValid = false;

    m_unicorn_matches_isSet = false;
    m_unicorn_matches_isValid = false;
}

void OAIEvent_Insights_2017::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEvent_Insights_2017::fromJsonObject(QJsonObject json) {

    m_average_foul_score_isValid = ::OpenAPI::fromJsonValue(m_average_foul_score, json[QString("average_foul_score")]);
    m_average_foul_score_isSet = !json[QString("average_foul_score")].isNull() && m_average_foul_score_isValid;

    m_average_fuel_points_isValid = ::OpenAPI::fromJsonValue(m_average_fuel_points, json[QString("average_fuel_points")]);
    m_average_fuel_points_isSet = !json[QString("average_fuel_points")].isNull() && m_average_fuel_points_isValid;

    m_average_fuel_points_auto_isValid = ::OpenAPI::fromJsonValue(m_average_fuel_points_auto, json[QString("average_fuel_points_auto")]);
    m_average_fuel_points_auto_isSet = !json[QString("average_fuel_points_auto")].isNull() && m_average_fuel_points_auto_isValid;

    m_average_fuel_points_teleop_isValid = ::OpenAPI::fromJsonValue(m_average_fuel_points_teleop, json[QString("average_fuel_points_teleop")]);
    m_average_fuel_points_teleop_isSet = !json[QString("average_fuel_points_teleop")].isNull() && m_average_fuel_points_teleop_isValid;

    m_average_high_goals_isValid = ::OpenAPI::fromJsonValue(m_average_high_goals, json[QString("average_high_goals")]);
    m_average_high_goals_isSet = !json[QString("average_high_goals")].isNull() && m_average_high_goals_isValid;

    m_average_high_goals_auto_isValid = ::OpenAPI::fromJsonValue(m_average_high_goals_auto, json[QString("average_high_goals_auto")]);
    m_average_high_goals_auto_isSet = !json[QString("average_high_goals_auto")].isNull() && m_average_high_goals_auto_isValid;

    m_average_high_goals_teleop_isValid = ::OpenAPI::fromJsonValue(m_average_high_goals_teleop, json[QString("average_high_goals_teleop")]);
    m_average_high_goals_teleop_isSet = !json[QString("average_high_goals_teleop")].isNull() && m_average_high_goals_teleop_isValid;

    m_average_low_goals_isValid = ::OpenAPI::fromJsonValue(m_average_low_goals, json[QString("average_low_goals")]);
    m_average_low_goals_isSet = !json[QString("average_low_goals")].isNull() && m_average_low_goals_isValid;

    m_average_low_goals_auto_isValid = ::OpenAPI::fromJsonValue(m_average_low_goals_auto, json[QString("average_low_goals_auto")]);
    m_average_low_goals_auto_isSet = !json[QString("average_low_goals_auto")].isNull() && m_average_low_goals_auto_isValid;

    m_average_low_goals_teleop_isValid = ::OpenAPI::fromJsonValue(m_average_low_goals_teleop, json[QString("average_low_goals_teleop")]);
    m_average_low_goals_teleop_isSet = !json[QString("average_low_goals_teleop")].isNull() && m_average_low_goals_teleop_isValid;

    m_average_mobility_points_auto_isValid = ::OpenAPI::fromJsonValue(m_average_mobility_points_auto, json[QString("average_mobility_points_auto")]);
    m_average_mobility_points_auto_isSet = !json[QString("average_mobility_points_auto")].isNull() && m_average_mobility_points_auto_isValid;

    m_average_points_auto_isValid = ::OpenAPI::fromJsonValue(m_average_points_auto, json[QString("average_points_auto")]);
    m_average_points_auto_isSet = !json[QString("average_points_auto")].isNull() && m_average_points_auto_isValid;

    m_average_points_teleop_isValid = ::OpenAPI::fromJsonValue(m_average_points_teleop, json[QString("average_points_teleop")]);
    m_average_points_teleop_isSet = !json[QString("average_points_teleop")].isNull() && m_average_points_teleop_isValid;

    m_average_rotor_points_isValid = ::OpenAPI::fromJsonValue(m_average_rotor_points, json[QString("average_rotor_points")]);
    m_average_rotor_points_isSet = !json[QString("average_rotor_points")].isNull() && m_average_rotor_points_isValid;

    m_average_rotor_points_auto_isValid = ::OpenAPI::fromJsonValue(m_average_rotor_points_auto, json[QString("average_rotor_points_auto")]);
    m_average_rotor_points_auto_isSet = !json[QString("average_rotor_points_auto")].isNull() && m_average_rotor_points_auto_isValid;

    m_average_rotor_points_teleop_isValid = ::OpenAPI::fromJsonValue(m_average_rotor_points_teleop, json[QString("average_rotor_points_teleop")]);
    m_average_rotor_points_teleop_isSet = !json[QString("average_rotor_points_teleop")].isNull() && m_average_rotor_points_teleop_isValid;

    m_average_score_isValid = ::OpenAPI::fromJsonValue(m_average_score, json[QString("average_score")]);
    m_average_score_isSet = !json[QString("average_score")].isNull() && m_average_score_isValid;

    m_average_takeoff_points_teleop_isValid = ::OpenAPI::fromJsonValue(m_average_takeoff_points_teleop, json[QString("average_takeoff_points_teleop")]);
    m_average_takeoff_points_teleop_isSet = !json[QString("average_takeoff_points_teleop")].isNull() && m_average_takeoff_points_teleop_isValid;

    m_average_win_margin_isValid = ::OpenAPI::fromJsonValue(m_average_win_margin, json[QString("average_win_margin")]);
    m_average_win_margin_isSet = !json[QString("average_win_margin")].isNull() && m_average_win_margin_isValid;

    m_average_win_score_isValid = ::OpenAPI::fromJsonValue(m_average_win_score, json[QString("average_win_score")]);
    m_average_win_score_isSet = !json[QString("average_win_score")].isNull() && m_average_win_score_isValid;

    m_high_kpa_isValid = ::OpenAPI::fromJsonValue(m_high_kpa, json[QString("high_kpa")]);
    m_high_kpa_isSet = !json[QString("high_kpa")].isNull() && m_high_kpa_isValid;

    m_high_score_isValid = ::OpenAPI::fromJsonValue(m_high_score, json[QString("high_score")]);
    m_high_score_isSet = !json[QString("high_score")].isNull() && m_high_score_isValid;

    m_kpa_achieved_isValid = ::OpenAPI::fromJsonValue(m_kpa_achieved, json[QString("kpa_achieved")]);
    m_kpa_achieved_isSet = !json[QString("kpa_achieved")].isNull() && m_kpa_achieved_isValid;

    m_mobility_counts_isValid = ::OpenAPI::fromJsonValue(m_mobility_counts, json[QString("mobility_counts")]);
    m_mobility_counts_isSet = !json[QString("mobility_counts")].isNull() && m_mobility_counts_isValid;

    m_rotor_1_engaged_isValid = ::OpenAPI::fromJsonValue(m_rotor_1_engaged, json[QString("rotor_1_engaged")]);
    m_rotor_1_engaged_isSet = !json[QString("rotor_1_engaged")].isNull() && m_rotor_1_engaged_isValid;

    m_rotor_1_engaged_auto_isValid = ::OpenAPI::fromJsonValue(m_rotor_1_engaged_auto, json[QString("rotor_1_engaged_auto")]);
    m_rotor_1_engaged_auto_isSet = !json[QString("rotor_1_engaged_auto")].isNull() && m_rotor_1_engaged_auto_isValid;

    m_rotor_2_engaged_isValid = ::OpenAPI::fromJsonValue(m_rotor_2_engaged, json[QString("rotor_2_engaged")]);
    m_rotor_2_engaged_isSet = !json[QString("rotor_2_engaged")].isNull() && m_rotor_2_engaged_isValid;

    m_rotor_2_engaged_auto_isValid = ::OpenAPI::fromJsonValue(m_rotor_2_engaged_auto, json[QString("rotor_2_engaged_auto")]);
    m_rotor_2_engaged_auto_isSet = !json[QString("rotor_2_engaged_auto")].isNull() && m_rotor_2_engaged_auto_isValid;

    m_rotor_3_engaged_isValid = ::OpenAPI::fromJsonValue(m_rotor_3_engaged, json[QString("rotor_3_engaged")]);
    m_rotor_3_engaged_isSet = !json[QString("rotor_3_engaged")].isNull() && m_rotor_3_engaged_isValid;

    m_rotor_4_engaged_isValid = ::OpenAPI::fromJsonValue(m_rotor_4_engaged, json[QString("rotor_4_engaged")]);
    m_rotor_4_engaged_isSet = !json[QString("rotor_4_engaged")].isNull() && m_rotor_4_engaged_isValid;

    m_takeoff_counts_isValid = ::OpenAPI::fromJsonValue(m_takeoff_counts, json[QString("takeoff_counts")]);
    m_takeoff_counts_isSet = !json[QString("takeoff_counts")].isNull() && m_takeoff_counts_isValid;

    m_unicorn_matches_isValid = ::OpenAPI::fromJsonValue(m_unicorn_matches, json[QString("unicorn_matches")]);
    m_unicorn_matches_isSet = !json[QString("unicorn_matches")].isNull() && m_unicorn_matches_isValid;
}

QString OAIEvent_Insights_2017::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEvent_Insights_2017::asJsonObject() const {
    QJsonObject obj;
    if (m_average_foul_score_isSet) {
        obj.insert(QString("average_foul_score"), ::OpenAPI::toJsonValue(m_average_foul_score));
    }
    if (m_average_fuel_points_isSet) {
        obj.insert(QString("average_fuel_points"), ::OpenAPI::toJsonValue(m_average_fuel_points));
    }
    if (m_average_fuel_points_auto_isSet) {
        obj.insert(QString("average_fuel_points_auto"), ::OpenAPI::toJsonValue(m_average_fuel_points_auto));
    }
    if (m_average_fuel_points_teleop_isSet) {
        obj.insert(QString("average_fuel_points_teleop"), ::OpenAPI::toJsonValue(m_average_fuel_points_teleop));
    }
    if (m_average_high_goals_isSet) {
        obj.insert(QString("average_high_goals"), ::OpenAPI::toJsonValue(m_average_high_goals));
    }
    if (m_average_high_goals_auto_isSet) {
        obj.insert(QString("average_high_goals_auto"), ::OpenAPI::toJsonValue(m_average_high_goals_auto));
    }
    if (m_average_high_goals_teleop_isSet) {
        obj.insert(QString("average_high_goals_teleop"), ::OpenAPI::toJsonValue(m_average_high_goals_teleop));
    }
    if (m_average_low_goals_isSet) {
        obj.insert(QString("average_low_goals"), ::OpenAPI::toJsonValue(m_average_low_goals));
    }
    if (m_average_low_goals_auto_isSet) {
        obj.insert(QString("average_low_goals_auto"), ::OpenAPI::toJsonValue(m_average_low_goals_auto));
    }
    if (m_average_low_goals_teleop_isSet) {
        obj.insert(QString("average_low_goals_teleop"), ::OpenAPI::toJsonValue(m_average_low_goals_teleop));
    }
    if (m_average_mobility_points_auto_isSet) {
        obj.insert(QString("average_mobility_points_auto"), ::OpenAPI::toJsonValue(m_average_mobility_points_auto));
    }
    if (m_average_points_auto_isSet) {
        obj.insert(QString("average_points_auto"), ::OpenAPI::toJsonValue(m_average_points_auto));
    }
    if (m_average_points_teleop_isSet) {
        obj.insert(QString("average_points_teleop"), ::OpenAPI::toJsonValue(m_average_points_teleop));
    }
    if (m_average_rotor_points_isSet) {
        obj.insert(QString("average_rotor_points"), ::OpenAPI::toJsonValue(m_average_rotor_points));
    }
    if (m_average_rotor_points_auto_isSet) {
        obj.insert(QString("average_rotor_points_auto"), ::OpenAPI::toJsonValue(m_average_rotor_points_auto));
    }
    if (m_average_rotor_points_teleop_isSet) {
        obj.insert(QString("average_rotor_points_teleop"), ::OpenAPI::toJsonValue(m_average_rotor_points_teleop));
    }
    if (m_average_score_isSet) {
        obj.insert(QString("average_score"), ::OpenAPI::toJsonValue(m_average_score));
    }
    if (m_average_takeoff_points_teleop_isSet) {
        obj.insert(QString("average_takeoff_points_teleop"), ::OpenAPI::toJsonValue(m_average_takeoff_points_teleop));
    }
    if (m_average_win_margin_isSet) {
        obj.insert(QString("average_win_margin"), ::OpenAPI::toJsonValue(m_average_win_margin));
    }
    if (m_average_win_score_isSet) {
        obj.insert(QString("average_win_score"), ::OpenAPI::toJsonValue(m_average_win_score));
    }
    if (m_high_kpa.size() > 0) {
        obj.insert(QString("high_kpa"), ::OpenAPI::toJsonValue(m_high_kpa));
    }
    if (m_high_score.size() > 0) {
        obj.insert(QString("high_score"), ::OpenAPI::toJsonValue(m_high_score));
    }
    if (m_kpa_achieved.size() > 0) {
        obj.insert(QString("kpa_achieved"), ::OpenAPI::toJsonValue(m_kpa_achieved));
    }
    if (m_mobility_counts.size() > 0) {
        obj.insert(QString("mobility_counts"), ::OpenAPI::toJsonValue(m_mobility_counts));
    }
    if (m_rotor_1_engaged.size() > 0) {
        obj.insert(QString("rotor_1_engaged"), ::OpenAPI::toJsonValue(m_rotor_1_engaged));
    }
    if (m_rotor_1_engaged_auto.size() > 0) {
        obj.insert(QString("rotor_1_engaged_auto"), ::OpenAPI::toJsonValue(m_rotor_1_engaged_auto));
    }
    if (m_rotor_2_engaged.size() > 0) {
        obj.insert(QString("rotor_2_engaged"), ::OpenAPI::toJsonValue(m_rotor_2_engaged));
    }
    if (m_rotor_2_engaged_auto.size() > 0) {
        obj.insert(QString("rotor_2_engaged_auto"), ::OpenAPI::toJsonValue(m_rotor_2_engaged_auto));
    }
    if (m_rotor_3_engaged.size() > 0) {
        obj.insert(QString("rotor_3_engaged"), ::OpenAPI::toJsonValue(m_rotor_3_engaged));
    }
    if (m_rotor_4_engaged.size() > 0) {
        obj.insert(QString("rotor_4_engaged"), ::OpenAPI::toJsonValue(m_rotor_4_engaged));
    }
    if (m_takeoff_counts.size() > 0) {
        obj.insert(QString("takeoff_counts"), ::OpenAPI::toJsonValue(m_takeoff_counts));
    }
    if (m_unicorn_matches.size() > 0) {
        obj.insert(QString("unicorn_matches"), ::OpenAPI::toJsonValue(m_unicorn_matches));
    }
    return obj;
}

float OAIEvent_Insights_2017::getAverageFoulScore() const {
    return m_average_foul_score;
}
void OAIEvent_Insights_2017::setAverageFoulScore(const float &average_foul_score) {
    m_average_foul_score = average_foul_score;
    m_average_foul_score_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_foul_score_Set() const{
    return m_average_foul_score_isSet;
}

bool OAIEvent_Insights_2017::is_average_foul_score_Valid() const{
    return m_average_foul_score_isValid;
}

float OAIEvent_Insights_2017::getAverageFuelPoints() const {
    return m_average_fuel_points;
}
void OAIEvent_Insights_2017::setAverageFuelPoints(const float &average_fuel_points) {
    m_average_fuel_points = average_fuel_points;
    m_average_fuel_points_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_fuel_points_Set() const{
    return m_average_fuel_points_isSet;
}

bool OAIEvent_Insights_2017::is_average_fuel_points_Valid() const{
    return m_average_fuel_points_isValid;
}

float OAIEvent_Insights_2017::getAverageFuelPointsAuto() const {
    return m_average_fuel_points_auto;
}
void OAIEvent_Insights_2017::setAverageFuelPointsAuto(const float &average_fuel_points_auto) {
    m_average_fuel_points_auto = average_fuel_points_auto;
    m_average_fuel_points_auto_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_fuel_points_auto_Set() const{
    return m_average_fuel_points_auto_isSet;
}

bool OAIEvent_Insights_2017::is_average_fuel_points_auto_Valid() const{
    return m_average_fuel_points_auto_isValid;
}

float OAIEvent_Insights_2017::getAverageFuelPointsTeleop() const {
    return m_average_fuel_points_teleop;
}
void OAIEvent_Insights_2017::setAverageFuelPointsTeleop(const float &average_fuel_points_teleop) {
    m_average_fuel_points_teleop = average_fuel_points_teleop;
    m_average_fuel_points_teleop_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_fuel_points_teleop_Set() const{
    return m_average_fuel_points_teleop_isSet;
}

bool OAIEvent_Insights_2017::is_average_fuel_points_teleop_Valid() const{
    return m_average_fuel_points_teleop_isValid;
}

float OAIEvent_Insights_2017::getAverageHighGoals() const {
    return m_average_high_goals;
}
void OAIEvent_Insights_2017::setAverageHighGoals(const float &average_high_goals) {
    m_average_high_goals = average_high_goals;
    m_average_high_goals_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_high_goals_Set() const{
    return m_average_high_goals_isSet;
}

bool OAIEvent_Insights_2017::is_average_high_goals_Valid() const{
    return m_average_high_goals_isValid;
}

float OAIEvent_Insights_2017::getAverageHighGoalsAuto() const {
    return m_average_high_goals_auto;
}
void OAIEvent_Insights_2017::setAverageHighGoalsAuto(const float &average_high_goals_auto) {
    m_average_high_goals_auto = average_high_goals_auto;
    m_average_high_goals_auto_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_high_goals_auto_Set() const{
    return m_average_high_goals_auto_isSet;
}

bool OAIEvent_Insights_2017::is_average_high_goals_auto_Valid() const{
    return m_average_high_goals_auto_isValid;
}

float OAIEvent_Insights_2017::getAverageHighGoalsTeleop() const {
    return m_average_high_goals_teleop;
}
void OAIEvent_Insights_2017::setAverageHighGoalsTeleop(const float &average_high_goals_teleop) {
    m_average_high_goals_teleop = average_high_goals_teleop;
    m_average_high_goals_teleop_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_high_goals_teleop_Set() const{
    return m_average_high_goals_teleop_isSet;
}

bool OAIEvent_Insights_2017::is_average_high_goals_teleop_Valid() const{
    return m_average_high_goals_teleop_isValid;
}

float OAIEvent_Insights_2017::getAverageLowGoals() const {
    return m_average_low_goals;
}
void OAIEvent_Insights_2017::setAverageLowGoals(const float &average_low_goals) {
    m_average_low_goals = average_low_goals;
    m_average_low_goals_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_low_goals_Set() const{
    return m_average_low_goals_isSet;
}

bool OAIEvent_Insights_2017::is_average_low_goals_Valid() const{
    return m_average_low_goals_isValid;
}

float OAIEvent_Insights_2017::getAverageLowGoalsAuto() const {
    return m_average_low_goals_auto;
}
void OAIEvent_Insights_2017::setAverageLowGoalsAuto(const float &average_low_goals_auto) {
    m_average_low_goals_auto = average_low_goals_auto;
    m_average_low_goals_auto_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_low_goals_auto_Set() const{
    return m_average_low_goals_auto_isSet;
}

bool OAIEvent_Insights_2017::is_average_low_goals_auto_Valid() const{
    return m_average_low_goals_auto_isValid;
}

float OAIEvent_Insights_2017::getAverageLowGoalsTeleop() const {
    return m_average_low_goals_teleop;
}
void OAIEvent_Insights_2017::setAverageLowGoalsTeleop(const float &average_low_goals_teleop) {
    m_average_low_goals_teleop = average_low_goals_teleop;
    m_average_low_goals_teleop_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_low_goals_teleop_Set() const{
    return m_average_low_goals_teleop_isSet;
}

bool OAIEvent_Insights_2017::is_average_low_goals_teleop_Valid() const{
    return m_average_low_goals_teleop_isValid;
}

float OAIEvent_Insights_2017::getAverageMobilityPointsAuto() const {
    return m_average_mobility_points_auto;
}
void OAIEvent_Insights_2017::setAverageMobilityPointsAuto(const float &average_mobility_points_auto) {
    m_average_mobility_points_auto = average_mobility_points_auto;
    m_average_mobility_points_auto_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_mobility_points_auto_Set() const{
    return m_average_mobility_points_auto_isSet;
}

bool OAIEvent_Insights_2017::is_average_mobility_points_auto_Valid() const{
    return m_average_mobility_points_auto_isValid;
}

float OAIEvent_Insights_2017::getAveragePointsAuto() const {
    return m_average_points_auto;
}
void OAIEvent_Insights_2017::setAveragePointsAuto(const float &average_points_auto) {
    m_average_points_auto = average_points_auto;
    m_average_points_auto_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_points_auto_Set() const{
    return m_average_points_auto_isSet;
}

bool OAIEvent_Insights_2017::is_average_points_auto_Valid() const{
    return m_average_points_auto_isValid;
}

float OAIEvent_Insights_2017::getAveragePointsTeleop() const {
    return m_average_points_teleop;
}
void OAIEvent_Insights_2017::setAveragePointsTeleop(const float &average_points_teleop) {
    m_average_points_teleop = average_points_teleop;
    m_average_points_teleop_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_points_teleop_Set() const{
    return m_average_points_teleop_isSet;
}

bool OAIEvent_Insights_2017::is_average_points_teleop_Valid() const{
    return m_average_points_teleop_isValid;
}

float OAIEvent_Insights_2017::getAverageRotorPoints() const {
    return m_average_rotor_points;
}
void OAIEvent_Insights_2017::setAverageRotorPoints(const float &average_rotor_points) {
    m_average_rotor_points = average_rotor_points;
    m_average_rotor_points_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_rotor_points_Set() const{
    return m_average_rotor_points_isSet;
}

bool OAIEvent_Insights_2017::is_average_rotor_points_Valid() const{
    return m_average_rotor_points_isValid;
}

float OAIEvent_Insights_2017::getAverageRotorPointsAuto() const {
    return m_average_rotor_points_auto;
}
void OAIEvent_Insights_2017::setAverageRotorPointsAuto(const float &average_rotor_points_auto) {
    m_average_rotor_points_auto = average_rotor_points_auto;
    m_average_rotor_points_auto_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_rotor_points_auto_Set() const{
    return m_average_rotor_points_auto_isSet;
}

bool OAIEvent_Insights_2017::is_average_rotor_points_auto_Valid() const{
    return m_average_rotor_points_auto_isValid;
}

float OAIEvent_Insights_2017::getAverageRotorPointsTeleop() const {
    return m_average_rotor_points_teleop;
}
void OAIEvent_Insights_2017::setAverageRotorPointsTeleop(const float &average_rotor_points_teleop) {
    m_average_rotor_points_teleop = average_rotor_points_teleop;
    m_average_rotor_points_teleop_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_rotor_points_teleop_Set() const{
    return m_average_rotor_points_teleop_isSet;
}

bool OAIEvent_Insights_2017::is_average_rotor_points_teleop_Valid() const{
    return m_average_rotor_points_teleop_isValid;
}

float OAIEvent_Insights_2017::getAverageScore() const {
    return m_average_score;
}
void OAIEvent_Insights_2017::setAverageScore(const float &average_score) {
    m_average_score = average_score;
    m_average_score_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_score_Set() const{
    return m_average_score_isSet;
}

bool OAIEvent_Insights_2017::is_average_score_Valid() const{
    return m_average_score_isValid;
}

float OAIEvent_Insights_2017::getAverageTakeoffPointsTeleop() const {
    return m_average_takeoff_points_teleop;
}
void OAIEvent_Insights_2017::setAverageTakeoffPointsTeleop(const float &average_takeoff_points_teleop) {
    m_average_takeoff_points_teleop = average_takeoff_points_teleop;
    m_average_takeoff_points_teleop_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_takeoff_points_teleop_Set() const{
    return m_average_takeoff_points_teleop_isSet;
}

bool OAIEvent_Insights_2017::is_average_takeoff_points_teleop_Valid() const{
    return m_average_takeoff_points_teleop_isValid;
}

float OAIEvent_Insights_2017::getAverageWinMargin() const {
    return m_average_win_margin;
}
void OAIEvent_Insights_2017::setAverageWinMargin(const float &average_win_margin) {
    m_average_win_margin = average_win_margin;
    m_average_win_margin_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_win_margin_Set() const{
    return m_average_win_margin_isSet;
}

bool OAIEvent_Insights_2017::is_average_win_margin_Valid() const{
    return m_average_win_margin_isValid;
}

float OAIEvent_Insights_2017::getAverageWinScore() const {
    return m_average_win_score;
}
void OAIEvent_Insights_2017::setAverageWinScore(const float &average_win_score) {
    m_average_win_score = average_win_score;
    m_average_win_score_isSet = true;
}

bool OAIEvent_Insights_2017::is_average_win_score_Set() const{
    return m_average_win_score_isSet;
}

bool OAIEvent_Insights_2017::is_average_win_score_Valid() const{
    return m_average_win_score_isValid;
}

QList<QString> OAIEvent_Insights_2017::getHighKpa() const {
    return m_high_kpa;
}
void OAIEvent_Insights_2017::setHighKpa(const QList<QString> &high_kpa) {
    m_high_kpa = high_kpa;
    m_high_kpa_isSet = true;
}

bool OAIEvent_Insights_2017::is_high_kpa_Set() const{
    return m_high_kpa_isSet;
}

bool OAIEvent_Insights_2017::is_high_kpa_Valid() const{
    return m_high_kpa_isValid;
}

QList<QString> OAIEvent_Insights_2017::getHighScore() const {
    return m_high_score;
}
void OAIEvent_Insights_2017::setHighScore(const QList<QString> &high_score) {
    m_high_score = high_score;
    m_high_score_isSet = true;
}

bool OAIEvent_Insights_2017::is_high_score_Set() const{
    return m_high_score_isSet;
}

bool OAIEvent_Insights_2017::is_high_score_Valid() const{
    return m_high_score_isValid;
}

QList<float> OAIEvent_Insights_2017::getKpaAchieved() const {
    return m_kpa_achieved;
}
void OAIEvent_Insights_2017::setKpaAchieved(const QList<float> &kpa_achieved) {
    m_kpa_achieved = kpa_achieved;
    m_kpa_achieved_isSet = true;
}

bool OAIEvent_Insights_2017::is_kpa_achieved_Set() const{
    return m_kpa_achieved_isSet;
}

bool OAIEvent_Insights_2017::is_kpa_achieved_Valid() const{
    return m_kpa_achieved_isValid;
}

QList<float> OAIEvent_Insights_2017::getMobilityCounts() const {
    return m_mobility_counts;
}
void OAIEvent_Insights_2017::setMobilityCounts(const QList<float> &mobility_counts) {
    m_mobility_counts = mobility_counts;
    m_mobility_counts_isSet = true;
}

bool OAIEvent_Insights_2017::is_mobility_counts_Set() const{
    return m_mobility_counts_isSet;
}

bool OAIEvent_Insights_2017::is_mobility_counts_Valid() const{
    return m_mobility_counts_isValid;
}

QList<float> OAIEvent_Insights_2017::getRotor1Engaged() const {
    return m_rotor_1_engaged;
}
void OAIEvent_Insights_2017::setRotor1Engaged(const QList<float> &rotor_1_engaged) {
    m_rotor_1_engaged = rotor_1_engaged;
    m_rotor_1_engaged_isSet = true;
}

bool OAIEvent_Insights_2017::is_rotor_1_engaged_Set() const{
    return m_rotor_1_engaged_isSet;
}

bool OAIEvent_Insights_2017::is_rotor_1_engaged_Valid() const{
    return m_rotor_1_engaged_isValid;
}

QList<float> OAIEvent_Insights_2017::getRotor1EngagedAuto() const {
    return m_rotor_1_engaged_auto;
}
void OAIEvent_Insights_2017::setRotor1EngagedAuto(const QList<float> &rotor_1_engaged_auto) {
    m_rotor_1_engaged_auto = rotor_1_engaged_auto;
    m_rotor_1_engaged_auto_isSet = true;
}

bool OAIEvent_Insights_2017::is_rotor_1_engaged_auto_Set() const{
    return m_rotor_1_engaged_auto_isSet;
}

bool OAIEvent_Insights_2017::is_rotor_1_engaged_auto_Valid() const{
    return m_rotor_1_engaged_auto_isValid;
}

QList<float> OAIEvent_Insights_2017::getRotor2Engaged() const {
    return m_rotor_2_engaged;
}
void OAIEvent_Insights_2017::setRotor2Engaged(const QList<float> &rotor_2_engaged) {
    m_rotor_2_engaged = rotor_2_engaged;
    m_rotor_2_engaged_isSet = true;
}

bool OAIEvent_Insights_2017::is_rotor_2_engaged_Set() const{
    return m_rotor_2_engaged_isSet;
}

bool OAIEvent_Insights_2017::is_rotor_2_engaged_Valid() const{
    return m_rotor_2_engaged_isValid;
}

QList<float> OAIEvent_Insights_2017::getRotor2EngagedAuto() const {
    return m_rotor_2_engaged_auto;
}
void OAIEvent_Insights_2017::setRotor2EngagedAuto(const QList<float> &rotor_2_engaged_auto) {
    m_rotor_2_engaged_auto = rotor_2_engaged_auto;
    m_rotor_2_engaged_auto_isSet = true;
}

bool OAIEvent_Insights_2017::is_rotor_2_engaged_auto_Set() const{
    return m_rotor_2_engaged_auto_isSet;
}

bool OAIEvent_Insights_2017::is_rotor_2_engaged_auto_Valid() const{
    return m_rotor_2_engaged_auto_isValid;
}

QList<float> OAIEvent_Insights_2017::getRotor3Engaged() const {
    return m_rotor_3_engaged;
}
void OAIEvent_Insights_2017::setRotor3Engaged(const QList<float> &rotor_3_engaged) {
    m_rotor_3_engaged = rotor_3_engaged;
    m_rotor_3_engaged_isSet = true;
}

bool OAIEvent_Insights_2017::is_rotor_3_engaged_Set() const{
    return m_rotor_3_engaged_isSet;
}

bool OAIEvent_Insights_2017::is_rotor_3_engaged_Valid() const{
    return m_rotor_3_engaged_isValid;
}

QList<float> OAIEvent_Insights_2017::getRotor4Engaged() const {
    return m_rotor_4_engaged;
}
void OAIEvent_Insights_2017::setRotor4Engaged(const QList<float> &rotor_4_engaged) {
    m_rotor_4_engaged = rotor_4_engaged;
    m_rotor_4_engaged_isSet = true;
}

bool OAIEvent_Insights_2017::is_rotor_4_engaged_Set() const{
    return m_rotor_4_engaged_isSet;
}

bool OAIEvent_Insights_2017::is_rotor_4_engaged_Valid() const{
    return m_rotor_4_engaged_isValid;
}

QList<float> OAIEvent_Insights_2017::getTakeoffCounts() const {
    return m_takeoff_counts;
}
void OAIEvent_Insights_2017::setTakeoffCounts(const QList<float> &takeoff_counts) {
    m_takeoff_counts = takeoff_counts;
    m_takeoff_counts_isSet = true;
}

bool OAIEvent_Insights_2017::is_takeoff_counts_Set() const{
    return m_takeoff_counts_isSet;
}

bool OAIEvent_Insights_2017::is_takeoff_counts_Valid() const{
    return m_takeoff_counts_isValid;
}

QList<float> OAIEvent_Insights_2017::getUnicornMatches() const {
    return m_unicorn_matches;
}
void OAIEvent_Insights_2017::setUnicornMatches(const QList<float> &unicorn_matches) {
    m_unicorn_matches = unicorn_matches;
    m_unicorn_matches_isSet = true;
}

bool OAIEvent_Insights_2017::is_unicorn_matches_Set() const{
    return m_unicorn_matches_isSet;
}

bool OAIEvent_Insights_2017::is_unicorn_matches_Valid() const{
    return m_unicorn_matches_isValid;
}

bool OAIEvent_Insights_2017::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_average_foul_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_fuel_points_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_fuel_points_auto_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_fuel_points_teleop_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_high_goals_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_high_goals_auto_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_high_goals_teleop_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_low_goals_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_low_goals_auto_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_low_goals_teleop_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_mobility_points_auto_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_points_auto_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_points_teleop_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_rotor_points_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_rotor_points_auto_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_rotor_points_teleop_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_takeoff_points_teleop_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_win_margin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_win_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_high_kpa.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_high_score.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_kpa_achieved.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_mobility_counts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rotor_1_engaged.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rotor_1_engaged_auto.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rotor_2_engaged.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rotor_2_engaged_auto.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rotor_3_engaged.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rotor_4_engaged.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_takeoff_counts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_unicorn_matches.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEvent_Insights_2017::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_average_foul_score_isValid && m_average_fuel_points_isValid && m_average_fuel_points_auto_isValid && m_average_fuel_points_teleop_isValid && m_average_high_goals_isValid && m_average_high_goals_auto_isValid && m_average_high_goals_teleop_isValid && m_average_low_goals_isValid && m_average_low_goals_auto_isValid && m_average_low_goals_teleop_isValid && m_average_mobility_points_auto_isValid && m_average_points_auto_isValid && m_average_points_teleop_isValid && m_average_rotor_points_isValid && m_average_rotor_points_auto_isValid && m_average_rotor_points_teleop_isValid && m_average_score_isValid && m_average_takeoff_points_teleop_isValid && m_average_win_margin_isValid && m_average_win_score_isValid && m_high_kpa_isValid && m_high_score_isValid && m_kpa_achieved_isValid && m_mobility_counts_isValid && m_rotor_1_engaged_isValid && m_rotor_1_engaged_auto_isValid && m_rotor_2_engaged_isValid && m_rotor_2_engaged_auto_isValid && m_rotor_3_engaged_isValid && m_rotor_4_engaged_isValid && m_takeoff_counts_isValid && m_unicorn_matches_isValid && true;
}

} // namespace OpenAPI
