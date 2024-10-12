/**
 * LoL v3 Stats
 * LoL v3 Stats
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

    qint32 getAreaId() const;
    void setAreaId(const qint32 &area_id);
    bool is_area_id_Set() const;
    bool is_area_id_Valid() const;

    QString getAreaName() const;
    void setAreaName(const QString &area_name);
    bool is_area_name_Set() const;
    bool is_area_name_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getFacebook() const;
    void setFacebook(const QString &facebook);
    bool is_facebook_Set() const;
    bool is_facebook_Valid() const;

    qint32 getFounded() const;
    void setFounded(const qint32 &founded);
    bool is_founded_Set() const;
    bool is_founded_Valid() const;

    QString getGender() const;
    void setGender(const QString &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    QString getInstagram() const;
    void setInstagram(const QString &instagram);
    bool is_instagram_Set() const;
    bool is_instagram_Valid() const;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

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

    QString getShortName() const;
    void setShortName(const QString &short_name);
    bool is_short_name_Set() const;
    bool is_short_name_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    QString getTertiaryColor() const;
    void setTertiaryColor(const QString &tertiary_color);
    bool is_tertiary_color_Set() const;
    bool is_tertiary_color_Valid() const;

    QString getTwitter() const;
    void setTwitter(const QString &twitter);
    bool is_twitter_Set() const;
    bool is_twitter_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getWebsite() const;
    void setWebsite(const QString &website);
    bool is_website_Set() const;
    bool is_website_Valid() const;

    QString getYouTube() const;
    void setYouTube(const QString &you_tube);
    bool is_you_tube_Set() const;
    bool is_you_tube_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_active;
    bool m_active_isSet;
    bool m_active_isValid;

    qint32 m_area_id;
    bool m_area_id_isSet;
    bool m_area_id_isValid;

    QString m_area_name;
    bool m_area_name_isSet;
    bool m_area_name_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_facebook;
    bool m_facebook_isSet;
    bool m_facebook_isValid;

    qint32 m_founded;
    bool m_founded_isSet;
    bool m_founded_isValid;

    QString m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    QString m_instagram;
    bool m_instagram_isSet;
    bool m_instagram_isValid;

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;

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

    QString m_short_name;
    bool m_short_name_isSet;
    bool m_short_name_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    QString m_tertiary_color;
    bool m_tertiary_color_isSet;
    bool m_tertiary_color_isValid;

    QString m_twitter;
    bool m_twitter_isSet;
    bool m_twitter_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_website;
    bool m_website_isSet;
    bool m_website_isValid;

    QString m_you_tube;
    bool m_you_tube_isSet;
    bool m_you_tube_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITeam)

#endif // OAITeam_H
