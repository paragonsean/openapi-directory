/**
 * CBB v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPeriod.h
 *
 * 
 */

#ifndef OAIPeriod_H
#define OAIPeriod_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPeriod : public OAIObject {
public:
    OAIPeriod();
    OAIPeriod(QString json);
    ~OAIPeriod() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAwayScore() const;
    void setAwayScore(const qint32 &away_score);
    bool is_away_score_Set() const;
    bool is_away_score_Valid() const;

    qint32 getGameId() const;
    void setGameId(const qint32 &game_id);
    bool is_game_id_Set() const;
    bool is_game_id_Valid() const;

    qint32 getHomeScore() const;
    void setHomeScore(const qint32 &home_score);
    bool is_home_score_Set() const;
    bool is_home_score_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNumber() const;
    void setNumber(const qint32 &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    qint32 getPeriodId() const;
    void setPeriodId(const qint32 &period_id);
    bool is_period_id_Set() const;
    bool is_period_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_away_score;
    bool m_away_score_isSet;
    bool m_away_score_isValid;

    qint32 m_game_id;
    bool m_game_id_isSet;
    bool m_game_id_isValid;

    qint32 m_home_score;
    bool m_home_score_isSet;
    bool m_home_score_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    qint32 m_period_id;
    bool m_period_id_isSet;
    bool m_period_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPeriod)

#endif // OAIPeriod_H
