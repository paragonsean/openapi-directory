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
 * OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings.h
 *
 * Settings related to 5Ghz band
 */

#ifndef OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings_H
#define OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings : public OAIObject {
public:
    OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings();
    OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings(QString json);
    ~OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getChannelWidth() const;
    void setChannelWidth(const QString &channel_width);
    bool is_channel_width_Set() const;
    bool is_channel_width_Valid() const;

    qint32 getMaxPower() const;
    void setMaxPower(const qint32 &max_power);
    bool is_max_power_Set() const;
    bool is_max_power_Valid() const;

    qint32 getMinBitrate() const;
    void setMinBitrate(const qint32 &min_bitrate);
    bool is_min_bitrate_Set() const;
    bool is_min_bitrate_Valid() const;

    qint32 getMinPower() const;
    void setMinPower(const qint32 &min_power);
    bool is_min_power_Set() const;
    bool is_min_power_Valid() const;

    qint32 getRxsop() const;
    void setRxsop(const qint32 &rxsop);
    bool is_rxsop_Set() const;
    bool is_rxsop_Valid() const;

    QList<qint32> getValidAutoChannels() const;
    void setValidAutoChannels(const QList<qint32> &valid_auto_channels);
    bool is_valid_auto_channels_Set() const;
    bool is_valid_auto_channels_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_channel_width;
    bool m_channel_width_isSet;
    bool m_channel_width_isValid;

    qint32 m_max_power;
    bool m_max_power_isSet;
    bool m_max_power_isValid;

    qint32 m_min_bitrate;
    bool m_min_bitrate_isSet;
    bool m_min_bitrate_isValid;

    qint32 m_min_power;
    bool m_min_power_isSet;
    bool m_min_power_isValid;

    qint32 m_rxsop;
    bool m_rxsop_isSet;
    bool m_rxsop_isValid;

    QList<qint32> m_valid_auto_channels;
    bool m_valid_auto_channels_isSet;
    bool m_valid_auto_channels_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings)

#endif // OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings_H
