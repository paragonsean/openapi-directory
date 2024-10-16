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

#include "OAIIEdmType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIEdmType::OAIIEdmType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIEdmType::OAIIEdmType() {
    this->initializeModel();
}

OAIIEdmType::~OAIIEdmType() {}

void OAIIEdmType::initializeModel() {

    m_type_kind_isSet = false;
    m_type_kind_isValid = false;
}

void OAIIEdmType::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIEdmType::fromJsonObject(QJsonObject json) {

    m_type_kind_isValid = ::OpenAPI::fromJsonValue(m_type_kind, json[QString("TypeKind")]);
    m_type_kind_isSet = !json[QString("TypeKind")].isNull() && m_type_kind_isValid;
}

QString OAIIEdmType::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIEdmType::asJsonObject() const {
    QJsonObject obj;
    if (m_type_kind_isSet) {
        obj.insert(QString("TypeKind"), ::OpenAPI::toJsonValue(m_type_kind));
    }
    return obj;
}

qint32 OAIIEdmType::getTypeKind() const {
    return m_type_kind;
}
void OAIIEdmType::setTypeKind(const qint32 &type_kind) {
    m_type_kind = type_kind;
    m_type_kind_isSet = true;
}

bool OAIIEdmType::is_type_kind_Set() const{
    return m_type_kind_isSet;
}

bool OAIIEdmType::is_type_kind_Valid() const{
    return m_type_kind_isValid;
}

bool OAIIEdmType::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_type_kind_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIEdmType::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
