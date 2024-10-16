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

#include "OAIPodcastAudienceResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPodcastAudienceResponse::OAIPodcastAudienceResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPodcastAudienceResponse::OAIPodcastAudienceResponse() {
    this->initializeModel();
}

OAIPodcastAudienceResponse::~OAIPodcastAudienceResponse() {}

void OAIPodcastAudienceResponse::initializeModel() {

    m_by_regions_isSet = false;
    m_by_regions_isValid = false;
}

void OAIPodcastAudienceResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPodcastAudienceResponse::fromJsonObject(QJsonObject json) {

    m_by_regions_isValid = ::OpenAPI::fromJsonValue(m_by_regions, json[QString("by_regions")]);
    m_by_regions_isSet = !json[QString("by_regions")].isNull() && m_by_regions_isValid;
}

QString OAIPodcastAudienceResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPodcastAudienceResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_by_regions.size() > 0) {
        obj.insert(QString("by_regions"), ::OpenAPI::toJsonValue(m_by_regions));
    }
    return obj;
}

QList<OAIPodcastAudienceResponse_by_regions_inner> OAIPodcastAudienceResponse::getByRegions() const {
    return m_by_regions;
}
void OAIPodcastAudienceResponse::setByRegions(const QList<OAIPodcastAudienceResponse_by_regions_inner> &by_regions) {
    m_by_regions = by_regions;
    m_by_regions_isSet = true;
}

bool OAIPodcastAudienceResponse::is_by_regions_Set() const{
    return m_by_regions_isSet;
}

bool OAIPodcastAudienceResponse::is_by_regions_Valid() const{
    return m_by_regions_isValid;
}

bool OAIPodcastAudienceResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_by_regions.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPodcastAudienceResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
