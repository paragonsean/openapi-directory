/**
 * EVEMarketer Marketstat API
 * EVEMarketer Marketstat API is almost compatible with EVE-Central's Marketstat API.
 *
 * The version of the OpenAPI document: 1.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITypeStat.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITypeStat::OAITypeStat(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITypeStat::OAITypeStat() {
    this->initializeModel();
}

OAITypeStat::~OAITypeStat() {}

void OAITypeStat::initializeModel() {

    m_avg_isSet = false;
    m_avg_isValid = false;

    m_five_percent_isSet = false;
    m_five_percent_isValid = false;

    m_for_query_isSet = false;
    m_for_query_isValid = false;

    m_generated_isSet = false;
    m_generated_isValid = false;

    m_high_to_low_isSet = false;
    m_high_to_low_isValid = false;

    m_max_isSet = false;
    m_max_isValid = false;

    m_median_isSet = false;
    m_median_isValid = false;

    m_min_isSet = false;
    m_min_isValid = false;

    m_std_dev_isSet = false;
    m_std_dev_isValid = false;

    m_variance_isSet = false;
    m_variance_isValid = false;

    m_volume_isSet = false;
    m_volume_isValid = false;

    m_wavg_isSet = false;
    m_wavg_isValid = false;
}

void OAITypeStat::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITypeStat::fromJsonObject(QJsonObject json) {

    m_avg_isValid = ::OpenAPI::fromJsonValue(m_avg, json[QString("avg")]);
    m_avg_isSet = !json[QString("avg")].isNull() && m_avg_isValid;

    m_five_percent_isValid = ::OpenAPI::fromJsonValue(m_five_percent, json[QString("fivePercent")]);
    m_five_percent_isSet = !json[QString("fivePercent")].isNull() && m_five_percent_isValid;

    m_for_query_isValid = ::OpenAPI::fromJsonValue(m_for_query, json[QString("forQuery")]);
    m_for_query_isSet = !json[QString("forQuery")].isNull() && m_for_query_isValid;

    m_generated_isValid = ::OpenAPI::fromJsonValue(m_generated, json[QString("generated")]);
    m_generated_isSet = !json[QString("generated")].isNull() && m_generated_isValid;

    m_high_to_low_isValid = ::OpenAPI::fromJsonValue(m_high_to_low, json[QString("highToLow")]);
    m_high_to_low_isSet = !json[QString("highToLow")].isNull() && m_high_to_low_isValid;

    m_max_isValid = ::OpenAPI::fromJsonValue(m_max, json[QString("max")]);
    m_max_isSet = !json[QString("max")].isNull() && m_max_isValid;

    m_median_isValid = ::OpenAPI::fromJsonValue(m_median, json[QString("median")]);
    m_median_isSet = !json[QString("median")].isNull() && m_median_isValid;

    m_min_isValid = ::OpenAPI::fromJsonValue(m_min, json[QString("min")]);
    m_min_isSet = !json[QString("min")].isNull() && m_min_isValid;

    m_std_dev_isValid = ::OpenAPI::fromJsonValue(m_std_dev, json[QString("stdDev")]);
    m_std_dev_isSet = !json[QString("stdDev")].isNull() && m_std_dev_isValid;

    m_variance_isValid = ::OpenAPI::fromJsonValue(m_variance, json[QString("variance")]);
    m_variance_isSet = !json[QString("variance")].isNull() && m_variance_isValid;

    m_volume_isValid = ::OpenAPI::fromJsonValue(m_volume, json[QString("volume")]);
    m_volume_isSet = !json[QString("volume")].isNull() && m_volume_isValid;

    m_wavg_isValid = ::OpenAPI::fromJsonValue(m_wavg, json[QString("wavg")]);
    m_wavg_isSet = !json[QString("wavg")].isNull() && m_wavg_isValid;
}

QString OAITypeStat::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITypeStat::asJsonObject() const {
    QJsonObject obj;
    if (m_avg_isSet) {
        obj.insert(QString("avg"), ::OpenAPI::toJsonValue(m_avg));
    }
    if (m_five_percent_isSet) {
        obj.insert(QString("fivePercent"), ::OpenAPI::toJsonValue(m_five_percent));
    }
    if (m_for_query.isSet()) {
        obj.insert(QString("forQuery"), ::OpenAPI::toJsonValue(m_for_query));
    }
    if (m_generated_isSet) {
        obj.insert(QString("generated"), ::OpenAPI::toJsonValue(m_generated));
    }
    if (m_high_to_low_isSet) {
        obj.insert(QString("highToLow"), ::OpenAPI::toJsonValue(m_high_to_low));
    }
    if (m_max_isSet) {
        obj.insert(QString("max"), ::OpenAPI::toJsonValue(m_max));
    }
    if (m_median_isSet) {
        obj.insert(QString("median"), ::OpenAPI::toJsonValue(m_median));
    }
    if (m_min_isSet) {
        obj.insert(QString("min"), ::OpenAPI::toJsonValue(m_min));
    }
    if (m_std_dev_isSet) {
        obj.insert(QString("stdDev"), ::OpenAPI::toJsonValue(m_std_dev));
    }
    if (m_variance_isSet) {
        obj.insert(QString("variance"), ::OpenAPI::toJsonValue(m_variance));
    }
    if (m_volume_isSet) {
        obj.insert(QString("volume"), ::OpenAPI::toJsonValue(m_volume));
    }
    if (m_wavg_isSet) {
        obj.insert(QString("wavg"), ::OpenAPI::toJsonValue(m_wavg));
    }
    return obj;
}

double OAITypeStat::getAvg() const {
    return m_avg;
}
void OAITypeStat::setAvg(const double &avg) {
    m_avg = avg;
    m_avg_isSet = true;
}

bool OAITypeStat::is_avg_Set() const{
    return m_avg_isSet;
}

bool OAITypeStat::is_avg_Valid() const{
    return m_avg_isValid;
}

double OAITypeStat::getFivePercent() const {
    return m_five_percent;
}
void OAITypeStat::setFivePercent(const double &five_percent) {
    m_five_percent = five_percent;
    m_five_percent_isSet = true;
}

bool OAITypeStat::is_five_percent_Set() const{
    return m_five_percent_isSet;
}

bool OAITypeStat::is_five_percent_Valid() const{
    return m_five_percent_isValid;
}

OAIForQuery OAITypeStat::getForQuery() const {
    return m_for_query;
}
void OAITypeStat::setForQuery(const OAIForQuery &for_query) {
    m_for_query = for_query;
    m_for_query_isSet = true;
}

bool OAITypeStat::is_for_query_Set() const{
    return m_for_query_isSet;
}

bool OAITypeStat::is_for_query_Valid() const{
    return m_for_query_isValid;
}

qint64 OAITypeStat::getGenerated() const {
    return m_generated;
}
void OAITypeStat::setGenerated(const qint64 &generated) {
    m_generated = generated;
    m_generated_isSet = true;
}

bool OAITypeStat::is_generated_Set() const{
    return m_generated_isSet;
}

bool OAITypeStat::is_generated_Valid() const{
    return m_generated_isValid;
}

bool OAITypeStat::isHighToLow() const {
    return m_high_to_low;
}
void OAITypeStat::setHighToLow(const bool &high_to_low) {
    m_high_to_low = high_to_low;
    m_high_to_low_isSet = true;
}

bool OAITypeStat::is_high_to_low_Set() const{
    return m_high_to_low_isSet;
}

bool OAITypeStat::is_high_to_low_Valid() const{
    return m_high_to_low_isValid;
}

double OAITypeStat::getMax() const {
    return m_max;
}
void OAITypeStat::setMax(const double &max) {
    m_max = max;
    m_max_isSet = true;
}

bool OAITypeStat::is_max_Set() const{
    return m_max_isSet;
}

bool OAITypeStat::is_max_Valid() const{
    return m_max_isValid;
}

double OAITypeStat::getMedian() const {
    return m_median;
}
void OAITypeStat::setMedian(const double &median) {
    m_median = median;
    m_median_isSet = true;
}

bool OAITypeStat::is_median_Set() const{
    return m_median_isSet;
}

bool OAITypeStat::is_median_Valid() const{
    return m_median_isValid;
}

double OAITypeStat::getMin() const {
    return m_min;
}
void OAITypeStat::setMin(const double &min) {
    m_min = min;
    m_min_isSet = true;
}

bool OAITypeStat::is_min_Set() const{
    return m_min_isSet;
}

bool OAITypeStat::is_min_Valid() const{
    return m_min_isValid;
}

double OAITypeStat::getStdDev() const {
    return m_std_dev;
}
void OAITypeStat::setStdDev(const double &std_dev) {
    m_std_dev = std_dev;
    m_std_dev_isSet = true;
}

bool OAITypeStat::is_std_dev_Set() const{
    return m_std_dev_isSet;
}

bool OAITypeStat::is_std_dev_Valid() const{
    return m_std_dev_isValid;
}

double OAITypeStat::getVariance() const {
    return m_variance;
}
void OAITypeStat::setVariance(const double &variance) {
    m_variance = variance;
    m_variance_isSet = true;
}

bool OAITypeStat::is_variance_Set() const{
    return m_variance_isSet;
}

bool OAITypeStat::is_variance_Valid() const{
    return m_variance_isValid;
}

qint64 OAITypeStat::getVolume() const {
    return m_volume;
}
void OAITypeStat::setVolume(const qint64 &volume) {
    m_volume = volume;
    m_volume_isSet = true;
}

bool OAITypeStat::is_volume_Set() const{
    return m_volume_isSet;
}

bool OAITypeStat::is_volume_Valid() const{
    return m_volume_isValid;
}

double OAITypeStat::getWavg() const {
    return m_wavg;
}
void OAITypeStat::setWavg(const double &wavg) {
    m_wavg = wavg;
    m_wavg_isSet = true;
}

bool OAITypeStat::is_wavg_Set() const{
    return m_wavg_isSet;
}

bool OAITypeStat::is_wavg_Valid() const{
    return m_wavg_isValid;
}

bool OAITypeStat::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_avg_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_five_percent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_for_query.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_generated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_high_to_low_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_median_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_std_dev_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_variance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_volume_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wavg_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITypeStat::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
