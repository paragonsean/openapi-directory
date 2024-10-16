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

#include "OAIRealEstateAssetsModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRealEstateAssetsModel::OAIRealEstateAssetsModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRealEstateAssetsModel::OAIRealEstateAssetsModel() {
    this->initializeModel();
}

OAIRealEstateAssetsModel::~OAIRealEstateAssetsModel() {}

void OAIRealEstateAssetsModel::initializeModel() {

    m_real_estate_assets_isSet = false;
    m_real_estate_assets_isValid = false;
}

void OAIRealEstateAssetsModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRealEstateAssetsModel::fromJsonObject(QJsonObject json) {

    m_real_estate_assets_isValid = ::OpenAPI::fromJsonValue(m_real_estate_assets, json[QString("realEstateAssets")]);
    m_real_estate_assets_isSet = !json[QString("realEstateAssets")].isNull() && m_real_estate_assets_isValid;
}

QString OAIRealEstateAssetsModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRealEstateAssetsModel::asJsonObject() const {
    QJsonObject obj;
    if (m_real_estate_assets.size() > 0) {
        obj.insert(QString("realEstateAssets"), ::OpenAPI::toJsonValue(m_real_estate_assets));
    }
    return obj;
}

QList<OAIRealEstateAssetWithIdModel> OAIRealEstateAssetsModel::getRealEstateAssets() const {
    return m_real_estate_assets;
}
void OAIRealEstateAssetsModel::setRealEstateAssets(const QList<OAIRealEstateAssetWithIdModel> &real_estate_assets) {
    m_real_estate_assets = real_estate_assets;
    m_real_estate_assets_isSet = true;
}

bool OAIRealEstateAssetsModel::is_real_estate_assets_Set() const{
    return m_real_estate_assets_isSet;
}

bool OAIRealEstateAssetsModel::is_real_estate_assets_Valid() const{
    return m_real_estate_assets_isValid;
}

bool OAIRealEstateAssetsModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_real_estate_assets.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRealEstateAssetsModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
