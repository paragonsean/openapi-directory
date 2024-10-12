/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage caches.
 *
 * The version of the OpenAPI document: 2019-08-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUsageModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUsageModel::OAIUsageModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUsageModel::OAIUsageModel() {
    this->initializeModel();
}

OAIUsageModel::~OAIUsageModel() {}

void OAIUsageModel::initializeModel() {

    m_display_isSet = false;
    m_display_isValid = false;

    m_model_name_isSet = false;
    m_model_name_isValid = false;

    m_target_type_isSet = false;
    m_target_type_isValid = false;
}

void OAIUsageModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUsageModel::fromJsonObject(QJsonObject json) {

    m_display_isValid = ::OpenAPI::fromJsonValue(m_display, json[QString("display")]);
    m_display_isSet = !json[QString("display")].isNull() && m_display_isValid;

    m_model_name_isValid = ::OpenAPI::fromJsonValue(m_model_name, json[QString("modelName")]);
    m_model_name_isSet = !json[QString("modelName")].isNull() && m_model_name_isValid;

    m_target_type_isValid = ::OpenAPI::fromJsonValue(m_target_type, json[QString("targetType")]);
    m_target_type_isSet = !json[QString("targetType")].isNull() && m_target_type_isValid;
}

QString OAIUsageModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUsageModel::asJsonObject() const {
    QJsonObject obj;
    if (m_display.isSet()) {
        obj.insert(QString("display"), ::OpenAPI::toJsonValue(m_display));
    }
    if (m_model_name_isSet) {
        obj.insert(QString("modelName"), ::OpenAPI::toJsonValue(m_model_name));
    }
    if (m_target_type_isSet) {
        obj.insert(QString("targetType"), ::OpenAPI::toJsonValue(m_target_type));
    }
    return obj;
}

OAIUsageModel_display OAIUsageModel::getDisplay() const {
    return m_display;
}
void OAIUsageModel::setDisplay(const OAIUsageModel_display &display) {
    m_display = display;
    m_display_isSet = true;
}

bool OAIUsageModel::is_display_Set() const{
    return m_display_isSet;
}

bool OAIUsageModel::is_display_Valid() const{
    return m_display_isValid;
}

QString OAIUsageModel::getModelName() const {
    return m_model_name;
}
void OAIUsageModel::setModelName(const QString &model_name) {
    m_model_name = model_name;
    m_model_name_isSet = true;
}

bool OAIUsageModel::is_model_name_Set() const{
    return m_model_name_isSet;
}

bool OAIUsageModel::is_model_name_Valid() const{
    return m_model_name_isValid;
}

QString OAIUsageModel::getTargetType() const {
    return m_target_type;
}
void OAIUsageModel::setTargetType(const QString &target_type) {
    m_target_type = target_type;
    m_target_type_isSet = true;
}

bool OAIUsageModel::is_target_type_Set() const{
    return m_target_type_isSet;
}

bool OAIUsageModel::is_target_type_Valid() const{
    return m_target_type_isValid;
}

bool OAIUsageModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_display.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUsageModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
