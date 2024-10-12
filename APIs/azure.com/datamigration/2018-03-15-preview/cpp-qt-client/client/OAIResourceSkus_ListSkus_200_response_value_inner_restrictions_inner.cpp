/**
 * Azure Data Migration Service Resource Provider
 * The Data Migration Service helps people migrate their data from on-premise database servers to Azure, or from older database software to newer software. The service manages one or more workers that are joined to a customer's virtual network, which is assumed to provide connectivity to their databases. To avoid frequent updates to the resource provider, data migration tasks are implemented by the resource provider in a generic way as task resources, each of which has a task type (which identifies the type of work to run), input, and output. The client is responsible for providing appropriate task type and inputs, which will be passed through unexamined to the machines that implement the functionality, and for understanding the output, which is passed back unexamined to the client.
 *
 * The version of the OpenAPI document: 2018-03-15-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner() {
    this->initializeModel();
}

OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::~OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner() {}

void OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::initializeModel() {

    m_reason_code_isSet = false;
    m_reason_code_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_values_isSet = false;
    m_values_isValid = false;
}

void OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::fromJsonObject(QJsonObject json) {

    m_reason_code_isValid = ::OpenAPI::fromJsonValue(m_reason_code, json[QString("reasonCode")]);
    m_reason_code_isSet = !json[QString("reasonCode")].isNull() && m_reason_code_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_values_isValid = ::OpenAPI::fromJsonValue(m_values, json[QString("values")]);
    m_values_isSet = !json[QString("values")].isNull() && m_values_isValid;
}

QString OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_reason_code_isSet) {
        obj.insert(QString("reasonCode"), ::OpenAPI::toJsonValue(m_reason_code));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_values.size() > 0) {
        obj.insert(QString("values"), ::OpenAPI::toJsonValue(m_values));
    }
    return obj;
}

QString OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::getReasonCode() const {
    return m_reason_code;
}
void OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::setReasonCode(const QString &reason_code) {
    m_reason_code = reason_code;
    m_reason_code_isSet = true;
}

bool OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::is_reason_code_Set() const{
    return m_reason_code_isSet;
}

bool OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::is_reason_code_Valid() const{
    return m_reason_code_isValid;
}

QString OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::getType() const {
    return m_type;
}
void OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::is_type_Valid() const{
    return m_type_isValid;
}

QList<QString> OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::getValues() const {
    return m_values;
}
void OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::setValues(const QList<QString> &values) {
    m_values = values;
    m_values_isSet = true;
}

bool OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::is_values_Set() const{
    return m_values_isSet;
}

bool OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::is_values_Valid() const{
    return m_values_isValid;
}

bool OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_reason_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_values.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
