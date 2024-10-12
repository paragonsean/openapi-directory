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

#include "OAIUrl2pdfrequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUrl2pdfrequest::OAIUrl2pdfrequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUrl2pdfrequest::OAIUrl2pdfrequest() {
    this->initializeModel();
}

OAIUrl2pdfrequest::~OAIUrl2pdfrequest() {}

void OAIUrl2pdfrequest::initializeModel() {

    m_actions_isSet = false;
    m_actions_isValid = false;

    m_ignore_http_status_err_codes_isSet = false;
    m_ignore_http_status_err_codes_isValid = false;

    m_initial_cookies_isSet = false;
    m_initial_cookies_isValid = false;

    m_landscape_isSet = false;
    m_landscape_isValid = false;

    m_margin_bottom_isSet = false;
    m_margin_bottom_isValid = false;

    m_margin_left_isSet = false;
    m_margin_left_isValid = false;

    m_margin_right_isSet = false;
    m_margin_right_isValid = false;

    m_margin_top_isSet = false;
    m_margin_top_isValid = false;

    m_output_isSet = false;
    m_output_isValid = false;

    m_page_ranges_isSet = false;
    m_page_ranges_isValid = false;

    m_paper_size_isSet = false;
    m_paper_size_isValid = false;

    m_print_background_isSet = false;
    m_print_background_isValid = false;

    m_print_header_footer_isSet = false;
    m_print_header_footer_isValid = false;

    m_proxy_isSet = false;
    m_proxy_isValid = false;

    m_scale_isSet = false;
    m_scale_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_wait_delay_isSet = false;
    m_wait_delay_isValid = false;
}

void OAIUrl2pdfrequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUrl2pdfrequest::fromJsonObject(QJsonObject json) {

    m_actions_isValid = ::OpenAPI::fromJsonValue(m_actions, json[QString("actions")]);
    m_actions_isSet = !json[QString("actions")].isNull() && m_actions_isValid;

    m_ignore_http_status_err_codes_isValid = ::OpenAPI::fromJsonValue(m_ignore_http_status_err_codes, json[QString("ignoreHTTPStatusErrCodes")]);
    m_ignore_http_status_err_codes_isSet = !json[QString("ignoreHTTPStatusErrCodes")].isNull() && m_ignore_http_status_err_codes_isValid;

    m_initial_cookies_isValid = ::OpenAPI::fromJsonValue(m_initial_cookies, json[QString("initialCookies")]);
    m_initial_cookies_isSet = !json[QString("initialCookies")].isNull() && m_initial_cookies_isValid;

    m_landscape_isValid = ::OpenAPI::fromJsonValue(m_landscape, json[QString("landscape")]);
    m_landscape_isSet = !json[QString("landscape")].isNull() && m_landscape_isValid;

    m_margin_bottom_isValid = ::OpenAPI::fromJsonValue(m_margin_bottom, json[QString("marginBottom")]);
    m_margin_bottom_isSet = !json[QString("marginBottom")].isNull() && m_margin_bottom_isValid;

    m_margin_left_isValid = ::OpenAPI::fromJsonValue(m_margin_left, json[QString("marginLeft")]);
    m_margin_left_isSet = !json[QString("marginLeft")].isNull() && m_margin_left_isValid;

    m_margin_right_isValid = ::OpenAPI::fromJsonValue(m_margin_right, json[QString("marginRight")]);
    m_margin_right_isSet = !json[QString("marginRight")].isNull() && m_margin_right_isValid;

    m_margin_top_isValid = ::OpenAPI::fromJsonValue(m_margin_top, json[QString("marginTop")]);
    m_margin_top_isSet = !json[QString("marginTop")].isNull() && m_margin_top_isValid;

    m_output_isValid = ::OpenAPI::fromJsonValue(m_output, json[QString("output")]);
    m_output_isSet = !json[QString("output")].isNull() && m_output_isValid;

    m_page_ranges_isValid = ::OpenAPI::fromJsonValue(m_page_ranges, json[QString("pageRanges")]);
    m_page_ranges_isSet = !json[QString("pageRanges")].isNull() && m_page_ranges_isValid;

    m_paper_size_isValid = ::OpenAPI::fromJsonValue(m_paper_size, json[QString("paperSize")]);
    m_paper_size_isSet = !json[QString("paperSize")].isNull() && m_paper_size_isValid;

    m_print_background_isValid = ::OpenAPI::fromJsonValue(m_print_background, json[QString("printBackground")]);
    m_print_background_isSet = !json[QString("printBackground")].isNull() && m_print_background_isValid;

    m_print_header_footer_isValid = ::OpenAPI::fromJsonValue(m_print_header_footer, json[QString("printHeaderFooter")]);
    m_print_header_footer_isSet = !json[QString("printHeaderFooter")].isNull() && m_print_header_footer_isValid;

    m_proxy_isValid = ::OpenAPI::fromJsonValue(m_proxy, json[QString("proxy")]);
    m_proxy_isSet = !json[QString("proxy")].isNull() && m_proxy_isValid;

    m_scale_isValid = ::OpenAPI::fromJsonValue(m_scale, json[QString("scale")]);
    m_scale_isSet = !json[QString("scale")].isNull() && m_scale_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_wait_delay_isValid = ::OpenAPI::fromJsonValue(m_wait_delay, json[QString("waitDelay")]);
    m_wait_delay_isSet = !json[QString("waitDelay")].isNull() && m_wait_delay_isValid;
}

QString OAIUrl2pdfrequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUrl2pdfrequest::asJsonObject() const {
    QJsonObject obj;
    if (m_actions.size() > 0) {
        obj.insert(QString("actions"), ::OpenAPI::toJsonValue(m_actions));
    }
    if (m_ignore_http_status_err_codes_isSet) {
        obj.insert(QString("ignoreHTTPStatusErrCodes"), ::OpenAPI::toJsonValue(m_ignore_http_status_err_codes));
    }
    if (m_initial_cookies.size() > 0) {
        obj.insert(QString("initialCookies"), ::OpenAPI::toJsonValue(m_initial_cookies));
    }
    if (m_landscape_isSet) {
        obj.insert(QString("landscape"), ::OpenAPI::toJsonValue(m_landscape));
    }
    if (m_margin_bottom_isSet) {
        obj.insert(QString("marginBottom"), ::OpenAPI::toJsonValue(m_margin_bottom));
    }
    if (m_margin_left_isSet) {
        obj.insert(QString("marginLeft"), ::OpenAPI::toJsonValue(m_margin_left));
    }
    if (m_margin_right_isSet) {
        obj.insert(QString("marginRight"), ::OpenAPI::toJsonValue(m_margin_right));
    }
    if (m_margin_top_isSet) {
        obj.insert(QString("marginTop"), ::OpenAPI::toJsonValue(m_margin_top));
    }
    if (m_output_isSet) {
        obj.insert(QString("output"), ::OpenAPI::toJsonValue(m_output));
    }
    if (m_page_ranges_isSet) {
        obj.insert(QString("pageRanges"), ::OpenAPI::toJsonValue(m_page_ranges));
    }
    if (m_paper_size_isSet) {
        obj.insert(QString("paperSize"), ::OpenAPI::toJsonValue(m_paper_size));
    }
    if (m_print_background_isSet) {
        obj.insert(QString("printBackground"), ::OpenAPI::toJsonValue(m_print_background));
    }
    if (m_print_header_footer_isSet) {
        obj.insert(QString("printHeaderFooter"), ::OpenAPI::toJsonValue(m_print_header_footer));
    }
    if (m_proxy_isSet) {
        obj.insert(QString("proxy"), ::OpenAPI::toJsonValue(m_proxy));
    }
    if (m_scale_isSet) {
        obj.insert(QString("scale"), ::OpenAPI::toJsonValue(m_scale));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_wait_delay_isSet) {
        obj.insert(QString("waitDelay"), ::OpenAPI::toJsonValue(m_wait_delay));
    }
    return obj;
}

QList<OAIAction> OAIUrl2pdfrequest::getActions() const {
    return m_actions;
}
void OAIUrl2pdfrequest::setActions(const QList<OAIAction> &actions) {
    m_actions = actions;
    m_actions_isSet = true;
}

bool OAIUrl2pdfrequest::is_actions_Set() const{
    return m_actions_isSet;
}

bool OAIUrl2pdfrequest::is_actions_Valid() const{
    return m_actions_isValid;
}

bool OAIUrl2pdfrequest::isIgnoreHttpStatusErrCodes() const {
    return m_ignore_http_status_err_codes;
}
void OAIUrl2pdfrequest::setIgnoreHttpStatusErrCodes(const bool &ignore_http_status_err_codes) {
    m_ignore_http_status_err_codes = ignore_http_status_err_codes;
    m_ignore_http_status_err_codes_isSet = true;
}

bool OAIUrl2pdfrequest::is_ignore_http_status_err_codes_Set() const{
    return m_ignore_http_status_err_codes_isSet;
}

bool OAIUrl2pdfrequest::is_ignore_http_status_err_codes_Valid() const{
    return m_ignore_http_status_err_codes_isValid;
}

QList<OAIInitialCookie> OAIUrl2pdfrequest::getInitialCookies() const {
    return m_initial_cookies;
}
void OAIUrl2pdfrequest::setInitialCookies(const QList<OAIInitialCookie> &initial_cookies) {
    m_initial_cookies = initial_cookies;
    m_initial_cookies_isSet = true;
}

bool OAIUrl2pdfrequest::is_initial_cookies_Set() const{
    return m_initial_cookies_isSet;
}

bool OAIUrl2pdfrequest::is_initial_cookies_Valid() const{
    return m_initial_cookies_isValid;
}

bool OAIUrl2pdfrequest::isLandscape() const {
    return m_landscape;
}
void OAIUrl2pdfrequest::setLandscape(const bool &landscape) {
    m_landscape = landscape;
    m_landscape_isSet = true;
}

bool OAIUrl2pdfrequest::is_landscape_Set() const{
    return m_landscape_isSet;
}

bool OAIUrl2pdfrequest::is_landscape_Valid() const{
    return m_landscape_isValid;
}

double OAIUrl2pdfrequest::getMarginBottom() const {
    return m_margin_bottom;
}
void OAIUrl2pdfrequest::setMarginBottom(const double &margin_bottom) {
    m_margin_bottom = margin_bottom;
    m_margin_bottom_isSet = true;
}

bool OAIUrl2pdfrequest::is_margin_bottom_Set() const{
    return m_margin_bottom_isSet;
}

bool OAIUrl2pdfrequest::is_margin_bottom_Valid() const{
    return m_margin_bottom_isValid;
}

double OAIUrl2pdfrequest::getMarginLeft() const {
    return m_margin_left;
}
void OAIUrl2pdfrequest::setMarginLeft(const double &margin_left) {
    m_margin_left = margin_left;
    m_margin_left_isSet = true;
}

bool OAIUrl2pdfrequest::is_margin_left_Set() const{
    return m_margin_left_isSet;
}

bool OAIUrl2pdfrequest::is_margin_left_Valid() const{
    return m_margin_left_isValid;
}

double OAIUrl2pdfrequest::getMarginRight() const {
    return m_margin_right;
}
void OAIUrl2pdfrequest::setMarginRight(const double &margin_right) {
    m_margin_right = margin_right;
    m_margin_right_isSet = true;
}

bool OAIUrl2pdfrequest::is_margin_right_Set() const{
    return m_margin_right_isSet;
}

bool OAIUrl2pdfrequest::is_margin_right_Valid() const{
    return m_margin_right_isValid;
}

double OAIUrl2pdfrequest::getMarginTop() const {
    return m_margin_top;
}
void OAIUrl2pdfrequest::setMarginTop(const double &margin_top) {
    m_margin_top = margin_top;
    m_margin_top_isSet = true;
}

bool OAIUrl2pdfrequest::is_margin_top_Set() const{
    return m_margin_top_isSet;
}

bool OAIUrl2pdfrequest::is_margin_top_Valid() const{
    return m_margin_top_isValid;
}

QString OAIUrl2pdfrequest::getOutput() const {
    return m_output;
}
void OAIUrl2pdfrequest::setOutput(const QString &output) {
    m_output = output;
    m_output_isSet = true;
}

bool OAIUrl2pdfrequest::is_output_Set() const{
    return m_output_isSet;
}

bool OAIUrl2pdfrequest::is_output_Valid() const{
    return m_output_isValid;
}

QString OAIUrl2pdfrequest::getPageRanges() const {
    return m_page_ranges;
}
void OAIUrl2pdfrequest::setPageRanges(const QString &page_ranges) {
    m_page_ranges = page_ranges;
    m_page_ranges_isSet = true;
}

bool OAIUrl2pdfrequest::is_page_ranges_Set() const{
    return m_page_ranges_isSet;
}

bool OAIUrl2pdfrequest::is_page_ranges_Valid() const{
    return m_page_ranges_isValid;
}

QString OAIUrl2pdfrequest::getPaperSize() const {
    return m_paper_size;
}
void OAIUrl2pdfrequest::setPaperSize(const QString &paper_size) {
    m_paper_size = paper_size;
    m_paper_size_isSet = true;
}

bool OAIUrl2pdfrequest::is_paper_size_Set() const{
    return m_paper_size_isSet;
}

bool OAIUrl2pdfrequest::is_paper_size_Valid() const{
    return m_paper_size_isValid;
}

bool OAIUrl2pdfrequest::isPrintBackground() const {
    return m_print_background;
}
void OAIUrl2pdfrequest::setPrintBackground(const bool &print_background) {
    m_print_background = print_background;
    m_print_background_isSet = true;
}

bool OAIUrl2pdfrequest::is_print_background_Set() const{
    return m_print_background_isSet;
}

bool OAIUrl2pdfrequest::is_print_background_Valid() const{
    return m_print_background_isValid;
}

bool OAIUrl2pdfrequest::isPrintHeaderFooter() const {
    return m_print_header_footer;
}
void OAIUrl2pdfrequest::setPrintHeaderFooter(const bool &print_header_footer) {
    m_print_header_footer = print_header_footer;
    m_print_header_footer_isSet = true;
}

bool OAIUrl2pdfrequest::is_print_header_footer_Set() const{
    return m_print_header_footer_isSet;
}

bool OAIUrl2pdfrequest::is_print_header_footer_Valid() const{
    return m_print_header_footer_isValid;
}

QString OAIUrl2pdfrequest::getProxy() const {
    return m_proxy;
}
void OAIUrl2pdfrequest::setProxy(const QString &proxy) {
    m_proxy = proxy;
    m_proxy_isSet = true;
}

bool OAIUrl2pdfrequest::is_proxy_Set() const{
    return m_proxy_isSet;
}

bool OAIUrl2pdfrequest::is_proxy_Valid() const{
    return m_proxy_isValid;
}

double OAIUrl2pdfrequest::getScale() const {
    return m_scale;
}
void OAIUrl2pdfrequest::setScale(const double &scale) {
    m_scale = scale;
    m_scale_isSet = true;
}

bool OAIUrl2pdfrequest::is_scale_Set() const{
    return m_scale_isSet;
}

bool OAIUrl2pdfrequest::is_scale_Valid() const{
    return m_scale_isValid;
}

QString OAIUrl2pdfrequest::getUrl() const {
    return m_url;
}
void OAIUrl2pdfrequest::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIUrl2pdfrequest::is_url_Set() const{
    return m_url_isSet;
}

bool OAIUrl2pdfrequest::is_url_Valid() const{
    return m_url_isValid;
}

double OAIUrl2pdfrequest::getWaitDelay() const {
    return m_wait_delay;
}
void OAIUrl2pdfrequest::setWaitDelay(const double &wait_delay) {
    m_wait_delay = wait_delay;
    m_wait_delay_isSet = true;
}

bool OAIUrl2pdfrequest::is_wait_delay_Set() const{
    return m_wait_delay_isSet;
}

bool OAIUrl2pdfrequest::is_wait_delay_Valid() const{
    return m_wait_delay_isValid;
}

bool OAIUrl2pdfrequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_actions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_ignore_http_status_err_codes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_initial_cookies.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_landscape_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_margin_bottom_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_margin_left_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_margin_right_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_margin_top_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_output_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_ranges_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_paper_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_print_background_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_print_header_footer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_proxy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scale_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wait_delay_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUrl2pdfrequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_url_isValid && true;
}

} // namespace OpenAPI
