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

/*
 * OAIMatch_Score_Breakdown_2017_Alliance.h
 *
 * 
 */

#ifndef OAIMatch_Score_Breakdown_2017_Alliance_H
#define OAIMatch_Score_Breakdown_2017_Alliance_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIMatch_Score_Breakdown_2017_Alliance : public OAIObject {
public:
    OAIMatch_Score_Breakdown_2017_Alliance();
    OAIMatch_Score_Breakdown_2017_Alliance(QString json);
    ~OAIMatch_Score_Breakdown_2017_Alliance() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAdjustPoints() const;
    void setAdjustPoints(const qint32 &adjust_points);
    bool is_adjust_points_Set() const;
    bool is_adjust_points_Valid() const;

    qint32 getAutoFuelHigh() const;
    void setAutoFuelHigh(const qint32 &auto_fuel_high);
    bool is_auto_fuel_high_Set() const;
    bool is_auto_fuel_high_Valid() const;

    qint32 getAutoFuelLow() const;
    void setAutoFuelLow(const qint32 &auto_fuel_low);
    bool is_auto_fuel_low_Set() const;
    bool is_auto_fuel_low_Valid() const;

    qint32 getAutoFuelPoints() const;
    void setAutoFuelPoints(const qint32 &auto_fuel_points);
    bool is_auto_fuel_points_Set() const;
    bool is_auto_fuel_points_Valid() const;

    qint32 getAutoMobilityPoints() const;
    void setAutoMobilityPoints(const qint32 &auto_mobility_points);
    bool is_auto_mobility_points_Set() const;
    bool is_auto_mobility_points_Valid() const;

    qint32 getAutoPoints() const;
    void setAutoPoints(const qint32 &auto_points);
    bool is_auto_points_Set() const;
    bool is_auto_points_Valid() const;

    qint32 getAutoRotorPoints() const;
    void setAutoRotorPoints(const qint32 &auto_rotor_points);
    bool is_auto_rotor_points_Set() const;
    bool is_auto_rotor_points_Valid() const;

    qint32 getFoulCount() const;
    void setFoulCount(const qint32 &foul_count);
    bool is_foul_count_Set() const;
    bool is_foul_count_Valid() const;

    qint32 getFoulPoints() const;
    void setFoulPoints(const qint32 &foul_points);
    bool is_foul_points_Set() const;
    bool is_foul_points_Valid() const;

    qint32 getKPaBonusPoints() const;
    void setKPaBonusPoints(const qint32 &k_pa_bonus_points);
    bool is_k_pa_bonus_points_Set() const;
    bool is_k_pa_bonus_points_Valid() const;

    bool isKPaRankingPointAchieved() const;
    void setKPaRankingPointAchieved(const bool &k_pa_ranking_point_achieved);
    bool is_k_pa_ranking_point_achieved_Set() const;
    bool is_k_pa_ranking_point_achieved_Valid() const;

    QString getRobot1Auto() const;
    void setRobot1Auto(const QString &robot1_auto);
    bool is_robot1_auto_Set() const;
    bool is_robot1_auto_Valid() const;

    QString getRobot2Auto() const;
    void setRobot2Auto(const QString &robot2_auto);
    bool is_robot2_auto_Set() const;
    bool is_robot2_auto_Valid() const;

    QString getRobot3Auto() const;
    void setRobot3Auto(const QString &robot3_auto);
    bool is_robot3_auto_Set() const;
    bool is_robot3_auto_Valid() const;

    bool isRotor1Auto() const;
    void setRotor1Auto(const bool &rotor1_auto);
    bool is_rotor1_auto_Set() const;
    bool is_rotor1_auto_Valid() const;

    bool isRotor1Engaged() const;
    void setRotor1Engaged(const bool &rotor1_engaged);
    bool is_rotor1_engaged_Set() const;
    bool is_rotor1_engaged_Valid() const;

    bool isRotor2Auto() const;
    void setRotor2Auto(const bool &rotor2_auto);
    bool is_rotor2_auto_Set() const;
    bool is_rotor2_auto_Valid() const;

    bool isRotor2Engaged() const;
    void setRotor2Engaged(const bool &rotor2_engaged);
    bool is_rotor2_engaged_Set() const;
    bool is_rotor2_engaged_Valid() const;

    bool isRotor3Engaged() const;
    void setRotor3Engaged(const bool &rotor3_engaged);
    bool is_rotor3_engaged_Set() const;
    bool is_rotor3_engaged_Valid() const;

    bool isRotor4Engaged() const;
    void setRotor4Engaged(const bool &rotor4_engaged);
    bool is_rotor4_engaged_Set() const;
    bool is_rotor4_engaged_Valid() const;

    qint32 getRotorBonusPoints() const;
    void setRotorBonusPoints(const qint32 &rotor_bonus_points);
    bool is_rotor_bonus_points_Set() const;
    bool is_rotor_bonus_points_Valid() const;

    bool isRotorRankingPointAchieved() const;
    void setRotorRankingPointAchieved(const bool &rotor_ranking_point_achieved);
    bool is_rotor_ranking_point_achieved_Set() const;
    bool is_rotor_ranking_point_achieved_Valid() const;

    qint32 getTechFoulCount() const;
    void setTechFoulCount(const qint32 &tech_foul_count);
    bool is_tech_foul_count_Set() const;
    bool is_tech_foul_count_Valid() const;

    qint32 getTeleopFuelHigh() const;
    void setTeleopFuelHigh(const qint32 &teleop_fuel_high);
    bool is_teleop_fuel_high_Set() const;
    bool is_teleop_fuel_high_Valid() const;

    qint32 getTeleopFuelLow() const;
    void setTeleopFuelLow(const qint32 &teleop_fuel_low);
    bool is_teleop_fuel_low_Set() const;
    bool is_teleop_fuel_low_Valid() const;

    qint32 getTeleopFuelPoints() const;
    void setTeleopFuelPoints(const qint32 &teleop_fuel_points);
    bool is_teleop_fuel_points_Set() const;
    bool is_teleop_fuel_points_Valid() const;

    qint32 getTeleopPoints() const;
    void setTeleopPoints(const qint32 &teleop_points);
    bool is_teleop_points_Set() const;
    bool is_teleop_points_Valid() const;

    qint32 getTeleopRotorPoints() const;
    void setTeleopRotorPoints(const qint32 &teleop_rotor_points);
    bool is_teleop_rotor_points_Set() const;
    bool is_teleop_rotor_points_Valid() const;

    qint32 getTeleopTakeoffPoints() const;
    void setTeleopTakeoffPoints(const qint32 &teleop_takeoff_points);
    bool is_teleop_takeoff_points_Set() const;
    bool is_teleop_takeoff_points_Valid() const;

    qint32 getTotalPoints() const;
    void setTotalPoints(const qint32 &total_points);
    bool is_total_points_Set() const;
    bool is_total_points_Valid() const;

    QString getTouchpadFar() const;
    void setTouchpadFar(const QString &touchpad_far);
    bool is_touchpad_far_Set() const;
    bool is_touchpad_far_Valid() const;

    QString getTouchpadMiddle() const;
    void setTouchpadMiddle(const QString &touchpad_middle);
    bool is_touchpad_middle_Set() const;
    bool is_touchpad_middle_Valid() const;

    QString getTouchpadNear() const;
    void setTouchpadNear(const QString &touchpad_near);
    bool is_touchpad_near_Set() const;
    bool is_touchpad_near_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_adjust_points;
    bool m_adjust_points_isSet;
    bool m_adjust_points_isValid;

    qint32 m_auto_fuel_high;
    bool m_auto_fuel_high_isSet;
    bool m_auto_fuel_high_isValid;

    qint32 m_auto_fuel_low;
    bool m_auto_fuel_low_isSet;
    bool m_auto_fuel_low_isValid;

    qint32 m_auto_fuel_points;
    bool m_auto_fuel_points_isSet;
    bool m_auto_fuel_points_isValid;

    qint32 m_auto_mobility_points;
    bool m_auto_mobility_points_isSet;
    bool m_auto_mobility_points_isValid;

    qint32 m_auto_points;
    bool m_auto_points_isSet;
    bool m_auto_points_isValid;

    qint32 m_auto_rotor_points;
    bool m_auto_rotor_points_isSet;
    bool m_auto_rotor_points_isValid;

    qint32 m_foul_count;
    bool m_foul_count_isSet;
    bool m_foul_count_isValid;

    qint32 m_foul_points;
    bool m_foul_points_isSet;
    bool m_foul_points_isValid;

    qint32 m_k_pa_bonus_points;
    bool m_k_pa_bonus_points_isSet;
    bool m_k_pa_bonus_points_isValid;

    bool m_k_pa_ranking_point_achieved;
    bool m_k_pa_ranking_point_achieved_isSet;
    bool m_k_pa_ranking_point_achieved_isValid;

    QString m_robot1_auto;
    bool m_robot1_auto_isSet;
    bool m_robot1_auto_isValid;

    QString m_robot2_auto;
    bool m_robot2_auto_isSet;
    bool m_robot2_auto_isValid;

    QString m_robot3_auto;
    bool m_robot3_auto_isSet;
    bool m_robot3_auto_isValid;

    bool m_rotor1_auto;
    bool m_rotor1_auto_isSet;
    bool m_rotor1_auto_isValid;

    bool m_rotor1_engaged;
    bool m_rotor1_engaged_isSet;
    bool m_rotor1_engaged_isValid;

    bool m_rotor2_auto;
    bool m_rotor2_auto_isSet;
    bool m_rotor2_auto_isValid;

    bool m_rotor2_engaged;
    bool m_rotor2_engaged_isSet;
    bool m_rotor2_engaged_isValid;

    bool m_rotor3_engaged;
    bool m_rotor3_engaged_isSet;
    bool m_rotor3_engaged_isValid;

    bool m_rotor4_engaged;
    bool m_rotor4_engaged_isSet;
    bool m_rotor4_engaged_isValid;

    qint32 m_rotor_bonus_points;
    bool m_rotor_bonus_points_isSet;
    bool m_rotor_bonus_points_isValid;

    bool m_rotor_ranking_point_achieved;
    bool m_rotor_ranking_point_achieved_isSet;
    bool m_rotor_ranking_point_achieved_isValid;

    qint32 m_tech_foul_count;
    bool m_tech_foul_count_isSet;
    bool m_tech_foul_count_isValid;

    qint32 m_teleop_fuel_high;
    bool m_teleop_fuel_high_isSet;
    bool m_teleop_fuel_high_isValid;

    qint32 m_teleop_fuel_low;
    bool m_teleop_fuel_low_isSet;
    bool m_teleop_fuel_low_isValid;

    qint32 m_teleop_fuel_points;
    bool m_teleop_fuel_points_isSet;
    bool m_teleop_fuel_points_isValid;

    qint32 m_teleop_points;
    bool m_teleop_points_isSet;
    bool m_teleop_points_isValid;

    qint32 m_teleop_rotor_points;
    bool m_teleop_rotor_points_isSet;
    bool m_teleop_rotor_points_isValid;

    qint32 m_teleop_takeoff_points;
    bool m_teleop_takeoff_points_isSet;
    bool m_teleop_takeoff_points_isValid;

    qint32 m_total_points;
    bool m_total_points_isSet;
    bool m_total_points_isValid;

    QString m_touchpad_far;
    bool m_touchpad_far_isSet;
    bool m_touchpad_far_isValid;

    QString m_touchpad_middle;
    bool m_touchpad_middle_isSet;
    bool m_touchpad_middle_isValid;

    QString m_touchpad_near;
    bool m_touchpad_near_isSet;
    bool m_touchpad_near_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMatch_Score_Breakdown_2017_Alliance)

#endif // OAIMatch_Score_Breakdown_2017_Alliance_H
