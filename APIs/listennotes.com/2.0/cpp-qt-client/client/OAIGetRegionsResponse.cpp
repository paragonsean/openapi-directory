/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetRegionsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetRegionsResponse::OAIGetRegionsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetRegionsResponse::OAIGetRegionsResponse() {
    this->initializeModel();
}

OAIGetRegionsResponse::~OAIGetRegionsResponse() {}

void OAIGetRegionsResponse::initializeModel() {

    m_regions_isSet = false;
    m_regions_isValid = false;
}

void OAIGetRegionsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetRegionsResponse::fromJsonObject(QJsonObject json) {

    m_regions_isValid = ::OpenAPI::fromJsonValue(m_regions, json[QString("regions")]);
    m_regions_isSet = !json[QString("regions")].isNull() && m_regions_isValid;
}

QString OAIGetRegionsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetRegionsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_regions_isSet) {
        obj.insert(QString("regions"), ::OpenAPI::toJsonValue(m_regions));
    }
    return obj;
}

OAIObject OAIGetRegionsResponse::getRegions() const {
    return m_regions;
}
void OAIGetRegionsResponse::setRegions(const OAIObject &regions) {
    m_regions = regions;
    m_regions_isSet = true;
}

bool OAIGetRegionsResponse::is_regions_Set() const{
    return m_regions_isSet;
}

bool OAIGetRegionsResponse::is_regions_Valid() const{
    return m_regions_isValid;
}

bool OAIGetRegionsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_regions_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetRegionsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_regions_isValid && true;
}

} // namespace OpenAPI
