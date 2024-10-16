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

#include "OAIRunnerResults_DurationHistogram.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRunnerResults_DurationHistogram::OAIRunnerResults_DurationHistogram(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRunnerResults_DurationHistogram::OAIRunnerResults_DurationHistogram() {
    this->initializeModel();
}

OAIRunnerResults_DurationHistogram::~OAIRunnerResults_DurationHistogram() {}

void OAIRunnerResults_DurationHistogram::initializeModel() {

    m_avg_isSet = false;
    m_avg_isValid = false;

    m_max_isSet = false;
    m_max_isValid = false;

    m_min_isSet = false;
    m_min_isValid = false;

    m_percentiles_isSet = false;
    m_percentiles_isValid = false;
}

void OAIRunnerResults_DurationHistogram::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRunnerResults_DurationHistogram::fromJsonObject(QJsonObject json) {

    m_avg_isValid = ::OpenAPI::fromJsonValue(m_avg, json[QString("Avg")]);
    m_avg_isSet = !json[QString("Avg")].isNull() && m_avg_isValid;

    m_max_isValid = ::OpenAPI::fromJsonValue(m_max, json[QString("Max")]);
    m_max_isSet = !json[QString("Max")].isNull() && m_max_isValid;

    m_min_isValid = ::OpenAPI::fromJsonValue(m_min, json[QString("Min")]);
    m_min_isSet = !json[QString("Min")].isNull() && m_min_isValid;

    m_percentiles_isValid = ::OpenAPI::fromJsonValue(m_percentiles, json[QString("Percentiles")]);
    m_percentiles_isSet = !json[QString("Percentiles")].isNull() && m_percentiles_isValid;
}

QString OAIRunnerResults_DurationHistogram::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRunnerResults_DurationHistogram::asJsonObject() const {
    QJsonObject obj;
    if (m_avg_isSet) {
        obj.insert(QString("Avg"), ::OpenAPI::toJsonValue(m_avg));
    }
    if (m_max_isSet) {
        obj.insert(QString("Max"), ::OpenAPI::toJsonValue(m_max));
    }
    if (m_min_isSet) {
        obj.insert(QString("Min"), ::OpenAPI::toJsonValue(m_min));
    }
    if (m_percentiles.size() > 0) {
        obj.insert(QString("Percentiles"), ::OpenAPI::toJsonValue(m_percentiles));
    }
    return obj;
}

double OAIRunnerResults_DurationHistogram::getAvg() const {
    return m_avg;
}
void OAIRunnerResults_DurationHistogram::setAvg(const double &avg) {
    m_avg = avg;
    m_avg_isSet = true;
}

bool OAIRunnerResults_DurationHistogram::is_avg_Set() const{
    return m_avg_isSet;
}

bool OAIRunnerResults_DurationHistogram::is_avg_Valid() const{
    return m_avg_isValid;
}

double OAIRunnerResults_DurationHistogram::getMax() const {
    return m_max;
}
void OAIRunnerResults_DurationHistogram::setMax(const double &max) {
    m_max = max;
    m_max_isSet = true;
}

bool OAIRunnerResults_DurationHistogram::is_max_Set() const{
    return m_max_isSet;
}

bool OAIRunnerResults_DurationHistogram::is_max_Valid() const{
    return m_max_isValid;
}

double OAIRunnerResults_DurationHistogram::getMin() const {
    return m_min;
}
void OAIRunnerResults_DurationHistogram::setMin(const double &min) {
    m_min = min;
    m_min_isSet = true;
}

bool OAIRunnerResults_DurationHistogram::is_min_Set() const{
    return m_min_isSet;
}

bool OAIRunnerResults_DurationHistogram::is_min_Valid() const{
    return m_min_isValid;
}

QList<OAIRunnerResults_DurationHistogram_Percentiles_inner> OAIRunnerResults_DurationHistogram::getPercentiles() const {
    return m_percentiles;
}
void OAIRunnerResults_DurationHistogram::setPercentiles(const QList<OAIRunnerResults_DurationHistogram_Percentiles_inner> &percentiles) {
    m_percentiles = percentiles;
    m_percentiles_isSet = true;
}

bool OAIRunnerResults_DurationHistogram::is_percentiles_Set() const{
    return m_percentiles_isSet;
}

bool OAIRunnerResults_DurationHistogram::is_percentiles_Valid() const{
    return m_percentiles_isValid;
}

bool OAIRunnerResults_DurationHistogram::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_avg_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_percentiles.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRunnerResults_DurationHistogram::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
