/**
 * MLB v3 Projections
 * MLB projections API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPlayerSeasonProjection.h
 *
 * 
 */

#ifndef OAIPlayerSeasonProjection_H
#define OAIPlayerSeasonProjection_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPlayerSeasonProjection : public OAIObject {
public:
    OAIPlayerSeasonProjection();
    OAIPlayerSeasonProjection(QString json);
    ~OAIPlayerSeasonProjection() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAtBats() const;
    void setAtBats(const double &at_bats);
    bool is_at_bats_Set() const;
    bool is_at_bats_Valid() const;

    qint32 getAuctionValue() const;
    void setAuctionValue(const qint32 &auction_value);
    bool is_auction_value_Set() const;
    bool is_auction_value_Valid() const;

    double getAverageDraftPosition() const;
    void setAverageDraftPosition(const double &average_draft_position);
    bool is_average_draft_position_Set() const;
    bool is_average_draft_position_Valid() const;

    double getBallsInPlay() const;
    void setBallsInPlay(const double &balls_in_play);
    bool is_balls_in_play_Set() const;
    bool is_balls_in_play_Valid() const;

    double getBattingAverage() const;
    void setBattingAverage(const double &batting_average);
    bool is_batting_average_Set() const;
    bool is_batting_average_Valid() const;

    double getBattingAverageOnBallsInPlay() const;
    void setBattingAverageOnBallsInPlay(const double &batting_average_on_balls_in_play);
    bool is_batting_average_on_balls_in_play_Set() const;
    bool is_batting_average_on_balls_in_play_Valid() const;

    qint32 getBattingOrder() const;
    void setBattingOrder(const qint32 &batting_order);
    bool is_batting_order_Set() const;
    bool is_batting_order_Valid() const;

    bool isBattingOrderConfirmed() const;
    void setBattingOrderConfirmed(const bool &batting_order_confirmed);
    bool is_batting_order_confirmed_Set() const;
    bool is_batting_order_confirmed_Valid() const;

    double getCaughtStealing() const;
    void setCaughtStealing(const double &caught_stealing);
    bool is_caught_stealing_Set() const;
    bool is_caught_stealing_Valid() const;

    double getDoublePlays() const;
    void setDoublePlays(const double &double_plays);
    bool is_double_plays_Set() const;
    bool is_double_plays_Valid() const;

    double getDoubles() const;
    void setDoubles(const double &doubles);
    bool is_doubles_Set() const;
    bool is_doubles_Valid() const;

    double getEarnedRunAverage() const;
    void setEarnedRunAverage(const double &earned_run_average);
    bool is_earned_run_average_Set() const;
    bool is_earned_run_average_Valid() const;

    double getErrors() const;
    void setErrors(const double &errors);
    bool is_errors_Set() const;
    bool is_errors_Valid() const;

    double getFantasyPoints() const;
    void setFantasyPoints(const double &fantasy_points);
    bool is_fantasy_points_Set() const;
    bool is_fantasy_points_Valid() const;

    double getFantasyPointsBatting() const;
    void setFantasyPointsBatting(const double &fantasy_points_batting);
    bool is_fantasy_points_batting_Set() const;
    bool is_fantasy_points_batting_Valid() const;

    double getFantasyPointsDraftKings() const;
    void setFantasyPointsDraftKings(const double &fantasy_points_draft_kings);
    bool is_fantasy_points_draft_kings_Set() const;
    bool is_fantasy_points_draft_kings_Valid() const;

    double getFantasyPointsFanDuel() const;
    void setFantasyPointsFanDuel(const double &fantasy_points_fan_duel);
    bool is_fantasy_points_fan_duel_Set() const;
    bool is_fantasy_points_fan_duel_Valid() const;

    double getFantasyPointsFantasyDraft() const;
    void setFantasyPointsFantasyDraft(const double &fantasy_points_fantasy_draft);
    bool is_fantasy_points_fantasy_draft_Set() const;
    bool is_fantasy_points_fantasy_draft_Valid() const;

    double getFantasyPointsPitching() const;
    void setFantasyPointsPitching(const double &fantasy_points_pitching);
    bool is_fantasy_points_pitching_Set() const;
    bool is_fantasy_points_pitching_Valid() const;

    double getFantasyPointsYahoo() const;
    void setFantasyPointsYahoo(const double &fantasy_points_yahoo);
    bool is_fantasy_points_yahoo_Set() const;
    bool is_fantasy_points_yahoo_Valid() const;

    double getFieldingIndependentPitching() const;
    void setFieldingIndependentPitching(const double &fielding_independent_pitching);
    bool is_fielding_independent_pitching_Set() const;
    bool is_fielding_independent_pitching_Valid() const;

    double getFlyOuts() const;
    void setFlyOuts(const double &fly_outs);
    bool is_fly_outs_Set() const;
    bool is_fly_outs_Valid() const;

    qint32 getGames() const;
    void setGames(const qint32 &games);
    bool is_games_Set() const;
    bool is_games_Valid() const;

    qint32 getGlobalTeamId() const;
    void setGlobalTeamId(const qint32 &global_team_id);
    bool is_global_team_id_Set() const;
    bool is_global_team_id_Valid() const;

    double getGrandSlams() const;
    void setGrandSlams(const double &grand_slams);
    bool is_grand_slams_Set() const;
    bool is_grand_slams_Valid() const;

    double getGroundIntoDoublePlay() const;
    void setGroundIntoDoublePlay(const double &ground_into_double_play);
    bool is_ground_into_double_play_Set() const;
    bool is_ground_into_double_play_Valid() const;

    double getGroundOuts() const;
    void setGroundOuts(const double &ground_outs);
    bool is_ground_outs_Set() const;
    bool is_ground_outs_Valid() const;

    double getHitByPitch() const;
    void setHitByPitch(const double &hit_by_pitch);
    bool is_hit_by_pitch_Set() const;
    bool is_hit_by_pitch_Valid() const;

    double getHits() const;
    void setHits(const double &hits);
    bool is_hits_Set() const;
    bool is_hits_Valid() const;

    double getHomeRuns() const;
    void setHomeRuns(const double &home_runs);
    bool is_home_runs_Set() const;
    bool is_home_runs_Valid() const;

    double getInningsPitchedDecimal() const;
    void setInningsPitchedDecimal(const double &innings_pitched_decimal);
    bool is_innings_pitched_decimal_Set() const;
    bool is_innings_pitched_decimal_Valid() const;

    double getInningsPitchedFull() const;
    void setInningsPitchedFull(const double &innings_pitched_full);
    bool is_innings_pitched_full_Set() const;
    bool is_innings_pitched_full_Valid() const;

    double getInningsPitchedOuts() const;
    void setInningsPitchedOuts(const double &innings_pitched_outs);
    bool is_innings_pitched_outs_Set() const;
    bool is_innings_pitched_outs_Valid() const;

    double getIntentionalWalks() const;
    void setIntentionalWalks(const double &intentional_walks);
    bool is_intentional_walks_Set() const;
    bool is_intentional_walks_Valid() const;

    double getIsolatedPower() const;
    void setIsolatedPower(const double &isolated_power);
    bool is_isolated_power_Set() const;
    bool is_isolated_power_Valid() const;

    double getLeftOnBase() const;
    void setLeftOnBase(const double &left_on_base);
    bool is_left_on_base_Set() const;
    bool is_left_on_base_Valid() const;

    double getLineOuts() const;
    void setLineOuts(const double &line_outs);
    bool is_line_outs_Set() const;
    bool is_line_outs_Valid() const;

    double getLosses() const;
    void setLosses(const double &losses);
    bool is_losses_Set() const;
    bool is_losses_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    double getOnBasePercentage() const;
    void setOnBasePercentage(const double &on_base_percentage);
    bool is_on_base_percentage_Set() const;
    bool is_on_base_percentage_Valid() const;

    double getOnBasePlusSlugging() const;
    void setOnBasePlusSlugging(const double &on_base_plus_slugging);
    bool is_on_base_plus_slugging_Set() const;
    bool is_on_base_plus_slugging_Valid() const;

    double getOuts() const;
    void setOuts(const double &outs);
    bool is_outs_Set() const;
    bool is_outs_Valid() const;

    double getPitchesSeen() const;
    void setPitchesSeen(const double &pitches_seen);
    bool is_pitches_seen_Set() const;
    bool is_pitches_seen_Valid() const;

    double getPitchesThrown() const;
    void setPitchesThrown(const double &pitches_thrown);
    bool is_pitches_thrown_Set() const;
    bool is_pitches_thrown_Valid() const;

    double getPitchesThrownStrikes() const;
    void setPitchesThrownStrikes(const double &pitches_thrown_strikes);
    bool is_pitches_thrown_strikes_Set() const;
    bool is_pitches_thrown_strikes_Valid() const;

    double getPitchingBallsInPlay() const;
    void setPitchingBallsInPlay(const double &pitching_balls_in_play);
    bool is_pitching_balls_in_play_Set() const;
    bool is_pitching_balls_in_play_Valid() const;

    double getPitchingBattingAverageAgainst() const;
    void setPitchingBattingAverageAgainst(const double &pitching_batting_average_against);
    bool is_pitching_batting_average_against_Set() const;
    bool is_pitching_batting_average_against_Valid() const;

    double getPitchingBattingAverageOnBallsInPlay() const;
    void setPitchingBattingAverageOnBallsInPlay(const double &pitching_batting_average_on_balls_in_play);
    bool is_pitching_batting_average_on_balls_in_play_Set() const;
    bool is_pitching_batting_average_on_balls_in_play_Valid() const;

    double getPitchingBlownSaves() const;
    void setPitchingBlownSaves(const double &pitching_blown_saves);
    bool is_pitching_blown_saves_Set() const;
    bool is_pitching_blown_saves_Valid() const;

    double getPitchingCatchersInterference() const;
    void setPitchingCatchersInterference(const double &pitching_catchers_interference);
    bool is_pitching_catchers_interference_Set() const;
    bool is_pitching_catchers_interference_Valid() const;

    double getPitchingCompleteGames() const;
    void setPitchingCompleteGames(const double &pitching_complete_games);
    bool is_pitching_complete_games_Set() const;
    bool is_pitching_complete_games_Valid() const;

    double getPitchingDoublePlays() const;
    void setPitchingDoublePlays(const double &pitching_double_plays);
    bool is_pitching_double_plays_Set() const;
    bool is_pitching_double_plays_Valid() const;

    double getPitchingDoubles() const;
    void setPitchingDoubles(const double &pitching_doubles);
    bool is_pitching_doubles_Set() const;
    bool is_pitching_doubles_Valid() const;

    double getPitchingEarnedRuns() const;
    void setPitchingEarnedRuns(const double &pitching_earned_runs);
    bool is_pitching_earned_runs_Set() const;
    bool is_pitching_earned_runs_Valid() const;

    double getPitchingFlyOuts() const;
    void setPitchingFlyOuts(const double &pitching_fly_outs);
    bool is_pitching_fly_outs_Set() const;
    bool is_pitching_fly_outs_Valid() const;

    double getPitchingGrandSlams() const;
    void setPitchingGrandSlams(const double &pitching_grand_slams);
    bool is_pitching_grand_slams_Set() const;
    bool is_pitching_grand_slams_Valid() const;

    double getPitchingGroundIntoDoublePlay() const;
    void setPitchingGroundIntoDoublePlay(const double &pitching_ground_into_double_play);
    bool is_pitching_ground_into_double_play_Set() const;
    bool is_pitching_ground_into_double_play_Valid() const;

    double getPitchingGroundOuts() const;
    void setPitchingGroundOuts(const double &pitching_ground_outs);
    bool is_pitching_ground_outs_Set() const;
    bool is_pitching_ground_outs_Valid() const;

    double getPitchingHitByPitch() const;
    void setPitchingHitByPitch(const double &pitching_hit_by_pitch);
    bool is_pitching_hit_by_pitch_Set() const;
    bool is_pitching_hit_by_pitch_Valid() const;

    double getPitchingHits() const;
    void setPitchingHits(const double &pitching_hits);
    bool is_pitching_hits_Set() const;
    bool is_pitching_hits_Valid() const;

    double getPitchingHolds() const;
    void setPitchingHolds(const double &pitching_holds);
    bool is_pitching_holds_Set() const;
    bool is_pitching_holds_Valid() const;

    double getPitchingHomeRuns() const;
    void setPitchingHomeRuns(const double &pitching_home_runs);
    bool is_pitching_home_runs_Set() const;
    bool is_pitching_home_runs_Valid() const;

    qint32 getPitchingInningStarted() const;
    void setPitchingInningStarted(const qint32 &pitching_inning_started);
    bool is_pitching_inning_started_Set() const;
    bool is_pitching_inning_started_Valid() const;

    double getPitchingIntentionalWalks() const;
    void setPitchingIntentionalWalks(const double &pitching_intentional_walks);
    bool is_pitching_intentional_walks_Set() const;
    bool is_pitching_intentional_walks_Valid() const;

    double getPitchingLineOuts() const;
    void setPitchingLineOuts(const double &pitching_line_outs);
    bool is_pitching_line_outs_Set() const;
    bool is_pitching_line_outs_Valid() const;

    double getPitchingNoHitters() const;
    void setPitchingNoHitters(const double &pitching_no_hitters);
    bool is_pitching_no_hitters_Set() const;
    bool is_pitching_no_hitters_Valid() const;

    double getPitchingOnBasePercentage() const;
    void setPitchingOnBasePercentage(const double &pitching_on_base_percentage);
    bool is_pitching_on_base_percentage_Set() const;
    bool is_pitching_on_base_percentage_Valid() const;

    double getPitchingOnBasePlusSlugging() const;
    void setPitchingOnBasePlusSlugging(const double &pitching_on_base_plus_slugging);
    bool is_pitching_on_base_plus_slugging_Set() const;
    bool is_pitching_on_base_plus_slugging_Valid() const;

    double getPitchingPerfectGames() const;
    void setPitchingPerfectGames(const double &pitching_perfect_games);
    bool is_pitching_perfect_games_Set() const;
    bool is_pitching_perfect_games_Valid() const;

    double getPitchingPlateAppearances() const;
    void setPitchingPlateAppearances(const double &pitching_plate_appearances);
    bool is_pitching_plate_appearances_Set() const;
    bool is_pitching_plate_appearances_Valid() const;

    double getPitchingPopOuts() const;
    void setPitchingPopOuts(const double &pitching_pop_outs);
    bool is_pitching_pop_outs_Set() const;
    bool is_pitching_pop_outs_Valid() const;

    double getPitchingQualityStarts() const;
    void setPitchingQualityStarts(const double &pitching_quality_starts);
    bool is_pitching_quality_starts_Set() const;
    bool is_pitching_quality_starts_Valid() const;

    double getPitchingReachedOnError() const;
    void setPitchingReachedOnError(const double &pitching_reached_on_error);
    bool is_pitching_reached_on_error_Set() const;
    bool is_pitching_reached_on_error_Valid() const;

    double getPitchingRuns() const;
    void setPitchingRuns(const double &pitching_runs);
    bool is_pitching_runs_Set() const;
    bool is_pitching_runs_Valid() const;

    double getPitchingSacrificeFlies() const;
    void setPitchingSacrificeFlies(const double &pitching_sacrifice_flies);
    bool is_pitching_sacrifice_flies_Set() const;
    bool is_pitching_sacrifice_flies_Valid() const;

    double getPitchingSacrifices() const;
    void setPitchingSacrifices(const double &pitching_sacrifices);
    bool is_pitching_sacrifices_Set() const;
    bool is_pitching_sacrifices_Valid() const;

    double getPitchingShutOuts() const;
    void setPitchingShutOuts(const double &pitching_shut_outs);
    bool is_pitching_shut_outs_Set() const;
    bool is_pitching_shut_outs_Valid() const;

    double getPitchingSingles() const;
    void setPitchingSingles(const double &pitching_singles);
    bool is_pitching_singles_Set() const;
    bool is_pitching_singles_Valid() const;

    double getPitchingSluggingPercentage() const;
    void setPitchingSluggingPercentage(const double &pitching_slugging_percentage);
    bool is_pitching_slugging_percentage_Set() const;
    bool is_pitching_slugging_percentage_Valid() const;

    double getPitchingStrikeouts() const;
    void setPitchingStrikeouts(const double &pitching_strikeouts);
    bool is_pitching_strikeouts_Set() const;
    bool is_pitching_strikeouts_Valid() const;

    double getPitchingStrikeoutsPerNineInnings() const;
    void setPitchingStrikeoutsPerNineInnings(const double &pitching_strikeouts_per_nine_innings);
    bool is_pitching_strikeouts_per_nine_innings_Set() const;
    bool is_pitching_strikeouts_per_nine_innings_Valid() const;

    double getPitchingTotalBases() const;
    void setPitchingTotalBases(const double &pitching_total_bases);
    bool is_pitching_total_bases_Set() const;
    bool is_pitching_total_bases_Valid() const;

    double getPitchingTriples() const;
    void setPitchingTriples(const double &pitching_triples);
    bool is_pitching_triples_Set() const;
    bool is_pitching_triples_Valid() const;

    double getPitchingWalks() const;
    void setPitchingWalks(const double &pitching_walks);
    bool is_pitching_walks_Set() const;
    bool is_pitching_walks_Valid() const;

    double getPitchingWalksPerNineInnings() const;
    void setPitchingWalksPerNineInnings(const double &pitching_walks_per_nine_innings);
    bool is_pitching_walks_per_nine_innings_Set() const;
    bool is_pitching_walks_per_nine_innings_Valid() const;

    double getPitchingWeightedOnBasePercentage() const;
    void setPitchingWeightedOnBasePercentage(const double &pitching_weighted_on_base_percentage);
    bool is_pitching_weighted_on_base_percentage_Set() const;
    bool is_pitching_weighted_on_base_percentage_Valid() const;

    double getPlateAppearances() const;
    void setPlateAppearances(const double &plate_appearances);
    bool is_plate_appearances_Set() const;
    bool is_plate_appearances_Valid() const;

    qint32 getPlayerId() const;
    void setPlayerId(const qint32 &player_id);
    bool is_player_id_Set() const;
    bool is_player_id_Valid() const;

    double getPopOuts() const;
    void setPopOuts(const double &pop_outs);
    bool is_pop_outs_Set() const;
    bool is_pop_outs_Valid() const;

    QString getPosition() const;
    void setPosition(const QString &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    QString getPositionCategory() const;
    void setPositionCategory(const QString &position_category);
    bool is_position_category_Set() const;
    bool is_position_category_Valid() const;

    double getReachedOnError() const;
    void setReachedOnError(const double &reached_on_error);
    bool is_reached_on_error_Set() const;
    bool is_reached_on_error_Valid() const;

    double getRuns() const;
    void setRuns(const double &runs);
    bool is_runs_Set() const;
    bool is_runs_Valid() const;

    double getRunsBattedIn() const;
    void setRunsBattedIn(const double &runs_batted_in);
    bool is_runs_batted_in_Set() const;
    bool is_runs_batted_in_Valid() const;

    double getSacrificeFlies() const;
    void setSacrificeFlies(const double &sacrifice_flies);
    bool is_sacrifice_flies_Set() const;
    bool is_sacrifice_flies_Valid() const;

    double getSacrifices() const;
    void setSacrifices(const double &sacrifices);
    bool is_sacrifices_Set() const;
    bool is_sacrifices_Valid() const;

    double getSaves() const;
    void setSaves(const double &saves);
    bool is_saves_Set() const;
    bool is_saves_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    double getSingles() const;
    void setSingles(const double &singles);
    bool is_singles_Set() const;
    bool is_singles_Valid() const;

    double getSluggingPercentage() const;
    void setSluggingPercentage(const double &slugging_percentage);
    bool is_slugging_percentage_Set() const;
    bool is_slugging_percentage_Valid() const;

    qint32 getStarted() const;
    void setStarted(const qint32 &started);
    bool is_started_Set() const;
    bool is_started_Valid() const;

    qint32 getStatId() const;
    void setStatId(const qint32 &stat_id);
    bool is_stat_id_Set() const;
    bool is_stat_id_Valid() const;

    double getStolenBases() const;
    void setStolenBases(const double &stolen_bases);
    bool is_stolen_bases_Set() const;
    bool is_stolen_bases_Valid() const;

    double getStrikeouts() const;
    void setStrikeouts(const double &strikeouts);
    bool is_strikeouts_Set() const;
    bool is_strikeouts_Valid() const;

    qint32 getSubstituteBattingOrder() const;
    void setSubstituteBattingOrder(const qint32 &substitute_batting_order);
    bool is_substitute_batting_order_Set() const;
    bool is_substitute_batting_order_Valid() const;

    qint32 getSubstituteBattingOrderSequence() const;
    void setSubstituteBattingOrderSequence(const qint32 &substitute_batting_order_sequence);
    bool is_substitute_batting_order_sequence_Set() const;
    bool is_substitute_batting_order_sequence_Valid() const;

    QString getTeam() const;
    void setTeam(const QString &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    double getTotalBases() const;
    void setTotalBases(const double &total_bases);
    bool is_total_bases_Set() const;
    bool is_total_bases_Valid() const;

    double getTotalOutsPitched() const;
    void setTotalOutsPitched(const double &total_outs_pitched);
    bool is_total_outs_pitched_Set() const;
    bool is_total_outs_pitched_Valid() const;

    double getTriples() const;
    void setTriples(const double &triples);
    bool is_triples_Set() const;
    bool is_triples_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    double getWalks() const;
    void setWalks(const double &walks);
    bool is_walks_Set() const;
    bool is_walks_Valid() const;

    double getWalksHitsPerInningsPitched() const;
    void setWalksHitsPerInningsPitched(const double &walks_hits_per_innings_pitched);
    bool is_walks_hits_per_innings_pitched_Set() const;
    bool is_walks_hits_per_innings_pitched_Valid() const;

    double getWeightedOnBasePercentage() const;
    void setWeightedOnBasePercentage(const double &weighted_on_base_percentage);
    bool is_weighted_on_base_percentage_Set() const;
    bool is_weighted_on_base_percentage_Valid() const;

    double getWins() const;
    void setWins(const double &wins);
    bool is_wins_Set() const;
    bool is_wins_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_at_bats;
    bool m_at_bats_isSet;
    bool m_at_bats_isValid;

    qint32 m_auction_value;
    bool m_auction_value_isSet;
    bool m_auction_value_isValid;

    double m_average_draft_position;
    bool m_average_draft_position_isSet;
    bool m_average_draft_position_isValid;

    double m_balls_in_play;
    bool m_balls_in_play_isSet;
    bool m_balls_in_play_isValid;

    double m_batting_average;
    bool m_batting_average_isSet;
    bool m_batting_average_isValid;

    double m_batting_average_on_balls_in_play;
    bool m_batting_average_on_balls_in_play_isSet;
    bool m_batting_average_on_balls_in_play_isValid;

    qint32 m_batting_order;
    bool m_batting_order_isSet;
    bool m_batting_order_isValid;

    bool m_batting_order_confirmed;
    bool m_batting_order_confirmed_isSet;
    bool m_batting_order_confirmed_isValid;

    double m_caught_stealing;
    bool m_caught_stealing_isSet;
    bool m_caught_stealing_isValid;

    double m_double_plays;
    bool m_double_plays_isSet;
    bool m_double_plays_isValid;

    double m_doubles;
    bool m_doubles_isSet;
    bool m_doubles_isValid;

    double m_earned_run_average;
    bool m_earned_run_average_isSet;
    bool m_earned_run_average_isValid;

    double m_errors;
    bool m_errors_isSet;
    bool m_errors_isValid;

    double m_fantasy_points;
    bool m_fantasy_points_isSet;
    bool m_fantasy_points_isValid;

    double m_fantasy_points_batting;
    bool m_fantasy_points_batting_isSet;
    bool m_fantasy_points_batting_isValid;

    double m_fantasy_points_draft_kings;
    bool m_fantasy_points_draft_kings_isSet;
    bool m_fantasy_points_draft_kings_isValid;

    double m_fantasy_points_fan_duel;
    bool m_fantasy_points_fan_duel_isSet;
    bool m_fantasy_points_fan_duel_isValid;

    double m_fantasy_points_fantasy_draft;
    bool m_fantasy_points_fantasy_draft_isSet;
    bool m_fantasy_points_fantasy_draft_isValid;

    double m_fantasy_points_pitching;
    bool m_fantasy_points_pitching_isSet;
    bool m_fantasy_points_pitching_isValid;

    double m_fantasy_points_yahoo;
    bool m_fantasy_points_yahoo_isSet;
    bool m_fantasy_points_yahoo_isValid;

    double m_fielding_independent_pitching;
    bool m_fielding_independent_pitching_isSet;
    bool m_fielding_independent_pitching_isValid;

    double m_fly_outs;
    bool m_fly_outs_isSet;
    bool m_fly_outs_isValid;

    qint32 m_games;
    bool m_games_isSet;
    bool m_games_isValid;

    qint32 m_global_team_id;
    bool m_global_team_id_isSet;
    bool m_global_team_id_isValid;

    double m_grand_slams;
    bool m_grand_slams_isSet;
    bool m_grand_slams_isValid;

    double m_ground_into_double_play;
    bool m_ground_into_double_play_isSet;
    bool m_ground_into_double_play_isValid;

    double m_ground_outs;
    bool m_ground_outs_isSet;
    bool m_ground_outs_isValid;

    double m_hit_by_pitch;
    bool m_hit_by_pitch_isSet;
    bool m_hit_by_pitch_isValid;

    double m_hits;
    bool m_hits_isSet;
    bool m_hits_isValid;

    double m_home_runs;
    bool m_home_runs_isSet;
    bool m_home_runs_isValid;

    double m_innings_pitched_decimal;
    bool m_innings_pitched_decimal_isSet;
    bool m_innings_pitched_decimal_isValid;

    double m_innings_pitched_full;
    bool m_innings_pitched_full_isSet;
    bool m_innings_pitched_full_isValid;

    double m_innings_pitched_outs;
    bool m_innings_pitched_outs_isSet;
    bool m_innings_pitched_outs_isValid;

    double m_intentional_walks;
    bool m_intentional_walks_isSet;
    bool m_intentional_walks_isValid;

    double m_isolated_power;
    bool m_isolated_power_isSet;
    bool m_isolated_power_isValid;

    double m_left_on_base;
    bool m_left_on_base_isSet;
    bool m_left_on_base_isValid;

    double m_line_outs;
    bool m_line_outs_isSet;
    bool m_line_outs_isValid;

    double m_losses;
    bool m_losses_isSet;
    bool m_losses_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    double m_on_base_percentage;
    bool m_on_base_percentage_isSet;
    bool m_on_base_percentage_isValid;

    double m_on_base_plus_slugging;
    bool m_on_base_plus_slugging_isSet;
    bool m_on_base_plus_slugging_isValid;

    double m_outs;
    bool m_outs_isSet;
    bool m_outs_isValid;

    double m_pitches_seen;
    bool m_pitches_seen_isSet;
    bool m_pitches_seen_isValid;

    double m_pitches_thrown;
    bool m_pitches_thrown_isSet;
    bool m_pitches_thrown_isValid;

    double m_pitches_thrown_strikes;
    bool m_pitches_thrown_strikes_isSet;
    bool m_pitches_thrown_strikes_isValid;

    double m_pitching_balls_in_play;
    bool m_pitching_balls_in_play_isSet;
    bool m_pitching_balls_in_play_isValid;

    double m_pitching_batting_average_against;
    bool m_pitching_batting_average_against_isSet;
    bool m_pitching_batting_average_against_isValid;

    double m_pitching_batting_average_on_balls_in_play;
    bool m_pitching_batting_average_on_balls_in_play_isSet;
    bool m_pitching_batting_average_on_balls_in_play_isValid;

    double m_pitching_blown_saves;
    bool m_pitching_blown_saves_isSet;
    bool m_pitching_blown_saves_isValid;

    double m_pitching_catchers_interference;
    bool m_pitching_catchers_interference_isSet;
    bool m_pitching_catchers_interference_isValid;

    double m_pitching_complete_games;
    bool m_pitching_complete_games_isSet;
    bool m_pitching_complete_games_isValid;

    double m_pitching_double_plays;
    bool m_pitching_double_plays_isSet;
    bool m_pitching_double_plays_isValid;

    double m_pitching_doubles;
    bool m_pitching_doubles_isSet;
    bool m_pitching_doubles_isValid;

    double m_pitching_earned_runs;
    bool m_pitching_earned_runs_isSet;
    bool m_pitching_earned_runs_isValid;

    double m_pitching_fly_outs;
    bool m_pitching_fly_outs_isSet;
    bool m_pitching_fly_outs_isValid;

    double m_pitching_grand_slams;
    bool m_pitching_grand_slams_isSet;
    bool m_pitching_grand_slams_isValid;

    double m_pitching_ground_into_double_play;
    bool m_pitching_ground_into_double_play_isSet;
    bool m_pitching_ground_into_double_play_isValid;

    double m_pitching_ground_outs;
    bool m_pitching_ground_outs_isSet;
    bool m_pitching_ground_outs_isValid;

    double m_pitching_hit_by_pitch;
    bool m_pitching_hit_by_pitch_isSet;
    bool m_pitching_hit_by_pitch_isValid;

    double m_pitching_hits;
    bool m_pitching_hits_isSet;
    bool m_pitching_hits_isValid;

    double m_pitching_holds;
    bool m_pitching_holds_isSet;
    bool m_pitching_holds_isValid;

    double m_pitching_home_runs;
    bool m_pitching_home_runs_isSet;
    bool m_pitching_home_runs_isValid;

    qint32 m_pitching_inning_started;
    bool m_pitching_inning_started_isSet;
    bool m_pitching_inning_started_isValid;

    double m_pitching_intentional_walks;
    bool m_pitching_intentional_walks_isSet;
    bool m_pitching_intentional_walks_isValid;

    double m_pitching_line_outs;
    bool m_pitching_line_outs_isSet;
    bool m_pitching_line_outs_isValid;

    double m_pitching_no_hitters;
    bool m_pitching_no_hitters_isSet;
    bool m_pitching_no_hitters_isValid;

    double m_pitching_on_base_percentage;
    bool m_pitching_on_base_percentage_isSet;
    bool m_pitching_on_base_percentage_isValid;

    double m_pitching_on_base_plus_slugging;
    bool m_pitching_on_base_plus_slugging_isSet;
    bool m_pitching_on_base_plus_slugging_isValid;

    double m_pitching_perfect_games;
    bool m_pitching_perfect_games_isSet;
    bool m_pitching_perfect_games_isValid;

    double m_pitching_plate_appearances;
    bool m_pitching_plate_appearances_isSet;
    bool m_pitching_plate_appearances_isValid;

    double m_pitching_pop_outs;
    bool m_pitching_pop_outs_isSet;
    bool m_pitching_pop_outs_isValid;

    double m_pitching_quality_starts;
    bool m_pitching_quality_starts_isSet;
    bool m_pitching_quality_starts_isValid;

    double m_pitching_reached_on_error;
    bool m_pitching_reached_on_error_isSet;
    bool m_pitching_reached_on_error_isValid;

    double m_pitching_runs;
    bool m_pitching_runs_isSet;
    bool m_pitching_runs_isValid;

    double m_pitching_sacrifice_flies;
    bool m_pitching_sacrifice_flies_isSet;
    bool m_pitching_sacrifice_flies_isValid;

    double m_pitching_sacrifices;
    bool m_pitching_sacrifices_isSet;
    bool m_pitching_sacrifices_isValid;

    double m_pitching_shut_outs;
    bool m_pitching_shut_outs_isSet;
    bool m_pitching_shut_outs_isValid;

    double m_pitching_singles;
    bool m_pitching_singles_isSet;
    bool m_pitching_singles_isValid;

    double m_pitching_slugging_percentage;
    bool m_pitching_slugging_percentage_isSet;
    bool m_pitching_slugging_percentage_isValid;

    double m_pitching_strikeouts;
    bool m_pitching_strikeouts_isSet;
    bool m_pitching_strikeouts_isValid;

    double m_pitching_strikeouts_per_nine_innings;
    bool m_pitching_strikeouts_per_nine_innings_isSet;
    bool m_pitching_strikeouts_per_nine_innings_isValid;

    double m_pitching_total_bases;
    bool m_pitching_total_bases_isSet;
    bool m_pitching_total_bases_isValid;

    double m_pitching_triples;
    bool m_pitching_triples_isSet;
    bool m_pitching_triples_isValid;

    double m_pitching_walks;
    bool m_pitching_walks_isSet;
    bool m_pitching_walks_isValid;

    double m_pitching_walks_per_nine_innings;
    bool m_pitching_walks_per_nine_innings_isSet;
    bool m_pitching_walks_per_nine_innings_isValid;

    double m_pitching_weighted_on_base_percentage;
    bool m_pitching_weighted_on_base_percentage_isSet;
    bool m_pitching_weighted_on_base_percentage_isValid;

    double m_plate_appearances;
    bool m_plate_appearances_isSet;
    bool m_plate_appearances_isValid;

    qint32 m_player_id;
    bool m_player_id_isSet;
    bool m_player_id_isValid;

    double m_pop_outs;
    bool m_pop_outs_isSet;
    bool m_pop_outs_isValid;

    QString m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_position_category;
    bool m_position_category_isSet;
    bool m_position_category_isValid;

    double m_reached_on_error;
    bool m_reached_on_error_isSet;
    bool m_reached_on_error_isValid;

    double m_runs;
    bool m_runs_isSet;
    bool m_runs_isValid;

    double m_runs_batted_in;
    bool m_runs_batted_in_isSet;
    bool m_runs_batted_in_isValid;

    double m_sacrifice_flies;
    bool m_sacrifice_flies_isSet;
    bool m_sacrifice_flies_isValid;

    double m_sacrifices;
    bool m_sacrifices_isSet;
    bool m_sacrifices_isValid;

    double m_saves;
    bool m_saves_isSet;
    bool m_saves_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    double m_singles;
    bool m_singles_isSet;
    bool m_singles_isValid;

    double m_slugging_percentage;
    bool m_slugging_percentage_isSet;
    bool m_slugging_percentage_isValid;

    qint32 m_started;
    bool m_started_isSet;
    bool m_started_isValid;

    qint32 m_stat_id;
    bool m_stat_id_isSet;
    bool m_stat_id_isValid;

    double m_stolen_bases;
    bool m_stolen_bases_isSet;
    bool m_stolen_bases_isValid;

    double m_strikeouts;
    bool m_strikeouts_isSet;
    bool m_strikeouts_isValid;

    qint32 m_substitute_batting_order;
    bool m_substitute_batting_order_isSet;
    bool m_substitute_batting_order_isValid;

    qint32 m_substitute_batting_order_sequence;
    bool m_substitute_batting_order_sequence_isSet;
    bool m_substitute_batting_order_sequence_isValid;

    QString m_team;
    bool m_team_isSet;
    bool m_team_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    double m_total_bases;
    bool m_total_bases_isSet;
    bool m_total_bases_isValid;

    double m_total_outs_pitched;
    bool m_total_outs_pitched_isSet;
    bool m_total_outs_pitched_isValid;

    double m_triples;
    bool m_triples_isSet;
    bool m_triples_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;

    double m_walks;
    bool m_walks_isSet;
    bool m_walks_isValid;

    double m_walks_hits_per_innings_pitched;
    bool m_walks_hits_per_innings_pitched_isSet;
    bool m_walks_hits_per_innings_pitched_isValid;

    double m_weighted_on_base_percentage;
    bool m_weighted_on_base_percentage_isSet;
    bool m_weighted_on_base_percentage_isValid;

    double m_wins;
    bool m_wins_isSet;
    bool m_wins_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlayerSeasonProjection)

#endif // OAIPlayerSeasonProjection_H
