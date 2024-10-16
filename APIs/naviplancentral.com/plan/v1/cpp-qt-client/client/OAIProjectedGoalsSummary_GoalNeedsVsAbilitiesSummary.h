/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProjectedGoalsSummary_GoalNeedsVsAbilitiesSummary.h
 *
 * 
 */

#ifndef OAIProjectedGoalsSummary_GoalNeedsVsAbilitiesSummary_H
#define OAIProjectedGoalsSummary_GoalNeedsVsAbilitiesSummary_H

#include <QJsonObject>

#include "OAIGoalNeedsVsAbilitiesSummary.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGoalNeedsVsAbilitiesSummary;

class OAIProjectedGoalsSummary_GoalNeedsVsAbilitiesSummary : public OAIObject {
public:
    OAIProjectedGoalsSummary_GoalNeedsVsAbilitiesSummary();
    OAIProjectedGoalsSummary_GoalNeedsVsAbilitiesSummary(QString json);
    ~OAIProjectedGoalsSummary_GoalNeedsVsAbilitiesSummary() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getClientAge() const;
    void setClientAge(const qint32 &client_age);
    bool is_client_age_Set() const;
    bool is_client_age_Valid() const;

    qint32 getCoClientAge() const;
    void setCoClientAge(const qint32 &co_client_age);
    bool is_co_client_age_Set() const;
    bool is_co_client_age_Valid() const;

    QList<OAIGoalNeedsVsAbilitiesSummary> getGoals() const;
    void setGoals(const QList<OAIGoalNeedsVsAbilitiesSummary> &goals);
    bool is_goals_Set() const;
    bool is_goals_Valid() const;

    qint32 getYear() const;
    void setYear(const qint32 &year);
    bool is_year_Set() const;
    bool is_year_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_client_age;
    bool m_client_age_isSet;
    bool m_client_age_isValid;

    qint32 m_co_client_age;
    bool m_co_client_age_isSet;
    bool m_co_client_age_isValid;

    QList<OAIGoalNeedsVsAbilitiesSummary> m_goals;
    bool m_goals_isSet;
    bool m_goals_isValid;

    qint32 m_year;
    bool m_year_isSet;
    bool m_year_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjectedGoalsSummary_GoalNeedsVsAbilitiesSummary)

#endif // OAIProjectedGoalsSummary_GoalNeedsVsAbilitiesSummary_H
