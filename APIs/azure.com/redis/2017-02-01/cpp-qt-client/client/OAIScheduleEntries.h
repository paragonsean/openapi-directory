/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2017-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIScheduleEntries.h
 *
 * List of patch schedules for a Redis cache.
 */

#ifndef OAIScheduleEntries_H
#define OAIScheduleEntries_H

#include <QJsonObject>

#include "OAIScheduleEntry.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIScheduleEntry;

class OAIScheduleEntries : public OAIObject {
public:
    OAIScheduleEntries();
    OAIScheduleEntries(QString json);
    ~OAIScheduleEntries() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIScheduleEntry> getScheduleEntries() const;
    void setScheduleEntries(const QList<OAIScheduleEntry> &schedule_entries);
    bool is_schedule_entries_Set() const;
    bool is_schedule_entries_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIScheduleEntry> m_schedule_entries;
    bool m_schedule_entries_isSet;
    bool m_schedule_entries_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScheduleEntries)

#endif // OAIScheduleEntries_H
