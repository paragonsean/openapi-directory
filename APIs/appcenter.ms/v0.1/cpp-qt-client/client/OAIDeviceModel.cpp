/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDeviceModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDeviceModel::OAIDeviceModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDeviceModel::OAIDeviceModel() {
    this->initializeModel();
}

OAIDeviceModel::~OAIDeviceModel() {}

void OAIDeviceModel::initializeModel() {

    m_availability_count_isSet = false;
    m_availability_count_isValid = false;

    m_cpu_isSet = false;
    m_cpu_isValid = false;

    m_device_frame_isSet = false;
    m_device_frame_isValid = false;

    m_dimensions_isSet = false;
    m_dimensions_isValid = false;

    m_form_factor_isSet = false;
    m_form_factor_isValid = false;

    m_manufacturer_isSet = false;
    m_manufacturer_isValid = false;

    m_memory_isSet = false;
    m_memory_isValid = false;

    m_model_isSet = false;
    m_model_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_platform_isSet = false;
    m_platform_isValid = false;

    m_release_date_isSet = false;
    m_release_date_isValid = false;

    m_resolution_isSet = false;
    m_resolution_isValid = false;

    m_screen_rotation_isSet = false;
    m_screen_rotation_isValid = false;

    m_screen_size_isSet = false;
    m_screen_size_isValid = false;
}

void OAIDeviceModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDeviceModel::fromJsonObject(QJsonObject json) {

    m_availability_count_isValid = ::OpenAPI::fromJsonValue(m_availability_count, json[QString("availabilityCount")]);
    m_availability_count_isSet = !json[QString("availabilityCount")].isNull() && m_availability_count_isValid;

    m_cpu_isValid = ::OpenAPI::fromJsonValue(m_cpu, json[QString("cpu")]);
    m_cpu_isSet = !json[QString("cpu")].isNull() && m_cpu_isValid;

    m_device_frame_isValid = ::OpenAPI::fromJsonValue(m_device_frame, json[QString("deviceFrame")]);
    m_device_frame_isSet = !json[QString("deviceFrame")].isNull() && m_device_frame_isValid;

    m_dimensions_isValid = ::OpenAPI::fromJsonValue(m_dimensions, json[QString("dimensions")]);
    m_dimensions_isSet = !json[QString("dimensions")].isNull() && m_dimensions_isValid;

    m_form_factor_isValid = ::OpenAPI::fromJsonValue(m_form_factor, json[QString("formFactor")]);
    m_form_factor_isSet = !json[QString("formFactor")].isNull() && m_form_factor_isValid;

    m_manufacturer_isValid = ::OpenAPI::fromJsonValue(m_manufacturer, json[QString("manufacturer")]);
    m_manufacturer_isSet = !json[QString("manufacturer")].isNull() && m_manufacturer_isValid;

    m_memory_isValid = ::OpenAPI::fromJsonValue(m_memory, json[QString("memory")]);
    m_memory_isSet = !json[QString("memory")].isNull() && m_memory_isValid;

    m_model_isValid = ::OpenAPI::fromJsonValue(m_model, json[QString("model")]);
    m_model_isSet = !json[QString("model")].isNull() && m_model_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_platform_isValid = ::OpenAPI::fromJsonValue(m_platform, json[QString("platform")]);
    m_platform_isSet = !json[QString("platform")].isNull() && m_platform_isValid;

    m_release_date_isValid = ::OpenAPI::fromJsonValue(m_release_date, json[QString("releaseDate")]);
    m_release_date_isSet = !json[QString("releaseDate")].isNull() && m_release_date_isValid;

    m_resolution_isValid = ::OpenAPI::fromJsonValue(m_resolution, json[QString("resolution")]);
    m_resolution_isSet = !json[QString("resolution")].isNull() && m_resolution_isValid;

    m_screen_rotation_isValid = ::OpenAPI::fromJsonValue(m_screen_rotation, json[QString("screenRotation")]);
    m_screen_rotation_isSet = !json[QString("screenRotation")].isNull() && m_screen_rotation_isValid;

    m_screen_size_isValid = ::OpenAPI::fromJsonValue(m_screen_size, json[QString("screenSize")]);
    m_screen_size_isSet = !json[QString("screenSize")].isNull() && m_screen_size_isValid;
}

QString OAIDeviceModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDeviceModel::asJsonObject() const {
    QJsonObject obj;
    if (m_availability_count_isSet) {
        obj.insert(QString("availabilityCount"), ::OpenAPI::toJsonValue(m_availability_count));
    }
    if (m_cpu.isSet()) {
        obj.insert(QString("cpu"), ::OpenAPI::toJsonValue(m_cpu));
    }
    if (m_device_frame.isSet()) {
        obj.insert(QString("deviceFrame"), ::OpenAPI::toJsonValue(m_device_frame));
    }
    if (m_dimensions.isSet()) {
        obj.insert(QString("dimensions"), ::OpenAPI::toJsonValue(m_dimensions));
    }
    if (m_form_factor_isSet) {
        obj.insert(QString("formFactor"), ::OpenAPI::toJsonValue(m_form_factor));
    }
    if (m_manufacturer_isSet) {
        obj.insert(QString("manufacturer"), ::OpenAPI::toJsonValue(m_manufacturer));
    }
    if (m_memory.isSet()) {
        obj.insert(QString("memory"), ::OpenAPI::toJsonValue(m_memory));
    }
    if (m_model_isSet) {
        obj.insert(QString("model"), ::OpenAPI::toJsonValue(m_model));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_platform_isSet) {
        obj.insert(QString("platform"), ::OpenAPI::toJsonValue(m_platform));
    }
    if (m_release_date_isSet) {
        obj.insert(QString("releaseDate"), ::OpenAPI::toJsonValue(m_release_date));
    }
    if (m_resolution.isSet()) {
        obj.insert(QString("resolution"), ::OpenAPI::toJsonValue(m_resolution));
    }
    if (m_screen_rotation_isSet) {
        obj.insert(QString("screenRotation"), ::OpenAPI::toJsonValue(m_screen_rotation));
    }
    if (m_screen_size.isSet()) {
        obj.insert(QString("screenSize"), ::OpenAPI::toJsonValue(m_screen_size));
    }
    return obj;
}

double OAIDeviceModel::getAvailabilityCount() const {
    return m_availability_count;
}
void OAIDeviceModel::setAvailabilityCount(const double &availability_count) {
    m_availability_count = availability_count;
    m_availability_count_isSet = true;
}

bool OAIDeviceModel::is_availability_count_Set() const{
    return m_availability_count_isSet;
}

bool OAIDeviceModel::is_availability_count_Valid() const{
    return m_availability_count_isValid;
}

OAITest_getDeviceConfigurations_200_response_inner_model_cpu OAIDeviceModel::getCpu() const {
    return m_cpu;
}
void OAIDeviceModel::setCpu(const OAITest_getDeviceConfigurations_200_response_inner_model_cpu &cpu) {
    m_cpu = cpu;
    m_cpu_isSet = true;
}

bool OAIDeviceModel::is_cpu_Set() const{
    return m_cpu_isSet;
}

bool OAIDeviceModel::is_cpu_Valid() const{
    return m_cpu_isValid;
}

OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame OAIDeviceModel::getDeviceFrame() const {
    return m_device_frame;
}
void OAIDeviceModel::setDeviceFrame(const OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame &device_frame) {
    m_device_frame = device_frame;
    m_device_frame_isSet = true;
}

bool OAIDeviceModel::is_device_frame_Set() const{
    return m_device_frame_isSet;
}

bool OAIDeviceModel::is_device_frame_Valid() const{
    return m_device_frame_isValid;
}

OAITest_getDeviceConfigurations_200_response_inner_model_dimensions OAIDeviceModel::getDimensions() const {
    return m_dimensions;
}
void OAIDeviceModel::setDimensions(const OAITest_getDeviceConfigurations_200_response_inner_model_dimensions &dimensions) {
    m_dimensions = dimensions;
    m_dimensions_isSet = true;
}

bool OAIDeviceModel::is_dimensions_Set() const{
    return m_dimensions_isSet;
}

bool OAIDeviceModel::is_dimensions_Valid() const{
    return m_dimensions_isValid;
}

QString OAIDeviceModel::getFormFactor() const {
    return m_form_factor;
}
void OAIDeviceModel::setFormFactor(const QString &form_factor) {
    m_form_factor = form_factor;
    m_form_factor_isSet = true;
}

bool OAIDeviceModel::is_form_factor_Set() const{
    return m_form_factor_isSet;
}

bool OAIDeviceModel::is_form_factor_Valid() const{
    return m_form_factor_isValid;
}

QString OAIDeviceModel::getManufacturer() const {
    return m_manufacturer;
}
void OAIDeviceModel::setManufacturer(const QString &manufacturer) {
    m_manufacturer = manufacturer;
    m_manufacturer_isSet = true;
}

bool OAIDeviceModel::is_manufacturer_Set() const{
    return m_manufacturer_isSet;
}

bool OAIDeviceModel::is_manufacturer_Valid() const{
    return m_manufacturer_isValid;
}

OAITest_getDeviceConfigurations_200_response_inner_model_memory OAIDeviceModel::getMemory() const {
    return m_memory;
}
void OAIDeviceModel::setMemory(const OAITest_getDeviceConfigurations_200_response_inner_model_memory &memory) {
    m_memory = memory;
    m_memory_isSet = true;
}

bool OAIDeviceModel::is_memory_Set() const{
    return m_memory_isSet;
}

bool OAIDeviceModel::is_memory_Valid() const{
    return m_memory_isValid;
}

QString OAIDeviceModel::getModel() const {
    return m_model;
}
void OAIDeviceModel::setModel(const QString &model) {
    m_model = model;
    m_model_isSet = true;
}

bool OAIDeviceModel::is_model_Set() const{
    return m_model_isSet;
}

bool OAIDeviceModel::is_model_Valid() const{
    return m_model_isValid;
}

QString OAIDeviceModel::getName() const {
    return m_name;
}
void OAIDeviceModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDeviceModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDeviceModel::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIDeviceModel::getPlatform() const {
    return m_platform;
}
void OAIDeviceModel::setPlatform(const QString &platform) {
    m_platform = platform;
    m_platform_isSet = true;
}

bool OAIDeviceModel::is_platform_Set() const{
    return m_platform_isSet;
}

bool OAIDeviceModel::is_platform_Valid() const{
    return m_platform_isValid;
}

QString OAIDeviceModel::getReleaseDate() const {
    return m_release_date;
}
void OAIDeviceModel::setReleaseDate(const QString &release_date) {
    m_release_date = release_date;
    m_release_date_isSet = true;
}

bool OAIDeviceModel::is_release_date_Set() const{
    return m_release_date_isSet;
}

bool OAIDeviceModel::is_release_date_Valid() const{
    return m_release_date_isValid;
}

OAITest_getDeviceConfigurations_200_response_inner_model_resolution OAIDeviceModel::getResolution() const {
    return m_resolution;
}
void OAIDeviceModel::setResolution(const OAITest_getDeviceConfigurations_200_response_inner_model_resolution &resolution) {
    m_resolution = resolution;
    m_resolution_isSet = true;
}

bool OAIDeviceModel::is_resolution_Set() const{
    return m_resolution_isSet;
}

bool OAIDeviceModel::is_resolution_Valid() const{
    return m_resolution_isValid;
}

double OAIDeviceModel::getScreenRotation() const {
    return m_screen_rotation;
}
void OAIDeviceModel::setScreenRotation(const double &screen_rotation) {
    m_screen_rotation = screen_rotation;
    m_screen_rotation_isSet = true;
}

bool OAIDeviceModel::is_screen_rotation_Set() const{
    return m_screen_rotation_isSet;
}

bool OAIDeviceModel::is_screen_rotation_Valid() const{
    return m_screen_rotation_isValid;
}

OAITest_getDeviceConfigurations_200_response_inner_model_screenSize OAIDeviceModel::getScreenSize() const {
    return m_screen_size;
}
void OAIDeviceModel::setScreenSize(const OAITest_getDeviceConfigurations_200_response_inner_model_screenSize &screen_size) {
    m_screen_size = screen_size;
    m_screen_size_isSet = true;
}

bool OAIDeviceModel::is_screen_size_Set() const{
    return m_screen_size_isSet;
}

bool OAIDeviceModel::is_screen_size_Valid() const{
    return m_screen_size_isValid;
}

bool OAIDeviceModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_availability_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cpu.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_device_frame.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_dimensions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_factor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_manufacturer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_memory.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_platform_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resolution.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_screen_rotation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_screen_size.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDeviceModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
