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

#include "OAIRangeVariable.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRangeVariable::OAIRangeVariable(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRangeVariable::OAIRangeVariable() {
    this->initializeModel();
}

OAIRangeVariable::~OAIRangeVariable() {}

void OAIRangeVariable::initializeModel() {

    m_kind_isSet = false;
    m_kind_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_reference_isSet = false;
    m_type_reference_isValid = false;
}

void OAIRangeVariable::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRangeVariable::fromJsonObject(QJsonObject json) {

    m_kind_isValid = ::OpenAPI::fromJsonValue(m_kind, json[QString("Kind")]);
    m_kind_isSet = !json[QString("Kind")].isNull() && m_kind_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_type_reference_isValid = ::OpenAPI::fromJsonValue(m_type_reference, json[QString("TypeReference")]);
    m_type_reference_isSet = !json[QString("TypeReference")].isNull() && m_type_reference_isValid;
}

QString OAIRangeVariable::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRangeVariable::asJsonObject() const {
    QJsonObject obj;
    if (m_kind_isSet) {
        obj.insert(QString("Kind"), ::OpenAPI::toJsonValue(m_kind));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_reference.isSet()) {
        obj.insert(QString("TypeReference"), ::OpenAPI::toJsonValue(m_type_reference));
    }
    return obj;
}

qint32 OAIRangeVariable::getKind() const {
    return m_kind;
}
void OAIRangeVariable::setKind(const qint32 &kind) {
    m_kind = kind;
    m_kind_isSet = true;
}

bool OAIRangeVariable::is_kind_Set() const{
    return m_kind_isSet;
}

bool OAIRangeVariable::is_kind_Valid() const{
    return m_kind_isValid;
}

QString OAIRangeVariable::getName() const {
    return m_name;
}
void OAIRangeVariable::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIRangeVariable::is_name_Set() const{
    return m_name_isSet;
}

bool OAIRangeVariable::is_name_Valid() const{
    return m_name_isValid;
}

OAIIEdmTypeReference OAIRangeVariable::getTypeReference() const {
    return m_type_reference;
}
void OAIRangeVariable::setTypeReference(const OAIIEdmTypeReference &type_reference) {
    m_type_reference = type_reference;
    m_type_reference_isSet = true;
}

bool OAIRangeVariable::is_type_reference_Set() const{
    return m_type_reference_isSet;
}

bool OAIRangeVariable::is_type_reference_Valid() const{
    return m_type_reference_isValid;
}

bool OAIRangeVariable::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_kind_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_reference.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRangeVariable::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
