/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMetrics.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMetrics::OAIMetrics(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMetrics::OAIMetrics() {
    this->initializeModel();
}

OAIMetrics::~OAIMetrics() {}

void OAIMetrics::initializeModel() {

    m_dimensions_isSet = false;
    m_dimensions_isValid = false;

    m_end_time_isSet = false;
    m_end_time_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_primary_aggregation_isSet = false;
    m_primary_aggregation_isValid = false;

    m_resource_id_isSet = false;
    m_resource_id_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_time_grain_isSet = false;
    m_time_grain_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_unit_isSet = false;
    m_unit_isValid = false;

    m_values_isSet = false;
    m_values_isValid = false;
}

void OAIMetrics::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMetrics::fromJsonObject(QJsonObject json) {

    m_dimensions_isValid = ::OpenAPI::fromJsonValue(m_dimensions, json[QString("dimensions")]);
    m_dimensions_isSet = !json[QString("dimensions")].isNull() && m_dimensions_isValid;

    m_end_time_isValid = ::OpenAPI::fromJsonValue(m_end_time, json[QString("endTime")]);
    m_end_time_isSet = !json[QString("endTime")].isNull() && m_end_time_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_primary_aggregation_isValid = ::OpenAPI::fromJsonValue(m_primary_aggregation, json[QString("primaryAggregation")]);
    m_primary_aggregation_isSet = !json[QString("primaryAggregation")].isNull() && m_primary_aggregation_isValid;

    m_resource_id_isValid = ::OpenAPI::fromJsonValue(m_resource_id, json[QString("resourceId")]);
    m_resource_id_isSet = !json[QString("resourceId")].isNull() && m_resource_id_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("startTime")]);
    m_start_time_isSet = !json[QString("startTime")].isNull() && m_start_time_isValid;

    m_time_grain_isValid = ::OpenAPI::fromJsonValue(m_time_grain, json[QString("timeGrain")]);
    m_time_grain_isSet = !json[QString("timeGrain")].isNull() && m_time_grain_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_unit_isValid = ::OpenAPI::fromJsonValue(m_unit, json[QString("unit")]);
    m_unit_isSet = !json[QString("unit")].isNull() && m_unit_isValid;

    m_values_isValid = ::OpenAPI::fromJsonValue(m_values, json[QString("values")]);
    m_values_isSet = !json[QString("values")].isNull() && m_values_isValid;
}

QString OAIMetrics::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMetrics::asJsonObject() const {
    QJsonObject obj;
    if (m_dimensions.size() > 0) {
        obj.insert(QString("dimensions"), ::OpenAPI::toJsonValue(m_dimensions));
    }
    if (m_end_time_isSet) {
        obj.insert(QString("endTime"), ::OpenAPI::toJsonValue(m_end_time));
    }
    if (m_name.isSet()) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_primary_aggregation_isSet) {
        obj.insert(QString("primaryAggregation"), ::OpenAPI::toJsonValue(m_primary_aggregation));
    }
    if (m_resource_id_isSet) {
        obj.insert(QString("resourceId"), ::OpenAPI::toJsonValue(m_resource_id));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("startTime"), ::OpenAPI::toJsonValue(m_start_time));
    }
    if (m_time_grain_isSet) {
        obj.insert(QString("timeGrain"), ::OpenAPI::toJsonValue(m_time_grain));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_unit_isSet) {
        obj.insert(QString("unit"), ::OpenAPI::toJsonValue(m_unit));
    }
    if (m_values.size() > 0) {
        obj.insert(QString("values"), ::OpenAPI::toJsonValue(m_values));
    }
    return obj;
}

QList<OAIMetricDimension> OAIMetrics::getDimensions() const {
    return m_dimensions;
}
void OAIMetrics::setDimensions(const QList<OAIMetricDimension> &dimensions) {
    m_dimensions = dimensions;
    m_dimensions_isSet = true;
}

bool OAIMetrics::is_dimensions_Set() const{
    return m_dimensions_isSet;
}

bool OAIMetrics::is_dimensions_Valid() const{
    return m_dimensions_isValid;
}

QDateTime OAIMetrics::getEndTime() const {
    return m_end_time;
}
void OAIMetrics::setEndTime(const QDateTime &end_time) {
    m_end_time = end_time;
    m_end_time_isSet = true;
}

bool OAIMetrics::is_end_time_Set() const{
    return m_end_time_isSet;
}

bool OAIMetrics::is_end_time_Valid() const{
    return m_end_time_isValid;
}

OAIMetricName OAIMetrics::getName() const {
    return m_name;
}
void OAIMetrics::setName(const OAIMetricName &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIMetrics::is_name_Set() const{
    return m_name_isSet;
}

bool OAIMetrics::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIMetrics::getPrimaryAggregation() const {
    return m_primary_aggregation;
}
void OAIMetrics::setPrimaryAggregation(const QString &primary_aggregation) {
    m_primary_aggregation = primary_aggregation;
    m_primary_aggregation_isSet = true;
}

bool OAIMetrics::is_primary_aggregation_Set() const{
    return m_primary_aggregation_isSet;
}

bool OAIMetrics::is_primary_aggregation_Valid() const{
    return m_primary_aggregation_isValid;
}

QString OAIMetrics::getResourceId() const {
    return m_resource_id;
}
void OAIMetrics::setResourceId(const QString &resource_id) {
    m_resource_id = resource_id;
    m_resource_id_isSet = true;
}

bool OAIMetrics::is_resource_id_Set() const{
    return m_resource_id_isSet;
}

bool OAIMetrics::is_resource_id_Valid() const{
    return m_resource_id_isValid;
}

QDateTime OAIMetrics::getStartTime() const {
    return m_start_time;
}
void OAIMetrics::setStartTime(const QDateTime &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAIMetrics::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAIMetrics::is_start_time_Valid() const{
    return m_start_time_isValid;
}

QString OAIMetrics::getTimeGrain() const {
    return m_time_grain;
}
void OAIMetrics::setTimeGrain(const QString &time_grain) {
    m_time_grain = time_grain;
    m_time_grain_isSet = true;
}

bool OAIMetrics::is_time_grain_Set() const{
    return m_time_grain_isSet;
}

bool OAIMetrics::is_time_grain_Valid() const{
    return m_time_grain_isValid;
}

QString OAIMetrics::getType() const {
    return m_type;
}
void OAIMetrics::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIMetrics::is_type_Set() const{
    return m_type_isSet;
}

bool OAIMetrics::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIMetrics::getUnit() const {
    return m_unit;
}
void OAIMetrics::setUnit(const QString &unit) {
    m_unit = unit;
    m_unit_isSet = true;
}

bool OAIMetrics::is_unit_Set() const{
    return m_unit_isSet;
}

bool OAIMetrics::is_unit_Valid() const{
    return m_unit_isValid;
}

QList<OAIMetricData> OAIMetrics::getValues() const {
    return m_values;
}
void OAIMetrics::setValues(const QList<OAIMetricData> &values) {
    m_values = values;
    m_values_isSet = true;
}

bool OAIMetrics::is_values_Set() const{
    return m_values_isSet;
}

bool OAIMetrics::is_values_Valid() const{
    return m_values_isValid;
}

bool OAIMetrics::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dimensions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_aggregation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_grain_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_values.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMetrics::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
