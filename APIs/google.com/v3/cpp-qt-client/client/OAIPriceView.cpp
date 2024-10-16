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

#include "OAIPriceView.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPriceView::OAIPriceView(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPriceView::OAIPriceView() {
    this->initializeModel();
}

OAIPriceView::~OAIPriceView() {}

void OAIPriceView::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_per_itinerary_prices_isSet = false;
    m_per_itinerary_prices_isValid = false;
}

void OAIPriceView::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPriceView::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_per_itinerary_prices_isValid = ::OpenAPI::fromJsonValue(m_per_itinerary_prices, json[QString("perItineraryPrices")]);
    m_per_itinerary_prices_isSet = !json[QString("perItineraryPrices")].isNull() && m_per_itinerary_prices_isValid;
}

QString OAIPriceView::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPriceView::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_per_itinerary_prices.size() > 0) {
        obj.insert(QString("perItineraryPrices"), ::OpenAPI::toJsonValue(m_per_itinerary_prices));
    }
    return obj;
}

QString OAIPriceView::getName() const {
    return m_name;
}
void OAIPriceView::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPriceView::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPriceView::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIHotelPricePerItinerary> OAIPriceView::getPerItineraryPrices() const {
    return m_per_itinerary_prices;
}
void OAIPriceView::setPerItineraryPrices(const QList<OAIHotelPricePerItinerary> &per_itinerary_prices) {
    m_per_itinerary_prices = per_itinerary_prices;
    m_per_itinerary_prices_isSet = true;
}

bool OAIPriceView::is_per_itinerary_prices_Set() const{
    return m_per_itinerary_prices_isSet;
}

bool OAIPriceView::is_per_itinerary_prices_Valid() const{
    return m_per_itinerary_prices_isValid;
}

bool OAIPriceView::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_per_itinerary_prices.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPriceView::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
