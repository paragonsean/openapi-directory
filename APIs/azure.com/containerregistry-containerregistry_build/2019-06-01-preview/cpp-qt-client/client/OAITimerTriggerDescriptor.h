/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITimerTriggerDescriptor.h
 *
 * 
 */

#ifndef OAITimerTriggerDescriptor_H
#define OAITimerTriggerDescriptor_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITimerTriggerDescriptor : public OAIObject {
public:
    OAITimerTriggerDescriptor();
    OAITimerTriggerDescriptor(QString json);
    ~OAITimerTriggerDescriptor() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getScheduleOccurrence() const;
    void setScheduleOccurrence(const QString &schedule_occurrence);
    bool is_schedule_occurrence_Set() const;
    bool is_schedule_occurrence_Valid() const;

    QString getTimerTriggerName() const;
    void setTimerTriggerName(const QString &timer_trigger_name);
    bool is_timer_trigger_name_Set() const;
    bool is_timer_trigger_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_schedule_occurrence;
    bool m_schedule_occurrence_isSet;
    bool m_schedule_occurrence_isValid;

    QString m_timer_trigger_name;
    bool m_timer_trigger_name_isSet;
    bool m_timer_trigger_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITimerTriggerDescriptor)

#endif // OAITimerTriggerDescriptor_H
