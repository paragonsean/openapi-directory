/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDistrict_Ranking.h
 *
 * Rank of a team in a district.
 */

#ifndef OAIDistrict_Ranking_H
#define OAIDistrict_Ranking_H

#include <QJsonObject>

#include "OAIDistrict_Ranking_event_points_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDistrict_Ranking_event_points_inner;

class OAIDistrict_Ranking : public OAIObject {
public:
    OAIDistrict_Ranking();
    OAIDistrict_Ranking(QString json);
    ~OAIDistrict_Ranking() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIDistrict_Ranking_event_points_inner> getEventPoints() const;
    void setEventPoints(const QList<OAIDistrict_Ranking_event_points_inner> &event_points);
    bool is_event_points_Set() const;
    bool is_event_points_Valid() const;

    qint32 getPointTotal() const;
    void setPointTotal(const qint32 &point_total);
    bool is_point_total_Set() const;
    bool is_point_total_Valid() const;

    qint32 getRank() const;
    void setRank(const qint32 &rank);
    bool is_rank_Set() const;
    bool is_rank_Valid() const;

    qint32 getRookieBonus() const;
    void setRookieBonus(const qint32 &rookie_bonus);
    bool is_rookie_bonus_Set() const;
    bool is_rookie_bonus_Valid() const;

    QString getTeamKey() const;
    void setTeamKey(const QString &team_key);
    bool is_team_key_Set() const;
    bool is_team_key_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIDistrict_Ranking_event_points_inner> m_event_points;
    bool m_event_points_isSet;
    bool m_event_points_isValid;

    qint32 m_point_total;
    bool m_point_total_isSet;
    bool m_point_total_isValid;

    qint32 m_rank;
    bool m_rank_isSet;
    bool m_rank_isValid;

    qint32 m_rookie_bonus;
    bool m_rookie_bonus_isSet;
    bool m_rookie_bonus_isValid;

    QString m_team_key;
    bool m_team_key_isSet;
    bool m_team_key_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDistrict_Ranking)

#endif // OAIDistrict_Ranking_H
