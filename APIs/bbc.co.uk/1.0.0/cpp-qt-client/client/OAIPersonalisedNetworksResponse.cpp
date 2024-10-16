/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPersonalisedNetworksResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPersonalisedNetworksResponse::OAIPersonalisedNetworksResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPersonalisedNetworksResponse::OAIPersonalisedNetworksResponse() {
    this->initializeModel();
}

OAIPersonalisedNetworksResponse::~OAIPersonalisedNetworksResponse() {}

void OAIPersonalisedNetworksResponse::initializeModel() {

    m_schema_isSet = false;
    m_schema_isValid = false;

    m_limit_isSet = false;
    m_limit_isValid = false;

    m_offset_isSet = false;
    m_offset_isValid = false;

    m_results_isSet = false;
    m_results_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;
}

void OAIPersonalisedNetworksResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPersonalisedNetworksResponse::fromJsonObject(QJsonObject json) {

    m_schema_isValid = ::OpenAPI::fromJsonValue(m_schema, json[QString("$schema")]);
    m_schema_isSet = !json[QString("$schema")].isNull() && m_schema_isValid;

    m_limit_isValid = ::OpenAPI::fromJsonValue(m_limit, json[QString("limit")]);
    m_limit_isSet = !json[QString("limit")].isNull() && m_limit_isValid;

    m_offset_isValid = ::OpenAPI::fromJsonValue(m_offset, json[QString("offset")]);
    m_offset_isSet = !json[QString("offset")].isNull() && m_offset_isValid;

    m_results_isValid = ::OpenAPI::fromJsonValue(m_results, json[QString("results")]);
    m_results_isSet = !json[QString("results")].isNull() && m_results_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;
}

QString OAIPersonalisedNetworksResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPersonalisedNetworksResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_schema_isSet) {
        obj.insert(QString("$schema"), ::OpenAPI::toJsonValue(m_schema));
    }
    if (m_limit_isSet) {
        obj.insert(QString("limit"), ::OpenAPI::toJsonValue(m_limit));
    }
    if (m_offset_isSet) {
        obj.insert(QString("offset"), ::OpenAPI::toJsonValue(m_offset));
    }
    if (m_results.size() > 0) {
        obj.insert(QString("results"), ::OpenAPI::toJsonValue(m_results));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    return obj;
}

QString OAIPersonalisedNetworksResponse::getSchema() const {
    return m_schema;
}
void OAIPersonalisedNetworksResponse::setSchema(const QString &schema) {
    m_schema = schema;
    m_schema_isSet = true;
}

bool OAIPersonalisedNetworksResponse::is_schema_Set() const{
    return m_schema_isSet;
}

bool OAIPersonalisedNetworksResponse::is_schema_Valid() const{
    return m_schema_isValid;
}

qint32 OAIPersonalisedNetworksResponse::getLimit() const {
    return m_limit;
}
void OAIPersonalisedNetworksResponse::setLimit(const qint32 &limit) {
    m_limit = limit;
    m_limit_isSet = true;
}

bool OAIPersonalisedNetworksResponse::is_limit_Set() const{
    return m_limit_isSet;
}

bool OAIPersonalisedNetworksResponse::is_limit_Valid() const{
    return m_limit_isValid;
}

qint32 OAIPersonalisedNetworksResponse::getOffset() const {
    return m_offset;
}
void OAIPersonalisedNetworksResponse::setOffset(const qint32 &offset) {
    m_offset = offset;
    m_offset_isSet = true;
}

bool OAIPersonalisedNetworksResponse::is_offset_Set() const{
    return m_offset_isSet;
}

bool OAIPersonalisedNetworksResponse::is_offset_Valid() const{
    return m_offset_isValid;
}

QList<OAIPersonalisedNetworks> OAIPersonalisedNetworksResponse::getResults() const {
    return m_results;
}
void OAIPersonalisedNetworksResponse::setResults(const QList<OAIPersonalisedNetworks> &results) {
    m_results = results;
    m_results_isSet = true;
}

bool OAIPersonalisedNetworksResponse::is_results_Set() const{
    return m_results_isSet;
}

bool OAIPersonalisedNetworksResponse::is_results_Valid() const{
    return m_results_isValid;
}

qint32 OAIPersonalisedNetworksResponse::getTotal() const {
    return m_total;
}
void OAIPersonalisedNetworksResponse::setTotal(const qint32 &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIPersonalisedNetworksResponse::is_total_Set() const{
    return m_total_isSet;
}

bool OAIPersonalisedNetworksResponse::is_total_Valid() const{
    return m_total_isValid;
}

bool OAIPersonalisedNetworksResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_schema_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offset_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_results.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPersonalisedNetworksResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_schema_isValid && m_limit_isValid && m_offset_isValid && m_results_isValid && m_total_isValid && true;
}

} // namespace OpenAPI
