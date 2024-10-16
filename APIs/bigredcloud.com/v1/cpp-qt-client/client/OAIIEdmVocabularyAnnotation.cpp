/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIEdmVocabularyAnnotation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIEdmVocabularyAnnotation::OAIIEdmVocabularyAnnotation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIEdmVocabularyAnnotation::OAIIEdmVocabularyAnnotation() {
    this->initializeModel();
}

OAIIEdmVocabularyAnnotation::~OAIIEdmVocabularyAnnotation() {}

void OAIIEdmVocabularyAnnotation::initializeModel() {

    m_qualifier_isSet = false;
    m_qualifier_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;

    m_term_isSet = false;
    m_term_isValid = false;
}

void OAIIEdmVocabularyAnnotation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIEdmVocabularyAnnotation::fromJsonObject(QJsonObject json) {

    m_qualifier_isValid = ::OpenAPI::fromJsonValue(m_qualifier, json[QString("Qualifier")]);
    m_qualifier_isSet = !json[QString("Qualifier")].isNull() && m_qualifier_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("Target")]);
    m_target_isSet = !json[QString("Target")].isNull() && m_target_isValid;

    m_term_isValid = ::OpenAPI::fromJsonValue(m_term, json[QString("Term")]);
    m_term_isSet = !json[QString("Term")].isNull() && m_term_isValid;
}

QString OAIIEdmVocabularyAnnotation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIEdmVocabularyAnnotation::asJsonObject() const {
    QJsonObject obj;
    if (m_qualifier_isSet) {
        obj.insert(QString("Qualifier"), ::OpenAPI::toJsonValue(m_qualifier));
    }
    if (m_target_isSet) {
        obj.insert(QString("Target"), ::OpenAPI::toJsonValue(m_target));
    }
    if (m_term.isSet()) {
        obj.insert(QString("Term"), ::OpenAPI::toJsonValue(m_term));
    }
    return obj;
}

QString OAIIEdmVocabularyAnnotation::getQualifier() const {
    return m_qualifier;
}
void OAIIEdmVocabularyAnnotation::setQualifier(const QString &qualifier) {
    m_qualifier = qualifier;
    m_qualifier_isSet = true;
}

bool OAIIEdmVocabularyAnnotation::is_qualifier_Set() const{
    return m_qualifier_isSet;
}

bool OAIIEdmVocabularyAnnotation::is_qualifier_Valid() const{
    return m_qualifier_isValid;
}

OAIObject OAIIEdmVocabularyAnnotation::getTarget() const {
    return m_target;
}
void OAIIEdmVocabularyAnnotation::setTarget(const OAIObject &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIIEdmVocabularyAnnotation::is_target_Set() const{
    return m_target_isSet;
}

bool OAIIEdmVocabularyAnnotation::is_target_Valid() const{
    return m_target_isValid;
}

OAIIEdmTerm OAIIEdmVocabularyAnnotation::getTerm() const {
    return m_term;
}
void OAIIEdmVocabularyAnnotation::setTerm(const OAIIEdmTerm &term) {
    m_term = term;
    m_term_isSet = true;
}

bool OAIIEdmVocabularyAnnotation::is_term_Set() const{
    return m_term_isSet;
}

bool OAIIEdmVocabularyAnnotation::is_term_Valid() const{
    return m_term_isValid;
}

bool OAIIEdmVocabularyAnnotation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_qualifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_term.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIEdmVocabularyAnnotation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
