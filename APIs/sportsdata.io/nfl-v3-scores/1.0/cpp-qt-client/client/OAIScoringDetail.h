/**
 * NFL v3 Scores
 * NFL schedules, scores, odds, weather, and news API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIScoringDetail.h
 *
 * 
 */

#ifndef OAIScoringDetail_H
#define OAIScoringDetail_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIScoringDetail : public OAIObject {
public:
    OAIScoringDetail();
    OAIScoringDetail(QString json);
    ~OAIScoringDetail() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getGameKey() const;
    void setGameKey(const QString &game_key);
    bool is_game_key_Set() const;
    bool is_game_key_Valid() const;

    qint32 getLength() const;
    void setLength(const qint32 &length);
    bool is_length_Set() const;
    bool is_length_Valid() const;

    qint32 getPlayerGameId() const;
    void setPlayerGameId(const qint32 &player_game_id);
    bool is_player_game_id_Set() const;
    bool is_player_game_id_Valid() const;

    qint32 getPlayerId() const;
    void setPlayerId(const qint32 &player_id);
    bool is_player_id_Set() const;
    bool is_player_id_Valid() const;

    qint32 getScoreId() const;
    void setScoreId(const qint32 &score_id);
    bool is_score_id_Set() const;
    bool is_score_id_Valid() const;

    qint32 getScoringDetailId() const;
    void setScoringDetailId(const qint32 &scoring_detail_id);
    bool is_scoring_detail_id_Set() const;
    bool is_scoring_detail_id_Valid() const;

    qint32 getScoringPlayId() const;
    void setScoringPlayId(const qint32 &scoring_play_id);
    bool is_scoring_play_id_Set() const;
    bool is_scoring_play_id_Valid() const;

    QString getScoringType() const;
    void setScoringType(const QString &scoring_type);
    bool is_scoring_type_Set() const;
    bool is_scoring_type_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    QString getTeam() const;
    void setTeam(const QString &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    qint32 getWeek() const;
    void setWeek(const qint32 &week);
    bool is_week_Set() const;
    bool is_week_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_game_key;
    bool m_game_key_isSet;
    bool m_game_key_isValid;

    qint32 m_length;
    bool m_length_isSet;
    bool m_length_isValid;

    qint32 m_player_game_id;
    bool m_player_game_id_isSet;
    bool m_player_game_id_isValid;

    qint32 m_player_id;
    bool m_player_id_isSet;
    bool m_player_id_isValid;

    qint32 m_score_id;
    bool m_score_id_isSet;
    bool m_score_id_isValid;

    qint32 m_scoring_detail_id;
    bool m_scoring_detail_id_isSet;
    bool m_scoring_detail_id_isValid;

    qint32 m_scoring_play_id;
    bool m_scoring_play_id_isSet;
    bool m_scoring_play_id_isValid;

    QString m_scoring_type;
    bool m_scoring_type_isSet;
    bool m_scoring_type_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    QString m_team;
    bool m_team_isSet;
    bool m_team_isValid;

    qint32 m_week;
    bool m_week_isSet;
    bool m_week_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScoringDetail)

#endif // OAIScoringDetail_H
