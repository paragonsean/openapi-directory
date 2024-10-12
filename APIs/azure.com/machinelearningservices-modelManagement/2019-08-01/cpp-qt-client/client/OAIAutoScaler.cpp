/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAutoScaler.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAutoScaler::OAIAutoScaler(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAutoScaler::OAIAutoScaler() {
    this->initializeModel();
}

OAIAutoScaler::~OAIAutoScaler() {}

void OAIAutoScaler::initializeModel() {

    m_autoscale_enabled_isSet = false;
    m_autoscale_enabled_isValid = false;

    m_max_replicas_isSet = false;
    m_max_replicas_isValid = false;

    m_min_replicas_isSet = false;
    m_min_replicas_isValid = false;

    m_refresh_period_in_seconds_isSet = false;
    m_refresh_period_in_seconds_isValid = false;

    m_target_utilization_isSet = false;
    m_target_utilization_isValid = false;
}

void OAIAutoScaler::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAutoScaler::fromJsonObject(QJsonObject json) {

    m_autoscale_enabled_isValid = ::OpenAPI::fromJsonValue(m_autoscale_enabled, json[QString("autoscaleEnabled")]);
    m_autoscale_enabled_isSet = !json[QString("autoscaleEnabled")].isNull() && m_autoscale_enabled_isValid;

    m_max_replicas_isValid = ::OpenAPI::fromJsonValue(m_max_replicas, json[QString("maxReplicas")]);
    m_max_replicas_isSet = !json[QString("maxReplicas")].isNull() && m_max_replicas_isValid;

    m_min_replicas_isValid = ::OpenAPI::fromJsonValue(m_min_replicas, json[QString("minReplicas")]);
    m_min_replicas_isSet = !json[QString("minReplicas")].isNull() && m_min_replicas_isValid;

    m_refresh_period_in_seconds_isValid = ::OpenAPI::fromJsonValue(m_refresh_period_in_seconds, json[QString("refreshPeriodInSeconds")]);
    m_refresh_period_in_seconds_isSet = !json[QString("refreshPeriodInSeconds")].isNull() && m_refresh_period_in_seconds_isValid;

    m_target_utilization_isValid = ::OpenAPI::fromJsonValue(m_target_utilization, json[QString("targetUtilization")]);
    m_target_utilization_isSet = !json[QString("targetUtilization")].isNull() && m_target_utilization_isValid;
}

QString OAIAutoScaler::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAutoScaler::asJsonObject() const {
    QJsonObject obj;
    if (m_autoscale_enabled_isSet) {
        obj.insert(QString("autoscaleEnabled"), ::OpenAPI::toJsonValue(m_autoscale_enabled));
    }
    if (m_max_replicas_isSet) {
        obj.insert(QString("maxReplicas"), ::OpenAPI::toJsonValue(m_max_replicas));
    }
    if (m_min_replicas_isSet) {
        obj.insert(QString("minReplicas"), ::OpenAPI::toJsonValue(m_min_replicas));
    }
    if (m_refresh_period_in_seconds_isSet) {
        obj.insert(QString("refreshPeriodInSeconds"), ::OpenAPI::toJsonValue(m_refresh_period_in_seconds));
    }
    if (m_target_utilization_isSet) {
        obj.insert(QString("targetUtilization"), ::OpenAPI::toJsonValue(m_target_utilization));
    }
    return obj;
}

bool OAIAutoScaler::isAutoscaleEnabled() const {
    return m_autoscale_enabled;
}
void OAIAutoScaler::setAutoscaleEnabled(const bool &autoscale_enabled) {
    m_autoscale_enabled = autoscale_enabled;
    m_autoscale_enabled_isSet = true;
}

bool OAIAutoScaler::is_autoscale_enabled_Set() const{
    return m_autoscale_enabled_isSet;
}

bool OAIAutoScaler::is_autoscale_enabled_Valid() const{
    return m_autoscale_enabled_isValid;
}

qint32 OAIAutoScaler::getMaxReplicas() const {
    return m_max_replicas;
}
void OAIAutoScaler::setMaxReplicas(const qint32 &max_replicas) {
    m_max_replicas = max_replicas;
    m_max_replicas_isSet = true;
}

bool OAIAutoScaler::is_max_replicas_Set() const{
    return m_max_replicas_isSet;
}

bool OAIAutoScaler::is_max_replicas_Valid() const{
    return m_max_replicas_isValid;
}

qint32 OAIAutoScaler::getMinReplicas() const {
    return m_min_replicas;
}
void OAIAutoScaler::setMinReplicas(const qint32 &min_replicas) {
    m_min_replicas = min_replicas;
    m_min_replicas_isSet = true;
}

bool OAIAutoScaler::is_min_replicas_Set() const{
    return m_min_replicas_isSet;
}

bool OAIAutoScaler::is_min_replicas_Valid() const{
    return m_min_replicas_isValid;
}

qint32 OAIAutoScaler::getRefreshPeriodInSeconds() const {
    return m_refresh_period_in_seconds;
}
void OAIAutoScaler::setRefreshPeriodInSeconds(const qint32 &refresh_period_in_seconds) {
    m_refresh_period_in_seconds = refresh_period_in_seconds;
    m_refresh_period_in_seconds_isSet = true;
}

bool OAIAutoScaler::is_refresh_period_in_seconds_Set() const{
    return m_refresh_period_in_seconds_isSet;
}

bool OAIAutoScaler::is_refresh_period_in_seconds_Valid() const{
    return m_refresh_period_in_seconds_isValid;
}

qint32 OAIAutoScaler::getTargetUtilization() const {
    return m_target_utilization;
}
void OAIAutoScaler::setTargetUtilization(const qint32 &target_utilization) {
    m_target_utilization = target_utilization;
    m_target_utilization_isSet = true;
}

bool OAIAutoScaler::is_target_utilization_Set() const{
    return m_target_utilization_isSet;
}

bool OAIAutoScaler::is_target_utilization_Valid() const{
    return m_target_utilization_isValid;
}

bool OAIAutoScaler::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_autoscale_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_replicas_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_replicas_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refresh_period_in_seconds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_utilization_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAutoScaler::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
