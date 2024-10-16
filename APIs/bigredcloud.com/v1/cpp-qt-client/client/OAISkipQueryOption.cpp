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

#include "OAISkipQueryOption.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISkipQueryOption::OAISkipQueryOption(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISkipQueryOption::OAISkipQueryOption() {
    this->initializeModel();
}

OAISkipQueryOption::~OAISkipQueryOption() {}

void OAISkipQueryOption::initializeModel() {

    m_context_isSet = false;
    m_context_isValid = false;

    m_raw_value_isSet = false;
    m_raw_value_isValid = false;

    m_validator_isSet = false;
    m_validator_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAISkipQueryOption::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISkipQueryOption::fromJsonObject(QJsonObject json) {

    m_context_isValid = ::OpenAPI::fromJsonValue(m_context, json[QString("Context")]);
    m_context_isSet = !json[QString("Context")].isNull() && m_context_isValid;

    m_raw_value_isValid = ::OpenAPI::fromJsonValue(m_raw_value, json[QString("RawValue")]);
    m_raw_value_isSet = !json[QString("RawValue")].isNull() && m_raw_value_isValid;

    m_validator_isValid = ::OpenAPI::fromJsonValue(m_validator, json[QString("Validator")]);
    m_validator_isSet = !json[QString("Validator")].isNull() && m_validator_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("Value")]);
    m_value_isSet = !json[QString("Value")].isNull() && m_value_isValid;
}

QString OAISkipQueryOption::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISkipQueryOption::asJsonObject() const {
    QJsonObject obj;
    if (m_context.isSet()) {
        obj.insert(QString("Context"), ::OpenAPI::toJsonValue(m_context));
    }
    if (m_raw_value_isSet) {
        obj.insert(QString("RawValue"), ::OpenAPI::toJsonValue(m_raw_value));
    }
    if (m_validator_isSet) {
        obj.insert(QString("Validator"), ::OpenAPI::toJsonValue(m_validator));
    }
    if (m_value_isSet) {
        obj.insert(QString("Value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

OAIODataQueryContext OAISkipQueryOption::getContext() const {
    return m_context;
}
void OAISkipQueryOption::setContext(const OAIODataQueryContext &context) {
    m_context = context;
    m_context_isSet = true;
}

bool OAISkipQueryOption::is_context_Set() const{
    return m_context_isSet;
}

bool OAISkipQueryOption::is_context_Valid() const{
    return m_context_isValid;
}

QString OAISkipQueryOption::getRawValue() const {
    return m_raw_value;
}
void OAISkipQueryOption::setRawValue(const QString &raw_value) {
    m_raw_value = raw_value;
    m_raw_value_isSet = true;
}

bool OAISkipQueryOption::is_raw_value_Set() const{
    return m_raw_value_isSet;
}

bool OAISkipQueryOption::is_raw_value_Valid() const{
    return m_raw_value_isValid;
}

OAIObject OAISkipQueryOption::getValidator() const {
    return m_validator;
}
void OAISkipQueryOption::setValidator(const OAIObject &validator) {
    m_validator = validator;
    m_validator_isSet = true;
}

bool OAISkipQueryOption::is_validator_Set() const{
    return m_validator_isSet;
}

bool OAISkipQueryOption::is_validator_Valid() const{
    return m_validator_isValid;
}

qint32 OAISkipQueryOption::getValue() const {
    return m_value;
}
void OAISkipQueryOption::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAISkipQueryOption::is_value_Set() const{
    return m_value_isSet;
}

bool OAISkipQueryOption::is_value_Valid() const{
    return m_value_isValid;
}

bool OAISkipQueryOption::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_context.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_raw_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_validator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISkipQueryOption::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
