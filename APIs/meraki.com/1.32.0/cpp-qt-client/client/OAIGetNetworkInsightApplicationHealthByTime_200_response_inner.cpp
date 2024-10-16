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

#include "OAIGetNetworkInsightApplicationHealthByTime_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::OAIGetNetworkInsightApplicationHealthByTime_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::OAIGetNetworkInsightApplicationHealthByTime_200_response_inner() {
    this->initializeModel();
}

OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::~OAIGetNetworkInsightApplicationHealthByTime_200_response_inner() {}

void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::initializeModel() {

    m_end_ts_isSet = false;
    m_end_ts_isValid = false;

    m_lan_goodput_isSet = false;
    m_lan_goodput_isValid = false;

    m_lan_latency_ms_isSet = false;
    m_lan_latency_ms_isValid = false;

    m_lan_loss_percent_isSet = false;
    m_lan_loss_percent_isValid = false;

    m_num_clients_isSet = false;
    m_num_clients_isValid = false;

    m_recv_isSet = false;
    m_recv_isValid = false;

    m_response_duration_isSet = false;
    m_response_duration_isValid = false;

    m_sent_isSet = false;
    m_sent_isValid = false;

    m_start_ts_isSet = false;
    m_start_ts_isValid = false;

    m_wan_goodput_isSet = false;
    m_wan_goodput_isValid = false;

    m_wan_latency_ms_isSet = false;
    m_wan_latency_ms_isValid = false;

    m_wan_loss_percent_isSet = false;
    m_wan_loss_percent_isValid = false;
}

void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::fromJsonObject(QJsonObject json) {

    m_end_ts_isValid = ::OpenAPI::fromJsonValue(m_end_ts, json[QString("endTs")]);
    m_end_ts_isSet = !json[QString("endTs")].isNull() && m_end_ts_isValid;

    m_lan_goodput_isValid = ::OpenAPI::fromJsonValue(m_lan_goodput, json[QString("lanGoodput")]);
    m_lan_goodput_isSet = !json[QString("lanGoodput")].isNull() && m_lan_goodput_isValid;

    m_lan_latency_ms_isValid = ::OpenAPI::fromJsonValue(m_lan_latency_ms, json[QString("lanLatencyMs")]);
    m_lan_latency_ms_isSet = !json[QString("lanLatencyMs")].isNull() && m_lan_latency_ms_isValid;

    m_lan_loss_percent_isValid = ::OpenAPI::fromJsonValue(m_lan_loss_percent, json[QString("lanLossPercent")]);
    m_lan_loss_percent_isSet = !json[QString("lanLossPercent")].isNull() && m_lan_loss_percent_isValid;

    m_num_clients_isValid = ::OpenAPI::fromJsonValue(m_num_clients, json[QString("numClients")]);
    m_num_clients_isSet = !json[QString("numClients")].isNull() && m_num_clients_isValid;

    m_recv_isValid = ::OpenAPI::fromJsonValue(m_recv, json[QString("recv")]);
    m_recv_isSet = !json[QString("recv")].isNull() && m_recv_isValid;

    m_response_duration_isValid = ::OpenAPI::fromJsonValue(m_response_duration, json[QString("responseDuration")]);
    m_response_duration_isSet = !json[QString("responseDuration")].isNull() && m_response_duration_isValid;

    m_sent_isValid = ::OpenAPI::fromJsonValue(m_sent, json[QString("sent")]);
    m_sent_isSet = !json[QString("sent")].isNull() && m_sent_isValid;

    m_start_ts_isValid = ::OpenAPI::fromJsonValue(m_start_ts, json[QString("startTs")]);
    m_start_ts_isSet = !json[QString("startTs")].isNull() && m_start_ts_isValid;

    m_wan_goodput_isValid = ::OpenAPI::fromJsonValue(m_wan_goodput, json[QString("wanGoodput")]);
    m_wan_goodput_isSet = !json[QString("wanGoodput")].isNull() && m_wan_goodput_isValid;

    m_wan_latency_ms_isValid = ::OpenAPI::fromJsonValue(m_wan_latency_ms, json[QString("wanLatencyMs")]);
    m_wan_latency_ms_isSet = !json[QString("wanLatencyMs")].isNull() && m_wan_latency_ms_isValid;

    m_wan_loss_percent_isValid = ::OpenAPI::fromJsonValue(m_wan_loss_percent, json[QString("wanLossPercent")]);
    m_wan_loss_percent_isSet = !json[QString("wanLossPercent")].isNull() && m_wan_loss_percent_isValid;
}

QString OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_end_ts_isSet) {
        obj.insert(QString("endTs"), ::OpenAPI::toJsonValue(m_end_ts));
    }
    if (m_lan_goodput_isSet) {
        obj.insert(QString("lanGoodput"), ::OpenAPI::toJsonValue(m_lan_goodput));
    }
    if (m_lan_latency_ms_isSet) {
        obj.insert(QString("lanLatencyMs"), ::OpenAPI::toJsonValue(m_lan_latency_ms));
    }
    if (m_lan_loss_percent_isSet) {
        obj.insert(QString("lanLossPercent"), ::OpenAPI::toJsonValue(m_lan_loss_percent));
    }
    if (m_num_clients_isSet) {
        obj.insert(QString("numClients"), ::OpenAPI::toJsonValue(m_num_clients));
    }
    if (m_recv_isSet) {
        obj.insert(QString("recv"), ::OpenAPI::toJsonValue(m_recv));
    }
    if (m_response_duration_isSet) {
        obj.insert(QString("responseDuration"), ::OpenAPI::toJsonValue(m_response_duration));
    }
    if (m_sent_isSet) {
        obj.insert(QString("sent"), ::OpenAPI::toJsonValue(m_sent));
    }
    if (m_start_ts_isSet) {
        obj.insert(QString("startTs"), ::OpenAPI::toJsonValue(m_start_ts));
    }
    if (m_wan_goodput_isSet) {
        obj.insert(QString("wanGoodput"), ::OpenAPI::toJsonValue(m_wan_goodput));
    }
    if (m_wan_latency_ms_isSet) {
        obj.insert(QString("wanLatencyMs"), ::OpenAPI::toJsonValue(m_wan_latency_ms));
    }
    if (m_wan_loss_percent_isSet) {
        obj.insert(QString("wanLossPercent"), ::OpenAPI::toJsonValue(m_wan_loss_percent));
    }
    return obj;
}

QDateTime OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getEndTs() const {
    return m_end_ts;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setEndTs(const QDateTime &end_ts) {
    m_end_ts = end_ts;
    m_end_ts_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_end_ts_Set() const{
    return m_end_ts_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_end_ts_Valid() const{
    return m_end_ts_isValid;
}

qint32 OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getLanGoodput() const {
    return m_lan_goodput;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setLanGoodput(const qint32 &lan_goodput) {
    m_lan_goodput = lan_goodput;
    m_lan_goodput_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_lan_goodput_Set() const{
    return m_lan_goodput_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_lan_goodput_Valid() const{
    return m_lan_goodput_isValid;
}

float OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getLanLatencyMs() const {
    return m_lan_latency_ms;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setLanLatencyMs(const float &lan_latency_ms) {
    m_lan_latency_ms = lan_latency_ms;
    m_lan_latency_ms_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_lan_latency_ms_Set() const{
    return m_lan_latency_ms_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_lan_latency_ms_Valid() const{
    return m_lan_latency_ms_isValid;
}

float OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getLanLossPercent() const {
    return m_lan_loss_percent;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setLanLossPercent(const float &lan_loss_percent) {
    m_lan_loss_percent = lan_loss_percent;
    m_lan_loss_percent_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_lan_loss_percent_Set() const{
    return m_lan_loss_percent_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_lan_loss_percent_Valid() const{
    return m_lan_loss_percent_isValid;
}

qint32 OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getNumClients() const {
    return m_num_clients;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setNumClients(const qint32 &num_clients) {
    m_num_clients = num_clients;
    m_num_clients_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_num_clients_Set() const{
    return m_num_clients_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_num_clients_Valid() const{
    return m_num_clients_isValid;
}

qint32 OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getRecv() const {
    return m_recv;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setRecv(const qint32 &recv) {
    m_recv = recv;
    m_recv_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_recv_Set() const{
    return m_recv_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_recv_Valid() const{
    return m_recv_isValid;
}

qint32 OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getResponseDuration() const {
    return m_response_duration;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setResponseDuration(const qint32 &response_duration) {
    m_response_duration = response_duration;
    m_response_duration_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_response_duration_Set() const{
    return m_response_duration_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_response_duration_Valid() const{
    return m_response_duration_isValid;
}

qint32 OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getSent() const {
    return m_sent;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setSent(const qint32 &sent) {
    m_sent = sent;
    m_sent_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_sent_Set() const{
    return m_sent_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_sent_Valid() const{
    return m_sent_isValid;
}

QDateTime OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getStartTs() const {
    return m_start_ts;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setStartTs(const QDateTime &start_ts) {
    m_start_ts = start_ts;
    m_start_ts_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_start_ts_Set() const{
    return m_start_ts_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_start_ts_Valid() const{
    return m_start_ts_isValid;
}

qint32 OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getWanGoodput() const {
    return m_wan_goodput;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setWanGoodput(const qint32 &wan_goodput) {
    m_wan_goodput = wan_goodput;
    m_wan_goodput_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_wan_goodput_Set() const{
    return m_wan_goodput_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_wan_goodput_Valid() const{
    return m_wan_goodput_isValid;
}

float OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getWanLatencyMs() const {
    return m_wan_latency_ms;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setWanLatencyMs(const float &wan_latency_ms) {
    m_wan_latency_ms = wan_latency_ms;
    m_wan_latency_ms_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_wan_latency_ms_Set() const{
    return m_wan_latency_ms_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_wan_latency_ms_Valid() const{
    return m_wan_latency_ms_isValid;
}

float OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::getWanLossPercent() const {
    return m_wan_loss_percent;
}
void OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::setWanLossPercent(const float &wan_loss_percent) {
    m_wan_loss_percent = wan_loss_percent;
    m_wan_loss_percent_isSet = true;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_wan_loss_percent_Set() const{
    return m_wan_loss_percent_isSet;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::is_wan_loss_percent_Valid() const{
    return m_wan_loss_percent_isValid;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_end_ts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lan_goodput_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lan_latency_ms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lan_loss_percent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_num_clients_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recv_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_response_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_ts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wan_goodput_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wan_latency_ms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wan_loss_percent_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkInsightApplicationHealthByTime_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
