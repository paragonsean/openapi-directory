/**
 * MLB v3 Scores
 * MLB scores API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIStanding.h
 *
 * 
 */

#ifndef OAIStanding_H
#define OAIStanding_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIStanding : public OAIObject {
public:
    OAIStanding();
    OAIStanding(QString json);
    ~OAIStanding() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAwayLosses() const;
    void setAwayLosses(const qint32 &away_losses);
    bool is_away_losses_Set() const;
    bool is_away_losses_Valid() const;

    qint32 getAwayWins() const;
    void setAwayWins(const qint32 &away_wins);
    bool is_away_wins_Set() const;
    bool is_away_wins_Valid() const;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    qint32 getDayLosses() const;
    void setDayLosses(const qint32 &day_losses);
    bool is_day_losses_Set() const;
    bool is_day_losses_Valid() const;

    qint32 getDayWins() const;
    void setDayWins(const qint32 &day_wins);
    bool is_day_wins_Set() const;
    bool is_day_wins_Valid() const;

    QString getDivision() const;
    void setDivision(const QString &division);
    bool is_division_Set() const;
    bool is_division_Valid() const;

    qint32 getDivisionLosses() const;
    void setDivisionLosses(const qint32 &division_losses);
    bool is_division_losses_Set() const;
    bool is_division_losses_Valid() const;

    qint32 getDivisionRank() const;
    void setDivisionRank(const qint32 &division_rank);
    bool is_division_rank_Set() const;
    bool is_division_rank_Valid() const;

    qint32 getDivisionWins() const;
    void setDivisionWins(const qint32 &division_wins);
    bool is_division_wins_Set() const;
    bool is_division_wins_Valid() const;

    double getGamesBehind() const;
    void setGamesBehind(const double &games_behind);
    bool is_games_behind_Set() const;
    bool is_games_behind_Valid() const;

    qint32 getGlobalTeamId() const;
    void setGlobalTeamId(const qint32 &global_team_id);
    bool is_global_team_id_Set() const;
    bool is_global_team_id_Valid() const;

    qint32 getHomeLosses() const;
    void setHomeLosses(const qint32 &home_losses);
    bool is_home_losses_Set() const;
    bool is_home_losses_Valid() const;

    qint32 getHomeWins() const;
    void setHomeWins(const qint32 &home_wins);
    bool is_home_wins_Set() const;
    bool is_home_wins_Valid() const;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    qint32 getLastTenGamesLosses() const;
    void setLastTenGamesLosses(const qint32 &last_ten_games_losses);
    bool is_last_ten_games_losses_Set() const;
    bool is_last_ten_games_losses_Valid() const;

    qint32 getLastTenGamesWins() const;
    void setLastTenGamesWins(const qint32 &last_ten_games_wins);
    bool is_last_ten_games_wins_Set() const;
    bool is_last_ten_games_wins_Valid() const;

    QString getLeague() const;
    void setLeague(const QString &league);
    bool is_league_Set() const;
    bool is_league_Valid() const;

    qint32 getLeagueRank() const;
    void setLeagueRank(const qint32 &league_rank);
    bool is_league_rank_Set() const;
    bool is_league_rank_Valid() const;

    qint32 getLosses() const;
    void setLosses(const qint32 &losses);
    bool is_losses_Set() const;
    bool is_losses_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNightLosses() const;
    void setNightLosses(const qint32 &night_losses);
    bool is_night_losses_Set() const;
    bool is_night_losses_Valid() const;

    qint32 getNightWins() const;
    void setNightWins(const qint32 &night_wins);
    bool is_night_wins_Set() const;
    bool is_night_wins_Valid() const;

    double getPercentage() const;
    void setPercentage(const double &percentage);
    bool is_percentage_Set() const;
    bool is_percentage_Valid() const;

    qint32 getRunsAgainst() const;
    void setRunsAgainst(const qint32 &runs_against);
    bool is_runs_against_Set() const;
    bool is_runs_against_Valid() const;

    qint32 getRunsScored() const;
    void setRunsScored(const qint32 &runs_scored);
    bool is_runs_scored_Set() const;
    bool is_runs_scored_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    QString getStreak() const;
    void setStreak(const QString &streak);
    bool is_streak_Set() const;
    bool is_streak_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    double getWildCardGamesBehind() const;
    void setWildCardGamesBehind(const double &wild_card_games_behind);
    bool is_wild_card_games_behind_Set() const;
    bool is_wild_card_games_behind_Valid() const;

    qint32 getWildCardRank() const;
    void setWildCardRank(const qint32 &wild_card_rank);
    bool is_wild_card_rank_Set() const;
    bool is_wild_card_rank_Valid() const;

    qint32 getWins() const;
    void setWins(const qint32 &wins);
    bool is_wins_Set() const;
    bool is_wins_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_away_losses;
    bool m_away_losses_isSet;
    bool m_away_losses_isValid;

    qint32 m_away_wins;
    bool m_away_wins_isSet;
    bool m_away_wins_isValid;

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    qint32 m_day_losses;
    bool m_day_losses_isSet;
    bool m_day_losses_isValid;

    qint32 m_day_wins;
    bool m_day_wins_isSet;
    bool m_day_wins_isValid;

    QString m_division;
    bool m_division_isSet;
    bool m_division_isValid;

    qint32 m_division_losses;
    bool m_division_losses_isSet;
    bool m_division_losses_isValid;

    qint32 m_division_rank;
    bool m_division_rank_isSet;
    bool m_division_rank_isValid;

    qint32 m_division_wins;
    bool m_division_wins_isSet;
    bool m_division_wins_isValid;

    double m_games_behind;
    bool m_games_behind_isSet;
    bool m_games_behind_isValid;

    qint32 m_global_team_id;
    bool m_global_team_id_isSet;
    bool m_global_team_id_isValid;

    qint32 m_home_losses;
    bool m_home_losses_isSet;
    bool m_home_losses_isValid;

    qint32 m_home_wins;
    bool m_home_wins_isSet;
    bool m_home_wins_isValid;

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;

    qint32 m_last_ten_games_losses;
    bool m_last_ten_games_losses_isSet;
    bool m_last_ten_games_losses_isValid;

    qint32 m_last_ten_games_wins;
    bool m_last_ten_games_wins_isSet;
    bool m_last_ten_games_wins_isValid;

    QString m_league;
    bool m_league_isSet;
    bool m_league_isValid;

    qint32 m_league_rank;
    bool m_league_rank_isSet;
    bool m_league_rank_isValid;

    qint32 m_losses;
    bool m_losses_isSet;
    bool m_losses_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_night_losses;
    bool m_night_losses_isSet;
    bool m_night_losses_isValid;

    qint32 m_night_wins;
    bool m_night_wins_isSet;
    bool m_night_wins_isValid;

    double m_percentage;
    bool m_percentage_isSet;
    bool m_percentage_isValid;

    qint32 m_runs_against;
    bool m_runs_against_isSet;
    bool m_runs_against_isValid;

    qint32 m_runs_scored;
    bool m_runs_scored_isSet;
    bool m_runs_scored_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    QString m_streak;
    bool m_streak_isSet;
    bool m_streak_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    double m_wild_card_games_behind;
    bool m_wild_card_games_behind_isSet;
    bool m_wild_card_games_behind_isValid;

    qint32 m_wild_card_rank;
    bool m_wild_card_rank_isSet;
    bool m_wild_card_rank_isValid;

    qint32 m_wins;
    bool m_wins_isSet;
    bool m_wins_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStanding)

#endif // OAIStanding_H
