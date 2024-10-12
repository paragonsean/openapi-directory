/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPeriodicTimerSourceInfo.h
 *
 * Periodic timer event source.
 */

#ifndef OAIPeriodicTimerSourceInfo_H
#define OAIPeriodicTimerSourceInfo_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPeriodicTimerSourceInfo : public OAIObject {
public:
    OAIPeriodicTimerSourceInfo();
    OAIPeriodicTimerSourceInfo(QString json);
    ~OAIPeriodicTimerSourceInfo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getSchedule() const;
    void setSchedule(const QString &schedule);
    bool is_schedule_Set() const;
    bool is_schedule_Valid() const;

    QDateTime getStartTime() const;
    void setStartTime(const QDateTime &start_time);
    bool is_start_time_Set() const;
    bool is_start_time_Valid() const;

    QString getTopic() const;
    void setTopic(const QString &topic);
    bool is_topic_Set() const;
    bool is_topic_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_schedule;
    bool m_schedule_isSet;
    bool m_schedule_isValid;

    QDateTime m_start_time;
    bool m_start_time_isSet;
    bool m_start_time_isValid;

    QString m_topic;
    bool m_topic_isSet;
    bool m_topic_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPeriodicTimerSourceInfo)

#endif // OAIPeriodicTimerSourceInfo_H
