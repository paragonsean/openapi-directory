/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITagSubmission.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITagSubmission::OAITagSubmission(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITagSubmission::OAITagSubmission() {
    this->initializeModel();
}

OAITagSubmission::~OAITagSubmission() {}

void OAITagSubmission::initializeModel() {

    m_colour_isSet = false;
    m_colour_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_tag_set_isSet = false;
    m_tag_set_isValid = false;

    m_url_words_isSet = false;
    m_url_words_isValid = false;
}

void OAITagSubmission::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITagSubmission::fromJsonObject(QJsonObject json) {

    m_colour_isValid = ::OpenAPI::fromJsonValue(m_colour, json[QString("colour")]);
    m_colour_isSet = !json[QString("colour")].isNull() && m_colour_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_tag_set_isValid = ::OpenAPI::fromJsonValue(m_tag_set, json[QString("tagSet")]);
    m_tag_set_isSet = !json[QString("tagSet")].isNull() && m_tag_set_isValid;

    m_url_words_isValid = ::OpenAPI::fromJsonValue(m_url_words, json[QString("urlWords")]);
    m_url_words_isSet = !json[QString("urlWords")].isNull() && m_url_words_isValid;
}

QString OAITagSubmission::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITagSubmission::asJsonObject() const {
    QJsonObject obj;
    if (m_colour_isSet) {
        obj.insert(QString("colour"), ::OpenAPI::toJsonValue(m_colour));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_tag_set.isSet()) {
        obj.insert(QString("tagSet"), ::OpenAPI::toJsonValue(m_tag_set));
    }
    if (m_url_words_isSet) {
        obj.insert(QString("urlWords"), ::OpenAPI::toJsonValue(m_url_words));
    }
    return obj;
}

QString OAITagSubmission::getColour() const {
    return m_colour;
}
void OAITagSubmission::setColour(const QString &colour) {
    m_colour = colour;
    m_colour_isSet = true;
}

bool OAITagSubmission::is_colour_Set() const{
    return m_colour_isSet;
}

bool OAITagSubmission::is_colour_Valid() const{
    return m_colour_isValid;
}

QString OAITagSubmission::getName() const {
    return m_name;
}
void OAITagSubmission::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITagSubmission::is_name_Set() const{
    return m_name_isSet;
}

bool OAITagSubmission::is_name_Valid() const{
    return m_name_isValid;
}

OAITagSet OAITagSubmission::getTagSet() const {
    return m_tag_set;
}
void OAITagSubmission::setTagSet(const OAITagSet &tag_set) {
    m_tag_set = tag_set;
    m_tag_set_isSet = true;
}

bool OAITagSubmission::is_tag_set_Set() const{
    return m_tag_set_isSet;
}

bool OAITagSubmission::is_tag_set_Valid() const{
    return m_tag_set_isValid;
}

QString OAITagSubmission::getUrlWords() const {
    return m_url_words;
}
void OAITagSubmission::setUrlWords(const QString &url_words) {
    m_url_words = url_words;
    m_url_words_isSet = true;
}

bool OAITagSubmission::is_url_words_Set() const{
    return m_url_words_isSet;
}

bool OAITagSubmission::is_url_words_Valid() const{
    return m_url_words_isValid;
}

bool OAITagSubmission::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_colour_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_set.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_words_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITagSubmission::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
