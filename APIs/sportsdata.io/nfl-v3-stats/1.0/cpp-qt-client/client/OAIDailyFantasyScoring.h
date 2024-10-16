/**
 * NFL v3 Stats
 * NFL rosters, player stats, team stats, and fantasy stats API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDailyFantasyScoring.h
 *
 * 
 */

#ifndef OAIDailyFantasyScoring_H
#define OAIDailyFantasyScoring_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDailyFantasyScoring : public OAIObject {
public:
    OAIDailyFantasyScoring();
    OAIDailyFantasyScoring(QString json);
    ~OAIDailyFantasyScoring() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDate() const;
    void setDate(const QString &date);
    bool is_date_Set() const;
    bool is_date_Valid() const;

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

    double getFantasyPointsFantasyDraft() const;
    void setFantasyPointsFantasyDraft(const double &fantasy_points_fantasy_draft);
    bool is_fantasy_points_fantasy_draft_Set() const;
    bool is_fantasy_points_fantasy_draft_Valid() const;

    double getFantasyPointsPpr() const;
    void setFantasyPointsPpr(const double &fantasy_points_ppr);
    bool is_fantasy_points_ppr_Set() const;
    bool is_fantasy_points_ppr_Valid() const;

    double getFantasyPointsYahoo() const;
    void setFantasyPointsYahoo(const double &fantasy_points_yahoo);
    bool is_fantasy_points_yahoo_Set() const;
    bool is_fantasy_points_yahoo_Valid() const;

    bool isHasStarted() const;
    void setHasStarted(const bool &has_started);
    bool is_has_started_Set() const;
    bool is_has_started_Valid() const;

    bool isIsInProgress() const;
    void setIsInProgress(const bool &is_in_progress);
    bool is_is_in_progress_Set() const;
    bool is_is_in_progress_Valid() const;

    bool isIsOver() const;
    void setIsOver(const bool &is_over);
    bool is_is_over_Set() const;
    bool is_is_over_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getPlayerId() const;
    void setPlayerId(const qint32 &player_id);
    bool is_player_id_Set() const;
    bool is_player_id_Valid() const;

    QString getPosition() const;
    void setPosition(const QString &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    QString getTeam() const;
    void setTeam(const QString &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_date;
    bool m_date_isSet;
    bool m_date_isValid;

    double m_fantasy_points;
    bool m_fantasy_points_isSet;
    bool m_fantasy_points_isValid;

    double m_fantasy_points_draft_kings;
    bool m_fantasy_points_draft_kings_isSet;
    bool m_fantasy_points_draft_kings_isValid;

    double m_fantasy_points_fan_duel;
    bool m_fantasy_points_fan_duel_isSet;
    bool m_fantasy_points_fan_duel_isValid;

    double m_fantasy_points_fantasy_draft;
    bool m_fantasy_points_fantasy_draft_isSet;
    bool m_fantasy_points_fantasy_draft_isValid;

    double m_fantasy_points_ppr;
    bool m_fantasy_points_ppr_isSet;
    bool m_fantasy_points_ppr_isValid;

    double m_fantasy_points_yahoo;
    bool m_fantasy_points_yahoo_isSet;
    bool m_fantasy_points_yahoo_isValid;

    bool m_has_started;
    bool m_has_started_isSet;
    bool m_has_started_isValid;

    bool m_is_in_progress;
    bool m_is_in_progress_isSet;
    bool m_is_in_progress_isValid;

    bool m_is_over;
    bool m_is_over_isSet;
    bool m_is_over_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_player_id;
    bool m_player_id_isSet;
    bool m_player_id_isValid;

    QString m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_team;
    bool m_team_isSet;
    bool m_team_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDailyFantasyScoring)

#endif // OAIDailyFantasyScoring_H
