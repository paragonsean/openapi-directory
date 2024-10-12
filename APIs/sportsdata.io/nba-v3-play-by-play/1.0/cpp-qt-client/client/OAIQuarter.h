/**
 * NBA v3 Play-by-Play
 * NBA play-by-play API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIQuarter.h
 *
 * 
 */

#ifndef OAIQuarter_H
#define OAIQuarter_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIQuarter : public OAIObject {
public:
    OAIQuarter();
    OAIQuarter(QString json);
    ~OAIQuarter() override;

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

    qint32 getQuarterId() const;
    void setQuarterId(const qint32 &quarter_id);
    bool is_quarter_id_Set() const;
    bool is_quarter_id_Valid() const;

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

    qint32 m_quarter_id;
    bool m_quarter_id_isSet;
    bool m_quarter_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQuarter)

#endif // OAIQuarter_H
