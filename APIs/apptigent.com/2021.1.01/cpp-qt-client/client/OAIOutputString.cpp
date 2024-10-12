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

#include "OAIOutputString.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOutputString::OAIOutputString(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOutputString::OAIOutputString() {
    this->initializeModel();
}

OAIOutputString::~OAIOutputString() {}

void OAIOutputString::initializeModel() {

    m_result_isSet = false;
    m_result_isValid = false;
}

void OAIOutputString::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOutputString::fromJsonObject(QJsonObject json) {

    m_result_isValid = ::OpenAPI::fromJsonValue(m_result, json[QString("result")]);
    m_result_isSet = !json[QString("result")].isNull() && m_result_isValid;
}

QString OAIOutputString::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOutputString::asJsonObject() const {
    QJsonObject obj;
    if (m_result_isSet) {
        obj.insert(QString("result"), ::OpenAPI::toJsonValue(m_result));
    }
    return obj;
}

QString OAIOutputString::getResult() const {
    return m_result;
}
void OAIOutputString::setResult(const QString &result) {
    m_result = result;
    m_result_isSet = true;
}

bool OAIOutputString::is_result_Set() const{
    return m_result_isSet;
}

bool OAIOutputString::is_result_Valid() const{
    return m_result_isValid;
}

bool OAIOutputString::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_result_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOutputString::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
