/**
 * CS:GO v3 Scores
 * CS:GO v3 Scores
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICompetitionDetail.h
 *
 * 
 */

#ifndef OAICompetitionDetail_H
#define OAICompetitionDetail_H

#include <QJsonObject>

#include "OAIGame.h"
#include "OAISeason.h"
#include "OAITeamDetail.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISeason;
class OAIGame;
class OAITeamDetail;

class OAICompetitionDetail : public OAIObject {
public:
    OAICompetitionDetail();
    OAICompetitionDetail(QString json);
    ~OAICompetitionDetail() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAreaId() const;
    void setAreaId(const qint32 &area_id);
    bool is_area_id_Set() const;
    bool is_area_id_Valid() const;

    QString getAreaName() const;
    void setAreaName(const QString &area_name);
    bool is_area_name_Set() const;
    bool is_area_name_Valid() const;

    qint32 getCompetitionId() const;
    void setCompetitionId(const qint32 &competition_id);
    bool is_competition_id_Set() const;
    bool is_competition_id_Valid() const;

    OAISeason getCurrentSeason() const;
    void setCurrentSeason(const OAISeason &current_season);
    bool is_current_season_Set() const;
    bool is_current_season_Valid() const;

    QString getFormat() const;
    void setFormat(const QString &format);
    bool is_format_Set() const;
    bool is_format_Valid() const;

    QList<OAIGame> getGames() const;
    void setGames(const QList<OAIGame> &games);
    bool is_games_Set() const;
    bool is_games_Valid() const;

    QString getGender() const;
    void setGender(const QString &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    bool isPlayerStatsCoverage() const;
    void setPlayerStatsCoverage(const bool &player_stats_coverage);
    bool is_player_stats_coverage_Set() const;
    bool is_player_stats_coverage_Valid() const;

    QList<OAISeason> getSeasons() const;
    void setSeasons(const QList<OAISeason> &seasons);
    bool is_seasons_Set() const;
    bool is_seasons_Valid() const;

    QList<OAITeamDetail> getTeams() const;
    void setTeams(const QList<OAITeamDetail> &teams);
    bool is_teams_Set() const;
    bool is_teams_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_area_id;
    bool m_area_id_isSet;
    bool m_area_id_isValid;

    QString m_area_name;
    bool m_area_name_isSet;
    bool m_area_name_isValid;

    qint32 m_competition_id;
    bool m_competition_id_isSet;
    bool m_competition_id_isValid;

    OAISeason m_current_season;
    bool m_current_season_isSet;
    bool m_current_season_isValid;

    QString m_format;
    bool m_format_isSet;
    bool m_format_isValid;

    QList<OAIGame> m_games;
    bool m_games_isSet;
    bool m_games_isValid;

    QString m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    bool m_player_stats_coverage;
    bool m_player_stats_coverage_isSet;
    bool m_player_stats_coverage_isValid;

    QList<OAISeason> m_seasons;
    bool m_seasons_isSet;
    bool m_seasons_isValid;

    QList<OAITeamDetail> m_teams;
    bool m_teams_isSet;
    bool m_teams_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICompetitionDetail)

#endif // OAICompetitionDetail_H
