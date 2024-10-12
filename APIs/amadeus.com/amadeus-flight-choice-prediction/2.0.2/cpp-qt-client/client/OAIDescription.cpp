/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDescription.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDescription::OAIDescription(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDescription::OAIDescription() {
    this->initializeModel();
}

OAIDescription::~OAIDescription() {}

void OAIDescription::initializeModel() {

    m_description_type_isSet = false;
    m_description_type_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;
}

void OAIDescription::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDescription::fromJsonObject(QJsonObject json) {

    m_description_type_isValid = ::OpenAPI::fromJsonValue(m_description_type, json[QString("descriptionType")]);
    m_description_type_isSet = !json[QString("descriptionType")].isNull() && m_description_type_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;
}

QString OAIDescription::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDescription::asJsonObject() const {
    QJsonObject obj;
    if (m_description_type_isSet) {
        obj.insert(QString("descriptionType"), ::OpenAPI::toJsonValue(m_description_type));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    return obj;
}

QString OAIDescription::getDescriptionType() const {
    return m_description_type;
}
void OAIDescription::setDescriptionType(const QString &description_type) {
    m_description_type = description_type;
    m_description_type_isSet = true;
}

bool OAIDescription::is_description_type_Set() const{
    return m_description_type_isSet;
}

bool OAIDescription::is_description_type_Valid() const{
    return m_description_type_isValid;
}

QString OAIDescription::getText() const {
    return m_text;
}
void OAIDescription::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIDescription::is_text_Set() const{
    return m_text_isSet;
}

bool OAIDescription::is_text_Valid() const{
    return m_text_isValid;
}

bool OAIDescription::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_type_isSet) {
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

bool OAIDescription::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
