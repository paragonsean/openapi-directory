/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAsyncOperationDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAsyncOperationDetails::OAIAsyncOperationDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAsyncOperationDetails::OAIAsyncOperationDetails() {
    this->initializeModel();
}

OAIAsyncOperationDetails::~OAIAsyncOperationDetails() {}

void OAIAsyncOperationDetails::initializeModel() {

    m_sub_operation_state_isSet = false;
    m_sub_operation_state_isValid = false;

    m_sub_operation_type_isSet = false;
    m_sub_operation_type_isValid = false;
}

void OAIAsyncOperationDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAsyncOperationDetails::fromJsonObject(QJsonObject json) {

    m_sub_operation_state_isValid = ::OpenAPI::fromJsonValue(m_sub_operation_state, json[QString("subOperationState")]);
    m_sub_operation_state_isSet = !json[QString("subOperationState")].isNull() && m_sub_operation_state_isValid;

    m_sub_operation_type_isValid = ::OpenAPI::fromJsonValue(m_sub_operation_type, json[QString("subOperationType")]);
    m_sub_operation_type_isSet = !json[QString("subOperationType")].isNull() && m_sub_operation_type_isValid;
}

QString OAIAsyncOperationDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAsyncOperationDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_sub_operation_state_isSet) {
        obj.insert(QString("subOperationState"), ::OpenAPI::toJsonValue(m_sub_operation_state));
    }
    if (m_sub_operation_type_isSet) {
        obj.insert(QString("subOperationType"), ::OpenAPI::toJsonValue(m_sub_operation_type));
    }
    return obj;
}

QString OAIAsyncOperationDetails::getSubOperationState() const {
    return m_sub_operation_state;
}
void OAIAsyncOperationDetails::setSubOperationState(const QString &sub_operation_state) {
    m_sub_operation_state = sub_operation_state;
    m_sub_operation_state_isSet = true;
}

bool OAIAsyncOperationDetails::is_sub_operation_state_Set() const{
    return m_sub_operation_state_isSet;
}

bool OAIAsyncOperationDetails::is_sub_operation_state_Valid() const{
    return m_sub_operation_state_isValid;
}

QString OAIAsyncOperationDetails::getSubOperationType() const {
    return m_sub_operation_type;
}
void OAIAsyncOperationDetails::setSubOperationType(const QString &sub_operation_type) {
    m_sub_operation_type = sub_operation_type;
    m_sub_operation_type_isSet = true;
}

bool OAIAsyncOperationDetails::is_sub_operation_type_Set() const{
    return m_sub_operation_type_isSet;
}

bool OAIAsyncOperationDetails::is_sub_operation_type_Valid() const{
    return m_sub_operation_type_isValid;
}

bool OAIAsyncOperationDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_sub_operation_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_operation_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAsyncOperationDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
