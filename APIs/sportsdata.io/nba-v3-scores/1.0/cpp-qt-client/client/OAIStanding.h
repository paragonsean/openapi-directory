/**
 * NBA v3 Scores
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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

    QString getConference() const;
    void setConference(const QString &conference);
    bool is_conference_Set() const;
    bool is_conference_Valid() const;

    qint32 getConferenceLosses() const;
    void setConferenceLosses(const qint32 &conference_losses);
    bool is_conference_losses_Set() const;
    bool is_conference_losses_Valid() const;

    qint32 getConferenceRank() const;
    void setConferenceRank(const qint32 &conference_rank);
    bool is_conference_rank_Set() const;
    bool is_conference_rank_Valid() const;

    qint32 getConferenceWins() const;
    void setConferenceWins(const qint32 &conference_wins);
    bool is_conference_wins_Set() const;
    bool is_conference_wins_Valid() const;

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

    double getGamesBack() const;
    void setGamesBack(const double &games_back);
    bool is_games_back_Set() const;
    bool is_games_back_Valid() const;

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

    qint32 getLastTenLosses() const;
    void setLastTenLosses(const qint32 &last_ten_losses);
    bool is_last_ten_losses_Set() const;
    bool is_last_ten_losses_Valid() const;

    qint32 getLastTenWins() const;
    void setLastTenWins(const qint32 &last_ten_wins);
    bool is_last_ten_wins_Set() const;
    bool is_last_ten_wins_Valid() const;

    qint32 getLosses() const;
    void setLosses(const qint32 &losses);
    bool is_losses_Set() const;
    bool is_losses_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    double getPercentage() const;
    void setPercentage(const double &percentage);
    bool is_percentage_Set() const;
    bool is_percentage_Valid() const;

    double getPointsPerGameAgainst() const;
    void setPointsPerGameAgainst(const double &points_per_game_against);
    bool is_points_per_game_against_Set() const;
    bool is_points_per_game_against_Valid() const;

    double getPointsPerGameFor() const;
    void setPointsPerGameFor(const double &points_per_game_for);
    bool is_points_per_game_for_Set() const;
    bool is_points_per_game_for_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    qint32 getStreak() const;
    void setStreak(const qint32 &streak);
    bool is_streak_Set() const;
    bool is_streak_Valid() const;

    QString getStreakDescription() const;
    void setStreakDescription(const QString &streak_description);
    bool is_streak_description_Set() const;
    bool is_streak_description_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

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

    QString m_conference;
    bool m_conference_isSet;
    bool m_conference_isValid;

    qint32 m_conference_losses;
    bool m_conference_losses_isSet;
    bool m_conference_losses_isValid;

    qint32 m_conference_rank;
    bool m_conference_rank_isSet;
    bool m_conference_rank_isValid;

    qint32 m_conference_wins;
    bool m_conference_wins_isSet;
    bool m_conference_wins_isValid;

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

    double m_games_back;
    bool m_games_back_isSet;
    bool m_games_back_isValid;

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

    qint32 m_last_ten_losses;
    bool m_last_ten_losses_isSet;
    bool m_last_ten_losses_isValid;

    qint32 m_last_ten_wins;
    bool m_last_ten_wins_isSet;
    bool m_last_ten_wins_isValid;

    qint32 m_losses;
    bool m_losses_isSet;
    bool m_losses_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    double m_percentage;
    bool m_percentage_isSet;
    bool m_percentage_isValid;

    double m_points_per_game_against;
    bool m_points_per_game_against_isSet;
    bool m_points_per_game_against_isValid;

    double m_points_per_game_for;
    bool m_points_per_game_for_isSet;
    bool m_points_per_game_for_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    qint32 m_streak;
    bool m_streak_isSet;
    bool m_streak_isValid;

    QString m_streak_description;
    bool m_streak_description_isSet;
    bool m_streak_description_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    qint32 m_wins;
    bool m_wins_isSet;
    bool m_wins_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStanding)

#endif // OAIStanding_H
