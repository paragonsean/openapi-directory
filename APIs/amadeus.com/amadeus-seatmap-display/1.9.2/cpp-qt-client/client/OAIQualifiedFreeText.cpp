/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQualifiedFreeText.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQualifiedFreeText::OAIQualifiedFreeText(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQualifiedFreeText::OAIQualifiedFreeText() {
    this->initializeModel();
}

OAIQualifiedFreeText::~OAIQualifiedFreeText() {}

void OAIQualifiedFreeText::initializeModel() {

    m_lang_isSet = false;
    m_lang_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;
}

void OAIQualifiedFreeText::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQualifiedFreeText::fromJsonObject(QJsonObject json) {

    m_lang_isValid = ::OpenAPI::fromJsonValue(m_lang, json[QString("lang")]);
    m_lang_isSet = !json[QString("lang")].isNull() && m_lang_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;
}

QString OAIQualifiedFreeText::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQualifiedFreeText::asJsonObject() const {
    QJsonObject obj;
    if (m_lang_isSet) {
        obj.insert(QString("lang"), ::OpenAPI::toJsonValue(m_lang));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    return obj;
}

QString OAIQualifiedFreeText::getLang() const {
    return m_lang;
}
void OAIQualifiedFreeText::setLang(const QString &lang) {
    m_lang = lang;
    m_lang_isSet = true;
}

bool OAIQualifiedFreeText::is_lang_Set() const{
    return m_lang_isSet;
}

bool OAIQualifiedFreeText::is_lang_Valid() const{
    return m_lang_isValid;
}

QString OAIQualifiedFreeText::getText() const {
    return m_text;
}
void OAIQualifiedFreeText::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIQualifiedFreeText::is_text_Set() const{
    return m_text_isSet;
}

bool OAIQualifiedFreeText::is_text_Valid() const{
    return m_text_isValid;
}

bool OAIQualifiedFreeText::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_lang_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQualifiedFreeText::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
