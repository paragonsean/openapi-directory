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

#include "OAIGuidance_warnings_warnings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGuidance_warnings_warnings::OAIGuidance_warnings_warnings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGuidance_warnings_warnings::OAIGuidance_warnings_warnings() {
    this->initializeModel();
}

OAIGuidance_warnings_warnings::~OAIGuidance_warnings_warnings() {}

void OAIGuidance_warnings_warnings::initializeModel() {

    m_warning_items_isSet = false;
    m_warning_items_isValid = false;

    m_warning_texts_isSet = false;
    m_warning_texts_isValid = false;

    m_warnings_isSet = false;
    m_warnings_isValid = false;
}

void OAIGuidance_warnings_warnings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGuidance_warnings_warnings::fromJsonObject(QJsonObject json) {

    m_warning_items_isValid = ::OpenAPI::fromJsonValue(m_warning_items, json[QString("warning_items")]);
    m_warning_items_isSet = !json[QString("warning_items")].isNull() && m_warning_items_isValid;

    m_warning_texts_isValid = ::OpenAPI::fromJsonValue(m_warning_texts, json[QString("warning_texts")]);
    m_warning_texts_isSet = !json[QString("warning_texts")].isNull() && m_warning_texts_isValid;

    m_warnings_isValid = ::OpenAPI::fromJsonValue(m_warnings, json[QString("warnings")]);
    m_warnings_isSet = !json[QString("warnings")].isNull() && m_warnings_isValid;
}

QString OAIGuidance_warnings_warnings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGuidance_warnings_warnings::asJsonObject() const {
    QJsonObject obj;
    if (m_warning_items.isSet()) {
        obj.insert(QString("warning_items"), ::OpenAPI::toJsonValue(m_warning_items));
    }
    if (m_warning_texts.isSet()) {
        obj.insert(QString("warning_texts"), ::OpenAPI::toJsonValue(m_warning_texts));
    }
    if (m_warnings.isSet()) {
        obj.insert(QString("warnings"), ::OpenAPI::toJsonValue(m_warnings));
    }
    return obj;
}

OAIWarning_items OAIGuidance_warnings_warnings::getWarningItems() const {
    return m_warning_items;
}
void OAIGuidance_warnings_warnings::setWarningItems(const OAIWarning_items &warning_items) {
    m_warning_items = warning_items;
    m_warning_items_isSet = true;
}

bool OAIGuidance_warnings_warnings::is_warning_items_Set() const{
    return m_warning_items_isSet;
}

bool OAIGuidance_warnings_warnings::is_warning_items_Valid() const{
    return m_warning_items_isValid;
}

OAIWarning_texts OAIGuidance_warnings_warnings::getWarningTexts() const {
    return m_warning_texts;
}
void OAIGuidance_warnings_warnings::setWarningTexts(const OAIWarning_texts &warning_texts) {
    m_warning_texts = warning_texts;
    m_warning_texts_isSet = true;
}

bool OAIGuidance_warnings_warnings::is_warning_texts_Set() const{
    return m_warning_texts_isSet;
}

bool OAIGuidance_warnings_warnings::is_warning_texts_Valid() const{
    return m_warning_texts_isValid;
}

OAIGuidance_warnings_warnings_warnings OAIGuidance_warnings_warnings::getWarnings() const {
    return m_warnings;
}
void OAIGuidance_warnings_warnings::setWarnings(const OAIGuidance_warnings_warnings_warnings &warnings) {
    m_warnings = warnings;
    m_warnings_isSet = true;
}

bool OAIGuidance_warnings_warnings::is_warnings_Set() const{
    return m_warnings_isSet;
}

bool OAIGuidance_warnings_warnings::is_warnings_Valid() const{
    return m_warnings_isValid;
}

bool OAIGuidance_warnings_warnings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_warning_items.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_warning_texts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_warnings.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGuidance_warnings_warnings::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
