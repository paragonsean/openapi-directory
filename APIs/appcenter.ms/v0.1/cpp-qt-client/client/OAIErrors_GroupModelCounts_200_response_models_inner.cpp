/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIErrors_GroupModelCounts_200_response_models_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIErrors_GroupModelCounts_200_response_models_inner::OAIErrors_GroupModelCounts_200_response_models_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIErrors_GroupModelCounts_200_response_models_inner::OAIErrors_GroupModelCounts_200_response_models_inner() {
    this->initializeModel();
}

OAIErrors_GroupModelCounts_200_response_models_inner::~OAIErrors_GroupModelCounts_200_response_models_inner() {}

void OAIErrors_GroupModelCounts_200_response_models_inner::initializeModel() {

    m_error_count_isSet = false;
    m_error_count_isValid = false;

    m_model_code_isSet = false;
    m_model_code_isValid = false;

    m_model_name_isSet = false;
    m_model_name_isValid = false;
}

void OAIErrors_GroupModelCounts_200_response_models_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIErrors_GroupModelCounts_200_response_models_inner::fromJsonObject(QJsonObject json) {

    m_error_count_isValid = ::OpenAPI::fromJsonValue(m_error_count, json[QString("errorCount")]);
    m_error_count_isSet = !json[QString("errorCount")].isNull() && m_error_count_isValid;

    m_model_code_isValid = ::OpenAPI::fromJsonValue(m_model_code, json[QString("modelCode")]);
    m_model_code_isSet = !json[QString("modelCode")].isNull() && m_model_code_isValid;

    m_model_name_isValid = ::OpenAPI::fromJsonValue(m_model_name, json[QString("modelName")]);
    m_model_name_isSet = !json[QString("modelName")].isNull() && m_model_name_isValid;
}

QString OAIErrors_GroupModelCounts_200_response_models_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIErrors_GroupModelCounts_200_response_models_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_error_count_isSet) {
        obj.insert(QString("errorCount"), ::OpenAPI::toJsonValue(m_error_count));
    }
    if (m_model_code_isSet) {
        obj.insert(QString("modelCode"), ::OpenAPI::toJsonValue(m_model_code));
    }
    if (m_model_name_isSet) {
        obj.insert(QString("modelName"), ::OpenAPI::toJsonValue(m_model_name));
    }
    return obj;
}

qint64 OAIErrors_GroupModelCounts_200_response_models_inner::getErrorCount() const {
    return m_error_count;
}
void OAIErrors_GroupModelCounts_200_response_models_inner::setErrorCount(const qint64 &error_count) {
    m_error_count = error_count;
    m_error_count_isSet = true;
}

bool OAIErrors_GroupModelCounts_200_response_models_inner::is_error_count_Set() const{
    return m_error_count_isSet;
}

bool OAIErrors_GroupModelCounts_200_response_models_inner::is_error_count_Valid() const{
    return m_error_count_isValid;
}

QString OAIErrors_GroupModelCounts_200_response_models_inner::getModelCode() const {
    return m_model_code;
}
void OAIErrors_GroupModelCounts_200_response_models_inner::setModelCode(const QString &model_code) {
    m_model_code = model_code;
    m_model_code_isSet = true;
}

bool OAIErrors_GroupModelCounts_200_response_models_inner::is_model_code_Set() const{
    return m_model_code_isSet;
}

bool OAIErrors_GroupModelCounts_200_response_models_inner::is_model_code_Valid() const{
    return m_model_code_isValid;
}

QString OAIErrors_GroupModelCounts_200_response_models_inner::getModelName() const {
    return m_model_name;
}
void OAIErrors_GroupModelCounts_200_response_models_inner::setModelName(const QString &model_name) {
    m_model_name = model_name;
    m_model_name_isSet = true;
}

bool OAIErrors_GroupModelCounts_200_response_models_inner::is_model_name_Set() const{
    return m_model_name_isSet;
}

bool OAIErrors_GroupModelCounts_200_response_models_inner::is_model_name_Valid() const{
    return m_model_name_isValid;
}

bool OAIErrors_GroupModelCounts_200_response_models_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIErrors_GroupModelCounts_200_response_models_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
