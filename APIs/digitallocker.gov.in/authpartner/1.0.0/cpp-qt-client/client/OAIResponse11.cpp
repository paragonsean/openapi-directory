/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResponse11.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResponse11::OAIResponse11(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResponse11::OAIResponse11() {
    this->initializeModel();
}

OAIResponse11::~OAIResponse11() {}

void OAIResponse11::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;

    m_error_description_isSet = false;
    m_error_description_isValid = false;
}

void OAIResponse11::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResponse11::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_error_description_isValid = ::OpenAPI::fromJsonValue(m_error_description, json[QString("error_description")]);
    m_error_description_isSet = !json[QString("error_description")].isNull() && m_error_description_isValid;
}

QString OAIResponse11::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResponse11::asJsonObject() const {
    QJsonObject obj;
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_error_description_isSet) {
        obj.insert(QString("error_description"), ::OpenAPI::toJsonValue(m_error_description));
    }
    return obj;
}

QString OAIResponse11::getError() const {
    return m_error;
}
void OAIResponse11::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIResponse11::is_error_Set() const{
    return m_error_isSet;
}

bool OAIResponse11::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIResponse11::getErrorDescription() const {
    return m_error_description;
}
void OAIResponse11::setErrorDescription(const QString &error_description) {
    m_error_description = error_description;
    m_error_description_isSet = true;
}

bool OAIResponse11::is_error_description_Set() const{
    return m_error_description_isSet;
}

bool OAIResponse11::is_error_description_Valid() const{
    return m_error_description_isValid;
}

bool OAIResponse11::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_description_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResponse11::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
