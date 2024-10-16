/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIErrorResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIErrorResponse::OAIErrorResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIErrorResponse::OAIErrorResponse() {
    this->initializeModel();
}

OAIErrorResponse::~OAIErrorResponse() {}

void OAIErrorResponse::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;
}

void OAIErrorResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIErrorResponse::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;
}

QString OAIErrorResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIErrorResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    return obj;
}

QString OAIErrorResponse::getCode() const {
    return m_code;
}
void OAIErrorResponse::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIErrorResponse::is_code_Set() const{
    return m_code_isSet;
}

bool OAIErrorResponse::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIErrorResponse::getDescription() const {
    return m_description;
}
void OAIErrorResponse::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIErrorResponse::is_description_Set() const{
    return m_description_isSet;
}

bool OAIErrorResponse::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIErrorResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIErrorResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
