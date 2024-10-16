/**
 * NHL v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPlay.h
 *
 * 
 */

#ifndef OAIPlay_H
#define OAIPlay_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPlay : public OAIObject {
public:
    OAIPlay();
    OAIPlay(QString json);
    ~OAIPlay() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAwayTeamScore() const;
    void setAwayTeamScore(const qint32 &away_team_score);
    bool is_away_team_score_Set() const;
    bool is_away_team_score_Valid() const;

    QString getCategory() const;
    void setCategory(const QString &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    qint32 getClockMinutes() const;
    void setClockMinutes(const qint32 &clock_minutes);
    bool is_clock_minutes_Set() const;
    bool is_clock_minutes_Valid() const;

    qint32 getClockSeconds() const;
    void setClockSeconds(const qint32 &clock_seconds);
    bool is_clock_seconds_Set() const;
    bool is_clock_seconds_Valid() const;

    QString getCreated() const;
    void setCreated(const QString &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    qint32 getFirstAssistedByPlayerId() const;
    void setFirstAssistedByPlayerId(const qint32 &first_assisted_by_player_id);
    bool is_first_assisted_by_player_id_Set() const;
    bool is_first_assisted_by_player_id_Valid() const;

    qint32 getHomeTeamScore() const;
    void setHomeTeamScore(const qint32 &home_team_score);
    bool is_home_team_score_Set() const;
    bool is_home_team_score_Valid() const;

    QString getOpponent() const;
    void setOpponent(const QString &opponent);
    bool is_opponent_Set() const;
    bool is_opponent_Valid() const;

    qint32 getOpponentId() const;
    void setOpponentId(const qint32 &opponent_id);
    bool is_opponent_id_Set() const;
    bool is_opponent_id_Valid() const;

    qint32 getOpposingPlayerId() const;
    void setOpposingPlayerId(const qint32 &opposing_player_id);
    bool is_opposing_player_id_Set() const;
    bool is_opposing_player_id_Valid() const;

    qint32 getPeriodId() const;
    void setPeriodId(const qint32 &period_id);
    bool is_period_id_Set() const;
    bool is_period_id_Valid() const;

    QString getPeriodName() const;
    void setPeriodName(const QString &period_name);
    bool is_period_name_Set() const;
    bool is_period_name_Valid() const;

    qint32 getPlayId() const;
    void setPlayId(const qint32 &play_id);
    bool is_play_id_Set() const;
    bool is_play_id_Valid() const;

    qint32 getPlayerId() const;
    void setPlayerId(const qint32 &player_id);
    bool is_player_id_Set() const;
    bool is_player_id_Valid() const;

    QString getPowerPlayTeam() const;
    void setPowerPlayTeam(const QString &power_play_team);
    bool is_power_play_team_Set() const;
    bool is_power_play_team_Valid() const;

    qint32 getPowerPlayTeamId() const;
    void setPowerPlayTeamId(const qint32 &power_play_team_id);
    bool is_power_play_team_id_Set() const;
    bool is_power_play_team_id_Valid() const;

    qint32 getSecondAssistedByPlayerId() const;
    void setSecondAssistedByPlayerId(const qint32 &second_assisted_by_player_id);
    bool is_second_assisted_by_player_id_Set() const;
    bool is_second_assisted_by_player_id_Valid() const;

    qint32 getSequence() const;
    void setSequence(const qint32 &sequence);
    bool is_sequence_Set() const;
    bool is_sequence_Valid() const;

    QString getTeam() const;
    void setTeam(const QString &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_away_team_score;
    bool m_away_team_score_isSet;
    bool m_away_team_score_isValid;

    QString m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    qint32 m_clock_minutes;
    bool m_clock_minutes_isSet;
    bool m_clock_minutes_isValid;

    qint32 m_clock_seconds;
    bool m_clock_seconds_isSet;
    bool m_clock_seconds_isValid;

    QString m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    qint32 m_first_assisted_by_player_id;
    bool m_first_assisted_by_player_id_isSet;
    bool m_first_assisted_by_player_id_isValid;

    qint32 m_home_team_score;
    bool m_home_team_score_isSet;
    bool m_home_team_score_isValid;

    QString m_opponent;
    bool m_opponent_isSet;
    bool m_opponent_isValid;

    qint32 m_opponent_id;
    bool m_opponent_id_isSet;
    bool m_opponent_id_isValid;

    qint32 m_opposing_player_id;
    bool m_opposing_player_id_isSet;
    bool m_opposing_player_id_isValid;

    qint32 m_period_id;
    bool m_period_id_isSet;
    bool m_period_id_isValid;

    QString m_period_name;
    bool m_period_name_isSet;
    bool m_period_name_isValid;

    qint32 m_play_id;
    bool m_play_id_isSet;
    bool m_play_id_isValid;

    qint32 m_player_id;
    bool m_player_id_isSet;
    bool m_player_id_isValid;

    QString m_power_play_team;
    bool m_power_play_team_isSet;
    bool m_power_play_team_isValid;

    qint32 m_power_play_team_id;
    bool m_power_play_team_id_isSet;
    bool m_power_play_team_id_isValid;

    qint32 m_second_assisted_by_player_id;
    bool m_second_assisted_by_player_id_isSet;
    bool m_second_assisted_by_player_id_isValid;

    qint32 m_sequence;
    bool m_sequence_isSet;
    bool m_sequence_isValid;

    QString m_team;
    bool m_team_isSet;
    bool m_team_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlay)

#endif // OAIPlay_H
