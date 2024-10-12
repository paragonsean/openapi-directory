/**
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPermission.h
 *
 * 
 */

#ifndef OAIPermission_H
#define OAIPermission_H

#include <QJsonObject>

#include "OAIPermission_dateRange.h"
#include "OAIPermission_frequency.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPermission_dateRange;
class OAIPermission_frequency;

class OAIPermission : public OAIObject {
public:
    OAIPermission();
    OAIPermission(QString json);
    ~OAIPermission() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccessMode() const;
    void setAccessMode(const QString &access_mode);
    bool is_access_mode_Set() const;
    bool is_access_mode_Valid() const;

    QDateTime getDataEraseAt() const;
    void setDataEraseAt(const QDateTime &data_erase_at);
    bool is_data_erase_at_Set() const;
    bool is_data_erase_at_Valid() const;

    OAIPermission_dateRange getDateRange() const;
    void setDateRange(const OAIPermission_dateRange &date_range);
    bool is_date_range_Set() const;
    bool is_date_range_Valid() const;

    OAIPermission_frequency getFrequency() const;
    void setFrequency(const OAIPermission_frequency &frequency);
    bool is_frequency_Set() const;
    bool is_frequency_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_access_mode;
    bool m_access_mode_isSet;
    bool m_access_mode_isValid;

    QDateTime m_data_erase_at;
    bool m_data_erase_at_isSet;
    bool m_data_erase_at_isValid;

    OAIPermission_dateRange m_date_range;
    bool m_date_range_isSet;
    bool m_date_range_isValid;

    OAIPermission_frequency m_frequency;
    bool m_frequency_isSet;
    bool m_frequency_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPermission)

#endif // OAIPermission_H
