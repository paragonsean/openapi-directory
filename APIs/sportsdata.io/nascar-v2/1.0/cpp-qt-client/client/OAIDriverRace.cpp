/**
 * NASCAR v2
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDriverRace.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDriverRace::OAIDriverRace(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDriverRace::OAIDriverRace() {
    this->initializeModel();
}

OAIDriverRace::~OAIDriverRace() {}

void OAIDriverRace::initializeModel() {

    m_bonus_isSet = false;
    m_bonus_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_current_position_isSet = false;
    m_current_position_isValid = false;

    m_date_time_isSet = false;
    m_date_time_isValid = false;

    m_day_isSet = false;
    m_day_isValid = false;

    m_draft_kings_salary_isSet = false;
    m_draft_kings_salary_isValid = false;

    m_driver_id_isSet = false;
    m_driver_id_isValid = false;

    m_fantasy_points_isSet = false;
    m_fantasy_points_isValid = false;

    m_fantasy_points_draft_kings_isSet = false;
    m_fantasy_points_draft_kings_isValid = false;

    m_fastest_laps_isSet = false;
    m_fastest_laps_isValid = false;

    m_final_position_isSet = false;
    m_final_position_isValid = false;

    m_laps_isSet = false;
    m_laps_isValid = false;

    m_laps_led_isSet = false;
    m_laps_led_isValid = false;

    m_manufacturer_isSet = false;
    m_manufacturer_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_number_display_isSet = false;
    m_number_display_isValid = false;

    m_penalty_isSet = false;
    m_penalty_isValid = false;

    m_points_isSet = false;
    m_points_isValid = false;

    m_pole_final_position_isSet = false;
    m_pole_final_position_isValid = false;

    m_poles_isSet = false;
    m_poles_isValid = false;

    m_position_differential_isSet = false;
    m_position_differential_isValid = false;

    m_qualifying_speed_isSet = false;
    m_qualifying_speed_isValid = false;

    m_race_id_isSet = false;
    m_race_id_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_start_position_isSet = false;
    m_start_position_isValid = false;

    m_stat_id_isSet = false;
    m_stat_id_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;

    m_wins_isSet = false;
    m_wins_isValid = false;
}

void OAIDriverRace::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDriverRace::fromJsonObject(QJsonObject json) {

    m_bonus_isValid = ::OpenAPI::fromJsonValue(m_bonus, json[QString("Bonus")]);
    m_bonus_isSet = !json[QString("Bonus")].isNull() && m_bonus_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("Created")]);
    m_created_isSet = !json[QString("Created")].isNull() && m_created_isValid;

    m_current_position_isValid = ::OpenAPI::fromJsonValue(m_current_position, json[QString("CurrentPosition")]);
    m_current_position_isSet = !json[QString("CurrentPosition")].isNull() && m_current_position_isValid;

    m_date_time_isValid = ::OpenAPI::fromJsonValue(m_date_time, json[QString("DateTime")]);
    m_date_time_isSet = !json[QString("DateTime")].isNull() && m_date_time_isValid;

    m_day_isValid = ::OpenAPI::fromJsonValue(m_day, json[QString("Day")]);
    m_day_isSet = !json[QString("Day")].isNull() && m_day_isValid;

    m_draft_kings_salary_isValid = ::OpenAPI::fromJsonValue(m_draft_kings_salary, json[QString("DraftKingsSalary")]);
    m_draft_kings_salary_isSet = !json[QString("DraftKingsSalary")].isNull() && m_draft_kings_salary_isValid;

    m_driver_id_isValid = ::OpenAPI::fromJsonValue(m_driver_id, json[QString("DriverID")]);
    m_driver_id_isSet = !json[QString("DriverID")].isNull() && m_driver_id_isValid;

    m_fantasy_points_isValid = ::OpenAPI::fromJsonValue(m_fantasy_points, json[QString("FantasyPoints")]);
    m_fantasy_points_isSet = !json[QString("FantasyPoints")].isNull() && m_fantasy_points_isValid;

    m_fantasy_points_draft_kings_isValid = ::OpenAPI::fromJsonValue(m_fantasy_points_draft_kings, json[QString("FantasyPointsDraftKings")]);
    m_fantasy_points_draft_kings_isSet = !json[QString("FantasyPointsDraftKings")].isNull() && m_fantasy_points_draft_kings_isValid;

    m_fastest_laps_isValid = ::OpenAPI::fromJsonValue(m_fastest_laps, json[QString("FastestLaps")]);
    m_fastest_laps_isSet = !json[QString("FastestLaps")].isNull() && m_fastest_laps_isValid;

    m_final_position_isValid = ::OpenAPI::fromJsonValue(m_final_position, json[QString("FinalPosition")]);
    m_final_position_isSet = !json[QString("FinalPosition")].isNull() && m_final_position_isValid;

    m_laps_isValid = ::OpenAPI::fromJsonValue(m_laps, json[QString("Laps")]);
    m_laps_isSet = !json[QString("Laps")].isNull() && m_laps_isValid;

    m_laps_led_isValid = ::OpenAPI::fromJsonValue(m_laps_led, json[QString("LapsLed")]);
    m_laps_led_isSet = !json[QString("LapsLed")].isNull() && m_laps_led_isValid;

    m_manufacturer_isValid = ::OpenAPI::fromJsonValue(m_manufacturer, json[QString("Manufacturer")]);
    m_manufacturer_isSet = !json[QString("Manufacturer")].isNull() && m_manufacturer_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("Number")]);
    m_number_isSet = !json[QString("Number")].isNull() && m_number_isValid;

    m_number_display_isValid = ::OpenAPI::fromJsonValue(m_number_display, json[QString("NumberDisplay")]);
    m_number_display_isSet = !json[QString("NumberDisplay")].isNull() && m_number_display_isValid;

    m_penalty_isValid = ::OpenAPI::fromJsonValue(m_penalty, json[QString("Penalty")]);
    m_penalty_isSet = !json[QString("Penalty")].isNull() && m_penalty_isValid;

    m_points_isValid = ::OpenAPI::fromJsonValue(m_points, json[QString("Points")]);
    m_points_isSet = !json[QString("Points")].isNull() && m_points_isValid;

    m_pole_final_position_isValid = ::OpenAPI::fromJsonValue(m_pole_final_position, json[QString("PoleFinalPosition")]);
    m_pole_final_position_isSet = !json[QString("PoleFinalPosition")].isNull() && m_pole_final_position_isValid;

    m_poles_isValid = ::OpenAPI::fromJsonValue(m_poles, json[QString("Poles")]);
    m_poles_isSet = !json[QString("Poles")].isNull() && m_poles_isValid;

    m_position_differential_isValid = ::OpenAPI::fromJsonValue(m_position_differential, json[QString("PositionDifferential")]);
    m_position_differential_isSet = !json[QString("PositionDifferential")].isNull() && m_position_differential_isValid;

    m_qualifying_speed_isValid = ::OpenAPI::fromJsonValue(m_qualifying_speed, json[QString("QualifyingSpeed")]);
    m_qualifying_speed_isSet = !json[QString("QualifyingSpeed")].isNull() && m_qualifying_speed_isValid;

    m_race_id_isValid = ::OpenAPI::fromJsonValue(m_race_id, json[QString("RaceID")]);
    m_race_id_isSet = !json[QString("RaceID")].isNull() && m_race_id_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("Season")]);
    m_season_isSet = !json[QString("Season")].isNull() && m_season_isValid;

    m_start_position_isValid = ::OpenAPI::fromJsonValue(m_start_position, json[QString("StartPosition")]);
    m_start_position_isSet = !json[QString("StartPosition")].isNull() && m_start_position_isValid;

    m_stat_id_isValid = ::OpenAPI::fromJsonValue(m_stat_id, json[QString("StatID")]);
    m_stat_id_isSet = !json[QString("StatID")].isNull() && m_stat_id_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;

    m_wins_isValid = ::OpenAPI::fromJsonValue(m_wins, json[QString("Wins")]);
    m_wins_isSet = !json[QString("Wins")].isNull() && m_wins_isValid;
}

QString OAIDriverRace::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDriverRace::asJsonObject() const {
    QJsonObject obj;
    if (m_bonus_isSet) {
        obj.insert(QString("Bonus"), ::OpenAPI::toJsonValue(m_bonus));
    }
    if (m_created_isSet) {
        obj.insert(QString("Created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_current_position_isSet) {
        obj.insert(QString("CurrentPosition"), ::OpenAPI::toJsonValue(m_current_position));
    }
    if (m_date_time_isSet) {
        obj.insert(QString("DateTime"), ::OpenAPI::toJsonValue(m_date_time));
    }
    if (m_day_isSet) {
        obj.insert(QString("Day"), ::OpenAPI::toJsonValue(m_day));
    }
    if (m_draft_kings_salary_isSet) {
        obj.insert(QString("DraftKingsSalary"), ::OpenAPI::toJsonValue(m_draft_kings_salary));
    }
    if (m_driver_id_isSet) {
        obj.insert(QString("DriverID"), ::OpenAPI::toJsonValue(m_driver_id));
    }
    if (m_fantasy_points_isSet) {
        obj.insert(QString("FantasyPoints"), ::OpenAPI::toJsonValue(m_fantasy_points));
    }
    if (m_fantasy_points_draft_kings_isSet) {
        obj.insert(QString("FantasyPointsDraftKings"), ::OpenAPI::toJsonValue(m_fantasy_points_draft_kings));
    }
    if (m_fastest_laps_isSet) {
        obj.insert(QString("FastestLaps"), ::OpenAPI::toJsonValue(m_fastest_laps));
    }
    if (m_final_position_isSet) {
        obj.insert(QString("FinalPosition"), ::OpenAPI::toJsonValue(m_final_position));
    }
    if (m_laps_isSet) {
        obj.insert(QString("Laps"), ::OpenAPI::toJsonValue(m_laps));
    }
    if (m_laps_led_isSet) {
        obj.insert(QString("LapsLed"), ::OpenAPI::toJsonValue(m_laps_led));
    }
    if (m_manufacturer_isSet) {
        obj.insert(QString("Manufacturer"), ::OpenAPI::toJsonValue(m_manufacturer));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_number_isSet) {
        obj.insert(QString("Number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_number_display_isSet) {
        obj.insert(QString("NumberDisplay"), ::OpenAPI::toJsonValue(m_number_display));
    }
    if (m_penalty_isSet) {
        obj.insert(QString("Penalty"), ::OpenAPI::toJsonValue(m_penalty));
    }
    if (m_points_isSet) {
        obj.insert(QString("Points"), ::OpenAPI::toJsonValue(m_points));
    }
    if (m_pole_final_position_isSet) {
        obj.insert(QString("PoleFinalPosition"), ::OpenAPI::toJsonValue(m_pole_final_position));
    }
    if (m_poles_isSet) {
        obj.insert(QString("Poles"), ::OpenAPI::toJsonValue(m_poles));
    }
    if (m_position_differential_isSet) {
        obj.insert(QString("PositionDifferential"), ::OpenAPI::toJsonValue(m_position_differential));
    }
    if (m_qualifying_speed_isSet) {
        obj.insert(QString("QualifyingSpeed"), ::OpenAPI::toJsonValue(m_qualifying_speed));
    }
    if (m_race_id_isSet) {
        obj.insert(QString("RaceID"), ::OpenAPI::toJsonValue(m_race_id));
    }
    if (m_season_isSet) {
        obj.insert(QString("Season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_start_position_isSet) {
        obj.insert(QString("StartPosition"), ::OpenAPI::toJsonValue(m_start_position));
    }
    if (m_stat_id_isSet) {
        obj.insert(QString("StatID"), ::OpenAPI::toJsonValue(m_stat_id));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    if (m_wins_isSet) {
        obj.insert(QString("Wins"), ::OpenAPI::toJsonValue(m_wins));
    }
    return obj;
}

double OAIDriverRace::getBonus() const {
    return m_bonus;
}
void OAIDriverRace::setBonus(const double &bonus) {
    m_bonus = bonus;
    m_bonus_isSet = true;
}

bool OAIDriverRace::is_bonus_Set() const{
    return m_bonus_isSet;
}

bool OAIDriverRace::is_bonus_Valid() const{
    return m_bonus_isValid;
}

QString OAIDriverRace::getCreated() const {
    return m_created;
}
void OAIDriverRace::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIDriverRace::is_created_Set() const{
    return m_created_isSet;
}

bool OAIDriverRace::is_created_Valid() const{
    return m_created_isValid;
}

double OAIDriverRace::getCurrentPosition() const {
    return m_current_position;
}
void OAIDriverRace::setCurrentPosition(const double &current_position) {
    m_current_position = current_position;
    m_current_position_isSet = true;
}

bool OAIDriverRace::is_current_position_Set() const{
    return m_current_position_isSet;
}

bool OAIDriverRace::is_current_position_Valid() const{
    return m_current_position_isValid;
}

QString OAIDriverRace::getDateTime() const {
    return m_date_time;
}
void OAIDriverRace::setDateTime(const QString &date_time) {
    m_date_time = date_time;
    m_date_time_isSet = true;
}

bool OAIDriverRace::is_date_time_Set() const{
    return m_date_time_isSet;
}

bool OAIDriverRace::is_date_time_Valid() const{
    return m_date_time_isValid;
}

QString OAIDriverRace::getDay() const {
    return m_day;
}
void OAIDriverRace::setDay(const QString &day) {
    m_day = day;
    m_day_isSet = true;
}

bool OAIDriverRace::is_day_Set() const{
    return m_day_isSet;
}

bool OAIDriverRace::is_day_Valid() const{
    return m_day_isValid;
}

qint32 OAIDriverRace::getDraftKingsSalary() const {
    return m_draft_kings_salary;
}
void OAIDriverRace::setDraftKingsSalary(const qint32 &draft_kings_salary) {
    m_draft_kings_salary = draft_kings_salary;
    m_draft_kings_salary_isSet = true;
}

bool OAIDriverRace::is_draft_kings_salary_Set() const{
    return m_draft_kings_salary_isSet;
}

bool OAIDriverRace::is_draft_kings_salary_Valid() const{
    return m_draft_kings_salary_isValid;
}

qint32 OAIDriverRace::getDriverId() const {
    return m_driver_id;
}
void OAIDriverRace::setDriverId(const qint32 &driver_id) {
    m_driver_id = driver_id;
    m_driver_id_isSet = true;
}

bool OAIDriverRace::is_driver_id_Set() const{
    return m_driver_id_isSet;
}

bool OAIDriverRace::is_driver_id_Valid() const{
    return m_driver_id_isValid;
}

double OAIDriverRace::getFantasyPoints() const {
    return m_fantasy_points;
}
void OAIDriverRace::setFantasyPoints(const double &fantasy_points) {
    m_fantasy_points = fantasy_points;
    m_fantasy_points_isSet = true;
}

bool OAIDriverRace::is_fantasy_points_Set() const{
    return m_fantasy_points_isSet;
}

bool OAIDriverRace::is_fantasy_points_Valid() const{
    return m_fantasy_points_isValid;
}

double OAIDriverRace::getFantasyPointsDraftKings() const {
    return m_fantasy_points_draft_kings;
}
void OAIDriverRace::setFantasyPointsDraftKings(const double &fantasy_points_draft_kings) {
    m_fantasy_points_draft_kings = fantasy_points_draft_kings;
    m_fantasy_points_draft_kings_isSet = true;
}

bool OAIDriverRace::is_fantasy_points_draft_kings_Set() const{
    return m_fantasy_points_draft_kings_isSet;
}

bool OAIDriverRace::is_fantasy_points_draft_kings_Valid() const{
    return m_fantasy_points_draft_kings_isValid;
}

double OAIDriverRace::getFastestLaps() const {
    return m_fastest_laps;
}
void OAIDriverRace::setFastestLaps(const double &fastest_laps) {
    m_fastest_laps = fastest_laps;
    m_fastest_laps_isSet = true;
}

bool OAIDriverRace::is_fastest_laps_Set() const{
    return m_fastest_laps_isSet;
}

bool OAIDriverRace::is_fastest_laps_Valid() const{
    return m_fastest_laps_isValid;
}

double OAIDriverRace::getFinalPosition() const {
    return m_final_position;
}
void OAIDriverRace::setFinalPosition(const double &final_position) {
    m_final_position = final_position;
    m_final_position_isSet = true;
}

bool OAIDriverRace::is_final_position_Set() const{
    return m_final_position_isSet;
}

bool OAIDriverRace::is_final_position_Valid() const{
    return m_final_position_isValid;
}

double OAIDriverRace::getLaps() const {
    return m_laps;
}
void OAIDriverRace::setLaps(const double &laps) {
    m_laps = laps;
    m_laps_isSet = true;
}

bool OAIDriverRace::is_laps_Set() const{
    return m_laps_isSet;
}

bool OAIDriverRace::is_laps_Valid() const{
    return m_laps_isValid;
}

double OAIDriverRace::getLapsLed() const {
    return m_laps_led;
}
void OAIDriverRace::setLapsLed(const double &laps_led) {
    m_laps_led = laps_led;
    m_laps_led_isSet = true;
}

bool OAIDriverRace::is_laps_led_Set() const{
    return m_laps_led_isSet;
}

bool OAIDriverRace::is_laps_led_Valid() const{
    return m_laps_led_isValid;
}

QString OAIDriverRace::getManufacturer() const {
    return m_manufacturer;
}
void OAIDriverRace::setManufacturer(const QString &manufacturer) {
    m_manufacturer = manufacturer;
    m_manufacturer_isSet = true;
}

bool OAIDriverRace::is_manufacturer_Set() const{
    return m_manufacturer_isSet;
}

bool OAIDriverRace::is_manufacturer_Valid() const{
    return m_manufacturer_isValid;
}

QString OAIDriverRace::getName() const {
    return m_name;
}
void OAIDriverRace::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDriverRace::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDriverRace::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIDriverRace::getNumber() const {
    return m_number;
}
void OAIDriverRace::setNumber(const qint32 &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIDriverRace::is_number_Set() const{
    return m_number_isSet;
}

bool OAIDriverRace::is_number_Valid() const{
    return m_number_isValid;
}

QString OAIDriverRace::getNumberDisplay() const {
    return m_number_display;
}
void OAIDriverRace::setNumberDisplay(const QString &number_display) {
    m_number_display = number_display;
    m_number_display_isSet = true;
}

bool OAIDriverRace::is_number_display_Set() const{
    return m_number_display_isSet;
}

bool OAIDriverRace::is_number_display_Valid() const{
    return m_number_display_isValid;
}

double OAIDriverRace::getPenalty() const {
    return m_penalty;
}
void OAIDriverRace::setPenalty(const double &penalty) {
    m_penalty = penalty;
    m_penalty_isSet = true;
}

bool OAIDriverRace::is_penalty_Set() const{
    return m_penalty_isSet;
}

bool OAIDriverRace::is_penalty_Valid() const{
    return m_penalty_isValid;
}

double OAIDriverRace::getPoints() const {
    return m_points;
}
void OAIDriverRace::setPoints(const double &points) {
    m_points = points;
    m_points_isSet = true;
}

bool OAIDriverRace::is_points_Set() const{
    return m_points_isSet;
}

bool OAIDriverRace::is_points_Valid() const{
    return m_points_isValid;
}

double OAIDriverRace::getPoleFinalPosition() const {
    return m_pole_final_position;
}
void OAIDriverRace::setPoleFinalPosition(const double &pole_final_position) {
    m_pole_final_position = pole_final_position;
    m_pole_final_position_isSet = true;
}

bool OAIDriverRace::is_pole_final_position_Set() const{
    return m_pole_final_position_isSet;
}

bool OAIDriverRace::is_pole_final_position_Valid() const{
    return m_pole_final_position_isValid;
}

double OAIDriverRace::getPoles() const {
    return m_poles;
}
void OAIDriverRace::setPoles(const double &poles) {
    m_poles = poles;
    m_poles_isSet = true;
}

bool OAIDriverRace::is_poles_Set() const{
    return m_poles_isSet;
}

bool OAIDriverRace::is_poles_Valid() const{
    return m_poles_isValid;
}

double OAIDriverRace::getPositionDifferential() const {
    return m_position_differential;
}
void OAIDriverRace::setPositionDifferential(const double &position_differential) {
    m_position_differential = position_differential;
    m_position_differential_isSet = true;
}

bool OAIDriverRace::is_position_differential_Set() const{
    return m_position_differential_isSet;
}

bool OAIDriverRace::is_position_differential_Valid() const{
    return m_position_differential_isValid;
}

double OAIDriverRace::getQualifyingSpeed() const {
    return m_qualifying_speed;
}
void OAIDriverRace::setQualifyingSpeed(const double &qualifying_speed) {
    m_qualifying_speed = qualifying_speed;
    m_qualifying_speed_isSet = true;
}

bool OAIDriverRace::is_qualifying_speed_Set() const{
    return m_qualifying_speed_isSet;
}

bool OAIDriverRace::is_qualifying_speed_Valid() const{
    return m_qualifying_speed_isValid;
}

qint32 OAIDriverRace::getRaceId() const {
    return m_race_id;
}
void OAIDriverRace::setRaceId(const qint32 &race_id) {
    m_race_id = race_id;
    m_race_id_isSet = true;
}

bool OAIDriverRace::is_race_id_Set() const{
    return m_race_id_isSet;
}

bool OAIDriverRace::is_race_id_Valid() const{
    return m_race_id_isValid;
}

qint32 OAIDriverRace::getSeason() const {
    return m_season;
}
void OAIDriverRace::setSeason(const qint32 &season) {
    m_season = season;
    m_season_isSet = true;
}

bool OAIDriverRace::is_season_Set() const{
    return m_season_isSet;
}

bool OAIDriverRace::is_season_Valid() const{
    return m_season_isValid;
}

double OAIDriverRace::getStartPosition() const {
    return m_start_position;
}
void OAIDriverRace::setStartPosition(const double &start_position) {
    m_start_position = start_position;
    m_start_position_isSet = true;
}

bool OAIDriverRace::is_start_position_Set() const{
    return m_start_position_isSet;
}

bool OAIDriverRace::is_start_position_Valid() const{
    return m_start_position_isValid;
}

qint32 OAIDriverRace::getStatId() const {
    return m_stat_id;
}
void OAIDriverRace::setStatId(const qint32 &stat_id) {
    m_stat_id = stat_id;
    m_stat_id_isSet = true;
}

bool OAIDriverRace::is_stat_id_Set() const{
    return m_stat_id_isSet;
}

bool OAIDriverRace::is_stat_id_Valid() const{
    return m_stat_id_isValid;
}

QString OAIDriverRace::getUpdated() const {
    return m_updated;
}
void OAIDriverRace::setUpdated(const QString &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIDriverRace::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIDriverRace::is_updated_Valid() const{
    return m_updated_isValid;
}

double OAIDriverRace::getWins() const {
    return m_wins;
}
void OAIDriverRace::setWins(const double &wins) {
    m_wins = wins;
    m_wins_isSet = true;
}

bool OAIDriverRace::is_wins_Set() const{
    return m_wins_isSet;
}

bool OAIDriverRace::is_wins_Valid() const{
    return m_wins_isValid;
}

bool OAIDriverRace::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bonus_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_current_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_day_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_draft_kings_salary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_driver_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fantasy_points_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fantasy_points_draft_kings_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fastest_laps_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_final_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_laps_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_laps_led_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_manufacturer_isSet) {
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

        if (m_number_display_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_penalty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_points_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pole_final_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_poles_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_differential_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_qualifying_speed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_race_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_season_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stat_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_isSet) {
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

bool OAIDriverRace::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
