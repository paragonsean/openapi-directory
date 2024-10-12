/**
 * Soccer v3 Scores
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRound.h
 *
 * 
 */

#ifndef OAIRound_H
#define OAIRound_H

#include <QJsonObject>

#include "OAIGame.h"
#include "OAIPlayerSeason.h"
#include "OAIStanding.h"
#include "OAITeamSeason.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGame;
class OAIPlayerSeason;
class OAIStanding;
class OAITeamSeason;

class OAIRound : public OAIObject {
public:
    OAIRound();
    OAIRound(QString json);
    ~OAIRound() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isCurrentRound() const;
    void setCurrentRound(const bool &current_round);
    bool is_current_round_Set() const;
    bool is_current_round_Valid() const;

    qint32 getCurrentWeek() const;
    void setCurrentWeek(const qint32 &current_week);
    bool is_current_week_Set() const;
    bool is_current_week_Valid() const;

    QString getEndDate() const;
    void setEndDate(const QString &end_date);
    bool is_end_date_Set() const;
    bool is_end_date_Valid() const;

    QList<OAIGame> getGames() const;
    void setGames(const QList<OAIGame> &games);
    bool is_games_Set() const;
    bool is_games_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAIPlayerSeason> getPlayerSeasons() const;
    void setPlayerSeasons(const QList<OAIPlayerSeason> &player_seasons);
    bool is_player_seasons_Set() const;
    bool is_player_seasons_Valid() const;

    qint32 getRoundId() const;
    void setRoundId(const qint32 &round_id);
    bool is_round_id_Set() const;
    bool is_round_id_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonId() const;
    void setSeasonId(const qint32 &season_id);
    bool is_season_id_Set() const;
    bool is_season_id_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    QList<OAIStanding> getStandings() const;
    void setStandings(const QList<OAIStanding> &standings);
    bool is_standings_Set() const;
    bool is_standings_Valid() const;

    QString getStartDate() const;
    void setStartDate(const QString &start_date);
    bool is_start_date_Set() const;
    bool is_start_date_Valid() const;

    QList<OAITeamSeason> getTeamSeasons() const;
    void setTeamSeasons(const QList<OAITeamSeason> &team_seasons);
    bool is_team_seasons_Set() const;
    bool is_team_seasons_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_current_round;
    bool m_current_round_isSet;
    bool m_current_round_isValid;

    qint32 m_current_week;
    bool m_current_week_isSet;
    bool m_current_week_isValid;

    QString m_end_date;
    bool m_end_date_isSet;
    bool m_end_date_isValid;

    QList<OAIGame> m_games;
    bool m_games_isSet;
    bool m_games_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAIPlayerSeason> m_player_seasons;
    bool m_player_seasons_isSet;
    bool m_player_seasons_isValid;

    qint32 m_round_id;
    bool m_round_id_isSet;
    bool m_round_id_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_id;
    bool m_season_id_isSet;
    bool m_season_id_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    QList<OAIStanding> m_standings;
    bool m_standings_isSet;
    bool m_standings_isValid;

    QString m_start_date;
    bool m_start_date_isSet;
    bool m_start_date_isValid;

    QList<OAITeamSeason> m_team_seasons;
    bool m_team_seasons_isSet;
    bool m_team_seasons_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRound)

#endif // OAIRound_H
