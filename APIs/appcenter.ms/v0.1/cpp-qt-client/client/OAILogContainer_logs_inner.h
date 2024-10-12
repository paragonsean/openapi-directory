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

/*
 * OAILogContainer_logs_inner.h
 *
 * 
 */

#ifndef OAILogContainer_logs_inner_H
#define OAILogContainer_logs_inner_H

#include <QJsonObject>

#include "OAIAnalytics_GenericLogFlow_200_response_logs_inner_device.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAnalytics_GenericLogFlow_200_response_logs_inner_device;

class OAILogContainer_logs_inner : public OAIObject {
public:
    OAILogContainer_logs_inner();
    OAILogContainer_logs_inner(QString json);
    ~OAILogContainer_logs_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAnalytics_GenericLogFlow_200_response_logs_inner_device getDevice() const;
    void setDevice(const OAIAnalytics_GenericLogFlow_200_response_logs_inner_device &device);
    bool is_device_Set() const;
    bool is_device_Valid() const;

    QString getInstallId() const;
    void setInstallId(const QString &install_id);
    bool is_install_id_Set() const;
    bool is_install_id_Valid() const;

    QDateTime getTimestamp() const;
    void setTimestamp(const QDateTime &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAnalytics_GenericLogFlow_200_response_logs_inner_device m_device;
    bool m_device_isSet;
    bool m_device_isValid;

    QString m_install_id;
    bool m_install_id_isSet;
    bool m_install_id_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILogContainer_logs_inner)

#endif // OAILogContainer_logs_inner_H
