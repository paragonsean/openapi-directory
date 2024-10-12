/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPredictionQueryResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPredictionQueryResult::OAIPredictionQueryResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPredictionQueryResult::OAIPredictionQueryResult() {
    this->initializeModel();
}

OAIPredictionQueryResult::~OAIPredictionQueryResult() {}

void OAIPredictionQueryResult::initializeModel() {

    m_results_isSet = false;
    m_results_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;
}

void OAIPredictionQueryResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPredictionQueryResult::fromJsonObject(QJsonObject json) {

    m_results_isValid = ::OpenAPI::fromJsonValue(m_results, json[QString("results")]);
    m_results_isSet = !json[QString("results")].isNull() && m_results_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;
}

QString OAIPredictionQueryResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPredictionQueryResult::asJsonObject() const {
    QJsonObject obj;
    if (m_results.size() > 0) {
        obj.insert(QString("results"), ::OpenAPI::toJsonValue(m_results));
    }
    if (m_token.isSet()) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    return obj;
}

QList<OAIStoredImagePrediction> OAIPredictionQueryResult::getResults() const {
    return m_results;
}
void OAIPredictionQueryResult::setResults(const QList<OAIStoredImagePrediction> &results) {
    m_results = results;
    m_results_isSet = true;
}

bool OAIPredictionQueryResult::is_results_Set() const{
    return m_results_isSet;
}

bool OAIPredictionQueryResult::is_results_Valid() const{
    return m_results_isValid;
}

OAIPredictionQueryToken OAIPredictionQueryResult::getToken() const {
    return m_token;
}
void OAIPredictionQueryResult::setToken(const OAIPredictionQueryToken &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIPredictionQueryResult::is_token_Set() const{
    return m_token_isSet;
}

bool OAIPredictionQueryResult::is_token_Valid() const{
    return m_token_isValid;
}

bool OAIPredictionQueryResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_results.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_token.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPredictionQueryResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
