/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence.h
 *
 * Schedule-based autoscale request parameters
 */

#ifndef OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_H
#define OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_H

#include <QJsonObject>

#include "OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner;

class OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence : public OAIObject {
public:
    OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence();
    OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence(QString json);
    ~OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner> getSchedule() const;
    void setSchedule(const QList<OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner> &schedule);
    bool is_schedule_Set() const;
    bool is_schedule_Valid() const;

    QString getTimeZone() const;
    void setTimeZone(const QString &time_zone);
    bool is_time_zone_Set() const;
    bool is_time_zone_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner> m_schedule;
    bool m_schedule_isSet;
    bool m_schedule_isValid;

    QString m_time_zone;
    bool m_time_zone_isSet;
    bool m_time_zone_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence)

#endif // OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_H
