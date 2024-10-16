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

#include "OAIVariable.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVariable::OAIVariable(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVariable::OAIVariable() {
    this->initializeModel();
}

OAIVariable::~OAIVariable() {}

void OAIVariable::initializeModel() {

    m_ident_isSet = false;
    m_ident_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_max_responses_isSet = false;
    m_max_responses_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_parent_type_isSet = false;
    m_parent_type_isValid = false;

    m_questions_isSet = false;
    m_questions_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_use_isSet = false;
    m_use_isValid = false;

    m_variable_values_isSet = false;
    m_variable_values_isValid = false;
}

void OAIVariable::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVariable::fromJsonObject(QJsonObject json) {

    m_ident_isValid = ::OpenAPI::fromJsonValue(m_ident, json[QString("ident")]);
    m_ident_isSet = !json[QString("ident")].isNull() && m_ident_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_max_responses_isValid = ::OpenAPI::fromJsonValue(m_max_responses, json[QString("maxResponses")]);
    m_max_responses_isSet = !json[QString("maxResponses")].isNull() && m_max_responses_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_parent_type_isValid = ::OpenAPI::fromJsonValue(m_parent_type, json[QString("parentType")]);
    m_parent_type_isSet = !json[QString("parentType")].isNull() && m_parent_type_isValid;

    m_questions_isValid = ::OpenAPI::fromJsonValue(m_questions, json[QString("questions")]);
    m_questions_isSet = !json[QString("questions")].isNull() && m_questions_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_use_isValid = ::OpenAPI::fromJsonValue(m_use, json[QString("use")]);
    m_use_isSet = !json[QString("use")].isNull() && m_use_isValid;

    m_variable_values_isValid = ::OpenAPI::fromJsonValue(m_variable_values, json[QString("variableValues")]);
    m_variable_values_isSet = !json[QString("variableValues")].isNull() && m_variable_values_isValid;
}

QString OAIVariable::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVariable::asJsonObject() const {
    QJsonObject obj;
    if (m_ident_isSet) {
        obj.insert(QString("ident"), ::OpenAPI::toJsonValue(m_ident));
    }
    if (m_label.isSet()) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_max_responses_isSet) {
        obj.insert(QString("maxResponses"), ::OpenAPI::toJsonValue(m_max_responses));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_parent_type.isSet()) {
        obj.insert(QString("parentType"), ::OpenAPI::toJsonValue(m_parent_type));
    }
    if (m_questions.size() > 0) {
        obj.insert(QString("questions"), ::OpenAPI::toJsonValue(m_questions));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_use.isSet()) {
        obj.insert(QString("use"), ::OpenAPI::toJsonValue(m_use));
    }
    if (m_variable_values.isSet()) {
        obj.insert(QString("variableValues"), ::OpenAPI::toJsonValue(m_variable_values));
    }
    return obj;
}

QString OAIVariable::getIdent() const {
    return m_ident;
}
void OAIVariable::setIdent(const QString &ident) {
    m_ident = ident;
    m_ident_isSet = true;
}

bool OAIVariable::is_ident_Set() const{
    return m_ident_isSet;
}

bool OAIVariable::is_ident_Valid() const{
    return m_ident_isValid;
}

OAILabel OAIVariable::getLabel() const {
    return m_label;
}
void OAIVariable::setLabel(const OAILabel &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIVariable::is_label_Set() const{
    return m_label_isSet;
}

bool OAIVariable::is_label_Valid() const{
    return m_label_isValid;
}

qint32 OAIVariable::getMaxResponses() const {
    return m_max_responses;
}
void OAIVariable::setMaxResponses(const qint32 &max_responses) {
    m_max_responses = max_responses;
    m_max_responses_isSet = true;
}

bool OAIVariable::is_max_responses_Set() const{
    return m_max_responses_isSet;
}

bool OAIVariable::is_max_responses_Valid() const{
    return m_max_responses_isValid;
}

QString OAIVariable::getName() const {
    return m_name;
}
void OAIVariable::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVariable::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVariable::is_name_Valid() const{
    return m_name_isValid;
}

OAIParentType OAIVariable::getParentType() const {
    return m_parent_type;
}
void OAIVariable::setParentType(const OAIParentType &parent_type) {
    m_parent_type = parent_type;
    m_parent_type_isSet = true;
}

bool OAIVariable::is_parent_type_Set() const{
    return m_parent_type_isSet;
}

bool OAIVariable::is_parent_type_Valid() const{
    return m_parent_type_isValid;
}

QList<OAIVariable> OAIVariable::getQuestions() const {
    return m_questions;
}
void OAIVariable::setQuestions(const QList<OAIVariable> &questions) {
    m_questions = questions;
    m_questions_isSet = true;
}

bool OAIVariable::is_questions_Set() const{
    return m_questions_isSet;
}

bool OAIVariable::is_questions_Valid() const{
    return m_questions_isValid;
}

OAIVariableType OAIVariable::getType() const {
    return m_type;
}
void OAIVariable::setType(const OAIVariableType &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIVariable::is_type_Set() const{
    return m_type_isSet;
}

bool OAIVariable::is_type_Valid() const{
    return m_type_isValid;
}

OAIUseType OAIVariable::getUse() const {
    return m_use;
}
void OAIVariable::setUse(const OAIUseType &use) {
    m_use = use;
    m_use_isSet = true;
}

bool OAIVariable::is_use_Set() const{
    return m_use_isSet;
}

bool OAIVariable::is_use_Valid() const{
    return m_use_isValid;
}

OAIVariableValues OAIVariable::getVariableValues() const {
    return m_variable_values;
}
void OAIVariable::setVariableValues(const OAIVariableValues &variable_values) {
    m_variable_values = variable_values;
    m_variable_values_isSet = true;
}

bool OAIVariable::is_variable_values_Set() const{
    return m_variable_values_isSet;
}

bool OAIVariable::is_variable_values_Valid() const{
    return m_variable_values_isValid;
}

bool OAIVariable::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ident_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_label.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_responses_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_questions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_use.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_variable_values.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVariable::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
