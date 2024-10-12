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

#include "OAIChart_RowCollections.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIChart_RowCollections::OAIChart_RowCollections(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIChart_RowCollections::OAIChart_RowCollections() {
    this->initializeModel();
}

OAIChart_RowCollections::~OAIChart_RowCollections() {}

void OAIChart_RowCollections::initializeModel() {

    m_axis_id_isSet = false;
    m_axis_id_isValid = false;

    m_chart_data_id_isSet = false;
    m_chart_data_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_format_type_isSet = false;
    m_name_format_type_isValid = false;
}

void OAIChart_RowCollections::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIChart_RowCollections::fromJsonObject(QJsonObject json) {

    m_axis_id_isValid = ::OpenAPI::fromJsonValue(m_axis_id, json[QString("axisId")]);
    m_axis_id_isSet = !json[QString("axisId")].isNull() && m_axis_id_isValid;

    m_chart_data_id_isValid = ::OpenAPI::fromJsonValue(m_chart_data_id, json[QString("chartDataId")]);
    m_chart_data_id_isSet = !json[QString("chartDataId")].isNull() && m_chart_data_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_format_type_isValid = ::OpenAPI::fromJsonValue(m_name_format_type, json[QString("nameFormatType")]);
    m_name_format_type_isSet = !json[QString("nameFormatType")].isNull() && m_name_format_type_isValid;
}

QString OAIChart_RowCollections::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIChart_RowCollections::asJsonObject() const {
    QJsonObject obj;
    if (m_axis_id_isSet) {
        obj.insert(QString("axisId"), ::OpenAPI::toJsonValue(m_axis_id));
    }
    if (m_chart_data_id_isSet) {
        obj.insert(QString("chartDataId"), ::OpenAPI::toJsonValue(m_chart_data_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_format_type_isSet) {
        obj.insert(QString("nameFormatType"), ::OpenAPI::toJsonValue(m_name_format_type));
    }
    return obj;
}

QString OAIChart_RowCollections::getAxisId() const {
    return m_axis_id;
}
void OAIChart_RowCollections::setAxisId(const QString &axis_id) {
    m_axis_id = axis_id;
    m_axis_id_isSet = true;
}

bool OAIChart_RowCollections::is_axis_id_Set() const{
    return m_axis_id_isSet;
}

bool OAIChart_RowCollections::is_axis_id_Valid() const{
    return m_axis_id_isValid;
}

QString OAIChart_RowCollections::getChartDataId() const {
    return m_chart_data_id;
}
void OAIChart_RowCollections::setChartDataId(const QString &chart_data_id) {
    m_chart_data_id = chart_data_id;
    m_chart_data_id_isSet = true;
}

bool OAIChart_RowCollections::is_chart_data_id_Set() const{
    return m_chart_data_id_isSet;
}

bool OAIChart_RowCollections::is_chart_data_id_Valid() const{
    return m_chart_data_id_isValid;
}

QString OAIChart_RowCollections::getId() const {
    return m_id;
}
void OAIChart_RowCollections::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIChart_RowCollections::is_id_Set() const{
    return m_id_isSet;
}

bool OAIChart_RowCollections::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIChart_RowCollections::getNameFormatType() const {
    return m_name_format_type;
}
void OAIChart_RowCollections::setNameFormatType(const qint32 &name_format_type) {
    m_name_format_type = name_format_type;
    m_name_format_type_isSet = true;
}

bool OAIChart_RowCollections::is_name_format_type_Set() const{
    return m_name_format_type_isSet;
}

bool OAIChart_RowCollections::is_name_format_type_Valid() const{
    return m_name_format_type_isValid;
}

bool OAIChart_RowCollections::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_axis_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_chart_data_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_format_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIChart_RowCollections::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
