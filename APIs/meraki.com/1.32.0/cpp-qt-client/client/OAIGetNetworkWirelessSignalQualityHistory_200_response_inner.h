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
 * OAIGetNetworkWirelessSignalQualityHistory_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetNetworkWirelessSignalQualityHistory_200_response_inner_H
#define OAIGetNetworkWirelessSignalQualityHistory_200_response_inner_H

#include <QJsonObject>

#include <QDateTime>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetNetworkWirelessSignalQualityHistory_200_response_inner : public OAIObject {
public:
    OAIGetNetworkWirelessSignalQualityHistory_200_response_inner();
    OAIGetNetworkWirelessSignalQualityHistory_200_response_inner(QString json);
    ~OAIGetNetworkWirelessSignalQualityHistory_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getEndTs() const;
    void setEndTs(const QDateTime &end_ts);
    bool is_end_ts_Set() const;
    bool is_end_ts_Valid() const;

    qint32 getRssi() const;
    void setRssi(const qint32 &rssi);
    bool is_rssi_Set() const;
    bool is_rssi_Valid() const;

    qint32 getSnr() const;
    void setSnr(const qint32 &snr);
    bool is_snr_Set() const;
    bool is_snr_Valid() const;

    QDateTime getStartTs() const;
    void setStartTs(const QDateTime &start_ts);
    bool is_start_ts_Set() const;
    bool is_start_ts_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_end_ts;
    bool m_end_ts_isSet;
    bool m_end_ts_isValid;

    qint32 m_rssi;
    bool m_rssi_isSet;
    bool m_rssi_isValid;

    qint32 m_snr;
    bool m_snr_isSet;
    bool m_snr_isValid;

    QDateTime m_start_ts;
    bool m_start_ts_isSet;
    bool m_start_ts_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkWirelessSignalQualityHistory_200_response_inner)

#endif // OAIGetNetworkWirelessSignalQualityHistory_200_response_inner_H
