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

#include "OAIInputStringToFile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInputStringToFile::OAIInputStringToFile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInputStringToFile::OAIInputStringToFile() {
    this->initializeModel();
}

OAIInputStringToFile::~OAIInputStringToFile() {}

void OAIInputStringToFile::initializeModel() {

    m_extension_isSet = false;
    m_extension_isValid = false;

    m_filename_isSet = false;
    m_filename_isValid = false;

    m_input_isSet = false;
    m_input_isValid = false;
}

void OAIInputStringToFile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInputStringToFile::fromJsonObject(QJsonObject json) {

    m_extension_isValid = ::OpenAPI::fromJsonValue(m_extension, json[QString("extension")]);
    m_extension_isSet = !json[QString("extension")].isNull() && m_extension_isValid;

    m_filename_isValid = ::OpenAPI::fromJsonValue(m_filename, json[QString("filename")]);
    m_filename_isSet = !json[QString("filename")].isNull() && m_filename_isValid;

    m_input_isValid = ::OpenAPI::fromJsonValue(m_input, json[QString("input")]);
    m_input_isSet = !json[QString("input")].isNull() && m_input_isValid;
}

QString OAIInputStringToFile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInputStringToFile::asJsonObject() const {
    QJsonObject obj;
    if (m_extension_isSet) {
        obj.insert(QString("extension"), ::OpenAPI::toJsonValue(m_extension));
    }
    if (m_filename_isSet) {
        obj.insert(QString("filename"), ::OpenAPI::toJsonValue(m_filename));
    }
    if (m_input_isSet) {
        obj.insert(QString("input"), ::OpenAPI::toJsonValue(m_input));
    }
    return obj;
}

QString OAIInputStringToFile::getExtension() const {
    return m_extension;
}
void OAIInputStringToFile::setExtension(const QString &extension) {
    m_extension = extension;
    m_extension_isSet = true;
}

bool OAIInputStringToFile::is_extension_Set() const{
    return m_extension_isSet;
}

bool OAIInputStringToFile::is_extension_Valid() const{
    return m_extension_isValid;
}

QString OAIInputStringToFile::getFilename() const {
    return m_filename;
}
void OAIInputStringToFile::setFilename(const QString &filename) {
    m_filename = filename;
    m_filename_isSet = true;
}

bool OAIInputStringToFile::is_filename_Set() const{
    return m_filename_isSet;
}

bool OAIInputStringToFile::is_filename_Valid() const{
    return m_filename_isValid;
}

QString OAIInputStringToFile::getInput() const {
    return m_input;
}
void OAIInputStringToFile::setInput(const QString &input) {
    m_input = input;
    m_input_isSet = true;
}

bool OAIInputStringToFile::is_input_Set() const{
    return m_input_isSet;
}

bool OAIInputStringToFile::is_input_Valid() const{
    return m_input_isValid;
}

bool OAIInputStringToFile::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_extension_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_filename_isSet) {
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

bool OAIInputStringToFile::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_extension_isValid && m_filename_isValid && m_input_isValid && true;
}

} // namespace OpenAPI
