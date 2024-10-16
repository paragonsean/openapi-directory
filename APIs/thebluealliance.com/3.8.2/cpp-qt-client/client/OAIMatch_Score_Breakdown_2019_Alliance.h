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
 * OAIMatch_Score_Breakdown_2019_Alliance.h
 *
 * 
 */

#ifndef OAIMatch_Score_Breakdown_2019_Alliance_H
#define OAIMatch_Score_Breakdown_2019_Alliance_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIMatch_Score_Breakdown_2019_Alliance : public OAIObject {
public:
    OAIMatch_Score_Breakdown_2019_Alliance();
    OAIMatch_Score_Breakdown_2019_Alliance(QString json);
    ~OAIMatch_Score_Breakdown_2019_Alliance() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAdjustPoints() const;
    void setAdjustPoints(const qint32 &adjust_points);
    bool is_adjust_points_Set() const;
    bool is_adjust_points_Valid() const;

    qint32 getAutoPoints() const;
    void setAutoPoints(const qint32 &auto_points);
    bool is_auto_points_Set() const;
    bool is_auto_points_Valid() const;

    QString getBay1() const;
    void setBay1(const QString &bay1);
    bool is_bay1_Set() const;
    bool is_bay1_Valid() const;

    QString getBay2() const;
    void setBay2(const QString &bay2);
    bool is_bay2_Set() const;
    bool is_bay2_Valid() const;

    QString getBay3() const;
    void setBay3(const QString &bay3);
    bool is_bay3_Set() const;
    bool is_bay3_Valid() const;

    QString getBay4() const;
    void setBay4(const QString &bay4);
    bool is_bay4_Set() const;
    bool is_bay4_Valid() const;

    QString getBay5() const;
    void setBay5(const QString &bay5);
    bool is_bay5_Set() const;
    bool is_bay5_Valid() const;

    QString getBay6() const;
    void setBay6(const QString &bay6);
    bool is_bay6_Set() const;
    bool is_bay6_Valid() const;

    QString getBay7() const;
    void setBay7(const QString &bay7);
    bool is_bay7_Set() const;
    bool is_bay7_Valid() const;

    QString getBay8() const;
    void setBay8(const QString &bay8);
    bool is_bay8_Set() const;
    bool is_bay8_Valid() const;

    qint32 getCargoPoints() const;
    void setCargoPoints(const qint32 &cargo_points);
    bool is_cargo_points_Set() const;
    bool is_cargo_points_Valid() const;

    bool isCompleteRocketRankingPoint() const;
    void setCompleteRocketRankingPoint(const bool &complete_rocket_ranking_point);
    bool is_complete_rocket_ranking_point_Set() const;
    bool is_complete_rocket_ranking_point_Valid() const;

    bool isCompletedRocketFar() const;
    void setCompletedRocketFar(const bool &completed_rocket_far);
    bool is_completed_rocket_far_Set() const;
    bool is_completed_rocket_far_Valid() const;

    bool isCompletedRocketNear() const;
    void setCompletedRocketNear(const bool &completed_rocket_near);
    bool is_completed_rocket_near_Set() const;
    bool is_completed_rocket_near_Valid() const;

    QString getEndgameRobot1() const;
    void setEndgameRobot1(const QString &endgame_robot1);
    bool is_endgame_robot1_Set() const;
    bool is_endgame_robot1_Valid() const;

    QString getEndgameRobot2() const;
    void setEndgameRobot2(const QString &endgame_robot2);
    bool is_endgame_robot2_Set() const;
    bool is_endgame_robot2_Valid() const;

    QString getEndgameRobot3() const;
    void setEndgameRobot3(const QString &endgame_robot3);
    bool is_endgame_robot3_Set() const;
    bool is_endgame_robot3_Valid() const;

    qint32 getFoulCount() const;
    void setFoulCount(const qint32 &foul_count);
    bool is_foul_count_Set() const;
    bool is_foul_count_Valid() const;

    qint32 getFoulPoints() const;
    void setFoulPoints(const qint32 &foul_points);
    bool is_foul_points_Set() const;
    bool is_foul_points_Valid() const;

    qint32 getHabClimbPoints() const;
    void setHabClimbPoints(const qint32 &hab_climb_points);
    bool is_hab_climb_points_Set() const;
    bool is_hab_climb_points_Valid() const;

    bool isHabDockingRankingPoint() const;
    void setHabDockingRankingPoint(const bool &hab_docking_ranking_point);
    bool is_hab_docking_ranking_point_Set() const;
    bool is_hab_docking_ranking_point_Valid() const;

    QString getHabLineRobot1() const;
    void setHabLineRobot1(const QString &hab_line_robot1);
    bool is_hab_line_robot1_Set() const;
    bool is_hab_line_robot1_Valid() const;

    QString getHabLineRobot2() const;
    void setHabLineRobot2(const QString &hab_line_robot2);
    bool is_hab_line_robot2_Set() const;
    bool is_hab_line_robot2_Valid() const;

    QString getHabLineRobot3() const;
    void setHabLineRobot3(const QString &hab_line_robot3);
    bool is_hab_line_robot3_Set() const;
    bool is_hab_line_robot3_Valid() const;

    qint32 getHatchPanelPoints() const;
    void setHatchPanelPoints(const qint32 &hatch_panel_points);
    bool is_hatch_panel_points_Set() const;
    bool is_hatch_panel_points_Valid() const;

    QString getLowLeftRocketFar() const;
    void setLowLeftRocketFar(const QString &low_left_rocket_far);
    bool is_low_left_rocket_far_Set() const;
    bool is_low_left_rocket_far_Valid() const;

    QString getLowLeftRocketNear() const;
    void setLowLeftRocketNear(const QString &low_left_rocket_near);
    bool is_low_left_rocket_near_Set() const;
    bool is_low_left_rocket_near_Valid() const;

    QString getLowRightRocketFar() const;
    void setLowRightRocketFar(const QString &low_right_rocket_far);
    bool is_low_right_rocket_far_Set() const;
    bool is_low_right_rocket_far_Valid() const;

    QString getLowRightRocketNear() const;
    void setLowRightRocketNear(const QString &low_right_rocket_near);
    bool is_low_right_rocket_near_Set() const;
    bool is_low_right_rocket_near_Valid() const;

    QString getMidLeftRocketFar() const;
    void setMidLeftRocketFar(const QString &mid_left_rocket_far);
    bool is_mid_left_rocket_far_Set() const;
    bool is_mid_left_rocket_far_Valid() const;

    QString getMidLeftRocketNear() const;
    void setMidLeftRocketNear(const QString &mid_left_rocket_near);
    bool is_mid_left_rocket_near_Set() const;
    bool is_mid_left_rocket_near_Valid() const;

    QString getMidRightRocketFar() const;
    void setMidRightRocketFar(const QString &mid_right_rocket_far);
    bool is_mid_right_rocket_far_Set() const;
    bool is_mid_right_rocket_far_Valid() const;

    QString getMidRightRocketNear() const;
    void setMidRightRocketNear(const QString &mid_right_rocket_near);
    bool is_mid_right_rocket_near_Set() const;
    bool is_mid_right_rocket_near_Valid() const;

    QString getPreMatchBay1() const;
    void setPreMatchBay1(const QString &pre_match_bay1);
    bool is_pre_match_bay1_Set() const;
    bool is_pre_match_bay1_Valid() const;

    QString getPreMatchBay2() const;
    void setPreMatchBay2(const QString &pre_match_bay2);
    bool is_pre_match_bay2_Set() const;
    bool is_pre_match_bay2_Valid() const;

    QString getPreMatchBay3() const;
    void setPreMatchBay3(const QString &pre_match_bay3);
    bool is_pre_match_bay3_Set() const;
    bool is_pre_match_bay3_Valid() const;

    QString getPreMatchBay6() const;
    void setPreMatchBay6(const QString &pre_match_bay6);
    bool is_pre_match_bay6_Set() const;
    bool is_pre_match_bay6_Valid() const;

    QString getPreMatchBay7() const;
    void setPreMatchBay7(const QString &pre_match_bay7);
    bool is_pre_match_bay7_Set() const;
    bool is_pre_match_bay7_Valid() const;

    QString getPreMatchBay8() const;
    void setPreMatchBay8(const QString &pre_match_bay8);
    bool is_pre_match_bay8_Set() const;
    bool is_pre_match_bay8_Valid() const;

    QString getPreMatchLevelRobot1() const;
    void setPreMatchLevelRobot1(const QString &pre_match_level_robot1);
    bool is_pre_match_level_robot1_Set() const;
    bool is_pre_match_level_robot1_Valid() const;

    QString getPreMatchLevelRobot2() const;
    void setPreMatchLevelRobot2(const QString &pre_match_level_robot2);
    bool is_pre_match_level_robot2_Set() const;
    bool is_pre_match_level_robot2_Valid() const;

    QString getPreMatchLevelRobot3() const;
    void setPreMatchLevelRobot3(const QString &pre_match_level_robot3);
    bool is_pre_match_level_robot3_Set() const;
    bool is_pre_match_level_robot3_Valid() const;

    qint32 getRp() const;
    void setRp(const qint32 &rp);
    bool is_rp_Set() const;
    bool is_rp_Valid() const;

    qint32 getSandStormBonusPoints() const;
    void setSandStormBonusPoints(const qint32 &sand_storm_bonus_points);
    bool is_sand_storm_bonus_points_Set() const;
    bool is_sand_storm_bonus_points_Valid() const;

    qint32 getTechFoulCount() const;
    void setTechFoulCount(const qint32 &tech_foul_count);
    bool is_tech_foul_count_Set() const;
    bool is_tech_foul_count_Valid() const;

    qint32 getTeleopPoints() const;
    void setTeleopPoints(const qint32 &teleop_points);
    bool is_teleop_points_Set() const;
    bool is_teleop_points_Valid() const;

    QString getTopLeftRocketFar() const;
    void setTopLeftRocketFar(const QString &top_left_rocket_far);
    bool is_top_left_rocket_far_Set() const;
    bool is_top_left_rocket_far_Valid() const;

    QString getTopLeftRocketNear() const;
    void setTopLeftRocketNear(const QString &top_left_rocket_near);
    bool is_top_left_rocket_near_Set() const;
    bool is_top_left_rocket_near_Valid() const;

    QString getTopRightRocketFar() const;
    void setTopRightRocketFar(const QString &top_right_rocket_far);
    bool is_top_right_rocket_far_Set() const;
    bool is_top_right_rocket_far_Valid() const;

    QString getTopRightRocketNear() const;
    void setTopRightRocketNear(const QString &top_right_rocket_near);
    bool is_top_right_rocket_near_Set() const;
    bool is_top_right_rocket_near_Valid() const;

    qint32 getTotalPoints() const;
    void setTotalPoints(const qint32 &total_points);
    bool is_total_points_Set() const;
    bool is_total_points_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_adjust_points;
    bool m_adjust_points_isSet;
    bool m_adjust_points_isValid;

    qint32 m_auto_points;
    bool m_auto_points_isSet;
    bool m_auto_points_isValid;

    QString m_bay1;
    bool m_bay1_isSet;
    bool m_bay1_isValid;

    QString m_bay2;
    bool m_bay2_isSet;
    bool m_bay2_isValid;

    QString m_bay3;
    bool m_bay3_isSet;
    bool m_bay3_isValid;

    QString m_bay4;
    bool m_bay4_isSet;
    bool m_bay4_isValid;

    QString m_bay5;
    bool m_bay5_isSet;
    bool m_bay5_isValid;

    QString m_bay6;
    bool m_bay6_isSet;
    bool m_bay6_isValid;

    QString m_bay7;
    bool m_bay7_isSet;
    bool m_bay7_isValid;

    QString m_bay8;
    bool m_bay8_isSet;
    bool m_bay8_isValid;

    qint32 m_cargo_points;
    bool m_cargo_points_isSet;
    bool m_cargo_points_isValid;

    bool m_complete_rocket_ranking_point;
    bool m_complete_rocket_ranking_point_isSet;
    bool m_complete_rocket_ranking_point_isValid;

    bool m_completed_rocket_far;
    bool m_completed_rocket_far_isSet;
    bool m_completed_rocket_far_isValid;

    bool m_completed_rocket_near;
    bool m_completed_rocket_near_isSet;
    bool m_completed_rocket_near_isValid;

    QString m_endgame_robot1;
    bool m_endgame_robot1_isSet;
    bool m_endgame_robot1_isValid;

    QString m_endgame_robot2;
    bool m_endgame_robot2_isSet;
    bool m_endgame_robot2_isValid;

    QString m_endgame_robot3;
    bool m_endgame_robot3_isSet;
    bool m_endgame_robot3_isValid;

    qint32 m_foul_count;
    bool m_foul_count_isSet;
    bool m_foul_count_isValid;

    qint32 m_foul_points;
    bool m_foul_points_isSet;
    bool m_foul_points_isValid;

    qint32 m_hab_climb_points;
    bool m_hab_climb_points_isSet;
    bool m_hab_climb_points_isValid;

    bool m_hab_docking_ranking_point;
    bool m_hab_docking_ranking_point_isSet;
    bool m_hab_docking_ranking_point_isValid;

    QString m_hab_line_robot1;
    bool m_hab_line_robot1_isSet;
    bool m_hab_line_robot1_isValid;

    QString m_hab_line_robot2;
    bool m_hab_line_robot2_isSet;
    bool m_hab_line_robot2_isValid;

    QString m_hab_line_robot3;
    bool m_hab_line_robot3_isSet;
    bool m_hab_line_robot3_isValid;

    qint32 m_hatch_panel_points;
    bool m_hatch_panel_points_isSet;
    bool m_hatch_panel_points_isValid;

    QString m_low_left_rocket_far;
    bool m_low_left_rocket_far_isSet;
    bool m_low_left_rocket_far_isValid;

    QString m_low_left_rocket_near;
    bool m_low_left_rocket_near_isSet;
    bool m_low_left_rocket_near_isValid;

    QString m_low_right_rocket_far;
    bool m_low_right_rocket_far_isSet;
    bool m_low_right_rocket_far_isValid;

    QString m_low_right_rocket_near;
    bool m_low_right_rocket_near_isSet;
    bool m_low_right_rocket_near_isValid;

    QString m_mid_left_rocket_far;
    bool m_mid_left_rocket_far_isSet;
    bool m_mid_left_rocket_far_isValid;

    QString m_mid_left_rocket_near;
    bool m_mid_left_rocket_near_isSet;
    bool m_mid_left_rocket_near_isValid;

    QString m_mid_right_rocket_far;
    bool m_mid_right_rocket_far_isSet;
    bool m_mid_right_rocket_far_isValid;

    QString m_mid_right_rocket_near;
    bool m_mid_right_rocket_near_isSet;
    bool m_mid_right_rocket_near_isValid;

    QString m_pre_match_bay1;
    bool m_pre_match_bay1_isSet;
    bool m_pre_match_bay1_isValid;

    QString m_pre_match_bay2;
    bool m_pre_match_bay2_isSet;
    bool m_pre_match_bay2_isValid;

    QString m_pre_match_bay3;
    bool m_pre_match_bay3_isSet;
    bool m_pre_match_bay3_isValid;

    QString m_pre_match_bay6;
    bool m_pre_match_bay6_isSet;
    bool m_pre_match_bay6_isValid;

    QString m_pre_match_bay7;
    bool m_pre_match_bay7_isSet;
    bool m_pre_match_bay7_isValid;

    QString m_pre_match_bay8;
    bool m_pre_match_bay8_isSet;
    bool m_pre_match_bay8_isValid;

    QString m_pre_match_level_robot1;
    bool m_pre_match_level_robot1_isSet;
    bool m_pre_match_level_robot1_isValid;

    QString m_pre_match_level_robot2;
    bool m_pre_match_level_robot2_isSet;
    bool m_pre_match_level_robot2_isValid;

    QString m_pre_match_level_robot3;
    bool m_pre_match_level_robot3_isSet;
    bool m_pre_match_level_robot3_isValid;

    qint32 m_rp;
    bool m_rp_isSet;
    bool m_rp_isValid;

    qint32 m_sand_storm_bonus_points;
    bool m_sand_storm_bonus_points_isSet;
    bool m_sand_storm_bonus_points_isValid;

    qint32 m_tech_foul_count;
    bool m_tech_foul_count_isSet;
    bool m_tech_foul_count_isValid;

    qint32 m_teleop_points;
    bool m_teleop_points_isSet;
    bool m_teleop_points_isValid;

    QString m_top_left_rocket_far;
    bool m_top_left_rocket_far_isSet;
    bool m_top_left_rocket_far_isValid;

    QString m_top_left_rocket_near;
    bool m_top_left_rocket_near_isSet;
    bool m_top_left_rocket_near_isValid;

    QString m_top_right_rocket_far;
    bool m_top_right_rocket_far_isSet;
    bool m_top_right_rocket_far_isValid;

    QString m_top_right_rocket_near;
    bool m_top_right_rocket_near_isSet;
    bool m_top_right_rocket_near_isValid;

    qint32 m_total_points;
    bool m_total_points_isSet;
    bool m_total_points_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMatch_Score_Breakdown_2019_Alliance)

#endif // OAIMatch_Score_Breakdown_2019_Alliance_H
