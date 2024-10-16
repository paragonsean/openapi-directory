/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateNetworkWirelessSsidSchedules_request_ranges_inner.h
 *
 * 
 */

#ifndef OAIUpdateNetworkWirelessSsidSchedules_request_ranges_inner_H
#define OAIUpdateNetworkWirelessSsidSchedules_request_ranges_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNetworkWirelessSsidSchedules_request_ranges_inner : public OAIObject {
public:
    OAIUpdateNetworkWirelessSsidSchedules_request_ranges_inner();
    OAIUpdateNetworkWirelessSsidSchedules_request_ranges_inner(QString json);
    ~OAIUpdateNetworkWirelessSsidSchedules_request_ranges_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEndDay() const;
    void setEndDay(const QString &end_day);
    bool is_end_day_Set() const;
    bool is_end_day_Valid() const;

    QString getEndTime() const;
    void setEndTime(const QString &end_time);
    bool is_end_time_Set() const;
    bool is_end_time_Valid() const;

    QString getStartDay() const;
    void setStartDay(const QString &start_day);
    bool is_start_day_Set() const;
    bool is_start_day_Valid() const;

    QString getStartTime() const;
    void setStartTime(const QString &start_time);
    bool is_start_time_Set() const;
    bool is_start_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_end_day;
    bool m_end_day_isSet;
    bool m_end_day_isValid;

    QString m_end_time;
    bool m_end_time_isSet;
    bool m_end_time_isValid;

    QString m_start_day;
    bool m_start_day_isSet;
    bool m_start_day_isValid;

    QString m_start_time;
    bool m_start_time_isSet;
    bool m_start_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkWirelessSsidSchedules_request_ranges_inner)

#endif // OAIUpdateNetworkWirelessSsidSchedules_request_ranges_inner_H
