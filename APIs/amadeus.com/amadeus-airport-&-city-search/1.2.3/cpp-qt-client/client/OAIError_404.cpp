/**
 * Airport & City Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, in test this API only contains data from the United States, Spain, United Kingdom, Germany and India. 
 *
 * The version of the OpenAPI document: 1.2.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIError_404.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIError_404::OAIError_404(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIError_404::OAIError_404() {
    this->initializeModel();
}

OAIError_404::~OAIError_404() {}

void OAIError_404::initializeModel() {

    m_errors_isSet = false;
    m_errors_isValid = false;
}

void OAIError_404::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIError_404::fromJsonObject(QJsonObject json) {

    m_errors_isValid = ::OpenAPI::fromJsonValue(m_errors, json[QString("errors")]);
    m_errors_isSet = !json[QString("errors")].isNull() && m_errors_isValid;
}

QString OAIError_404::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIError_404::asJsonObject() const {
    QJsonObject obj;
    if (m_errors.size() > 0) {
        obj.insert(QString("errors"), ::OpenAPI::toJsonValue(m_errors));
    }
    return obj;
}

QList<OAIIssue> OAIError_404::getErrors() const {
    return m_errors;
}
void OAIError_404::setErrors(const QList<OAIIssue> &errors) {
    m_errors = errors;
    m_errors_isSet = true;
}

bool OAIError_404::is_errors_Set() const{
    return m_errors_isSet;
}

bool OAIError_404::is_errors_Valid() const{
    return m_errors_isValid;
}

bool OAIError_404::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_errors.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIError_404::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_errors_isValid && true;
}

} // namespace OpenAPI
