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

#include "OAIListHotelViewsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListHotelViewsResponse::OAIListHotelViewsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListHotelViewsResponse::OAIListHotelViewsResponse() {
    this->initializeModel();
}

OAIListHotelViewsResponse::~OAIListHotelViewsResponse() {}

void OAIListHotelViewsResponse::initializeModel() {

    m_hotel_views_isSet = false;
    m_hotel_views_isValid = false;

    m_next_page_token_isSet = false;
    m_next_page_token_isValid = false;
}

void OAIListHotelViewsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListHotelViewsResponse::fromJsonObject(QJsonObject json) {

    m_hotel_views_isValid = ::OpenAPI::fromJsonValue(m_hotel_views, json[QString("hotelViews")]);
    m_hotel_views_isSet = !json[QString("hotelViews")].isNull() && m_hotel_views_isValid;

    m_next_page_token_isValid = ::OpenAPI::fromJsonValue(m_next_page_token, json[QString("nextPageToken")]);
    m_next_page_token_isSet = !json[QString("nextPageToken")].isNull() && m_next_page_token_isValid;
}

QString OAIListHotelViewsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListHotelViewsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_hotel_views.size() > 0) {
        obj.insert(QString("hotelViews"), ::OpenAPI::toJsonValue(m_hotel_views));
    }
    if (m_next_page_token_isSet) {
        obj.insert(QString("nextPageToken"), ::OpenAPI::toJsonValue(m_next_page_token));
    }
    return obj;
}

QList<OAIHotelView> OAIListHotelViewsResponse::getHotelViews() const {
    return m_hotel_views;
}
void OAIListHotelViewsResponse::setHotelViews(const QList<OAIHotelView> &hotel_views) {
    m_hotel_views = hotel_views;
    m_hotel_views_isSet = true;
}

bool OAIListHotelViewsResponse::is_hotel_views_Set() const{
    return m_hotel_views_isSet;
}

bool OAIListHotelViewsResponse::is_hotel_views_Valid() const{
    return m_hotel_views_isValid;
}

QString OAIListHotelViewsResponse::getNextPageToken() const {
    return m_next_page_token;
}
void OAIListHotelViewsResponse::setNextPageToken(const QString &next_page_token) {
    m_next_page_token = next_page_token;
    m_next_page_token_isSet = true;
}

bool OAIListHotelViewsResponse::is_next_page_token_Set() const{
    return m_next_page_token_isSet;
}

bool OAIListHotelViewsResponse::is_next_page_token_Valid() const{
    return m_next_page_token_isValid;
}

bool OAIListHotelViewsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_hotel_views.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_page_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListHotelViewsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
