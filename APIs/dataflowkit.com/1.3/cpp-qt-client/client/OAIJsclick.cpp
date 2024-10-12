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

#include "OAIJsclick.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIJsclick::OAIJsclick(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIJsclick::OAIJsclick() {
    this->initializeModel();
}

OAIJsclick::~OAIJsclick() {}

void OAIJsclick::initializeModel() {

    m_ignore_if_not_present_isSet = false;
    m_ignore_if_not_present_isValid = false;

    m_selector_isSet = false;
    m_selector_isValid = false;

    m_skip_last_iteration_isSet = false;
    m_skip_last_iteration_isValid = false;
}

void OAIJsclick::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIJsclick::fromJsonObject(QJsonObject json) {

    m_ignore_if_not_present_isValid = ::OpenAPI::fromJsonValue(m_ignore_if_not_present, json[QString("ignoreIfNotPresent")]);
    m_ignore_if_not_present_isSet = !json[QString("ignoreIfNotPresent")].isNull() && m_ignore_if_not_present_isValid;

    m_selector_isValid = ::OpenAPI::fromJsonValue(m_selector, json[QString("selector")]);
    m_selector_isSet = !json[QString("selector")].isNull() && m_selector_isValid;

    m_skip_last_iteration_isValid = ::OpenAPI::fromJsonValue(m_skip_last_iteration, json[QString("skipLastIteration")]);
    m_skip_last_iteration_isSet = !json[QString("skipLastIteration")].isNull() && m_skip_last_iteration_isValid;
}

QString OAIJsclick::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIJsclick::asJsonObject() const {
    QJsonObject obj;
    if (m_ignore_if_not_present_isSet) {
        obj.insert(QString("ignoreIfNotPresent"), ::OpenAPI::toJsonValue(m_ignore_if_not_present));
    }
    if (m_selector_isSet) {
        obj.insert(QString("selector"), ::OpenAPI::toJsonValue(m_selector));
    }
    if (m_skip_last_iteration_isSet) {
        obj.insert(QString("skipLastIteration"), ::OpenAPI::toJsonValue(m_skip_last_iteration));
    }
    return obj;
}

bool OAIJsclick::isIgnoreIfNotPresent() const {
    return m_ignore_if_not_present;
}
void OAIJsclick::setIgnoreIfNotPresent(const bool &ignore_if_not_present) {
    m_ignore_if_not_present = ignore_if_not_present;
    m_ignore_if_not_present_isSet = true;
}

bool OAIJsclick::is_ignore_if_not_present_Set() const{
    return m_ignore_if_not_present_isSet;
}

bool OAIJsclick::is_ignore_if_not_present_Valid() const{
    return m_ignore_if_not_present_isValid;
}

QString OAIJsclick::getSelector() const {
    return m_selector;
}
void OAIJsclick::setSelector(const QString &selector) {
    m_selector = selector;
    m_selector_isSet = true;
}

bool OAIJsclick::is_selector_Set() const{
    return m_selector_isSet;
}

bool OAIJsclick::is_selector_Valid() const{
    return m_selector_isValid;
}

bool OAIJsclick::isSkipLastIteration() const {
    return m_skip_last_iteration;
}
void OAIJsclick::setSkipLastIteration(const bool &skip_last_iteration) {
    m_skip_last_iteration = skip_last_iteration;
    m_skip_last_iteration_isSet = true;
}

bool OAIJsclick::is_skip_last_iteration_Set() const{
    return m_skip_last_iteration_isSet;
}

bool OAIJsclick::is_skip_last_iteration_Valid() const{
    return m_skip_last_iteration_isValid;
}

bool OAIJsclick::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ignore_if_not_present_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_selector_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_skip_last_iteration_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIJsclick::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
