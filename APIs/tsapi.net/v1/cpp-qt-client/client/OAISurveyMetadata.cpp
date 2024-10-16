/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISurveyMetadata.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISurveyMetadata::OAISurveyMetadata(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISurveyMetadata::OAISurveyMetadata() {
    this->initializeModel();
}

OAISurveyMetadata::~OAISurveyMetadata() {}

void OAISurveyMetadata::initializeModel() {

    m_hierarchies_isSet = false;
    m_hierarchies_isValid = false;

    m_interview_count_isSet = false;
    m_interview_count_isValid = false;

    m_languages_isSet = false;
    m_languages_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_variables_isSet = false;
    m_variables_isValid = false;
}

void OAISurveyMetadata::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISurveyMetadata::fromJsonObject(QJsonObject json) {

    m_hierarchies_isValid = ::OpenAPI::fromJsonValue(m_hierarchies, json[QString("hierarchies")]);
    m_hierarchies_isSet = !json[QString("hierarchies")].isNull() && m_hierarchies_isValid;

    m_interview_count_isValid = ::OpenAPI::fromJsonValue(m_interview_count, json[QString("interviewCount")]);
    m_interview_count_isSet = !json[QString("interviewCount")].isNull() && m_interview_count_isValid;

    m_languages_isValid = ::OpenAPI::fromJsonValue(m_languages, json[QString("languages")]);
    m_languages_isSet = !json[QString("languages")].isNull() && m_languages_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_variables_isValid = ::OpenAPI::fromJsonValue(m_variables, json[QString("variables")]);
    m_variables_isSet = !json[QString("variables")].isNull() && m_variables_isValid;
}

QString OAISurveyMetadata::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISurveyMetadata::asJsonObject() const {
    QJsonObject obj;
    if (m_hierarchies.size() > 0) {
        obj.insert(QString("hierarchies"), ::OpenAPI::toJsonValue(m_hierarchies));
    }
    if (m_interview_count_isSet) {
        obj.insert(QString("interviewCount"), ::OpenAPI::toJsonValue(m_interview_count));
    }
    if (m_languages.size() > 0) {
        obj.insert(QString("languages"), ::OpenAPI::toJsonValue(m_languages));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_variables.size() > 0) {
        obj.insert(QString("variables"), ::OpenAPI::toJsonValue(m_variables));
    }
    return obj;
}

QList<OAIHierarchy> OAISurveyMetadata::getHierarchies() const {
    return m_hierarchies;
}
void OAISurveyMetadata::setHierarchies(const QList<OAIHierarchy> &hierarchies) {
    m_hierarchies = hierarchies;
    m_hierarchies_isSet = true;
}

bool OAISurveyMetadata::is_hierarchies_Set() const{
    return m_hierarchies_isSet;
}

bool OAISurveyMetadata::is_hierarchies_Valid() const{
    return m_hierarchies_isValid;
}

qint32 OAISurveyMetadata::getInterviewCount() const {
    return m_interview_count;
}
void OAISurveyMetadata::setInterviewCount(const qint32 &interview_count) {
    m_interview_count = interview_count;
    m_interview_count_isSet = true;
}

bool OAISurveyMetadata::is_interview_count_Set() const{
    return m_interview_count_isSet;
}

bool OAISurveyMetadata::is_interview_count_Valid() const{
    return m_interview_count_isValid;
}

QList<OAILanguage> OAISurveyMetadata::getLanguages() const {
    return m_languages;
}
void OAISurveyMetadata::setLanguages(const QList<OAILanguage> &languages) {
    m_languages = languages;
    m_languages_isSet = true;
}

bool OAISurveyMetadata::is_languages_Set() const{
    return m_languages_isSet;
}

bool OAISurveyMetadata::is_languages_Valid() const{
    return m_languages_isValid;
}

QString OAISurveyMetadata::getName() const {
    return m_name;
}
void OAISurveyMetadata::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISurveyMetadata::is_name_Set() const{
    return m_name_isSet;
}

bool OAISurveyMetadata::is_name_Valid() const{
    return m_name_isValid;
}

QString OAISurveyMetadata::getTitle() const {
    return m_title;
}
void OAISurveyMetadata::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAISurveyMetadata::is_title_Set() const{
    return m_title_isSet;
}

bool OAISurveyMetadata::is_title_Valid() const{
    return m_title_isValid;
}

QList<OAIVariable> OAISurveyMetadata::getVariables() const {
    return m_variables;
}
void OAISurveyMetadata::setVariables(const QList<OAIVariable> &variables) {
    m_variables = variables;
    m_variables_isSet = true;
}

bool OAISurveyMetadata::is_variables_Set() const{
    return m_variables_isSet;
}

bool OAISurveyMetadata::is_variables_Valid() const{
    return m_variables_isValid;
}

bool OAISurveyMetadata::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_hierarchies.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_interview_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_languages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_variables.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISurveyMetadata::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
