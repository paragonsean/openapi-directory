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
 * OAIBandwidthScheduleProperties.h
 *
 * The properties of the bandwidth schedule.
 */

#ifndef OAIBandwidthScheduleProperties_H
#define OAIBandwidthScheduleProperties_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBandwidthScheduleProperties : public OAIObject {
public:
    OAIBandwidthScheduleProperties();
    OAIBandwidthScheduleProperties(QString json);
    ~OAIBandwidthScheduleProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getDays() const;
    void setDays(const QList<QString> &days);
    bool is_days_Set() const;
    bool is_days_Valid() const;

    qint32 getRateInMbps() const;
    void setRateInMbps(const qint32 &rate_in_mbps);
    bool is_rate_in_mbps_Set() const;
    bool is_rate_in_mbps_Valid() const;

    QString getStart() const;
    void setStart(const QString &start);
    bool is_start_Set() const;
    bool is_start_Valid() const;

    QString getStop() const;
    void setStop(const QString &stop);
    bool is_stop_Set() const;
    bool is_stop_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_days;
    bool m_days_isSet;
    bool m_days_isValid;

    qint32 m_rate_in_mbps;
    bool m_rate_in_mbps_isSet;
    bool m_rate_in_mbps_isValid;

    QString m_start;
    bool m_start_isSet;
    bool m_start_isValid;

    QString m_stop;
    bool m_stop_isSet;
    bool m_stop_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBandwidthScheduleProperties)

#endif // OAIBandwidthScheduleProperties_H
