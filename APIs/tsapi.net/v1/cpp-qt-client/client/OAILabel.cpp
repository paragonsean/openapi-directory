/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILabel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILabel::OAILabel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILabel::OAILabel() {
    this->initializeModel();
}

OAILabel::~OAILabel() {}

void OAILabel::initializeModel() {

    m_alt_labels_isSet = false;
    m_alt_labels_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;
}

void OAILabel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILabel::fromJsonObject(QJsonObject json) {

    m_alt_labels_isValid = ::OpenAPI::fromJsonValue(m_alt_labels, json[QString("altLabels")]);
    m_alt_labels_isSet = !json[QString("altLabels")].isNull() && m_alt_labels_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;
}

QString OAILabel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILabel::asJsonObject() const {
    QJsonObject obj;
    if (m_alt_labels.size() > 0) {
        obj.insert(QString("altLabels"), ::OpenAPI::toJsonValue(m_alt_labels));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    return obj;
}

QList<OAIAltLabel> OAILabel::getAltLabels() const {
    return m_alt_labels;
}
void OAILabel::setAltLabels(const QList<OAIAltLabel> &alt_labels) {
    m_alt_labels = alt_labels;
    m_alt_labels_isSet = true;
}

bool OAILabel::is_alt_labels_Set() const{
    return m_alt_labels_isSet;
}

bool OAILabel::is_alt_labels_Valid() const{
    return m_alt_labels_isValid;
}

QString OAILabel::getText() const {
    return m_text;
}
void OAILabel::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAILabel::is_text_Set() const{
    return m_text_isSet;
}

bool OAILabel::is_text_Valid() const{
    return m_text_isValid;
}

bool OAILabel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alt_labels.size() > 0) {
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

bool OAILabel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
