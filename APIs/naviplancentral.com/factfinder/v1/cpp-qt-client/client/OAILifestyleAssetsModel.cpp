/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILifestyleAssetsModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILifestyleAssetsModel::OAILifestyleAssetsModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILifestyleAssetsModel::OAILifestyleAssetsModel() {
    this->initializeModel();
}

OAILifestyleAssetsModel::~OAILifestyleAssetsModel() {}

void OAILifestyleAssetsModel::initializeModel() {

    m_lifestyle_assets_isSet = false;
    m_lifestyle_assets_isValid = false;
}

void OAILifestyleAssetsModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILifestyleAssetsModel::fromJsonObject(QJsonObject json) {

    m_lifestyle_assets_isValid = ::OpenAPI::fromJsonValue(m_lifestyle_assets, json[QString("lifestyleAssets")]);
    m_lifestyle_assets_isSet = !json[QString("lifestyleAssets")].isNull() && m_lifestyle_assets_isValid;
}

QString OAILifestyleAssetsModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILifestyleAssetsModel::asJsonObject() const {
    QJsonObject obj;
    if (m_lifestyle_assets.size() > 0) {
        obj.insert(QString("lifestyleAssets"), ::OpenAPI::toJsonValue(m_lifestyle_assets));
    }
    return obj;
}

QList<OAILifestyleAssetWithIdModel> OAILifestyleAssetsModel::getLifestyleAssets() const {
    return m_lifestyle_assets;
}
void OAILifestyleAssetsModel::setLifestyleAssets(const QList<OAILifestyleAssetWithIdModel> &lifestyle_assets) {
    m_lifestyle_assets = lifestyle_assets;
    m_lifestyle_assets_isSet = true;
}

bool OAILifestyleAssetsModel::is_lifestyle_assets_Set() const{
    return m_lifestyle_assets_isSet;
}

bool OAILifestyleAssetsModel::is_lifestyle_assets_Valid() const{
    return m_lifestyle_assets_isValid;
}

bool OAILifestyleAssetsModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_lifestyle_assets.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILifestyleAssetsModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
