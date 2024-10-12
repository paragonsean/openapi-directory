/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIInputSplitString.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInputSplitString::OAIInputSplitString(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInputSplitString::OAIInputSplitString() {
    this->initializeModel();
}

OAIInputSplitString::~OAIInputSplitString() {}

void OAIInputSplitString::initializeModel() {

    m_characters_isSet = false;
    m_characters_isValid = false;

    m_input_isSet = false;
    m_input_isValid = false;
}

void OAIInputSplitString::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInputSplitString::fromJsonObject(QJsonObject json) {

    m_characters_isValid = ::OpenAPI::fromJsonValue(m_characters, json[QString("characters")]);
    m_characters_isSet = !json[QString("characters")].isNull() && m_characters_isValid;

    m_input_isValid = ::OpenAPI::fromJsonValue(m_input, json[QString("input")]);
    m_input_isSet = !json[QString("input")].isNull() && m_input_isValid;
}

QString OAIInputSplitString::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInputSplitString::asJsonObject() const {
    QJsonObject obj;
    if (m_characters_isSet) {
        obj.insert(QString("characters"), ::OpenAPI::toJsonValue(m_characters));
    }
    if (m_input_isSet) {
        obj.insert(QString("input"), ::OpenAPI::toJsonValue(m_input));
    }
    return obj;
}

QString OAIInputSplitString::getCharacters() const {
    return m_characters;
}
void OAIInputSplitString::setCharacters(const QString &characters) {
    m_characters = characters;
    m_characters_isSet = true;
}

bool OAIInputSplitString::is_characters_Set() const{
    return m_characters_isSet;
}

bool OAIInputSplitString::is_characters_Valid() const{
    return m_characters_isValid;
}

QString OAIInputSplitString::getInput() const {
    return m_input;
}
void OAIInputSplitString::setInput(const QString &input) {
    m_input = input;
    m_input_isSet = true;
}

bool OAIInputSplitString::is_input_Set() const{
    return m_input_isSet;
}

bool OAIInputSplitString::is_input_Valid() const{
    return m_input_isValid;
}

bool OAIInputSplitString::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_characters_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_input_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInputSplitString::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_characters_isValid && m_input_isValid && true;
}

} // namespace OpenAPI
