/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateNetworkWirelessRfProfile_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkWirelessRfProfile_request::OAIUpdateNetworkWirelessRfProfile_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkWirelessRfProfile_request::OAIUpdateNetworkWirelessRfProfile_request() {
    this->initializeModel();
}

OAIUpdateNetworkWirelessRfProfile_request::~OAIUpdateNetworkWirelessRfProfile_request() {}

void OAIUpdateNetworkWirelessRfProfile_request::initializeModel() {

    m_ap_band_settings_isSet = false;
    m_ap_band_settings_isValid = false;

    m_band_selection_type_isSet = false;
    m_band_selection_type_isValid = false;

    m_client_balancing_enabled_isSet = false;
    m_client_balancing_enabled_isValid = false;

    m_five_ghz_settings_isSet = false;
    m_five_ghz_settings_isValid = false;

    m_min_bitrate_type_isSet = false;
    m_min_bitrate_type_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_two_four_ghz_settings_isSet = false;
    m_two_four_ghz_settings_isValid = false;
}

void OAIUpdateNetworkWirelessRfProfile_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkWirelessRfProfile_request::fromJsonObject(QJsonObject json) {

    m_ap_band_settings_isValid = ::OpenAPI::fromJsonValue(m_ap_band_settings, json[QString("apBandSettings")]);
    m_ap_band_settings_isSet = !json[QString("apBandSettings")].isNull() && m_ap_band_settings_isValid;

    m_band_selection_type_isValid = ::OpenAPI::fromJsonValue(m_band_selection_type, json[QString("bandSelectionType")]);
    m_band_selection_type_isSet = !json[QString("bandSelectionType")].isNull() && m_band_selection_type_isValid;

    m_client_balancing_enabled_isValid = ::OpenAPI::fromJsonValue(m_client_balancing_enabled, json[QString("clientBalancingEnabled")]);
    m_client_balancing_enabled_isSet = !json[QString("clientBalancingEnabled")].isNull() && m_client_balancing_enabled_isValid;

    m_five_ghz_settings_isValid = ::OpenAPI::fromJsonValue(m_five_ghz_settings, json[QString("fiveGhzSettings")]);
    m_five_ghz_settings_isSet = !json[QString("fiveGhzSettings")].isNull() && m_five_ghz_settings_isValid;

    m_min_bitrate_type_isValid = ::OpenAPI::fromJsonValue(m_min_bitrate_type, json[QString("minBitrateType")]);
    m_min_bitrate_type_isSet = !json[QString("minBitrateType")].isNull() && m_min_bitrate_type_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_two_four_ghz_settings_isValid = ::OpenAPI::fromJsonValue(m_two_four_ghz_settings, json[QString("twoFourGhzSettings")]);
    m_two_four_ghz_settings_isSet = !json[QString("twoFourGhzSettings")].isNull() && m_two_four_ghz_settings_isValid;
}

QString OAIUpdateNetworkWirelessRfProfile_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkWirelessRfProfile_request::asJsonObject() const {
    QJsonObject obj;
    if (m_ap_band_settings.isSet()) {
        obj.insert(QString("apBandSettings"), ::OpenAPI::toJsonValue(m_ap_band_settings));
    }
    if (m_band_selection_type_isSet) {
        obj.insert(QString("bandSelectionType"), ::OpenAPI::toJsonValue(m_band_selection_type));
    }
    if (m_client_balancing_enabled_isSet) {
        obj.insert(QString("clientBalancingEnabled"), ::OpenAPI::toJsonValue(m_client_balancing_enabled));
    }
    if (m_five_ghz_settings.isSet()) {
        obj.insert(QString("fiveGhzSettings"), ::OpenAPI::toJsonValue(m_five_ghz_settings));
    }
    if (m_min_bitrate_type_isSet) {
        obj.insert(QString("minBitrateType"), ::OpenAPI::toJsonValue(m_min_bitrate_type));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_two_four_ghz_settings.isSet()) {
        obj.insert(QString("twoFourGhzSettings"), ::OpenAPI::toJsonValue(m_two_four_ghz_settings));
    }
    return obj;
}

OAIUpdateNetworkWirelessRfProfile_request_apBandSettings OAIUpdateNetworkWirelessRfProfile_request::getApBandSettings() const {
    return m_ap_band_settings;
}
void OAIUpdateNetworkWirelessRfProfile_request::setApBandSettings(const OAIUpdateNetworkWirelessRfProfile_request_apBandSettings &ap_band_settings) {
    m_ap_band_settings = ap_band_settings;
    m_ap_band_settings_isSet = true;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_ap_band_settings_Set() const{
    return m_ap_band_settings_isSet;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_ap_band_settings_Valid() const{
    return m_ap_band_settings_isValid;
}

QString OAIUpdateNetworkWirelessRfProfile_request::getBandSelectionType() const {
    return m_band_selection_type;
}
void OAIUpdateNetworkWirelessRfProfile_request::setBandSelectionType(const QString &band_selection_type) {
    m_band_selection_type = band_selection_type;
    m_band_selection_type_isSet = true;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_band_selection_type_Set() const{
    return m_band_selection_type_isSet;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_band_selection_type_Valid() const{
    return m_band_selection_type_isValid;
}

bool OAIUpdateNetworkWirelessRfProfile_request::isClientBalancingEnabled() const {
    return m_client_balancing_enabled;
}
void OAIUpdateNetworkWirelessRfProfile_request::setClientBalancingEnabled(const bool &client_balancing_enabled) {
    m_client_balancing_enabled = client_balancing_enabled;
    m_client_balancing_enabled_isSet = true;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_client_balancing_enabled_Set() const{
    return m_client_balancing_enabled_isSet;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_client_balancing_enabled_Valid() const{
    return m_client_balancing_enabled_isValid;
}

OAIUpdateNetworkWirelessRfProfile_request_fiveGhzSettings OAIUpdateNetworkWirelessRfProfile_request::getFiveGhzSettings() const {
    return m_five_ghz_settings;
}
void OAIUpdateNetworkWirelessRfProfile_request::setFiveGhzSettings(const OAIUpdateNetworkWirelessRfProfile_request_fiveGhzSettings &five_ghz_settings) {
    m_five_ghz_settings = five_ghz_settings;
    m_five_ghz_settings_isSet = true;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_five_ghz_settings_Set() const{
    return m_five_ghz_settings_isSet;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_five_ghz_settings_Valid() const{
    return m_five_ghz_settings_isValid;
}

QString OAIUpdateNetworkWirelessRfProfile_request::getMinBitrateType() const {
    return m_min_bitrate_type;
}
void OAIUpdateNetworkWirelessRfProfile_request::setMinBitrateType(const QString &min_bitrate_type) {
    m_min_bitrate_type = min_bitrate_type;
    m_min_bitrate_type_isSet = true;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_min_bitrate_type_Set() const{
    return m_min_bitrate_type_isSet;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_min_bitrate_type_Valid() const{
    return m_min_bitrate_type_isValid;
}

QString OAIUpdateNetworkWirelessRfProfile_request::getName() const {
    return m_name;
}
void OAIUpdateNetworkWirelessRfProfile_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_name_Valid() const{
    return m_name_isValid;
}

OAIUpdateNetworkWirelessRfProfile_request_twoFourGhzSettings OAIUpdateNetworkWirelessRfProfile_request::getTwoFourGhzSettings() const {
    return m_two_four_ghz_settings;
}
void OAIUpdateNetworkWirelessRfProfile_request::setTwoFourGhzSettings(const OAIUpdateNetworkWirelessRfProfile_request_twoFourGhzSettings &two_four_ghz_settings) {
    m_two_four_ghz_settings = two_four_ghz_settings;
    m_two_four_ghz_settings_isSet = true;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_two_four_ghz_settings_Set() const{
    return m_two_four_ghz_settings_isSet;
}

bool OAIUpdateNetworkWirelessRfProfile_request::is_two_four_ghz_settings_Valid() const{
    return m_two_four_ghz_settings_isValid;
}

bool OAIUpdateNetworkWirelessRfProfile_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ap_band_settings.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_band_selection_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_balancing_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_five_ghz_settings.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_bitrate_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_two_four_ghz_settings.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkWirelessRfProfile_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
