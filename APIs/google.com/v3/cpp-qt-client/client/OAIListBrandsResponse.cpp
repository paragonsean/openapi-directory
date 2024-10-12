/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIListBrandsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListBrandsResponse::OAIListBrandsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListBrandsResponse::OAIListBrandsResponse() {
    this->initializeModel();
}

OAIListBrandsResponse::~OAIListBrandsResponse() {}

void OAIListBrandsResponse::initializeModel() {

    m_brands_isSet = false;
    m_brands_isValid = false;
}

void OAIListBrandsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListBrandsResponse::fromJsonObject(QJsonObject json) {

    m_brands_isValid = ::OpenAPI::fromJsonValue(m_brands, json[QString("brands")]);
    m_brands_isSet = !json[QString("brands")].isNull() && m_brands_isValid;
}

QString OAIListBrandsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListBrandsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_brands.size() > 0) {
        obj.insert(QString("brands"), ::OpenAPI::toJsonValue(m_brands));
    }
    return obj;
}

QList<OAIBrand> OAIListBrandsResponse::getBrands() const {
    return m_brands;
}
void OAIListBrandsResponse::setBrands(const QList<OAIBrand> &brands) {
    m_brands = brands;
    m_brands_isSet = true;
}

bool OAIListBrandsResponse::is_brands_Set() const{
    return m_brands_isSet;
}

bool OAIListBrandsResponse::is_brands_Valid() const{
    return m_brands_isValid;
}

bool OAIListBrandsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_brands.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListBrandsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
