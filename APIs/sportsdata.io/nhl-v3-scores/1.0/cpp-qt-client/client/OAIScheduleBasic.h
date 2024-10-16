/**
 * NHL v3 Scores
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIScheduleBasic.h
 *
 * 
 */

#ifndef OAIScheduleBasic_H
#define OAIScheduleBasic_H

#include <QJsonObject>

#include "OAISeries.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISeries;

class OAIScheduleBasic : public OAIObject {
public:
    OAIScheduleBasic();
    OAIScheduleBasic(QString json);
    ~OAIScheduleBasic() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAwayTeam() const;
    void setAwayTeam(const QString &away_team);
    bool is_away_team_Set() const;
    bool is_away_team_Valid() const;

    qint32 getAwayTeamId() const;
    void setAwayTeamId(const qint32 &away_team_id);
    bool is_away_team_id_Set() const;
    bool is_away_team_id_Valid() const;

    qint32 getAwayTeamScore() const;
    void setAwayTeamScore(const qint32 &away_team_score);
    bool is_away_team_score_Set() const;
    bool is_away_team_score_Valid() const;

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

    QString getHomeTeam() const;
    void setHomeTeam(const QString &home_team);
    bool is_home_team_Set() const;
    bool is_home_team_Valid() const;

    qint32 getHomeTeamId() const;
    void setHomeTeamId(const qint32 &home_team_id);
    bool is_home_team_id_Set() const;
    bool is_home_team_id_Valid() const;

    qint32 getHomeTeamScore() const;
    void setHomeTeamScore(const qint32 &home_team_score);
    bool is_home_team_score_Set() const;
    bool is_home_team_score_Valid() const;

    bool isIsClosed() const;
    void setIsClosed(const bool &is_closed);
    bool is_is_closed_Set() const;
    bool is_is_closed_Valid() const;

    bool isNeutralVenue() const;
    void setNeutralVenue(const bool &neutral_venue);
    bool is_neutral_venue_Set() const;
    bool is_neutral_venue_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    qint32 getSeasonType() const;
    void setSeasonType(const qint32 &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    OAISeries getSeriesInfo() const;
    void setSeriesInfo(const OAISeries &series_info);
    bool is_series_info_Set() const;
    bool is_series_info_Valid() const;

    qint32 getStadiumId() const;
    void setStadiumId(const qint32 &stadium_id);
    bool is_stadium_id_Set() const;
    bool is_stadium_id_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_away_team;
    bool m_away_team_isSet;
    bool m_away_team_isValid;

    qint32 m_away_team_id;
    bool m_away_team_id_isSet;
    bool m_away_team_id_isValid;

    qint32 m_away_team_score;
    bool m_away_team_score_isSet;
    bool m_away_team_score_isValid;

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

    qint32 m_global_away_team_id;
    bool m_global_away_team_id_isSet;
    bool m_global_away_team_id_isValid;

    qint32 m_global_game_id;
    bool m_global_game_id_isSet;
    bool m_global_game_id_isValid;

    qint32 m_global_home_team_id;
    bool m_global_home_team_id_isSet;
    bool m_global_home_team_id_isValid;

    QString m_home_team;
    bool m_home_team_isSet;
    bool m_home_team_isValid;

    qint32 m_home_team_id;
    bool m_home_team_id_isSet;
    bool m_home_team_id_isValid;

    qint32 m_home_team_score;
    bool m_home_team_score_isSet;
    bool m_home_team_score_isValid;

    bool m_is_closed;
    bool m_is_closed_isSet;
    bool m_is_closed_isValid;

    bool m_neutral_venue;
    bool m_neutral_venue_isSet;
    bool m_neutral_venue_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    qint32 m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;

    OAISeries m_series_info;
    bool m_series_info_isSet;
    bool m_series_info_isValid;

    qint32 m_stadium_id;
    bool m_stadium_id_isSet;
    bool m_stadium_id_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScheduleBasic)

#endif // OAIScheduleBasic_H
