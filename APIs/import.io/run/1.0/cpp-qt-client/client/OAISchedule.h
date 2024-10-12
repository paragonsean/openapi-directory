/**
 * import.io
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISchedule.h
 *
 * 
 */

#ifndef OAISchedule_H
#define OAISchedule_H

#include <QJsonObject>

#include "OAISchedule_intervalData.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISchedule_intervalData;

class OAISchedule : public OAIObject {
public:
    OAISchedule();
    OAISchedule(QString json);
    ~OAISchedule() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getExtractorId() const;
    void setExtractorId(const QString &extractor_id);
    bool is_extractor_id_Set() const;
    bool is_extractor_id_Valid() const;

    QString getInterval() const;
    void setInterval(const QString &interval);
    bool is_interval_Set() const;
    bool is_interval_Valid() const;

    OAISchedule_intervalData getIntervalData() const;
    void setIntervalData(const OAISchedule_intervalData &interval_data);
    bool is_interval_data_Set() const;
    bool is_interval_data_Valid() const;

    qint64 getNextRunAt() const;
    void setNextRunAt(const qint64 &next_run_at);
    bool is_next_run_at_Set() const;
    bool is_next_run_at_Valid() const;

    QString getOwnerId() const;
    void setOwnerId(const QString &owner_id);
    bool is_owner_id_Set() const;
    bool is_owner_id_Valid() const;

    qint64 getStartTimestamp() const;
    void setStartTimestamp(const qint64 &start_timestamp);
    bool is_start_timestamp_Set() const;
    bool is_start_timestamp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_extractor_id;
    bool m_extractor_id_isSet;
    bool m_extractor_id_isValid;

    QString m_interval;
    bool m_interval_isSet;
    bool m_interval_isValid;

    OAISchedule_intervalData m_interval_data;
    bool m_interval_data_isSet;
    bool m_interval_data_isValid;

    qint64 m_next_run_at;
    bool m_next_run_at_isSet;
    bool m_next_run_at_isValid;

    QString m_owner_id;
    bool m_owner_id_isSet;
    bool m_owner_id_isValid;

    qint64 m_start_timestamp;
    bool m_start_timestamp_isSet;
    bool m_start_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISchedule)

#endif // OAISchedule_H
