/**
 * Azure SQL Database
 * Provides create, read, update and delete functionality for Azure SQL Database resources including recommendations and operations.
 *
 * The version of the OpenAPI document: 2014-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRecommendedElasticPoolListMetricsResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRecommendedElasticPoolListMetricsResult::OAIRecommendedElasticPoolListMetricsResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRecommendedElasticPoolListMetricsResult::OAIRecommendedElasticPoolListMetricsResult() {
    this->initializeModel();
}

OAIRecommendedElasticPoolListMetricsResult::~OAIRecommendedElasticPoolListMetricsResult() {}

void OAIRecommendedElasticPoolListMetricsResult::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIRecommendedElasticPoolListMetricsResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRecommendedElasticPoolListMetricsResult::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIRecommendedElasticPoolListMetricsResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRecommendedElasticPoolListMetricsResult::asJsonObject() const {
    QJsonObject obj;
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QList<OAIRecommendedElasticPoolMetric> OAIRecommendedElasticPoolListMetricsResult::getValue() const {
    return m_value;
}
void OAIRecommendedElasticPoolListMetricsResult::setValue(const QList<OAIRecommendedElasticPoolMetric> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIRecommendedElasticPoolListMetricsResult::is_value_Set() const{
    return m_value_isSet;
}

bool OAIRecommendedElasticPoolListMetricsResult::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIRecommendedElasticPoolListMetricsResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRecommendedElasticPoolListMetricsResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid && true;
}

} // namespace OpenAPI
