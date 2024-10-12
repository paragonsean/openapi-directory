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

#include "OAIWarning_text.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWarning_text::OAIWarning_text(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWarning_text::OAIWarning_text() {
    this->initializeModel();
}

OAIWarning_text::~OAIWarning_text() {}

void OAIWarning_text::initializeModel() {

    m_text_isSet = false;
    m_text_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;
}

void OAIWarning_text::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWarning_text::fromJsonObject(QJsonObject json) {

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("#text")]);
    m_text_isSet = !json[QString("#text")].isNull() && m_text_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("length")]);
    m_length_isSet = !json[QString("length")].isNull() && m_length_isValid;
}

QString OAIWarning_text::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWarning_text::asJsonObject() const {
    QJsonObject obj;
    if (m_text_isSet) {
        obj.insert(QString("#text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_length_isSet) {
        obj.insert(QString("length"), ::OpenAPI::toJsonValue(m_length));
    }
    return obj;
}

QString OAIWarning_text::getText() const {
    return m_text;
}
void OAIWarning_text::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIWarning_text::is_text_Set() const{
    return m_text_isSet;
}

bool OAIWarning_text::is_text_Valid() const{
    return m_text_isValid;
}

QString OAIWarning_text::getLength() const {
    return m_length;
}
void OAIWarning_text::setLength(const QString &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAIWarning_text::is_length_Set() const{
    return m_length_isSet;
}

bool OAIWarning_text::is_length_Valid() const{
    return m_length_isValid;
}

bool OAIWarning_text::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWarning_text::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
