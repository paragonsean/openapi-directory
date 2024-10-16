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
 * OAIGoal.h
 *
 * 
 */

#ifndef OAIGoal_H
#define OAIGoal_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGoal : public OAIObject {
public:
    OAIGoal();
    OAIGoal(QString json);
    ~OAIGoal() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAssistedByPlayerId1() const;
    void setAssistedByPlayerId1(const qint32 &assisted_by_player_id1);
    bool is_assisted_by_player_id1_Set() const;
    bool is_assisted_by_player_id1_Valid() const;

    qint32 getAssistedByPlayerId2() const;
    void setAssistedByPlayerId2(const qint32 &assisted_by_player_id2);
    bool is_assisted_by_player_id2_Set() const;
    bool is_assisted_by_player_id2_Valid() const;

    QString getAssistedByPlayerName1() const;
    void setAssistedByPlayerName1(const QString &assisted_by_player_name1);
    bool is_assisted_by_player_name1_Set() const;
    bool is_assisted_by_player_name1_Valid() const;

    QString getAssistedByPlayerName2() const;
    void setAssistedByPlayerName2(const QString &assisted_by_player_name2);
    bool is_assisted_by_player_name2_Set() const;
    bool is_assisted_by_player_name2_Valid() const;

    qint32 getGameId() const;
    void setGameId(const qint32 &game_id);
    bool is_game_id_Set() const;
    bool is_game_id_Valid() const;

    qint32 getGameMinute() const;
    void setGameMinute(const qint32 &game_minute);
    bool is_game_minute_Set() const;
    bool is_game_minute_Valid() const;

    qint32 getGameMinuteExtra() const;
    void setGameMinuteExtra(const qint32 &game_minute_extra);
    bool is_game_minute_extra_Set() const;
    bool is_game_minute_extra_Valid() const;

    qint32 getGoalId() const;
    void setGoalId(const qint32 &goal_id);
    bool is_goal_id_Set() const;
    bool is_goal_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getPlayerId() const;
    void setPlayerId(const qint32 &player_id);
    bool is_player_id_Set() const;
    bool is_player_id_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_assisted_by_player_id1;
    bool m_assisted_by_player_id1_isSet;
    bool m_assisted_by_player_id1_isValid;

    qint32 m_assisted_by_player_id2;
    bool m_assisted_by_player_id2_isSet;
    bool m_assisted_by_player_id2_isValid;

    QString m_assisted_by_player_name1;
    bool m_assisted_by_player_name1_isSet;
    bool m_assisted_by_player_name1_isValid;

    QString m_assisted_by_player_name2;
    bool m_assisted_by_player_name2_isSet;
    bool m_assisted_by_player_name2_isValid;

    qint32 m_game_id;
    bool m_game_id_isSet;
    bool m_game_id_isValid;

    qint32 m_game_minute;
    bool m_game_minute_isSet;
    bool m_game_minute_isValid;

    qint32 m_game_minute_extra;
    bool m_game_minute_extra_isSet;
    bool m_game_minute_extra_isValid;

    qint32 m_goal_id;
    bool m_goal_id_isSet;
    bool m_goal_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_player_id;
    bool m_player_id_isSet;
    bool m_player_id_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGoal)

#endif // OAIGoal_H
