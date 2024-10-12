/**
 * MLB v3 Play-by-Play
 * MLB play-by-play API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISeries.h
 *
 * 
 */

#ifndef OAISeries_H
#define OAISeries_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISeries : public OAIObject {
public:
    OAISeries();
    OAISeries(QString json);
    ~OAISeries() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAwayTeamWins() const;
    void setAwayTeamWins(const qint32 &away_team_wins);
    bool is_away_team_wins_Set() const;
    bool is_away_team_wins_Valid() const;

    qint32 getGameNumber() const;
    void setGameNumber(const qint32 &game_number);
    bool is_game_number_Set() const;
    bool is_game_number_Valid() const;

    qint32 getHomeTeamWins() const;
    void setHomeTeamWins(const qint32 &home_team_wins);
    bool is_home_team_wins_Set() const;
    bool is_home_team_wins_Valid() const;

    qint32 getMaxLength() const;
    void setMaxLength(const qint32 &max_length);
    bool is_max_length_Set() const;
    bool is_max_length_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_away_team_wins;
    bool m_away_team_wins_isSet;
    bool m_away_team_wins_isValid;

    qint32 m_game_number;
    bool m_game_number_isSet;
    bool m_game_number_isValid;

    qint32 m_home_team_wins;
    bool m_home_team_wins_isSet;
    bool m_home_team_wins_isValid;

    qint32 m_max_length;
    bool m_max_length_isSet;
    bool m_max_length_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISeries)

#endif // OAISeries_H
