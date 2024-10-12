/**
 * Soccer v3 Scores
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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

    QString getBirthCountry() const;
    void setBirthCountry(const QString &birth_country);
    bool is_birth_country_Set() const;
    bool is_birth_country_Valid() const;

    QString getBirthDate() const;
    void setBirthDate(const QString &birth_date);
    bool is_birth_date_Set() const;
    bool is_birth_date_Valid() const;

    QString getCommonName() const;
    void setCommonName(const QString &common_name);
    bool is_common_name_Set() const;
    bool is_common_name_Valid() const;

    QString getDraftKingsPosition() const;
    void setDraftKingsPosition(const QString &draft_kings_position);
    bool is_draft_kings_position_Set() const;
    bool is_draft_kings_position_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getFoot() const;
    void setFoot(const QString &foot);
    bool is_foot_Set() const;
    bool is_foot_Valid() const;

    QString getGender() const;
    void setGender(const QString &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

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

    QString getNationality() const;
    void setNationality(const QString &nationality);
    bool is_nationality_Set() const;
    bool is_nationality_Valid() const;

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

    qint32 getRotoWirePlayerId() const;
    void setRotoWirePlayerId(const qint32 &roto_wire_player_id);
    bool is_roto_wire_player_id_Set() const;
    bool is_roto_wire_player_id_Valid() const;

    QString getShortName() const;
    void setShortName(const QString &short_name);
    bool is_short_name_Set() const;
    bool is_short_name_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

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

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_birth_city;
    bool m_birth_city_isSet;
    bool m_birth_city_isValid;

    QString m_birth_country;
    bool m_birth_country_isSet;
    bool m_birth_country_isValid;

    QString m_birth_date;
    bool m_birth_date_isSet;
    bool m_birth_date_isValid;

    QString m_common_name;
    bool m_common_name_isSet;
    bool m_common_name_isValid;

    QString m_draft_kings_position;
    bool m_draft_kings_position_isSet;
    bool m_draft_kings_position_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_foot;
    bool m_foot_isSet;
    bool m_foot_isValid;

    QString m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

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

    QString m_nationality;
    bool m_nationality_isSet;
    bool m_nationality_isValid;

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

    qint32 m_roto_wire_player_id;
    bool m_roto_wire_player_id_isSet;
    bool m_roto_wire_player_id_isValid;

    QString m_short_name;
    bool m_short_name_isSet;
    bool m_short_name_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;

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
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlayer)

#endif // OAIPlayer_H
