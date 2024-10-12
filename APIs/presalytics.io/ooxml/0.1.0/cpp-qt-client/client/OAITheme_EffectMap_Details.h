/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITheme_EffectMap_Details.h
 *
 * 
 */

#ifndef OAITheme_EffectMap_Details_H
#define OAITheme_EffectMap_Details_H

#include <QJsonObject>

#include "OAIShared_Effects_Details.h"
#include "OAITheme_Themes_Details.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIShared_Effects_Details;
class OAITheme_Themes_Details;

class OAITheme_EffectMap_Details : public OAIObject {
public:
    OAITheme_EffectMap_Details();
    OAITheme_EffectMap_Details(QString json);
    ~OAITheme_EffectMap_Details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getDateCreated() const;
    void setDateCreated(const QDateTime &date_created);
    bool is_date_created_Set() const;
    bool is_date_created_Valid() const;

    QDateTime getDateModified() const;
    void setDateModified(const QDateTime &date_modified);
    bool is_date_modified_Set() const;
    bool is_date_modified_Valid() const;

    OAIShared_Effects_Details getEffect() const;
    void setEffect(const OAIShared_Effects_Details &effect);
    bool is_effect_Set() const;
    bool is_effect_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint32 getIntensityId() const;
    void setIntensityId(const qint32 &intensity_id);
    bool is_intensity_id_Set() const;
    bool is_intensity_id_Valid() const;

    OAITheme_Themes_Details getTheme() const;
    void setTheme(const OAITheme_Themes_Details &theme);
    bool is_theme_Set() const;
    bool is_theme_Valid() const;

    QString getThemeId() const;
    void setThemeId(const QString &theme_id);
    bool is_theme_id_Set() const;
    bool is_theme_id_Valid() const;

    QString getUserCreated() const;
    void setUserCreated(const QString &user_created);
    bool is_user_created_Set() const;
    bool is_user_created_Valid() const;

    QString getUserModified() const;
    void setUserModified(const QString &user_modified);
    bool is_user_modified_Set() const;
    bool is_user_modified_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_date_created;
    bool m_date_created_isSet;
    bool m_date_created_isValid;

    QDateTime m_date_modified;
    bool m_date_modified_isSet;
    bool m_date_modified_isValid;

    OAIShared_Effects_Details m_effect;
    bool m_effect_isSet;
    bool m_effect_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint32 m_intensity_id;
    bool m_intensity_id_isSet;
    bool m_intensity_id_isValid;

    OAITheme_Themes_Details m_theme;
    bool m_theme_isSet;
    bool m_theme_isValid;

    QString m_theme_id;
    bool m_theme_id_isSet;
    bool m_theme_id_isValid;

    QString m_user_created;
    bool m_user_created_isSet;
    bool m_user_created_isValid;

    QString m_user_modified;
    bool m_user_modified_isSet;
    bool m_user_modified_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITheme_EffectMap_Details)

#endif // OAITheme_EffectMap_Details_H
