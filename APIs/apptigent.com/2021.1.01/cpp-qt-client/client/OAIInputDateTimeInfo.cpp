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

#include "OAIInputDateTimeInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInputDateTimeInfo::OAIInputDateTimeInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInputDateTimeInfo::OAIInputDateTimeInfo() {
    this->initializeModel();
}

OAIInputDateTimeInfo::~OAIInputDateTimeInfo() {}

void OAIInputDateTimeInfo::initializeModel() {

    m_culture_isSet = false;
    m_culture_isValid = false;

    m_input_isSet = false;
    m_input_isValid = false;
}

void OAIInputDateTimeInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInputDateTimeInfo::fromJsonObject(QJsonObject json) {

    m_culture_isValid = ::OpenAPI::fromJsonValue(m_culture, json[QString("culture")]);
    m_culture_isSet = !json[QString("culture")].isNull() && m_culture_isValid;

    m_input_isValid = ::OpenAPI::fromJsonValue(m_input, json[QString("input")]);
    m_input_isSet = !json[QString("input")].isNull() && m_input_isValid;
}

QString OAIInputDateTimeInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInputDateTimeInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_culture_isSet) {
        obj.insert(QString("culture"), ::OpenAPI::toJsonValue(m_culture));
    }
    if (m_input_isSet) {
        obj.insert(QString("input"), ::OpenAPI::toJsonValue(m_input));
    }
    return obj;
}

QString OAIInputDateTimeInfo::getCulture() const {
    return m_culture;
}
void OAIInputDateTimeInfo::setCulture(const QString &culture) {
    m_culture = culture;
    m_culture_isSet = true;
}

bool OAIInputDateTimeInfo::is_culture_Set() const{
    return m_culture_isSet;
}

bool OAIInputDateTimeInfo::is_culture_Valid() const{
    return m_culture_isValid;
}

QString OAIInputDateTimeInfo::getInput() const {
    return m_input;
}
void OAIInputDateTimeInfo::setInput(const QString &input) {
    m_input = input;
    m_input_isSet = true;
}

bool OAIInputDateTimeInfo::is_input_Set() const{
    return m_input_isSet;
}

bool OAIInputDateTimeInfo::is_input_Valid() const{
    return m_input_isValid;
}

bool OAIInputDateTimeInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_culture_isSet) {
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

bool OAIInputDateTimeInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_culture_isValid && m_input_isValid && true;
}

} // namespace OpenAPI
