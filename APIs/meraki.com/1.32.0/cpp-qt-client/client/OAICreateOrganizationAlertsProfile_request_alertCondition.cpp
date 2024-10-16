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

#include "OAICreateOrganizationAlertsProfile_request_alertCondition.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateOrganizationAlertsProfile_request_alertCondition::OAICreateOrganizationAlertsProfile_request_alertCondition(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateOrganizationAlertsProfile_request_alertCondition::OAICreateOrganizationAlertsProfile_request_alertCondition() {
    this->initializeModel();
}

OAICreateOrganizationAlertsProfile_request_alertCondition::~OAICreateOrganizationAlertsProfile_request_alertCondition() {}

void OAICreateOrganizationAlertsProfile_request_alertCondition::initializeModel() {

    m_bit_rate_bps_isSet = false;
    m_bit_rate_bps_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_interface_isSet = false;
    m_interface_isValid = false;

    m_jitter_ms_isSet = false;
    m_jitter_ms_isValid = false;

    m_latency_ms_isSet = false;
    m_latency_ms_isValid = false;

    m_loss_ratio_isSet = false;
    m_loss_ratio_isValid = false;

    m_mos_isSet = false;
    m_mos_isValid = false;

    m_window_isSet = false;
    m_window_isValid = false;
}

void OAICreateOrganizationAlertsProfile_request_alertCondition::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateOrganizationAlertsProfile_request_alertCondition::fromJsonObject(QJsonObject json) {

    m_bit_rate_bps_isValid = ::OpenAPI::fromJsonValue(m_bit_rate_bps, json[QString("bit_rate_bps")]);
    m_bit_rate_bps_isSet = !json[QString("bit_rate_bps")].isNull() && m_bit_rate_bps_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_interface_isValid = ::OpenAPI::fromJsonValue(m_interface, json[QString("interface")]);
    m_interface_isSet = !json[QString("interface")].isNull() && m_interface_isValid;

    m_jitter_ms_isValid = ::OpenAPI::fromJsonValue(m_jitter_ms, json[QString("jitter_ms")]);
    m_jitter_ms_isSet = !json[QString("jitter_ms")].isNull() && m_jitter_ms_isValid;

    m_latency_ms_isValid = ::OpenAPI::fromJsonValue(m_latency_ms, json[QString("latency_ms")]);
    m_latency_ms_isSet = !json[QString("latency_ms")].isNull() && m_latency_ms_isValid;

    m_loss_ratio_isValid = ::OpenAPI::fromJsonValue(m_loss_ratio, json[QString("loss_ratio")]);
    m_loss_ratio_isSet = !json[QString("loss_ratio")].isNull() && m_loss_ratio_isValid;

    m_mos_isValid = ::OpenAPI::fromJsonValue(m_mos, json[QString("mos")]);
    m_mos_isSet = !json[QString("mos")].isNull() && m_mos_isValid;

    m_window_isValid = ::OpenAPI::fromJsonValue(m_window, json[QString("window")]);
    m_window_isSet = !json[QString("window")].isNull() && m_window_isValid;
}

QString OAICreateOrganizationAlertsProfile_request_alertCondition::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateOrganizationAlertsProfile_request_alertCondition::asJsonObject() const {
    QJsonObject obj;
    if (m_bit_rate_bps_isSet) {
        obj.insert(QString("bit_rate_bps"), ::OpenAPI::toJsonValue(m_bit_rate_bps));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_interface_isSet) {
        obj.insert(QString("interface"), ::OpenAPI::toJsonValue(m_interface));
    }
    if (m_jitter_ms_isSet) {
        obj.insert(QString("jitter_ms"), ::OpenAPI::toJsonValue(m_jitter_ms));
    }
    if (m_latency_ms_isSet) {
        obj.insert(QString("latency_ms"), ::OpenAPI::toJsonValue(m_latency_ms));
    }
    if (m_loss_ratio_isSet) {
        obj.insert(QString("loss_ratio"), ::OpenAPI::toJsonValue(m_loss_ratio));
    }
    if (m_mos_isSet) {
        obj.insert(QString("mos"), ::OpenAPI::toJsonValue(m_mos));
    }
    if (m_window_isSet) {
        obj.insert(QString("window"), ::OpenAPI::toJsonValue(m_window));
    }
    return obj;
}

qint32 OAICreateOrganizationAlertsProfile_request_alertCondition::getBitRateBps() const {
    return m_bit_rate_bps;
}
void OAICreateOrganizationAlertsProfile_request_alertCondition::setBitRateBps(const qint32 &bit_rate_bps) {
    m_bit_rate_bps = bit_rate_bps;
    m_bit_rate_bps_isSet = true;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_bit_rate_bps_Set() const{
    return m_bit_rate_bps_isSet;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_bit_rate_bps_Valid() const{
    return m_bit_rate_bps_isValid;
}

qint32 OAICreateOrganizationAlertsProfile_request_alertCondition::getDuration() const {
    return m_duration;
}
void OAICreateOrganizationAlertsProfile_request_alertCondition::setDuration(const qint32 &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAICreateOrganizationAlertsProfile_request_alertCondition::getInterface() const {
    return m_interface;
}
void OAICreateOrganizationAlertsProfile_request_alertCondition::setInterface(const QString &interface) {
    m_interface = interface;
    m_interface_isSet = true;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_interface_Set() const{
    return m_interface_isSet;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_interface_Valid() const{
    return m_interface_isValid;
}

qint32 OAICreateOrganizationAlertsProfile_request_alertCondition::getJitterMs() const {
    return m_jitter_ms;
}
void OAICreateOrganizationAlertsProfile_request_alertCondition::setJitterMs(const qint32 &jitter_ms) {
    m_jitter_ms = jitter_ms;
    m_jitter_ms_isSet = true;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_jitter_ms_Set() const{
    return m_jitter_ms_isSet;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_jitter_ms_Valid() const{
    return m_jitter_ms_isValid;
}

qint32 OAICreateOrganizationAlertsProfile_request_alertCondition::getLatencyMs() const {
    return m_latency_ms;
}
void OAICreateOrganizationAlertsProfile_request_alertCondition::setLatencyMs(const qint32 &latency_ms) {
    m_latency_ms = latency_ms;
    m_latency_ms_isSet = true;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_latency_ms_Set() const{
    return m_latency_ms_isSet;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_latency_ms_Valid() const{
    return m_latency_ms_isValid;
}

float OAICreateOrganizationAlertsProfile_request_alertCondition::getLossRatio() const {
    return m_loss_ratio;
}
void OAICreateOrganizationAlertsProfile_request_alertCondition::setLossRatio(const float &loss_ratio) {
    m_loss_ratio = loss_ratio;
    m_loss_ratio_isSet = true;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_loss_ratio_Set() const{
    return m_loss_ratio_isSet;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_loss_ratio_Valid() const{
    return m_loss_ratio_isValid;
}

float OAICreateOrganizationAlertsProfile_request_alertCondition::getMos() const {
    return m_mos;
}
void OAICreateOrganizationAlertsProfile_request_alertCondition::setMos(const float &mos) {
    m_mos = mos;
    m_mos_isSet = true;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_mos_Set() const{
    return m_mos_isSet;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_mos_Valid() const{
    return m_mos_isValid;
}

qint32 OAICreateOrganizationAlertsProfile_request_alertCondition::getWindow() const {
    return m_window;
}
void OAICreateOrganizationAlertsProfile_request_alertCondition::setWindow(const qint32 &window) {
    m_window = window;
    m_window_isSet = true;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_window_Set() const{
    return m_window_isSet;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::is_window_Valid() const{
    return m_window_isValid;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bit_rate_bps_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_interface_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_jitter_ms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latency_ms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_loss_ratio_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mos_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_window_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateOrganizationAlertsProfile_request_alertCondition::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
