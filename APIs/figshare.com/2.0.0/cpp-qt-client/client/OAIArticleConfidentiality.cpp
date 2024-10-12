/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArticleConfidentiality.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArticleConfidentiality::OAIArticleConfidentiality(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArticleConfidentiality::OAIArticleConfidentiality() {
    this->initializeModel();
}

OAIArticleConfidentiality::~OAIArticleConfidentiality() {}

void OAIArticleConfidentiality::initializeModel() {

    m_is_confidential_isSet = false;
    m_is_confidential_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;
}

void OAIArticleConfidentiality::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArticleConfidentiality::fromJsonObject(QJsonObject json) {

    m_is_confidential_isValid = ::OpenAPI::fromJsonValue(m_is_confidential, json[QString("is_confidential")]);
    m_is_confidential_isSet = !json[QString("is_confidential")].isNull() && m_is_confidential_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;
}

QString OAIArticleConfidentiality::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArticleConfidentiality::asJsonObject() const {
    QJsonObject obj;
    if (m_is_confidential_isSet) {
        obj.insert(QString("is_confidential"), ::OpenAPI::toJsonValue(m_is_confidential));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    return obj;
}

bool OAIArticleConfidentiality::isIsConfidential() const {
    return m_is_confidential;
}
void OAIArticleConfidentiality::setIsConfidential(const bool &is_confidential) {
    m_is_confidential = is_confidential;
    m_is_confidential_isSet = true;
}

bool OAIArticleConfidentiality::is_is_confidential_Set() const{
    return m_is_confidential_isSet;
}

bool OAIArticleConfidentiality::is_is_confidential_Valid() const{
    return m_is_confidential_isValid;
}

QString OAIArticleConfidentiality::getReason() const {
    return m_reason;
}
void OAIArticleConfidentiality::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIArticleConfidentiality::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIArticleConfidentiality::is_reason_Valid() const{
    return m_reason_isValid;
}

bool OAIArticleConfidentiality::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_confidential_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArticleConfidentiality::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_is_confidential_isValid && m_reason_isValid && true;
}

} // namespace OpenAPI
