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

/*
 * OAIDriverRaceProjection.h
 *
 * 
 */

#ifndef OAIDriverRaceProjection_H
#define OAIDriverRaceProjection_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDriverRaceProjection : public OAIObject {
public:
    OAIDriverRaceProjection();
    OAIDriverRaceProjection(QString json);
    ~OAIDriverRaceProjection() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getBonus() const;
    void setBonus(const double &bonus);
    bool is_bonus_Set() const;
    bool is_bonus_Valid() const;

    QString getCreated() const;
    void setCreated(const QString &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    double getCurrentPosition() const;
    void setCurrentPosition(const double &current_position);
    bool is_current_position_Set() const;
    bool is_current_position_Valid() const;

    QString getDateTime() const;
    void setDateTime(const QString &date_time);
    bool is_date_time_Set() const;
    bool is_date_time_Valid() const;

    QString getDay() const;
    void setDay(const QString &day);
    bool is_day_Set() const;
    bool is_day_Valid() const;

    qint32 getDraftKingsSalary() const;
    void setDraftKingsSalary(const qint32 &draft_kings_salary);
    bool is_draft_kings_salary_Set() const;
    bool is_draft_kings_salary_Valid() const;

    qint32 getDriverId() const;
    void setDriverId(const qint32 &driver_id);
    bool is_driver_id_Set() const;
    bool is_driver_id_Valid() const;

    double getFantasyPoints() const;
    void setFantasyPoints(const double &fantasy_points);
    bool is_fantasy_points_Set() const;
    bool is_fantasy_points_Valid() const;

    double getFantasyPointsDraftKings() const;
    void setFantasyPointsDraftKings(const double &fantasy_points_draft_kings);
    bool is_fantasy_points_draft_kings_Set() const;
    bool is_fantasy_points_draft_kings_Valid() const;

    double getFastestLaps() const;
    void setFastestLaps(const double &fastest_laps);
    bool is_fastest_laps_Set() const;
    bool is_fastest_laps_Valid() const;

    double getFinalPosition() const;
    void setFinalPosition(const double &final_position);
    bool is_final_position_Set() const;
    bool is_final_position_Valid() const;

    double getLaps() const;
    void setLaps(const double &laps);
    bool is_laps_Set() const;
    bool is_laps_Valid() const;

    double getLapsLed() const;
    void setLapsLed(const double &laps_led);
    bool is_laps_led_Set() const;
    bool is_laps_led_Valid() const;

    QString getManufacturer() const;
    void setManufacturer(const QString &manufacturer);
    bool is_manufacturer_Set() const;
    bool is_manufacturer_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNumber() const;
    void setNumber(const qint32 &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    QString getNumberDisplay() const;
    void setNumberDisplay(const QString &number_display);
    bool is_number_display_Set() const;
    bool is_number_display_Valid() const;

    double getPenalty() const;
    void setPenalty(const double &penalty);
    bool is_penalty_Set() const;
    bool is_penalty_Valid() const;

    double getPoints() const;
    void setPoints(const double &points);
    bool is_points_Set() const;
    bool is_points_Valid() const;

    double getPoleFinalPosition() const;
    void setPoleFinalPosition(const double &pole_final_position);
    bool is_pole_final_position_Set() const;
    bool is_pole_final_position_Valid() const;

    double getPoles() const;
    void setPoles(const double &poles);
    bool is_poles_Set() const;
    bool is_poles_Valid() const;

    double getPositionDifferential() const;
    void setPositionDifferential(const double &position_differential);
    bool is_position_differential_Set() const;
    bool is_position_differential_Valid() const;

    double getQualifyingSpeed() const;
    void setQualifyingSpeed(const double &qualifying_speed);
    bool is_qualifying_speed_Set() const;
    bool is_qualifying_speed_Valid() const;

    qint32 getRaceId() const;
    void setRaceId(const qint32 &race_id);
    bool is_race_id_Set() const;
    bool is_race_id_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    double getStartPosition() const;
    void setStartPosition(const double &start_position);
    bool is_start_position_Set() const;
    bool is_start_position_Valid() const;

    qint32 getStatId() const;
    void setStatId(const qint32 &stat_id);
    bool is_stat_id_Set() const;
    bool is_stat_id_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    double getWins() const;
    void setWins(const double &wins);
    bool is_wins_Set() const;
    bool is_wins_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_bonus;
    bool m_bonus_isSet;
    bool m_bonus_isValid;

    QString m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    double m_current_position;
    bool m_current_position_isSet;
    bool m_current_position_isValid;

    QString m_date_time;
    bool m_date_time_isSet;
    bool m_date_time_isValid;

    QString m_day;
    bool m_day_isSet;
    bool m_day_isValid;

    qint32 m_draft_kings_salary;
    bool m_draft_kings_salary_isSet;
    bool m_draft_kings_salary_isValid;

    qint32 m_driver_id;
    bool m_driver_id_isSet;
    bool m_driver_id_isValid;

    double m_fantasy_points;
    bool m_fantasy_points_isSet;
    bool m_fantasy_points_isValid;

    double m_fantasy_points_draft_kings;
    bool m_fantasy_points_draft_kings_isSet;
    bool m_fantasy_points_draft_kings_isValid;

    double m_fastest_laps;
    bool m_fastest_laps_isSet;
    bool m_fastest_laps_isValid;

    double m_final_position;
    bool m_final_position_isSet;
    bool m_final_position_isValid;

    double m_laps;
    bool m_laps_isSet;
    bool m_laps_isValid;

    double m_laps_led;
    bool m_laps_led_isSet;
    bool m_laps_led_isValid;

    QString m_manufacturer;
    bool m_manufacturer_isSet;
    bool m_manufacturer_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    QString m_number_display;
    bool m_number_display_isSet;
    bool m_number_display_isValid;

    double m_penalty;
    bool m_penalty_isSet;
    bool m_penalty_isValid;

    double m_points;
    bool m_points_isSet;
    bool m_points_isValid;

    double m_pole_final_position;
    bool m_pole_final_position_isSet;
    bool m_pole_final_position_isValid;

    double m_poles;
    bool m_poles_isSet;
    bool m_poles_isValid;

    double m_position_differential;
    bool m_position_differential_isSet;
    bool m_position_differential_isValid;

    double m_qualifying_speed;
    bool m_qualifying_speed_isSet;
    bool m_qualifying_speed_isValid;

    qint32 m_race_id;
    bool m_race_id_isSet;
    bool m_race_id_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    double m_start_position;
    bool m_start_position_isSet;
    bool m_start_position_isValid;

    qint32 m_stat_id;
    bool m_stat_id_isSet;
    bool m_stat_id_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;

    double m_wins;
    bool m_wins_isSet;
    bool m_wins_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDriverRaceProjection)

#endif // OAIDriverRaceProjection_H
