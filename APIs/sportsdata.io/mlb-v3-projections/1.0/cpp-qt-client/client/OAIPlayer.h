/**
 * MLB v3 Projections
 * MLB projections API.
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

    QString getBatHand() const;
    void setBatHand(const QString &bat_hand);
    bool is_bat_hand_Set() const;
    bool is_bat_hand_Valid() const;

    QString getBirthCity() const;
    void setBirthCity(const QString &birth_city);
    bool is_birth_city_Set() const;
    bool is_birth_city_Valid() const;

    QString getBirthCountry() const;
    void setBirthCountry(const QString &birth_country);
    bool is_birth_country_Set() const;
    bool is_birth_country_Valid() const;

    QString getBirthDate() const;
    void setBirthDate(const QString &birth_date);
    bool is_birth_date_Set() const;
    bool is_birth_date_Valid() const;

    QString getBirthState() const;
    void setBirthState(const QString &birth_state);
    bool is_birth_state_Set() const;
    bool is_birth_state_Valid() const;

    QString getCollege() const;
    void setCollege(const QString &college);
    bool is_college_Set() const;
    bool is_college_Valid() const;

    QString getDraftKingsName() const;
    void setDraftKingsName(const QString &draft_kings_name);
    bool is_draft_kings_name_Set() const;
    bool is_draft_kings_name_Valid() const;

    qint32 getDraftKingsPlayerId() const;
    void setDraftKingsPlayerId(const qint32 &draft_kings_player_id);
    bool is_draft_kings_player_id_Set() const;
    bool is_draft_kings_player_id_Valid() const;

    QString getExperience() const;
    void setExperience(const QString &experience);
    bool is_experience_Set() const;
    bool is_experience_Valid() const;

    QString getFanDuelName() const;
    void setFanDuelName(const QString &fan_duel_name);
    bool is_fan_duel_name_Set() const;
    bool is_fan_duel_name_Valid() const;

    qint32 getFanDuelPlayerId() const;
    void setFanDuelPlayerId(const qint32 &fan_duel_player_id);
    bool is_fan_duel_player_id_Set() const;
    bool is_fan_duel_player_id_Valid() const;

    qint32 getFantasyAlarmPlayerId() const;
    void setFantasyAlarmPlayerId(const qint32 &fantasy_alarm_player_id);
    bool is_fantasy_alarm_player_id_Set() const;
    bool is_fantasy_alarm_player_id_Valid() const;

    QString getFantasyDraftName() const;
    void setFantasyDraftName(const QString &fantasy_draft_name);
    bool is_fantasy_draft_name_Set() const;
    bool is_fantasy_draft_name_Valid() const;

    qint32 getFantasyDraftPlayerId() const;
    void setFantasyDraftPlayerId(const qint32 &fantasy_draft_player_id);
    bool is_fantasy_draft_player_id_Set() const;
    bool is_fantasy_draft_player_id_Valid() const;

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

    QString getHighSchool() const;
    void setHighSchool(const QString &high_school);
    bool is_high_school_Set() const;
    bool is_high_school_Valid() const;

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

    qint32 getMlbamid() const;
    void setMlbamid(const qint32 &mlbamid);
    bool is_mlbamid_Set() const;
    bool is_mlbamid_Valid() const;

    QString getPhotoUrl() const;
    void setPhotoUrl(const QString &photo_url);
    bool is_photo_url_Set() const;
    bool is_photo_url_Valid() const;

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

    QString getProDebut() const;
    void setProDebut(const QString &pro_debut);
    bool is_pro_debut_Set() const;
    bool is_pro_debut_Valid() const;

    qint32 getRotoWirePlayerId() const;
    void setRotoWirePlayerId(const qint32 &roto_wire_player_id);
    bool is_roto_wire_player_id_Set() const;
    bool is_roto_wire_player_id_Valid() const;

    qint32 getRotoworldPlayerId() const;
    void setRotoworldPlayerId(const qint32 &rotoworld_player_id);
    bool is_rotoworld_player_id_Set() const;
    bool is_rotoworld_player_id_Valid() const;

    qint32 getSalary() const;
    void setSalary(const qint32 &salary);
    bool is_salary_Set() const;
    bool is_salary_Valid() const;

    QString getSportRadarPlayerId() const;
    void setSportRadarPlayerId(const QString &sport_radar_player_id);
    bool is_sport_radar_player_id_Set() const;
    bool is_sport_radar_player_id_Valid() const;

    QString getSportsDataId() const;
    void setSportsDataId(const QString &sports_data_id);
    bool is_sports_data_id_Set() const;
    bool is_sports_data_id_Valid() const;

    qint32 getSportsDirectPlayerId() const;
    void setSportsDirectPlayerId(const qint32 &sports_direct_player_id);
    bool is_sports_direct_player_id_Set() const;
    bool is_sports_direct_player_id_Valid() const;

    qint32 getStatsPlayerId() const;
    void setStatsPlayerId(const qint32 &stats_player_id);
    bool is_stats_player_id_Set() const;
    bool is_stats_player_id_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getTeam() const;
    void setTeam(const QString &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    QString getThrowHand() const;
    void setThrowHand(const QString &throw_hand);
    bool is_throw_hand_Set() const;
    bool is_throw_hand_Valid() const;

    qint32 getUpcomingGameId() const;
    void setUpcomingGameId(const qint32 &upcoming_game_id);
    bool is_upcoming_game_id_Set() const;
    bool is_upcoming_game_id_Valid() const;

    QString getUsaTodayHeadshotNoBackgroundUpdated() const;
    void setUsaTodayHeadshotNoBackgroundUpdated(const QString &usa_today_headshot_no_background_updated);
    bool is_usa_today_headshot_no_background_updated_Set() const;
    bool is_usa_today_headshot_no_background_updated_Valid() const;

    QString getUsaTodayHeadshotNoBackgroundUrl() const;
    void setUsaTodayHeadshotNoBackgroundUrl(const QString &usa_today_headshot_no_background_url);
    bool is_usa_today_headshot_no_background_url_Set() const;
    bool is_usa_today_headshot_no_background_url_Valid() const;

    QString getUsaTodayHeadshotUpdated() const;
    void setUsaTodayHeadshotUpdated(const QString &usa_today_headshot_updated);
    bool is_usa_today_headshot_updated_Set() const;
    bool is_usa_today_headshot_updated_Valid() const;

    QString getUsaTodayHeadshotUrl() const;
    void setUsaTodayHeadshotUrl(const QString &usa_today_headshot_url);
    bool is_usa_today_headshot_url_Set() const;
    bool is_usa_today_headshot_url_Valid() const;

    qint32 getUsaTodayPlayerId() const;
    void setUsaTodayPlayerId(const qint32 &usa_today_player_id);
    bool is_usa_today_player_id_Set() const;
    bool is_usa_today_player_id_Valid() const;

    qint32 getWeight() const;
    void setWeight(const qint32 &weight);
    bool is_weight_Set() const;
    bool is_weight_Valid() const;

    qint32 getXmlTeamPlayerId() const;
    void setXmlTeamPlayerId(const qint32 &xml_team_player_id);
    bool is_xml_team_player_id_Set() const;
    bool is_xml_team_player_id_Valid() const;

    QString getYahooName() const;
    void setYahooName(const QString &yahoo_name);
    bool is_yahoo_name_Set() const;
    bool is_yahoo_name_Valid() const;

    qint32 getYahooPlayerId() const;
    void setYahooPlayerId(const qint32 &yahoo_player_id);
    bool is_yahoo_player_id_Set() const;
    bool is_yahoo_player_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_bat_hand;
    bool m_bat_hand_isSet;
    bool m_bat_hand_isValid;

    QString m_birth_city;
    bool m_birth_city_isSet;
    bool m_birth_city_isValid;

    QString m_birth_country;
    bool m_birth_country_isSet;
    bool m_birth_country_isValid;

    QString m_birth_date;
    bool m_birth_date_isSet;
    bool m_birth_date_isValid;

    QString m_birth_state;
    bool m_birth_state_isSet;
    bool m_birth_state_isValid;

    QString m_college;
    bool m_college_isSet;
    bool m_college_isValid;

    QString m_draft_kings_name;
    bool m_draft_kings_name_isSet;
    bool m_draft_kings_name_isValid;

    qint32 m_draft_kings_player_id;
    bool m_draft_kings_player_id_isSet;
    bool m_draft_kings_player_id_isValid;

    QString m_experience;
    bool m_experience_isSet;
    bool m_experience_isValid;

    QString m_fan_duel_name;
    bool m_fan_duel_name_isSet;
    bool m_fan_duel_name_isValid;

    qint32 m_fan_duel_player_id;
    bool m_fan_duel_player_id_isSet;
    bool m_fan_duel_player_id_isValid;

    qint32 m_fantasy_alarm_player_id;
    bool m_fantasy_alarm_player_id_isSet;
    bool m_fantasy_alarm_player_id_isValid;

    QString m_fantasy_draft_name;
    bool m_fantasy_draft_name_isSet;
    bool m_fantasy_draft_name_isValid;

    qint32 m_fantasy_draft_player_id;
    bool m_fantasy_draft_player_id_isSet;
    bool m_fantasy_draft_player_id_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    qint32 m_global_team_id;
    bool m_global_team_id_isSet;
    bool m_global_team_id_isValid;

    qint32 m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    QString m_high_school;
    bool m_high_school_isSet;
    bool m_high_school_isValid;

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

    qint32 m_mlbamid;
    bool m_mlbamid_isSet;
    bool m_mlbamid_isValid;

    QString m_photo_url;
    bool m_photo_url_isSet;
    bool m_photo_url_isValid;

    qint32 m_player_id;
    bool m_player_id_isSet;
    bool m_player_id_isValid;

    QString m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_position_category;
    bool m_position_category_isSet;
    bool m_position_category_isValid;

    QString m_pro_debut;
    bool m_pro_debut_isSet;
    bool m_pro_debut_isValid;

    qint32 m_roto_wire_player_id;
    bool m_roto_wire_player_id_isSet;
    bool m_roto_wire_player_id_isValid;

    qint32 m_rotoworld_player_id;
    bool m_rotoworld_player_id_isSet;
    bool m_rotoworld_player_id_isValid;

    qint32 m_salary;
    bool m_salary_isSet;
    bool m_salary_isValid;

    QString m_sport_radar_player_id;
    bool m_sport_radar_player_id_isSet;
    bool m_sport_radar_player_id_isValid;

    QString m_sports_data_id;
    bool m_sports_data_id_isSet;
    bool m_sports_data_id_isValid;

    qint32 m_sports_direct_player_id;
    bool m_sports_direct_player_id_isSet;
    bool m_sports_direct_player_id_isValid;

    qint32 m_stats_player_id;
    bool m_stats_player_id_isSet;
    bool m_stats_player_id_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_team;
    bool m_team_isSet;
    bool m_team_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    QString m_throw_hand;
    bool m_throw_hand_isSet;
    bool m_throw_hand_isValid;

    qint32 m_upcoming_game_id;
    bool m_upcoming_game_id_isSet;
    bool m_upcoming_game_id_isValid;

    QString m_usa_today_headshot_no_background_updated;
    bool m_usa_today_headshot_no_background_updated_isSet;
    bool m_usa_today_headshot_no_background_updated_isValid;

    QString m_usa_today_headshot_no_background_url;
    bool m_usa_today_headshot_no_background_url_isSet;
    bool m_usa_today_headshot_no_background_url_isValid;

    QString m_usa_today_headshot_updated;
    bool m_usa_today_headshot_updated_isSet;
    bool m_usa_today_headshot_updated_isValid;

    QString m_usa_today_headshot_url;
    bool m_usa_today_headshot_url_isSet;
    bool m_usa_today_headshot_url_isValid;

    qint32 m_usa_today_player_id;
    bool m_usa_today_player_id_isSet;
    bool m_usa_today_player_id_isValid;

    qint32 m_weight;
    bool m_weight_isSet;
    bool m_weight_isValid;

    qint32 m_xml_team_player_id;
    bool m_xml_team_player_id_isSet;
    bool m_xml_team_player_id_isValid;

    QString m_yahoo_name;
    bool m_yahoo_name_isSet;
    bool m_yahoo_name_isValid;

    qint32 m_yahoo_player_id;
    bool m_yahoo_player_id_isSet;
    bool m_yahoo_player_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlayer)

#endif // OAIPlayer_H
