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
 * OAICreateNetworkWirelessRfProfile_201_response.h
 *
 * 
 */

#ifndef OAICreateNetworkWirelessRfProfile_201_response_H
#define OAICreateNetworkWirelessRfProfile_201_response_H

#include <QJsonObject>

#include "OAICreateNetworkWirelessRfProfile_201_response_apBandSettings.h"
#include "OAICreateNetworkWirelessRfProfile_201_response_perSsidSettings.h"
#include "OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings.h"
#include "OAICreateNetworkWirelessRfProfile_request_transmission.h"
#include "OAICreateNetworkWirelessRfProfile_request_twoFourGhzSettings.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICreateNetworkWirelessRfProfile_201_response_apBandSettings;
class OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings;
class OAICreateNetworkWirelessRfProfile_201_response_perSsidSettings;
class OAICreateNetworkWirelessRfProfile_request_transmission;
class OAICreateNetworkWirelessRfProfile_request_twoFourGhzSettings;

class OAICreateNetworkWirelessRfProfile_201_response : public OAIObject {
public:
    OAICreateNetworkWirelessRfProfile_201_response();
    OAICreateNetworkWirelessRfProfile_201_response(QString json);
    ~OAICreateNetworkWirelessRfProfile_201_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICreateNetworkWirelessRfProfile_201_response_apBandSettings getApBandSettings() const;
    void setApBandSettings(const OAICreateNetworkWirelessRfProfile_201_response_apBandSettings &ap_band_settings);
    bool is_ap_band_settings_Set() const;
    bool is_ap_band_settings_Valid() const;

    QString getBandSelectionType() const;
    void setBandSelectionType(const QString &band_selection_type);
    bool is_band_selection_type_Set() const;
    bool is_band_selection_type_Valid() const;

    bool isClientBalancingEnabled() const;
    void setClientBalancingEnabled(const bool &client_balancing_enabled);
    bool is_client_balancing_enabled_Set() const;
    bool is_client_balancing_enabled_Valid() const;

    OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings getFiveGhzSettings() const;
    void setFiveGhzSettings(const OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings &five_ghz_settings);
    bool is_five_ghz_settings_Set() const;
    bool is_five_ghz_settings_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getMinBitrateType() const;
    void setMinBitrateType(const QString &min_bitrate_type);
    bool is_min_bitrate_type_Set() const;
    bool is_min_bitrate_type_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getNetworkId() const;
    void setNetworkId(const QString &network_id);
    bool is_network_id_Set() const;
    bool is_network_id_Valid() const;

    OAICreateNetworkWirelessRfProfile_201_response_perSsidSettings getPerSsidSettings() const;
    void setPerSsidSettings(const OAICreateNetworkWirelessRfProfile_201_response_perSsidSettings &per_ssid_settings);
    bool is_per_ssid_settings_Set() const;
    bool is_per_ssid_settings_Valid() const;

    OAICreateNetworkWirelessRfProfile_request_transmission getTransmission() const;
    void setTransmission(const OAICreateNetworkWirelessRfProfile_request_transmission &transmission);
    bool is_transmission_Set() const;
    bool is_transmission_Valid() const;

    OAICreateNetworkWirelessRfProfile_request_twoFourGhzSettings getTwoFourGhzSettings() const;
    void setTwoFourGhzSettings(const OAICreateNetworkWirelessRfProfile_request_twoFourGhzSettings &two_four_ghz_settings);
    bool is_two_four_ghz_settings_Set() const;
    bool is_two_four_ghz_settings_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICreateNetworkWirelessRfProfile_201_response_apBandSettings m_ap_band_settings;
    bool m_ap_band_settings_isSet;
    bool m_ap_band_settings_isValid;

    QString m_band_selection_type;
    bool m_band_selection_type_isSet;
    bool m_band_selection_type_isValid;

    bool m_client_balancing_enabled;
    bool m_client_balancing_enabled_isSet;
    bool m_client_balancing_enabled_isValid;

    OAICreateNetworkWirelessRfProfile_request_fiveGhzSettings m_five_ghz_settings;
    bool m_five_ghz_settings_isSet;
    bool m_five_ghz_settings_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_min_bitrate_type;
    bool m_min_bitrate_type_isSet;
    bool m_min_bitrate_type_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_network_id;
    bool m_network_id_isSet;
    bool m_network_id_isValid;

    OAICreateNetworkWirelessRfProfile_201_response_perSsidSettings m_per_ssid_settings;
    bool m_per_ssid_settings_isSet;
    bool m_per_ssid_settings_isValid;

    OAICreateNetworkWirelessRfProfile_request_transmission m_transmission;
    bool m_transmission_isSet;
    bool m_transmission_isValid;

    OAICreateNetworkWirelessRfProfile_request_twoFourGhzSettings m_two_four_ghz_settings;
    bool m_two_four_ghz_settings_isSet;
    bool m_two_four_ghz_settings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateNetworkWirelessRfProfile_201_response)

#endif // OAICreateNetworkWirelessRfProfile_201_response_H
