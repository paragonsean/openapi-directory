/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISnowMonkeyConfig.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISnowMonkeyConfig::OAISnowMonkeyConfig(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISnowMonkeyConfig::OAISnowMonkeyConfig() {
    this->initializeModel();
}

OAISnowMonkeyConfig::~OAISnowMonkeyConfig() {}

void OAISnowMonkeyConfig::initializeModel() {

    m_chaos_config_isSet = false;
    m_chaos_config_isValid = false;

    m_dry_run_isSet = false;
    m_dry_run_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_include_user_facing_descriptors_isSet = false;
    m_include_user_facing_descriptors_isValid = false;

    m_outage_duration_from_isSet = false;
    m_outage_duration_from_isValid = false;

    m_outage_duration_to_isSet = false;
    m_outage_duration_to_isValid = false;

    m_outage_strategy_isSet = false;
    m_outage_strategy_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_stop_time_isSet = false;
    m_stop_time_isValid = false;

    m_target_groups_isSet = false;
    m_target_groups_isValid = false;

    m_times_per_day_isSet = false;
    m_times_per_day_isValid = false;
}

void OAISnowMonkeyConfig::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISnowMonkeyConfig::fromJsonObject(QJsonObject json) {

    m_chaos_config_isValid = ::OpenAPI::fromJsonValue(m_chaos_config, json[QString("chaosConfig")]);
    m_chaos_config_isSet = !json[QString("chaosConfig")].isNull() && m_chaos_config_isValid;

    m_dry_run_isValid = ::OpenAPI::fromJsonValue(m_dry_run, json[QString("dryRun")]);
    m_dry_run_isSet = !json[QString("dryRun")].isNull() && m_dry_run_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_include_user_facing_descriptors_isValid = ::OpenAPI::fromJsonValue(m_include_user_facing_descriptors, json[QString("includeUserFacingDescriptors")]);
    m_include_user_facing_descriptors_isSet = !json[QString("includeUserFacingDescriptors")].isNull() && m_include_user_facing_descriptors_isValid;

    m_outage_duration_from_isValid = ::OpenAPI::fromJsonValue(m_outage_duration_from, json[QString("outageDurationFrom")]);
    m_outage_duration_from_isSet = !json[QString("outageDurationFrom")].isNull() && m_outage_duration_from_isValid;

    m_outage_duration_to_isValid = ::OpenAPI::fromJsonValue(m_outage_duration_to, json[QString("outageDurationTo")]);
    m_outage_duration_to_isSet = !json[QString("outageDurationTo")].isNull() && m_outage_duration_to_isValid;

    m_outage_strategy_isValid = ::OpenAPI::fromJsonValue(m_outage_strategy, json[QString("outageStrategy")]);
    m_outage_strategy_isSet = !json[QString("outageStrategy")].isNull() && m_outage_strategy_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("startTime")]);
    m_start_time_isSet = !json[QString("startTime")].isNull() && m_start_time_isValid;

    m_stop_time_isValid = ::OpenAPI::fromJsonValue(m_stop_time, json[QString("stopTime")]);
    m_stop_time_isSet = !json[QString("stopTime")].isNull() && m_stop_time_isValid;

    m_target_groups_isValid = ::OpenAPI::fromJsonValue(m_target_groups, json[QString("targetGroups")]);
    m_target_groups_isSet = !json[QString("targetGroups")].isNull() && m_target_groups_isValid;

    m_times_per_day_isValid = ::OpenAPI::fromJsonValue(m_times_per_day, json[QString("timesPerDay")]);
    m_times_per_day_isSet = !json[QString("timesPerDay")].isNull() && m_times_per_day_isValid;
}

QString OAISnowMonkeyConfig::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISnowMonkeyConfig::asJsonObject() const {
    QJsonObject obj;
    if (m_chaos_config.isSet()) {
        obj.insert(QString("chaosConfig"), ::OpenAPI::toJsonValue(m_chaos_config));
    }
    if (m_dry_run_isSet) {
        obj.insert(QString("dryRun"), ::OpenAPI::toJsonValue(m_dry_run));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_include_user_facing_descriptors_isSet) {
        obj.insert(QString("includeUserFacingDescriptors"), ::OpenAPI::toJsonValue(m_include_user_facing_descriptors));
    }
    if (m_outage_duration_from_isSet) {
        obj.insert(QString("outageDurationFrom"), ::OpenAPI::toJsonValue(m_outage_duration_from));
    }
    if (m_outage_duration_to_isSet) {
        obj.insert(QString("outageDurationTo"), ::OpenAPI::toJsonValue(m_outage_duration_to));
    }
    if (m_outage_strategy.isSet()) {
        obj.insert(QString("outageStrategy"), ::OpenAPI::toJsonValue(m_outage_strategy));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("startTime"), ::OpenAPI::toJsonValue(m_start_time));
    }
    if (m_stop_time_isSet) {
        obj.insert(QString("stopTime"), ::OpenAPI::toJsonValue(m_stop_time));
    }
    if (m_target_groups.size() > 0) {
        obj.insert(QString("targetGroups"), ::OpenAPI::toJsonValue(m_target_groups));
    }
    if (m_times_per_day_isSet) {
        obj.insert(QString("timesPerDay"), ::OpenAPI::toJsonValue(m_times_per_day));
    }
    return obj;
}

OAIChaosConfig OAISnowMonkeyConfig::getChaosConfig() const {
    return m_chaos_config;
}
void OAISnowMonkeyConfig::setChaosConfig(const OAIChaosConfig &chaos_config) {
    m_chaos_config = chaos_config;
    m_chaos_config_isSet = true;
}

bool OAISnowMonkeyConfig::is_chaos_config_Set() const{
    return m_chaos_config_isSet;
}

bool OAISnowMonkeyConfig::is_chaos_config_Valid() const{
    return m_chaos_config_isValid;
}

bool OAISnowMonkeyConfig::isDryRun() const {
    return m_dry_run;
}
void OAISnowMonkeyConfig::setDryRun(const bool &dry_run) {
    m_dry_run = dry_run;
    m_dry_run_isSet = true;
}

bool OAISnowMonkeyConfig::is_dry_run_Set() const{
    return m_dry_run_isSet;
}

bool OAISnowMonkeyConfig::is_dry_run_Valid() const{
    return m_dry_run_isValid;
}

bool OAISnowMonkeyConfig::isEnabled() const {
    return m_enabled;
}
void OAISnowMonkeyConfig::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAISnowMonkeyConfig::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAISnowMonkeyConfig::is_enabled_Valid() const{
    return m_enabled_isValid;
}

bool OAISnowMonkeyConfig::isIncludeUserFacingDescriptors() const {
    return m_include_user_facing_descriptors;
}
void OAISnowMonkeyConfig::setIncludeUserFacingDescriptors(const bool &include_user_facing_descriptors) {
    m_include_user_facing_descriptors = include_user_facing_descriptors;
    m_include_user_facing_descriptors_isSet = true;
}

bool OAISnowMonkeyConfig::is_include_user_facing_descriptors_Set() const{
    return m_include_user_facing_descriptors_isSet;
}

bool OAISnowMonkeyConfig::is_include_user_facing_descriptors_Valid() const{
    return m_include_user_facing_descriptors_isValid;
}

qint32 OAISnowMonkeyConfig::getOutageDurationFrom() const {
    return m_outage_duration_from;
}
void OAISnowMonkeyConfig::setOutageDurationFrom(const qint32 &outage_duration_from) {
    m_outage_duration_from = outage_duration_from;
    m_outage_duration_from_isSet = true;
}

bool OAISnowMonkeyConfig::is_outage_duration_from_Set() const{
    return m_outage_duration_from_isSet;
}

bool OAISnowMonkeyConfig::is_outage_duration_from_Valid() const{
    return m_outage_duration_from_isValid;
}

qint32 OAISnowMonkeyConfig::getOutageDurationTo() const {
    return m_outage_duration_to;
}
void OAISnowMonkeyConfig::setOutageDurationTo(const qint32 &outage_duration_to) {
    m_outage_duration_to = outage_duration_to;
    m_outage_duration_to_isSet = true;
}

bool OAISnowMonkeyConfig::is_outage_duration_to_Set() const{
    return m_outage_duration_to_isSet;
}

bool OAISnowMonkeyConfig::is_outage_duration_to_Valid() const{
    return m_outage_duration_to_isValid;
}

OAIOutageStrategy OAISnowMonkeyConfig::getOutageStrategy() const {
    return m_outage_strategy;
}
void OAISnowMonkeyConfig::setOutageStrategy(const OAIOutageStrategy &outage_strategy) {
    m_outage_strategy = outage_strategy;
    m_outage_strategy_isSet = true;
}

bool OAISnowMonkeyConfig::is_outage_strategy_Set() const{
    return m_outage_strategy_isSet;
}

bool OAISnowMonkeyConfig::is_outage_strategy_Valid() const{
    return m_outage_strategy_isValid;
}

QString OAISnowMonkeyConfig::getStartTime() const {
    return m_start_time;
}
void OAISnowMonkeyConfig::setStartTime(const QString &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAISnowMonkeyConfig::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAISnowMonkeyConfig::is_start_time_Valid() const{
    return m_start_time_isValid;
}

QString OAISnowMonkeyConfig::getStopTime() const {
    return m_stop_time;
}
void OAISnowMonkeyConfig::setStopTime(const QString &stop_time) {
    m_stop_time = stop_time;
    m_stop_time_isSet = true;
}

bool OAISnowMonkeyConfig::is_stop_time_Set() const{
    return m_stop_time_isSet;
}

bool OAISnowMonkeyConfig::is_stop_time_Valid() const{
    return m_stop_time_isValid;
}

QList<QString> OAISnowMonkeyConfig::getTargetGroups() const {
    return m_target_groups;
}
void OAISnowMonkeyConfig::setTargetGroups(const QList<QString> &target_groups) {
    m_target_groups = target_groups;
    m_target_groups_isSet = true;
}

bool OAISnowMonkeyConfig::is_target_groups_Set() const{
    return m_target_groups_isSet;
}

bool OAISnowMonkeyConfig::is_target_groups_Valid() const{
    return m_target_groups_isValid;
}

qint32 OAISnowMonkeyConfig::getTimesPerDay() const {
    return m_times_per_day;
}
void OAISnowMonkeyConfig::setTimesPerDay(const qint32 &times_per_day) {
    m_times_per_day = times_per_day;
    m_times_per_day_isSet = true;
}

bool OAISnowMonkeyConfig::is_times_per_day_Set() const{
    return m_times_per_day_isSet;
}

bool OAISnowMonkeyConfig::is_times_per_day_Valid() const{
    return m_times_per_day_isValid;
}

bool OAISnowMonkeyConfig::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_chaos_config.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_dry_run_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_user_facing_descriptors_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_outage_duration_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_outage_duration_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_outage_strategy.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stop_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_times_per_day_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISnowMonkeyConfig::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_chaos_config_isValid && m_dry_run_isValid && m_enabled_isValid && m_include_user_facing_descriptors_isValid && m_outage_duration_from_isValid && m_outage_duration_to_isValid && m_outage_strategy_isValid && m_start_time_isValid && m_stop_time_isValid && m_target_groups_isValid && m_times_per_day_isValid && true;
}

} // namespace OpenAPI
