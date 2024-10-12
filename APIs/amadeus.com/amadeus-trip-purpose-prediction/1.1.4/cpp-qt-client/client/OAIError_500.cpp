/**
 * Trip Purpose Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.1.4
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIError_500.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIError_500::OAIError_500(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIError_500::OAIError_500() {
    this->initializeModel();
}

OAIError_500::~OAIError_500() {}

void OAIError_500::initializeModel() {

    m_errors_isSet = false;
    m_errors_isValid = false;
}

void OAIError_500::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIError_500::fromJsonObject(QJsonObject json) {

    m_errors_isValid = ::OpenAPI::fromJsonValue(m_errors, json[QString("errors")]);
    m_errors_isSet = !json[QString("errors")].isNull() && m_errors_isValid;
}

QString OAIError_500::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIError_500::asJsonObject() const {
    QJsonObject obj;
    if (m_errors.size() > 0) {
        obj.insert(QString("errors"), ::OpenAPI::toJsonValue(m_errors));
    }
    return obj;
}

QList<OAIIssue> OAIError_500::getErrors() const {
    return m_errors;
}
void OAIError_500::setErrors(const QList<OAIIssue> &errors) {
    m_errors = errors;
    m_errors_isSet = true;
}

bool OAIError_500::is_errors_Set() const{
    return m_errors_isSet;
}

bool OAIError_500::is_errors_Valid() const{
    return m_errors_isValid;
}

bool OAIError_500::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_errors.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIError_500::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_errors_isValid && true;
}

} // namespace OpenAPI
