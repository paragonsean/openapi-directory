/**
 * Pinecone API
 * Pinecone is a vector database. This is an unofficial, community-managed OpenAPI spec that (should) accurately model the Pinecone API. This project was developed independent of and is unaffiliated with Pinecone Systems. Users should switch to the official API spec, if and when Pinecone releases it.
 *
 * The version of the OpenAPI document: 20230406.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDescribeIndexStatsRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDescribeIndexStatsRequest::OAIDescribeIndexStatsRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDescribeIndexStatsRequest::OAIDescribeIndexStatsRequest() {
    this->initializeModel();
}

OAIDescribeIndexStatsRequest::~OAIDescribeIndexStatsRequest() {}

void OAIDescribeIndexStatsRequest::initializeModel() {

    m_filter_isSet = false;
    m_filter_isValid = false;
}

void OAIDescribeIndexStatsRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDescribeIndexStatsRequest::fromJsonObject(QJsonObject json) {

    m_filter_isValid = ::OpenAPI::fromJsonValue(m_filter, json[QString("filter")]);
    m_filter_isSet = !json[QString("filter")].isNull() && m_filter_isValid;
}

QString OAIDescribeIndexStatsRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDescribeIndexStatsRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_filter.size() > 0) {
        obj.insert(QString("filter"), ::OpenAPI::toJsonValue(m_filter));
    }
    return obj;
}

QMap<QString, QJsonValue> OAIDescribeIndexStatsRequest::getFilter() const {
    return m_filter;
}
void OAIDescribeIndexStatsRequest::setFilter(const QMap<QString, QJsonValue> &filter) {
    m_filter = filter;
    m_filter_isSet = true;
}

bool OAIDescribeIndexStatsRequest::is_filter_Set() const{
    return m_filter_isSet;
}

bool OAIDescribeIndexStatsRequest::is_filter_Valid() const{
    return m_filter_isValid;
}

bool OAIDescribeIndexStatsRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_filter.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDescribeIndexStatsRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
