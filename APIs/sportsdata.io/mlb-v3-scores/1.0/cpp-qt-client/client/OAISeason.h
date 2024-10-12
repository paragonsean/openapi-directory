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
 * OAISeason.h
 *
 * 
 */

#ifndef OAISeason_H
#define OAISeason_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISeason : public OAIObject {
public:
    OAISeason();
    OAISeason(QString json);
    ~OAISeason() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getApiSeason() const;
    void setApiSeason(const QString &api_season);
    bool is_api_season_Set() const;
    bool is_api_season_Valid() const;

    QString getPostSeasonStartDate() const;
    void setPostSeasonStartDate(const QString &post_season_start_date);
    bool is_post_season_start_date_Set() const;
    bool is_post_season_start_date_Valid() const;

    QString getRegularSeasonStartDate() const;
    void setRegularSeasonStartDate(const QString &regular_season_start_date);
    bool is_regular_season_start_date_Set() const;
    bool is_regular_season_start_date_Valid() const;

    qint32 getSeason() const;
    void setSeason(const qint32 &season);
    bool is_season_Set() const;
    bool is_season_Valid() const;

    QString getSeasonType() const;
    void setSeasonType(const QString &season_type);
    bool is_season_type_Set() const;
    bool is_season_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_api_season;
    bool m_api_season_isSet;
    bool m_api_season_isValid;

    QString m_post_season_start_date;
    bool m_post_season_start_date_isSet;
    bool m_post_season_start_date_isValid;

    QString m_regular_season_start_date;
    bool m_regular_season_start_date_isSet;
    bool m_regular_season_start_date_isValid;

    qint32 m_season;
    bool m_season_isSet;
    bool m_season_isValid;

    QString m_season_type;
    bool m_season_type_isSet;
    bool m_season_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISeason)

#endif // OAISeason_H
