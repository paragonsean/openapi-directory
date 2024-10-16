/**
 * CBB v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITeamSeason.h
 *
 * 
 */

#ifndef OAITeamSeason_H
#define OAITeamSeason_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITeamSeason : public OAIObject {
public:
    OAITeamSeason();
    OAITeamSeason(QString json);
    ~OAITeamSeason() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAssists() const;
    void setAssists(const qint32 &assists);
    bool is_assists_Set() const;
    bool is_assists_Valid() const;

    double getAssistsPercentage() const;
    void setAssistsPercentage(const double &assists_percentage);
    bool is_assists_percentage_Set() const;
    bool is_assists_percentage_Valid() const;

    qint32 getBlockedShots() const;
    void setBlockedShots(const qint32 &blocked_shots);
    bool is_blocked_shots_Set() const;
    bool is_blocked_shots_Valid() const;

    double getBlocksPercentage() const;
    void setBlocksPercentage(const double &blocks_percentage);
    bool is_blocks_percentage_Set() const;
    bool is_blocks_percentage_Valid() const;

    qint32 getConferenceLosses() const;
    void setConferenceLosses(const qint32 &conference_losses);
    bool is_conference_losses_Set() const;
    bool is_conference_losses_Valid() const;

    qint32 getConferenceWins() const;
    void setConferenceWins(const qint32 &conference_wins);
    bool is_conference_wins_Set() const;
    bool is_conference_wins_Valid() const;

    qint32 getDefensiveRebounds() const;
    void setDefensiveRebounds(const qint32 &defensive_rebounds);
    bool is_defensive_rebounds_Set() const;
    bool is_defensive_rebounds_Valid() const;

    double getDefensiveReboundsPercentage() const;
    void setDefensiveReboundsPercentage(const double &defensive_rebounds_percentage);
    bool is_defensive_rebounds_percentage_Set() const;
    bool is_defensive_rebounds_percentage_Valid() const;

    double getEffectiveFieldGoalsPercentage() const;
    void setEffectiveFieldGoalsPercentage(const double &effective_field_goals_percentage);
    bool is_effective_field_goals_percentage_Set() const;
    bool is_effective_field_goals_percentage_Valid() const;

    double getFantasyPoints() const;
    void setFantasyPoints(const double &fantasy_points);
    bool is_fantasy_points_Set() const;
    bool is_fantasy_points_Valid() const;

    double getFantasyPointsDraftKings() const;
    void setFantasyPointsDraftKings(const double &fantasy_points_draft_kings);
    bool is_fantasy_points_draft_kings_Set() const;
    bool is_fantasy_points_draft_kings_Valid() const;

    double getFantasyPointsFanDuel() const;
    void setFantasyPointsFanDuel(const double &fantasy_points_fan_duel);
    bool is_fantasy_points_fan_duel_Set() const;
    bool is_fantasy_points_fan_duel_Valid() const;

    double getFantasyPointsYahoo() const;
    void setFantasyPointsYahoo(const double &fantasy_points_yahoo);
    bool is_fantasy_points_yahoo_Set() const;
    bool is_fantasy_points_yahoo_Valid() const;

    qint32 getFieldGoalsAttempted() const;
    void setFieldGoalsAttempted(const qint32 &field_goals_attempted);
    bool is_field_goals_attempted_Set() const;
    bool is_field_goals_attempted_Valid() const;

    qint32 getFieldGoalsMade() const;
    void setFieldGoalsMade(const qint32 &field_goals_made);
    bool is_field_goals_made_Set() const;
    bool is_field_goals_made_Valid() const;

    double getFieldGoalsPercentage() const;
    void setFieldGoalsPercentage(const double &field_goals_percentage);
    bool is_field_goals_percentage_Set() const;
    bool is_field_goals_percentage_Valid() const;

    qint32 getFreeThrowsAttempted() const;
    void setFreeThrowsAttempted(const qint32 &free_throws_attempted);
    bool is_free_throws_attempted_Set() const;
    bool is_free_throws_attempted_Valid() const;

    qint32 getFreeThrowsMade() const;
    void setFreeThrowsMade(const qint32 &free_throws_made);
    bool is_free_throws_made_Set() const;
    bool is_free_throws_made_Valid() const;

    double getFreeThrowsPercentage() const;
    void setFreeThrowsPercentage(const double &free_throws_percentage);
    bool is_free_throws_percentage_Set() const;
    bool is_free_throws_percentage_Valid() const;

    qint32 getGames() const;
    void setGames(const qint32 &games);
    bool is_games_Set() const;
    bool is_games_Valid() const;

    qint32 getGlobalTeamId() const;
    void setGlobalTeamId(const qint32 &global_team_id);
    bool is_global_team_id_Set() const;
    bool is_global_team_id_Valid() const;

    qint32 getLosses() const;
    void setLosses(const qint32 &losses);
    bool is_losses_Set() const;
    bool is_losses_Valid() const;

    qint32 getMinutes() const;
    void setMinutes(const qint32 &minutes);
    bool is_minutes_Set() const;
    bool is_minutes_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getOffensiveRebounds() const;
    void setOffensiveRebounds(const qint32 &offensive_rebounds);
    bool is_offensive_rebounds_Set() const;
    bool is_offensive_rebounds_Valid() const;

    double getOffensiveReboundsPercentage() const;
    void setOffensiveReboundsPercentage(const double &offensive_rebounds_percentage);
    bool is_offensive_rebounds_percentage_Set() const;
    bool is_offensive_rebounds_percentage_Valid() const;

    qint32 getPersonalFouls() const;
    void setPersonalFouls(const qint32 &personal_fouls);
    bool is_personal_fouls_Set() const;
    bool is_personal_fouls_Valid() const;

    double getPlayerEfficiencyRating() const;
    void setPlayerEfficiencyRating(const double &player_efficiency_rating);
    bool is_player_efficiency_rating_Set() const;
    bool is_player_efficiency_rating_Valid() const;

    qint32 getPoints() const;
    void setPoints(const qint32 &points);
    bool is_points_Set() const;
    bool is_points_Valid() const;

    double getPossessions() const;
    void setPossessions(const double &possessions);
    bool is_possessions_Set() const;
    bool is_possessions_Valid() const;

    qint32 getRebounds() const;
    void setRebounds(const qint32 &rebounds);
    bool is_rebounds_Set() const;
    bool is_rebounds_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    qint32 getStatId() const;
    void setStatId(const qint32 &stat_id);
    bool is_stat_id_Set() const;
    bool is_stat_id_Valid() const;

    qint32 getSteals() const;
    void setSteals(const qint32 &steals);
    bool is_steals_Set() const;
    bool is_steals_Valid() const;

    double getStealsPercentage() const;
    void setStealsPercentage(const double &steals_percentage);
    bool is_steals_percentage_Set() const;
    bool is_steals_percentage_Valid() const;

    QString getTeam() const;
    void setTeam(const QString &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    qint32 getThreePointersAttempted() const;
    void setThreePointersAttempted(const qint32 &three_pointers_attempted);
    bool is_three_pointers_attempted_Set() const;
    bool is_three_pointers_attempted_Valid() const;

    qint32 getThreePointersMade() const;
    void setThreePointersMade(const qint32 &three_pointers_made);
    bool is_three_pointers_made_Set() const;
    bool is_three_pointers_made_Valid() const;

    double getThreePointersPercentage() const;
    void setThreePointersPercentage(const double &three_pointers_percentage);
    bool is_three_pointers_percentage_Set() const;
    bool is_three_pointers_percentage_Valid() const;

    double getTotalReboundsPercentage() const;
    void setTotalReboundsPercentage(const double &total_rebounds_percentage);
    bool is_total_rebounds_percentage_Set() const;
    bool is_total_rebounds_percentage_Valid() const;

    double getTrueShootingAttempts() const;
    void setTrueShootingAttempts(const double &true_shooting_attempts);
    bool is_true_shooting_attempts_Set() const;
    bool is_true_shooting_attempts_Valid() const;

    double getTrueShootingPercentage() const;
    void setTrueShootingPercentage(const double &true_shooting_percentage);
    bool is_true_shooting_percentage_Set() const;
    bool is_true_shooting_percentage_Valid() const;

    double getTurnOversPercentage() const;
    void setTurnOversPercentage(const double &turn_overs_percentage);
    bool is_turn_overs_percentage_Set() const;
    bool is_turn_overs_percentage_Valid() const;

    qint32 getTurnovers() const;
    void setTurnovers(const qint32 &turnovers);
    bool is_turnovers_Set() const;
    bool is_turnovers_Valid() const;

    qint32 getTwoPointersAttempted() const;
    void setTwoPointersAttempted(const qint32 &two_pointers_attempted);
    bool is_two_pointers_attempted_Set() const;
    bool is_two_pointers_attempted_Valid() const;

    qint32 getTwoPointersMade() const;
    void setTwoPointersMade(const qint32 &two_pointers_made);
    bool is_two_pointers_made_Set() const;
    bool is_two_pointers_made_Valid() const;

    double getTwoPointersPercentage() const;
    void setTwoPointersPercentage(const double &two_pointers_percentage);
    bool is_two_pointers_percentage_Set() const;
    bool is_two_pointers_percentage_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    double getUsageRatePercentage() const;
    void setUsageRatePercentage(const double &usage_rate_percentage);
    bool is_usage_rate_percentage_Set() const;
    bool is_usage_rate_percentage_Valid() const;

    qint32 getWins() const;
    void setWins(const qint32 &wins);
    bool is_wins_Set() const;
    bool is_wins_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_assists;
    bool m_assists_isSet;
    bool m_assists_isValid;

    double m_assists_percentage;
    bool m_assists_percentage_isSet;
    bool m_assists_percentage_isValid;

    qint32 m_blocked_shots;
    bool m_blocked_shots_isSet;
    bool m_blocked_shots_isValid;

    double m_blocks_percentage;
    bool m_blocks_percentage_isSet;
    bool m_blocks_percentage_isValid;

    qint32 m_conference_losses;
    bool m_conference_losses_isSet;
    bool m_conference_losses_isValid;

    qint32 m_conference_wins;
    bool m_conference_wins_isSet;
    bool m_conference_wins_isValid;

    qint32 m_defensive_rebounds;
    bool m_defensive_rebounds_isSet;
    bool m_defensive_rebounds_isValid;

    double m_defensive_rebounds_percentage;
    bool m_defensive_rebounds_percentage_isSet;
    bool m_defensive_rebounds_percentage_isValid;

    double m_effective_field_goals_percentage;
    bool m_effective_field_goals_percentage_isSet;
    bool m_effective_field_goals_percentage_isValid;

    double m_fantasy_points;
    bool m_fantasy_points_isSet;
    bool m_fantasy_points_isValid;

    double m_fantasy_points_draft_kings;
    bool m_fantasy_points_draft_kings_isSet;
    bool m_fantasy_points_draft_kings_isValid;

    double m_fantasy_points_fan_duel;
    bool m_fantasy_points_fan_duel_isSet;
    bool m_fantasy_points_fan_duel_isValid;

    double m_fantasy_points_yahoo;
    bool m_fantasy_points_yahoo_isSet;
    bool m_fantasy_points_yahoo_isValid;

    qint32 m_field_goals_attempted;
    bool m_field_goals_attempted_isSet;
    bool m_field_goals_attempted_isValid;

    qint32 m_field_goals_made;
    bool m_field_goals_made_isSet;
    bool m_field_goals_made_isValid;

    double m_field_goals_percentage;
    bool m_field_goals_percentage_isSet;
    bool m_field_goals_percentage_isValid;

    qint32 m_free_throws_attempted;
    bool m_free_throws_attempted_isSet;
    bool m_free_throws_attempted_isValid;

    qint32 m_free_throws_made;
    bool m_free_throws_made_isSet;
    bool m_free_throws_made_isValid;

    double m_free_throws_percentage;
    bool m_free_throws_percentage_isSet;
    bool m_free_throws_percentage_isValid;

    qint32 m_games;
    bool m_games_isSet;
    bool m_games_isValid;

    qint32 m_global_team_id;
    bool m_global_team_id_isSet;
    bool m_global_team_id_isValid;

    qint32 m_losses;
    bool m_losses_isSet;
    bool m_losses_isValid;

    qint32 m_minutes;
    bool m_minutes_isSet;
    bool m_minutes_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_offensive_rebounds;
    bool m_offensive_rebounds_isSet;
    bool m_offensive_rebounds_isValid;

    double m_offensive_rebounds_percentage;
    bool m_offensive_rebounds_percentage_isSet;
    bool m_offensive_rebounds_percentage_isValid;

    qint32 m_personal_fouls;
    bool m_personal_fouls_isSet;
    bool m_personal_fouls_isValid;

    double m_player_efficiency_rating;
    bool m_player_efficiency_rating_isSet;
    bool m_player_efficiency_rating_isValid;

    qint32 m_points;
    bool m_points_isSet;
    bool m_points_isValid;

    double m_possessions;
    bool m_possessions_isSet;
    bool m_possessions_isValid;

    qint32 m_rebounds;
    bool m_rebounds_isSet;
    bool m_rebounds_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    qint32 m_stat_id;
    bool m_stat_id_isSet;
    bool m_stat_id_isValid;

    qint32 m_steals;
    bool m_steals_isSet;
    bool m_steals_isValid;

    double m_steals_percentage;
    bool m_steals_percentage_isSet;
    bool m_steals_percentage_isValid;

    QString m_team;
    bool m_team_isSet;
    bool m_team_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    qint32 m_three_pointers_attempted;
    bool m_three_pointers_attempted_isSet;
    bool m_three_pointers_attempted_isValid;

    qint32 m_three_pointers_made;
    bool m_three_pointers_made_isSet;
    bool m_three_pointers_made_isValid;

    double m_three_pointers_percentage;
    bool m_three_pointers_percentage_isSet;
    bool m_three_pointers_percentage_isValid;

    double m_total_rebounds_percentage;
    bool m_total_rebounds_percentage_isSet;
    bool m_total_rebounds_percentage_isValid;

    double m_true_shooting_attempts;
    bool m_true_shooting_attempts_isSet;
    bool m_true_shooting_attempts_isValid;

    double m_true_shooting_percentage;
    bool m_true_shooting_percentage_isSet;
    bool m_true_shooting_percentage_isValid;

    double m_turn_overs_percentage;
    bool m_turn_overs_percentage_isSet;
    bool m_turn_overs_percentage_isValid;

    qint32 m_turnovers;
    bool m_turnovers_isSet;
    bool m_turnovers_isValid;

    qint32 m_two_pointers_attempted;
    bool m_two_pointers_attempted_isSet;
    bool m_two_pointers_attempted_isValid;

    qint32 m_two_pointers_made;
    bool m_two_pointers_made_isSet;
    bool m_two_pointers_made_isValid;

    double m_two_pointers_percentage;
    bool m_two_pointers_percentage_isSet;
    bool m_two_pointers_percentage_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;

    double m_usage_rate_percentage;
    bool m_usage_rate_percentage_isSet;
    bool m_usage_rate_percentage_isValid;

    qint32 m_wins;
    bool m_wins_isSet;
    bool m_wins_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITeamSeason)

#endif // OAITeamSeason_H
