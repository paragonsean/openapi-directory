/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPanel_yAxis.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPanel_yAxis::OAIPanel_yAxis(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPanel_yAxis::OAIPanel_yAxis() {
    this->initializeModel();
}

OAIPanel_yAxis::~OAIPanel_yAxis() {}

void OAIPanel_yAxis::initializeModel() {

    m_decimals_isSet = false;
    m_decimals_isValid = false;

    m_format_isSet = false;
    m_format_isValid = false;

    m_log_base_isSet = false;
    m_log_base_isValid = false;

    m_max_isSet = false;
    m_max_isValid = false;

    m_min_isSet = false;
    m_min_isValid = false;

    m_show_isSet = false;
    m_show_isValid = false;

    m_split_factor_isSet = false;
    m_split_factor_isValid = false;
}

void OAIPanel_yAxis::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPanel_yAxis::fromJsonObject(QJsonObject json) {

    m_decimals_isValid = ::OpenAPI::fromJsonValue(m_decimals, json[QString("decimals")]);
    m_decimals_isSet = !json[QString("decimals")].isNull() && m_decimals_isValid;

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;

    m_log_base_isValid = ::OpenAPI::fromJsonValue(m_log_base, json[QString("logBase")]);
    m_log_base_isSet = !json[QString("logBase")].isNull() && m_log_base_isValid;

    m_max_isValid = ::OpenAPI::fromJsonValue(m_max, json[QString("max")]);
    m_max_isSet = !json[QString("max")].isNull() && m_max_isValid;

    m_min_isValid = ::OpenAPI::fromJsonValue(m_min, json[QString("min")]);
    m_min_isSet = !json[QString("min")].isNull() && m_min_isValid;

    m_show_isValid = ::OpenAPI::fromJsonValue(m_show, json[QString("show")]);
    m_show_isSet = !json[QString("show")].isNull() && m_show_isValid;

    m_split_factor_isValid = ::OpenAPI::fromJsonValue(m_split_factor, json[QString("splitFactor")]);
    m_split_factor_isSet = !json[QString("splitFactor")].isNull() && m_split_factor_isValid;
}

QString OAIPanel_yAxis::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPanel_yAxis::asJsonObject() const {
    QJsonObject obj;
    if (m_decimals_isSet) {
        obj.insert(QString("decimals"), ::OpenAPI::toJsonValue(m_decimals));
    }
    if (m_format_isSet) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_log_base_isSet) {
        obj.insert(QString("logBase"), ::OpenAPI::toJsonValue(m_log_base));
    }
    if (m_max_isSet) {
        obj.insert(QString("max"), ::OpenAPI::toJsonValue(m_max));
    }
    if (m_min_isSet) {
        obj.insert(QString("min"), ::OpenAPI::toJsonValue(m_min));
    }
    if (m_show_isSet) {
        obj.insert(QString("show"), ::OpenAPI::toJsonValue(m_show));
    }
    if (m_split_factor_isSet) {
        obj.insert(QString("splitFactor"), ::OpenAPI::toJsonValue(m_split_factor));
    }
    return obj;
}

qint64 OAIPanel_yAxis::getDecimals() const {
    return m_decimals;
}
void OAIPanel_yAxis::setDecimals(const qint64 &decimals) {
    m_decimals = decimals;
    m_decimals_isSet = true;
}

bool OAIPanel_yAxis::is_decimals_Set() const{
    return m_decimals_isSet;
}

bool OAIPanel_yAxis::is_decimals_Valid() const{
    return m_decimals_isValid;
}

QString OAIPanel_yAxis::getFormat() const {
    return m_format;
}
void OAIPanel_yAxis::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAIPanel_yAxis::is_format_Set() const{
    return m_format_isSet;
}

bool OAIPanel_yAxis::is_format_Valid() const{
    return m_format_isValid;
}

qint64 OAIPanel_yAxis::getLogBase() const {
    return m_log_base;
}
void OAIPanel_yAxis::setLogBase(const qint64 &log_base) {
    m_log_base = log_base;
    m_log_base_isSet = true;
}

bool OAIPanel_yAxis::is_log_base_Set() const{
    return m_log_base_isSet;
}

bool OAIPanel_yAxis::is_log_base_Valid() const{
    return m_log_base_isValid;
}

QString OAIPanel_yAxis::getMax() const {
    return m_max;
}
void OAIPanel_yAxis::setMax(const QString &max) {
    m_max = max;
    m_max_isSet = true;
}

bool OAIPanel_yAxis::is_max_Set() const{
    return m_max_isSet;
}

bool OAIPanel_yAxis::is_max_Valid() const{
    return m_max_isValid;
}

QString OAIPanel_yAxis::getMin() const {
    return m_min;
}
void OAIPanel_yAxis::setMin(const QString &min) {
    m_min = min;
    m_min_isSet = true;
}

bool OAIPanel_yAxis::is_min_Set() const{
    return m_min_isSet;
}

bool OAIPanel_yAxis::is_min_Valid() const{
    return m_min_isValid;
}

bool OAIPanel_yAxis::isShow() const {
    return m_show;
}
void OAIPanel_yAxis::setShow(const bool &show) {
    m_show = show;
    m_show_isSet = true;
}

bool OAIPanel_yAxis::is_show_Set() const{
    return m_show_isSet;
}

bool OAIPanel_yAxis::is_show_Valid() const{
    return m_show_isValid;
}

double OAIPanel_yAxis::getSplitFactor() const {
    return m_split_factor;
}
void OAIPanel_yAxis::setSplitFactor(const double &split_factor) {
    m_split_factor = split_factor;
    m_split_factor_isSet = true;
}

bool OAIPanel_yAxis::is_split_factor_Set() const{
    return m_split_factor_isSet;
}

bool OAIPanel_yAxis::is_split_factor_Valid() const{
    return m_split_factor_isValid;
}

bool OAIPanel_yAxis::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_decimals_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_log_base_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_split_factor_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPanel_yAxis::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
