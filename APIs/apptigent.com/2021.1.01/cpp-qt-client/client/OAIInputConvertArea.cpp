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

#include "OAIInputConvertArea.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInputConvertArea::OAIInputConvertArea(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInputConvertArea::OAIInputConvertArea() {
    this->initializeModel();
}

OAIInputConvertArea::~OAIInputConvertArea() {}

void OAIInputConvertArea::initializeModel() {

    m_input_isSet = false;
    m_input_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;
}

void OAIInputConvertArea::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInputConvertArea::fromJsonObject(QJsonObject json) {

    m_input_isValid = ::OpenAPI::fromJsonValue(m_input, json[QString("input")]);
    m_input_isSet = !json[QString("input")].isNull() && m_input_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;
}

QString OAIInputConvertArea::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInputConvertArea::asJsonObject() const {
    QJsonObject obj;
    if (m_input_isSet) {
        obj.insert(QString("input"), ::OpenAPI::toJsonValue(m_input));
    }
    if (m_source_isSet) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_target_isSet) {
        obj.insert(QString("target"), ::OpenAPI::toJsonValue(m_target));
    }
    return obj;
}

double OAIInputConvertArea::getInput() const {
    return m_input;
}
void OAIInputConvertArea::setInput(const double &input) {
    m_input = input;
    m_input_isSet = true;
}

bool OAIInputConvertArea::is_input_Set() const{
    return m_input_isSet;
}

bool OAIInputConvertArea::is_input_Valid() const{
    return m_input_isValid;
}

QString OAIInputConvertArea::getSource() const {
    return m_source;
}
void OAIInputConvertArea::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIInputConvertArea::is_source_Set() const{
    return m_source_isSet;
}

bool OAIInputConvertArea::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIInputConvertArea::getTarget() const {
    return m_target;
}
void OAIInputConvertArea::setTarget(const QString &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIInputConvertArea::is_target_Set() const{
    return m_target_isSet;
}

bool OAIInputConvertArea::is_target_Valid() const{
    return m_target_isValid;
}

bool OAIInputConvertArea::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_input_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInputConvertArea::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_input_isValid && m_source_isValid && m_target_isValid && true;
}

} // namespace OpenAPI
