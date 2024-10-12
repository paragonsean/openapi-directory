/**
 * NFL v3 Play-by-Play
 * NFL play-by-play API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIScoringPlay.h
 *
 * 
 */

#ifndef OAIScoringPlay_H
#define OAIScoringPlay_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIScoringPlay : public OAIObject {
public:
    OAIScoringPlay();
    OAIScoringPlay(QString json);
    ~OAIScoringPlay() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAwayScore() const;
    void setAwayScore(const qint32 &away_score);
    bool is_away_score_Set() const;
    bool is_away_score_Valid() const;

    QString getAwayTeam() const;
    void setAwayTeam(const QString &away_team);
    bool is_away_team_Set() const;
    bool is_away_team_Valid() const;

    QString getDate() const;
    void setDate(const QString &date);
    bool is_date_Set() const;
    bool is_date_Valid() const;

    QString getGameKey() const;
    void setGameKey(const QString &game_key);
    bool is_game_key_Set() const;
    bool is_game_key_Valid() const;

    qint32 getHomeScore() const;
    void setHomeScore(const qint32 &home_score);
    bool is_home_score_Set() const;
    bool is_home_score_Valid() const;

    QString getHomeTeam() const;
    void setHomeTeam(const QString &home_team);
    bool is_home_team_Set() const;
    bool is_home_team_Valid() const;

    QString getPlayDescription() const;
    void setPlayDescription(const QString &play_description);
    bool is_play_description_Set() const;
    bool is_play_description_Valid() const;

    QString getQuarter() const;
    void setQuarter(const QString &quarter);
    bool is_quarter_Set() const;
    bool is_quarter_Valid() const;

    qint32 getScoreId() const;
    void setScoreId(const qint32 &score_id);
    bool is_score_id_Set() const;
    bool is_score_id_Valid() const;

    qint32 getScoringPlayId() const;
    void setScoringPlayId(const qint32 &scoring_play_id);
    bool is_scoring_play_id_Set() const;
    bool is_scoring_play_id_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    qint32 getSequence() const;
    void setSequence(const qint32 &sequence);
    bool is_sequence_Set() const;
    bool is_sequence_Valid() const;

    QString getTeam() const;
    void setTeam(const QString &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    QString getTimeRemaining() const;
    void setTimeRemaining(const QString &time_remaining);
    bool is_time_remaining_Set() const;
    bool is_time_remaining_Valid() const;

    qint32 getWeek() const;
    void setWeek(const qint32 &week);
    bool is_week_Set() const;
    bool is_week_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_away_score;
    bool m_away_score_isSet;
    bool m_away_score_isValid;

    QString m_away_team;
    bool m_away_team_isSet;
    bool m_away_team_isValid;

    QString m_date;
    bool m_date_isSet;
    bool m_date_isValid;

    QString m_game_key;
    bool m_game_key_isSet;
    bool m_game_key_isValid;

    qint32 m_home_score;
    bool m_home_score_isSet;
    bool m_home_score_isValid;

    QString m_home_team;
    bool m_home_team_isSet;
    bool m_home_team_isValid;

    QString m_play_description;
    bool m_play_description_isSet;
    bool m_play_description_isValid;

    QString m_quarter;
    bool m_quarter_isSet;
    bool m_quarter_isValid;

    qint32 m_score_id;
    bool m_score_id_isSet;
    bool m_score_id_isValid;

    qint32 m_scoring_play_id;
    bool m_scoring_play_id_isSet;
    bool m_scoring_play_id_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    qint32 m_sequence;
    bool m_sequence_isSet;
    bool m_sequence_isValid;

    QString m_team;
    bool m_team_isSet;
    bool m_team_isValid;

    QString m_time_remaining;
    bool m_time_remaining_isSet;
    bool m_time_remaining_isValid;

    qint32 m_week;
    bool m_week_isSet;
    bool m_week_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScoringPlay)

#endif // OAIScoringPlay_H
