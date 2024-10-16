/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGrowthRateValues.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGrowthRateValues::OAIGrowthRateValues(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGrowthRateValues::OAIGrowthRateValues() {
    this->initializeModel();
}

OAIGrowthRateValues::~OAIGrowthRateValues() {}

void OAIGrowthRateValues::initializeModel() {

    m_additional_growth_percent_isSet = false;
    m_additional_growth_percent_isValid = false;

    m_is_inflation_adjusted_isSet = false;
    m_is_inflation_adjusted_isValid = false;

    m_total_growth_isSet = false;
    m_total_growth_isValid = false;
}

void OAIGrowthRateValues::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGrowthRateValues::fromJsonObject(QJsonObject json) {

    m_additional_growth_percent_isValid = ::OpenAPI::fromJsonValue(m_additional_growth_percent, json[QString("additionalGrowthPercent")]);
    m_additional_growth_percent_isSet = !json[QString("additionalGrowthPercent")].isNull() && m_additional_growth_percent_isValid;

    m_is_inflation_adjusted_isValid = ::OpenAPI::fromJsonValue(m_is_inflation_adjusted, json[QString("isInflationAdjusted")]);
    m_is_inflation_adjusted_isSet = !json[QString("isInflationAdjusted")].isNull() && m_is_inflation_adjusted_isValid;

    m_total_growth_isValid = ::OpenAPI::fromJsonValue(m_total_growth, json[QString("totalGrowth")]);
    m_total_growth_isSet = !json[QString("totalGrowth")].isNull() && m_total_growth_isValid;
}

QString OAIGrowthRateValues::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGrowthRateValues::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_growth_percent.isSet()) {
        obj.insert(QString("additionalGrowthPercent"), ::OpenAPI::toJsonValue(m_additional_growth_percent));
    }
    if (m_is_inflation_adjusted_isSet) {
        obj.insert(QString("isInflationAdjusted"), ::OpenAPI::toJsonValue(m_is_inflation_adjusted));
    }
    if (m_total_growth.isSet()) {
        obj.insert(QString("totalGrowth"), ::OpenAPI::toJsonValue(m_total_growth));
    }
    return obj;
}

OAIPercent OAIGrowthRateValues::getAdditionalGrowthPercent() const {
    return m_additional_growth_percent;
}
void OAIGrowthRateValues::setAdditionalGrowthPercent(const OAIPercent &additional_growth_percent) {
    m_additional_growth_percent = additional_growth_percent;
    m_additional_growth_percent_isSet = true;
}

bool OAIGrowthRateValues::is_additional_growth_percent_Set() const{
    return m_additional_growth_percent_isSet;
}

bool OAIGrowthRateValues::is_additional_growth_percent_Valid() const{
    return m_additional_growth_percent_isValid;
}

bool OAIGrowthRateValues::isIsInflationAdjusted() const {
    return m_is_inflation_adjusted;
}
void OAIGrowthRateValues::setIsInflationAdjusted(const bool &is_inflation_adjusted) {
    m_is_inflation_adjusted = is_inflation_adjusted;
    m_is_inflation_adjusted_isSet = true;
}

bool OAIGrowthRateValues::is_is_inflation_adjusted_Set() const{
    return m_is_inflation_adjusted_isSet;
}

bool OAIGrowthRateValues::is_is_inflation_adjusted_Valid() const{
    return m_is_inflation_adjusted_isValid;
}

OAIPercent OAIGrowthRateValues::getTotalGrowth() const {
    return m_total_growth;
}
void OAIGrowthRateValues::setTotalGrowth(const OAIPercent &total_growth) {
    m_total_growth = total_growth;
    m_total_growth_isSet = true;
}

bool OAIGrowthRateValues::is_total_growth_Set() const{
    return m_total_growth_isSet;
}

bool OAIGrowthRateValues::is_total_growth_Valid() const{
    return m_total_growth_isValid;
}

bool OAIGrowthRateValues::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_growth_percent.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_inflation_adjusted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_growth.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGrowthRateValues::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
