/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGuidance_warnings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGuidance_warnings::OAIGuidance_warnings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGuidance_warnings::OAIGuidance_warnings() {
    this->initializeModel();
}

OAIGuidance_warnings::~OAIGuidance_warnings() {}

void OAIGuidance_warnings::initializeModel() {

    m_warnings_isSet = false;
    m_warnings_isValid = false;
}

void OAIGuidance_warnings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGuidance_warnings::fromJsonObject(QJsonObject json) {

    m_warnings_isValid = ::OpenAPI::fromJsonValue(m_warnings, json[QString("warnings")]);
    m_warnings_isSet = !json[QString("warnings")].isNull() && m_warnings_isValid;
}

QString OAIGuidance_warnings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGuidance_warnings::asJsonObject() const {
    QJsonObject obj;
    if (m_warnings.isSet()) {
        obj.insert(QString("warnings"), ::OpenAPI::toJsonValue(m_warnings));
    }
    return obj;
}

OAIGuidance_warnings_warnings OAIGuidance_warnings::getWarnings() const {
    return m_warnings;
}
void OAIGuidance_warnings::setWarnings(const OAIGuidance_warnings_warnings &warnings) {
    m_warnings = warnings;
    m_warnings_isSet = true;
}

bool OAIGuidance_warnings::is_warnings_Set() const{
    return m_warnings_isSet;
}

bool OAIGuidance_warnings::is_warnings_Valid() const{
    return m_warnings_isValid;
}

bool OAIGuidance_warnings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_warnings.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGuidance_warnings::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
