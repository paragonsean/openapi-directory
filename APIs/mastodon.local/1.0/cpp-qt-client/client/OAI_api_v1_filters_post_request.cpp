/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_api_v1_filters_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_api_v1_filters_post_request::OAI_api_v1_filters_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_api_v1_filters_post_request::OAI_api_v1_filters_post_request() {
    this->initializeModel();
}

OAI_api_v1_filters_post_request::~OAI_api_v1_filters_post_request() {}

void OAI_api_v1_filters_post_request::initializeModel() {

    m_context_isSet = false;
    m_context_isValid = false;

    m_expires_in_isSet = false;
    m_expires_in_isValid = false;

    m_irreversible_isSet = false;
    m_irreversible_isValid = false;

    m_phrase_isSet = false;
    m_phrase_isValid = false;

    m_whole_word_isSet = false;
    m_whole_word_isValid = false;
}

void OAI_api_v1_filters_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_api_v1_filters_post_request::fromJsonObject(QJsonObject json) {

    m_context_isValid = ::OpenAPI::fromJsonValue(m_context, json[QString("context")]);
    m_context_isSet = !json[QString("context")].isNull() && m_context_isValid;

    m_expires_in_isValid = ::OpenAPI::fromJsonValue(m_expires_in, json[QString("expires_in")]);
    m_expires_in_isSet = !json[QString("expires_in")].isNull() && m_expires_in_isValid;

    m_irreversible_isValid = ::OpenAPI::fromJsonValue(m_irreversible, json[QString("irreversible")]);
    m_irreversible_isSet = !json[QString("irreversible")].isNull() && m_irreversible_isValid;

    m_phrase_isValid = ::OpenAPI::fromJsonValue(m_phrase, json[QString("phrase")]);
    m_phrase_isSet = !json[QString("phrase")].isNull() && m_phrase_isValid;

    m_whole_word_isValid = ::OpenAPI::fromJsonValue(m_whole_word, json[QString("whole_word")]);
    m_whole_word_isSet = !json[QString("whole_word")].isNull() && m_whole_word_isValid;
}

QString OAI_api_v1_filters_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_api_v1_filters_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_context.size() > 0) {
        obj.insert(QString("context"), ::OpenAPI::toJsonValue(m_context));
    }
    if (m_expires_in_isSet) {
        obj.insert(QString("expires_in"), ::OpenAPI::toJsonValue(m_expires_in));
    }
    if (m_irreversible_isSet) {
        obj.insert(QString("irreversible"), ::OpenAPI::toJsonValue(m_irreversible));
    }
    if (m_phrase_isSet) {
        obj.insert(QString("phrase"), ::OpenAPI::toJsonValue(m_phrase));
    }
    if (m_whole_word_isSet) {
        obj.insert(QString("whole_word"), ::OpenAPI::toJsonValue(m_whole_word));
    }
    return obj;
}

QList<QString> OAI_api_v1_filters_post_request::getContext() const {
    return m_context;
}
void OAI_api_v1_filters_post_request::setContext(const QList<QString> &context) {
    m_context = context;
    m_context_isSet = true;
}

bool OAI_api_v1_filters_post_request::is_context_Set() const{
    return m_context_isSet;
}

bool OAI_api_v1_filters_post_request::is_context_Valid() const{
    return m_context_isValid;
}

qint32 OAI_api_v1_filters_post_request::getExpiresIn() const {
    return m_expires_in;
}
void OAI_api_v1_filters_post_request::setExpiresIn(const qint32 &expires_in) {
    m_expires_in = expires_in;
    m_expires_in_isSet = true;
}

bool OAI_api_v1_filters_post_request::is_expires_in_Set() const{
    return m_expires_in_isSet;
}

bool OAI_api_v1_filters_post_request::is_expires_in_Valid() const{
    return m_expires_in_isValid;
}

bool OAI_api_v1_filters_post_request::isIrreversible() const {
    return m_irreversible;
}
void OAI_api_v1_filters_post_request::setIrreversible(const bool &irreversible) {
    m_irreversible = irreversible;
    m_irreversible_isSet = true;
}

bool OAI_api_v1_filters_post_request::is_irreversible_Set() const{
    return m_irreversible_isSet;
}

bool OAI_api_v1_filters_post_request::is_irreversible_Valid() const{
    return m_irreversible_isValid;
}

QString OAI_api_v1_filters_post_request::getPhrase() const {
    return m_phrase;
}
void OAI_api_v1_filters_post_request::setPhrase(const QString &phrase) {
    m_phrase = phrase;
    m_phrase_isSet = true;
}

bool OAI_api_v1_filters_post_request::is_phrase_Set() const{
    return m_phrase_isSet;
}

bool OAI_api_v1_filters_post_request::is_phrase_Valid() const{
    return m_phrase_isValid;
}

bool OAI_api_v1_filters_post_request::isWholeWord() const {
    return m_whole_word;
}
void OAI_api_v1_filters_post_request::setWholeWord(const bool &whole_word) {
    m_whole_word = whole_word;
    m_whole_word_isSet = true;
}

bool OAI_api_v1_filters_post_request::is_whole_word_Set() const{
    return m_whole_word_isSet;
}

bool OAI_api_v1_filters_post_request::is_whole_word_Valid() const{
    return m_whole_word_isValid;
}

bool OAI_api_v1_filters_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_context.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_expires_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_irreversible_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phrase_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_whole_word_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_api_v1_filters_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_context_isValid && m_phrase_isValid && true;
}

} // namespace OpenAPI
