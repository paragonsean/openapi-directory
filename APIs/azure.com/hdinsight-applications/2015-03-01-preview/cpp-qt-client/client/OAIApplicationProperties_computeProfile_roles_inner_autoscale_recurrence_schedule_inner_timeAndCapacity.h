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
 * OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity.h
 *
 * Time and capacity request parameters
 */

#ifndef OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity_H
#define OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity : public OAIObject {
public:
    OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity();
    OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity(QString json);
    ~OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getMaxInstanceCount() const;
    void setMaxInstanceCount(const qint32 &max_instance_count);
    bool is_max_instance_count_Set() const;
    bool is_max_instance_count_Valid() const;

    qint32 getMinInstanceCount() const;
    void setMinInstanceCount(const qint32 &min_instance_count);
    bool is_min_instance_count_Set() const;
    bool is_min_instance_count_Valid() const;

    QString getTime() const;
    void setTime(const QString &time);
    bool is_time_Set() const;
    bool is_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_max_instance_count;
    bool m_max_instance_count_isSet;
    bool m_max_instance_count_isValid;

    qint32 m_min_instance_count;
    bool m_min_instance_count_isSet;
    bool m_min_instance_count_isValid;

    QString m_time;
    bool m_time_isSet;
    bool m_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity)

#endif // OAIApplicationProperties_computeProfile_roles_inner_autoscale_recurrence_schedule_inner_timeAndCapacity_H
