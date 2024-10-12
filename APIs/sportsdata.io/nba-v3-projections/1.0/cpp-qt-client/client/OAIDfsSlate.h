/**
 * NBA v3 Projections
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDfsSlate.h
 *
 * 
 */

#ifndef OAIDfsSlate_H
#define OAIDfsSlate_H

#include <QJsonObject>

#include "OAIDfsSlateGame.h"
#include "OAIDfsSlatePlayer.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDfsSlateGame;
class OAIDfsSlatePlayer;

class OAIDfsSlate : public OAIObject {
public:
    OAIDfsSlate();
    OAIDfsSlate(QString json);
    ~OAIDfsSlate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIDfsSlateGame> getDfsSlateGames() const;
    void setDfsSlateGames(const QList<OAIDfsSlateGame> &dfs_slate_games);
    bool is_dfs_slate_games_Set() const;
    bool is_dfs_slate_games_Valid() const;

    QList<OAIDfsSlatePlayer> getDfsSlatePlayers() const;
    void setDfsSlatePlayers(const QList<OAIDfsSlatePlayer> &dfs_slate_players);
    bool is_dfs_slate_players_Set() const;
    bool is_dfs_slate_players_Valid() const;

    bool isIsMultiDaySlate() const;
    void setIsMultiDaySlate(const bool &is_multi_day_slate);
    bool is_is_multi_day_slate_Set() const;
    bool is_is_multi_day_slate_Valid() const;

    qint32 getNumberOfGames() const;
    void setNumberOfGames(const qint32 &number_of_games);
    bool is_number_of_games_Set() const;
    bool is_number_of_games_Valid() const;

    QString getROperator() const;
    void setROperator(const QString &r_operator);
    bool is_r_operator_Set() const;
    bool is_r_operator_Valid() const;

    QString getOperatorDay() const;
    void setOperatorDay(const QString &operator_day);
    bool is_operator_day_Set() const;
    bool is_operator_day_Valid() const;

    QString getOperatorGameType() const;
    void setOperatorGameType(const QString &operator_game_type);
    bool is_operator_game_type_Set() const;
    bool is_operator_game_type_Valid() const;

    QString getOperatorName() const;
    void setOperatorName(const QString &operator_name);
    bool is_operator_name_Set() const;
    bool is_operator_name_Valid() const;

    qint32 getOperatorSlateId() const;
    void setOperatorSlateId(const qint32 &operator_slate_id);
    bool is_operator_slate_id_Set() const;
    bool is_operator_slate_id_Valid() const;

    QString getOperatorStartTime() const;
    void setOperatorStartTime(const QString &operator_start_time);
    bool is_operator_start_time_Set() const;
    bool is_operator_start_time_Valid() const;

    bool isRemovedByOperator() const;
    void setRemovedByOperator(const bool &removed_by_operator);
    bool is_removed_by_operator_Set() const;
    bool is_removed_by_operator_Valid() const;

    qint32 getSalaryCap() const;
    void setSalaryCap(const qint32 &salary_cap);
    bool is_salary_cap_Set() const;
    bool is_salary_cap_Valid() const;

    qint32 getSlateId() const;
    void setSlateId(const qint32 &slate_id);
    bool is_slate_id_Set() const;
    bool is_slate_id_Valid() const;

    QList<QString> getSlateRosterSlots() const;
    void setSlateRosterSlots(const QList<QString> &slate_roster_slots);
    bool is_slate_roster_slots_Set() const;
    bool is_slate_roster_slots_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIDfsSlateGame> m_dfs_slate_games;
    bool m_dfs_slate_games_isSet;
    bool m_dfs_slate_games_isValid;

    QList<OAIDfsSlatePlayer> m_dfs_slate_players;
    bool m_dfs_slate_players_isSet;
    bool m_dfs_slate_players_isValid;

    bool m_is_multi_day_slate;
    bool m_is_multi_day_slate_isSet;
    bool m_is_multi_day_slate_isValid;

    qint32 m_number_of_games;
    bool m_number_of_games_isSet;
    bool m_number_of_games_isValid;

    QString m_r_operator;
    bool m_r_operator_isSet;
    bool m_r_operator_isValid;

    QString m_operator_day;
    bool m_operator_day_isSet;
    bool m_operator_day_isValid;

    QString m_operator_game_type;
    bool m_operator_game_type_isSet;
    bool m_operator_game_type_isValid;

    QString m_operator_name;
    bool m_operator_name_isSet;
    bool m_operator_name_isValid;

    qint32 m_operator_slate_id;
    bool m_operator_slate_id_isSet;
    bool m_operator_slate_id_isValid;

    QString m_operator_start_time;
    bool m_operator_start_time_isSet;
    bool m_operator_start_time_isValid;

    bool m_removed_by_operator;
    bool m_removed_by_operator_isSet;
    bool m_removed_by_operator_isValid;

    qint32 m_salary_cap;
    bool m_salary_cap_isSet;
    bool m_salary_cap_isValid;

    qint32 m_slate_id;
    bool m_slate_id_isSet;
    bool m_slate_id_isValid;

    QList<QString> m_slate_roster_slots;
    bool m_slate_roster_slots_isSet;
    bool m_slate_roster_slots_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDfsSlate)

#endif // OAIDfsSlate_H
