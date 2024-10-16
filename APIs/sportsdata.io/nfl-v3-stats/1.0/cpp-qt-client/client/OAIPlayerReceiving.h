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
 * OAIPlayerReceiving.h
 *
 * 
 */

#ifndef OAIPlayerReceiving_H
#define OAIPlayerReceiving_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPlayerReceiving : public OAIObject {
public:
    OAIPlayerReceiving();
    OAIPlayerReceiving(QString json);
    ~OAIPlayerReceiving() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getFantasyPoints() const;
    void setFantasyPoints(const double &fantasy_points);
    bool is_fantasy_points_Set() const;
    bool is_fantasy_points_Valid() const;

    QString getFantasyPosition() const;
    void setFantasyPosition(const QString &fantasy_position);
    bool is_fantasy_position_Set() const;
    bool is_fantasy_position_Valid() const;

    qint32 getFumblesLost() const;
    void setFumblesLost(const qint32 &fumbles_lost);
    bool is_fumbles_lost_Set() const;
    bool is_fumbles_lost_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNumber() const;
    void setNumber(const qint32 &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    qint32 getPlayerGameId() const;
    void setPlayerGameId(const qint32 &player_game_id);
    bool is_player_game_id_Set() const;
    bool is_player_game_id_Valid() const;

    qint32 getPlayerId() const;
    void setPlayerId(const qint32 &player_id);
    bool is_player_id_Set() const;
    bool is_player_id_Valid() const;

    QString getPosition() const;
    void setPosition(const QString &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    QString getPositionCategory() const;
    void setPositionCategory(const QString &position_category);
    bool is_position_category_Set() const;
    bool is_position_category_Valid() const;

    qint32 getReceivingLong() const;
    void setReceivingLong(const qint32 &receiving_long);
    bool is_receiving_long_Set() const;
    bool is_receiving_long_Valid() const;

    qint32 getReceivingTargets() const;
    void setReceivingTargets(const qint32 &receiving_targets);
    bool is_receiving_targets_Set() const;
    bool is_receiving_targets_Valid() const;

    qint32 getReceivingTouchdowns() const;
    void setReceivingTouchdowns(const qint32 &receiving_touchdowns);
    bool is_receiving_touchdowns_Set() const;
    bool is_receiving_touchdowns_Valid() const;

    qint32 getReceivingYards() const;
    void setReceivingYards(const qint32 &receiving_yards);
    bool is_receiving_yards_Set() const;
    bool is_receiving_yards_Valid() const;

    double getReceivingYardsPerReception() const;
    void setReceivingYardsPerReception(const double &receiving_yards_per_reception);
    bool is_receiving_yards_per_reception_Set() const;
    bool is_receiving_yards_per_reception_Valid() const;

    double getReceivingYardsPerTarget() const;
    void setReceivingYardsPerTarget(const double &receiving_yards_per_target);
    bool is_receiving_yards_per_target_Set() const;
    bool is_receiving_yards_per_target_Valid() const;

    double getReceptionPercentage() const;
    void setReceptionPercentage(const double &reception_percentage);
    bool is_reception_percentage_Set() const;
    bool is_reception_percentage_Valid() const;

    qint32 getReceptions() const;
    void setReceptions(const qint32 &receptions);
    bool is_receptions_Set() const;
    bool is_receptions_Valid() const;

    QString getShortName() const;
    void setShortName(const QString &short_name);
    bool is_short_name_Set() const;
    bool is_short_name_Valid() const;

    QString getTeam() const;
    void setTeam(const QString &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    qint32 getTwoPointConversionReceptions() const;
    void setTwoPointConversionReceptions(const qint32 &two_point_conversion_receptions);
    bool is_two_point_conversion_receptions_Set() const;
    bool is_two_point_conversion_receptions_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_fantasy_points;
    bool m_fantasy_points_isSet;
    bool m_fantasy_points_isValid;

    QString m_fantasy_position;
    bool m_fantasy_position_isSet;
    bool m_fantasy_position_isValid;

    qint32 m_fumbles_lost;
    bool m_fumbles_lost_isSet;
    bool m_fumbles_lost_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    qint32 m_player_game_id;
    bool m_player_game_id_isSet;
    bool m_player_game_id_isValid;

    qint32 m_player_id;
    bool m_player_id_isSet;
    bool m_player_id_isValid;

    QString m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_position_category;
    bool m_position_category_isSet;
    bool m_position_category_isValid;

    qint32 m_receiving_long;
    bool m_receiving_long_isSet;
    bool m_receiving_long_isValid;

    qint32 m_receiving_targets;
    bool m_receiving_targets_isSet;
    bool m_receiving_targets_isValid;

    qint32 m_receiving_touchdowns;
    bool m_receiving_touchdowns_isSet;
    bool m_receiving_touchdowns_isValid;

    qint32 m_receiving_yards;
    bool m_receiving_yards_isSet;
    bool m_receiving_yards_isValid;

    double m_receiving_yards_per_reception;
    bool m_receiving_yards_per_reception_isSet;
    bool m_receiving_yards_per_reception_isValid;

    double m_receiving_yards_per_target;
    bool m_receiving_yards_per_target_isSet;
    bool m_receiving_yards_per_target_isValid;

    double m_reception_percentage;
    bool m_reception_percentage_isSet;
    bool m_reception_percentage_isValid;

    qint32 m_receptions;
    bool m_receptions_isSet;
    bool m_receptions_isValid;

    QString m_short_name;
    bool m_short_name_isSet;
    bool m_short_name_isValid;

    QString m_team;
    bool m_team_isSet;
    bool m_team_isValid;

    qint32 m_two_point_conversion_receptions;
    bool m_two_point_conversion_receptions_isSet;
    bool m_two_point_conversion_receptions_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlayerReceiving)

#endif // OAIPlayerReceiving_H
