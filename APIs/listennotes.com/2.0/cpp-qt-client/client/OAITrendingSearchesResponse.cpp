/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITrendingSearchesResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITrendingSearchesResponse::OAITrendingSearchesResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITrendingSearchesResponse::OAITrendingSearchesResponse() {
    this->initializeModel();
}

OAITrendingSearchesResponse::~OAITrendingSearchesResponse() {}

void OAITrendingSearchesResponse::initializeModel() {

    m_terms_isSet = false;
    m_terms_isValid = false;
}

void OAITrendingSearchesResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITrendingSearchesResponse::fromJsonObject(QJsonObject json) {

    m_terms_isValid = ::OpenAPI::fromJsonValue(m_terms, json[QString("terms")]);
    m_terms_isSet = !json[QString("terms")].isNull() && m_terms_isValid;
}

QString OAITrendingSearchesResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITrendingSearchesResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_terms.size() > 0) {
        obj.insert(QString("terms"), ::OpenAPI::toJsonValue(m_terms));
    }
    return obj;
}

QList<QString> OAITrendingSearchesResponse::getTerms() const {
    return m_terms;
}
void OAITrendingSearchesResponse::setTerms(const QList<QString> &terms) {
    m_terms = terms;
    m_terms_isSet = true;
}

bool OAITrendingSearchesResponse::is_terms_Set() const{
    return m_terms_isSet;
}

bool OAITrendingSearchesResponse::is_terms_Valid() const{
    return m_terms_isValid;
}

bool OAITrendingSearchesResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_terms.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITrendingSearchesResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_terms_isValid && true;
}

} // namespace OpenAPI
