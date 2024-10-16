/**
 * Football Prediction API
 * The Football Prediction API allows developers to get predictions for upcoming football (soccer) matches, results for past matches, and performance monitoring for statistical models.
 *
 * The version of the OpenAPI document: 2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days() {
    this->initializeModel();
}

OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::~OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days() {}

void OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::initializeModel() {

    m_lost_isSet = false;
    m_lost_isValid = false;

    m_pending_isSet = false;
    m_pending_isValid = false;

    m_postponed_isSet = false;
    m_postponed_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;

    m_won_isSet = false;
    m_won_isValid = false;
}

void OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::fromJsonObject(QJsonObject json) {

    m_lost_isValid = ::OpenAPI::fromJsonValue(m_lost, json[QString("lost")]);
    m_lost_isSet = !json[QString("lost")].isNull() && m_lost_isValid;

    m_pending_isValid = ::OpenAPI::fromJsonValue(m_pending, json[QString("pending")]);
    m_pending_isSet = !json[QString("pending")].isNull() && m_pending_isValid;

    m_postponed_isValid = ::OpenAPI::fromJsonValue(m_postponed, json[QString("postponed")]);
    m_postponed_isSet = !json[QString("postponed")].isNull() && m_postponed_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;

    m_won_isValid = ::OpenAPI::fromJsonValue(m_won, json[QString("won")]);
    m_won_isSet = !json[QString("won")].isNull() && m_won_isValid;
}

QString OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::asJsonObject() const {
    QJsonObject obj;
    if (m_lost_isSet) {
        obj.insert(QString("lost"), ::OpenAPI::toJsonValue(m_lost));
    }
    if (m_pending_isSet) {
        obj.insert(QString("pending"), ::OpenAPI::toJsonValue(m_pending));
    }
    if (m_postponed_isSet) {
        obj.insert(QString("postponed"), ::OpenAPI::toJsonValue(m_postponed));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    if (m_won_isSet) {
        obj.insert(QString("won"), ::OpenAPI::toJsonValue(m_won));
    }
    return obj;
}

qint32 OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::getLost() const {
    return m_lost;
}
void OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::setLost(const qint32 &lost) {
    m_lost = lost;
    m_lost_isSet = true;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_lost_Set() const{
    return m_lost_isSet;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_lost_Valid() const{
    return m_lost_isValid;
}

qint32 OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::getPending() const {
    return m_pending;
}
void OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::setPending(const qint32 &pending) {
    m_pending = pending;
    m_pending_isSet = true;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_pending_Set() const{
    return m_pending_isSet;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_pending_Valid() const{
    return m_pending_isValid;
}

qint32 OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::getPostponed() const {
    return m_postponed;
}
void OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::setPostponed(const qint32 &postponed) {
    m_postponed = postponed;
    m_postponed_isSet = true;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_postponed_Set() const{
    return m_postponed_isSet;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_postponed_Valid() const{
    return m_postponed_isValid;
}

qint32 OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::getTotal() const {
    return m_total;
}
void OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::setTotal(const qint32 &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_total_Set() const{
    return m_total_isSet;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_total_Valid() const{
    return m_total_isValid;
}

qint32 OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::getWon() const {
    return m_won;
}
void OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::setWon(const qint32 &won) {
    m_won = won;
    m_won_isSet = true;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_won_Set() const{
    return m_won_isSet;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::is_won_Valid() const{
    return m_won_isValid;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_lost_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pending_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postponed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_won_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_api_v2_performance_stats_get_200_response_data_details_last_14_days::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
