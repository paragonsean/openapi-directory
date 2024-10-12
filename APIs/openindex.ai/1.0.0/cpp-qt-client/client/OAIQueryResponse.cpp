/**
 * OpenIndex Retrieval Plugin API
 * A retrieval API for querying and filtering documents based on natural language queries and metadata
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQueryResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQueryResponse::OAIQueryResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQueryResponse::OAIQueryResponse() {
    this->initializeModel();
}

OAIQueryResponse::~OAIQueryResponse() {}

void OAIQueryResponse::initializeModel() {

    m_results_isSet = false;
    m_results_isValid = false;
}

void OAIQueryResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQueryResponse::fromJsonObject(QJsonObject json) {

    m_results_isValid = ::OpenAPI::fromJsonValue(m_results, json[QString("results")]);
    m_results_isSet = !json[QString("results")].isNull() && m_results_isValid;
}

QString OAIQueryResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQueryResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_results.size() > 0) {
        obj.insert(QString("results"), ::OpenAPI::toJsonValue(m_results));
    }
    return obj;
}

QList<OAIQueryResult> OAIQueryResponse::getResults() const {
    return m_results;
}
void OAIQueryResponse::setResults(const QList<OAIQueryResult> &results) {
    m_results = results;
    m_results_isSet = true;
}

bool OAIQueryResponse::is_results_Set() const{
    return m_results_isSet;
}

bool OAIQueryResponse::is_results_Valid() const{
    return m_results_isValid;
}

bool OAIQueryResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_results.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQueryResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_results_isValid && true;
}

} // namespace OpenAPI
