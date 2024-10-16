/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPersonalisedRadioMetaData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPersonalisedRadioMetaData::OAIPersonalisedRadioMetaData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPersonalisedRadioMetaData::OAIPersonalisedRadioMetaData() {
    this->initializeModel();
}

OAIPersonalisedRadioMetaData::~OAIPersonalisedRadioMetaData() {}

void OAIPersonalisedRadioMetaData::initializeModel() {

    m_key_isSet = false;
    m_key_isValid = false;
}

void OAIPersonalisedRadioMetaData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPersonalisedRadioMetaData::fromJsonObject(QJsonObject json) {

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("key")]);
    m_key_isSet = !json[QString("key")].isNull() && m_key_isValid;
}

QString OAIPersonalisedRadioMetaData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPersonalisedRadioMetaData::asJsonObject() const {
    QJsonObject obj;
    if (m_key_isSet) {
        obj.insert(QString("key"), ::OpenAPI::toJsonValue(m_key));
    }
    return obj;
}

QString OAIPersonalisedRadioMetaData::getKey() const {
    return m_key;
}
void OAIPersonalisedRadioMetaData::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAIPersonalisedRadioMetaData::is_key_Set() const{
    return m_key_isSet;
}

bool OAIPersonalisedRadioMetaData::is_key_Valid() const{
    return m_key_isValid;
}

bool OAIPersonalisedRadioMetaData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_key_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPersonalisedRadioMetaData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_key_isValid && true;
}

} // namespace OpenAPI
