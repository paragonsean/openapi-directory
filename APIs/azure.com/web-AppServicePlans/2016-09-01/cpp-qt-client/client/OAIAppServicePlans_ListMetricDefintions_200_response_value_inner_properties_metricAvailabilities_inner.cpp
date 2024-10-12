/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner() {
    this->initializeModel();
}

OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::~OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner() {}

void OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::initializeModel() {

    m_retention_isSet = false;
    m_retention_isValid = false;

    m_time_grain_isSet = false;
    m_time_grain_isValid = false;
}

void OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::fromJsonObject(QJsonObject json) {

    m_retention_isValid = ::OpenAPI::fromJsonValue(m_retention, json[QString("retention")]);
    m_retention_isSet = !json[QString("retention")].isNull() && m_retention_isValid;

    m_time_grain_isValid = ::OpenAPI::fromJsonValue(m_time_grain, json[QString("timeGrain")]);
    m_time_grain_isSet = !json[QString("timeGrain")].isNull() && m_time_grain_isValid;
}

QString OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_retention_isSet) {
        obj.insert(QString("retention"), ::OpenAPI::toJsonValue(m_retention));
    }
    if (m_time_grain_isSet) {
        obj.insert(QString("timeGrain"), ::OpenAPI::toJsonValue(m_time_grain));
    }
    return obj;
}

QString OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::getRetention() const {
    return m_retention;
}
void OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::setRetention(const QString &retention) {
    m_retention = retention;
    m_retention_isSet = true;
}

bool OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::is_retention_Set() const{
    return m_retention_isSet;
}

bool OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::is_retention_Valid() const{
    return m_retention_isValid;
}

QString OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::getTimeGrain() const {
    return m_time_grain;
}
void OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::setTimeGrain(const QString &time_grain) {
    m_time_grain = time_grain;
    m_time_grain_isSet = true;
}

bool OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::is_time_grain_Set() const{
    return m_time_grain_isSet;
}

bool OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::is_time_grain_Valid() const{
    return m_time_grain_isValid;
}

bool OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_retention_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_grain_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListMetricDefintions_200_response_value_inner_properties_metricAvailabilities_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
