/**
 * MLB v3 Scores
 * MLB scores API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITeam.h
 *
 * 
 */

#ifndef OAITeam_H
#define OAITeam_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITeam : public OAIObject {
public:
    OAITeam();
    OAITeam(QString json);
    ~OAITeam() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isActive() const;
    void setActive(const bool &active);
    bool is_active_Set() const;
    bool is_active_Valid() const;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    QString getDivision() const;
    void setDivision(const QString &division);
    bool is_division_Set() const;
    bool is_division_Valid() const;

    qint32 getGlobalTeamId() const;
    void setGlobalTeamId(const qint32 &global_team_id);
    bool is_global_team_id_Set() const;
    bool is_global_team_id_Valid() const;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    QString getLeague() const;
    void setLeague(const QString &league);
    bool is_league_Set() const;
    bool is_league_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPrimaryColor() const;
    void setPrimaryColor(const QString &primary_color);
    bool is_primary_color_Set() const;
    bool is_primary_color_Valid() const;

    QString getQuaternaryColor() const;
    void setQuaternaryColor(const QString &quaternary_color);
    bool is_quaternary_color_Set() const;
    bool is_quaternary_color_Valid() const;

    QString getSecondaryColor() const;
    void setSecondaryColor(const QString &secondary_color);
    bool is_secondary_color_Set() const;
    bool is_secondary_color_Valid() const;

    qint32 getStadiumId() const;
    void setStadiumId(const qint32 &stadium_id);
    bool is_stadium_id_Set() const;
    bool is_stadium_id_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    QString getTertiaryColor() const;
    void setTertiaryColor(const QString &tertiary_color);
    bool is_tertiary_color_Set() const;
    bool is_tertiary_color_Valid() const;

    QString getWikipediaLogoUrl() const;
    void setWikipediaLogoUrl(const QString &wikipedia_logo_url);
    bool is_wikipedia_logo_url_Set() const;
    bool is_wikipedia_logo_url_Valid() const;

    QString getWikipediaWordMarkUrl() const;
    void setWikipediaWordMarkUrl(const QString &wikipedia_word_mark_url);
    bool is_wikipedia_word_mark_url_Set() const;
    bool is_wikipedia_word_mark_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_active;
    bool m_active_isSet;
    bool m_active_isValid;

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    QString m_division;
    bool m_division_isSet;
    bool m_division_isValid;

    qint32 m_global_team_id;
    bool m_global_team_id_isSet;
    bool m_global_team_id_isValid;

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;

    QString m_league;
    bool m_league_isSet;
    bool m_league_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_primary_color;
    bool m_primary_color_isSet;
    bool m_primary_color_isValid;

    QString m_quaternary_color;
    bool m_quaternary_color_isSet;
    bool m_quaternary_color_isValid;

    QString m_secondary_color;
    bool m_secondary_color_isSet;
    bool m_secondary_color_isValid;

    qint32 m_stadium_id;
    bool m_stadium_id_isSet;
    bool m_stadium_id_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    QString m_tertiary_color;
    bool m_tertiary_color_isSet;
    bool m_tertiary_color_isValid;

    QString m_wikipedia_logo_url;
    bool m_wikipedia_logo_url_isSet;
    bool m_wikipedia_logo_url_isValid;

    QString m_wikipedia_word_mark_url;
    bool m_wikipedia_word_mark_url_isSet;
    bool m_wikipedia_word_mark_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITeam)

#endif // OAITeam_H
