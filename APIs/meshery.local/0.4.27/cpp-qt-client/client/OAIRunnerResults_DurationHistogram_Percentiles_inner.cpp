/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRunnerResults_DurationHistogram_Percentiles_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRunnerResults_DurationHistogram_Percentiles_inner::OAIRunnerResults_DurationHistogram_Percentiles_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRunnerResults_DurationHistogram_Percentiles_inner::OAIRunnerResults_DurationHistogram_Percentiles_inner() {
    this->initializeModel();
}

OAIRunnerResults_DurationHistogram_Percentiles_inner::~OAIRunnerResults_DurationHistogram_Percentiles_inner() {}

void OAIRunnerResults_DurationHistogram_Percentiles_inner::initializeModel() {

    m_percentile_isSet = false;
    m_percentile_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIRunnerResults_DurationHistogram_Percentiles_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRunnerResults_DurationHistogram_Percentiles_inner::fromJsonObject(QJsonObject json) {

    m_percentile_isValid = ::OpenAPI::fromJsonValue(m_percentile, json[QString("Percentile")]);
    m_percentile_isSet = !json[QString("Percentile")].isNull() && m_percentile_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("Value")]);
    m_value_isSet = !json[QString("Value")].isNull() && m_value_isValid;
}

QString OAIRunnerResults_DurationHistogram_Percentiles_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRunnerResults_DurationHistogram_Percentiles_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_percentile_isSet) {
        obj.insert(QString("Percentile"), ::OpenAPI::toJsonValue(m_percentile));
    }
    if (m_value_isSet) {
        obj.insert(QString("Value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

double OAIRunnerResults_DurationHistogram_Percentiles_inner::getPercentile() const {
    return m_percentile;
}
void OAIRunnerResults_DurationHistogram_Percentiles_inner::setPercentile(const double &percentile) {
    m_percentile = percentile;
    m_percentile_isSet = true;
}

bool OAIRunnerResults_DurationHistogram_Percentiles_inner::is_percentile_Set() const{
    return m_percentile_isSet;
}

bool OAIRunnerResults_DurationHistogram_Percentiles_inner::is_percentile_Valid() const{
    return m_percentile_isValid;
}

double OAIRunnerResults_DurationHistogram_Percentiles_inner::getValue() const {
    return m_value;
}
void OAIRunnerResults_DurationHistogram_Percentiles_inner::setValue(const double &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIRunnerResults_DurationHistogram_Percentiles_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIRunnerResults_DurationHistogram_Percentiles_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIRunnerResults_DurationHistogram_Percentiles_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_percentile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRunnerResults_DurationHistogram_Percentiles_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
