/**
 * SheerSEO API
 * Sheerseo API has 2 stages:<br>First stage - initiating the task: You fill in your task and receive in return the task id. <br>Second stage - collecting the results: send a request containing the task ids you got at the first stage and collecting the results.
 *
 * The version of the OpenAPI document: 0.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIKeywordJobRank.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIKeywordJobRank::OAIKeywordJobRank(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIKeywordJobRank::OAIKeywordJobRank() {
    this->initializeModel();
}

OAIKeywordJobRank::~OAIKeywordJobRank() {}

void OAIKeywordJobRank::initializeModel() {

    m_domain_isSet = false;
    m_domain_isValid = false;

    m_keyword_isSet = false;
    m_keyword_isValid = false;

    m_localization_code_isSet = false;
    m_localization_code_isValid = false;

    m_localization_zip_isSet = false;
    m_localization_zip_isValid = false;

    m_search_engine_isSet = false;
    m_search_engine_isValid = false;
}

void OAIKeywordJobRank::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIKeywordJobRank::fromJsonObject(QJsonObject json) {

    m_domain_isValid = ::OpenAPI::fromJsonValue(m_domain, json[QString("domain")]);
    m_domain_isSet = !json[QString("domain")].isNull() && m_domain_isValid;

    m_keyword_isValid = ::OpenAPI::fromJsonValue(m_keyword, json[QString("keyword")]);
    m_keyword_isSet = !json[QString("keyword")].isNull() && m_keyword_isValid;

    m_localization_code_isValid = ::OpenAPI::fromJsonValue(m_localization_code, json[QString("localization_code")]);
    m_localization_code_isSet = !json[QString("localization_code")].isNull() && m_localization_code_isValid;

    m_localization_zip_isValid = ::OpenAPI::fromJsonValue(m_localization_zip, json[QString("localization_zip")]);
    m_localization_zip_isSet = !json[QString("localization_zip")].isNull() && m_localization_zip_isValid;

    m_search_engine_isValid = ::OpenAPI::fromJsonValue(m_search_engine, json[QString("search_engine")]);
    m_search_engine_isSet = !json[QString("search_engine")].isNull() && m_search_engine_isValid;
}

QString OAIKeywordJobRank::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIKeywordJobRank::asJsonObject() const {
    QJsonObject obj;
    if (m_domain_isSet) {
        obj.insert(QString("domain"), ::OpenAPI::toJsonValue(m_domain));
    }
    if (m_keyword_isSet) {
        obj.insert(QString("keyword"), ::OpenAPI::toJsonValue(m_keyword));
    }
    if (m_localization_code_isSet) {
        obj.insert(QString("localization_code"), ::OpenAPI::toJsonValue(m_localization_code));
    }
    if (m_localization_zip_isSet) {
        obj.insert(QString("localization_zip"), ::OpenAPI::toJsonValue(m_localization_zip));
    }
    if (m_search_engine_isSet) {
        obj.insert(QString("search_engine"), ::OpenAPI::toJsonValue(m_search_engine));
    }
    return obj;
}

QString OAIKeywordJobRank::getDomain() const {
    return m_domain;
}
void OAIKeywordJobRank::setDomain(const QString &domain) {
    m_domain = domain;
    m_domain_isSet = true;
}

bool OAIKeywordJobRank::is_domain_Set() const{
    return m_domain_isSet;
}

bool OAIKeywordJobRank::is_domain_Valid() const{
    return m_domain_isValid;
}

QString OAIKeywordJobRank::getKeyword() const {
    return m_keyword;
}
void OAIKeywordJobRank::setKeyword(const QString &keyword) {
    m_keyword = keyword;
    m_keyword_isSet = true;
}

bool OAIKeywordJobRank::is_keyword_Set() const{
    return m_keyword_isSet;
}

bool OAIKeywordJobRank::is_keyword_Valid() const{
    return m_keyword_isValid;
}

QString OAIKeywordJobRank::getLocalizationCode() const {
    return m_localization_code;
}
void OAIKeywordJobRank::setLocalizationCode(const QString &localization_code) {
    m_localization_code = localization_code;
    m_localization_code_isSet = true;
}

bool OAIKeywordJobRank::is_localization_code_Set() const{
    return m_localization_code_isSet;
}

bool OAIKeywordJobRank::is_localization_code_Valid() const{
    return m_localization_code_isValid;
}

QString OAIKeywordJobRank::getLocalizationZip() const {
    return m_localization_zip;
}
void OAIKeywordJobRank::setLocalizationZip(const QString &localization_zip) {
    m_localization_zip = localization_zip;
    m_localization_zip_isSet = true;
}

bool OAIKeywordJobRank::is_localization_zip_Set() const{
    return m_localization_zip_isSet;
}

bool OAIKeywordJobRank::is_localization_zip_Valid() const{
    return m_localization_zip_isValid;
}

QString OAIKeywordJobRank::getSearchEngine() const {
    return m_search_engine;
}
void OAIKeywordJobRank::setSearchEngine(const QString &search_engine) {
    m_search_engine = search_engine;
    m_search_engine_isSet = true;
}

bool OAIKeywordJobRank::is_search_engine_Set() const{
    return m_search_engine_isSet;
}

bool OAIKeywordJobRank::is_search_engine_Valid() const{
    return m_search_engine_isValid;
}

bool OAIKeywordJobRank::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_domain_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_keyword_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_localization_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_localization_zip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_search_engine_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIKeywordJobRank::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_keyword_isValid && m_localization_code_isValid && true;
}

} // namespace OpenAPI
