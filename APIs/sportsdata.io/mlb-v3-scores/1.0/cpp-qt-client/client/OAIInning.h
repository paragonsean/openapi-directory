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
 * OAIInning.h
 *
 * 
 */

#ifndef OAIInning_H
#define OAIInning_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInning : public OAIObject {
public:
    OAIInning();
    OAIInning(QString json);
    ~OAIInning() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAwayTeamRuns() const;
    void setAwayTeamRuns(const qint32 &away_team_runs);
    bool is_away_team_runs_Set() const;
    bool is_away_team_runs_Valid() const;

    qint32 getGameId() const;
    void setGameId(const qint32 &game_id);
    bool is_game_id_Set() const;
    bool is_game_id_Valid() const;

    qint32 getHomeTeamRuns() const;
    void setHomeTeamRuns(const qint32 &home_team_runs);
    bool is_home_team_runs_Set() const;
    bool is_home_team_runs_Valid() const;

    qint32 getInningId() const;
    void setInningId(const qint32 &inning_id);
    bool is_inning_id_Set() const;
    bool is_inning_id_Valid() const;

    qint32 getInningNumber() const;
    void setInningNumber(const qint32 &inning_number);
    bool is_inning_number_Set() const;
    bool is_inning_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_away_team_runs;
    bool m_away_team_runs_isSet;
    bool m_away_team_runs_isValid;

    qint32 m_game_id;
    bool m_game_id_isSet;
    bool m_game_id_isValid;

    qint32 m_home_team_runs;
    bool m_home_team_runs_isSet;
    bool m_home_team_runs_isValid;

    qint32 m_inning_id;
    bool m_inning_id_isSet;
    bool m_inning_id_isValid;

    qint32 m_inning_number;
    bool m_inning_number_isSet;
    bool m_inning_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInning)

#endif // OAIInning_H
