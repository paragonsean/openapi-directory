/**
 * CFB v3 Scores
 * CFB schedules, scores, team stats, odds, weather, and news API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPlayer.h
 *
 * 
 */

#ifndef OAIPlayer_H
#define OAIPlayer_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPlayer : public OAIObject {
public:
    OAIPlayer();
    OAIPlayer(QString json);
    ~OAIPlayer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBirthCity() const;
    void setBirthCity(const QString &birth_city);
    bool is_birth_city_Set() const;
    bool is_birth_city_Valid() const;

    QString getBirthState() const;
    void setBirthState(const QString &birth_state);
    bool is_birth_state_Set() const;
    bool is_birth_state_Valid() const;

    QString getRClass() const;
    void setRClass(const QString &r_class);
    bool is_r_class_Set() const;
    bool is_r_class_Valid() const;

    QString getCreated() const;
    void setCreated(const QString &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    qint32 getGlobalTeamId() const;
    void setGlobalTeamId(const qint32 &global_team_id);
    bool is_global_team_id_Set() const;
    bool is_global_team_id_Valid() const;

    qint32 getHeight() const;
    void setHeight(const qint32 &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    QString getInjuryBodyPart() const;
    void setInjuryBodyPart(const QString &injury_body_part);
    bool is_injury_body_part_Set() const;
    bool is_injury_body_part_Valid() const;

    QString getInjuryNotes() const;
    void setInjuryNotes(const QString &injury_notes);
    bool is_injury_notes_Set() const;
    bool is_injury_notes_Valid() const;

    QString getInjuryStartDate() const;
    void setInjuryStartDate(const QString &injury_start_date);
    bool is_injury_start_date_Set() const;
    bool is_injury_start_date_Valid() const;

    QString getInjuryStatus() const;
    void setInjuryStatus(const QString &injury_status);
    bool is_injury_status_Set() const;
    bool is_injury_status_Valid() const;

    qint32 getJersey() const;
    void setJersey(const qint32 &jersey);
    bool is_jersey_Set() const;
    bool is_jersey_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

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

    QString getTeam() const;
    void setTeam(const QString &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    qint32 getWeight() const;
    void setWeight(const qint32 &weight);
    bool is_weight_Set() const;
    bool is_weight_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_birth_city;
    bool m_birth_city_isSet;
    bool m_birth_city_isValid;

    QString m_birth_state;
    bool m_birth_state_isSet;
    bool m_birth_state_isValid;

    QString m_r_class;
    bool m_r_class_isSet;
    bool m_r_class_isValid;

    QString m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    qint32 m_global_team_id;
    bool m_global_team_id_isSet;
    bool m_global_team_id_isValid;

    qint32 m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    QString m_injury_body_part;
    bool m_injury_body_part_isSet;
    bool m_injury_body_part_isValid;

    QString m_injury_notes;
    bool m_injury_notes_isSet;
    bool m_injury_notes_isValid;

    QString m_injury_start_date;
    bool m_injury_start_date_isSet;
    bool m_injury_start_date_isValid;

    QString m_injury_status;
    bool m_injury_status_isSet;
    bool m_injury_status_isValid;

    qint32 m_jersey;
    bool m_jersey_isSet;
    bool m_jersey_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    qint32 m_player_id;
    bool m_player_id_isSet;
    bool m_player_id_isValid;

    QString m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_position_category;
    bool m_position_category_isSet;
    bool m_position_category_isValid;

    QString m_team;
    bool m_team_isSet;
    bool m_team_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;

    qint32 m_weight;
    bool m_weight_isSet;
    bool m_weight_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlayer)

#endif // OAIPlayer_H
