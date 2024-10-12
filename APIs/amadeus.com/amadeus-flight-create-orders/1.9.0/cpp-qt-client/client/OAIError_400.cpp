/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIError_400.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIError_400::OAIError_400(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIError_400::OAIError_400() {
    this->initializeModel();
}

OAIError_400::~OAIError_400() {}

void OAIError_400::initializeModel() {

    m_errors_isSet = false;
    m_errors_isValid = false;
}

void OAIError_400::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIError_400::fromJsonObject(QJsonObject json) {

    m_errors_isValid = ::OpenAPI::fromJsonValue(m_errors, json[QString("errors")]);
    m_errors_isSet = !json[QString("errors")].isNull() && m_errors_isValid;
}

QString OAIError_400::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIError_400::asJsonObject() const {
    QJsonObject obj;
    if (m_errors.size() > 0) {
        obj.insert(QString("errors"), ::OpenAPI::toJsonValue(m_errors));
    }
    return obj;
}

QList<OAIIssue> OAIError_400::getErrors() const {
    return m_errors;
}
void OAIError_400::setErrors(const QList<OAIIssue> &errors) {
    m_errors = errors;
    m_errors_isSet = true;
}

bool OAIError_400::is_errors_Set() const{
    return m_errors_isSet;
}

bool OAIError_400::is_errors_Valid() const{
    return m_errors_isValid;
}

bool OAIError_400::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_errors.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIError_400::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_errors_isValid && true;
}

} // namespace OpenAPI
