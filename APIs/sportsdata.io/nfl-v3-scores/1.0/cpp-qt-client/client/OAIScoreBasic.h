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
 * OAIScoreBasic.h
 *
 * 
 */

#ifndef OAIScoreBasic_H
#define OAIScoreBasic_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIScoreBasic : public OAIObject {
public:
    OAIScoreBasic();
    OAIScoreBasic(QString json);
    ~OAIScoreBasic() override;

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

    qint32 getAwayTeamId() const;
    void setAwayTeamId(const qint32 &away_team_id);
    bool is_away_team_id_Set() const;
    bool is_away_team_id_Valid() const;

    bool isCanceled() const;
    void setCanceled(const bool &canceled);
    bool is_canceled_Set() const;
    bool is_canceled_Valid() const;

    bool isClosed() const;
    void setClosed(const bool &closed);
    bool is_closed_Set() const;
    bool is_closed_Valid() const;

    QString getDate() const;
    void setDate(const QString &date);
    bool is_date_Set() const;
    bool is_date_Valid() const;

    QString getDateTime() const;
    void setDateTime(const QString &date_time);
    bool is_date_time_Set() const;
    bool is_date_time_Valid() const;

    QString getDateTimeUtc() const;
    void setDateTimeUtc(const QString &date_time_utc);
    bool is_date_time_utc_Set() const;
    bool is_date_time_utc_Valid() const;

    QString getDay() const;
    void setDay(const QString &day);
    bool is_day_Set() const;
    bool is_day_Valid() const;

    QString getGameEndDateTime() const;
    void setGameEndDateTime(const QString &game_end_date_time);
    bool is_game_end_date_time_Set() const;
    bool is_game_end_date_time_Valid() const;

    qint32 getGameId() const;
    void setGameId(const qint32 &game_id);
    bool is_game_id_Set() const;
    bool is_game_id_Valid() const;

    QString getGameKey() const;
    void setGameKey(const QString &game_key);
    bool is_game_key_Set() const;
    bool is_game_key_Valid() const;

    qint32 getGlobalAwayTeamId() const;
    void setGlobalAwayTeamId(const qint32 &global_away_team_id);
    bool is_global_away_team_id_Set() const;
    bool is_global_away_team_id_Valid() const;

    qint32 getGlobalGameId() const;
    void setGlobalGameId(const qint32 &global_game_id);
    bool is_global_game_id_Set() const;
    bool is_global_game_id_Valid() const;

    qint32 getGlobalHomeTeamId() const;
    void setGlobalHomeTeamId(const qint32 &global_home_team_id);
    bool is_global_home_team_id_Set() const;
    bool is_global_home_team_id_Valid() const;

    qint32 getHomeScore() const;
    void setHomeScore(const qint32 &home_score);
    bool is_home_score_Set() const;
    bool is_home_score_Valid() const;

    QString getHomeTeam() const;
    void setHomeTeam(const QString &home_team);
    bool is_home_team_Set() const;
    bool is_home_team_Valid() const;

    qint32 getHomeTeamId() const;
    void setHomeTeamId(const qint32 &home_team_id);
    bool is_home_team_id_Set() const;
    bool is_home_team_id_Valid() const;

    QString getLastUpdated() const;
    void setLastUpdated(const QString &last_updated);
    bool is_last_updated_Set() const;
    bool is_last_updated_Valid() const;

    QString getQuarter() const;
    void setQuarter(const QString &quarter);
    bool is_quarter_Set() const;
    bool is_quarter_Valid() const;

    QString getQuarterDescription() const;
    void setQuarterDescription(const QString &quarter_description);
    bool is_quarter_description_Set() const;
    bool is_quarter_description_Valid() const;

    qint32 getScoreId() const;
    void setScoreId(const qint32 &score_id);
    bool is_score_id_Set() const;
    bool is_score_id_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    qint32 getStadiumId() const;
    void setStadiumId(const qint32 &stadium_id);
    bool is_stadium_id_Set() const;
    bool is_stadium_id_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

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

    qint32 m_away_team_id;
    bool m_away_team_id_isSet;
    bool m_away_team_id_isValid;

    bool m_canceled;
    bool m_canceled_isSet;
    bool m_canceled_isValid;

    bool m_closed;
    bool m_closed_isSet;
    bool m_closed_isValid;

    QString m_date;
    bool m_date_isSet;
    bool m_date_isValid;

    QString m_date_time;
    bool m_date_time_isSet;
    bool m_date_time_isValid;

    QString m_date_time_utc;
    bool m_date_time_utc_isSet;
    bool m_date_time_utc_isValid;

    QString m_day;
    bool m_day_isSet;
    bool m_day_isValid;

    QString m_game_end_date_time;
    bool m_game_end_date_time_isSet;
    bool m_game_end_date_time_isValid;

    qint32 m_game_id;
    bool m_game_id_isSet;
    bool m_game_id_isValid;

    QString m_game_key;
    bool m_game_key_isSet;
    bool m_game_key_isValid;

    qint32 m_global_away_team_id;
    bool m_global_away_team_id_isSet;
    bool m_global_away_team_id_isValid;

    qint32 m_global_game_id;
    bool m_global_game_id_isSet;
    bool m_global_game_id_isValid;

    qint32 m_global_home_team_id;
    bool m_global_home_team_id_isSet;
    bool m_global_home_team_id_isValid;

    qint32 m_home_score;
    bool m_home_score_isSet;
    bool m_home_score_isValid;

    QString m_home_team;
    bool m_home_team_isSet;
    bool m_home_team_isValid;

    qint32 m_home_team_id;
    bool m_home_team_id_isSet;
    bool m_home_team_id_isValid;

    QString m_last_updated;
    bool m_last_updated_isSet;
    bool m_last_updated_isValid;

    QString m_quarter;
    bool m_quarter_isSet;
    bool m_quarter_isValid;

    QString m_quarter_description;
    bool m_quarter_description_isSet;
    bool m_quarter_description_isValid;

    qint32 m_score_id;
    bool m_score_id_isSet;
    bool m_score_id_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    qint32 m_stadium_id;
    bool m_stadium_id_isSet;
    bool m_stadium_id_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_time_remaining;
    bool m_time_remaining_isSet;
    bool m_time_remaining_isValid;

    qint32 m_week;
    bool m_week_isSet;
    bool m_week_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScoreBasic)

#endif // OAIScoreBasic_H
