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

#include "OAIIAssetCategories.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIAssetCategories::OAIIAssetCategories(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIAssetCategories::OAIIAssetCategories() {
    this->initializeModel();
}

OAIIAssetCategories::~OAIIAssetCategories() {}

void OAIIAssetCategories::initializeModel() {

    m_all_assets_isSet = false;
    m_all_assets_isValid = false;

    m_business_assets_isSet = false;
    m_business_assets_isValid = false;

    m_lifestyle_assets_isSet = false;
    m_lifestyle_assets_isValid = false;

    m_non_qualified_annuities_isSet = false;
    m_non_qualified_annuities_isValid = false;

    m_non_qualified_assets_isSet = false;
    m_non_qualified_assets_isValid = false;

    m_private_corporations_isSet = false;
    m_private_corporations_isValid = false;

    m_qualified_annuities_isSet = false;
    m_qualified_annuities_isValid = false;

    m_qualified_assets_isSet = false;
    m_qualified_assets_isValid = false;

    m_real_estate_isSet = false;
    m_real_estate_isValid = false;

    m_total_assets_isSet = false;
    m_total_assets_isValid = false;
}

void OAIIAssetCategories::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIAssetCategories::fromJsonObject(QJsonObject json) {

    m_all_assets_isValid = ::OpenAPI::fromJsonValue(m_all_assets, json[QString("allAssets")]);
    m_all_assets_isSet = !json[QString("allAssets")].isNull() && m_all_assets_isValid;

    m_business_assets_isValid = ::OpenAPI::fromJsonValue(m_business_assets, json[QString("businessAssets")]);
    m_business_assets_isSet = !json[QString("businessAssets")].isNull() && m_business_assets_isValid;

    m_lifestyle_assets_isValid = ::OpenAPI::fromJsonValue(m_lifestyle_assets, json[QString("lifestyleAssets")]);
    m_lifestyle_assets_isSet = !json[QString("lifestyleAssets")].isNull() && m_lifestyle_assets_isValid;

    m_non_qualified_annuities_isValid = ::OpenAPI::fromJsonValue(m_non_qualified_annuities, json[QString("nonQualifiedAnnuities")]);
    m_non_qualified_annuities_isSet = !json[QString("nonQualifiedAnnuities")].isNull() && m_non_qualified_annuities_isValid;

    m_non_qualified_assets_isValid = ::OpenAPI::fromJsonValue(m_non_qualified_assets, json[QString("nonQualifiedAssets")]);
    m_non_qualified_assets_isSet = !json[QString("nonQualifiedAssets")].isNull() && m_non_qualified_assets_isValid;

    m_private_corporations_isValid = ::OpenAPI::fromJsonValue(m_private_corporations, json[QString("privateCorporations")]);
    m_private_corporations_isSet = !json[QString("privateCorporations")].isNull() && m_private_corporations_isValid;

    m_qualified_annuities_isValid = ::OpenAPI::fromJsonValue(m_qualified_annuities, json[QString("qualifiedAnnuities")]);
    m_qualified_annuities_isSet = !json[QString("qualifiedAnnuities")].isNull() && m_qualified_annuities_isValid;

    m_qualified_assets_isValid = ::OpenAPI::fromJsonValue(m_qualified_assets, json[QString("qualifiedAssets")]);
    m_qualified_assets_isSet = !json[QString("qualifiedAssets")].isNull() && m_qualified_assets_isValid;

    m_real_estate_isValid = ::OpenAPI::fromJsonValue(m_real_estate, json[QString("realEstate")]);
    m_real_estate_isSet = !json[QString("realEstate")].isNull() && m_real_estate_isValid;

    m_total_assets_isValid = ::OpenAPI::fromJsonValue(m_total_assets, json[QString("totalAssets")]);
    m_total_assets_isSet = !json[QString("totalAssets")].isNull() && m_total_assets_isValid;
}

QString OAIIAssetCategories::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIAssetCategories::asJsonObject() const {
    QJsonObject obj;
    if (m_all_assets.size() > 0) {
        obj.insert(QString("allAssets"), ::OpenAPI::toJsonValue(m_all_assets));
    }
    if (m_business_assets.isSet()) {
        obj.insert(QString("businessAssets"), ::OpenAPI::toJsonValue(m_business_assets));
    }
    if (m_lifestyle_assets.isSet()) {
        obj.insert(QString("lifestyleAssets"), ::OpenAPI::toJsonValue(m_lifestyle_assets));
    }
    if (m_non_qualified_annuities.isSet()) {
        obj.insert(QString("nonQualifiedAnnuities"), ::OpenAPI::toJsonValue(m_non_qualified_annuities));
    }
    if (m_non_qualified_assets.isSet()) {
        obj.insert(QString("nonQualifiedAssets"), ::OpenAPI::toJsonValue(m_non_qualified_assets));
    }
    if (m_private_corporations.isSet()) {
        obj.insert(QString("privateCorporations"), ::OpenAPI::toJsonValue(m_private_corporations));
    }
    if (m_qualified_annuities.isSet()) {
        obj.insert(QString("qualifiedAnnuities"), ::OpenAPI::toJsonValue(m_qualified_annuities));
    }
    if (m_qualified_assets.isSet()) {
        obj.insert(QString("qualifiedAssets"), ::OpenAPI::toJsonValue(m_qualified_assets));
    }
    if (m_real_estate.isSet()) {
        obj.insert(QString("realEstate"), ::OpenAPI::toJsonValue(m_real_estate));
    }
    if (m_total_assets.isSet()) {
        obj.insert(QString("totalAssets"), ::OpenAPI::toJsonValue(m_total_assets));
    }
    return obj;
}

QList<OAIIValueDescriptionPair_Currency> OAIIAssetCategories::getAllAssets() const {
    return m_all_assets;
}
void OAIIAssetCategories::setAllAssets(const QList<OAIIValueDescriptionPair_Currency> &all_assets) {
    m_all_assets = all_assets;
    m_all_assets_isSet = true;
}

bool OAIIAssetCategories::is_all_assets_Set() const{
    return m_all_assets_isSet;
}

bool OAIIAssetCategories::is_all_assets_Valid() const{
    return m_all_assets_isValid;
}

OAIINetWorthCategory OAIIAssetCategories::getBusinessAssets() const {
    return m_business_assets;
}
void OAIIAssetCategories::setBusinessAssets(const OAIINetWorthCategory &business_assets) {
    m_business_assets = business_assets;
    m_business_assets_isSet = true;
}

bool OAIIAssetCategories::is_business_assets_Set() const{
    return m_business_assets_isSet;
}

bool OAIIAssetCategories::is_business_assets_Valid() const{
    return m_business_assets_isValid;
}

OAIINetWorthCategory OAIIAssetCategories::getLifestyleAssets() const {
    return m_lifestyle_assets;
}
void OAIIAssetCategories::setLifestyleAssets(const OAIINetWorthCategory &lifestyle_assets) {
    m_lifestyle_assets = lifestyle_assets;
    m_lifestyle_assets_isSet = true;
}

bool OAIIAssetCategories::is_lifestyle_assets_Set() const{
    return m_lifestyle_assets_isSet;
}

bool OAIIAssetCategories::is_lifestyle_assets_Valid() const{
    return m_lifestyle_assets_isValid;
}

OAIINetWorthCategory OAIIAssetCategories::getNonQualifiedAnnuities() const {
    return m_non_qualified_annuities;
}
void OAIIAssetCategories::setNonQualifiedAnnuities(const OAIINetWorthCategory &non_qualified_annuities) {
    m_non_qualified_annuities = non_qualified_annuities;
    m_non_qualified_annuities_isSet = true;
}

bool OAIIAssetCategories::is_non_qualified_annuities_Set() const{
    return m_non_qualified_annuities_isSet;
}

bool OAIIAssetCategories::is_non_qualified_annuities_Valid() const{
    return m_non_qualified_annuities_isValid;
}

OAIINetWorthCategory OAIIAssetCategories::getNonQualifiedAssets() const {
    return m_non_qualified_assets;
}
void OAIIAssetCategories::setNonQualifiedAssets(const OAIINetWorthCategory &non_qualified_assets) {
    m_non_qualified_assets = non_qualified_assets;
    m_non_qualified_assets_isSet = true;
}

bool OAIIAssetCategories::is_non_qualified_assets_Set() const{
    return m_non_qualified_assets_isSet;
}

bool OAIIAssetCategories::is_non_qualified_assets_Valid() const{
    return m_non_qualified_assets_isValid;
}

OAIINetWorthCategory OAIIAssetCategories::getPrivateCorporations() const {
    return m_private_corporations;
}
void OAIIAssetCategories::setPrivateCorporations(const OAIINetWorthCategory &private_corporations) {
    m_private_corporations = private_corporations;
    m_private_corporations_isSet = true;
}

bool OAIIAssetCategories::is_private_corporations_Set() const{
    return m_private_corporations_isSet;
}

bool OAIIAssetCategories::is_private_corporations_Valid() const{
    return m_private_corporations_isValid;
}

OAIINetWorthCategory OAIIAssetCategories::getQualifiedAnnuities() const {
    return m_qualified_annuities;
}
void OAIIAssetCategories::setQualifiedAnnuities(const OAIINetWorthCategory &qualified_annuities) {
    m_qualified_annuities = qualified_annuities;
    m_qualified_annuities_isSet = true;
}

bool OAIIAssetCategories::is_qualified_annuities_Set() const{
    return m_qualified_annuities_isSet;
}

bool OAIIAssetCategories::is_qualified_annuities_Valid() const{
    return m_qualified_annuities_isValid;
}

OAIINetWorthCategory OAIIAssetCategories::getQualifiedAssets() const {
    return m_qualified_assets;
}
void OAIIAssetCategories::setQualifiedAssets(const OAIINetWorthCategory &qualified_assets) {
    m_qualified_assets = qualified_assets;
    m_qualified_assets_isSet = true;
}

bool OAIIAssetCategories::is_qualified_assets_Set() const{
    return m_qualified_assets_isSet;
}

bool OAIIAssetCategories::is_qualified_assets_Valid() const{
    return m_qualified_assets_isValid;
}

OAIINetWorthCategory OAIIAssetCategories::getRealEstate() const {
    return m_real_estate;
}
void OAIIAssetCategories::setRealEstate(const OAIINetWorthCategory &real_estate) {
    m_real_estate = real_estate;
    m_real_estate_isSet = true;
}

bool OAIIAssetCategories::is_real_estate_Set() const{
    return m_real_estate_isSet;
}

bool OAIIAssetCategories::is_real_estate_Valid() const{
    return m_real_estate_isValid;
}

OAIINetWorthCategory OAIIAssetCategories::getTotalAssets() const {
    return m_total_assets;
}
void OAIIAssetCategories::setTotalAssets(const OAIINetWorthCategory &total_assets) {
    m_total_assets = total_assets;
    m_total_assets_isSet = true;
}

bool OAIIAssetCategories::is_total_assets_Set() const{
    return m_total_assets_isSet;
}

bool OAIIAssetCategories::is_total_assets_Valid() const{
    return m_total_assets_isValid;
}

bool OAIIAssetCategories::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_all_assets.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_business_assets.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_lifestyle_assets.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_non_qualified_annuities.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_non_qualified_assets.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_private_corporations.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_qualified_annuities.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_qualified_assets.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_real_estate.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_assets.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIAssetCategories::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
