/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIChart_Axes_Details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIChart_Axes_Details::OAIChart_Axes_Details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIChart_Axes_Details::OAIChart_Axes_Details() {
    this->initializeModel();
}

OAIChart_Axes_Details::~OAIChart_Axes_Details() {}

void OAIChart_Axes_Details::initializeModel() {

    m_axis_data_type_id_isSet = false;
    m_axis_data_type_id_isValid = false;

    m_chart_isSet = false;
    m_chart_isValid = false;

    m_charts_id_isSet = false;
    m_charts_id_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_modified_isSet = false;
    m_date_modified_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_ooxml_id_isSet = false;
    m_ooxml_id_isValid = false;

    m_title_text_container_isSet = false;
    m_title_text_container_isValid = false;

    m_user_created_isSet = false;
    m_user_created_isValid = false;

    m_user_modified_isSet = false;
    m_user_modified_isValid = false;
}

void OAIChart_Axes_Details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIChart_Axes_Details::fromJsonObject(QJsonObject json) {

    m_axis_data_type_id_isValid = ::OpenAPI::fromJsonValue(m_axis_data_type_id, json[QString("axisDataTypeId")]);
    m_axis_data_type_id_isSet = !json[QString("axisDataTypeId")].isNull() && m_axis_data_type_id_isValid;

    m_chart_isValid = ::OpenAPI::fromJsonValue(m_chart, json[QString("chart")]);
    m_chart_isSet = !json[QString("chart")].isNull() && m_chart_isValid;

    m_charts_id_isValid = ::OpenAPI::fromJsonValue(m_charts_id, json[QString("chartsId")]);
    m_charts_id_isSet = !json[QString("chartsId")].isNull() && m_charts_id_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("dateCreated")]);
    m_date_created_isSet = !json[QString("dateCreated")].isNull() && m_date_created_isValid;

    m_date_modified_isValid = ::OpenAPI::fromJsonValue(m_date_modified, json[QString("dateModified")]);
    m_date_modified_isSet = !json[QString("dateModified")].isNull() && m_date_modified_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_ooxml_id_isValid = ::OpenAPI::fromJsonValue(m_ooxml_id, json[QString("ooxmlId")]);
    m_ooxml_id_isSet = !json[QString("ooxmlId")].isNull() && m_ooxml_id_isValid;

    m_title_text_container_isValid = ::OpenAPI::fromJsonValue(m_title_text_container, json[QString("titleTextContainer")]);
    m_title_text_container_isSet = !json[QString("titleTextContainer")].isNull() && m_title_text_container_isValid;

    m_user_created_isValid = ::OpenAPI::fromJsonValue(m_user_created, json[QString("userCreated")]);
    m_user_created_isSet = !json[QString("userCreated")].isNull() && m_user_created_isValid;

    m_user_modified_isValid = ::OpenAPI::fromJsonValue(m_user_modified, json[QString("userModified")]);
    m_user_modified_isSet = !json[QString("userModified")].isNull() && m_user_modified_isValid;
}

QString OAIChart_Axes_Details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIChart_Axes_Details::asJsonObject() const {
    QJsonObject obj;
    if (m_axis_data_type_id_isSet) {
        obj.insert(QString("axisDataTypeId"), ::OpenAPI::toJsonValue(m_axis_data_type_id));
    }
    if (m_chart.isSet()) {
        obj.insert(QString("chart"), ::OpenAPI::toJsonValue(m_chart));
    }
    if (m_charts_id_isSet) {
        obj.insert(QString("chartsId"), ::OpenAPI::toJsonValue(m_charts_id));
    }
    if (m_date_created_isSet) {
        obj.insert(QString("dateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_date_modified_isSet) {
        obj.insert(QString("dateModified"), ::OpenAPI::toJsonValue(m_date_modified));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_ooxml_id_isSet) {
        obj.insert(QString("ooxmlId"), ::OpenAPI::toJsonValue(m_ooxml_id));
    }
    if (m_title_text_container.isSet()) {
        obj.insert(QString("titleTextContainer"), ::OpenAPI::toJsonValue(m_title_text_container));
    }
    if (m_user_created_isSet) {
        obj.insert(QString("userCreated"), ::OpenAPI::toJsonValue(m_user_created));
    }
    if (m_user_modified_isSet) {
        obj.insert(QString("userModified"), ::OpenAPI::toJsonValue(m_user_modified));
    }
    return obj;
}

qint32 OAIChart_Axes_Details::getAxisDataTypeId() const {
    return m_axis_data_type_id;
}
void OAIChart_Axes_Details::setAxisDataTypeId(const qint32 &axis_data_type_id) {
    m_axis_data_type_id = axis_data_type_id;
    m_axis_data_type_id_isSet = true;
}

bool OAIChart_Axes_Details::is_axis_data_type_id_Set() const{
    return m_axis_data_type_id_isSet;
}

bool OAIChart_Axes_Details::is_axis_data_type_id_Valid() const{
    return m_axis_data_type_id_isValid;
}

OAIChart_Charts_Details OAIChart_Axes_Details::getChart() const {
    return m_chart;
}
void OAIChart_Axes_Details::setChart(const OAIChart_Charts_Details &chart) {
    m_chart = chart;
    m_chart_isSet = true;
}

bool OAIChart_Axes_Details::is_chart_Set() const{
    return m_chart_isSet;
}

bool OAIChart_Axes_Details::is_chart_Valid() const{
    return m_chart_isValid;
}

QString OAIChart_Axes_Details::getChartsId() const {
    return m_charts_id;
}
void OAIChart_Axes_Details::setChartsId(const QString &charts_id) {
    m_charts_id = charts_id;
    m_charts_id_isSet = true;
}

bool OAIChart_Axes_Details::is_charts_id_Set() const{
    return m_charts_id_isSet;
}

bool OAIChart_Axes_Details::is_charts_id_Valid() const{
    return m_charts_id_isValid;
}

QDateTime OAIChart_Axes_Details::getDateCreated() const {
    return m_date_created;
}
void OAIChart_Axes_Details::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAIChart_Axes_Details::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAIChart_Axes_Details::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAIChart_Axes_Details::getDateModified() const {
    return m_date_modified;
}
void OAIChart_Axes_Details::setDateModified(const QDateTime &date_modified) {
    m_date_modified = date_modified;
    m_date_modified_isSet = true;
}

bool OAIChart_Axes_Details::is_date_modified_Set() const{
    return m_date_modified_isSet;
}

bool OAIChart_Axes_Details::is_date_modified_Valid() const{
    return m_date_modified_isValid;
}

QString OAIChart_Axes_Details::getId() const {
    return m_id;
}
void OAIChart_Axes_Details::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIChart_Axes_Details::is_id_Set() const{
    return m_id_isSet;
}

bool OAIChart_Axes_Details::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIChart_Axes_Details::getOoxmlId() const {
    return m_ooxml_id;
}
void OAIChart_Axes_Details::setOoxmlId(const qint32 &ooxml_id) {
    m_ooxml_id = ooxml_id;
    m_ooxml_id_isSet = true;
}

bool OAIChart_Axes_Details::is_ooxml_id_Set() const{
    return m_ooxml_id_isSet;
}

bool OAIChart_Axes_Details::is_ooxml_id_Valid() const{
    return m_ooxml_id_isValid;
}

OAIShared_TextContainer_Details OAIChart_Axes_Details::getTitleTextContainer() const {
    return m_title_text_container;
}
void OAIChart_Axes_Details::setTitleTextContainer(const OAIShared_TextContainer_Details &title_text_container) {
    m_title_text_container = title_text_container;
    m_title_text_container_isSet = true;
}

bool OAIChart_Axes_Details::is_title_text_container_Set() const{
    return m_title_text_container_isSet;
}

bool OAIChart_Axes_Details::is_title_text_container_Valid() const{
    return m_title_text_container_isValid;
}

QString OAIChart_Axes_Details::getUserCreated() const {
    return m_user_created;
}
void OAIChart_Axes_Details::setUserCreated(const QString &user_created) {
    m_user_created = user_created;
    m_user_created_isSet = true;
}

bool OAIChart_Axes_Details::is_user_created_Set() const{
    return m_user_created_isSet;
}

bool OAIChart_Axes_Details::is_user_created_Valid() const{
    return m_user_created_isValid;
}

QString OAIChart_Axes_Details::getUserModified() const {
    return m_user_modified;
}
void OAIChart_Axes_Details::setUserModified(const QString &user_modified) {
    m_user_modified = user_modified;
    m_user_modified_isSet = true;
}

bool OAIChart_Axes_Details::is_user_modified_Set() const{
    return m_user_modified_isSet;
}

bool OAIChart_Axes_Details::is_user_modified_Valid() const{
    return m_user_modified_isValid;
}

bool OAIChart_Axes_Details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_axis_data_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_chart.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_charts_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ooxml_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_text_container.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_modified_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIChart_Axes_Details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
