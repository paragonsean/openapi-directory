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

#include "OAIAvailable_media_sets_media_sets_media_set_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAvailable_media_sets_media_sets_media_set_inner::OAIAvailable_media_sets_media_sets_media_set_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAvailable_media_sets_media_sets_media_set_inner::OAIAvailable_media_sets_media_sets_media_set_inner() {
    this->initializeModel();
}

OAIAvailable_media_sets_media_sets_media_set_inner::~OAIAvailable_media_sets_media_sets_media_set_inner() {}

void OAIAvailable_media_sets_media_sets_media_set_inner::initializeModel() {

    m_text_isSet = false;
    m_text_isValid = false;

    m_media_sets_isSet = false;
    m_media_sets_isValid = false;
}

void OAIAvailable_media_sets_media_sets_media_set_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAvailable_media_sets_media_sets_media_set_inner::fromJsonObject(QJsonObject json) {

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("#text")]);
    m_text_isSet = !json[QString("#text")].isNull() && m_text_isValid;

    m_media_sets_isValid = ::OpenAPI::fromJsonValue(m_media_sets, json[QString("media_sets")]);
    m_media_sets_isSet = !json[QString("media_sets")].isNull() && m_media_sets_isValid;
}

QString OAIAvailable_media_sets_media_sets_media_set_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAvailable_media_sets_media_sets_media_set_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_text_isSet) {
        obj.insert(QString("#text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_media_sets.isSet()) {
        obj.insert(QString("media_sets"), ::OpenAPI::toJsonValue(m_media_sets));
    }
    return obj;
}

QString OAIAvailable_media_sets_media_sets_media_set_inner::getText() const {
    return m_text;
}
void OAIAvailable_media_sets_media_sets_media_set_inner::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIAvailable_media_sets_media_sets_media_set_inner::is_text_Set() const{
    return m_text_isSet;
}

bool OAIAvailable_media_sets_media_sets_media_set_inner::is_text_Valid() const{
    return m_text_isValid;
}

OAIAvailable_media_sets_media_sets_media_set_inner_media_sets OAIAvailable_media_sets_media_sets_media_set_inner::getMediaSets() const {
    return m_media_sets;
}
void OAIAvailable_media_sets_media_sets_media_set_inner::setMediaSets(const OAIAvailable_media_sets_media_sets_media_set_inner_media_sets &media_sets) {
    m_media_sets = media_sets;
    m_media_sets_isSet = true;
}

bool OAIAvailable_media_sets_media_sets_media_set_inner::is_media_sets_Set() const{
    return m_media_sets_isSet;
}

bool OAIAvailable_media_sets_media_sets_media_set_inner::is_media_sets_Valid() const{
    return m_media_sets_isValid;
}

bool OAIAvailable_media_sets_media_sets_media_set_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_media_sets.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAvailable_media_sets_media_sets_media_set_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
