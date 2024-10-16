/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWeeklySchedule.h
 *
 * Weekly schedule allows to schedule operations by day of week and time of the day
 */

#ifndef OAIWeeklySchedule_H
#define OAIWeeklySchedule_H

#include <QJsonObject>

#include "OAILocalTime.h"
#include <QSet>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILocalTime;

class OAIWeeklySchedule : public OAIObject {
public:
    OAIWeeklySchedule();
    OAIWeeklySchedule(QString json);
    ~OAIWeeklySchedule() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QSet<QString> getDaysOfWeek() const;
    void setDaysOfWeek(const QSet<QString> &days_of_week);
    bool is_days_of_week_Set() const;
    bool is_days_of_week_Valid() const;

    OAILocalTime getStartTimeOfDay() const;
    void setStartTimeOfDay(const OAILocalTime &start_time_of_day);
    bool is_start_time_of_day_Set() const;
    bool is_start_time_of_day_Valid() const;

    OAILocalTime getStopTimeOfDay() const;
    void setStopTimeOfDay(const OAILocalTime &stop_time_of_day);
    bool is_stop_time_of_day_Set() const;
    bool is_stop_time_of_day_Valid() const;

    QString getTimeZone() const;
    void setTimeZone(const QString &time_zone);
    bool is_time_zone_Set() const;
    bool is_time_zone_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QSet<QString> m_days_of_week;
    bool m_days_of_week_isSet;
    bool m_days_of_week_isValid;

    OAILocalTime m_start_time_of_day;
    bool m_start_time_of_day_isSet;
    bool m_start_time_of_day_isValid;

    OAILocalTime m_stop_time_of_day;
    bool m_stop_time_of_day_isSet;
    bool m_stop_time_of_day_isValid;

    QString m_time_zone;
    bool m_time_zone_isSet;
    bool m_time_zone_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWeeklySchedule)

#endif // OAIWeeklySchedule_H
