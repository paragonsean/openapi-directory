/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetCountriesDictOut.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetCountriesDictOut::OAIGetCountriesDictOut(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetCountriesDictOut::OAIGetCountriesDictOut() {
    this->initializeModel();
}

OAIGetCountriesDictOut::~OAIGetCountriesDictOut() {}

void OAIGetCountriesDictOut::initializeModel() {

    m_dictionary_isSet = false;
    m_dictionary_isValid = false;
}

void OAIGetCountriesDictOut::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetCountriesDictOut::fromJsonObject(QJsonObject json) {

    m_dictionary_isValid = ::OpenAPI::fromJsonValue(m_dictionary, json[QString("dictionary")]);
    m_dictionary_isSet = !json[QString("dictionary")].isNull() && m_dictionary_isValid;
}

QString OAIGetCountriesDictOut::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetCountriesDictOut::asJsonObject() const {
    QJsonObject obj;
    if (m_dictionary.size() > 0) {
        obj.insert(QString("dictionary"), ::OpenAPI::toJsonValue(m_dictionary));
    }
    return obj;
}

QList<OAICountry_schema> OAIGetCountriesDictOut::getDictionary() const {
    return m_dictionary;
}
void OAIGetCountriesDictOut::setDictionary(const QList<OAICountry_schema> &dictionary) {
    m_dictionary = dictionary;
    m_dictionary_isSet = true;
}

bool OAIGetCountriesDictOut::is_dictionary_Set() const{
    return m_dictionary_isSet;
}

bool OAIGetCountriesDictOut::is_dictionary_Valid() const{
    return m_dictionary_isValid;
}

bool OAIGetCountriesDictOut::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dictionary.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetCountriesDictOut::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
