/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner() {
    this->initializeModel();
}

OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::~OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner() {}

void OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::initializeModel() {

    m_bucket_isSet = false;
    m_bucket_isValid = false;

    m_count_isSet = false;
    m_count_isValid = false;
}

void OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::fromJsonObject(QJsonObject json) {

    m_bucket_isValid = ::OpenAPI::fromJsonValue(m_bucket, json[QString("bucket")]);
    m_bucket_isSet = !json[QString("bucket")].isNull() && m_bucket_isValid;

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;
}

QString OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_bucket_isSet) {
        obj.insert(QString("bucket"), ::OpenAPI::toJsonValue(m_bucket));
    }
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    return obj;
}

QString OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::getBucket() const {
    return m_bucket;
}
void OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::setBucket(const QString &bucket) {
    m_bucket = bucket;
    m_bucket_isSet = true;
}

bool OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::is_bucket_Set() const{
    return m_bucket_isSet;
}

bool OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::is_bucket_Valid() const{
    return m_bucket_isValid;
}

qint64 OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::getCount() const {
    return m_count;
}
void OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::setCount(const qint64 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::is_count_Set() const{
    return m_count_isSet;
}

bool OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::is_count_Valid() const{
    return m_count_isValid;
}

bool OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bucket_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAnalytics_SessionDurationsDistribution_200_response_distribution_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
