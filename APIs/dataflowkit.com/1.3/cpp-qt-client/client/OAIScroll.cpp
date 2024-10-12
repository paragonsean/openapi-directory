/**
 * Dataflow Kit Web Scraper
 * Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the `api_key` query parameter.  
 *
 * The version of the OpenAPI document: 1.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIScroll.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIScroll::OAIScroll(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIScroll::OAIScroll() {
    this->initializeModel();
}

OAIScroll::~OAIScroll() {}

void OAIScroll::initializeModel() {

    m_scroll_by_pixels_isSet = false;
    m_scroll_by_pixels_isValid = false;

    m_scrolling_element_selector_isSet = false;
    m_scrolling_element_selector_isValid = false;

    m_selector_isSet = false;
    m_selector_isValid = false;

    m_times_isSet = false;
    m_times_isValid = false;
}

void OAIScroll::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIScroll::fromJsonObject(QJsonObject json) {

    m_scroll_by_pixels_isValid = ::OpenAPI::fromJsonValue(m_scroll_by_pixels, json[QString("scrollByPixels")]);
    m_scroll_by_pixels_isSet = !json[QString("scrollByPixels")].isNull() && m_scroll_by_pixels_isValid;

    m_scrolling_element_selector_isValid = ::OpenAPI::fromJsonValue(m_scrolling_element_selector, json[QString("scrollingElementSelector")]);
    m_scrolling_element_selector_isSet = !json[QString("scrollingElementSelector")].isNull() && m_scrolling_element_selector_isValid;

    m_selector_isValid = ::OpenAPI::fromJsonValue(m_selector, json[QString("selector")]);
    m_selector_isSet = !json[QString("selector")].isNull() && m_selector_isValid;

    m_times_isValid = ::OpenAPI::fromJsonValue(m_times, json[QString("times")]);
    m_times_isSet = !json[QString("times")].isNull() && m_times_isValid;
}

QString OAIScroll::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIScroll::asJsonObject() const {
    QJsonObject obj;
    if (m_scroll_by_pixels_isSet) {
        obj.insert(QString("scrollByPixels"), ::OpenAPI::toJsonValue(m_scroll_by_pixels));
    }
    if (m_scrolling_element_selector_isSet) {
        obj.insert(QString("scrollingElementSelector"), ::OpenAPI::toJsonValue(m_scrolling_element_selector));
    }
    if (m_selector_isSet) {
        obj.insert(QString("selector"), ::OpenAPI::toJsonValue(m_selector));
    }
    if (m_times_isSet) {
        obj.insert(QString("times"), ::OpenAPI::toJsonValue(m_times));
    }
    return obj;
}

double OAIScroll::getScrollByPixels() const {
    return m_scroll_by_pixels;
}
void OAIScroll::setScrollByPixels(const double &scroll_by_pixels) {
    m_scroll_by_pixels = scroll_by_pixels;
    m_scroll_by_pixels_isSet = true;
}

bool OAIScroll::is_scroll_by_pixels_Set() const{
    return m_scroll_by_pixels_isSet;
}

bool OAIScroll::is_scroll_by_pixels_Valid() const{
    return m_scroll_by_pixels_isValid;
}

QString OAIScroll::getScrollingElementSelector() const {
    return m_scrolling_element_selector;
}
void OAIScroll::setScrollingElementSelector(const QString &scrolling_element_selector) {
    m_scrolling_element_selector = scrolling_element_selector;
    m_scrolling_element_selector_isSet = true;
}

bool OAIScroll::is_scrolling_element_selector_Set() const{
    return m_scrolling_element_selector_isSet;
}

bool OAIScroll::is_scrolling_element_selector_Valid() const{
    return m_scrolling_element_selector_isValid;
}

QString OAIScroll::getSelector() const {
    return m_selector;
}
void OAIScroll::setSelector(const QString &selector) {
    m_selector = selector;
    m_selector_isSet = true;
}

bool OAIScroll::is_selector_Set() const{
    return m_selector_isSet;
}

bool OAIScroll::is_selector_Valid() const{
    return m_selector_isValid;
}

qint32 OAIScroll::getTimes() const {
    return m_times;
}
void OAIScroll::setTimes(const qint32 &times) {
    m_times = times;
    m_times_isSet = true;
}

bool OAIScroll::is_times_Set() const{
    return m_times_isSet;
}

bool OAIScroll::is_times_Valid() const{
    return m_times_isValid;
}

bool OAIScroll::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_scroll_by_pixels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scrolling_element_selector_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_selector_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_times_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIScroll::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
