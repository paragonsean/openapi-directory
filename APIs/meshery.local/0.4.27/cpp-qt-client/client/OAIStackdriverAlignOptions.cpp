/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStackdriverAlignOptions.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStackdriverAlignOptions::OAIStackdriverAlignOptions(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStackdriverAlignOptions::OAIStackdriverAlignOptions() {
    this->initializeModel();
}

OAIStackdriverAlignOptions::~OAIStackdriverAlignOptions() {}

void OAIStackdriverAlignOptions::initializeModel() {

    m_expanded_isSet = false;
    m_expanded_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_options_isSet = false;
    m_options_isValid = false;
}

void OAIStackdriverAlignOptions::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStackdriverAlignOptions::fromJsonObject(QJsonObject json) {

    m_expanded_isValid = ::OpenAPI::fromJsonValue(m_expanded, json[QString("expanded")]);
    m_expanded_isSet = !json[QString("expanded")].isNull() && m_expanded_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_options_isValid = ::OpenAPI::fromJsonValue(m_options, json[QString("options")]);
    m_options_isSet = !json[QString("options")].isNull() && m_options_isValid;
}

QString OAIStackdriverAlignOptions::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStackdriverAlignOptions::asJsonObject() const {
    QJsonObject obj;
    if (m_expanded_isSet) {
        obj.insert(QString("expanded"), ::OpenAPI::toJsonValue(m_expanded));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_options.size() > 0) {
        obj.insert(QString("options"), ::OpenAPI::toJsonValue(m_options));
    }
    return obj;
}

bool OAIStackdriverAlignOptions::isExpanded() const {
    return m_expanded;
}
void OAIStackdriverAlignOptions::setExpanded(const bool &expanded) {
    m_expanded = expanded;
    m_expanded_isSet = true;
}

bool OAIStackdriverAlignOptions::is_expanded_Set() const{
    return m_expanded_isSet;
}

bool OAIStackdriverAlignOptions::is_expanded_Valid() const{
    return m_expanded_isValid;
}

QString OAIStackdriverAlignOptions::getLabel() const {
    return m_label;
}
void OAIStackdriverAlignOptions::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIStackdriverAlignOptions::is_label_Set() const{
    return m_label_isSet;
}

bool OAIStackdriverAlignOptions::is_label_Valid() const{
    return m_label_isValid;
}

QList<OAIStackdriverAlignOption> OAIStackdriverAlignOptions::getOptions() const {
    return m_options;
}
void OAIStackdriverAlignOptions::setOptions(const QList<OAIStackdriverAlignOption> &options) {
    m_options = options;
    m_options_isSet = true;
}

bool OAIStackdriverAlignOptions::is_options_Set() const{
    return m_options_isSet;
}

bool OAIStackdriverAlignOptions::is_options_Valid() const{
    return m_options_isValid;
}

bool OAIStackdriverAlignOptions::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_expanded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStackdriverAlignOptions::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
