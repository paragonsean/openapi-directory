/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImageProcessingSettings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageProcessingSettings::OAIImageProcessingSettings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageProcessingSettings::OAIImageProcessingSettings() {
    this->initializeModel();
}

OAIImageProcessingSettings::~OAIImageProcessingSettings() {}

void OAIImageProcessingSettings::initializeModel() {

    m_augmentation_methods_isSet = false;
    m_augmentation_methods_isValid = false;
}

void OAIImageProcessingSettings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageProcessingSettings::fromJsonObject(QJsonObject json) {

    m_augmentation_methods_isValid = ::OpenAPI::fromJsonValue(m_augmentation_methods, json[QString("augmentationMethods")]);
    m_augmentation_methods_isSet = !json[QString("augmentationMethods")].isNull() && m_augmentation_methods_isValid;
}

QString OAIImageProcessingSettings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageProcessingSettings::asJsonObject() const {
    QJsonObject obj;
    if (m_augmentation_methods.size() > 0) {
        obj.insert(QString("augmentationMethods"), ::OpenAPI::toJsonValue(m_augmentation_methods));
    }
    return obj;
}

QMap<QString, bool> OAIImageProcessingSettings::getAugmentationMethods() const {
    return m_augmentation_methods;
}
void OAIImageProcessingSettings::setAugmentationMethods(const QMap<QString, bool> &augmentation_methods) {
    m_augmentation_methods = augmentation_methods;
    m_augmentation_methods_isSet = true;
}

bool OAIImageProcessingSettings::is_augmentation_methods_Set() const{
    return m_augmentation_methods_isSet;
}

bool OAIImageProcessingSettings::is_augmentation_methods_Valid() const{
    return m_augmentation_methods_isValid;
}

bool OAIImageProcessingSettings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_augmentation_methods.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImageProcessingSettings::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
