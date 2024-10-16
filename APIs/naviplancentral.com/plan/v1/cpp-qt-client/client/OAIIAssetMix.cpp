/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIAssetMix.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIAssetMix::OAIIAssetMix(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIAssetMix::OAIIAssetMix() {
    this->initializeModel();
}

OAIIAssetMix::~OAIIAssetMix() {}

void OAIIAssetMix::initializeModel() {

    m_asset_class_display_level_isSet = false;
    m_asset_class_display_level_isValid = false;

    m_asset_class_info_for_display_level_isSet = false;
    m_asset_class_info_for_display_level_isValid = false;

    m_classes_isSet = false;
    m_classes_isValid = false;

    m_super_asset_classes_isSet = false;
    m_super_asset_classes_isValid = false;
}

void OAIIAssetMix::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIAssetMix::fromJsonObject(QJsonObject json) {

    m_asset_class_display_level_isValid = ::OpenAPI::fromJsonValue(m_asset_class_display_level, json[QString("assetClassDisplayLevel")]);
    m_asset_class_display_level_isSet = !json[QString("assetClassDisplayLevel")].isNull() && m_asset_class_display_level_isValid;

    m_asset_class_info_for_display_level_isValid = ::OpenAPI::fromJsonValue(m_asset_class_info_for_display_level, json[QString("assetClassInfoForDisplayLevel")]);
    m_asset_class_info_for_display_level_isSet = !json[QString("assetClassInfoForDisplayLevel")].isNull() && m_asset_class_info_for_display_level_isValid;

    m_classes_isValid = ::OpenAPI::fromJsonValue(m_classes, json[QString("classes")]);
    m_classes_isSet = !json[QString("classes")].isNull() && m_classes_isValid;

    m_super_asset_classes_isValid = ::OpenAPI::fromJsonValue(m_super_asset_classes, json[QString("superAssetClasses")]);
    m_super_asset_classes_isSet = !json[QString("superAssetClasses")].isNull() && m_super_asset_classes_isValid;
}

QString OAIIAssetMix::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIAssetMix::asJsonObject() const {
    QJsonObject obj;
    if (m_asset_class_display_level_isSet) {
        obj.insert(QString("assetClassDisplayLevel"), ::OpenAPI::toJsonValue(m_asset_class_display_level));
    }
    if (m_asset_class_info_for_display_level.size() > 0) {
        obj.insert(QString("assetClassInfoForDisplayLevel"), ::OpenAPI::toJsonValue(m_asset_class_info_for_display_level));
    }
    if (m_classes.size() > 0) {
        obj.insert(QString("classes"), ::OpenAPI::toJsonValue(m_classes));
    }
    if (m_super_asset_classes.size() > 0) {
        obj.insert(QString("superAssetClasses"), ::OpenAPI::toJsonValue(m_super_asset_classes));
    }
    return obj;
}

qint32 OAIIAssetMix::getAssetClassDisplayLevel() const {
    return m_asset_class_display_level;
}
void OAIIAssetMix::setAssetClassDisplayLevel(const qint32 &asset_class_display_level) {
    m_asset_class_display_level = asset_class_display_level;
    m_asset_class_display_level_isSet = true;
}

bool OAIIAssetMix::is_asset_class_display_level_Set() const{
    return m_asset_class_display_level_isSet;
}

bool OAIIAssetMix::is_asset_class_display_level_Valid() const{
    return m_asset_class_display_level_isValid;
}

QList<qint32> OAIIAssetMix::getAssetClassInfoForDisplayLevel() const {
    return m_asset_class_info_for_display_level;
}
void OAIIAssetMix::setAssetClassInfoForDisplayLevel(const QList<qint32> &asset_class_info_for_display_level) {
    m_asset_class_info_for_display_level = asset_class_info_for_display_level;
    m_asset_class_info_for_display_level_isSet = true;
}

bool OAIIAssetMix::is_asset_class_info_for_display_level_Set() const{
    return m_asset_class_info_for_display_level_isSet;
}

bool OAIIAssetMix::is_asset_class_info_for_display_level_Valid() const{
    return m_asset_class_info_for_display_level_isValid;
}

QList<OAIIAssetClass> OAIIAssetMix::getClasses() const {
    return m_classes;
}
void OAIIAssetMix::setClasses(const QList<OAIIAssetClass> &classes) {
    m_classes = classes;
    m_classes_isSet = true;
}

bool OAIIAssetMix::is_classes_Set() const{
    return m_classes_isSet;
}

bool OAIIAssetMix::is_classes_Valid() const{
    return m_classes_isValid;
}

QList<OAIIAssetClass> OAIIAssetMix::getSuperAssetClasses() const {
    return m_super_asset_classes;
}
void OAIIAssetMix::setSuperAssetClasses(const QList<OAIIAssetClass> &super_asset_classes) {
    m_super_asset_classes = super_asset_classes;
    m_super_asset_classes_isSet = true;
}

bool OAIIAssetMix::is_super_asset_classes_Set() const{
    return m_super_asset_classes_isSet;
}

bool OAIIAssetMix::is_super_asset_classes_Valid() const{
    return m_super_asset_classes_isValid;
}

bool OAIIAssetMix::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_asset_class_display_level_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_asset_class_info_for_display_level.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_classes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_super_asset_classes.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIAssetMix::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
