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

#include "OAIWarning_texts_warning_text_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWarning_texts_warning_text_inner::OAIWarning_texts_warning_text_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWarning_texts_warning_text_inner::OAIWarning_texts_warning_text_inner() {
    this->initializeModel();
}

OAIWarning_texts_warning_text_inner::~OAIWarning_texts_warning_text_inner() {}

void OAIWarning_texts_warning_text_inner::initializeModel() {

    m_text_isSet = false;
    m_text_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_warning_text_isSet = false;
    m_warning_text_isValid = false;
}

void OAIWarning_texts_warning_text_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWarning_texts_warning_text_inner::fromJsonObject(QJsonObject json) {

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("#text")]);
    m_text_isSet = !json[QString("#text")].isNull() && m_text_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("length")]);
    m_length_isSet = !json[QString("length")].isNull() && m_length_isValid;

    m_warning_text_isValid = ::OpenAPI::fromJsonValue(m_warning_text, json[QString("warning_text")]);
    m_warning_text_isSet = !json[QString("warning_text")].isNull() && m_warning_text_isValid;
}

QString OAIWarning_texts_warning_text_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWarning_texts_warning_text_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_text_isSet) {
        obj.insert(QString("#text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_length_isSet) {
        obj.insert(QString("length"), ::OpenAPI::toJsonValue(m_length));
    }
    if (m_warning_text.size() > 0) {
        obj.insert(QString("warning_text"), ::OpenAPI::toJsonValue(m_warning_text));
    }
    return obj;
}

QString OAIWarning_texts_warning_text_inner::getText() const {
    return m_text;
}
void OAIWarning_texts_warning_text_inner::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIWarning_texts_warning_text_inner::is_text_Set() const{
    return m_text_isSet;
}

bool OAIWarning_texts_warning_text_inner::is_text_Valid() const{
    return m_text_isValid;
}

QString OAIWarning_texts_warning_text_inner::getLength() const {
    return m_length;
}
void OAIWarning_texts_warning_text_inner::setLength(const QString &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAIWarning_texts_warning_text_inner::is_length_Set() const{
    return m_length_isSet;
}

bool OAIWarning_texts_warning_text_inner::is_length_Valid() const{
    return m_length_isValid;
}

QList<OAIWarning_texts_warning_text_inner_warning_text_inner> OAIWarning_texts_warning_text_inner::getWarningText() const {
    return m_warning_text;
}
void OAIWarning_texts_warning_text_inner::setWarningText(const QList<OAIWarning_texts_warning_text_inner_warning_text_inner> &warning_text) {
    m_warning_text = warning_text;
    m_warning_text_isSet = true;
}

bool OAIWarning_texts_warning_text_inner::is_warning_text_Set() const{
    return m_warning_text_isSet;
}

bool OAIWarning_texts_warning_text_inner::is_warning_text_Valid() const{
    return m_warning_text_isValid;
}

bool OAIWarning_texts_warning_text_inner::isSet() const {
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

        if (m_warning_text.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWarning_texts_warning_text_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
