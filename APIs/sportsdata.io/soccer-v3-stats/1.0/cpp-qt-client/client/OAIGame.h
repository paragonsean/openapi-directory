/**
 * Soccer v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGame.h
 *
 * 
 */

#ifndef OAIGame_H
#define OAIGame_H

#include <QJsonObject>

#include "OAIPlayoffAggregateScore.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPlayoffAggregateScore;

class OAIGame : public OAIObject {
public:
    OAIGame();
    OAIGame(QString json);
    ~OAIGame() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAttendance() const;
    void setAttendance(const qint32 &attendance);
    bool is_attendance_Set() const;
    bool is_attendance_Valid() const;

    QString getAwayTeamCountryCode() const;
    void setAwayTeamCountryCode(const QString &away_team_country_code);
    bool is_away_team_country_code_Set() const;
    bool is_away_team_country_code_Valid() const;

    QString getAwayTeamFormation() const;
    void setAwayTeamFormation(const QString &away_team_formation);
    bool is_away_team_formation_Set() const;
    bool is_away_team_formation_Valid() const;

    qint32 getAwayTeamId() const;
    void setAwayTeamId(const qint32 &away_team_id);
    bool is_away_team_id_Set() const;
    bool is_away_team_id_Valid() const;

    QString getAwayTeamKey() const;
    void setAwayTeamKey(const QString &away_team_key);
    bool is_away_team_key_Set() const;
    bool is_away_team_key_Valid() const;

    qint32 getAwayTeamMoneyLine() const;
    void setAwayTeamMoneyLine(const qint32 &away_team_money_line);
    bool is_away_team_money_line_Set() const;
    bool is_away_team_money_line_Valid() const;

    QString getAwayTeamName() const;
    void setAwayTeamName(const QString &away_team_name);
    bool is_away_team_name_Set() const;
    bool is_away_team_name_Valid() const;

    qint32 getAwayTeamPointSpreadPayout() const;
    void setAwayTeamPointSpreadPayout(const qint32 &away_team_point_spread_payout);
    bool is_away_team_point_spread_payout_Set() const;
    bool is_away_team_point_spread_payout_Valid() const;

    qint32 getAwayTeamScore() const;
    void setAwayTeamScore(const qint32 &away_team_score);
    bool is_away_team_score_Set() const;
    bool is_away_team_score_Valid() const;

    qint32 getAwayTeamScoreExtraTime() const;
    void setAwayTeamScoreExtraTime(const qint32 &away_team_score_extra_time);
    bool is_away_team_score_extra_time_Set() const;
    bool is_away_team_score_extra_time_Valid() const;

    qint32 getAwayTeamScorePenalty() const;
    void setAwayTeamScorePenalty(const qint32 &away_team_score_penalty);
    bool is_away_team_score_penalty_Set() const;
    bool is_away_team_score_penalty_Valid() const;

    qint32 getAwayTeamScorePeriod1() const;
    void setAwayTeamScorePeriod1(const qint32 &away_team_score_period1);
    bool is_away_team_score_period1_Set() const;
    bool is_away_team_score_period1_Valid() const;

    qint32 getAwayTeamScorePeriod2() const;
    void setAwayTeamScorePeriod2(const qint32 &away_team_score_period2);
    bool is_away_team_score_period2_Set() const;
    bool is_away_team_score_period2_Valid() const;

    qint32 getClock() const;
    void setClock(const qint32 &clock);
    bool is_clock_Set() const;
    bool is_clock_Valid() const;

    QString getClockDisplay() const;
    void setClockDisplay(const QString &clock_display);
    bool is_clock_display_Set() const;
    bool is_clock_display_Valid() const;

    qint32 getClockExtra() const;
    void setClockExtra(const qint32 &clock_extra);
    bool is_clock_extra_Set() const;
    bool is_clock_extra_Valid() const;

    QString getDateTime() const;
    void setDateTime(const QString &date_time);
    bool is_date_time_Set() const;
    bool is_date_time_Valid() const;

    QString getDay() const;
    void setDay(const QString &day);
    bool is_day_Set() const;
    bool is_day_Valid() const;

    qint32 getDrawMoneyLine() const;
    void setDrawMoneyLine(const qint32 &draw_money_line);
    bool is_draw_money_line_Set() const;
    bool is_draw_money_line_Valid() const;

    qint32 getGameId() const;
    void setGameId(const qint32 &game_id);
    bool is_game_id_Set() const;
    bool is_game_id_Valid() const;

    qint32 getGlobalAwayTeamId() const;
    void setGlobalAwayTeamId(const qint32 &global_away_team_id);
    bool is_global_away_team_id_Set() const;
    bool is_global_away_team_id_Valid() const;

    qint32 getGlobalGameId() const;
    void setGlobalGameId(const qint32 &global_game_id);
    bool is_global_game_id_Set() const;
    bool is_global_game_id_Valid() const;

    qint32 getGlobalHomeTeamId() const;
    void setGlobalHomeTeamId(const qint32 &global_home_team_id);
    bool is_global_home_team_id_Set() const;
    bool is_global_home_team_id_Valid() const;

    QString getGroup() const;
    void setGroup(const QString &group);
    bool is_group_Set() const;
    bool is_group_Valid() const;

    QString getHomeTeamCountryCode() const;
    void setHomeTeamCountryCode(const QString &home_team_country_code);
    bool is_home_team_country_code_Set() const;
    bool is_home_team_country_code_Valid() const;

    QString getHomeTeamFormation() const;
    void setHomeTeamFormation(const QString &home_team_formation);
    bool is_home_team_formation_Set() const;
    bool is_home_team_formation_Valid() const;

    qint32 getHomeTeamId() const;
    void setHomeTeamId(const qint32 &home_team_id);
    bool is_home_team_id_Set() const;
    bool is_home_team_id_Valid() const;

    QString getHomeTeamKey() const;
    void setHomeTeamKey(const QString &home_team_key);
    bool is_home_team_key_Set() const;
    bool is_home_team_key_Valid() const;

    qint32 getHomeTeamMoneyLine() const;
    void setHomeTeamMoneyLine(const qint32 &home_team_money_line);
    bool is_home_team_money_line_Set() const;
    bool is_home_team_money_line_Valid() const;

    QString getHomeTeamName() const;
    void setHomeTeamName(const QString &home_team_name);
    bool is_home_team_name_Set() const;
    bool is_home_team_name_Valid() const;

    qint32 getHomeTeamPointSpreadPayout() const;
    void setHomeTeamPointSpreadPayout(const qint32 &home_team_point_spread_payout);
    bool is_home_team_point_spread_payout_Set() const;
    bool is_home_team_point_spread_payout_Valid() const;

    qint32 getHomeTeamScore() const;
    void setHomeTeamScore(const qint32 &home_team_score);
    bool is_home_team_score_Set() const;
    bool is_home_team_score_Valid() const;

    qint32 getHomeTeamScoreExtraTime() const;
    void setHomeTeamScoreExtraTime(const qint32 &home_team_score_extra_time);
    bool is_home_team_score_extra_time_Set() const;
    bool is_home_team_score_extra_time_Valid() const;

    qint32 getHomeTeamScorePenalty() const;
    void setHomeTeamScorePenalty(const qint32 &home_team_score_penalty);
    bool is_home_team_score_penalty_Set() const;
    bool is_home_team_score_penalty_Valid() const;

    qint32 getHomeTeamScorePeriod1() const;
    void setHomeTeamScorePeriod1(const qint32 &home_team_score_period1);
    bool is_home_team_score_period1_Set() const;
    bool is_home_team_score_period1_Valid() const;

    qint32 getHomeTeamScorePeriod2() const;
    void setHomeTeamScorePeriod2(const qint32 &home_team_score_period2);
    bool is_home_team_score_period2_Set() const;
    bool is_home_team_score_period2_Valid() const;

    bool isIsClosed() const;
    void setIsClosed(const bool &is_closed);
    bool is_is_closed_Set() const;
    bool is_is_closed_Valid() const;

    qint32 getOverPayout() const;
    void setOverPayout(const qint32 &over_payout);
    bool is_over_payout_Set() const;
    bool is_over_payout_Valid() const;

    double getOverUnder() const;
    void setOverUnder(const double &over_under);
    bool is_over_under_Set() const;
    bool is_over_under_Valid() const;

    QString getPeriod() const;
    void setPeriod(const QString &period);
    bool is_period_Set() const;
    bool is_period_Valid() const;

    OAIPlayoffAggregateScore getPlayoffAggregateScore() const;
    void setPlayoffAggregateScore(const OAIPlayoffAggregateScore &playoff_aggregate_score);
    bool is_playoff_aggregate_score_Set() const;
    bool is_playoff_aggregate_score_Valid() const;

    double getPointSpread() const;
    void setPointSpread(const double &point_spread);
    bool is_point_spread_Set() const;
    bool is_point_spread_Valid() const;

    qint32 getRoundId() const;
    void setRoundId(const qint32 &round_id);
    bool is_round_id_Set() const;
    bool is_round_id_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    qint32 getUnderPayout() const;
    void setUnderPayout(const qint32 &under_payout);
    bool is_under_payout_Set() const;
    bool is_under_payout_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    QString getUpdatedUtc() const;
    void setUpdatedUtc(const QString &updated_utc);
    bool is_updated_utc_Set() const;
    bool is_updated_utc_Valid() const;

    qint32 getVenueId() const;
    void setVenueId(const qint32 &venue_id);
    bool is_venue_id_Set() const;
    bool is_venue_id_Valid() const;

    QString getVenueType() const;
    void setVenueType(const QString &venue_type);
    bool is_venue_type_Set() const;
    bool is_venue_type_Valid() const;

    qint32 getWeek() const;
    void setWeek(const qint32 &week);
    bool is_week_Set() const;
    bool is_week_Valid() const;

    QString getWinner() const;
    void setWinner(const QString &winner);
    bool is_winner_Set() const;
    bool is_winner_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_attendance;
    bool m_attendance_isSet;
    bool m_attendance_isValid;

    QString m_away_team_country_code;
    bool m_away_team_country_code_isSet;
    bool m_away_team_country_code_isValid;

    QString m_away_team_formation;
    bool m_away_team_formation_isSet;
    bool m_away_team_formation_isValid;

    qint32 m_away_team_id;
    bool m_away_team_id_isSet;
    bool m_away_team_id_isValid;

    QString m_away_team_key;
    bool m_away_team_key_isSet;
    bool m_away_team_key_isValid;

    qint32 m_away_team_money_line;
    bool m_away_team_money_line_isSet;
    bool m_away_team_money_line_isValid;

    QString m_away_team_name;
    bool m_away_team_name_isSet;
    bool m_away_team_name_isValid;

    qint32 m_away_team_point_spread_payout;
    bool m_away_team_point_spread_payout_isSet;
    bool m_away_team_point_spread_payout_isValid;

    qint32 m_away_team_score;
    bool m_away_team_score_isSet;
    bool m_away_team_score_isValid;

    qint32 m_away_team_score_extra_time;
    bool m_away_team_score_extra_time_isSet;
    bool m_away_team_score_extra_time_isValid;

    qint32 m_away_team_score_penalty;
    bool m_away_team_score_penalty_isSet;
    bool m_away_team_score_penalty_isValid;

    qint32 m_away_team_score_period1;
    bool m_away_team_score_period1_isSet;
    bool m_away_team_score_period1_isValid;

    qint32 m_away_team_score_period2;
    bool m_away_team_score_period2_isSet;
    bool m_away_team_score_period2_isValid;

    qint32 m_clock;
    bool m_clock_isSet;
    bool m_clock_isValid;

    QString m_clock_display;
    bool m_clock_display_isSet;
    bool m_clock_display_isValid;

    qint32 m_clock_extra;
    bool m_clock_extra_isSet;
    bool m_clock_extra_isValid;

    QString m_date_time;
    bool m_date_time_isSet;
    bool m_date_time_isValid;

    QString m_day;
    bool m_day_isSet;
    bool m_day_isValid;

    qint32 m_draw_money_line;
    bool m_draw_money_line_isSet;
    bool m_draw_money_line_isValid;

    qint32 m_game_id;
    bool m_game_id_isSet;
    bool m_game_id_isValid;

    qint32 m_global_away_team_id;
    bool m_global_away_team_id_isSet;
    bool m_global_away_team_id_isValid;

    qint32 m_global_game_id;
    bool m_global_game_id_isSet;
    bool m_global_game_id_isValid;

    qint32 m_global_home_team_id;
    bool m_global_home_team_id_isSet;
    bool m_global_home_team_id_isValid;

    QString m_group;
    bool m_group_isSet;
    bool m_group_isValid;

    QString m_home_team_country_code;
    bool m_home_team_country_code_isSet;
    bool m_home_team_country_code_isValid;

    QString m_home_team_formation;
    bool m_home_team_formation_isSet;
    bool m_home_team_formation_isValid;

    qint32 m_home_team_id;
    bool m_home_team_id_isSet;
    bool m_home_team_id_isValid;

    QString m_home_team_key;
    bool m_home_team_key_isSet;
    bool m_home_team_key_isValid;

    qint32 m_home_team_money_line;
    bool m_home_team_money_line_isSet;
    bool m_home_team_money_line_isValid;

    QString m_home_team_name;
    bool m_home_team_name_isSet;
    bool m_home_team_name_isValid;

    qint32 m_home_team_point_spread_payout;
    bool m_home_team_point_spread_payout_isSet;
    bool m_home_team_point_spread_payout_isValid;

    qint32 m_home_team_score;
    bool m_home_team_score_isSet;
    bool m_home_team_score_isValid;

    qint32 m_home_team_score_extra_time;
    bool m_home_team_score_extra_time_isSet;
    bool m_home_team_score_extra_time_isValid;

    qint32 m_home_team_score_penalty;
    bool m_home_team_score_penalty_isSet;
    bool m_home_team_score_penalty_isValid;

    qint32 m_home_team_score_period1;
    bool m_home_team_score_period1_isSet;
    bool m_home_team_score_period1_isValid;

    qint32 m_home_team_score_period2;
    bool m_home_team_score_period2_isSet;
    bool m_home_team_score_period2_isValid;

    bool m_is_closed;
    bool m_is_closed_isSet;
    bool m_is_closed_isValid;

    qint32 m_over_payout;
    bool m_over_payout_isSet;
    bool m_over_payout_isValid;

    double m_over_under;
    bool m_over_under_isSet;
    bool m_over_under_isValid;

    QString m_period;
    bool m_period_isSet;
    bool m_period_isValid;

    OAIPlayoffAggregateScore m_playoff_aggregate_score;
    bool m_playoff_aggregate_score_isSet;
    bool m_playoff_aggregate_score_isValid;

    double m_point_spread;
    bool m_point_spread_isSet;
    bool m_point_spread_isValid;

    qint32 m_round_id;
    bool m_round_id_isSet;
    bool m_round_id_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    qint32 m_under_payout;
    bool m_under_payout_isSet;
    bool m_under_payout_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;

    QString m_updated_utc;
    bool m_updated_utc_isSet;
    bool m_updated_utc_isValid;

    qint32 m_venue_id;
    bool m_venue_id_isSet;
    bool m_venue_id_isValid;

    QString m_venue_type;
    bool m_venue_type_isSet;
    bool m_venue_type_isValid;

    qint32 m_week;
    bool m_week_isSet;
    bool m_week_isValid;

    QString m_winner;
    bool m_winner_isSet;
    bool m_winner_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGame)

#endif // OAIGame_H
