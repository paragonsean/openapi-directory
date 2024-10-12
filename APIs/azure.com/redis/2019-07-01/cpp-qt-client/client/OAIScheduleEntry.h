/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIScheduleEntry.h
 *
 * Patch schedule entry for a Premium Redis Cache.
 */

#ifndef OAIScheduleEntry_H
#define OAIScheduleEntry_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIScheduleEntry : public OAIObject {
public:
    OAIScheduleEntry();
    OAIScheduleEntry(QString json);
    ~OAIScheduleEntry() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDayOfWeek() const;
    void setDayOfWeek(const QString &day_of_week);
    bool is_day_of_week_Set() const;
    bool is_day_of_week_Valid() const;

    QString getMaintenanceWindow() const;
    void setMaintenanceWindow(const QString &maintenance_window);
    bool is_maintenance_window_Set() const;
    bool is_maintenance_window_Valid() const;

    qint32 getStartHourUtc() const;
    void setStartHourUtc(const qint32 &start_hour_utc);
    bool is_start_hour_utc_Set() const;
    bool is_start_hour_utc_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_day_of_week;
    bool m_day_of_week_isSet;
    bool m_day_of_week_isValid;

    QString m_maintenance_window;
    bool m_maintenance_window_isSet;
    bool m_maintenance_window_isValid;

    qint32 m_start_hour_utc;
    bool m_start_hour_utc_isSet;
    bool m_start_hour_utc_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScheduleEntry)

#endif // OAIScheduleEntry_H
