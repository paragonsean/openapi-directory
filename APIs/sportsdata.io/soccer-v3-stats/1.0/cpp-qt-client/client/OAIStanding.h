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

    qint32 getDraws() const;
    void setDraws(const qint32 &draws);
    bool is_draws_Set() const;
    bool is_draws_Valid() const;

    qint32 getGames() const;
    void setGames(const qint32 &games);
    bool is_games_Set() const;
    bool is_games_Valid() const;

    qint32 getGlobalTeamId() const;
    void setGlobalTeamId(const qint32 &global_team_id);
    bool is_global_team_id_Set() const;
    bool is_global_team_id_Valid() const;

    qint32 getGoalsAgainst() const;
    void setGoalsAgainst(const qint32 &goals_against);
    bool is_goals_against_Set() const;
    bool is_goals_against_Valid() const;

    qint32 getGoalsDifferential() const;
    void setGoalsDifferential(const qint32 &goals_differential);
    bool is_goals_differential_Set() const;
    bool is_goals_differential_Valid() const;

    qint32 getGoalsScored() const;
    void setGoalsScored(const qint32 &goals_scored);
    bool is_goals_scored_Set() const;
    bool is_goals_scored_Valid() const;

    QString getGroup() const;
    void setGroup(const QString &group);
    bool is_group_Set() const;
    bool is_group_Valid() const;

    qint32 getLosses() const;
    void setLosses(const qint32 &losses);
    bool is_losses_Set() const;
    bool is_losses_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getOrder() const;
    void setOrder(const qint32 &order);
    bool is_order_Set() const;
    bool is_order_Valid() const;

    qint32 getPoints() const;
    void setPoints(const qint32 &points);
    bool is_points_Set() const;
    bool is_points_Valid() const;

    qint32 getRoundId() const;
    void setRoundId(const qint32 &round_id);
    bool is_round_id_Set() const;
    bool is_round_id_Valid() const;

    QString getScope() const;
    void setScope(const QString &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    QString getShortName() const;
    void setShortName(const QString &short_name);
    bool is_short_name_Set() const;
    bool is_short_name_Valid() const;

    qint32 getStandingId() const;
    void setStandingId(const qint32 &standing_id);
    bool is_standing_id_Set() const;
    bool is_standing_id_Valid() const;

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

    qint32 m_draws;
    bool m_draws_isSet;
    bool m_draws_isValid;

    qint32 m_games;
    bool m_games_isSet;
    bool m_games_isValid;

    qint32 m_global_team_id;
    bool m_global_team_id_isSet;
    bool m_global_team_id_isValid;

    qint32 m_goals_against;
    bool m_goals_against_isSet;
    bool m_goals_against_isValid;

    qint32 m_goals_differential;
    bool m_goals_differential_isSet;
    bool m_goals_differential_isValid;

    qint32 m_goals_scored;
    bool m_goals_scored_isSet;
    bool m_goals_scored_isValid;

    QString m_group;
    bool m_group_isSet;
    bool m_group_isValid;

    qint32 m_losses;
    bool m_losses_isSet;
    bool m_losses_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_order;
    bool m_order_isSet;
    bool m_order_isValid;

    qint32 m_points;
    bool m_points_isSet;
    bool m_points_isValid;

    qint32 m_round_id;
    bool m_round_id_isSet;
    bool m_round_id_isValid;

    QString m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;

    QString m_short_name;
    bool m_short_name_isSet;
    bool m_short_name_isValid;

    qint32 m_standing_id;
    bool m_standing_id_isSet;
    bool m_standing_id_isValid;

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
