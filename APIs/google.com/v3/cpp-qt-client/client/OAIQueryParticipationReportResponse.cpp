/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQueryParticipationReportResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQueryParticipationReportResponse::OAIQueryParticipationReportResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQueryParticipationReportResponse::OAIQueryParticipationReportResponse() {
    this->initializeModel();
}

OAIQueryParticipationReportResponse::~OAIQueryParticipationReportResponse() {}

void OAIQueryParticipationReportResponse::initializeModel() {

    m_next_page_token_isSet = false;
    m_next_page_token_isValid = false;

    m_results_isSet = false;
    m_results_isValid = false;
}

void OAIQueryParticipationReportResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQueryParticipationReportResponse::fromJsonObject(QJsonObject json) {

    m_next_page_token_isValid = ::OpenAPI::fromJsonValue(m_next_page_token, json[QString("nextPageToken")]);
    m_next_page_token_isSet = !json[QString("nextPageToken")].isNull() && m_next_page_token_isValid;

    m_results_isValid = ::OpenAPI::fromJsonValue(m_results, json[QString("results")]);
    m_results_isSet = !json[QString("results")].isNull() && m_results_isValid;
}

QString OAIQueryParticipationReportResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQueryParticipationReportResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_next_page_token_isSet) {
        obj.insert(QString("nextPageToken"), ::OpenAPI::toJsonValue(m_next_page_token));
    }
    if (m_results.size() > 0) {
        obj.insert(QString("results"), ::OpenAPI::toJsonValue(m_results));
    }
    return obj;
}

QString OAIQueryParticipationReportResponse::getNextPageToken() const {
    return m_next_page_token;
}
void OAIQueryParticipationReportResponse::setNextPageToken(const QString &next_page_token) {
    m_next_page_token = next_page_token;
    m_next_page_token_isSet = true;
}

bool OAIQueryParticipationReportResponse::is_next_page_token_Set() const{
    return m_next_page_token_isSet;
}

bool OAIQueryParticipationReportResponse::is_next_page_token_Valid() const{
    return m_next_page_token_isValid;
}

QList<OAIParticipationResult> OAIQueryParticipationReportResponse::getResults() const {
    return m_results;
}
void OAIQueryParticipationReportResponse::setResults(const QList<OAIParticipationResult> &results) {
    m_results = results;
    m_results_isSet = true;
}

bool OAIQueryParticipationReportResponse::is_results_Set() const{
    return m_results_isSet;
}

bool OAIQueryParticipationReportResponse::is_results_Valid() const{
    return m_results_isValid;
}

bool OAIQueryParticipationReportResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_next_page_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_results.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQueryParticipationReportResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
