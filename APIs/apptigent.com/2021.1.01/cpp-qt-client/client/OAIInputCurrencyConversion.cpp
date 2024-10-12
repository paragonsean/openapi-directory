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

#include "OAIInputCurrencyConversion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInputCurrencyConversion::OAIInputCurrencyConversion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInputCurrencyConversion::OAIInputCurrencyConversion() {
    this->initializeModel();
}

OAIInputCurrencyConversion::~OAIInputCurrencyConversion() {}

void OAIInputCurrencyConversion::initializeModel() {

    m_input_isSet = false;
    m_input_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;
}

void OAIInputCurrencyConversion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInputCurrencyConversion::fromJsonObject(QJsonObject json) {

    m_input_isValid = ::OpenAPI::fromJsonValue(m_input, json[QString("input")]);
    m_input_isSet = !json[QString("input")].isNull() && m_input_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;
}

QString OAIInputCurrencyConversion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInputCurrencyConversion::asJsonObject() const {
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

double OAIInputCurrencyConversion::getInput() const {
    return m_input;
}
void OAIInputCurrencyConversion::setInput(const double &input) {
    m_input = input;
    m_input_isSet = true;
}

bool OAIInputCurrencyConversion::is_input_Set() const{
    return m_input_isSet;
}

bool OAIInputCurrencyConversion::is_input_Valid() const{
    return m_input_isValid;
}

QString OAIInputCurrencyConversion::getSource() const {
    return m_source;
}
void OAIInputCurrencyConversion::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIInputCurrencyConversion::is_source_Set() const{
    return m_source_isSet;
}

bool OAIInputCurrencyConversion::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIInputCurrencyConversion::getTarget() const {
    return m_target;
}
void OAIInputCurrencyConversion::setTarget(const QString &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIInputCurrencyConversion::is_target_Set() const{
    return m_target_isSet;
}

bool OAIInputCurrencyConversion::is_target_Valid() const{
    return m_target_isValid;
}

bool OAIInputCurrencyConversion::isSet() const {
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

bool OAIInputCurrencyConversion::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_input_isValid && m_source_isValid && m_target_isValid && true;
}

} // namespace OpenAPI
